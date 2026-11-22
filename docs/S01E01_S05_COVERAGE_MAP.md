# S01E01/S05 — picture/audio ownership coverage map (GM-COV-005)

**Prepared:** 2026-11-22 · **Repository:** `sriharidevstudios-star/gajendra-moksham` · branch `production-artwork` · draft PR #1 into `main`  
**Verified source HEAD:** `6346a8b5c82b368ee65030941b4a71c9c4cc96fa` · **Canonical source:** `seasons/season-01/episodes/s01e01-the-lake-at-trikuta/episode.json` · Git blob `4cd9ae7db28542fe3fbc2254394aed43f4a75bea`  
**Scene:** `S01E01/S05` — “The Calm Beneath the Surface” · [Śrīmad-Bhāgavatam 8.2.26](https://vedabase.io/en/library/sb/8/2/26/) (with [8.2.27](https://vedabase.io/en/library/sb/8/2/27/) reserved exclusively for S06)  
**Status:** **METADATA-ONLY PLAN**. Four canonical narration lines are mapped once to three PRESENT editorial shot descriptions, with **10+10+10=30 seconds** of provisional budgets. All described start/end frames, recordings, SFX and motion are merely **PLANNED**, actual media **MISSING**.

## Live GitHub proof: PRESENT text vs MISSING media

| Evidence | State confirmed at `6346a8b5c82b368ee65030941b4a71c9c4cc96fa` |
|---|---|
| Canonical `episode.json` | **PRESENT source text**, blob `4cd9ae7db28542fe3fbc2254394aed43f4a75bea`: six authored scenes / 54 stable trilingual line IDs; `partial_scene_draft`, E01 preferred `330s` |
| S05 editorial shot and narration objects | **PRESENT source metadata**: 4 stable lines, 3 canonical shots `S01E01-S05-SH01`/SH02/SH03 with **10/10/10** budget; 1 verse paraphrase and 3 clearly labeled original dramatizations |
| Previous four coverage maps | **PRESENT documentation only**: `docs/S01E01_S01_COVERAGE_MAP.md` through `docs/S01E01_S04_COVERAGE_MAP.md`, none providing real artwork or audio |
| `assets/asset_registry.json` | **PRESENT metadata**, blob `2036bb5675635a81c8713b1b6c15ba38a46547bc`: `status=empty_no_media_generated` and `assets=[]` |
| `assets/character_bible.json` | **PRESENT textual identity guide**, blob `aa387fdeb136ce708ed9b9a905f14cca1ec98972`: `GAJENDRA.approved=false`, `approved_reference=null`; no approved elephant/mother/calf artwork |
| `assets/shot_spec_policy.json` | **PRESENT policy**, blob `c682d95dab2690e9b37921c6621b1cc9053d26a2`: `status=policy_brief_not_compiler_schema`; no accepted per-S05 shot spec, prompt receipt or output record |
| `seasons/season-01/voice_cast.json` | **PRESENT planning file**, blob `d4d03e6bf72cdf7cc877e656acb1fbb81c3ce713`: te/hi/en `NARRATOR` voice candidates, audio references all `null`; approvals `false` |
| `seasons/season-01/production_tracker.json` | **PRESENT planning file**, blob `e7e5a3a524846be8ed60a79d50e60f43dff77364`: `media_files=[]`, no approved image references/voices, keyframes, recorded audio, verified specs or motion |
| `docs/S01E01_NATIVE_LISTENER_CHECKLIST.md` | **PRESENT blank review checklist**, blob `abcbdfb4811c41c7ec795fcb5c35e1fb48987554`; native Telugu/Hindi/English listening and devotional/table-read approval **NOT APPROVED** |
| Non-truncated recursive Git tree | Tree `b7d50310a0537f73fb5253800bba532d46c04d69`: **zero tracked PNG/JPEG/WebP/GIF/SVG, WAV/MP3/M4A/FLAC/OGG or MP4/MOV/WebM/MKV media files**; no source-approved S05 image/start/end still, recorded track, review hash, sound asset or motion clip |

**Tracker caveat:** `production_tracker.json` retains `canonical_story_written=false` from early planning even though E01 now contains six *partially authored* canonical scenes. This mismatch is noted, not silently fixed or promoted to a completed/approved episode in this docs-only batch.

## Source-honest line/shot ownership — 4 of 4 covered once

The exact spoken Telugu, Hindi and English text remains **solely** in `episode.json → dialogue[id].text.te/.hi/.en`. This map assigns a future language-specific audio requirement to each canonical text field, with `speaker=NARRATOR`, `audio_owner=NARRATOR`, `performance_mode=narration` and `lip_sync_target=null` on all rows: **4 lines × 3 languages = 12 PLANNED narration tracks, 0 recordings**.

| Canonical narration ID | Existing shot | Attribution kind and exact provenance | te audio owner | hi audio owner | en audio owner | Lip-sync | Audio file |
|---|---|---|---|---|---|---|---|
| `S01E01-S05-L001` | `S01E01-S05-SH01` | [`scripture_paraphrase` — SB 8.2.26](https://vedabase.io/en/library/sb/8/2/26/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S05-L002` | `S01E01-S05-SH02` | `original_dramatization` — exact disclosure preserved below | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S05-L003` | `S01E01-S05-SH03` | `original_dramatization` — exact disclosure preserved below | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S05-L004` | `S01E01-S05-SH03` | `original_dramatization` — exact disclosure preserved below | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |

**Coverage:** `L001 → SH01` (10s), `L002 → SH02` (10s), `L003–L004 → SH03` (10s); four unique line IDs assigned exactly once, no unowned or duplicated dialogue.

### Complete original-dramatization disclosures (not scripture claims)

These are the exact existing canonical `source_attribution.note` values; the three screenplay/atmosphere beats are **not** episodes narrated separately in the source.

- `S01E01-S05-L002` — **`original_dramatization`**: Original visual continuity insert: a calf beside its mother and the last droplets from Gajendra's trunk are staged, not a separately narrated verse incident.
- `S01E01-S05-L003` — **`original_dramatization`**: Original atmospheric insert of normal water movement in the already established lotus lake; not a plot incident or a sign of a crocodile.
- `S01E01-S05-L004` — **`original_dramatization`**: Original brief scenic hold for editorial transition only; the source moves directly to the foot-grip in 8.2.27 and makes no claim of preceding calm or stalking.

The only scripture-paraphrase line is `S01E01-S05-L001` with locator **8.2.26**. S05's canonical source anchor also contains 8.2.25 as surrounding continuity, but **no S05 narration line cites 8.2.25**, and the original-atmosphere lines are not assigned imaginary verse locators. [Verse 8.2.27](https://vedabase.io/en/library/sb/8/2/27/) starts with the crocodile's sudden leg-grip; there is **no** separate source-described underwater stalk/approach/ominous pause. The working S05 title is metaphorical only.

## Three PLANNED shot-boundary composition, sound and motion requirements

The six entries below are **requirements for potential future start/end compositions** (two per existing shot). They are NOT named frame IDs, generated files or a guarantee six separate stills will be needed. Any approved cross-shot reuse must follow actual future continuity/reference review.

### S01E01-S05-SH01 — Settling after the herd's water play

- **Exact line owners:** `S01E01-S05-L001`. **Provisional budget:** 10s. **te/hi/en audio:** NARRATOR narration, `lip_sync_target=null`; no audio file or voice approval. **English whitespace words:** 9 (not a measured spoken duration).
- **PLANNED start-frame requirement:** The exact concluding S04/SH03 family tableau at the freshwater lake's near-shallow bank: Gajendra naturally quadrupedal with female elephants and calves beside him; established tree line and golden-lotus band hold the same screen orientation.
- **PLANNED end-frame requirement:** Same calm herd group with large splashes subsiding; Gajendra's natural head/trunk orientation remains consistent, calves safe among adults, and no newly approaching or hidden predator.
- **PLANNED camera/composition:** Fixed 16:9 medium-wide lakeside master, gentle observational hold. No underwater view, reverse-axis geography, expressive humanlike elephant face or fabricated suspense framing.
- **PLANNED motion treatment:** Only small settling movements in the elephants, ordinary breathing and easing lake splashes as a continuous source-disclosed editorial pause.
- **PLANNED ambient sound/SFX:** Natural subdued fresh-water lapping, distant lake birds and the last quiet drops beneath NARRATOR; do not add rising threatening music or a 'something is coming' cue.
- **PLANNED cut/continuity:** S04's real last shot flows directly into this S05 hold; the family is in the same place, not a separate episode or new event.
- **Source-fidelity note:** L001 is the only scripture_paraphrase here (SB 8.2.26: Gajendra remains preoccupied with the female elephants and young). This line repeats S04/L011's family focus; its performance and possible redundancy remain flagged for a later native-listener/editorial table read, not changed here.
- **Actual media status:** start still **MISSING**, end still **MISSING**, approved Gajendra/mother/calf/lake reference **MISSING**, te/hi/en narration recordings **MISSING**, voice IDs **MISSING**, ambient/SFX/music audio **MISSING**, reviewed per-shot spec and receipt **MISSING**, motion/video output **MISSING**. No invented file paths, start/end frame IDs, hashes, approved jobs or delivered art.

### S01E01-S05-SH02 — A calf beside its mother as droplets fall

- **Exact line owners:** `S01E01-S05-L002`. **Provisional budget:** 10s. **te/hi/en audio:** NARRATOR narration, `lip_sync_target=null`; no audio file or voice approval. **English whitespace words:** 15 (not a measured spoken duration).
- **PLANNED start-frame requirement:** A close but natural medium view of an existing calf standing near its mother at the same safe shallow shoreline; Gajendra's trunk is still positioned just at the frame edge, droplets plausibly hanging from it.
- **PLANNED end-frame requirement:** The last few drops fall from Gajendra's trunk and the calf remains close to its mother with consistent body scale and shore depth; no novel named calf, no human affection gestures or mouth dialogue.
- **PLANNED camera/composition:** Single 16:9 medium detail tied visibly to the preceding bank-facing wide composition; simple focus on mother/calf spacing and trunk water, retaining the golden lotus area in background when possible.
- **PLANNED motion treatment:** Gentle water droplets falling by gravity and minor natural breathing/head motion; a later frame/animation team may choose a stable hold rather than assuming this needs independent character animation.
- **PLANNED ambient sound/SFX:** Light individual water drops, normal waterline ambience, soft elephant movement with no scripted animal voices; NARRATOR has one as-yet-unrecorded line.
- **PLANNED cut/continuity:** Return the look from the family detail to the *same* lake surface/lotus area in SH03, without interposing a crocodile or mysterious shadow.
- **Source-fidelity note:** L002 is original_dramatization. Exact canonical disclosure: Original visual continuity insert: a calf beside its mother and the last droplets from Gajendra's trunk are staged, not a separately narrated verse incident.
- **Actual media status:** start still **MISSING**, end still **MISSING**, approved Gajendra/mother/calf/lake reference **MISSING**, te/hi/en narration recordings **MISSING**, voice IDs **MISSING**, ambient/SFX/music audio **MISSING**, reviewed per-shot spec and receipt **MISSING**, motion/video output **MISSING**. No invented file paths, start/end frame IDs, hashes, approved jobs or delivered art.

### S01E01-S05-SH03 — Ordinary ripples fade among lotus leaves

- **Exact line owners:** `S01E01-S05-L003`, `S01E01-S05-L004`. **Provisional budget:** 10s. **te/hi/en audio:** NARRATOR narration, `lip_sync_target=null`; no audio file or voice approval. **English whitespace words:** 18 (not a measured spoken duration).
- **PLANNED start-frame requirement:** Shoreline-facing 16:9 composition of the existing freshwater golden-lotus band and natural water-surface ripples, at the same bank/center orientation as S02–S04. No submerged eye or unseen creature suggestion.
- **PLANNED end-frame requirement:** The same surface and lotus leaves grow visibly still through ordinary water movement while the narrator finishes L003–L004; end on a genuine quiet environmental tail with no crocodile, stalked POV, looming silhouette or ominous cue.
- **PLANNED camera/composition:** Still water-level/near-shore medium-wide with mild environmental motion; DO NOT create a crocodile POV, underwater shot, threat-colored lighting, or sudden dramatic push-in.
- **PLANNED motion treatment:** Small physical ripples dissipate, leaves move subtly, cut at end. This is only an editorial atmosphere hold and not a verse-described pre-attack incident.
- **PLANNED ambient sound/SFX:** Soft water and bird ambience, a gentle natural silence after narration, no horror sting; audio remains future planned SFX separate from NARRATOR.
- **PLANNED cut/continuity:** Cut from S05's peaceful surface directly into S06's *first* crocodile leg-grip (8.2.27). No foreshadowing shot, water shadow or stalking. Preserve the bank/deeper-water geography for S06's later leg-grip direction.
- **Source-fidelity note:** L003 and L004 are separate original_dramatization descriptions. Their exact notes: L003 — Original atmospheric insert of normal water movement in the already established lotus lake; not a plot incident or a sign of a crocodile. L004 — Original brief scenic hold for editorial transition only; the source moves directly to the foot-grip in 8.2.27 and makes no claim of preceding calm or stalking.
- **Actual media status:** start still **MISSING**, end still **MISSING**, approved Gajendra/mother/calf/lake reference **MISSING**, te/hi/en narration recordings **MISSING**, voice IDs **MISSING**, ambient/SFX/music audio **MISSING**, reviewed per-shot spec and receipt **MISSING**, motion/video output **MISSING**. No invented file paths, start/end frame IDs, hashes, approved jobs or delivered art.

## Fidelity, timing and approval gates

1. **Lake continuity:** S05 begins at S04/SH03's exact peaceful freshwater family grouping, with the same tree-lined near bank, adult/calf placement, golden-lotus band and deeper center from S02–S04. The cosmic Ocean of Milk in S01 remains separate.
2. **Natural animal behavior:** Gajendra remains quadrupedal with consistent ears, trunk and tusks. A calf beside its mother and final falling droplets in L002 are explicitly original blocking, not a newly discovered scriptural event. No talking elephants, lip-sync, crowns, human hands or invented named calf.
3. **Ordinary ripples, no threat cue:** L003 and L004 are disclosed atmospheric staging. No underwater camera, lurking eye, crocodile silhouette/shadow, unnatural suspense score, supernatural warning, predator POV or hidden stalk. **The first crocodile appears only in S06**, with the foot-grip in 8.2.27.
4. **Time budget and source fidelity:** SH01/SH02/SH03 = 10/10/10 seconds, not the original abandoned 60-second S05 plan. Do **not** pad the source with a separate stalking subplot. S05's 4 lines need a timed Telugu/Hindi/English table read; S05/SH03 L003–L004 must still leave room for a gentle environmental tail. These are estimates, not recordings.
5. **Open editorial duplication:** L001 reiterates Gajendra's focus on his herd from S04/L011. The language audit leaves this repetition **DEFERRED for human table-read**, and the coverage map doesn't delete, renumber or mark the line approved.
6. **Future acceptance order:** native language pronunciation and devotional review, real accepted visual references, per-shot source-aware specs, explicitly chosen start/end images with hashes and human review, licensed/original environmental audio, voice casting/recordings and measured timing, then motion/quality/delivery receipts. All remain **PENDING / MISSING**. A coverage plan is not production readiness.

## In-process validation and unrun gates

- **PASS (in-process, source-derived):** all four stable S05 line IDs mapped exactly once to three existing shots; 1 verse 8.2.26 paraphrase + 3 original dramatization notes; source owners `NARRATOR` in `te/hi/en`, `narration`, null lip-sync; shot budgets 10+10+10=30; original language fields nonempty.
- **CHECKED (GitHub inventory):** empty asset registry; no approved Gajendra reference, narration voice or recorded tracks; tracker media empty; full tree no tracked media; only planning shot-policy file. No image/TTS/audio/video or motion tool calls.
- **UNRUN** Python unit tests: `python3 -m unittest discover -s tests -v` — connected GitHub API has no repository code execution.
- **UNRUN** scoped source validator: `python3 scripts/validate_content.py --episode S01E01 --scene S05` — no executed `SCOPED_READY` claim.
- **UNRUN** deterministic text-only draft builder: `python3 scripts/build_season_dialogue.py --episode S01E01 --scene S05` and `--check`; no exports generated.
- **UNRUN** full-season validator: `python3 scripts/validate_content.py` — season expected **NOT_READY** due five missing canonical sources.
- **Preserved:** all 54 canonical source lines and 6 scene/18 shot objects, existing S01–S04 coverage maps, episode 330-second preferred, listener checklist, season index and all registries/tools/art. First episode stays `partial_scene_draft`.

**Next:** **GM-COV-006** — a single bounded S01E01/S06 crocodile first-grip coverage mapping. It begins only after S05, with source 8.2.27–28 and the extended struggle deferred to S01E02; see `docs/NEXT_CHAT_PROMPT.md`.
