# S01E01/S06 — picture/audio ownership coverage map (GM-COV-006)

**Prepared:** 2026-11-22  
**Repository:** `sriharidevstudios-star/gajendra-moksham` · branch `production-artwork` · draft PR #1 targeting `main`  
**Read-only canonical source:** `seasons/season-01/episodes/s01e01-the-lake-at-trikuta/episode.json` at remote HEAD `c7ddfa31cdf7b14cea64aea96d63e751552e83a0` · blob `4cd9ae7db28542fe3fbc2254394aed43f4a75bea`  
**Scene:** `S01E01/S06` — “The Crocodile's Sudden Grip” · [Śrīmad-Bhāgavatam 8.2.27](https://vedabase.io/en/library/sb/8/2/27/) and [8.2.28](https://vedabase.io/en/library/sb/8/2/28/)  
**Scope:** **9/9** canonical narration IDs mapped once to **3 PRESENT editorial shot records** totaling **18+22+20 = 60 provisional seconds**. This is a **DOCS-ONLY PLAN**, not finished motion or any approved artwork/audio.

## Repository evidence — PRESENT planning versus missing actual media

| Live source | Checked state |
|---|---|
| Canonical `episode.json` | **PRESENT source text** (blob `4cd9ae7db28542fe3fbc2254394aed43f4a75bea`): six scenes, 54 te/hi/en narration lines, `partial_scene_draft`, E01 preferred **330s** |
| Canonical S06 shots and source | **PRESENT textual metadata**: `S01E01-S06-SH01` / `SH02` / `SH03`, **18/22/20s**; nine stable line IDs, eight verse paraphrases and one disclosed original line |
| S01–S05 coverage maps | **PRESENT docs-only plans**: all five `docs/S01E01_S01_COVERAGE_MAP.md` through `S05`; no delivered frame or audio implied |
| `assets/asset_registry.json` | **PRESENT metadata**, blob `2036bb5675635a81c8713b1b6c15ba38a46547bc`; `status=empty_no_media_generated`, `assets=[]`; zero delivered images/audio/motion/receipts |
| `assets/character_bible.json` | **PRESENT textual character briefs**, blob `aa387fdeb136ce708ed9b9a905f14cca1ec98972`; both `GAJENDRA` and `CROCODILE` have `approved=false`, `approved_reference=null` |
| `assets/shot_spec_policy.json` | **PRESENT policy brief**, blob `c682d95dab2690e9b37921c6621b1cc9053d26a2`; `status=policy_brief_not_compiler_schema`, no accepted per-S06 spec/receipt |
| `seasons/season-01/voice_cast.json` | **PRESENT planning metadata**, blob `d4d03e6bf72cdf7cc877e656acb1fbb81c3ce713`; no approved te/hi/en `NARRATOR` voice, each candidate and audio reference `null` |
| `seasons/season-01/production_tracker.json` | **PRESENT planning metadata**, blob `e7e5a3a524846be8ed60a79d50e60f43dff77364`; `media_files=[]`, audio/images/specs/motion unapproved and unverified |
| `docs/S01E01_NATIVE_LISTENER_CHECKLIST.md` | **PRESENT unapproved review form**, blob `abcbdfb4811c41c7ec795fcb5c35e1fb48987554`; no native language, devotional, recording or timing signoff |
| Full recursive Git tree | Tree `f4a2c4313ba7436c540b509ab452616bcc3f23b7` verified **non-truncated**, 36 tracked blobs and **zero image/audio/video files** (no PNG/JPEG/WebP/GIF/SVG, WAV/MP3/M4A/FLAC/OGG, MP4/MOV/WebM/MKV) |

**Historical tracker caveat:** The planning tracker still records `canonical_story_written=false` despite the authored **partial** E01 source. Its flag has not been changed here and is not evidence of a completed or approved script. The exact scene/line JSON is authoritative for current text ownership.

