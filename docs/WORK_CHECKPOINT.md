# Work checkpoint — GM-REF-001: approved visual identity intake

**Date:** 2026-11-22 · repo `sriharidevstudios-star/gajendra-moksham` · `production-artwork` · draft PR #1.

## Owner-approved character lock

- User explicitly approved the **last revised full-body character overview**. Original exact PNG: 1536×1024 / 2,779,513 bytes / SHA-256 `389568f7590fe2230892c0de3aaafde88f256f4a50e4e4a54ddd65071e4cab06`, generation ID `3691b3b1-45ba-4cd1-9331-e954442a810c`.
- Uploaded original unchanged, nine lossless per-character panel crops, provenance JSON and downloadable ZIP to the user's ChatGPT Library `/Gajendra Moksham/References/`. GitHub now records the nine locked character identities and 10 metadata asset entries with individual hashes, dimensions, crop boxes, library-backed paths, owner approval scope and unknown model/seed honestly null.
- **Important binary limitation:** the GitHub connection accepts text/tree blobs but cannot read the model's local image bytes; actual approved PNGs are **not mirrored to GitHub**. Metadata remains publicly readable; downstream pipeline must ingest approved bytes from Library/bundle and verify SHA-256 before image-to-image generation. Do not claim GitHub has approved image bytes.
- User explicitly requested **production first**, so stop allocating routine batches to CI/reviewer-infrastructure polish. Unnamed herd elephants and calves still require dedicated visual references; none was falsely marked approved.
- Original episode S01E01 unchanged, 54 narration lines, six scenes, 18 shot descriptions, 330-second preferred, all human narrator/script approvals remain NOT REVIEWED / NOT APPROVED. No scene keyframes, TTS or motion created by this registry batch.

## Next production batch

**GM-STY-007:** create canonical **S01E02/S01**, “The herd rushes to help,” with exact SB 8.2.28 failed rear-body pull, te/hi/en narrator lines, 3 16:9 source-owned shot specs, continuity of original crocodile grip, still-resolved-later timeline. Update season index from `planned_no_episode_source` to `partial_scene_draft` and root descriptor to reflect **two partial episode sources, four absent**, without promoting script/media/approval. Continue scene by scene rather than reviewer/tooling-only increments. See `docs/NEXT_CHAT_PROMPT.md`.
