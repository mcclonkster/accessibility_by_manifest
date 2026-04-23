# Handoff

## What This Project Is

`accessibility_by_manifest` is a local/open-first document accessibility project. The current v0.1.0 priority is a narrow PDF accessibility workflow that can move from input PDF through evidence collection, accessibility review, structure planning, structure mapping, tagged draft output when legal, validation, human review, review decisions, replanning/remapping when needed, and finalization only when legal.

The repo also contains a broader active manifest-first package for PPTX, PDF, DOCX, review artifacts, and output projections. Do not collapse these two tracks casually.

## What Is Current Right Now

- Planning recovery pass completed on 2026-04-22.
- The project management files in `project-file-structure-md/` have been updated from placeholders into a usable planning baseline.
- The repo has two active-looking implementation tracks:
  - `accessibility_by_manifest/`: broad manifest-first pipelines.
  - `src/pdf_accessibility/`: v0.1.0 PDF tagged workflow scaffold.
- Full repo tests passed with `.venv/bin/python -m pytest`: 67 passed.
- `tests/pdf_accessibility/` is the targeted v0.1.0 workflow test suite and passed as part of the full run.

## What Changed In The Last Pass

- Read project-planning instructions and repo-local guardrail skills.
- Inventoried source-relevant repository areas.
- Read project files, top-level docs, design docs, v0.1.0 specs, current code, tests, archive context, and generated run evidence.
- Rewrote:
  - `PLAN.md`
  - `STATUS.md`
  - `TASKS.md`
  - `FINDINGS.md`
  - `HANDOFF.md`
- Added:
  - `DECISIONS.md`
- Updated the shared project-files note to include `DECISIONS.md`.

## What Still Needs Resolution

- Confirm whether `project-file-structure-md/` is the canonical planning location.
- Decide how `accessibility_by_manifest/` and `src/pdf_accessibility/` should relate.
- Fix or ticket the validator/no-draft artifact issue: generated `validator_findings.json` can say the internal validator passed even when no tagged draft exists.
- Decide whether to mark `docs/pdf_spec_drafts/` explicitly as historical/superseded where it conflicts with `AGENTS.md`.

## Start Here Next Time

1. Read `project-file-structure-md/PLAN.md`.
2. Read `project-file-structure-md/STATUS.md`.
3. Read `project-file-structure-md/DECISIONS.md`.
4. Read `AGENTS.md`.
5. If implementing, inspect the specific module named by the task before editing.

## Files To Read First

- `AGENTS.md`
- `project-file-structure-md/PLAN.md`
- `project-file-structure-md/STATUS.md`
- `project-file-structure-md/DECISIONS.md`
- `project-file-structure-md/FINDINGS.md`
- `src/pdf_accessibility/graph/build_graph.py`
- `src/pdf_accessibility/persistence/artifacts.py`
- `src/pdf_accessibility/reducers/apply_events.py`
- `src/pdf_accessibility/writeback/draft_writer.py`

Add others if needed:

- `PROJECT.md`
- `README.md`
- `v0.1.0_plan.md`
- `docs/design/`
- `tests/pdf_accessibility/`

## Traps, Caveats, Or Easy-To-Forget Details

- Do not treat a tagged draft as finalized.
- Do not expand v0.1.0 beyond the frozen supported scope.
- Do not use stale node names from older draft specs.
- Do not treat `docs/chats/` or `archive/` as current authority.
- Do not use generated `test_outputs/` as source truth unless the output is explicitly cited as evidence and preferably rerun.
- Use `.venv/bin/python`, not system Python, for verification.
- A `needs_review` terminal state is acceptable for real v0.1.0 documents.

## Suggested Next Checkpoint

- Trigger: after user review of this planning recovery.
- Purpose: decide planning-file location and package relationship before making README/project-wide edits.
