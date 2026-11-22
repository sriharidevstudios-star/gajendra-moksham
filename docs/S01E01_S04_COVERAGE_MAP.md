# S01E01/S04 — picture and audio ownership coverage map (GM-COV-004)

**Date:** 2026-11-22  
**Repository:** `sriharidevstudios-star/gajendra-moksham` · branch `production-artwork` · draft PR #1 into `main`  
**Verified canonical source snapshot:** commit `095963bc98e5b05d15e7e429738996410c06a7e5`; Git blob `4cd9ae7db28542fe3fbc2254394aed43f4a75bea`  
**Canonical authority:** `seasons/season-01/episodes/s01e01-the-lake-at-trikuta/episode.json`  
**Scene:** `S01E01/S04` — “Thirst and Relief at the Water”; exact scripture [Śrīmad-Bhāgavatam 8.2.25](https://vedabase.io/en/library/sb/8/2/25/) and [8.2.26](https://vedabase.io/en/library/sb/8/2/26/)  
**Status:** **METADATA-ONLY PLAN**. Eleven canonical trilingual narration lines mapped once to three existing editorial shots. Media and native signoff are **MISSING / NOT APPROVED**.

## Current live GitHub inventory — source documents PRESENT; media MISSING

| Source / tracker | Verified evidence |
|---|---|
| Canonical episode source | **PRESENT text:** `episode.json` blob `4cd9ae7db28542fe3fbc2254394aed43f4a75bea`, six authored scenes, 54 trilingual line IDs, S01E01 `partial_scene_draft`, preferred **330 seconds** |
| S04 text, IDs and shots | **PRESENT canonical data:** 11 `S01E01-S04-L001–L011`, three editorial shot objects `SH01–SH03`, **18+18+24=60 seconds** provisional |
| Prior S01/S02/S03 maps | **PRESENT docs-only plans:** `docs/S01E01_S01_COVERAGE_MAP.md` (blob `c9da0c1ae199c49a7b0a73c3f8708c6a9eb7d009`), S02 (blob `59c7fe128fa0c014aa0ca971df9f41c8fcf164e2`), S03 (blob `9062e842712e1878ed00940d59bb8aae12ac553c`); none is delivered artwork |
| `assets/asset_registry.json` | **PRESENT registry file:** blob `2036bb5675635a81c8713b1b6c15ba38a46547bc`, `status=empty_no_media_generated`, `assets=[]`; no registered images, audio or clips |
| `assets/character_bible.json` | **PRESENT text brief:** blob `aa387fdeb136ce708ed9b9a905f14cca1ec98972`, Gajendra `approved=false`, approved reference `null`; herd lacks a supplied approved visual reference |
| `assets/shot_spec_policy.json` | **PRESENT planning policy:** blob `c682d95dab2690e9b37921c6621b1cc9053d26a2`, `status=policy_brief_not_compiler_schema`; no validated per-shot frame specifications/receipts |
| `seasons/season-01/voice_cast.json` | **PRESENT voice planning:** blob `d4d03e6bf72cdf7cc877e656acb1fbb81c3ce713`; NARRATOR for te/hi/en has `candidate_id=null`, `audio_reference=null`, `approved=false` |
| `seasons/season-01/production_tracker.json` | **PRESENT planning:** blob `e7e5a3a524846be8ed60a79d50e60f43dff77364`; S01E01 `media_files=[]`, unapproved voices/references/shot specs, no verified keyframes, recordings or motion |
| `docs/S01E01_NATIVE_LISTENER_CHECKLIST.md` | **PRESENT unapproved checklist**, blob `abcbdfb4811c41c7ec795fcb5c35e1fb48987554`; no accepted human listener, devotional review, table-read timing or voice |
| Live recursive Git tree | `1101dbd48fabc8828adfd58706600ea984e844ab` inspected completely and non-truncated: **no tracked PNG/JPEG/WebP/GIF/SVG, WAV/MP3/M4A/FLAC/OGG, MP4/MOV/WebM/MKV media**. No S04 frame, narration audio, still receipt, sound clip or motion video exists in the verified Git tree |

**Readiness nuance:** The planning tracker still says `canonical_story_written=false` although S01E01 has a six-scene **partial** written source. It is a stale planning flag, not permission to claim the episode is voice-approved, image-produced or fully scripted. This batch does **not** change it.

## Canonical S04 narration line → existing editorial shot

The authoritative Telugu, Hindi and English spoken words stay exclusively in `episode.json` `dialogue[id].text.te/.hi/.en`; this document is an *ownership plan*, not replacement text or a recording. All eleven rows have `speaker=NARRATOR`, `audio_owner=NARRATOR`, `performance_mode=narration`, `lip_sync_target=null`, `source_attribution.kind=scripture_paraphrase`. Each implies one future narration line per language, **33 PLANNED audio-line requirements, 0 actual recorded clips**.

| Canonical S04 line ID | Existing shot owner | Exact verse locator | te owner | hi owner | en owner | Lip-sync | Actual audio |
|---|---|---|---|---|---|---|---|
| `S01E01-S04-L001` | `S01E01-S04-SH01` | [`SB 8.2.25`](https://vedabase.io/en/library/sb/8/2/25/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S04-L002` | `S01E01-S04-SH01` | [`SB 8.2.25`](https://vedabase.io/en/library/sb/8/2/25/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S04-L003` | `S01E01-S04-SH01` | [`SB 8.2.25`](https://vedabase.io/en/library/sb/8/2/25/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S04-L004` | `S01E01-S04-SH02` | [`SB 8.2.25`](https://vedabase.io/en/library/sb/8/2/25/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S04-L005` | `S01E01-S04-SH02` | [`SB 8.2.25`](https://vedabase.io/en/library/sb/8/2/25/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S04-L006` | `S01E01-S04-SH02` | [`SB 8.2.25`](https://vedabase.io/en/library/sb/8/2/25/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S04-L007` | `S01E01-S04-SH02` | [`SB 8.2.25`](https://vedabase.io/en/library/sb/8/2/25/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S04-L008` | `S01E01-S04-SH03` | [`SB 8.2.26`](https://vedabase.io/en/library/sb/8/2/26/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S04-L009` | `S01E01-S04-SH03` | [`SB 8.2.26`](https://vedabase.io/en/library/sb/8/2/26/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S04-L010` | `S01E01-S04-SH03` | [`SB 8.2.26`](https://vedabase.io/en/library/sb/8/2/26/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S04-L011` | `S01E01-S04-SH03` | [`SB 8.2.26`](https://vedabase.io/en/library/sb/8/2/26/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |

**Integrity:** 11/11 S04 IDs assigned exactly once; all 11 locators covered by existing 8.2.25–26 anchors. SH01 owns **L001–L003**, SH02 **L004–L007**, SH03 **L008–L011**. No Gajendra, calf or crocodile has an authored speaking turn.

## Per-shot PLANNED boundary image, motion and sound requirements

There are **six shot-boundary composition requirements** (one planned start and one planned end for each of three *existing* shots), **not six generated or named frame files**. Any future shared boundary image must be justified and reviewed in a separate artwork/shot-spec batch.

### S01E01-S04-SH01 — Entering and bathing at the established lake bank

- **Canonical line owner:** `S01E01-S04-L001`, `S01E01-S04-L002`, `S01E01-S04-L003`; **budget:** 18s, **English whitespace words:** 26 (not measured speech). te/hi/en are planned `NARRATOR` voice tracks with no approved voice ID, `narration`, `lip_sync_target=null`.
- **PLANNED start-frame requirement:** An approved-in-future 16:9 master of the *same freshwater approach bank* visible at the end of S03, with the golden lotus/water-lily band and deeper center fixed in the background; Gajendra on land or just stepping into the near shallows. Female elephants/calves remain safely near the shoreline, no crocodile.
- **PLANNED end-frame requirement:** Gajendra now naturally within the lake near the entry bank, water on his tired body, gentle ripples and visually coherent lotus/water-lily pollen *mixed in the lake water*; clear bank/lotus/deep-center positions persist. No injured leg or lurking creature.
- **PLANNED camera and composition:** Medium-wide 16:9 bank-to-water tracking and steady water-level view; keep Gajendra quadrupedal, trunk/tusks/ears consistent and shoreline axis readable.
- **PLANNED motion:** Natural elephant stepping/first bathing as water gently moves; no human hands, extra trunks, mouth-synced speech or excessive splash spectacle. Approved start/end composition stills are required before selecting any image-to-video method.
- **PLANNED environmental/SFX/music:** Proposed lake birds, mild water laps and bathing/slosh under an offscreen NARRATOR; an original/licensed score may be planned but no sound file or voice exists.
- **PLANNED edit/continuity:** Resume S03's exact final bank/master view, not S01's Ocean of Milk shoreline; SH02 stays at the same close shoreline for drinking.
- **Source/production review note:** SB 8.2.25 grounds the lake entry, cool clear lotus-pollen water and bathing; the precise camera movement, trunk posture and placement of herd are staging decisions. Do not portray pollen as magically drifting independent of the water.
- **Actual assets:** start still **MISSING**, end still **MISSING**, approved Gajendra/herd/lake reference **MISSING**, recorded te/hi/en narration **MISSING**, sound/music files **MISSING**, validated shot specs/receipts **MISSING**, I2V/motion clips **MISSING**. No file path, frame ID, generation job, receipt or SHA is implied.

### S01E01-S04-SH02 — Trunk drinking, relief of thirst and continuing bath

- **Canonical line owner:** `S01E01-S04-L004`, `S01E01-S04-L005`, `S01E01-S04-L006`, `S01E01-S04-L007`; **budget:** 18s, **English whitespace words:** 33 (not measured speech). te/hi/en are planned `NARRATOR` voice tracks with no approved voice ID, `narration`, `lip_sync_target=null`.
- **PLANNED start-frame requirement:** Natural-profile medium shot of Gajendra at the same shore waterline, trunk drawing lake water; body size, eyes, ears and tusks match SH01. Clear water with flower pollen remains physically plausible.
- **PLANNED end-frame requirement:** Gajendra visibly refreshed, trunk and forehead wet from drinking and gently splashing his own body, still within the same shallows with the bank visible and the herd near shore; prepare for sharing with the family in SH03.
- **PLANNED camera and composition:** Medium trunk detail and natural medium-wide bathing coverage, no change of bank orientation or false close-up of a talking elephant mouth.
- **PLANNED motion:** Trunk draws water and pours it naturally into mouth, with a calm second splash across his body. No invented prolonged ritual, lotus offering or transformation; two separate editorial visual states are proposed rather than already produced frames.
- **PLANNED environmental/SFX/music:** Trunk drawing and drinking, natural soft splashes, lake birds and calm forest atmosphere; all proposed SFX, no approved/recorded actor voice.
- **PLANNED edit/continuity:** Maintain the exact trunk/tusk/shore continuity into SH03's wider herd group. The S04 story begins with an initial bath already in SH01; repeating self-splashing after drinking is an editorial order to verify at table read.
- **Source/production review note:** SB 8.2.25 supports his drinking with trunk until satisfied, bathing and relief of fatigue. The existing script L006 says 'Then he poured water over himself' after drinking; a second bath is not an independently described scriptural event. GM-LANG-004 deferred this phrasing/shot order to a timed human table read, so do not silently rewrite or claim a second canon incident here.
- **Actual assets:** start still **MISSING**, end still **MISSING**, approved Gajendra/herd/lake reference **MISSING**, recorded te/hi/en narration **MISSING**, sound/music files **MISSING**, validated shot specs/receipts **MISSING**, I2V/motion clips **MISSING**. No file path, frame ID, generation job, receipt or SHA is implied.

### S01E01-S04-SH03 — Sharing water with female elephants and calves

- **Canonical line owner:** `S01E01-S04-L008`, `S01E01-S04-L009`, `S01E01-S04-L010`, `S01E01-S04-L011`; **budget:** 24s, **English whitespace words:** 41 (not measured speech). te/hi/en are planned `NARRATOR` voice tracks with no approved voice ID, `narration`, `lip_sync_target=null`.
- **PLANNED start-frame requirement:** Wide family grouping on the same near-shallow bank. Adult females and smaller calves are naturally scaled; Gajendra lifts clean lake water with his trunk while the golden-lotus band/deeper center remain in their established relation.
- **PLANNED end-frame requirement:** Gajendra and his family bathing/drinking in coherent near-shallow positions as his trunk spray subsides; calm living-water ripples with no ominous underwater cut. S05 begins from this exact peaceful grouping.
- **PLANNED camera and composition:** Stable wide 16:9 lake-bank group composition plus one natural medium trunk-spray angle if approved; no reversal of calf/adult placement, and no speaking elephant mouth or anthropomorphic hands.
- **PLANNED motion:** Source-grounded water lifted with trunk, gentle spray over female elephants and calves, help them bathe/drink. Keep children near adults and in visually safe shallows. No magically offered lotus, no staged predatory shadow.
- **PLANNED environmental/SFX/music:** Gentle spray, natural calf/elephant ambient calls and lake/forest birds under the NARRATOR; no recorded animals as scripted voices or human-mouth lip-sync.
- **PLANNED edit/continuity:** S04 ends at a peaceful herd-water tableau; S05 is a short source-disclosed cinematic pause after the verse-26 water play. Save first crocodile appearance and sudden grip only for S06 in verse 8.2.27.
- **Source/production review note:** SB 8.2.26 covers lifting/sprinkling water and helping female elephants/calves drink and bathe, with an editorially simplified reflection on attachment/effort. S04/L011's devotional nuance involving māyā needs expert review, not invented additional doctrine; family care is not treated as intrinsically wrong.
- **Actual assets:** start still **MISSING**, end still **MISSING**, approved Gajendra/herd/lake reference **MISSING**, recorded te/hi/en narration **MISSING**, sound/music files **MISSING**, validated shot specs/receipts **MISSING**, I2V/motion clips **MISSING**. No file path, frame ID, generation job, receipt or SHA is implied.

## Boundary, scripture, animal and cultural continuity

1. **Source (8.2.25–26):** Gajendra enters the lake, bathes in clear cold water mixed with lotus/water-lily pollen, drinks using his trunk until satisfied, and helps female elephants and calves bathe and drink by lifting/sprinkling water. All prose is independently authored; this map does not reproduce published translations or add named animal dialogue.
2. **S03 → S04 geography:** Reuse S02's single **freshwater** lake with tree-lined near approach bank, recognizable lotus band and deeper center; S03 ends *on that bank*. S04 enters the water from that location. S01's Ocean of Milk is geographically distinct.
3. **Gajendra form and family:** Natural Indian elephant quadruped with consistent trunk, tusks, ears and brow; female elephants are adults with smaller calves, kept close in shallow water. Water should move naturally. No crowns, anthropomorphic hands, lip-synced human speech, costume, invented named calves or speaking crocodile.
4. **Deferred scene-order issue:** S04/SH01 and L001–L003 describe bathing at entry; SH02's L004–L007 include drinking then a second trunk-water splash. A **native-language table read/shot-edit review** must assess whether the flow needs a separately authorized continuity refinement; do not call two distinct baths a verse-verified event or change the canonical text here.
5. **Verse 26 devotional nuance:** The passage also reflects on familial attachment/spiritual perception. The three-language child-accessible L011 paraphrase is **not approved as full theological interpretation**. Require a source-aware devotional reviewer, without declaring family care sinful or inserting new divine punishment.
6. **No crocodile yet:** S04 and the short reflective S05 have no predator, eye, lurking water shadow, attack sound, horror cue or pre-attack point-of-view. The crocodile first grips Gajendra in S06 (8.2.27). The lotus Gajendra later offers belongs at Nārāyaṇa's arrival in 8.3.31–32, not S04.
7. **Timing and audio:** SH01 3 lines in 18s; SH02 4 lines in 18s; SH03 4 lines in 24s. These are **provisional scene/shot editorial budgets**, not timed three-language readings. SFX need original/licensed files, and all real narrator audio, shot stills, motion renders and native approval are missing. Do not imply a table-read PASS or a single consistent narration speed for all three languages.

## Validation and handoff

- **In-process checks PASS:** 11 unique ordered S04 IDs, one-to-one assignment to existing shot IDs, 18+18+24 = 60s, correct 8.2.25/26 line-to-URL anchors, all te/hi/en nonempty, 11 NARRATOR audio owners with `narration` and `lip_sync_target=null`.
- **Live GitHub inventory CHECKED:** source/registry metadata present, full tree has no media, no accepted Gajendra image or narrator voice, no approved per-shot spec and no motion/voice deliveries. Frame/audio/sound/motion are MISSING.
- **Python tests:** `python3 -m unittest discover -s tests -v` — **UNRUN**, remote GitHub connector has no checked-in code execution.
- **Python scoped validation:** `python3 scripts/validate_content.py --episode S01E01 --scene S04` — **UNRUN**; do not claim executed `SCOPED_READY`.
- **Deterministic text-only builder/`--check`:** `python3 scripts/build_season_dialogue.py --episode S01E01 --scene S04` and `--check` — **UNRUN**, no exports or media created.
- **Whole-season validator:** `python3 scripts/validate_content.py` — **UNRUN**, expected NOT_READY due missing E02–E06 canonical episode sources.
- **Unchanged:** canonical `episode.json`, all 54 trilingual lines, six scenes/18 shots, earlier S01–S03 coverage maps, listener checklist, season status, source/asset/voice registries and production tracker.
- **Next bounded batch:** GM-COV-005 for S01E01/S05. The S05 bridge lasts **30 provisional seconds**, with **4** canonical narrator lines and three existing **10-second** shots. It is mostly clearly labeled `original_dramatization` and must not invent an approaching crocodile. See `docs/NEXT_CHAT_PROMPT.md`.
