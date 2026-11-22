# GM-PROD-001 — canonical source and media inventory

Verified snapshot: production-artwork at 3abaf19f7da152b8077c95637070340ccb815b0a (2026-11-22), open draft PR #1. Counts below refer to AUTHORING, not acceptance or completed audio/video.

| Episode | Source status | Scenes | Shots | NARRATOR IDs | te+hi+en strings | Editorial seconds | Canonical blob SHA |
|---|---|---:|---:|---:|---:|---:|---|
| S01E01 | partial_scene_draft | 6 | 18 | 54 | 162 | 330 | `885da53d8990` |
| S01E02 | draft_for_table_read | 6 | 18 | 53 | 159 | 330 | `a198dfd9c0d6` |
| S01E03 | draft_for_table_read | 6 | 18 | 48 | 144 | 330 | `909b0ed0c902` |
| S01E04 | draft_for_table_read | 6 | 18 | 45 | 135 | 300 | `2fff1273636d` |
| S01E05 | draft_for_table_read | 6 | 18 | 48 | 144 | 330 | `3d80684ed639` |
| S01E06 | draft_for_table_read | 6 | 18 | 48 | 144 | 330 | `27f01eac6a70` |
| **Total** | **1 partial + 5 table-read drafts** | **36** | **108** | **296** | **888** | **1950** | — |

All 36 existing `docs/S01E##_S##_COVERAGE_MAP.md` documents are tracked. All 36 scenes have exactly 3 editorial shots, 108 total. Read-only checks on the six actual episode JSONs found: zero duplicate line IDs, zero orphaned scene lines, zero missing te/hi/en fields, zero missing attribution kinds, zero non-NARRATOR audio owners, zero non-null lip-sync targets and zero shot/scene seconds mismatches. Python repository gates and human/scripture reviews have NOT run in this batch.

216 prospective shot-boundary frame positions (108 shots × start/end) are PLANNED, not necessarily 216 distinct files. 888 potential trilingual line-recording units, 18 language-specific episode masters (6×3), and 1950 seconds of editorial timing are ALL PLANNED; measured speech durations remain missing.

**Actual verified character source:** user-owned Library ZIP `approved-character-references-v1.zip` was materialized to an ephemeral analysis workspace, archive SHA-256 `97231bc30058dce3dff97a36e39c973182fce20ae0d7eb0a2c8e29d81deb8323`. Composite (1536×1024 PNG, SHA `389568f7590fe2230892c0de3aaafde88f256f4a50e4e4a54ddd65071e4cab06`) and all nine derived panel PNGs match the registry byte hashes; 9/9 panels are pixel-exact crops of that composite. This is evidence of source reference integrity ONLY, NOT a GitHub PNG mirror or a production runner input. See `assets/artwork/references/GM-PROD-001_BYTE_CHECK.json`.

**Not produced in remote Git tree:** 10 reference PNG binaries, environment masters, approved scene keyframes, speaking portraits, voice audio/TTS, SFX, soundtrack, motion clips, edits or finished videos. The nine cast references are VISUAL-IDENTITY-approved; additional environments, herd turnarounds and scene images do not inherit that approval. `voice_cast.json` contains no selected narrator voice IDs. `production_tracker.json` stays `planning_only`, its per-episode approval flags false and media_files empty.

**Source blockers:** Episode 1 has all six written scenes but remains `partial_scene_draft` until actual native/devotional source review; the other five are written `draft_for_table_read` rather than approved. E01 read packets are prepared but lack signed human decisions and measured timings. Never change this on the strength of structure checks.

**First production work:** `GM-KF-001` for E04/S02/SH01, a two-character (approved Nārāyaṇa ON approved Garuḍa) 16:9 sky-approach hero still pair with direct registry hashes. It avoids unapproved lake/herd references and can prove identity preservation quickly. First start-frame candidate comes before end frame or motion. Next high-use lake pair is `GM-KF-002` for E02/S02/SH02 using approved Gajendra+crocodile but awaiting a separate lake master.

No story/dialogue, season status, approved cast, media tracker or CI test code was changed by this inventory.
