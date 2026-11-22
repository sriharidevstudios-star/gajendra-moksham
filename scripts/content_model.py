"""Gajendra Moksham source validation: stdlib-only, no TTS or media calls.

This is a deliberately small adaptation of the Prahlada dialogue-first contract.
A scoped partial scene can validate, but never counts as a complete episode.
"""

from __future__ import annotations

import json
from pathlib import Path
import re

LANGUAGES = ("te", "hi", "en")
EPISODE_IDS = tuple(f"S01E{i:02d}" for i in range(1, 7))
SCENE_IDS = tuple(f"S{i:02d}" for i in range(1, 7))
NON_HUMAN_SPEAKERS = frozenset({"GAJENDRA", "CROCODILE", "GARUDA"})
LINE_ID = re.compile(r"^(S01E0[1-6])-(S0[1-6])-L([0-9]{3})$")
LOCATOR = re.compile(r"^8\.([234])\.([1-9][0-9]*)(?:[-–][1-9][0-9]*)?$")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def has_text(value):
    return isinstance(value, str) and bool(value.strip())


def chapter(locator):
    """Return e.g. '8.2' for an individual single-chapter verse anchor."""
    match = LOCATOR.fullmatch(locator) if isinstance(locator, str) else None
    return f"8.{match.group(1)}" if match else None


def covered_by_anchor(locator, anchors):
    """A line's verse must belong to an explicit scene anchor range."""
    match = LOCATOR.fullmatch(locator) if isinstance(locator, str) else None
    if not match:
        return False
    line_chapter, line_start = match.group(1), int(match.group(2))
    line_end = int(locator.split("-", 1)[1]) if "-" in locator else int(locator.split("–", 1)[1]) if "–" in locator else line_start
    for anchor in anchors:
        m = LOCATOR.fullmatch(anchor) if isinstance(anchor, str) else None
        if not m or m.group(1) != line_chapter:
            continue
        a_start = int(m.group(2))
        a_end = int(anchor.split("-", 1)[1]) if "-" in anchor else int(anchor.split("–", 1)[1]) if "–" in anchor else a_start
        if a_start <= line_start <= line_end <= a_end:
            return True
    return False


def chapters_in_episode(locator):
    if not has_text(locator):
        return set()
    return set(re.findall(r"8\.([234])\.", locator))


def validate_language_text(value, where, errors):
    if not isinstance(value, dict) or set(value) != set(LANGUAGES):
        errors.append(f"{where}: must contain exactly te, hi, en")
    else:
        for lang in LANGUAGES:
            if not has_text(value[lang]):
                errors.append(f"{where}.{lang}: missing spoken text")


