# COPY INTO NEXT CHAT — GM-STY-002

Work directly through GitHub on **sriharidevstudios-star/gajendra-moksham**, branch **production-artwork**, draft PR **#1** into `main`. This document is the operating prompt for exactly **one** bounded source-authoring batch. No local checkout from the user is required.

Read the current remote branch head and draft PR and inspect: `docs/WORK_CHECKPOINT.md`, `docs/CHAT_WORKFLOW.md`, `docs/SOURCE_REGISTER.md`, `docs/SERIES_BIBLE.md`, `docs/SEASON_01_EPISODE_GUIDE.md`, `docs/DATA_MODEL.md`, `schemas/episode.schema.json`, `scripts/content_model.py`, `scripts/build_season_dialogue.py`, `scripts/validate_content.py`, `seasons/season-01/season.json`, and **the existing** `seasons/season-01/episodes/s01e01-the-lake-at-trikuta/episode.json`. Verify the actual source verses in **Śrīmad Bhāgavatam 8.2.5–19**, especially the Ṛtumat garden in **8.2.9–13** and the separate **freshwater lotus lake** in **8.2.14–19**, from reliable source text. Do not lift copyrighted publisher prose into screenplay lines.

**Execute GM-STY-002 only:** extend **S01E01** from its present `partial_scene_draft` `S01` to **exactly two scenes (`S01`, `S02`)** by authoring **only `S02`** as a source-faithful, engaging visual/narration scene for Ṛtumat garden and lake, with natural aligned modern Telugu, Hindi and English, new stable IDs `S01E01-S02-L001`, etc.; do not reuse or renumber any `S01` IDs. Retain complete S01 source/three shot specs unchanged. S02 must include verse-level scene anchors, original-vs-scripture attribution per line, explicit `audio_owner`, safe `performance_mode`, `lip_sync_target: null` for narrator/animal voiceovers, three new S02 editorial shots with budgets summing to ~60 sec, nonverbal beats and clear geography differentiating the **Ocean of Milk** from the **lotus lake**. Do not move later elephant-herd/crocodile attack or any invented character dialogue into this scene; the intended order is S01 mountain geography, S02 garden and lake, S03 elephant arrival. If new named characters are actually scripted, register source-compatible cast, but do not force characters into a landscape description.

Change only the essential existing `episode.json` and checkpoint/handoff docs; keep `season.json` S01E01 `partial_scene_draft`, leave E02–E06 untouched, and preserve assets, voices, schemas and pipeline code. Do not write S03–S06, render any image, produce sound, issue TTS calls, or claim a completed episode.

Run actual gates where possible (with Python stdlib plus existing schema/test tools):

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_content.py --episode S01E01 --scene S02
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S02
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S02 --check
python3 scripts/validate_content.py  # EXPECT NOT_READY / exit 2
```

Keep generated `out/` files local/ignored and unapproved. Mark any unavailable tests **UNRUN**, never PASS. Make a guarded **non-force** commit/push to `production-artwork`, verify exact live remote head/file hashes and draft PR #1, and stop with a concise report and **ONE COPY INTO NEXT CHAT** prompt handing off **GM-STY-003 (S01E01/S03)** without executing it. No routine confirmation.
