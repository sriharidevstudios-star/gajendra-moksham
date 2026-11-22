# Work checkpoint — GM-COV-003

**Date:** 2026-11-22  
**Repo:** `sriharidevstudios-star/gajendra-moksham` · branch `production-artwork` · open draft PR #1 into `main`  
**Verified starting remote head:** `41ce748a0c90fc72c9d1730db205c40071765e87` (GM-COV-002)  
**Batch:** Only S01E01/S03 picture/audio ownership mapping. **Next:** GM-COV-004 for S01E01/S04.

## Bounded delivery

- Created `docs/S01E01_S03_COVERAGE_MAP.md` for **11 source-authored, trilingual S03 narrator lines**. Each line maps once to the exact canonical shots: `L001–L004 → SH01` (**18s**), `L005–L008 → SH02` (**20s**), `L009–L011 → SH03` (**22s**). Explicit `speaker=audio_owner=NARRATOR`, `narration` mode, `lip_sync_target=null`, source anchor/URL and te/hi/en text ownership (33 future language-line narration requirements, no recordings).
- Recorded **six PLANNED shot-boundary composition requirements**, elephant and herd physical identities, natural family/calf scale, source-grounded thorn/forest breaks, fierce animals departing versus small animals safe by Gajendra's mercy, heat/thirst/bees/lotus-pollen scent, motion/camera/SFX and end at the same S02 freshwater approach bank. Reserved first bathing for S04 and crocodile grip for S06.
- Direct verse pages reviewed: [8.2.20](https://vedabase.io/en/library/sb/8/2/20/), [8.2.21](https://vedabase.io/en/library/sb/8/2/21/), [8.2.22](https://vedabase.io/en/library/sb/8/2/22/), [8.2.23–24](https://vedabase.io/en/library/sb/8/2/23-24/). Source exact meaning not quoted as a published translation.
- Verified tree `4006eeae22f27d6fc6e83c5f64efc582ddee5ae5` has **no tracked media objects**, asset registry `2036bb5675635a81c8713b1b6c15ba38a46547bc` has `assets=[]`, `character_bible.json` `aa387fdeb136ce708ed9b9a905f14cca1ec98972` Gajendra image `approved=false` and null reference, `voice_cast.json` `d4d03e6bf72cdf7cc877e656acb1fbb81c3ce713` has no approved narrator te/hi/en voice, tracker `e7e5a3a524846be8ed60a79d50e60f43dff77364` lists zero media/approved shots, and shot-spec policy is `policy_brief_not_compiler_schema`. All actual images, audio and motion are **MISSING**; visuals/audio in map **PLANNED** only.
- Preserved the complete 54-line canonical episode, all six scenes/18 shots and their budgets, prior S01/S02 coverage docs, human-listener review status, asset/voice/tracker/season metadata and all source IDs/words unchanged. S01E01 stays `partial_scene_draft`, preferred 330 seconds; five other episodes remain uncreated. `production_tracker.json`'s old `canonical_story_written=false` flag remains unchanged and is not proof of accepted script.

## Validation and limitations

| Gate | Result |
|---|---|
| Canonical GitHub scene IDs, anchor/line and shot ownership | **PASS**: 11 unique S03 lines once; 4+4+3 across SH01/SH02/SH03, 18+20+22=60 seconds |
| All te/hi/en `NARRATOR` audio ownership and no lip-sync | **PASS**: 11/11 lines, 33 future track requirements, 0 media |
| Remote asset/voice/shot-spec/Git tree inventory | **CHECKED** as empty/unapproved, including no approved Gajendra reference |
| `python3 -m unittest discover -s tests -v` | **UNRUN** — connector cannot execute repository Python |
| `python3 scripts/validate_content.py --episode S01E01 --scene S03` | **UNRUN** — no claimed executed `SCOPED_READY` |
| `python3 scripts/build_season_dialogue.py --episode S01E01 --scene S03` / `--check` | **UNRUN** — no generated text files or approval |
| `python3 scripts/validate_content.py` | **UNRUN** — expected `NOT_READY` (five missing episode sources) |
| Actual image/TTS/audio/motion | **NONE** generated or approved |
| Guarded non-force commit and remote verification | Verify post-push: head, exactly three paths, Git blob SHA, draft PR |

### Local commands when canonical source is available to Python

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_content.py --episode S01E01 --scene S03
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S03
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S03 --check
python3 scripts/validate_content.py  # expected NOT_READY, exit 2
```

## Next bounded work

**GM-COV-004:** map only S01E01/S04's canonical line-to-three-shot ownership, preserving all media as missing and all previously written story/registries. Use the prompt in `docs/NEXT_CHAT_PROMPT.md`.
