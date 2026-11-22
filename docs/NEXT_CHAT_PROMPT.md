# COPY INTO NEXT CHAT — GM-STY-001

Work directly through GitHub on **sriharidevstudios-star/gajendra-moksham**, branch **production-artwork**, draft PR **#1** into `main`. Execute exactly this **single canonical scene** batch. No separate local checkout required.

Read the live branch and draft PR, `docs/WORK_CHECKPOINT.md`, `docs/CHAT_WORKFLOW.md`, `docs/SOURCE_REGISTER.md`, `docs/SERIES_BIBLE.md`, `docs/SEASON_01_EPISODE_GUIDE.md`, `docs/DATA_MODEL.md`, `schemas/episode.schema.json`, and existing offline builder/validator. Inspect the actual verses in **Śrīmad Bhāgavatam 8.2.1–4** through the cited source. Do not copy copyrighted published English translations or commentary as screenplay dialogue.

**GM-STY-001 scope:** create `seasons/season-01/episodes/s01e01-the-lake-at-trikuta/episode.json` as **status `partial_scene_draft`**, only scene **`S01`** (Trikūṭa's distinctive three peaks and setting; source-faithful and visually readable). Include source/explicit adaptation notes, scene source anchors with valid URL, original **natural modern Telugu, Hindi and English** aligned by stable `S01E01-S01-L###` IDs, appropriate narrator and speaker profiles, clear `audio_owner`, `performance_mode`, `lip_sync_target: null` for narrator/nonhuman voiceovers, and **exactly three editorial shots** with `S01E01-S01-SH01` … `SH03`, budgets totaling the S01 scene duration (working 60 seconds). Do not fabricate out-of-verse incidents or tack on unrelated morals. Use the source register to ensure continuity with S02 lake/garden action later; no crocodile attack in this opening geography scene unless source planning is deliberately and explicitly revised in a later approved batch.

Change the **one** `season.json` episode entry from `planned_no_episode_source` to `partial_scene_draft` in the same commit. Leave E02–E06 and all other un-authored scenes missing. Do **not** write later scene lines, final full episode, voice IDs, TTS audio requests, images, motion or actual recording files. Do not mutate approved assets or Prahlada repository.

Run actual Python gate commands if possible:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_content.py --episode S01E01 --scene S01
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S01
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S01 --check
python3 scripts/validate_content.py   # EXPECT NOT_READY / exit 2
```

If Python or a gate is inaccessible, record **UNRUN** honestly; do not call it PASS. Regenerated scoped files under ignored `out/` are **text-only preview outputs**, not recorded audio/approved images. Update only `seasons/season-01/episodes/s01e01-the-lake-at-trikuta/episode.json`, the one `season.json` entry and essential checkpoint/handoff docs. Make guarded **non-force** commit/push on `production-artwork` and verify remote commit and files. Stop with concise report and **ONE COPY INTO NEXT CHAT** prompt handing off GM-STY-002 for S01E01/S02, without executing it. No routine confirmation.