def validate_episode(doc, entry, errors, known_characters):
    episode_id = entry["episode_id"]
    where = f"{episode_id}"
    if not isinstance(doc, dict):
        errors.append(f"{where}: episode source must be an object")
        return False

    required = {"schema_version", "season_id", "episode_id", "episode_number", "slug", "title",
                "status", "logline", "target_runtime_seconds", "source", "adaptation",
                "characters", "scenes", "dialogue", "performance_notes", "timing_note"}
    for name in sorted(required - set(doc)):
        errors.append(f"{where}: missing {name}")
    if set(doc) - required:
        errors.append(f"{where}: unexpected root fields {sorted(set(doc) - required)}")
    if doc.get("schema_version") != "1.0-dialogue" or doc.get("season_id") != "S01":
        errors.append(f"{where}: incorrect schema_version or season_id")
    if doc.get("episode_id") != episode_id or doc.get("episode_number") != int(episode_id[-2:]):
        errors.append(f"{where}: episode ID/number disagrees with season index")
    if doc.get("slug") != entry["path"].split("/", 1)[-1].removeprefix(episode_id.lower() + "-"):
        errors.append(f"{where}: slug disagrees with season index")
    validate_language_text(doc.get("title"), f"{where}.title", errors)
    if not has_text(doc.get("logline")):
        errors.append(f"{where}: missing logline")
    timing = doc.get("target_runtime_seconds")
    if not isinstance(timing, dict) or any(type(timing.get(k)) is not int for k in ("min", "preferred", "max")) or not (timing.get("min", 0) <= timing.get("preferred", 0) <= timing.get("max", 0)):
        errors.append(f"{where}: invalid runtime bounds")
    source = doc.get("source")
    expected_chapters = chapters_in_episode(entry.get("source_locator"))
    if not isinstance(source, dict) or not all(has_text(source.get(k)) for k in ("edition", "url", "source_locator", "verification_notes")):
        errors.append(f"{where}: incomplete source attribution")
    else:
        if not source["url"].startswith("https://") or source["source_locator"] != entry.get("source_locator"):
            errors.append(f"{where}: source URL or locator disagrees with registered source")
    adaptation = doc.get("adaptation")
    if not isinstance(adaptation, dict) or not isinstance(adaptation.get("core_preserved"), list) or not adaptation["core_preserved"] or not isinstance(adaptation.get("changes"), list) or not has_text(adaptation.get("fidelity_note")):
        errors.append(f"{where}: adaptation disclosure missing")

    characters = doc.get("characters")
    ids = set()
    if not isinstance(characters, list) or not characters:
        errors.append(f"{where}: characters must be nonempty")
    else:
        for char in characters:
            if not isinstance(char, dict) or not re.fullmatch(r"[A-Z][A-Z_]*", str(char.get("id", ""))):
                errors.append(f"{where}: invalid cast record")
                continue
            cid = char["id"]
            if cid in ids:
                errors.append(f"{where}: duplicate cast ID {cid}")
            ids.add(cid)
            if cid not in known_characters and cid != "NARRATOR":
                errors.append(f"{where}: character {cid} missing from character bible")
            validate_language_text(char.get("name"), f"{where}.{cid}.name", errors)
            if not has_text(char.get("description")) or not has_text(char.get("voice_direction")):
                errors.append(f"{where}: incomplete character {cid}")

    scenes = doc.get("scenes")
    if not isinstance(scenes, list) or not (1 <= len(scenes) <= 6):
        errors.append(f"{where}: scenes must contain 1–6 ordered scenes")
        scenes = []
    present_scenes = []
    total_seconds = 0
    scene_chapters = {}
    scene_anchors = {}
    for index, scene in enumerate(scenes):
        sid = f"S{index + 1:02d}"
        if not isinstance(scene, dict) or scene.get("id") != sid:
            errors.append(f"{where}: scene order must start at S01 with no gaps ({sid})")
            continue
        present_scenes.append(sid)
        duration = scene.get("duration_budget_seconds")
        if type(duration) is not int or duration < 1:
            errors.append(f"{where}/{sid}: invalid duration")
            duration = 0
        total_seconds += duration
        if not all(has_text(scene.get(k)) for k in ("title", "setting", "action")):
            errors.append(f"{where}/{sid}: scene missing title/setting/action")
        if not isinstance(scene.get("nonverbal_beats"), list):
            errors.append(f"{where}/{sid}: nonverbal_beats must be a list")
        anchors = scene.get("source_anchors")
        scene_chapters[sid] = set()
        scene_anchors[sid] = []
        if not isinstance(anchors, list) or not anchors:
            errors.append(f"{where}/{sid}: missing source anchors")
        else:
            for anchor in anchors:
                loc = anchor.get("locator") if isinstance(anchor, dict) else None
                found = chapter(loc)
                if not found or found[-1] not in expected_chapters:
                    errors.append(f"{where}/{sid}: invalid or out-of-episode anchor {loc}")
                else:
                    scene_chapters[sid].add(found)
                    scene_anchors[sid].append(loc)
                if not isinstance(anchor, dict) or not has_text(anchor.get("url")) or not anchor["url"].startswith("https://"):
                    errors.append(f"{where}/{sid}: anchor URL missing")
                elif found and f"/sb/8/{found[-1]}/" not in anchor["url"]:
                    errors.append(f"{where}/{sid}: anchor URL chapter differs from locator")
        shots = scene.get("shots")
        if not isinstance(shots, list) or len(shots) != 3:
            errors.append(f"{where}/{sid}: exactly 3 editorial shots required")
            continue
        shot_seconds = 0
        for j, shot in enumerate(shots):
            expect = f"{episode_id}-{sid}-SH{j + 1:02d}"
            if not isinstance(shot, dict) or shot.get("id") != expect:
                errors.append(f"{where}/{sid}: incorrect shot ID {expect}")
                continue
            budget = shot.get("budget_seconds")
            if type(budget) is not int or budget <= 0:
                errors.append(f"{expect}: invalid shot duration")
            else:
                shot_seconds += budget
            if not all(has_text(shot.get(k)) for k in ("action", "camera", "sound")):
                errors.append(f"{expect}: missing action/camera/sound")
        if shot_seconds != duration:
            errors.append(f"{where}/{sid}: shot seconds {shot_seconds} != scene seconds {duration}")

    status = doc.get("status")
    if status not in ("partial_scene_draft", "draft_for_table_read"):
        errors.append(f"{where}: invalid authoring status")
    if status == "draft_for_table_read" and len(present_scenes) != 6:
        errors.append(f"{where}: full table-read status requires six scenes")
    if len(present_scenes) == 6 and total_seconds != doc.get("target_runtime_seconds", {}).get("preferred"):
        errors.append(f"{where}: full episode scene budgets must sum to preferred runtime")

    lines = doc.get("dialogue")
    if not isinstance(lines, list) or not lines:
        errors.append(f"{where}: dialogue must contain at least one authored line")
        lines = []
    seen = set()
    previous_scene_index = -1
    previous_line_num = {}
    lines_per_scene = {sid: 0 for sid in present_scenes}
    for row in lines:
        line_id = row.get("id") if isinstance(row, dict) else None
        match = LINE_ID.fullmatch(line_id) if isinstance(line_id, str) else None
        if not match or match.group(1) != episode_id:
            errors.append(f"{where}: invalid line ID {line_id}")
            continue
        if line_id in seen:
            errors.append(f"{where}: duplicate line ID {line_id}")
        seen.add(line_id)
        sid = row.get("scene_id")
        if sid != match.group(2) or sid not in lines_per_scene:
            errors.append(f"{line_id}: scene ownership mismatch or missing scene")
            continue
        scene_index = SCENE_IDS.index(sid)
        number = int(match.group(3))
        if scene_index < previous_scene_index or number <= previous_line_num.get(sid, 0):
            errors.append(f"{line_id}: dialogue order or line number is not increasing")
        previous_scene_index = scene_index
        previous_line_num[sid] = number
        lines_per_scene[sid] += 1
        speaker = row.get("speaker")
        mode = row.get("performance_mode")
        target = row.get("lip_sync_target")
        if speaker not in ids:
            errors.append(f"{line_id}: speaker {speaker} missing from cast")
        if row.get("audio_owner") != speaker:
            errors.append(f"{line_id}: audio_owner must equal speaker")
        if mode not in ("spoken", "narration", "offscreen_voiceover", "inner_prayer_voiceover"):
            errors.append(f"{line_id}: invalid performance_mode")
        if speaker == "NARRATOR" and mode not in ("narration", "offscreen_voiceover"):
            errors.append(f"{line_id}: NARRATOR must be voiceover/narration")
        if speaker in NON_HUMAN_SPEAKERS and mode not in ("narration", "offscreen_voiceover", "inner_prayer_voiceover"):
            errors.append(f"{line_id}: nonhuman speaker cannot use spoken lip-sync mode")
        if target is not None and (target != speaker or mode != "spoken" or speaker in NON_HUMAN_SPEAKERS or speaker == "NARRATOR"):
            errors.append(f"{line_id}: unsafe/unowned lip_sync_target")
        if not has_text(row.get("delivery")) or not has_text(row.get("intent")):
            errors.append(f"{line_id}: missing performance intent")
        validate_language_text(row.get("text"), f"{line_id}.text", errors)
        attribution = row.get("source_attribution")
        kind = attribution.get("kind") if isinstance(attribution, dict) else None
        if kind == "scripture_paraphrase":
            locator = attribution.get("locator")
            if chapter(locator) not in scene_chapters[sid] or not covered_by_anchor(locator, scene_anchors[sid]):
                errors.append(f"{line_id}: scripture locator missing/invalid for scene anchor")
        elif kind == "original_dramatization":
            if not has_text(attribution.get("note")) or attribution.get("locator"):
                errors.append(f"{line_id}: original dramatization needs note, not a scripture locator")
        else:
            errors.append(f"{line_id}: missing/invalid source attribution")

    for sid, count in lines_per_scene.items():
        if count == 0:
            errors.append(f"{where}/{sid}: no dialogue or narration line")
    return status == "draft_for_table_read" and len(present_scenes) == 6


