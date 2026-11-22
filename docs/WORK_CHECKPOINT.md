# Work checkpoint — GM-NATIVE-001

**Date:** 2026-11-22  
**Repository:** `sriharidevstudios-star/gajendra-moksham` · branch `production-artwork` · open draft PR #1 targeting `main`  
**Verified starting head:** `32c9f8ce00273e446a9ef480cf74ef8c88fdf7ce` · tree `2f901e2810f636f8f92952c38680b074c57db72a`  
**Scope:** prepare S01E01/S01's trilingual **human table-read packet only**, next GM-NATIVE-002.

## Delivered within bounds

- Created `docs/S01E01_S01_NATIVE_READ_PACKET.md` with **exactly eight canonical** S01 narration IDs `S01E01-S01-L001–L008`. The packet copies their **eight exact te / eight exact hi / eight exact en spoken strings**, preserves source verse locators (8.2.1 / 8.2.2–3 / 8.2.4) and canonical delivery cues, and does not change any script words.
- Explicit S01 shot-to-line grouping: `S01E01-S01-SH01` L001–L002 **18s**, `SH02` L003–L004 **18s**, `SH03` L005–L008 **24s**; total **60 seconds provisional**. The packet includes future human line/shot duration blanks, blank reviewer/date/source-SHA/correction fields, devotional/source/translation checks, and the original ocean/waterfall/wind ambience planning constraints.
- Provisional pronunciation notes address **Śukadeva/Śuka Maharṣi**, **Trikūṭa**, **Ocean of Milk/Kṣīrasāgara**, and gold/silver/iron peaks. They are **instructions for eventual human verification, not approved pronunciations**.
- All session/line/shot review states **NOT REVIEWED / NOT APPROVED**; no named reviewer, human listening, recorded voice, timing measurement, audio/TTS, image, video, motion or asset/rights acceptance occurred.
- **Unchanged** live `episode.json` (Git blob `885da53d89900aed431b541654971f997054b91d`), all six scenes/54 lines/18 shots/330s preferred E01; root season status `partial_first_episode_draft_five_sources_missing`; `production_tracker.json.canonical_story_written=false`, te/hi/en NARRATOR voice approval false; native-listener checklist, source register, older six coverage maps and all assets. Overall **NOT_READY**.

## Checks and limits

| Gate | Result |
|---|---|
| In-process exact 8 stable S01 IDs, 24 canonical spoken strings, three real shots, source URLs/ownership | **PASS** |
| 18 + 18 + 24 = 60 S01 budget and 330-second episode budget | **PASS** |
| No claimed human review, recording, pronunciation acceptance, missing media approval | **CHECKED / PRESERVED** |
| `python3 -m unittest discover -s tests -v` | **UNRUN** — connected GitHub cannot execute checked-in repository Python |
| `python3 scripts/validate_content.py --episode S01E01 --scene S01` | **UNRUN**, no executed SCOPED_READY claimed |
| `python3 scripts/build_season_dialogue.py --episode S01E01 --scene S01` / `--check` | **UNRUN**, no exports built |
| Whole-season `python3 scripts/validate_content.py` | **UNRUN**, expected NOT_READY due five missing episode sources |
| Guarded non-force commit, remote head, exact three paths and Git blob identities | Verify after push |

### Commands to run in an executable repository

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_content.py --episode S01E01 --scene S01
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S01
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S01 --check
python3 scripts/validate_content.py  # expected NOT_READY / exit 2
```

## Next

**GM-NATIVE-002:** one **S01E01/S02-only** trilingual narrator table-read packet with 11 source IDs, 3 shot budgets and unfilled human signoffs. Exact next instructions in `docs/NEXT_CHAT_PROMPT.md`.
