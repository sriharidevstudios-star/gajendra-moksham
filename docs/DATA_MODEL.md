# Gajendra Moksham canonical source model — GM-ARCH-001

This is a **small six-episode adaptation** of the Prahlada dialogue-first architecture, not a copy of its episode content or TTS/media pipeline. Runtime is Python 3.10+ standard library only. The schema (`schemas/episode.schema.json`), semantic validator (`scripts/content_model.py`) and draft builder (`scripts/build_season_dialogue.py`) are now implemented. The **canonical S01E01** now has six authored scenes and 54 trilingual narration lines but remains `partial_scene_draft` and not table-read approved. The separate `tests/fixtures/S01E01_partial.fixture.json` contains exclusively synthetic test data, not a production script.

## Authoritative ownership

- `seasons/season-01/season.json` is the existing index: S01E01 is an authored **partial-scene draft**, while S01E02–S01E06 remain `planned_no_episode_source` until their canonical scripts exist.
- `seasons/season-01/episodes/<indexed-slug>/episode.json` becomes authoritative **when authored**. The schema version is `1.0-dialogue`.
- `assets/character_bible.json` determines permissible named character IDs; `NARRATOR` is the off-screen exception.
- `docs/SOURCE_REGISTER.md` determines story anchors (Śrīmad Bhāgavatam 8.2–8.4). Every scene has explicit `source_anchors`, and every spoken line has `source_attribution` with either `scripture_paraphrase` + an anchored locator or `original_dramatization` + a disclosure note.
- `assets/asset_registry.json`, `voice_cast.json`, and `production_tracker.json` remain the truthful **unapproved/empty** state. This batch does not change them.

## Portable authoring contract

A source document has episode metadata (`episode_id: S01E01–S01E06`, episode number, slug, three-language title, source, adaptation and runtime), cast profiles, **one to six ordered scenes** and dialogue turns. Each scene has exactly three budgeted editorial shots with stable IDs. A partially authored `episode.json` uses `status: partial_scene_draft`; **only six present scenes** may be marked `draft_for_table_read`. When all six are present, their shot and scene budgets must sum to **that episode's** `target_runtime_seconds.preferred`. A season-wide 360-second working preference does not prohibit an individual episode choosing 330 seconds within the 330–390-second season range after a source-fidelity review. S01E01's episode-level preferred target is now **330**, consistent with its untouched scene budgets; this is not a measured runtime. The validator deliberately **retains** the exact per-episode equality and the scene/shot structural gates; an invalid 330-vs-360 mismatch still fails.

Stable identifiers: `S01E01`, `S01`, `S01E01-S01-SH01`, `S01E01-S01-L001`. Never renumber an established line after script edits. It is safe for line numbers to have gaps, but they must be unique and ascending within ordered scenes. Each turn contains exact `te`, `hi`, and `en` spoken text and explicit `speaker`, **matching `audio_owner`**, `performance_mode`, `lip_sync_target`, intent, delivery and provenance. **Gajendra, crocodile and Garuḍa cannot use `spoken` human mouth/lip-sync mode.** Gajendra's inner prayer uses `inner_prayer_voiceover` with `lip_sync_target: null`; narrator uses `narration` or `offscreen_voiceover`.

This schema is authoring structure, not a guarantee of fluent translation, correctly interpreted Sanskrit, approved audio, visual continuity or completed episodes. The stdlib semantic validator covers meaningful cross-file constraints that a static JSON Schema alone does not.

## Validator commands and statuses

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_content.py
python3 scripts/validate_content.py --episode S01E01 --scene S01
python3 scripts/validate_content.py --episode S01E01 --scene S01 --require-complete
```

- `READY` (exit 0) means **all six written episodes structurally valid as full six-scene table-read drafts**, **not** editorial approval.
- `SCOPED_READY` (exit 0) means a requested authored episode/scene is internally valid even if the episode/season is partial. It never means the entire season is done.
- `NOT_READY` (exit 2) is an honest absence/incompleteness, not a passing season gate. At this checkpoint the real season returns `NOT_READY`: **S01E01 is a structurally scoped, six-scene partial draft**, while the other five canonical episode sources are missing. `SCOPED_READY` never implies native-language approval, audio readiness or a finished episode.
- `FAIL` (exit 1) reports invalid identifiers, cast/source ownership, structure, or other errors.

If the true source is drafted in GM-STY-001, set its `season.json` index entry status from `planned_no_episode_source` to `partial_scene_draft` in the same commit. Never fake six scenes merely to satisfy a whole-season gate.

## Deterministic draft export

```bash
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S01
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S01 --check
```

Only **scoped valid authored** sources can be built while the season is incomplete. Output defaults to the ignored `out/season-01/S01E01/S01/` folder: three `SCRIPT.*.md`, three `RECORDING.*.jsonl`, plus `manifest.json`. The manifest records source SHA-256, generated file SHA-256, line IDs, scope and an explicit **`media_produced: false`**. Recording rows contain `audio_file: null`, `voice_id: null`, `audio_approved: false` and source ownership. Files are deterministic (no timestamps/provider calls). `--check` verifies exact byte freshness without rewriting. A no-selector full-season build returns exit 2 / `NOT_READY` until the entire source package is written.

**Not yet included:** provider-specific TTS exporter, voice casting/approval, per-frame shot-spec schema/compiler, image jobs, audio files, A2V, lip-sync and final assembly. Those remain later bounded batches; the present builder **never** claims to produce them.
