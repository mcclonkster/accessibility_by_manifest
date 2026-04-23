# Status

## Current Phase

- Planning recovery and source-of-truth repair.

## Current Overall Status

- The codebase is healthier than the old planning files implied.
- The planning layer was not safe before this pass because `PLAN.md`, `STATUS.md`, `TASKS.md`, `FINDINGS.md`, and `RESEARCH-PLAN.md` were mostly templates.
- The repository has two active-looking code paths:
  - `accessibility_by_manifest/` for the broader manifest-first pipelines.
  - `src/pdf_accessibility/` for the narrow v0.1.0 PDF tagged-draft/finalization workflow.
- The v0.1.0 PDF workflow should use `AGENTS.md` and `src/pdf_accessibility/` as its governing implementation path.

## Current Health

- at risk

Reason: tests pass, but project truth is split across active code, specs, historical docs, generated outputs, and newly created planning files. The main risk is not broken code; it is drift and accidental use of the wrong source as authoritative.

## Verification This Pass

- Inventory covered source-relevant repo areas: `.agents/skills`, `AGENTS.md`, `PROJECT.md`, `README.md`, `v0.1.0_plan.md`, `project-file-structure-md`, `docs/design`, `docs/pdf_spec_drafts`, `accessibility_by_manifest`, `src/pdf_accessibility`, `tests`, `test_inputs`, `test_outputs`, `reference`, and `archive`.
- Full test suite passed with `.venv/bin/python -m pytest`: 67 passed.
- Targeted v0.1.0 workflow tests passed as part of that run: 34 tests under `tests/pdf_accessibility`.
- System `pytest tests/pdf_accessibility` is not reliable because system Python was missing `pikepdf`.

## What Changed Recently

- Intake was corrected to reflect actual repo inspection.
- This planning recovery pass identified the source hierarchy and the dual active implementation tracks.
- The generated `finreport25` workflow run was inspected as evidence: it ends honestly in `needs_review` with no tagged draft and no final output.
- The broader manifest-first `finreport25` output was inspected as evidence: it produces a master PDF manifest, extractor manifests, normalized view, review queue, and draft DOCX review artifact.

## Active Blockers

- Planning location is unresolved: `project-file-structure-md/` is being used, but it is not yet confirmed as the canonical location.
- Dual-track architecture is unresolved: the relation between `accessibility_by_manifest/` and `src/pdf_accessibility/` needs an explicit decision.
- Some older specs use superseded terminology or node names; they cannot be read as current truth without the terminology freeze.
- The generated v0.1.0 `validator_findings.json` can report `"passed": true` even when no tagged draft exists because persistence wrote an empty validator report. This needs a code/test follow-up before validator artifacts are trusted in no-draft runs.

## Open Questions

- Should project management files stay in `project-file-structure-md/` or move to the repo root?
- Should `src/pdf_accessibility/` remain a separate package from `accessibility_by_manifest/`, or should the v0.1.0 workflow eventually be integrated into the manifest-first package?
- Should `docs/pdf_spec_drafts/` be marked explicitly as historical draft material in README or an index file?
- Should generated `test_outputs/` be curated, cleaned, or excluded from planning evidence except when explicitly named?

## Next Planning Moves

1. Review and accept or correct the source hierarchy in `PLAN.md`.
2. Decide the canonical location of project management files.
3. Record the package-relationship decision in `DECISIONS.md`.
4. Turn the validator/no-draft artifact issue into an implementation task.
5. Update README/PROJECT only after the package-relationship decision is made.

## Next Checkpoint

- Trigger: after the user reviews the recovered planning files.
- Purpose: lock the planning-file location and decide how the two implementation tracks should be described.