## Nine canonical lines → shot, scripture attribution, and three-language audio ownership

The authoritative spoken `text.te`, `text.hi`, `text.en` remain in **`episode.json`**, not duplicated in this coverage map. Each line has `speaker=NARRATOR`, `audio_owner=NARRATOR`, `performance_mode=narration`, `lip_sync_target=null`; no narrator voice is selected and no animal has a spoken line. Thus nine IDs create **27 PLANNED language-specific audio requirements**, **zero files or approvals**.

| Canonical line ID | Existing shot | Exact verse/attribution | te audio owner | hi audio owner | en audio owner | Lip sync | Actual recording |
|---|---|---|---|---|---|---|---|
| `S01E01-S06-L001` | `S01E01-S06-SH01` | [`scripture_paraphrase` SB 8.2.27](https://vedabase.io/en/library/sb/8/2/27/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S06-L002` | `S01E01-S06-SH01` | [`scripture_paraphrase` SB 8.2.27](https://vedabase.io/en/library/sb/8/2/27/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S06-L003` | `S01E01-S06-SH02` | [`scripture_paraphrase` SB 8.2.27](https://vedabase.io/en/library/sb/8/2/27/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S06-L004` | `S01E01-S06-SH02` | [`scripture_paraphrase` SB 8.2.27](https://vedabase.io/en/library/sb/8/2/27/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S06-L005` | `S01E01-S06-SH02` | [`scripture_paraphrase` SB 8.2.27](https://vedabase.io/en/library/sb/8/2/27/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S06-L006` | `S01E01-S06-SH02` | `original_dramatization` — disclosure below | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S06-L007` | `S01E01-S06-SH03` | [`scripture_paraphrase` SB 8.2.28](https://vedabase.io/en/library/sb/8/2/28/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S06-L008` | `S01E01-S06-SH03` | [`scripture_paraphrase` SB 8.2.28](https://vedabase.io/en/library/sb/8/2/28/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |
| `S01E01-S06-L009` | `S01E01-S06-SH03` | [`scripture_paraphrase` SB 8.2.27](https://vedabase.io/en/library/sb/8/2/27/) | NARRATOR — PLANNED | NARRATOR — PLANNED | NARRATOR — PLANNED | `null` | MISSING |

**Completeness:** SH01 has `L001–L002` (two lines), SH02 has `L003–L006` (four lines), SH03 has `L007–L009` (three lines). **9 unique assigned exactly once, zero unassigned, zero duplicated.** The verse anchors are precisely `8.2.27` and `8.2.28`; `L009` revisits the ongoing grip (8.2.27), even though it occurs after the herd's first cries (8.2.28).

### Exact canonical L006 original-dramatization disclosure

`S01E01-S06-L006` is **not** a scripture quotation or a newly stated Sanskrit detail. Its existing `source_attribution.kind` is `original_dramatization` and its **exact** `source_attribution.note` is:

> Original non-graphic water-splash staging to make the verse-27 effort readable; scripture does not specify the exact splashes or camera viewpoint.

No separate `source_attribution.locator` is attached to L006; the S06 source anchors remain background provenance for the grip. This distinguishes ordinary screenplay splashing from the 8.2.27 event itself.

## Per-shot future start/end still, motion, SFX and transition requirements

These are **six PLANNED boundary composition requirements** (one start, one end for each *existing* shot), **not** six named files, produced stills or assigned frame IDs. Future reviewed work may reuse an approved still at a shot boundary; this map does not invent that reuse.

### S01E01-S06-SH01 — First contact — the crocodile's sudden grip

- **Canonical narration owners:** `S01E01-S06-L001`, `S01E01-S06-L002`. **Budget:** 18s. **English whitespace words:** 21 (not a recorded narrator speed). Three unrecorded `NARRATOR` language requirements per line, `narration`, `lip_sync_target=null`.
- **PLANNED start-frame composition:** First S06 camera composition after S05's serene surface: 16:9 clear bank-side waterline medium-wide. Gajendra is natural and quadrupedal in the established shallows; **the crocodile first appears precisely as it makes sudden contact with Gajendra's left foreleg**. There is no preceding crocodile in S05, swimming stalk, shadow or predator-view frame.
- **PLANNED end-frame composition:** The newly introduced realistic crocodile has a readable non-graphic hold on Gajendra's left foreleg; Gajendra's other three legs, tusks, trunk, ears and body scale remain coherent. Golden-lotus region and deeper center stay in their established relative positions; no bleeding, wound or extra limb.
- **PLANNED camera/shot axis:** Use a stable 16:9 medium-wide body-blocking axis from the established near bank, large enough to read which foreleg is caught and where the crocodile lies in water, without a bite or wound close-up.
- **PLANNED motion:** A brief surprise cut from S05, water displacement and immediate capture at the first visible predator moment. Keep anatomical proportions stable; do not generate a hidden stalking approach, jump-scare or magically appearing extra crocodile.
- **PLANNED ambient sound and effects:** Proposed natural sudden water movement and a short non-graphic contact effect beneath NARRATOR. No horror sting, child-distressing gore sound, talking crocodile or unapproved score.
- **PLANNED continuity/cut:** S05/SH03's ordinary surface ripple ends peacefully; S06/SH01 begins the first visibly gripping crocodile. The same lake bank must remain bank/near-shallow and the deeper water remains beyond.
- **Verse/script/editorial distinction:** The verse 8.2.27 establishes a sudden powerful crocodile grasping Gajendra's foot/leg in water. **'Left foreleg' is an editorial repeatability decision**, not an exact scriptural designation. Neither image has been rendered or approved.
- **Actual delivery status:** start frame **MISSING**; end frame **MISSING**; approved Gajendra/crocodile/lake references **MISSING**; audio te/hi/en files **MISSING**; selected narrator voice IDs **MISSING**; ambient/SFX/music files **MISSING**; validated shot specs and prompt/review receipts **MISSING**; motion/video **MISSING**. No fabricated file, SHA, approved media job or identity.

### S01E01-S06-SH02 — Gajendra strains to escape; ordinary water splashes

- **Canonical narration owners:** `S01E01-S06-L003`, `S01E01-S06-L004`, `S01E01-S06-L005`, `S01E01-S06-L006`. **Budget:** 22s. **English whitespace words:** 30 (not a recorded narrator speed). Three unrecorded `NARRATOR` language requirements per line, `narration`, `lip_sync_target=null`.
- **PLANNED start-frame composition:** Continuity from SH01's fixed near-bank axis: the crocodile is still on the **same left foreleg**, Gajendra plants his other feet to brace in natural water depth. No change of tusks, trunk, leg contact, crocodile head profile or tail length.
- **PLANNED end-frame composition:** Gajendra remains held even as he pulls back with his strength; ordinary water is disturbed by the physical motion, with realistic non-graphic ripples/splashes. The crocodile's jaw stays consistent; no torn skin or long-battle montage.
- **PLANNED camera/shot axis:** One readable wide/medium-wide profile and optional natural leg/trunk insert, always returning to a complete anatomical view; avoid switching the leg via reverse shot or implying dismemberment.
- **PLANNED motion:** Naturalistic traction/pull-back effort, controlled crocodile grip and water sloshing; no impossible elephant joint movement, predatory POV, visual fantasy shockwave or prolonged repeated fight.
- **PLANNED ambient sound and effects:** Proposed moving water, a single natural elephant distress call as **SFX only**, environmental lake sounds and clear NARRATOR; no human animal voice/phoneme mouth tracking.
- **PLANNED continuity/cut:** Maintain axis, left foreleg, shore and deeper center from SH01 into SH03's family-wide response. Do not suggest a successful release before the other elephants appear.
- **Verse/script/editorial distinction:** L003–L005 remain `scripture_paraphrase` (SB 8.2.27). **L006 is `original_dramatization`**, and its exact existing disclosure reads: Original non-graphic water-splash staging to make the verse-27 effort readable; scripture does not specify the exact splashes or camera viewpoint. The canonical source does **not** prescribe the splash pattern, injury detail or camera viewpoint.
- **Actual delivery status:** start frame **MISSING**; end frame **MISSING**; approved Gajendra/crocodile/lake references **MISSING**; audio te/hi/en files **MISSING**; selected narrator voice IDs **MISSING**; ambient/SFX/music files **MISSING**; validated shot specs and prompt/review receipts **MISSING**; motion/video **MISSING**. No fabricated file, SHA, approved media job or identity.

### S01E01-S06-SH03 — Female elephants cry; the herd approaches but cannot yet free him

- **Canonical narration owners:** `S01E01-S06-L007`, `S01E01-S06-L008`, `S01E01-S06-L009`. **Budget:** 20s. **English whitespace words:** 26 (not a recorded narrator speed). Three unrecorded `NARRATOR` language requirements per line, `narration`, `lip_sync_target=null`.
- **PLANNED start-frame composition:** Return to the same readable 16:9 lake master: Gajendra's left foreleg is still caught near the entry shallows; female elephants and calves are grouped near the established bank, adult females reacting with natural calls.
- **PLANNED end-frame composition:** Female elephants are distressed and other elephants move nearer to help, but Gajendra's left leg remains **securely trapped** in the same crocodile hold. Calves remain behind adults, and the episode closes as a child-safe, non-graphic unresolved scene.
- **PLANNED camera/shot axis:** Near-bank master wide view, natural herd spatial separation and matching line of action to SH01–SH02; emphasize an intelligible leg hold without close violent detail or cinematic horror POV.
- **PLANNED motion:** Natural female-elephant distress calls/body cues, other adults begin to step toward Gajendra (not yet gripping/pulling him from behind); subtle waves stay physically grounded.
- **PLANNED ambient sound and effects:** Offscreen NARRATOR te/hi/en requirements; future planned elephant calls and water splashes as independent SFX. A brief restrained environmental tail is sufficient, not an ominous threat sting.
- **PLANNED continuity/cut:** The last S06 image is a still-trapped Gajendra, with family nearby. **S01E02/S01** must later depict the actual elephants grabbing/pulling from behind and failing as described by SB 8.2.28; SB 8.2.29's thousand-year struggle is subsequent, not inserted here.
- **Verse/script/editorial distinction:** L007 and L008 paraphrase the cries/approaching help in 8.2.28; L009 returns to the unresolved grip of 8.2.27. The failure of coordinated rescue is genuinely in 8.2.28 but is **adapted into Episode 2**, not invented as a newly later scriptural event. Do not portray success or repeat the whole failed rescue here.
- **Actual delivery status:** start frame **MISSING**; end frame **MISSING**; approved Gajendra/crocodile/lake references **MISSING**; audio te/hi/en files **MISSING**; selected narrator voice IDs **MISSING**; ambient/SFX/music files **MISSING**; validated shot specs and prompt/review receipts **MISSING**; motion/video **MISSING**. No fabricated file, SHA, approved media job or identity.

## Source-fidelity and production gates

1. **First crocodile visibility:** S05 ends on ordinary lotus-surface ripples with neither crocodile nor threat cue. S06/SH01 must contain its **first appearance as it grabs Gajendra's leg**; no underwater stalking, lurking eye, shadow, predator POV, foreshadowing score or early attack before this instant.
2. **Leg and lake geography:** SB 8.2.27 says `caraṇe` — foot/leg — without side. S06's **left foreleg** and master framing (entry bank left, deeper water right) are **editorial continuity choices**, not sacred text. Keep same anatomical contact/leg, elephant trunk/tusks, crocodile jaw/tail and shallows/deep-region direction through all three shots and later S01E02 footage.
3. **Child-safe, natural animals:** Gajendra remains a four-legged Indian elephant, not a crowned or speaking humanlike animal. The crocodile is one powerful real-shaped wild reptile, not an evil talking villain (later Hūhū history is not disclosed here). No blood, wounds, impossible legs, dismemberment, anthropomorphic expressions, action-horror sound or repeated jump-scares.
4. **Attribution boundary:** The grasp and Gajendra's initial efforts in 8.2.27 are **scripture paraphrases**; L006's exact existing original-atmosphere disclosure protects the separate splash staging. In 8.2.28 the female elephants cry and other elephants unsuccessfully grip from behind. **This adaptation shows only their distressed approach in S06 and reserves the actual unsuccessful pulling action for S01E02/S01**. Do not present that editorial scene split as separate scriptural chronology; do not stage a successful release in either episode.
5. **Long battle deferred:** [SB 8.2.29](https://vedabase.io/en/library/sb/8/2/29/) describes the extraordinary **thousand-year struggle**. No repeated extended combat, montage, water-versus-land advantage changes or spiritual resolution belongs in this 60-second S06 opening crisis scene. End the episode with Gajendra still held.
6. **Audio and time honesty:** 2 lines over SH01=18s, 4 lines over SH02=22s (L006 an original visual beat), 3 lines over SH03=20s. Natural te/hi/en narration timing, action pauses and SFX sync need **actual native-language table reads**; neither their duration nor their voice performances have been measured. Animal calls and splashes are ambient effects only; nobody provides a fictional voiced crocodile/elephant turn.
7. **Media prerequisites:** Before a *separate approved* artwork or audio batch, acquire and review consistent Gajendra/crocodile references, safe composition/specs, exact required frame IDs and real stills with hashes/receipts, an approved narrator per language, original or licensed audio effects, video-generation and handoffs. **All are MISSING** today. This plan is not an accepted shot-spec compiler artifact or a media delivery.

## Scope validation and unchanged source

- **PASS (in-process on live GitHub JSON):** nine unique S06 lines, canonical shot mapping 2+4+3, 18+22+20=60 scene seconds; eight verse-paraphrase lines cite existing 8.2.27 or 8.2.28 source URLs; L006 retains its original-dramatization note; all nine lines have te/hi/en `NARRATOR` ownership, `performance_mode=narration`, `lip_sync_target=null`.
- **CHECKED GitHub media truth:** non-truncated empty-media Git tree, asset registry `assets=[]`, Gajendra/crocodile reference images not approved, narrator voices not selected, production tracker with `media_files=[]`, shot-spec policy only a brief. Actual images, narration, SFX and motion **MISSING**.
- **UNRUN Python tests:** `python3 -m unittest discover -s tests -v`; remote GitHub connector does not execute checked-in repository Python.
- **UNRUN Python scoped validator:** `python3 scripts/validate_content.py --episode S01E01 --scene S06`; do not claim an executed `SCOPED_READY`.
- **UNRUN deterministic text-only build and freshness check:** `python3 scripts/build_season_dialogue.py --episode S01E01 --scene S06` followed by `--check`; no files built.
- **UNRUN whole-season gate:** `python3 scripts/validate_content.py`; expected **NOT_READY** because E02–E06 lack canonical episode sources.
- **Unchanged:** complete `episode.json`, all 54 script IDs/scene/shot specs and 330-second target, S01–S05 coverage docs, native-listener checklist, season metadata, character/voice/asset registries, production tracker, Python code, and all media (none).
- **Next bounded task:** **GM-COV-007**, reconcile the six now-documented S01E01 scene coverage maps against all 54 source line IDs, 18 shot IDs and honesty/continuity/source gates; no images or story change. Exact handoff in `docs/NEXT_CHAT_PROMPT.md`.
