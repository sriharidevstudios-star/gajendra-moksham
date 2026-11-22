# Season/source status semantics audit — GM-STATUS-001

**Audited:** 2026-11-22  
**Repo:** `sriharidevstudios-star/gajendra-moksham` · branch `production-artwork` · draft PR #1 into `main`  
**Verified starting commit:** `082e0eae6f32256bb124773b85a3b255d173234c` · base Git tree `eac82787781ba91baa2d0117f16509486c3b2602`  
**Scope:** status-field meaning and metadata only; no story, audio, image, pipeline or approval changes. All statements below refer to repository files verified at the starting commit unless explicitly labeled a new decision.

## Decision: one season-index root status corrected; tracker completion flag retained

| Path / field | Previous | Current disposition | Justification |
|---|---|---|---|
| `seasons/season-01/season.json.status` | `planned_only_no_canonical_episode_sources` | **CHANGED to `partial_first_episode_draft_five_sources_missing`** | Live first-episode `episode.json` exists with `partial_scene_draft`, six scenes, 18 editorial shots and 54 trilingual lines. E02–E06 have no authored episode files. Former root label incorrectly asserted zero canonical episode sources. The new descriptive label explicitly retains partial and five-missing qualifiers; it is **not** `READY` or a release/recording approval. |
| `seasons/season-01/season.json.episodes[0].status` | `partial_scene_draft` | **UNCHANGED** | Matches the authored `S01E01/episode.json.status`. The source is not a finalized `draft_for_table_read`. |
| `season.json.episodes[1..5].status` | `planned_no_episode_source` | **UNCHANGED** | No canonical E02–E06 episode sources exist in this Git tree. |
| `seasons/season-01/production_tracker.json.status` | `planning_only` | **UNCHANGED** | Media, casting and production are still planning-only. |
| `production_tracker.json.episodes.S01E01.canonical_story_written` | `false` | **UNCHANGED; ambiguous completion marker** | No schema, validator branch, builder or test in this repo defines whether this Boolean means *any episode text has been authored* or *finalized canonical script*. If the latter, `false` is correct for `partial_scene_draft`. Changing it to `true` without a contract would risk claiming script completion. The JSON source existence and its episode status independently establish partial authorship. |
| `production_tracker.json.episodes[*].te_script_approved`, `hi_script_approved`, `en_script_approved`, `voices_approved`, `recorded_audio_complete`, `visual_references_approved`, `shot_specs_validated`, `keyframes_verified`, `motion_complete`, `final_master_approved` | all `false` | **UNCHANGED** | No human approvals or media evidence exists. `media_files=[]` for all six. |

### Code and test evidence (verified source paths)

- `scripts/content_model.py` `validate_project` reads `season.get("episodes")`, validates each **episode index entry** `status` against `planned_no_episode_source`, `partial_scene_draft`, `draft_for_table_read`, and checks a present episode's `doc.status` matches its index entry. It does **not** read the **top-level** `season.status`, nor `production_tracker.json`. The new root label therefore does **not change this validator's decision logic**.
- `schemas/episode.schema.json` validates an authored **episode's own** `status` with enum `partial_scene_draft | draft_for_table_read`; it does not define the season root or the tracker Boolean. **No season-root status enum/schema or tracker Boolean contract exists in the inspected Git tree**.
- `tests/test_content_model.py` constructs a season index **without a root `status`** and checks index/episode status consistency plus missing sources; `tests/test_runtime_budget.py` likewise checks `SCOPED_READY` for partial, `NOT_READY` for the unfinished season, and the episode-level 330s versus season-level 360s preference. The two tests do not reference `canonical_story_written` or the obsolete root literal.
- `scripts/build_season_dialogue.py` calls `validate_project` and labels a partial source's exports as **PARTIAL SCOPED DRAFT**; it does not use the tracker Boolean to infer a recorded or complete story.
- `docs/DATA_MODEL.md` distinguishes `SCOPED_READY` (requested authored scene/episode structurally valid) from `READY` (six full authoring drafts structurally valid), both separate from audio/native/editorial approval. `NOT_READY` is the current whole-season result expected from E02–E06 absent. The current E01 has six drafted scenes but retains `partial_scene_draft` deliberately.

**External-reader caveat:** The new top-level status label is a descriptive status string, not a new validator enum or a guarantee about unknown third-party consumers. Existing checked-in code does not branch on it. The statuses of individual episodes remain authoritative for source readiness. Do not use a root string alone to enable media, voice casting or publishing.

## Source/production readiness and unaltered evidence

**Authored (not yet approved):** S01E01 `partial_scene_draft`, six scenes / 18 shot descriptions / 54 narration rows, all with te/hi/en text and `NARRATOR` ownership; episode preferred 330s while season working preference is 360s. Six coverage maps plus `docs/S01E01_COVERAGE_RECONCILIATION.md` document source ownership but **do not** prove render, voice or human approval.

**Not authored:** E02–E06 episode sources. **Not approved/produced:** native-language listening, devotional review, casting, voices, recording audio, character/environment reference images, compiled shot specs, actual keyframes, motion or final video. `assets/asset_registry.json` remains empty and the production tracker retains `media_files=[]`.

**Known historical documentation drift outside this batch:** `README.md` still contains initial-setup claims that episode JSON sources and validators are absent. Those claims are stale; update a narrowly scoped introductory document in a later authorized documentation batch rather than rewriting unrelated files in GM-STATUS-001.

## Verification evidence and limits

| Gate | Result |
|---|---|
| In-process exact JSON diff | **PASS**: only `season.json.status` modified; all six per-episode entries, order, source paths and 330–390s range/360s general preference unchanged |
| Episode and index alignment | **PASS**, unchanged E01 `partial_scene_draft`, E02–E06 missing-source markers |
| Static read of validator/schema/builder and tests | **CHECKED**: no checked-in code/test use of the root status or tracker Boolean found; cannot guarantee unknown external tools |
| Production approval and cast/asset states | **UNCHANGED / UNAPPROVED**; no approvals inferred |
| `python3 -m unittest discover -s tests -v` | **UNRUN** — connected GitHub API cannot execute the checked-in Python repository |
| `python3 scripts/validate_content.py --episode S01E01 --scene S06` | **UNRUN** — scoped readiness not claimed as executed |
| `python3 scripts/build_season_dialogue.py --episode S01E01 --scene S06` and `--check` | **UNRUN** — no generated `out/` exports |
| `python3 scripts/validate_content.py` | **UNRUN** — expected `NOT_READY` while E02–E06 sources are missing |
| Human native-language/devotional/voice/art review | **NOT PERFORMED** |

### Exact local Python gate commands

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_content.py --episode S01E01 --scene S06
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S06
python3 scripts/build_season_dialogue.py --episode S01E01 --scene S06 --check
python3 scripts/validate_content.py  # expected NOT_READY, exit 2
```

## Follow-up contract recommendation (not executed in this batch)

A separately scoped status-contract task should decide whether `canonical_story_written` denotes **finalized authored script** (false until explicitly table-read-complete) or **presence of any canonical script file** (true even for partials). Avoid ambiguous reuse for both. If tool consumers need both concepts, introduce an explicit source-presence / editorial-completion distinction *with tests* rather than silently flipping the existing production Boolean.

**Next bounded task: GM-NATIVE-001**, prepare S01E01/S01's first **eight-line Telugu/Hindi/English human table-read packet**, with exact canonical source references, scene/shot budgets and blank measured timings/signoff fields. This is a readiness document only, **not** human listening or voice production. See `docs/NEXT_CHAT_PROMPT.md`.
