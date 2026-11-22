# Native and devotional review evidence contract — GM-NATIVE-009

**Status:** design/code contract only; NO human-review receipts have been created, and NO language, devotional, casting, audio or media approval has occurred. The canonical S01E01 remains a `partial_scene_draft`; S01E02–S01E06 sources are missing. This document is not a signed form or authorization to produce.

## Scope, default and non-approval boundary

- Read-only stdlib Python entry point: `python3 scripts/validate_native_review_evidence.py`.
- Default future evidence location (currently **ABSENT**): `reviews/native/S01E01/evidence.json`. A user can pass `--root PATH` and `--evidence PATH` for an existing evidence file. The validator **never writes** either path or touches the episode, cast, production tracker or listener checklist.
- Source authority: `seasons/season-01/episodes/s01e01-the-lake-at-trikuta/episode.json`. The validator computes **Git blob SHA-1 from the actual raw file bytes**, rather than trusting a previously printed value or a receipt's claim. Current canonical Git blob: `885da53d89900aed431b541654971f997054b91d`; changing the source invalidates old evidence.
- **No receipt:** `NOT_REVIEWED`, `approved=false`, exit **2**. **Invalid, missing or stale evidence in a submitted receipt:** `INVALID`, `approved=false`, exit **1**. **Complete evidence with revision/rejection:** `EVIDENCE_RECORDED_NOT_APPROVED`, exit **2**. **Structurally complete all-positive evidence:** `EVIDENCE_PRESENT_UNVERIFIED`, exit **2**, **still `approved=false`**. The last state is NOT native or devotional signoff: the script cannot authenticate an alleged human just because a JSON file and hash exist. A separate accountable human decision is required.
- Do **not** interpret `SCOPED_READY`, matching source Git blob, `EVIDENCE_PRESENT_UNVERIFIED` or these tests as `te_script_approved`, `hi_script_approved`, `en_script_approved`, `voices_approved`, or production readiness. Those flags remain false.

## Exact JSON contract for a later human-generated receipt

Top-level object has **exactly** `schema_version`, `episode_id`, `source_git_blob_sha`, and `reviews`. Require `schema_version="1.0"`, `episode_id="S01E01"`, the currently computed canonical Git SHA and four ordered review sessions: `native_te`, `native_hi`, `native_en`, then `devotional_source`. All must be actual documented sessions, not generated placeholder data.

Every review session requires `role`, nonblank `reviewer_identity`, real ISO `review_date`, independently checked `verified_source_blob_sha`, `decision` (`approve`, `revise` or `reject`), nonblank `decision_note`, `evidence` and `lines`. An evidence object has **exactly** `path` and `sha256`; the referenced file must already exist **inside the repository root**, and its raw content must match the supplied SHA-256. A relative path escaping the root is rejected. The validator confirms only that the referenced file is present and hash-consistent; it cannot establish reviewer identity or provenance by cryptography alone.

Each language review adds `language` (`te`, `hi`, `en` as appropriate) and `shots`. Its `lines` list must contain **all 54 canonical line IDs once, in source order**; each row requires exactly `line_id`, canonical `spoken_text`, finite positive `speech_seconds`, `pronunciation` and `meaning` (`pass` or `needs_revision`), `correction_status` (`none`, `proposed`, `deferred`, `accepted`) and text `correction_note`. Explain each non-`none` correction/deferral. A review with `decision=approve` may not have unresolved `needs_revision`, `proposed` or `deferred` items. For each language, `shots` must contain all **18 canonical shot IDs in order**, with finite positive `measured_seconds` at least as long as the sum of its assigned per-line speech measurements (small rounding tolerance 0.05 seconds). These are human measurement assertions, not invented or auto-filled by the validator. The provisional 330-second shot plan is *not* asserted to be a measured reading.

The `devotional_source` review uses the same reviewer/date/source/decision/evidence fields and 54 `lines`, but **no `language` or `shots`**. Each source-review line has exactly `line_id`, `source_attribution` (the full *unchanged* canonical dictionary, including verse locator or the exact original-dramatization note), `meaning` (`pass` or `needs_revision`), `correction_status` and `correction_note`. A claimed positive decision cannot coexist with outstanding source/meaning corrections. The four original cinematographic disclosure notes are never assigned invented verse locators.

**Evidence principle:** a complete JSON receipt that merely *says* a reviewer approved something is not verifiable real-world signoff. Qualified humans must separately authenticate the evidence and version, resolve or explicitly defer the open S03/L009, S04/L006, S04/L011, S05/L001 and S06/L008 questions, and determine approval outside this static validator. No workflow automatically flips production or script flags.

## Running the bounded synthetic tests

```bash
python3 -m unittest tests/test_native_review_evidence.py -v
python3 -m unittest discover -s tests -v
python3 scripts/validate_native_review_evidence.py
python3 scripts/validate_content.py --episode S01E01 --scene S06
python3 scripts/validate_content.py  # expected NOT_READY while other episodes are absent
```

The new unit tests create **synthetic S01E01-shaped temporary fixtures and fake text evidence inside temporary directories only**. The synthetic all-positive fixture must still report `EVIDENCE_PRESENT_UNVERIFIED` with `approved=false`; negative tests reject stale SHA, missing/duplicate line IDs, incomplete measurements, wrong source notes, invalid dates, blank identities, non-existent/mismatched evidence files and inconsistent approvals. These tests are *not* a submitted human review. When the repository is accessible only through GitHub metadata tools, code/tests are authored but execution is **UNRUN**.

**Copyright/media:** this contract needs no voice sample, music, narration recording, scripture publication text, image or rendered motion. Human-review notes and signed evidence, if acquired in a later authorized workflow, require privacy/rights consideration and actual reviewer consent.
