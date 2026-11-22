"""GM-NATIVE-009: entirely synthetic review-evidence regression tests.

No test fixture is a real person, receipt, approved source or production media.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_native_review_evidence import (  # noqa: E402
    git_blob_sha, validate_review_evidence,
)


class SyntheticReviewEvidenceTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.source_path = (
            self.root / "seasons/season-01/episodes/"
            "s01e01-the-lake-at-trikuta/episode.json"
        )
        self.source_path.parent.mkdir(parents=True)
        self.receipt_path = self.root / "reviews/native/S01E01/evidence.json"
        scenes, dialogue = [], []
        for scene_no in range(1, 7):
            sid = f"S{scene_no:02d}"
            shots = []
            for shot_no in range(1, 4):
                start = (shot_no - 1) * 3 + 1
                end = start + 2
                shots.append({
                    "id": f"S01E01-{sid}-SH{shot_no:02d}",
                    "action": f"Test-only narration L{start:03d}–L{end:03d}",
                    "budget_seconds": 10 if sid == "S05" else 20,
                })
            scenes.append({
                "id": sid,
                "shots": shots,
                "duration_budget_seconds": 30 if sid == "S05" else 60,
            })
            for line_no in range(1, 10):
                lid = f"S01E01-{sid}-L{line_no:03d}"
                attribution = {"kind": "scripture_paraphrase", "locator": "8.2.1"}
                if (sid == "S05" and line_no in (2, 3, 4)) or (
                    sid == "S06" and line_no == 6
                ):
                    attribution = {
                        "kind": "original_dramatization",
                        "note": "Synthetic, not a verse event or real source text.",
                    }
                dialogue.append({
                    "id": lid,
                    "scene_id": sid,
                    "text": {
                        "te": f"TEST-ONLY te {lid}",
                        "hi": f"TEST-ONLY hi {lid}",
                        "en": f"TEST-ONLY en {lid}",
                    },
                    "source_attribution": attribution,
                })
        self.source = {
            "episode_id": "S01E01",
            "status": "partial_scene_draft",
            "target_runtime_seconds": {"min": 330, "preferred": 330, "max": 390},
            "scenes": scenes,
            "dialogue": dialogue,
        }
        self.write_source()
        self.receipt = self.make_receipt()

    def write_source(self):
        raw = (json.dumps(self.source, ensure_ascii=False, indent=2)
               + "\n").encode("utf-8")
        self.source_path.write_bytes(raw)
        self.source_sha = git_blob_sha(raw)

    def evidence_file(self, role):
        path = f"synthetic-only/{role}.txt"
        dest = self.root / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        raw = f"TEST DATA ONLY: {role} evidence, not a human review.\n".encode()
        dest.write_bytes(raw)
        return {"path": path, "sha256": hashlib.sha256(raw).hexdigest()}

    def make_receipt(self):
        reviews = []
        for role, lang in (("native_te", "te"), ("native_hi", "hi"),
                           ("native_en", "en"), ("devotional_source", None)):
            review = {
                "role": role,
                "reviewer_identity": "TEST-ONLY synthetic reviewer",
                "review_date": "2026-04-15",
                "verified_source_blob_sha": self.source_sha,
                "decision": "approve",
                "decision_note": "TEST-ONLY hypothetical reviewed text.",
                "evidence": self.evidence_file(role),
            }
            if lang:
                review["language"] = lang
                review["lines"] = [{
                    "line_id": l["id"],
                    "spoken_text": l["text"][lang],
                    "speech_seconds": 2.0,
                    "pronunciation": "pass",
                    "meaning": "pass",
                    "correction_status": "none",
                    "correction_note": "",
                } for l in self.source["dialogue"]]
                review["shots"] = [{
                    "shot_id": shot["id"],
                    "measured_seconds": 6.5,
                } for scene in self.source["scenes"] for shot in scene["shots"]]
            else:
                review["lines"] = [{
                    "line_id": l["id"],
                    "source_attribution": copy.deepcopy(l["source_attribution"]),
                    "meaning": "pass",
                    "correction_status": "none",
                    "correction_note": "",
                } for l in self.source["dialogue"]]
            reviews.append(review)
        return {
            "schema_version": "1.0",
            "episode_id": "S01E01",
            "source_git_blob_sha": self.source_sha,
            "reviews": reviews,
        }

    def write_receipt(self):
        self.receipt_path.parent.mkdir(parents=True, exist_ok=True)
        self.receipt_path.write_text(
            json.dumps(self.receipt, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    def result(self):
        return validate_review_evidence(self.root, self.receipt_path)

    def assert_invalid(self, phrase):
        self.write_receipt()
        report = self.result()
        self.assertEqual(report["status"], "INVALID", report)
        self.assertIs(report["approved"], False)
        self.assertIn(phrase, " ".join(report["errors"]))

    def test_absent_receipt_is_not_reviewed_and_read_only(self):
        before = sorted(p.relative_to(self.root) for p in self.root.rglob("*"))
        report = validate_review_evidence(self.root)
        self.assertEqual(report["status"], "NOT_REVIEWED")
        self.assertIs(report["approved"], False)
        self.assertEqual(before,
                         sorted(p.relative_to(self.root) for p in self.root.rglob("*")))

    def test_complete_synthetic_receipt_never_auto_approves(self):
        self.write_receipt()
        data_before = self.receipt_path.read_bytes()
        report = self.result()
        self.assertEqual(report["status"], "EVIDENCE_PRESENT_UNVERIFIED", report)
        self.assertIs(report["approved"], False)
        self.assertEqual(len(report["reviewed_roles"]), 4)
        self.assertEqual(data_before, self.receipt_path.read_bytes())

    def test_missing_language_role_rejected(self):
        self.receipt["reviews"].pop()
        self.assert_invalid("exactly four")

    def test_wrong_source_sha_rejected(self):
        self.receipt["source_git_blob_sha"] = "0" * 40
        self.assert_invalid("canonical Git blob SHA mismatch")

    def test_wrong_reviewer_verified_sha_rejected(self):
        self.receipt["reviews"][1]["verified_source_blob_sha"] = "f" * 40
        self.assert_invalid("reviewer-confirmed source")

    def test_canonical_changes_after_receipt_rejected(self):
        self.source["dialogue"][0]["text"]["en"] += " changed after review"
        self.write_source()
        self.assert_invalid("canonical Git blob SHA mismatch")

    def test_missing_line_or_duplicate_line_rejected(self):
        self.receipt["reviews"][0]["lines"].pop()
        self.assert_invalid("incomplete line evidence")
        self.receipt = self.make_receipt()
        self.receipt["reviews"][0]["lines"][1]["line_id"] = (
            self.receipt["reviews"][0]["lines"][0]["line_id"]
        )
        self.assert_invalid("line ID/order mismatch")

    def test_wrong_spoken_text_and_original_note_rejected(self):
        self.receipt["reviews"][0]["lines"][0]["spoken_text"] = "other version"
        self.assert_invalid("spoken text differs")
        self.receipt = self.make_receipt()
        source_session = self.receipt["reviews"][3]
        source_session["lines"][37]["source_attribution"]["note"] = "wrong"
        self.assert_invalid("source locator or original disclosure mismatch")

    def test_missing_or_invalid_timing_rejected(self):
        self.receipt["reviews"][0]["lines"][0]["speech_seconds"] = None
        self.assert_invalid("measured line seconds")
        self.receipt = self.make_receipt()
        self.receipt["reviews"][1]["shots"].pop()
        self.assert_invalid("incomplete per-shot")
        self.receipt = self.make_receipt()
        self.receipt["reviews"][2]["shots"][0]["measured_seconds"] = 1.0
        self.assert_invalid("shot duration shorter")
        self.receipt = self.make_receipt()
        self.receipt["reviews"][2]["lines"][0]["speech_seconds"] = float("nan")
        self.assert_invalid("nonpositive or nonfinite")

    def test_fake_evidence_path_and_bad_hash_rejected(self):
        self.receipt["reviews"][0]["evidence"]["path"] = "no-such-file.txt"
        self.assert_invalid("evidence file not present")
        self.receipt = self.make_receipt()
        self.receipt["reviews"][1]["evidence"]["sha256"] = "0" * 64
        self.assert_invalid("evidence SHA-256 mismatch")
        self.receipt = self.make_receipt()
        self.receipt["reviews"][1]["evidence"]["path"] = "../outside.txt"
        self.assert_invalid("unsafe evidence path")

    def test_missing_identity_and_invalid_date_rejected(self):
        self.receipt["reviews"][0]["reviewer_identity"] = "__________"
        self.assert_invalid("reviewer identity missing")
        self.receipt = self.make_receipt()
        self.receipt["reviews"][1]["review_date"] = "2026-02-31"
        self.assert_invalid("invalid review date")

    def test_unresolved_correction_cannot_be_approved(self):
        entry = self.receipt["reviews"][0]["lines"][0]
        entry["correction_status"] = "deferred"
        entry["correction_note"] = "Needs a later oral review."
        self.assert_invalid("cannot approve with unresolved")
        self.receipt["reviews"][0]["decision"] = "revise"
        self.write_receipt()
        result = self.result()
        self.assertEqual(result["status"], "EVIDENCE_RECORDED_NOT_APPROVED")
        self.assertIs(result["approved"], False)

    def test_claimed_approval_override_field_rejected(self):
        self.receipt["reviews"][0]["approved"] = True
        self.assert_invalid("expected exactly")


if __name__ == "__main__":
    unittest.main()
