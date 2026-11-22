# Canonical data model — target contract (not implemented yet)

This project will adapt the **Prahlada** dialogue-first model (`seasons/season-01/episode.json`, `assets/character_bible.json`, per-frame `shot_specs`, season-level cast/asset registry, generated language exports). The exact schema and working builder are **next-batch work**, not available now.

## Currently present

- `seasons/season-01/season.json`: provisional **six** episode index and future path names; each episode has `status: "planned_no_episode_source"`.
- `assets/character_bible.json`: text-only design briefs with `approved_reference: null`; **not approved media**.
- `assets/asset_registry.json`: empty inventory.
- `seasons/season-01/voice_cast.json`: null voice candidates/approvals, no provider or recordings claimed.
- `seasons/season-01/production_tracker.json`: all review gates false.
- `assets/shot_spec_policy.json`: planned animal/anatomy and source constraints, not a validated rendering schema.

## Intended authoritative source

`seasons/season-01/episodes/<slug>/episode.json`: one episode's source anchors; cast; six ordered scenes; shot beats; complete three-language spoken turns; factual/adaptation notes; voice-over vs on-camera spoken status; and provisional timings. The **episode source**, not separate copy-edited scripts, is canonical. Generated scripts, recordings, scene packs and TTS requests must be regenerated deterministically from it.

Identifiers:

- Episode `S01E01` … `S01E06`
- Scene `S01` … `S06` within each episode
- Dialogue `S01E01-S01-L001`, increment only on new lines; **never reassign** an existing ID
- Editorial shot `S01E01-S01-SH01`
- Authored frame `S01E01-S01-SH01-F01`

Keep text separate from TTS style, emotion, pronunciation overrides and visual camera direction. A narrator or Gajendra's prayer voice-over does not imply a face/lip-sync target. Image frames are planned from shot specs with explicit `cast_visible`, `cast_offscreen` and identity anchors, never inferred from a speaker ID alone.

## Planned build/validation semantics

A new stdlib-only offline compiler and validator should support exactly six episodes and `te/hi/en` and refuse to claim a complete season until all six canonical sources exist. During partial drafting, a **scoped** `--episode` or `--scene` validation may pass while the whole-season completeness gate remains **NOT READY**.

Required gates: schema/IDs, line language alignment, speaker ownership, source anchors, sum of scene/shot timing budgets, generated-manifest hash consistency, editable versus generated ownership, per-frame subject count/anatomy, audio provenance and artifact existence checks. Never create fake checksum placeholders. Unit tests must be executed before reporting PASS; if Python is unavailable report UNRUN.

## Migration rule

Copy only generic utilities and data contracts from Prahlada after reviewing them. **Do not** copy Prahlada episode dialogue, prayers, character portraits, hashes, assets, model IDs or production completion counts. `schema_version` and language/TTS provider fields must reflect actual implemented behavior.
