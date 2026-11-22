#!/usr/bin/env python3
"""Deterministic draft dialogue/recording exports; never calls a TTS provider."""

import argparse
import hashlib
import json
from pathlib import Path
from content_model import LANGUAGES, read_json, validate_project

ROOT = Path(__file__).resolve().parents[1]


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def render_episode(root, entry, scene_id=None):
    source_path = root / "seasons" / "season-01" / entry["path"] / "episode.json"
    episode = read_json(source_path)
    selected = [s for s in episode["scenes"] if scene_id is None or s["id"] == scene_id]
    selected_ids = {s["id"] for s in selected}
    rows = [r for r in episode["dialogue"] if r["scene_id"] in selected_ids]
    partial = (episode["status"] != "draft_for_table_read" or len(episode["scenes"]) != 6 or scene_id is not None)
    header = "PARTIAL SCOPED DRAFT — not a completed episode" if partial else "DRAFT FOR TABLE READ — not approved audio"
    results = {}
    for lang in LANGUAGES:
        script = [f"# {episode['title'][lang]}", "", f"**{header}**", ""]
        for scene in selected:
            script.extend([f"## {scene['id']}: {scene['title']}", ""])
            for line in rows:
                if line["scene_id"] == scene["id"]:
                    script.append(f"- **{line['id']} / {line['speaker']}**: {line['text'][lang]}")
            script.append("")
        results[f"SCRIPT.{lang}.md"] = ("\n".join(script).rstrip() + "\n").encode("utf-8")
        audio_rows = [{
            "line_id": line["id"], "scene_id": line["scene_id"],
            "speaker": line["speaker"], "audio_owner": line["audio_owner"],
            "performance_mode": line["performance_mode"],
            "lip_sync_target": line["lip_sync_target"],
            "text": line["text"][lang], "text_sha256": sha256(line["text"][lang].encode("utf-8")),
            "delivery": line["delivery"], "intent": line["intent"],
            "source_attribution": line["source_attribution"],
            "audio_file": None, "voice_id": None, "audio_approved": False
        } for line in rows]
        results[f"RECORDING.{lang}.jsonl"] = ("\n".join(json.dumps(r, ensure_ascii=False, sort_keys=True) for r in audio_rows) + "\n").encode("utf-8")
    manifest = {
        "schema_version": "1.0-draft-export",
        "episode_id": episode["episode_id"], "scope_scene_id": scene_id,
        "complete_episode": not partial, "source_status": episode["status"],
        "source_path": f"seasons/season-01/{entry['path']}/episode.json",
        "source_sha256": sha256(source_path.read_bytes()),
        "line_ids": [r["id"] for r in rows],
        "generated_files_sha256": {name: sha256(data) for name, data in sorted(results.items())},
        "media_produced": False, "voices_approved": False,
        "warning": "Text exports only; no recordings, TTS requests or animation were generated."
    }
    results["manifest.json"] = json_bytes(manifest)
    return results


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root")
    parser.add_argument("--episode", help="S01E01–S01E06; required for partial-season build")
    parser.add_argument("--scene", help="S01–S06; requires --episode")
    parser.add_argument("--output", type=Path, help="Output directory (default: <root>/out/season-01)")
    parser.add_argument("--check", action="store_true", help="Verify outputs exist and are current; do not write")
    args = parser.parse_args(argv)
    report = validate_project(args.root, args.episode, args.scene)
    if report["status"] not in ("READY", "SCOPED_READY"):
        print(json.dumps(report, ensure_ascii=False, sort_keys=True))
        return 1 if report["status"] == "FAIL" else 2
    season = read_json(args.root / "seasons" / "season-01" / "season.json")
    entries = [e for e in season["episodes"] if args.episode is None or e["episode_id"] == args.episode]
    base = args.output if args.output else args.root / "out" / "season-01"
    changed = 0
    for entry in entries:
        files = render_episode(args.root, entry, args.scene)
        output = base / entry["episode_id"]
        if args.scene is not None:
            output = output / args.scene
        for name, data in files.items():
            destination = output / name
            if args.check:
                if not destination.is_file() or destination.read_bytes() != data:
                    print(f"STALE_OR_MISSING {destination}")
                    changed += 1
            else:
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(data)
                changed += 1
    print(json.dumps({"status": "CHECK_OK" if args.check and not changed else "STALE" if args.check else "BUILT_DRAFT_TEXT_ONLY",
                      "episodes": [e["episode_id"] for e in entries], "output_files": len(entries) * 7,
                      "changed_or_stale": changed, "media_generated": False}, sort_keys=True))
    return 2 if args.check and changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
