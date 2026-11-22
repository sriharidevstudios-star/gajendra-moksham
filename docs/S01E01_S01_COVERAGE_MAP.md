# S01E01/S01 — picture and audio ownership coverage map (GM-COV-001)

**Prepared:** 2026-11-22  
**Repository:** `sriharidevstudios-star/gajendra-moksham` · branch `production-artwork` · draft PR #1 into `main`  
**Verified source head:** `0e828cbb7b113efe95557ab7d514e75e6a4de8a6`  
**Canonical authority:** `seasons/season-01/episodes/s01e01-the-lake-at-trikuta/episode.json` · Git blob `4cd9ae7db28542fe3fbc2254394aed43f4a75bea`  
**Scene:** `S01E01/S01`, “The three peaks of Trikūṭa” · [Śrīmad-Bhāgavatam 8.2.1–4](https://vedabase.io/en/library/sb/8/2/)  
**Status:** **METADATA-ONLY COVERAGE PLAN** — 8 narrated lines accounted for across 3 existing shots, but **NO created image/audio/motion assets**, no approved references and no approved voice.

## Repository-grounded inventory (do not mistake planning records for delivered assets)

| Verified source or gate | Remote proof / precise current state |
|---|---|
| Canonical `episode.json` | PRESENT source file; six scenes overall, 54 stable trilingual turns, `partial_scene_draft`, 330 seconds episode editorial target |
| Scoped S01 dialogue and shot data | PRESENT as text: eight lines `L001–L008`, three shot descriptions `SH01–SH03` with 18 + 18 + 24 = **60 provisional seconds** |
| `assets/asset_registry.json` | PRESENT **metadata**, `status=empty_no_media_generated`, `assets=[]` (blob `2036bb5675635a81c8713b1b6c15ba38a46547bc`) |
| `assets/shot_spec_policy.json` | PRESENT policy brief, `status=policy_brief_not_compiler_schema` (blob `c682d95dab2690e9b37921c6621b1cc9053d26a2`); there are no validated per-shot image specs/receipts in this repo |
| `seasons/season-01/voice_cast.json` | PRESENT planning metadata, `status=not_auditioned_no_voice_ids_selected`; `NARRATOR` for te/hi/en has null candidate/audio reference and `approved=false` (blob `d4d03e6bf72cdf7cc877e656acb1fbb81c3ce713`) |
| `seasons/season-01/production_tracker.json` | PRESENT planning metadata, `media_files=[]`, `recorded_audio_complete=false`, `visual_references_approved=false`, `shot_specs_validated=false`, `keyframes_verified=false`, `motion_complete=false` (blob `e7e5a3a524846be8ed60a79d50e60f43dff77364`) |
| `docs/S01E01_NATIVE_LISTENER_CHECKLIST.md` | PRESENT unchecked human-review checklist (blob `abcbdfb4811c41c7ec795fcb5c35e1fb48987554`); **no native-listener, devotional or voice approval** |
| Git tree / media check | Remote tree `955d3bfcefcbdbb93975224baaf63e8315450f6e` has no tracked PNG/JPEG/WebP/WAV/MP3/MP4 or other delivered media objects; no S01 image, start frame, end frame, sound file or clip is PRESENT |

**Important:** The production tracker retains an older planning flag `canonical_story_written=false` even though the live `episode.json` now has six authored scenes. This map treats the actual source file as authoritative, does **not** silently change the tracker, and does **not** promote partial authorship to approved/completed production.

## Exact canonical line → editorial shot ownership

The table is an **ownership map**, not a duplicate narration script. For any row, the exact Telugu, Hindi and English spoken strings remain authoritative **only** in `episode.json` at `dialogue[id].text.te`, `.hi` and `.en`. All three versions have the same stable ID, one audio owner **NARRATOR**, `performance_mode=narration`, `lip_sync_target=null`; **24 language-line audio requirements** are *planned*, not 24 files created.

| Canonical narration ID | Shot owner | Verse provenance | te audio owner | hi audio owner | en audio owner | Lip-sync target | Spoken role |
|---|---|---|---|---|---|---|---|
| `S01E01-S01-L001` | `S01E01-S01-SH01` | [`SB 8.2.1`](https://vedabase.io/en/library/sb/8/2/1/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | Offscreen narration |
| `S01E01-S01-L002` | `S01E01-S01-SH01` | [`SB 8.2.1`](https://vedabase.io/en/library/sb/8/2/1/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | Offscreen narration |
| `S01E01-S01-L003` | `S01E01-S01-SH02` | [`SB 8.2.2-3`](https://vedabase.io/en/library/sb/8/2/2-3/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | Offscreen narration |
| `S01E01-S01-L004` | `S01E01-S01-SH02` | [`SB 8.2.2-3`](https://vedabase.io/en/library/sb/8/2/2-3/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | Offscreen narration |
| `S01E01-S01-L005` | `S01E01-S01-SH03` | [`SB 8.2.2-3`](https://vedabase.io/en/library/sb/8/2/2-3/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | Offscreen narration |
| `S01E01-S01-L006` | `S01E01-S01-SH03` | [`SB 8.2.2-3`](https://vedabase.io/en/library/sb/8/2/2-3/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | Offscreen narration |
| `S01E01-S01-L007` | `S01E01-S01-SH03` | [`SB 8.2.2-3`](https://vedabase.io/en/library/sb/8/2/2-3/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | Offscreen narration |
| `S01E01-S01-L008` | `S01E01-S01-SH03` | [`SB 8.2.4`](https://vedabase.io/en/library/sb/8/2/4/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | Offscreen narration |

**Completeness:** 8/8 unique authored S01 IDs assigned once; 0 unassigned, 0 multiply assigned. 8/8 line source locators belong to canonical S01 anchors `8.2.1`, `8.2.2-3` and `8.2.4`. The shot IDs already exist as editorial objects; **there are no approved voice clips, frame IDs or visual asset filenames.** For human listening, track every line in `docs/S01E01_NATIVE_LISTENER_CHECKLIST.md`; its unchecked status is not changed here.

## Per-shot future frame, motion, sound and transition requirements

Everything labeled **PLANNED** below is a specification of missing work, **not** a claim of generated or registered frames. Each shot will require a visual start and end composition before motion work. These are **6 shot-boundary requirements**, *not* six named frame IDs/files or a claim that six distinct images must eventually be rendered.

### S01E01-S01-SH01 — The Ocean of Milk and the reveal of Trikūṭa

- **Canonical lines:** `S01E01-S01-L001`, `S01E01-S01-L002`. **Planned duration:** 18s. **Audio:** NARRATOR `te/hi/en`, `narration`, `lip_sync_target=null`, three language-specific, as-yet-unrecorded performance requirements per line. 23 English whitespace words (not a measured performance).
- **PLANNED start-frame requirement:** A calm, extreme-wide 16:9 view over the mythic Ocean of Milk; distant Trikūṭa as an upcoming central silhouette, no people or animals.
- **PLANNED end-frame requirement:** Recognizable mountain island rising from the Ocean of Milk, centered with clear shoreline scale; set up the three-peak reveal without prematurely showing the Ṛtumat garden.
- **PLANNED motion/visual treatment:** Slow aerial rise or reveal across the ocean surface; do not invent a new character or creature. Planned start-to-end motion only.
- **PLANNED SFX/music:** Low ocean surf and restrained original ambient score underneath NARRATOR; no other voice.
- **PLANNED cut/continuity:** Cut or gentle visual match into the wide frontal three-peak silhouette of SH02; match the central massif and ocean level.
- **Required reference or environment work:** Trikūṭa/milky ocean environment visual brief and two shot-boundary still requirements; no existing accepted still reference.
- **Actual media state:** start image **MISSING**, end image **MISSING**, approved reference **MISSING**, recorded te/hi/en narration **MISSING**, usable SFX/score **MISSING**, motion render **MISSING**, audited shot-spec/receipt **MISSING**. No delivery blob, hash, verification receipt, gallery entry or provider job verified.
### S01E01-S01-SH02 — Three principal peaks: gold, silver, iron

- **Canonical lines:** `S01E01-S01-L003`, `S01E01-S01-L004`. **Planned duration:** 18s. **Audio:** NARRATOR `te/hi/en`, `narration`, `lip_sync_target=null`, three language-specific, as-yet-unrecorded performance requirements per line. 26 English whitespace words (not a measured performance).
- **PLANNED start-frame requirement:** Wide frontal silhouette containing three clear principal peaks together: gold left, silver center, iron right (editorial orientation, not a claim of verse-specified positions).
- **PLANNED end-frame requirement:** All three peaks remain in the same screen positions with readable material identity against the sky; continuity axis holds for the following descent.
- **PLANNED motion/visual treatment:** Gentle lateral drift without swapping peak order or transforming materials; keep three peaks identifiable in one view.
- **PLANNED SFX/music:** Altitude wind and subtle non-diegetic atmosphere below NARRATOR; no characters speaking.
- **PLANNED cut/continuity:** Preserve the gold/silver/iron skyline as the camera moves from the main peaks toward jewel-bearing smaller slopes in SH03.
- **Required reference or environment work:** A reviewed three-peak visual concept and two boundary still requirements; no approved mountain design or image exists.
- **Actual media state:** start image **MISSING**, end image **MISSING**, approved reference **MISSING**, recorded te/hi/en narration **MISSING**, usable SFX/score **MISSING**, motion render **MISSING**, audited shot-spec/receipt **MISSING**. No delivery blob, hash, verification receipt, gallery entry or provider job verified.
### S01E01-S01-SH03 — Gem-rich lesser slopes, forest, waterfalls and emerald foothills

- **Canonical lines:** `S01E01-S01-L005`, `S01E01-S01-L006`, `S01E01-S01-L007`, `S01E01-S01-L008`. **Planned duration:** 24s. **Audio:** NARRATOR `te/hi/en`, `narration`, `lip_sync_target=null`, three language-specific, as-yet-unrecorded performance requirements per line. 46 English whitespace words (not a measured performance).
- **PLANNED start-frame requirement:** Smaller mineral- and jewel-rich peaks, living trees, climbing vines and shrubs below the three main summits; do not confuse real jewels with modern objects.
- **PLANNED end-frame requirement:** Emerald-green foothills where waves from the Ocean of Milk meet the mountain shoreline; reserve freshwater Ṛtumat garden and lotus lake for S02.
- **PLANNED motion/visual treatment:** Controlled downward travel from gem-bearing slopes through trees and waterfalls to sea-washed foothills, with a gentle shore cut; avoid anachronistic geography.
- **PLANNED SFX/music:** Running waterfalls bridge to the ocean waves; allow a brief wordless tail after L008. NARRATOR voice track remains unrecorded.
- **PLANNED cut/continuity:** S01 ends at the Ocean of Milk shoreline. S02 must deliberately transition into a *separate valley and freshwater lake*, not equate the milk-ocean surf with the lotus lake.
- **Required reference or environment work:** Visual design requirements for gems, vines, waterfall and emerald shoreline; two boundary still requirements and possible internal edit points, not created frames.
- **Actual media state:** start image **MISSING**, end image **MISSING**, approved reference **MISSING**, recorded te/hi/en narration **MISSING**, usable SFX/score **MISSING**, motion render **MISSING**, audited shot-spec/receipt **MISSING**. No delivery blob, hash, verification receipt, gallery entry or provider job verified.

## Consistency, provenance and generation gates

1. **Visual continuity:** Ocean of Milk first, Trikūṭa rising with three **gold/silver/iron** peaks, then smaller gem-bearing and forested slopes, waterfalls, emerald foot. SH02 uses **gold on screen left, silver center, iron right** as an *original editorial orientation*, not as words supplied by scripture. S01 has **no** Ṛtumat garden, herd, freshwater lotus lake or crocodile; these belong to later scenes.
2. **Motion interfaces:** A future approved start/end composition is required for each shot. After imagery is authored and reviewed, a later batch may decide whether a start/end frame is reused across edits. There is **no** approved image identity, no numeric frame identifier, no path, no motion clip and no inference that stills can be generated safely without references.
3. **Audio ownership and provenance:** Eight × three-language `NARRATOR` text requirements are canonical; there are **zero** recorded clips/voice IDs and **zero** approved music/SFX files. Environmental waves, wind, waterfalls and ambient score are only editorial sound requests, **not** cast dialogue or lip-sync. Do not send raw XR/TTS or copy commercial recordings.
4. **Timing integrity:** This shot map assigns line-to-shot *groups*, not per-line timestamps or waveform sync. A table read for each language must check scene SH01=18s, SH02=18s, SH03=24s, including natural pauses and sound bridges; no claimed measured fit. The total 60s remains a budget.
5. **Source anchoring:** All lines are `scripture_paraphrase`, grounded in the canonical excerpt [SB 8.2.1](https://vedabase.io/en/library/sb/8/2/1/), [8.2.2–3](https://vedabase.io/en/library/sb/8/2/2-3/), [8.2.4](https://vedabase.io/en/library/sb/8/2/4/). Do not rewrite any `text` or original source attribution in this coverage batch.
6. **Future review gates before production:** native te/hi/en table-read and pronunciation signoff; explicit visual identity reference selection and acceptance; source-aware shot specs and exact frame requirements; new actual stills with SHA/receipt and human review; environment/SFX licensing or original generation; appropriate motion/generation jobs; sound/timing validation; guarded delivery proof. All are **PENDING / MISSING**, not silently marked complete.

## Verification and unchanged sources

- Verified live branch and draft PR #1 at `0e828cbb7b113efe95557ab7d514e75e6a4de8a6`; queried full Git tree, the **empty** asset registry, **unapproved** voice cast, **planning-only** production tracker, shot-spec policy and native-listener checklist.
- In-process checks: **PASS** for 8 canonical S01 IDs each assigned once in ordered L001–L008; **PASS** for 3 existing shot IDs, **18+18+24=60** seconds, all 8 source locators covered, all 8 line speakers/audio owners = NARRATOR, all three nonempty `text.te/hi/en`, all 8 lip-sync targets `null`.
- Python tests/validator/build `python3 -m unittest discover -s tests -v` / `python3 scripts/validate_content.py --episode S01E01 --scene S01` / text-only builder `--scene S01` and `--check`: **UNRUN** in connected GitHub chat context (repository execution unavailable). No tests or generated exports were claimed.
- Canonical episode, season metadata, asset registry, voice cast, production tracker, native-listener checklist, schema and pipeline code are **UNCHANGED**. Overall season **NOT_READY**; S01E01 remains `partial_scene_draft`, with five other episode sources missing.

## Next bounded mapping

**GM-COV-002:** map only S01E01/S02's 11 canonical narrator lines to its own three established editorial shots and truthful planned still/audio/motion requirements. No existing media may be invented or approved. See `docs/NEXT_CHAT_PROMPT.md`.
