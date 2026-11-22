"""Synthetic, never-canonical regression fixtures for GM-ARCH-001."""

import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from content_model import validate_project  # noqa: E402
from build_season_dialogue import main as build_main  # noqa: E402

FIXTURE = ROOT / "tests" / "fixtures" / "S01E01_partial.fixture.json"


def sample_season():
    """Tests only. Every absent episode remains explicitly planned."""
    episodes = []
    for i in range(1, 7):
        eid = f"S01E{i:02d}"
        slug = "the-lake-at-trikuta" if i == 1 else f"test-only-episode-{i:02d}"
        episodes.append({
            "episode_id": eid, "release_order": i,
            "path": f"episodes/{eid.lower()}-{slug}",
            "status": "planned_no_episode_source",
            "source_locator": "SB 8.2.1–28" if i <= 2 else "SB 8.3.1–29" if i <= 4 else "SB 8.4.1–26"
        })
    return {"season_id": "S01", "language_order": ["te", "hi", "en"], "episodes": episodes}


class SourceContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.base = self.root / "seasons" / "season-01"
        self.base.mkdir(parents=True)
        assets = self.root / "assets"
        assets.mkdir()
        (assets / "character_bible.json").write_text(json.dumps({"characters": {"GAJENDRA": {}, "CROCODILE": {}, "GARUDA": {}, "NARAYANA": {}}}), encoding="utf-8")
        self.season = sample_season()
        self._write_season()
        self.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def _write_season(self):
        (self.base / "season.json").write_text(json.dumps(self.season, ensure_ascii=False), encoding="utf-8")

    def write_episode(self, fixture=None):
        self.season["episodes"][0]["status"] = "partial_scene_draft"
        self._write_season()
        dest = self.base / self.season["episodes"][0]["path"] / "episode.json"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(json.dumps(fixture if fixture is not None else self.fixture, ensure_ascii=False), encoding="utf-8")

    def report(self, episode="S01E01", scene="S01"):
        return validate_project(self.root, episode, scene)

    def assert_bad(self, expected):
        report = self.report()
        self.assertEqual(report["status"], "FAIL", report)
        self.assertIn(expected, " | ".join(report["errors"]))

    def test_current_planning_only_is_not_ready(self):
        report = validate_project(self.root)
        self.assertEqual(report["status"], "NOT_READY")
        self.assertEqual(len(report["pending"]), 6)
        self.assertEqual(report["ready_episode_ids"], [])

    def test_partial_scene_ready_but_season_not_ready(self):
        self.write_episode()
        self.assertEqual(self.report()["status"], "SCOPED_READY")
        self.assertEqual(validate_project(self.root)["status"], "NOT_READY")
        self.assertEqual(validate_project(self.root, "S01E01", "S01", True)["status"], "NOT_READY")

    def test_missing_requested_scene_is_not_ready(self):
        self.write_episode()
        self.assertEqual(validate_project(self.root, "S01E01", "S02")["status"], "NOT_READY")

    def test_out_of_range_episode_id_rejected(self):
        self.assertEqual(validate_project(self.root, "S01E07")["status"], "FAIL")

    def test_duplicate_line_id_rejected(self):
        self.fixture["dialogue"][1]["id"] = self.fixture["dialogue"][0]["id"]
        self.write_episode()
        self.assert_bad("duplicate line ID")

    def test_missing_language_rejected(self):
        del self.fixture["dialogue"][0]["text"]["hi"]
        self.write_episode()
        self.assert_bad("exactly te, hi, en")

    def test_scene_ownership_rejected(self):
        self.fixture["dialogue"][1]["scene_id"] = "S02"
        self.write_episode()
        self.assert_bad("scene ownership mismatch")

    def test_animal_spoken_lip_sync_rejected(self):
        row = self.fixture["dialogue"][1]
        row["performance_mode"] = "spoken"
        row["lip_sync_target"] = "GAJENDRA"
        self.write_episode()
        self.assert_bad("nonhuman speaker cannot use spoken lip-sync")

    def test_animal_voiceover_is_not_lipsynced(self):
        self.write_episode()
        self.assertEqual(self.report()["status"], "SCOPED_READY")
        row = self.fixture["dialogue"][1]
        self.assertEqual(row["performance_mode"], "inner_prayer_voiceover")
        self.assertIsNone(row["lip_sync_target"])

    def test_audio_owner_mismatch_rejected(self):
        self.fixture["dialogue"][1]["audio_owner"] = "NARRATOR"
        self.write_episode()
        self.assert_bad("audio_owner must equal speaker")

    def test_character_must_be_registered_in_bible(self):
        self.fixture["characters"][1]["id"] = "UNKNOWN_ANIMAL"
        self.fixture["dialogue"][1]["speaker"] = "UNKNOWN_ANIMAL"
        self.fixture["dialogue"][1]["audio_owner"] = "UNKNOWN_ANIMAL"
        self.write_episode()
        self.assert_bad("missing from character bible")

    def test_verse_must_fit_scene_anchor_range(self):
        self.fixture["dialogue"][2]["source_attribution"]["locator"] = "8.2.5"
        self.write_episode()
        self.assert_bad("scripture locator missing")

    def test_anchor_chapter_must_match_url(self):
        self.fixture["scenes"][0]["source_anchors"][0]["url"] = "https://vedabase.io/en/library/sb/8/3/"
        self.write_episode()
        self.assert_bad("anchor URL chapter differs")

    def test_unregistered_speaker_rejected(self):
        self.fixture["dialogue"][1]["speaker"] = "MADE_UP"
        self.fixture["dialogue"][1]["audio_owner"] = "MADE_UP"
        self.write_episode()
        self.assert_bad("missing from cast")

    def test_scripture_citation_required(self):
        del self.fixture["dialogue"][2]["source_attribution"]["locator"]
        self.write_episode()
        self.assert_bad("scripture locator missing")

    def test_unanchored_chapter_rejected(self):
        self.fixture["dialogue"][2]["source_attribution"]["locator"] = "8.3.1"
        self.write_episode()
        self.assert_bad("scripture locator missing")

    def test_original_line_requires_note(self):
        del self.fixture["dialogue"][0]["source_attribution"]["note"]
        self.write_episode()
        self.assert_bad("original dramatization needs note")

    def test_unregistered_source_chapter_rejected(self):
        self.fixture["scenes"][0]["source_anchors"][0]["locator"] = "8.3.1"
        self.write_episode()
        self.assert_bad("invalid or out-of-episode anchor")

    def test_bad_shot_timing_rejected(self):
        self.fixture["scenes"][0]["shots"][0]["budget_seconds"] = 5
        self.write_episode()
        self.assert_bad("shot seconds")

    def test_false_full_status_rejected(self):
        self.fixture["status"] = "draft_for_table_read"
        self.write_episode()
        self.assert_bad("requires six scenes")

    def test_index_cannot_claim_source_missing_if_present(self):
        self.write_episode()
        self.season["episodes"][0]["status"] = "planned_no_episode_source"
        self._write_season()
        self.assert_bad("index still marks existing source as missing")

    def test_builder_refuses_unwritten_full_season(self):
        output = self.root / "out"
        self.assertEqual(build_main(["--root", str(self.root), "--output", str(output)]), 2)
        self.assertFalse(output.exists())

    def test_deterministic_build_and_stale_detection(self):
        self.write_episode()
        output = self.root / "out"
        args = ["--root", str(self.root), "--episode", "S01E01", "--scene", "S01", "--output", str(output)]
        self.assertEqual(build_main(args), 0)
        path = output / "S01E01" / "S01"
        files = sorted(path.iterdir())
        self.assertEqual(len(files), 7)
        hashes = {f.name: hashlib.sha256(f.read_bytes()).hexdigest() for f in files}
        manifest = json.loads((path / "manifest.json").read_text(encoding="utf-8"))
        self.assertFalse(manifest["complete_episode"])
        self.assertFalse(manifest["media_produced"])
        self.assertIsNone(json.loads((path / "RECORDING.te.jsonl").read_text(encoding="utf-8").splitlines()[1])["audio_file"])
        self.assertEqual(build_main(args + ["--check"]), 0)
        self.assertEqual(build_main(args), 0)
        self.assertEqual(hashes, {f.name: hashlib.sha256(f.read_bytes()).hexdigest() for f in files})
        (path / "SCRIPT.en.md").write_text("stale", encoding="utf-8")
        self.assertEqual(build_main(args + ["--check"]), 2)

    def test_json_schema_matches_six_episode_contract(self):
        schema = json.loads((ROOT / "schemas" / "episode.schema.json").read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["episode_id"]["pattern"], "^S01E0[1-6]$")
        self.assertEqual(schema["properties"]["dialogue"]["items"]["required"].count("audio_owner"), 1)
        self.assertEqual(schema["properties"]["scenes"]["minItems"], 1)


if __name__ == "__main__":
    unittest.main()
