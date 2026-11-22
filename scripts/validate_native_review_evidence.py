#!/usr/bin/env python3
"""Read-only S01E01 human-review evidence intake. Never grants approval.

Missing receipts are NOT_REVIEWED; present but malformed evidence is INVALID.
A structurally complete synthetic/real submission remains UNVERIFIED and
cannot set a native, devotional, casting, or media approval flag.
"""
from __future__ import annotations

import argparse
from datetime import date
import hashlib
import json
import math
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path("seasons/season-01/episodes/s01e01-the-lake-at-trikuta/episode.json")
DEFAULT_RECEIPT = Path("reviews/native/S01E01/evidence.json")
ROLES = ("native_te", "native_hi", "native_en", "devotional_source")
LANGUAGES = {"native_te": "te", "native_hi": "hi", "native_en": "en"}
SHOT_RANGE = re.compile(r"\bL(\d{3})(?:[–-]L(\d{3}))?\b")
SHA256 = re.compile(r"[0-9a-f]{64}")
GIT_SHA = re.compile(r"[0-9a-f]{40}")
PLACEHOLDERS = frozenset({"_", "n/a", "na", "none", "tbd", "pending", "unknown",
                           "not reviewed", "not approved"})


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _keys(value, required, where):
    _require(isinstance(value, dict) and set(value) == set(required),
             f"{where}: expected exactly {sorted(required)}")


def _text(value):
    return (isinstance(value, str) and bool(value.strip())
            and value.strip().lower() not in PLACEHOLDERS
            and not set(value.strip()) <= {"_"})


def _date(value):
    if not isinstance(value, str):
        return False
    try:
        checked = date.fromisoformat(value)
        return checked.isoformat() == value and checked <= date.today()
    except ValueError:
        return False


def _number(value, zero_ok=False):
    return (type(value) in (int, float) and math.isfinite(value)
            and (value >= 0 if zero_ok else value > 0))


def git_blob_sha(data: bytes) -> str:
    """Match git hash-object on raw canonical bytes, not a text-string claim."""
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii")
                        + b"\0" + data).hexdigest()


def _source(root):
    raw = (root / SOURCE).read_bytes()
    canonical = json.loads(raw)
    _require(isinstance(canonical, dict) and canonical.get("episode_id") == "S01E01",
             "canonical source is not S01E01")
    scenes, lines = canonical.get("scenes"), canonical.get("dialogue")
    _require(isinstance(scenes, list) and len(scenes) == 6
             and isinstance(lines, list) and len(lines) == 54,
             "canonical S01E01 must have six scenes and 54 dialogue IDs")
    _require(canonical.get("target_runtime_seconds", {}).get("preferred") == 330,
             "canonical episode preferred budget differs from 330 seconds")
    line_by_id, shots, ownership = {}, [], {}
    for line in lines:
        _require(isinstance(line, dict) and isinstance(line.get("id"), str),
                 "canonical dialogue has an invalid line")
        lid = line["id"]
        _require(re.fullmatch(r"S01E01-S0[1-6]-L[0-9]{3}", lid)
                 and lid not in line_by_id, f"duplicate/invalid canonical line: {lid}")
        _require(isinstance(line.get("text"), dict)
                 and all(_text(line["text"].get(x)) for x in LANGUAGES.values()),
                 f"{lid}: missing canonical language text")
        line_by_id[lid] = line
    for i, scene in enumerate(scenes, 1):
        sid = f"S{i:02d}"
        _require(isinstance(scene, dict) and scene.get("id") == sid,
                 f"canonical scene {sid} missing or out of order")
        own_lines = [lid for lid in line_by_id if lid.startswith(f"S01E01-{sid}-")]
        own_shots = scene.get("shots")
        _require(isinstance(own_shots, list) and len(own_shots) == 3,
                 f"{sid}: expected three canonical shots")
        for j, shot in enumerate(own_shots, 1):
            expected_id = f"S01E01-{sid}-SH{j:02d}"
            _require(isinstance(shot, dict) and shot.get("id") == expected_id,
                     f"{sid}: invalid canonical shot {j}")
            match = SHOT_RANGE.search(shot.get("action", ""))
            _require(match is not None,
                     f"{expected_id}: canonical shot has no line range")
            first = int(match.group(1))
            last = int(match.group(2) or match.group(1))
            _require(1 <= first <= last, f"{expected_id}: invalid line range")
            for k in range(first, last + 1):
                lid = f"S01E01-{sid}-L{k:03d}"
                _require(lid in line_by_id and lid not in ownership,
                         f"{expected_id}: missing/repeated line {lid}")
                ownership[lid] = expected_id
            shots.append(expected_id)
        _require(set(own_lines) == set(lid for lid in ownership
                                     if lid.startswith(f"S01E01-{sid}-")),
                 f"{sid}: shot ownership does not cover canonical dialogue")
    _require(len(shots) == 18 and len(ownership) == 54,
             "canonical line/shot ownership is incomplete")
    return git_blob_sha(raw), lines, shots, ownership


