# Handoff

## What This Project Is

`accessibility_by_manifest` is a local/open-first document accessibility project. The current v0.1.0 priority is a narrow PDF accessibility workflow that can move from input PDF through evidence collection, accessibility review, structure planning, structure mapping, tagged draft output when legal, validation, human review, review decisions, replanning/remapping when needed, and finalization only when legal.

The repo also contains a broader active manifest-first package for PPTX, PDF, DOCX, review artifacts, and output projections. Do not collapse these two tracks casually.

## What Is Current Right Now

- Planning recovery pass completed on 2026-04-22.
- The project management files in `project-file-structure-md/` have been updated from placeholders into a usable planning baseline.
- The architecture blueprint is complete:
  - shared normalized accessibility contract
  - shared-core PDF and DOCX bridges
  - PDF workflow integration against the shared model
  - shared projection helpers
  - honest PDF finalization path
  - accessible HTML as a sibling output path
  - root-doc alignment
- The repo has a deliberate layered structure:
  - `accessibility_by_manifest/`: shared core
  - `src/pdf_accessibility/`: first integrated PDF workflow vertical
- Full repo tests now pass with `.venv/bin/python -m pytest`: 81 passed.

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

## Cleanup Pass Added Later

- Ran a non-destructive cleanup audit.
- Added:
  - `QUARANTINE/`
  - `CLEANUP-REPORT.md`
- Added explicit boundary markers for historical/reference directories:
  - `archive/README.md`
  - `docs/chats/README.md`
  - `docs/pdf_spec_drafts/README.md`
- Recorded cleanup candidates for:
  - generated run outputs in `test_outputs/`
  - historical/generated outputs in `archive/test_outputs/`
  - duplicated document bundles under `docs/chats/`
  - unclear ownership of `.agents/`
  - the standalone `multi_agent_pdf_tagger_app.jsx` prototype
- No cleanup deletions, moves, renames, or history rewrites were performed.

## What Still Needs Resolution

- Extend the review-decision path beyond document metadata so the real
  `finreport25` loop can address more than the title blocker.
- Decide whether OCR-required pages and table-review outcomes should be handled
  as richer decision inputs, new operator artifacts, or separate remediation
  steps.
- Decide the explicit status of `.agents/` and `multi_agent_pdf_tagger_app.jsx`
  once product workflow hardening is no longer the clearer next value.

## Start Here Next Time

1. Read `project-file-structure-md/PLAN.md`.
2. Read `project-file-structure-md/STATUS.md`.
3. Read `project-file-structure-md/DECISIONS.md`.
4. Read `project-file-structure-md/REVIEW.md`.
5. Read `AGENTS.md`.
6. Inspect the review-decision and artifact path in `src/pdf_accessibility/`.
7. If implementing, start with the next blocker-clearing operator-flow step
   before returning to broad cleanup notes.

## Files To Read First

- `AGENTS.md`
- `project-file-structure-md/PLAN.md`
- `project-file-structure-md/STATUS.md`
- `project-file-structure-md/DECISIONS.md`
- `project-file-structure-md/QUARANTINE/README.md`
- `project-file-structure-md/CLEANUP-REPORT.md`
- `plans/post-architecture-cleanup-and-consolidation.md`
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
- Do not collapse `accessibility_by_manifest/` and `src/pdf_accessibility/` casually; the current decision is layered coexistence, not merge-now.
- Do not use stale node names from older draft specs.
- Do not treat `docs/chats/` or `archive/` as current authority.
- Do not use generated `test_outputs/` as source truth unless the output is explicitly cited as evidence and preferably rerun.
- Do not treat `QUARANTINE/` as a delete-now checklist; it is a manual decision queue.
- Use `.venv/bin/python`, not system Python, for verification.
- A `needs_review` terminal state is acceptable for real v0.1.0 documents.

## Suggested Next Checkpoint

- Trigger: after the workflow can clear at least one non-metadata blocker on a
  real run artifact.
- Purpose: confirm that the human-in-the-loop PDF workflow is progressing from
  metadata handling into richer accessibility remediation.