def validate_project(root: Path, episode_id=None, scene_id=None, require_complete=False):
    """Return structured errors and honest readiness, without writing files."""
    root = Path(root)
    errors, pending, ready, complete = [], [], [], []
    base = root / "seasons" / "season-01"
    try:
        bible = read_json(root / "assets" / "character_bible.json")
        known_characters = set(bible["characters"])
        if not known_characters:
            errors.append("character bible has no characters")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"character bible unavailable or invalid: {exc}")
        known_characters = set()
    try:
        season = read_json(base / "season.json")
    except (OSError, ValueError) as exc:
        return {"status": "FAIL", "errors": [f"season.json: {exc}"], "pending": [], "ready_episode_ids": [], "complete_episode_ids": []}
    entries = season.get("episodes")
    if season.get("season_id") != "S01" or season.get("language_order") != list(LANGUAGES) or not isinstance(entries, list) or len(entries) != 6:
        errors.append("season.json: must describe six ordered episodes and te/hi/en")
        entries = entries if isinstance(entries, list) else []
    if episode_id is not None and episode_id not in EPISODE_IDS:
        errors.append(f"invalid requested episode ID: {episode_id}")
    if scene_id is not None and (episode_id is None or scene_id not in SCENE_IDS):
        errors.append("--scene requires --episode and a valid S01–S06 scene ID")
    for i, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append("season.json: non-object episode entry")
            continue
        expected = EPISODE_IDS[i] if i < len(EPISODE_IDS) else None
        eid = entry.get("episode_id")
        path = entry.get("path")
        if eid != expected or entry.get("release_order") != i + 1:
            errors.append(f"season.json: bad episode order at position {i + 1}")
            continue
        if not isinstance(path, str) or not re.fullmatch(r"episodes/s01e0[1-6]-[a-z0-9-]+", path) or not path.startswith(f"episodes/{eid.lower()}-"):
            errors.append(f"{eid}: unsafe or malformed source path")
            continue
        if not chapters_in_episode(entry.get("source_locator")):
            errors.append(f"{eid}: no Canto 8 verse source in season index")
        if entry.get("status") not in ("planned_no_episode_source", "partial_scene_draft", "draft_for_table_read"):
            errors.append(f"{eid}: invalid season index source status")
        if episode_id is not None and eid != episode_id:
            continue
        source_path = base / path / "episode.json"
        if not source_path.is_file():
            pending.append(f"{eid}: canonical source missing ({path}/episode.json)")
            continue
        try:
            doc = read_json(source_path)
        except (OSError, ValueError) as exc:
            errors.append(f"{eid}: episode.json parse/read failed: {exc}")
            continue
        if entry["status"] == "planned_no_episode_source":
            errors.append(f"{eid}: index still marks existing source as missing")
        before = len(errors)
        is_complete = validate_episode(doc, entry, errors, known_characters)
        if entry["status"] != doc.get("status"):
            errors.append(f"{eid}: index status disagrees with episode source status")
        if len(errors) == before:
            ready.append(eid)
            if is_complete:
                complete.append(eid)
            else:
                pending.append(f"{eid}: partial episode; not a six-scene table-read draft")
            if scene_id and scene_id not in [s.get("id") for s in doc.get("scenes", []) if isinstance(s, dict)]:
                pending.append(f"{eid}/{scene_id}: scene not authored")
    if errors:
        status = "FAIL"
    elif episode_id is None:
        status = "READY" if len(complete) == 6 and not pending else "NOT_READY"
    else:
        status = "SCOPED_READY" if episode_id in ready and (not scene_id or not any(f"{episode_id}/{scene_id}:" in x for x in pending)) else "NOT_READY"
        if require_complete and episode_id not in complete:
            status = "NOT_READY"
    return {"status": status, "errors": errors, "pending": pending,
            "ready_episode_ids": ready, "complete_episode_ids": complete}