def _evidence_file(root, evidence, where):
    _keys(evidence, {"path", "sha256"}, where)
    path, digest = evidence["path"], evidence["sha256"]
    _require(_text(path) and isinstance(digest, str) and SHA256.fullmatch(digest),
             f"{where}: missing evidence path or SHA-256")
    rel = Path(path)
    _require(not rel.is_absolute() and ".." not in rel.parts and "\\" not in path,
             f"{where}: unsafe evidence path")
    _require(not (root / rel).is_symlink(),
             f"{where}: unsafe evidence symlink")
    absolute = (root / rel).resolve()
    _require(absolute.is_relative_to(root.resolve()) and absolute.is_file(),
             f"{where}: evidence file not present inside repository")
    actual = hashlib.sha256(absolute.read_bytes()).hexdigest()
    _require(actual == digest, f"{where}: evidence SHA-256 mismatch")


def _correction(row, where, approved):
    state, note = row["correction_status"], row["correction_note"]
    _require(state in ("none", "proposed", "deferred", "accepted"),
             f"{where}: invalid correction disposition")
    _require(isinstance(note, str), f"{where}: correction_note must be text")
    _require(state == "none" or _text(note),
             f"{where}: missing correction/deferral explanation")
    _require(not approved or state not in ("proposed", "deferred"),
             f"{where}: cannot approve with unresolved proposed/deferred correction")


def _validate_session(root, review, role, source_sha, lines, shots, owner):
    common = {"role", "reviewer_identity", "review_date",
              "verified_source_blob_sha", "decision", "decision_note",
              "evidence", "lines"}
    native = role in LANGUAGES
    expected = common | ({"language", "shots"} if native else set())
    _keys(review, expected, role)
    _require(review["role"] == role, f"{role}: role mismatch")
    if native:
        _require(review["language"] == LANGUAGES[role],
                 f"{role}: language mismatch")
    _require(_text(review["reviewer_identity"]),
             f"{role}: reviewer identity missing")
    _require(_date(review["review_date"]), f"{role}: invalid review date")
    _require(review["verified_source_blob_sha"] == source_sha,
             f"{role}: reviewer-confirmed source Git blob SHA mismatch")
    decision = review["decision"]
    _require(decision in ("approve", "revise", "reject"),
             f"{role}: decision missing or invalid")
    _require(_text(review["decision_note"]),
             f"{role}: missing evidence-backed decision explanation")
    _evidence_file(root, review["evidence"], f"{role}.evidence")
    records = review["lines"]
    _require(isinstance(records, list) and len(records) == len(lines),
             f"{role}: incomplete line evidence")
    line_seconds = {}
    for expected_line, record in zip(lines, records):
        lid = expected_line["id"]
        where = f"{role}/{lid}"
        if native:
            keys = {"line_id", "spoken_text", "speech_seconds",
                    "pronunciation", "meaning", "correction_status",
                    "correction_note"}
        else:
            keys = {"line_id", "source_attribution", "meaning",
                    "correction_status", "correction_note"}
        _keys(record, keys, where)
        _require(record["line_id"] == lid, f"{where}: line ID/order mismatch")
        _require(record["meaning"] in ("pass", "needs_revision"),
                 f"{where}: missing meaning decision")
        if native:
            _require(record["spoken_text"] == expected_line["text"][review["language"]],
                     f"{where}: spoken text differs from canonical source")
            _require(_number(record["speech_seconds"]),
                     f"{where}: missing/nonpositive or nonfinite measured line seconds")
            _require(record["pronunciation"] in ("pass", "needs_revision"),
                     f"{where}: missing pronunciation decision")
            line_seconds[lid] = record["speech_seconds"]
        else:
            _require(record["source_attribution"] == expected_line["source_attribution"],
                     f"{where}: source locator or original disclosure mismatch")
        _correction(record, where, decision == "approve")
        if decision == "approve":
            _require(record["meaning"] == "pass"
                     and (not native or record["pronunciation"] == "pass"),
                     f"{where}: approved review contains unresolved decision")
    if native:
        measured = review["shots"]
        _require(isinstance(measured, list) and len(measured) == len(shots),
                 f"{role}: incomplete per-shot measured durations")
        for shot_id, shot_record in zip(shots, measured):
            _keys(shot_record, {"shot_id", "measured_seconds"},
                  f"{role}/{shot_id}")
            _require(shot_record["shot_id"] == shot_id,
                     f"{role}/{shot_id}: shot ID/order mismatch")
            _require(_number(shot_record["measured_seconds"]),
                     f"{role}/{shot_id}: missing/nonfinite shot duration")
            minimum = sum(value for lid, value in line_seconds.items()
                          if owner[lid] == shot_id)
            _require(shot_record["measured_seconds"] + 0.05 >= minimum,
                     f"{role}/{shot_id}: shot duration shorter than its line timings")


