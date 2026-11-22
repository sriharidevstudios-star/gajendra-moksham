"""GM-RET-001: synthetic six-scene timing regression tests (no story/media fixtures).

These tests exercise the real stdlib content validator and draft builder.
No synthetic dialogue here is a canonical scripture script.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from content_model import validate_project  # noqa: E402
from build_season_dialogue import main as build_main  # noqa: E402

FIXTURE_PATH = ROOT / "tests" / "fixtures" / "S01E01_partial.fixture.json"
CANONICAL_PATH = ROOT / "seasons" / "season-01" / "episodes" / "s01e01-the-lake-at-trikuta" / "episode.json"


class SixSceneBudgetTests(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.root = Path(self.workspace.name)
        self.base = self.root / "seasons" / "season-01"
        self.base.mkdir(parents=True)
        assets = self.root / "assets"
        assets.mkdir()
        (assets / "character_bible.json").write_text(
            json.dumps({"characters": {"GAJENDRA": {}, "CROCODILE": {}}}),
            encoding="utf-8",
        )
        self.target_path = self.base / "episodes" / "s01e01-the-lake-at-trikuta" / "episode.json"
        self.episode = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        self.episode["scenes"] = []
        self.episode["dialogue"] = []
        original = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        for idx in range(1, 7):
            scene = copy.deepcopy(original["scenes"][0])
            sid = f"S{idx:02d}"
            scene["id"] = sid
            # S05 is the source-honest short bridge; every other scene is 60s.
            shot_seconds = 10 if idx == 5 else 20
            scene["duration_budget_seconds"] = 3 * shot_seconds
            for shot_idx, shot in enumerate(scene["shots"], start=1):
                shot["id"] = f"S01E01-{sid}-SH{shot_idx:02d}"
                shot["budget_seconds"] = shot_seconds
            self.episode["scenes"].append(scene)
            for sample in original["dialogue"]:
                row = copy.deepcopy(sample)
                row["scene_id"] = sid
                row["id"] = f"S01E01-{sid}-{sample['id'].rsplit('-', 1)[-1]}"
                self.episode["dialogue"].append(row)
        self.episode["status"] = "partial_scene_draft"
        self.episode["target_runtime_seconds"]["preferred"] = 330
        self.season = {
            "season_id": "S01",
            "language_order": ["te", "hi", "en"],
            "target_runtime_seconds": {"min": 330, "preferred": 360, "max": 390},
            "episodes": [
                {
                    "episode_id": f"S01E{i:02d}",
                    "release_order": i,
                    "path": "episodes/s01e01-the-lake-at-trikuta" if i == 1
                            else f"episodes/s01e{i:02d}-synthetic-{i:02d}",
                    "status": "partial_scene_draft" if i == 1 else "planned_no_episode_source",
                    "source_locator": "SB 8.2.1–28" if i in (1, 2)
                                      else "SB 8.3.1–29" if i in (3, 4)
                                      else "SB 8.4.1–26",
                }
                for i in range(1, 7)
            ],
        }
        self.persist()

    def persist(self):
        self.target_path.parent.mkdir(parents=True, exist_ok=True)
        self.target_path.write_text(
            json.dumps(self.episode, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        (self.base / "season.json").write_text(
            json.dumps(self.season, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def scoped(self):
        return validate_project(self.root, "S01E01", "S06")

    def test_six_scene_partial_330_scoped_ready_without_approval(self):
        result = self.scoped()
        self.assertEqual(result["status"], "SCOPED_READY", result)
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["complete_episode_ids"], [])
        self.assertEqual(result["ready_episode_ids"], ["S01E01"])
        self.assertEqual(validate_project(self.root)["status"], "NOT_READY")
        self.assertEqual(validate_project(self.root, "S01E01", "S06", True)["status"], "NOT_READY")
        self.assertEqual(sum(s["duration_budget_seconds"] for s in self.episode["scenes"]), 330)

    def test_season_preference_360_may_differ_from_episode_preference_330(self):
        self.assertEqual(self.season["target_runtime_seconds"]["preferred"], 360)
        self.assertEqual(self.episode["target_runtime_seconds"]["preferred"], 330)
        self.assertEqual(self.scoped()["status"], "SCOPED_READY")

    def test_wrong_preferred_360_with_330_scene_budget_still_fails(self):
        self.episode["target_runtime_seconds"]["preferred"] = 360
        self.persist()
        report = self.scoped()
        self.assertEqual(report["status"], "FAIL", report)
        self.assertIn("full episode scene budgets must sum to preferred runtime", " ".join(report["errors"]))

    def test_incorrect_shot_sum_still_fails(self):
        self.episode["scenes"][4]["shots"][0]["budget_seconds"] += 1
        self.persist()
        report = self.scoped()
        self.assertEqual(report["status"], "FAIL", report)
        self.assertIn("shot seconds", " ".join(report["errors"]))

    def test_preferred_below_minimum_still_fails(self):
        self.episode["target_runtime_seconds"]["preferred"] = 300
        self.persist()
        report = self.scoped()
        self.assertEqual(report["status"], "FAIL", report)
        self.assertIn("invalid runtime bounds", " ".join(report["errors"]))

    def test_full_table_read_status_is_not_an_approval_or_complete_season(self):
        self.episode["status"] = "draft_for_table_read"
        self.season["episodes"][0]["status"] = "draft_for_table_read"
        self.persist()
        scoped = self.scoped()
        self.assertEqual(scoped["status"], "SCOPED_READY", scoped)
        self.assertEqual(scoped["complete_episode_ids"], ["S01E01"])
        self.assertEqual(validate_project(self.root)["status"], "NOT_READY")

    def test_partial_330_text_only_builder_and_check(self):
        out = self.root / "generated-test-only"
        args = [
            "--root", str(self.root), "--episode", "S01E01",
            "--scene", "S06", "--output", str(out),
        ]
        self.assertEqual(build_main(args), 0)
        generated = out / "S01E01" / "S06"
        self.assertEqual(len(list(generated.iterdir())), 7)
        manifest = json.loads((generated / "manifest.json").read_text(encoding="utf-8"))
        self.assertFalse(manifest["complete_episode"])
        self.assertFalse(manifest["media_produced"])
        self.assertFalse(manifest["voices_approved"])
        self.assertEqual(len(manifest["line_ids"]), 3)
        self.assertEqual(build_main(args + ["--check"]), 0)

    def test_real_canonical_episode_330_remains_scoped_only(self):
        canonical = json.loads(CANONICAL_PATH.read_text(encoding="utf-8"))
        self.assertEqual(canonical["status"], "partial_scene_draft")
        self.assertEqual(canonical["target_runtime_seconds"]["preferred"], 330)
        self.assertEqual(len(canonical["scenes"]), 6)
        self.assertEqual(len(canonical["dialogue"]), 54)
        self.assertEqual(
            sum(s["duration_budget_seconds"] for s in canonical["scenes"]), 330
        )
        self.assertEqual(
            validate_project(ROOT, "S01E01", "S06")["status"], "SCOPED_READY"
        )
        self.assertEqual(validate_project(ROOT)["status"], "NOT_READY")


if __name__ == "__main__":
    unittest.main()
