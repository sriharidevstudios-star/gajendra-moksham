# Work checkpoint — GM-NATIVE-006

**Date:** 2026-11-22 · **Repo:** `sriharidevstudios-star/gajendra-moksham` · branch `production-artwork` · draft PR #1  
**Verified starting HEAD/tree:** `603917c3d389fd2432d6d1116ae76e4a4fc42de2` / `db80bf655f210dba651ff6b589650552aaa7f46f`  
**Scope:** prepare S01E01/S06 human trilingual narrator read packet only. **Next:** GM-NATIVE-007.

## Completed

- Created `docs/S01E01_S06_NATIVE_READ_PACKET.md` with all **nine** S06 stable canonical IDs and **27 exact te/hi/en narration strings**, unchanged delivery cues and correct source ownership. **Eight** `scripture_paraphrase` IDs point to SB 8.2.27–28 (L009 continuing the verse-27 grip after verse-28 cries); **one** `original_dramatization` line `S01E01-S06-L006` retains the entire existing original non-graphic water-splash disclosure, **without a fabricated verse locator**.
- Verified line-to-shot allocation: `L001–L002 → S01E01-S06-SH01 (18s)`, `L003–L006 → SH02 (22s)`, `L007–L009 → SH03 (20s)` = **60s provisional**. All lines have `speaker=audio_owner=NARRATOR`, `performance_mode=narration`, `lip_sync_target=null`.
- Included blank te/hi/en reviewer identity, date, independently checked Git SHA, per-line/per-shot measured speech seconds, pronunciation and source notes, devotional review and approvals; **all sessions, lines and shots remain NOT REVIEWED / NOT APPROVED**. Natural water/animal effects remain ungenerated plans. No named narrator, voice ID, timing result, recorded audio, image, video or motion created.
- Child-safe source guidance preserves the sudden **first** crocodile grip only in S06, Gajendra's natural quadruped anatomy, female-elephant nonverbal calls, still-trapped ending, left foreleg as *editorial choice not verse*, and actual failed rear-pulling effort of 8.2.28 plus 8.2.29's thousand-year struggle **deferred in the adaptation** to S01E02.
- Preserved all 54 source lines, six scenes, 18 shot IDs and 330s preferred episode budget, S01–S05 native-read packets and prior coverage maps, unchecked native listener and language audit, season root `partial_first_episode_draft_five_sources_missing`, voice cast, `production_tracker.json.canonical_story_written=false`, and empty asset registry. Whole season **NOT_READY**.

## Validation and limits

| Gate | Status |
|---|---|
| In-process nine canonical lines, 27 verbatim te/hi/en texts, nine exact delivery cues | **PASS** |
| Source ownership 8 scripture + 1 disclosed original, verse URLs and shot groups | **PASS** |
| 18+22+20=60 shot budget; 54/6/18/330 unchanged | **PASS** |
| Human read, source/native approval and audio/art/media | **NOT PERFORMED / MISSING** |
| `python3 -m unittest discover -s tests -v` | **UNRUN**, GitHub connector cannot execute checked-in Python |
| `python3 scripts/validate_content.py --episode S01E01 --scene S06` | **UNRUN**, no executed SCOPED_READY |
| `python3 scripts/build_season_dialogue.py --episode S01E01 --scene S06` and `--check` | **UNRUN**, no exports |
| Whole-season `python3 scripts/validate_content.py` | **UNRUN**, expected NOT_READY |
| Guarded commit/remote paths and blobs/draft PR | Verify post-push |

### Commands for an executable repository

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_content.py --episode S01E01 --scene S06
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S06
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S06 --check
python3 scripts/validate_content.py  # expected NOT_READY / exit 2
```

## Next

**GM-NATIVE-007:** one docs-only cross-scene native-read-packet reconciliation of all six prepared packets, 54 canonical line IDs and three-language text/source versions, without human listening or production actions. Exact prompt in `docs/NEXT_CHAT_PROMPT.md`.
