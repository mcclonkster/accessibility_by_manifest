# Tasks

## Active

- [x] Task: Recover planning baseline from actual repository state
  - Owner: Codex
  - Next action: user review of recovered planning files
  - Notes: Inspected docs, code, tests, generated outputs, archive context, and repo-local skills. Full repo test suite passed in `.venv`.

## Blocked

- [ ] Task: Declare project management file location canonical
  - Blocker: user/project decision needed
  - What is needed: decide whether `project-file-structure-md/` remains canonical or whether `INTAKE.md`, `PLAN.md`, `STATUS.md`, `TASKS.md`, `FINDINGS.md`, `DECISIONS.md`, and `HANDOFF.md` should move to the repository root.
  - Notes: Current pass updates files in `project-file-structure-md/` because that is where the existing file set lives.

- [ ] Task: Decide package relationship
  - Blocker: architecture decision needed
  - What is needed: decide whether `accessibility_by_manifest/` and `src/pdf_accessibility/` remain separate, merge gradually, or one becomes legacy.
  - Notes: Both are active-looking and tested. `AGENTS.md` governs v0.1.0 tagged PDF workflow work.

## Waiting

- [ ] Task: Update README/PROJECT to match planning recovery
  - Waiting on: package-relationship decision
  - Expected trigger: after `DECISIONS.md` records how the two implementation tracks relate
  - Notes: Editing README first would risk turning an unresolved architecture question into accidental truth.

## Next

- [ ] Task: Create implementation issue for validator/no-draft reporting
  - Why next: generated `validator_findings.json` can say `passed: true` when no tagged draft exists; this undermines artifact trust.
  - Notes: This belongs in `src/pdf_accessibility/persistence/artifacts.py` and related tests, not in planning docs.

- [ ] Task: Add explicit historical marker for superseded draft specs
  - Why next: old docs contain stale node names and superseded decision wording that conflicts with `AGENTS.md`.
  - Notes: Could be a short index note in `docs/pdf_spec_drafts/` or README language.

- [ ] Task: Add a sample review-decision loop run
  - Why next: review decisions exist in reducers and tests, but an end-to-end sample would make the workflow easier to trust.
  - Notes: Keep v0.1.0 narrow; do not imply finalization if blockers remain.

## Done

- [x] Task: Read project-planning skill
  - Completed on: 2026-04-22
  - Notes: Used to repair `PLAN.md`, `STATUS.md`, `DECISIONS.md`, and `HANDOFF.md`.

- [x] Task: Read repo-local workflow guardrails
  - Completed on: 2026-04-22
  - Notes: Used `pdf-workflow-state`, `pdf-writeback-output`, and `terminology-scope-check`.

- [x] Task: Run full repo tests
  - Completed on: 2026-04-22
  - Notes: `.venv/bin/python -m pytest` passed 67 tests.

## Resume Notes

- If restarting, do this first: read `PLAN.md`, `STATUS.md`, `DECISIONS.md`, and `HANDOFF.md` from this folder.
- Re-open these files first: `AGENTS.md`, `src/pdf_accessibility/graph/build_graph.py`, `src/pdf_accessibility/persistence/artifacts.py`, `PROJECT.md`, `README.md`.
- Watch out for: stale draft-spec terminology, generated output that is useful but not authoritative, and accidental expansion beyond v0.1.0.
