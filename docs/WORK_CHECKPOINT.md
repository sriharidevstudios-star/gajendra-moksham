# Work checkpoint — GM-PROD-001

2026-11-22 · production-artwork · draft PR #1 · source HEAD 3abaf19f7da152b8077c95637070340ccb815b0a. Inventory of six live canonical episode JSON sources: 36 scenes, 108 16:9 shots, 296 NARRATOR IDs/888 te/hi/en strings, 1950 unmeasured seconds. All 36 source coverage docs present; read-only consistency checks found no missing IDs/lang, unsafe spoken owners/lip targets or scene/shot sum mismatch. E01 partial and E02–E06 draft-for-table-read, all audio/media and human approvals absent.

**Real approved Library byte inspection DONE:** SHA-256 archive `97231bc30058dce3dff97a36e39c973182fce20ae0d7eb0a2c8e29d81deb8323`, original composite `389568f7590fe2230892c0de3aaafde88f256f4a50e4e4a54ddd65071e4cab06`; exact registry-matching SHA for all nine panel PNGs; 9/9 panels pixel-identical to corresponding crop boxes. Receipt: `assets/artwork/references/GM-PROD-001_BYTE_CHECK.json`. Temporary analysis verification only, NOT durable renderer ingestion/GitHub binary mirror.

Added `docs/GM_PRODUCTION_SOURCE_INVENTORY.md`, `docs/GM_MEDIA_EXECUTION_PLAN.md`, planned `assets/artwork/jobs/GM-KF-001.json` for Narayana-on-Garuda 16:9 hero pair. Rendered images ZERO, approved scene images ZERO. Source, cast and media tracker untouched. Python repository validators/ComfyUI/audio and human review UNRUN.

**Next GM-PROD-002:** real two-reference pixel ingestion into image-conditioned renderer, first start-frame candidate with actual bytes/hash/QC and nonforce commit on success; if binary asset route absent, label missing honestly. Avoid CI polish.
