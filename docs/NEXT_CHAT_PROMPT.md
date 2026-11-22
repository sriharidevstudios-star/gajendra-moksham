# COPY INTO NEXT CHAT — GM-ARCH-001

Work on **sriharidevstudios-star/gajendra-moksham**, branch **production-artwork**, draft PR to main. This document is the complete operating prompt for the *next one bounded batch*.

Read `docs/WORK_CHECKPOINT.md`, `docs/CHAT_WORKFLOW.md`, `docs/PRAHLADA_PARITY.md`, `docs/DATA_MODEL.md`, `docs/SOURCE_REGISTER.md`, `seasons/season-01/season.json` and current repository content. Inspect the actual portable schemas and offline build/validator code in `sriharidevstudios-star/prahlada-narasimha` on `production-artwork` via GitHub; do not require a separate local checkout.

**Execute exactly GM-ARCH-001:** adapt the **minimum necessary** six-episode `S01E01–S01E06`, three-language (`te/hi/en`) episode/dialogue source schema and deterministic standard-library offline validation/build scaffolding. Add small synthetic test fixtures in tests (clearly marked **fixture, not canonical story**) and regression tests for episode ID range, unique stable line IDs, scene ownership, complete language mapping, animal narration/voiceover ownership, source citations, and explicit partial-season completeness. Ensure the current planning-only `season.json` does **not** falsely pass as a fully scripted season. Reuse general Prahlada design, not Prahlada story text, 12-episode assumptions, character assets or voice IDs.

Allowed scope: essential `schemas/`, `scripts/`, `tests/`, limited `seasons/season-01/` metadata as necessary for compatibility, and docs checkpoint/handoff. Do **not** author a full canonical episode or change the six-episode plot in this batch; zero image calls and zero generated audio/video. Keep existing planning metadata and character design integrity.

Run Python/stdlib unit tests and source checks if actually runnable; otherwise label exact gates **UNRUN** and include commands for local verification. Make a guarded **non-force** GitHub commit/push, inspect remote files and confirm commit SHA. Update `docs/WORK_CHECKPOINT.md` and `docs/NEXT_CHAT_PROMPT.md` with the exact next bounded **GM-STY-001** story task for `S01E01/S01`. Stop with a short report and **ONE COPY INTO NEXT CHAT** prompt. No routine confirmation.
