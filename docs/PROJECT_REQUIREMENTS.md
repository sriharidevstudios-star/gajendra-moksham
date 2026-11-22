# Project requirements — working release target

## Editorial intent

Create a faithful, emotionally engaging, family-friendly original dramatization of **Gajendra Moksham**, rooted in **Śrīmad Bhāgavatam 8.2–8.4**, in **natural spoken Telugu, Hindi and English**. Aim at children around 6–10 and their families, without reducing surrender/moksha to generic self-help. Suggest six connected ~6-minute episodes (330–390 seconds per language) rather than forcing the shorter canonical account into the twelve-episode Prahlada season.

## Acceptance gates

| ID | Requirement | Evidence needed |
|---|---|---|
| GM-R01 | Faithful source chronology and verse map | Each scene maps to SB 8.2–8.4; non-scriptural connective scenes labeled original |
| GM-R02 | Complete meaningful six-episode arc | All six canonical episode sources exist; no unresolved ending |
| GM-R03 | Telugu/Hindi/English performed dialogue | Stable line IDs and aligned meaning, three complete native-language scripts; Telugu first |
| GM-R04 | Truthful duration | Measured 330–390 seconds per language after rough-cut audio and action timing |
| GM-R05 | Gajendra as elephant, not a human in costume | Consistent trunk, ears, tusks, scale and quadrupedal anatomy; spoken prayer uses deliberate voice-over treatment |
| GM-R06 | Non-graphic child-safe danger | Crocodile attack/struggle/rescue clear, but no blood, wounds, suffering spectacle or gruesome disc strike |
| GM-R07 | Scriptural prayer carefully portrayed | Gajendra's remembered prayer, lotus offering, Garuḍa arrival, Nārāyaṇa's intervention shown in correct order |
| GM-R08 | Correct previous lives | Crocodile = cursed Gandharva Hūhū; elephant = former Indradyumna; respective sages Devala/Agastya not swapped |
| GM-R09 | Complete devotional conclusion | Crocodile's animal life ends; Hūhū is restored, Gajendra obtains sārūpya-mukti; Lord's benediction and departure |
| GM-R10 | Stable identity/scale and audio ownership | Approved refs/voice auditions, per-line audio and per-frame/motion ownership, no invented assets |
| GM-R11 | Reproducible pipeline | Local schema/build/validators pass once implemented, with exact checked file hashes |
| GM-R12 | Publishing-ready output | Actual rendered video/audio/subtitles and rights/quality reviews, no placeholder assets passed off as completed |

## Non-negotiable distinction

Planning, authored specs, rendered artwork, reviewed artwork, published media and completed tests are different statuses. Never label one as another. A text-only character brief is not an approved portrait. A line with script text is not an audio recording. A planned frame is not a generated still.

## Production approach

Reuse proven *mechanisms* from Prahlada: stable IDs, dialogue-first canonical sources, per-language recordings, two-pass reference-driven art, per-frame spec hashing, audit receipts, explicit visual/audio/motion coverage, ComfyUI + A2V and guarded commits. Rework *content and anatomy* for quadrupeds, divine figures and naturalistic non-talking animals.

`main` is for reviewed merges. Proposed development branch: `production-artwork` with a draft pull request.