def validate_review_evidence(root=ROOT, evidence_path=None):
    """Purely read the source + receipt; NEVER infer human approval from JSON."""
    root = Path(root)
    try:
        sha, lines, shots, owner = _source(root)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        return {"status": "INVALID", "approved": False, "errors": [str(exc)]}
    explicit = evidence_path is not None
    try:
        requested = Path(evidence_path) if explicit else root / DEFAULT_RECEIPT
        if explicit and not requested.is_absolute():
            requested = root / requested
        resolved = requested.resolve()
        _require(resolved.is_relative_to(root.resolve())
                 and not requested.is_symlink(),
                 "receipt: unsafe path (outside repository or symlink)")
    except (OSError, ValueError, TypeError, AttributeError) as exc:
        return {"status": "INVALID", "approved": False,
                "source_git_blob_sha": sha, "errors": [str(exc)]}
    if not resolved.is_file():
        if explicit:
            return {"status": "INVALID", "approved": False,
                    "source_git_blob_sha": sha,
                    "errors": ["receipt: explicitly specified evidence file is missing"]}
        return {"status": "NOT_REVIEWED", "approved": False,
                "source_git_blob_sha": sha,
                "missing": ["human review receipt absent"],
                "errors": [], "reviewed_roles": []}
    try:
        receipt = json.loads(resolved.read_text(encoding="utf-8"))
        _keys(receipt, {"schema_version", "episode_id", "source_git_blob_sha",
                        "reviews"}, "receipt")
        _require(receipt["schema_version"] == "1.0"
                 and receipt["episode_id"] == "S01E01",
                 "receipt: invalid schema or episode ID")
        _require(receipt["source_git_blob_sha"] == sha,
                 "receipt: canonical Git blob SHA mismatch")
        reviews = receipt["reviews"]
        _require(isinstance(reviews, list) and len(reviews) == len(ROLES),
                 "receipt: exactly four human-review roles required")
        for expected_role, review in zip(ROLES, reviews):
            _validate_session(root, review, expected_role,
                              sha, lines, shots, owner)
        decisions = [review["decision"] for review in reviews]
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        return {"status": "INVALID", "approved": False,
                "source_git_blob_sha": sha, "errors": [str(exc)]}
    return {
        "status": ("EVIDENCE_PRESENT_UNVERIFIED" if all(d == "approve" for d in decisions)
                   else "EVIDENCE_RECORDED_NOT_APPROVED"),
        "approved": False,
        "source_git_blob_sha": sha,
        "reviewed_roles": list(ROLES),
        "errors": [],
        "warning": "Structural receipt validation is NOT human identity authentication, "
                   "native/scripture signoff, voice approval, or media readiness.",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--evidence", type=Path, default=None,
                        help="Existing JSON evidence receipt; never created by this script")
    args = parser.parse_args(argv)
    result = validate_review_evidence(args.root, args.evidence)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    # No status returned by this structural intake can authorize production.
    return 1 if result["status"] == "INVALID" else 2


if __name__ == "__main__":
    raise SystemExit(main())
