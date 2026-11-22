# Work checkpoint — GM-NATIVE-004

**Date:** 2026-11-22 · **Repo:** `sriharidevstudios-star/gajendra-moksham` · branch `production-artwork` · draft PR #1  
**Verified starting commit/tree:** `c1ef2fb7b0cc757eb9601e42a53b2d1c3d34b978` / `b2361bdc3aebeeea63a5b65e1fe0cb4b2dd2bf1c`  
**Scope:** S01E01/S04 native human read **packet preparation only**. Next **GM-NATIVE-005**.

## Delivered in bounded scope

- Created `docs/S01E01_S04_NATIVE_READ_PACKET.md` with **11 exact canonical S04 narration IDs, 33 verbatim te/hi/en text strings, unchanged existing `delivery` cues, and the SB 8.2.25–26 locator and URL per line**. All 11 retain `speaker=audio_owner=NARRATOR`, `performance_mode=narration`, `lip_sync_target=null` and `source_attribution.kind=scripture_paraphrase`.
- Verified `L001–L003 → S01E01-S04-SH01 (18s)`, `L004–L007 → SH02 (18s)`, `L008–L011 → SH03 (24s)`; total **60-second provisional budget**, **not measured performance time**.
- Added unfilled per-language reviewer name/date, personally verified source SHA, actual line/shot seconds, pronunciation/correction fields, and verse/devotional decision. All sessions/lines/shots **NOT REVIEWED / NOT APPROVED**.
- Review guidance addresses Gajendra, female elephants/calves, freshwater and **pollen mingled through lake water**, drinking and post-drinking **pouring with trunk** (GM-SPC-002 fixes preserved), gentle water sharing and consistent lake bank/lotus/deeper-water geography. Flagged **L006 order** for timed human read and **L011 family-care/attachment/māyā nuance** for a qualified devotional review; no fabricated second full scripture bath or theological signoff.
- **No human read, timing, reviewer, approval, voice audition, TTS, audio, image, video, motion or SFX produced.** Existing canonical `seasons/season-01/episodes/s01e01-the-lake-at-trikuta/episode.json` blob `885da53d89900aed431b541654971f997054b91d`, 54 narration objects, six scenes/18 shots, 330s E01 preferred, S01–S03 native packets, six coverage maps, language and native-checklist files, voice/asset/production tracker/season metadata all **UNCHANGED**. Root `partial_first_episode_draft_five_sources_missing`, tracker `canonical_story_written=false`, five other episode sources absent; whole season **NOT_READY**.

## Validation and limits

| Gate | Status |
|---|---|
| In-process 11 line IDs, 33 exact te/hi/en strings/delivery/source URLs | **PASS** |
| Three canonical shot groups 3+4+4 and 18+18+24=60 | **PASS** |
| Human devotional/native-listening review and media | **NOT PERFORMED / MISSING** |
| `python3 -m unittest discover -s tests -v` | **UNRUN** (remote GitHub does not execute code) |
| `python3 scripts/validate_content.py --episode S01E01 --scene S04` | **UNRUN** |
| `python3 scripts/build_season_dialogue.py --episode S01E01 --scene S04` and `--check` | **UNRUN**, no exports |
| Whole-season `python3 scripts/validate_content.py` | **UNRUN**, expected NOT_READY |
| Guarded non-force push, exact 3 docs and blob SHAs | Verify after commit |

### Commands for executable repository

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_content.py --episode S01E01 --scene S04
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S04
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S04 --check
python3 scripts/validate_content.py  # expected NOT_READY; not run here
```

## Next

**GM-NATIVE-005:** S01E01/S05 human narrator read packet, **four** lines and exact provenance, no human performance or media generation. See `docs/NEXT_CHAT_PROMPT.md`.
