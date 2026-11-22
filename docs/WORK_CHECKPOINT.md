# Work checkpoint — GM-NATIVE-009

**Date:** 2026-11-22 · **Repository:** `sriharidevstudios-star/gajendra-moksham` · branch `production-artwork` · draft PR #1 to `main`  
**Verified starting HEAD/tree:** `ca5544b4414ecdf628d0959e6752949c0d161a3e` / `ea0cfbc5ca423a2737a7d5f2a2c3d60d5bdd43bc`  
**Task:** new **read-only** human-review evidence validator, focused synthetic regression tests and explicit evidence contract. **Next:** GM-NATIVE-010.

## Bounded work

- Added `scripts/validate_native_review_evidence.py`: stdlib-only command `--root` / `--evidence`; reads the actual S01E01 canonical bytes and computes **Git blob SHA**; missing default future receipt returns **`NOT_REVIEWED`, `approved=false`**, without creating folders or files. Present but malformed, stale or missing receipts are `INVALID`. Even hypothetical structurally complete positive evidence returns `EVIDENCE_PRESENT_UNVERIFIED`, **never `approved=true`** or any production-readiness flag.
- Evidence contract requires **four distinct** future roles (native te, hi, en, qualified devotional/source), non-placeholder reviewer identity, real ISO date, own source SHA confirmation, explicit decision/notes and a **pre-existing** evidence-file path plus verified SHA-256 under root. Native sessions must include all 54 source-exact text/ID and real positive line durations, 18 shot durations, pronunciation and meaning decisions/correction dispositions; source review must include exact 54 canonical attribution records and the four original disclosure notes. Rejects unresolved revision assertions within claimed approved sessions.
- Added `tests/test_native_review_evidence.py` with **synthetic-only temporary data** for missing/valid-but-unverified receipts, wrong SHA, changed canonical, missing/duplicate line, wrong spoken text/original disclosure, invalid/missing timings, missing/tampered/traversal evidence refs, missing identity/date, pending correction under asserted approval and illicit approval override field. No production receipt or person was invented.
- Added `docs/NATIVE_REVIEW_EVIDENCE_CONTRACT.md` documenting file/line/shot/specialist evidence shape, read-only semantics and why validation cannot authenticate a human or automatically advance narrator/voice/media/season gates.
- Verified live tree `ea0cfbc5ca423a2737a7d5f2a2c3d60d5bdd43bc` at starting HEAD has **47 tracked blobs, no review receipts or tracked media**; source blob `885da53d89900aed431b541654971f997054b91d`, E01 `partial_scene_draft` (54 lines/6 scenes/18 shots/330s), E02–E06 absent, native listener NOT APPROVED, te/hi/en NARRATOR candidate/audio null and `approved=false`, tracker `canonical_story_written=false` and approval fields false, asset registry empty. All these source/production files **UNCHANGED**.

## Validation and limits

| Gate | Result |
|---|---|
| In-process read-only contract/type/edge-case review and exact allowed-file scope | **CHECKED** (not Python execution) |
| Expected no-receipt status `NOT_REVIEWED` / approval false | **DESIGNED AND TESTED SYNTHETICALLY IN CODE; UNRUN** in Python |
| `python3 -m unittest discover -s tests -v` | **UNRUN** — GitHub connector cannot execute checked-in repository Python |
| `python3 scripts/validate_native_review_evidence.py` | **UNRUN** — expected NOT_REVIEWED/exit 2 from absent receipt |
| `python3 scripts/validate_content.py --episode S01E01 --scene S06` | **UNRUN**, no executed SCOPED_READY |
| Whole-season `python3 scripts/validate_content.py` | **UNRUN**, expected NOT_READY |
| Reviewer identity/signoff, actual durations, voice or media approval | **NOT PERFORMED / ABSENT** |
| Guarded non-force commit, remote exact changed paths/blobs/PR | Verify after push |

### Commands for an executable checkout

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_native_review_evidence.py  # expected NOT_REVIEWED, exit 2
python3 scripts/validate_content.py --episode S01E01 --scene S06
python3 scripts/validate_content.py  # expected NOT_READY, exit 2
```

## Next

**GM-NATIVE-010** — bounded *read-only validator hardening and explicit interface audit* of GM-NATIVE-009 (e.g. positive synthetic edge cases, date/source checks, receipt-path security), without introducing or falsely approving human evidence. Exact prompt in `docs/NEXT_CHAT_PROMPT.md`.
