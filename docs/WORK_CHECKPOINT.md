# Work checkpoint — GM-NATIVE-010

**Date:** 2026-11-22 · **Repo:** `sriharidevstudios-star/gajendra-moksham` · `production-artwork` · draft PR #1 to `main`  
**Starting verified HEAD/tree:** `455d497b8466c00dc33c2c4af6aa3531ba63338b` / `5f7401afbea74877cd77d1be1a033e167231b894`  
**Scope:** bounded read-only receipt gate hardening, regression additions and contract clarification. Next **GM-NATIVE-011**.

## Findings and corrections

- **Confirmed issue 1 (explicit receipt path handling):** earlier `--evidence` paths used working-directory relative lookup and, if explicitly absent, returned the indistinguishable `NOT_REVIEWED`. Corrected to root-relative lookup, verified inside-root containment, refusal of final-path symlinks and `INVALID` for explicitly missing evidence. The *default* genuinely absent receipt still reports `NOT_REVIEWED` with `approved=false`.
- **Confirmed issue 2 (evidence aliases):** a final symlink pointing to an otherwise valid supporting evidence file would previously satisfy the hash check. It is now rejected to avoid accepting aliased proof, in addition to existing SHA-256 and resolved-root containment.
- **Confirmed issue 3 (future review dates):** valid ISO text for an event later than `date.today()` was previously accepted. Future-dated sessions now fail the read-date check. Existing synthetic `2026-04-15` remains in the past at this checkpoint.
- **Regression coverage:** added eight entirely synthetic test methods to `tests/test_native_review_evidence.py` (**21 synthetic test methods total**), covering explicit missing/root-relative/external/symlinked receipt paths, supporting evidence symlink, duplicate shot ID, future date, and missing evidence SHA. Existing 13 test methods preserved. No real named reviewer, evidence, receipt, voice file or measured time created.
- **Source/version integrity preserved:** SHA-1 Git blob comparison of canonical S01E01 source; all 54 ordered lines, 18 shot IDs and source attribution checks remain unchanged. Structural all-positive evidence **never grants approval** — still `EVIDENCE_PRESENT_UNVERIFIED`, `approved=false`, exit 2. No season/voice/media promotion or altered production status.
- **Read-only gate:** no file creation/mutation in the validator; metadata and signed evidence remain human-produced external inputs. Changes confined to the authorized validator, synthetic tests, evidence contract and two handoff docs.

## Checks and honest limits

| Gate | Outcome |
|---|---|
| Live GitHub source/branch/PR and baseline blob checks | **CHECKED** |
| In-process exact patch construction / static guard and approval-output checks | **PASS (source/static)**, NOT a Python execution |
| Existing 13 and new 8 regression test methods | **AUTHORED (21 total), UNRUN** |
| `python3 -m unittest discover -s tests -v` | **UNRUN** — no executable checkout of connected GitHub repository; container GitHub DNS unavailable |
| `python3 scripts/validate_native_review_evidence.py` | **UNRUN** — expected default `NOT_REVIEWED`, exit 2, not asserted as executed |
| `python3 scripts/validate_content.py --episode S01E01 --scene S06` | **UNRUN**, do not claim SCOPED_READY execution |
| Whole-season `python3 scripts/validate_content.py` | **UNRUN**, expected NOT_READY with E02–E06 missing |
| Human review, native/source signoff, casting, media | **NOT PERFORMED / NO PROOF** |
| Non-force push, exact five changed files, remote blob/draft PR verification | Verify after commit |

### Commands for a trusted executable repository runner

```bash
python3 -m unittest discover -s tests -p 'test_native_review_evidence.py' -v
python3 -m unittest discover -s tests -v
python3 scripts/validate_native_review_evidence.py  # expect NOT_REVIEWED, exit 2
python3 scripts/validate_content.py --episode S01E01 --scene S06
python3 scripts/validate_content.py  # expect NOT_READY, exit 2
```

## Next bounded handoff

**GM-NATIVE-011:** a narrow GitHub Actions/Python-runner readiness gate for actual automated synthetic test execution (without approving humans, cast, scripts or media). If workflow permissions/execution are unavailable, document exactly which gates remained UNRUN and do not fabricate CI green statuses. Full prompt in `docs/NEXT_CHAT_PROMPT.md`.
