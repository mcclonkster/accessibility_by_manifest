# Research Plan

## Research Question

- No external research question is active for the immediate planning recovery.

## Why This Matters

- The current uncertainty is internal project reconciliation, not missing outside evidence.

## Scope

- Internal follow-up research should focus on the cleanest reuse/interface boundary between `accessibility_by_manifest/` and `src/pdf_accessibility/` under the newly chosen layered relationship.
- If implementation work begins, inspect the specific modules and tests named by the task.

## Exclusions

- Do not reopen broad tool-selection research unless a concrete implementation blocker requires it.
- Do not use old chat transcripts as current authority without checking current code and `AGENTS.md`.

## Source Types To Check

- Current code under `accessibility_by_manifest/` and `src/pdf_accessibility/`
- Current tests under `tests/`
- Current design docs under `docs/design/`
- Current workflow constraints in `AGENTS.md`

## Evidence Threshold

What counts as enough evidence for a planning decision?

- A decision should cite at least one current spec or design doc and at least one current implementation or test source when it affects code direction.

## Subquestions

### Subquestion 1
- Question: Should the v0.1.0 PDF workflow remain in `src/pdf_accessibility/` or become part of `accessibility_by_manifest/`?
- Why it matters: This determines README guidance, CLI guidance, package boundaries, and where future work should land.

### Subquestion 2
- Question: Which evidence from the broader PDF manifest pipeline should feed the v0.1.0 shared-state workflow?
- Why it matters: The broader pipeline extracts more deterministic evidence than the current v0.1.0 scaffold, but integration must not blur reducer/node boundaries.

## Open Uncertainties

- Canonical location for project management files.
- Package relationship between the two active implementation tracks.
- Whether generated output fixtures should be curated or rebuilt.

## Planned Output

- A future decision entry in `DECISIONS.md`, followed by any required `README.md`, `PROJECT.md`, or module-boundary updates.

## Stop Point For This Pass

- Stop when the planning files are internally consistent and the next decision point is explicit.
