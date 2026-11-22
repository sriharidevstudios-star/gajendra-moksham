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

## GM-NATIVE-012 — verified execution evidence (2026-11-22)

**Evidence source:** independently re-read GitHub's repository Actions run list, both completed job/step summaries, and the **full remote job logs** for the **same exact workflow/source commit `c06f03b59054449a84fb341d03214706f1e40da3`**. These are real executed results, unlike the pre-run predictions in the original sections above. **Draft PR #1 remains open**. No workflow or code was edited in this documentation batch.

| GitHub Actions run | Trigger | Job ID / job name | Workflow `head_sha` | Final run and job conclusion |
|---|---|---|---|---|
| [45062106563](https://github.com/sriharidevstudios-star/gajendra-moksham/actions/runs/45062106563) | `push` | `137330104938` — Python 3.10 synthetic and source gates | `c06f03b59054449a84fb341d03214706f1e40da3` | **completed / success** |
| [45062106660](https://github.com/sriharidevstudios-star/gajendra-moksham/actions/runs/45062106660) | `pull_request` | `137330104680` — Python 3.10 synthetic and source gates | `c06f03b59054449a84fb341d03214706f1e40da3` | **completed / success** |

**Run metadata:** Both are first attempts (`run_attempt=1`), created **2026-11-22 19:40:41 UTC**. Push run completed by **19:40:54 UTC**; PR run completed by **19:40:57 UTC**. GitHub recorded successful checkout, setup-python, regression and explicit-status assertion steps in both jobs. Python environment log includes **Python 3.10.22**.

### Actual test output and exact expected status pairs

| Observed evidence (both job logs) | Push run | PR run |
|---|---|---|
| `python3 -m unittest discover -s tests -v` | **53/53 tests, OK**, 0.207 seconds | **53/53 tests, OK**, 0.584 seconds |
| `test_content_model` source tests | **24/24** logged `ok` | **24/24** logged `ok` |
| `test_native_review_evidence` synthetic tests | **21/21** logged `ok` | **21/21** logged `ok` |
| `test_runtime_budget` tests | **8/8** logged `ok` | **8/8** logged `ok` |
| `scripts/validate_native_review_evidence.py` | JSON `NOT_REVIEWED`, `approved=false`, exit **2** | Same, exit **2** |
| Scoped `S01E01/S06` content validator | JSON `SCOPED_READY`, exit **0** | Same, exit **0** |
| Whole-season content validator | JSON `NOT_READY`, exit **2** | Same, exit **2** |
| Explicit assertion-step conclusion | **success**, `NO HUMAN APPROVAL inferred` | **success**, `NO HUMAN APPROVAL inferred` |

**Independent log verification:** Both full logs include actual `Ran 53 tests ... OK` output and all three **`CONFIRMED:`** lines with the exact expected exit/status pairs. The validator's JSON includes `approved: false` and no recorded reviewer roles. The exit code **2** is expected for missing real human-review receipts and an unfinished season; the workflow deliberately verifies these conditions rather than treating them as a full episode or season-ready signoff.

**Verified nonblocking runner warning, not a failed gate:** Both logs report **“Node.js 20 is deprecated”**; the runner forces `actions/checkout@v4` and `actions/setup-python@v5` to Node.js 24. The warning did **not** fail either run. A separately scoped, source-verified action-version maintenance task is appropriate; GM-NATIVE-012 does not change working CI based on warning text alone.

**What this proves:** The Python tests and three explicit source/evidence checks **executed and passed for commit `c06f03b59054449a84fb341d03214706f1e40da3`**, on two real jobs with run IDs and logs. The results must **not** be automatically generalized to a later commit, a new workflow version, a human-read performance, a reviewed translation, an approved narrator, artwork, motion, a finished episode, or publication.

**Current production truth (unchanged):** S01E01 `partial_scene_draft` contains **54 lines, six scenes, 18 shots, 330s preferred editorial budget**. E02–E06 canonical sources are missing; season status `partial_first_episode_draft_five_sources_missing`. Native te/hi/en and devotional sessions remain **NOT REVIEWED / NOT APPROVED**; narrator candidates absent; audio, keyframes, motion, video and media master **MISSING**; all relevant production tracker approval fields remain false. A green CI source check is not human or media approval.

**Document-only commit caveat:** Adding this evidence section to the runbook, checkpoint and next prompt does **not** alter the passing workflow, tests or source files. The configured path filters do not by themselves require a new Actions run for these three documentation-only changes. The two success runs above refer strictly to `c06f03b59054449a84fb341d03214706f1e40da3` and should be cited with that SHA, not silently assigned to this later evidence-recording commit.

## GM-NATIVE-013 — official Node.js 24 action-version migration (2026-11-22)

**This section records a verified official-release decision and workflow edit; GitHub Actions passing status must be checked against the *new resulting commit* before it can be claimed.** No story, human-review, approval, validator or media change is part of this maintenance batch.

### Evidence for supported new major versions

- **GitHub's Node 20 retirement notice** ([2026-09-23 changelog](https://github.blog/changelog/2026-09-23-node-20-is-no-longer-available-in-github-actions/)) says hosted Actions now use **Node 24** for JavaScript actions; the temporary Node 20 opt-out has ended. The previous GM-NATIVE-011/012 logs showed Node 20 deprecation for the older versions, while the 53-test suite passed.
- **Checkout:** official [`actions/checkout` releases](https://github.com/actions/checkout/releases/tag/v7.0.1) show v7.0.1 latest as checked on 2026-11-22 (published 2026-07-20), and the `v7` Git ref resolved to `3d3c42e5aac5ba805825da76410c181273ba90b1`. Official [`v7/action.yml`](https://github.com/actions/checkout/blob/v7/action.yml) states `runs.using: node24`.
- **Setup Python:** official [`actions/setup-python` releases](https://github.com/actions/setup-python/releases/tag/v7.1.0) show v7.1.0 latest as checked on 2026-11-22 (published 2026-10-22), and the `v7` Git ref resolved to `6d4fd22b20465ccc0f7354476588e8df7c9ca0e0`. Official [`v7/action.yml`](https://github.com/actions/setup-python/blob/v7/action.yml) states `runs.using: node24`, while the [README](https://github.com/actions/setup-python#readme) retains `python-version` and documents the Node 24 major transition and runner minimum **v2.327.1**.

### Exactly two changes to the CI workflow

| Field | Prior | Updated |
|---|---|---|
| Checkout action | `actions/checkout@v4` | **`actions/checkout@v7`** |
| Python action | `actions/setup-python@v5` | **`actions/setup-python@v7`** |

No other YAML character or logic changed. The job remains **Python 3.10**, `contents: read`, full `python3 -m unittest discover -s tests -v`, and exact status/exit assertions for absent human evidence `NOT_REVIEWED`/2 with `approved=false`, S01E01/S06 text `SCOPED_READY`/0 and whole season `NOT_READY`/2. Upgrading Node-based action wrappers **does not upgrade Python** or authorize publishing.

### Evidence gate still required after the edit

The existing GM-NATIVE-012 evidence (push `45062106563`, PR `45062106660`, and later PR `45062666676`) proves older workflow revisions passed. **It does not prove the new v7 action references work.** Require a new run ID at the new source commit, completed-success job, 53/53 tests and three expected `CONFIRMED:` outputs from actual logs. Also verify the prior Node 20 deprecation warning is absent, or record any remaining warning precisely.

Until independent post-push verification, call the new-run status **UNVERIFIED/UNRUN**, not PASS. Regardless of automated test outcome, **native-language/devotional review is NOT REVIEWED / NOT APPROVED, all casting/media absent, E01 remains partial and the six-episode season NOT_READY**.
