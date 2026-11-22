# Production pipeline and release gates

Follow the working **Prahlada** process, not its story files, finished counts or unreviewed outputs.

| Stage | Output | Pass condition |
|---|---|---|
| 0. Setup (GM-SETUP-001) | Source plan, bible, six-episode map, handoff | Docs committed and branch/PR verified; **this batch only** |
| 1. Schema and offline tools (GM-ARCH-001) | Adapted episode schema, tiny fixture, stdlib validator/builder | Unit tests really run and pass; no fake season completion |
| 2. Canonical scripts (GM-STY series) | Episode/scene sources in Telugu, Hindi, English | Full line ID alignment and native reading; source deviations logged |
| 3. TTS & voice casting | Candidate voice IDs, pronunciation tests, clean manifests | Listening approval for each named role and language |
| 4. Visual bible and reference art | Approved character turnarounds, environment masters | Actual rendered stills + hashes + human visual approval |
| 5. Shot specs and coverage | Per-scene/per-frame visibility, exact audio owner, shot budgets | Validator checks geometry, identity, referenced assets and missing truth |
| 6. Keyframes and motion | Approved start/end frames, LTX/Wan/ComfyUI clip receipts | Real source/output files, coverage map and QC evidence |
| 7. Compositing, dialogue animation and edit | Speaker-correct scenes, actual runtime, captions | Animal voiceover policy, seam/identity/mouth/latency checks |
| 8. Publication | 3-language masters, audio/captions/metadata | Rights, family-safety, native-language and final-playback gates signed |

## Bounded batch rules

- Each chat changes **one scoped responsibility**; record next exact batch in `docs/NEXT_CHAT_PROMPT.md`.
- Do not create fake assets to satisfy validators. A missing image or audio file stays missing until checked.
- Keep `episode.json` and named source references authoritative; derived exports must be reproducible and content-hashed.
- Build from approved reference art and preserve identity across start/end frames and speaking crops.
- Guard against anatomic drift: extra legs/trunks/tusks for Gajendra, extra jaws/tails for crocodile, extra wings for Garuḍa, unexpected arm counts for divine forms.
- Avoid unsafe assumptions on running a ComfyUI/GPU test within a GitHub connector. If unavailable label **UNRUN**, not PASS.
- Only non-force commits and pushes to `production-artwork`; verify remote content/tree/branch head after every batch.
- Keep reusable common code compatible with multiple story projects, but change story-specific names/constraints explicitly.

## Milestones

First prove a 60–90-second **lake → danger → inner-prayer** audio animatic. Then build one complete episode and measure each language. The six-episode plan is an initial editorial choice and can be revised after a credible table read; do not pad the story only to hit time.

No media, voices, pipeline code or tests were authored in the setup batch.
