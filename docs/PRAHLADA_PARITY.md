# Prahlada parity — verified source architecture, selective reuse

**Reference inspected:** `sriharidevstudios-star/prahlada-narasimha` on `production-artwork`; reference head observed at setup time: `e7cdd9a8e51b9ed53e89be97d84ddeb0a326b137`. This is a reference snapshot, not a linked submodule. Project itself is new.

## Verified architecture to adapt

| Prahlada path/component | Gajendra target | Status |
|---|---|---|
| `seasons/season-01/season.json` | six-episode planned `season.json` | Initialized planning index; episode folders absent |
| `episode.json` and `schemas/episode.schema.json` | six-scene trilingual source and adapted schema | **Missing**, GM-ARCH-001 |
| `scripts/build_season_dialogue.py` | deterministic scripts, recording/TTS and scene manifests | **Missing**, port with adjustments |
| `scripts/validate_content.py` | source/manifest/ID/gate validator | **Missing**, port with tests |
| `assets/character_bible.json` | text-only Gajendra cast and anatomy | Initialized, **unapproved** |
| `assets/shot_spec_policy.json` and `schemas/shot_spec.schema.json` | animal/deity-specific per-frame authoring | Policy notes initialized; schema **missing** |
| `pipeline/shot_specs.py` | per-frame compiler, identity refs and hashes | **Missing** |
| `pipeline/artwork*.py`, `assets/asset_registry.json` | image jobs, provenance, receipts | Empty manual registry; pipeline **missing** |
| `pipeline/a2v.py`, `animate.py`, `comfy.py`, `assemble.py` | motion, optional A2V and final assembly | **Missing** |
| `seasons/season-01/voice_cast.json` | candidate and approved voice maps | Initialized **null/unapproved** |
| Prahlada `.github/workflows` | CI for new offline checks | **Missing** pending working validators |
| source/bible/rights/production docs | Gajendra-specific originals | Initialized in setup |

## Required differences, not simple find-and-replace

1. **Six** episodes are provisionally proposed versus Prahlada's twelve.
2. Gajendra, herd, crocodile and Garuḍa are animals, not extra human-face identities. No mandatory human mouth/lip-sync on elephant or crocodile.
3. The two prior-life identities and corresponding curses are **source distinct**; flashbacks require proper actor/animal-state tracking.
4. Land/water physics, the thousand-year struggle and waterline geography are central.
5. `GAJENDRA_LIBERATED` four-armed form is separate from elephant body; no recycled Prahlada/Narasimha portraits or prompt hashes.
6. Three-language devotional prayer needs special recitation, accurate verse reference and native listening; `NARAYANA` and `GARUDA` must not inherit the Narasimha art cast.
7. All reference code has to be inspected before copying; no existing scripts are claimed runnable here.

## Production learning to retain

Audio-first editing, stable content ownership, explicit shot visibility, single-frame decisions instead of merging insert/reverse compositions, artifact receipts, online/offline gates and small commit-push-verify batches. Keep source edits separate from generated media and document absent resources honestly.
