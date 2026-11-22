# S01E01 native-review CI gate — GM-NATIVE-011

**Prepared:** 2026-11-22 · repo `sriharidevstudios-star/gajendra-moksham` · branch `production-artwork` · draft PR #1 targeting `main`.  
**Workflow:** [`.github/workflows/native-review-evidence.yml`](https://github.com/sriharidevstudios-star/gajendra-moksham/blob/production-artwork/.github/workflows/native-review-evidence.yml). This is a workflow definition, **not a claim of any executed CI pass or human review**.

## Baseline inspection and workflow scope

- Verified pre-batch GitHub commit `f290c72a0bb2ea71273a896f210c309f27d99572` and nontruncated tree `0c63758cafa8defc8f968d5454de481af91f3d3c`: **no existing `.github/workflows/` paths**, no tracked media files, and no human-review evidence receipts.
- The connected GitHub `actions/workflows` collection and Actions permissions endpoints were not accessible through the available public-resource fetch interface. An `actions/runs` repository listing was accessible and returned **0 prior runs** at baseline. This does **not** prove Actions are enabled, that the new workflow can execute, or that the token has `workflow`/Actions write permission.
- Proposed workflow uses read-only `contents: read` permission on `ubuntu-latest`, `actions/checkout@v4`, `actions/setup-python@v5` with Python **3.10**, no pip installation or untrusted scripts beyond the repository's checked-in standard-library validators/tests.
- Triggers: push to `production-artwork`, pull requests to `main`, or manual dispatch after GitHub registers the workflow; path filters cover the workflow file, code/tests, season sources, assets, future review evidence and the evidence contract.
- All workflow steps run **without** an actual review receipt in the current tree. A future genuine receipt would change the expected `NOT_REVIEWED` state and require a separate reviewed update to this gate; no receipt is fabricated here.

## Exact expected commands and exit/status checks

| Check | Command or method | Expected result | What this does **not** authorize |
|---|---|---|---|
| Existing and synthetic tests | `python3 -m unittest discover -s tests -v` | Exit **0** only if tests really pass | Human or media approval |
| Current missing human receipt | `python3 scripts/validate_native_review_evidence.py` | Exit **2**, JSON `status=NOT_REVIEWED`, `approved=false`, `reviewed_roles=[]` | Script or narrator approval |
| Valid scoped S01E01/S06 text | `python3 scripts/validate_content.py --episode S01E01 --scene S06` | Exit **0**, JSON `status=SCOPED_READY` | Finished episode, measured audio, source signoff |
| Incomplete whole season | `python3 scripts/validate_content.py` | Exit **2**, JSON `status=NOT_READY` | Release readiness |

A nonzero result is **intentionally expected** in the review and whole-season gates, but only with their matching JSON status. The workflow's Python assertion step rejects a mismatched exit code, missing JSON, unexpected status, or human approval claim. GitHub Actions must actually launch the job and record logs before any test can be labeled **PASS**.

## Finding and trusting real CI evidence

In GitHub, open [Actions](https://github.com/sriharidevstudios-star/gajendra-moksham/actions), select **Native review evidence and source checks**, choose the run corresponding to the exact production-artwork commit, and inspect the **Python 3.10 synthetic and source gates** job. The trusted evidence minimum is:

1. Workflow run ID, exact `head_sha`, trigger (`push` or `pull_request`), runner version and job status/conclusion.
2. Recorded full `unittest` step log (number of executed tests, failures/errors and exit).
3. Captured script stdout showing `NOT_REVIEWED` and `approved=false` for missing receipts, `SCOPED_READY` for E01/S06, and `NOT_READY` for the unfinished season.
4. An actual **completed-success** conclusion for this commit's run before saying CI passed. `queued`, `in_progress`, `skipped`, absent, or inaccessible run data **is not PASS**. Tests remain **UNRUN / not verified** until evidence is observed.

For another authorized checkout the commands above may be run manually, but do not present their predicted states as measured GitHub Actions results.

## Known limitations and gate boundaries

- The workflow file exists only if GitHub accepts a guarded non-force update under `.github/workflows/`; this file's authoring alone never proves workflow registration or execution.
- Repo `production-artwork` is a draft PR; `main` remains unchanged. The read-only job cannot push, modify production trackers, set script/voice approvals, create media or authenticate real reviewer identities.
- All 54 source narration lines, six scenes, 18 shots and E01 **330-second preferred editorial budget** remain a `partial_scene_draft`; S01E02–S01E06 sources remain absent. Human te/hi/en and devotional review remains **NOT REVIEWED / NOT APPROVED**, voice-cast and assets empty, full season **NOT_READY**.
- If Actions are disabled, workflow permissions are missing, jobs cannot launch, or the run/logs are inaccessible, record the concrete API/UI error or missing run as a blocker. Never report a green result or fabricate run IDs.
- No images, TTS, audio, video, motion or actual reviewer receipts have been generated or approved in this batch.

**Next candidate bounded task:** GM-NATIVE-012 — verify an actual GitHub Actions run/steps/logs for the new workflow and triage any observed failure only; do not automatically advance human-review or production readiness.
