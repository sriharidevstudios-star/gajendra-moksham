# Work checkpoint — GM-PROD-003 / GM-KF-001 F01 pose and identity

2026-11-22 · GitHub `sriharidevstudios-star/gajendra-moksham` branch `production-artwork` · draft PR #1. Initial head `1ad5a4d7ac347a53df1a20e0fbc7f4ec7d159fd8`. Scoped to real visual production studies and evidence; canonical script, owner-approved references, source/cast and production tracker unchanged.

**Two actual Library PNGs uploaded and independently roundtrip SHA-verified:**

- Posed generative study: `/Gajendra Moksham/Artwork/Candidates/GM-KF-001-F01-PoseStudy-UNVERIFIED-IDENTITY.png`, 1920×1080, 3,358,286 bytes, SHA-256 `ae77baf29db961cf5e7b4eb1e4340b2467a825d90ef414cd773f1449cf1c4f96`; shows Nārāyaṇa convincingly mounted on flying Garuḍa, but Garuḍa's original golden humanoid bird head/dark hair are replaced by a white-headed eagle form and style drift. Tool did not return verifiable source-image-conditioning lineage; this is a pose concept ONLY, not owner-approved character art.
- Direct pixel geometry study: `/Gajendra Moksham/Artwork/Candidates/GM-KF-001-F01-ApprovedPixels-WarpStudy-UNAPPROVED.png`, 1920×1080, 1,443,689 bytes, SHA-256 `d3eb3ee7c5016017ec831b9fb01c9647b894d5cf7a86979611762549b72fe8fc`; uses actual SHA-verified Narayana/Garuda PNG pixel mattes with rotated flight geometry, but Nārāyaṇa looks like he is standing on a wing rather than seated. Source identities are protected but seating still FAILS.

Exact SHA/reference input/output/method limitations and BOTH persistent Library IDs are recorded in `assets/artwork/receipts/GM-PROD-003_GM-KF-001-F01-pose-studies.json`. Neither image is canonical `F01`, neither is in GitHub as a binary PNG; actual human art approval **NOT_REVIEWED**. `assets/artwork/jobs/GM-KF-001.json` keeps `actual_outputs.start_frame=null`, `end_frame=null`, motion null. The first-frame identity and pose gates are still OPEN. F02, narration, motion and final video remain MISSING.

**Next GM-PROD-004:** use an image-model workflow with provable reference-conditioned source pixels or an artist-grade re-pose with the actual approved golden Garuḍa and exact 4-arm Nārāyaṇa identity, natural seated flight and 16:9 compositional continuity. Produce ONE new source-credible candidate, verify media bytes, obtain explicit human art-QC; do NOT claim approval or generate motion based on this rejected study. No generic CI changes.
