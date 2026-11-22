# Work checkpoint — GM-RET-001

**Date:** 2026-11-22  
**Repository:** `sriharidevstudios-star/gajendra-moksham` · branch `production-artwork` · draft PR #1 targeting `main`  
**Starting remote head verified:** `3e5d4439b845ca2b95591527de4dcac18a55d393` (GM-STY-006).  
**Batch:** One bounded editorial runtime/validation review; next GM-LANG-001.

## Editorial decision — first episode is 5:30 as a working target

The six authored S01E01 scene budgets are **S01=60, S02=60, S03=60, S04=60, S05=30, S06=60 seconds**, totaling **330 seconds (5:30)**. The reduced S05 is intentional: SB 8.2.26 moves immediately to the crocodile's first grip in 8.2.27, without an independent stalking scene. There is no source justification to invent another 30-second attack montage or repeat the lake play just to reach 360.

- Kept all **six scenes**, **18 shot IDs**, **54 original trilingual line objects**, **three cast IDs**, **all source anchors**, original narration/voiceover ownership, current media registry/approvals, and all story text **unchanged**.
- Changed only S01E01 `target_runtime_seconds.preferred: 360 -> 330`; `min=330`, `max=390` unchanged. The season-level `preferred=360` remains a general target for *other* episodes; episode-specific selection inside season bounds is allowed. **This is still a provisional shot budget, not measured speech or approved editorial runtime.**
- **No runtime validator changes needed**: the preexisting strict six-scene equality rule now compares 330 to S01E01's own 330 preferred. The rule still rejects mismatched preferred values (such as 360 against a 330-second scene sum), incorrect shot totals, and invalid bounds.
- Added `tests/test_runtime_budget.py`: eight synthetic-fixture/real-source regression tests covering the 330-second partial-scene scoped status, season-wide 360 preference, rejecting 330-vs-360 mismatches, bad shot sums/bounds, distinguishing a full table-read draft from complete-season status, deterministic text-only builder freshness, and canonical source scoped status. Existing regression tests were not modified.
- Updated `docs/DATA_MODEL.md` to reflect the authored canonical episode, the episode-specific preference override and the remaining five missing episodes. No story additions, images, TTS, audio, motion, art or publication calls.

## Validation and operational honesty

| Gate | Status |
|---|---|
| Live GitHub source/metadata inspection | **PASS** — previous canonical blob and draft PR #1 verified |
| In-process structural comparison | **PASS** — unchanged scene/shot/dialogue/characters/source objects and 330 second scene budget |
| JSON syntax of updated episode | **PASS** — parsed/serialized and reconfirmed structurally |
| Python tests: `python3 -m unittest discover -s tests -v` | **UNRUN** — external GitHub connector does not execute repo code; direct public raw source download is unavailable in runtime |
| Python canonical scoped check: `python3 scripts/validate_content.py --episode S01E01 --scene S06` | **UNRUN**; with this metadata change and current validator, expected **SCOPED_READY**; must run before claiming gate PASS |
| Python deterministic build/`--check` | **UNRUN**; 7 text-only outputs should be testable locally but none are represented as produced in GitHub |
| Python whole-season check | **UNRUN**; expected **NOT_READY** because S01E01 status remains partial and E02–E06 lack canonical sources |
| Third-party JSON Schema package | **UNRUN** — not installed/executed via GitHub; schema unchanged |
| Media/voices/native-language listening | **MISSING/UNAPPROVED**; not part of this batch |
| Remote non-force commit and three-way file verification | Verify after push via remote head, draft PR, changed files and blob identities |

### Exact commands to run when Python is available

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_content.py --episode S01E01 --scene S06
python3 scripts/validate_content.py --episode S01E01 --scene S06 --require-complete  # expected NOT_READY
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S06
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S06 --check
python3 scripts/validate_content.py  # expected NOT_READY, exit 2
```

## Next bounded task

**GM-LANG-001:** Review first episode's 54 aligned Telugu/Hindi/English narration turns for naturalness, pronunciation, source meaning, and performing feasibility, documenting line-level findings before authoring new scripts. No voices or visual rendering. Follow the exact next-chat prompt in `docs/NEXT_CHAT_PROMPT.md`.
