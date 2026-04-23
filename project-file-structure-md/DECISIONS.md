# Decisions

## Decision Log

### 2026-04-22: Use `AGENTS.md` As The Governing v0.1.0 PDF Workflow Source
- Decision: For v0.1.0 PDF tagged workflow work, `AGENTS.md` supersedes older draft specs and historical chat/archive material.
- Rationale: `AGENTS.md` contains the current frozen scope, terminology, node names, architecture rules, artifact rules, and definition of done.
- Consequence: Older draft-spec names and superseded decision wording must be translated through the terminology freeze before use.

### 2026-04-22: Treat `src/pdf_accessibility/` As The Current v0.1.0 Tagged PDF Workflow Implementation
- Decision: Planning for tagged draft output, validator checks, human review, review decisions, and finalization gating should use `src/pdf_accessibility/` and `tests/pdf_accessibility/` as implementation evidence.
- Rationale: This package matches the `AGENTS.md` module boundaries and has targeted tests for workflow state, reducers, transition guards, artifacts, writeback, validation, review decisions, and graph routing.
- Consequence: The broader `accessibility_by_manifest/` package remains active but should not be mistaken for the v0.1.0 finalization workflow unless a future decision merges the tracks.

### 2026-04-22: Treat `accessibility_by_manifest/` As Active Broader Manifest-First Infrastructure
- Decision: Do not archive or ignore `accessibility_by_manifest/`.
- Rationale: It has current code and passing tests for PPTX/PDF/DOCX manifest pipelines, normalization, review artifacts, DOCX/Markdown outputs, Adobe reference comparison, and optional sidecar evidence.
- Consequence: Future planning must explicitly decide whether this package feeds `src/pdf_accessibility/`, remains parallel, or is gradually integrated.

### 2026-04-22: Use `.venv/bin/python` For Verification
- Decision: Verification commands should use the repo-local virtual environment.
- Rationale: System Python failed targeted test collection because `pikepdf` was missing; `.venv/bin/python -m pytest` passed the full test suite.
- Consequence: Status reports should cite `.venv/bin/python -m pytest`, not bare `pytest`, unless the environment is known.

### 2026-04-22: Keep `project-file-structure-md/` As The Temporary Planning Location
- Decision: Update the existing project files in `project-file-structure-md/` for this recovery pass.
- Rationale: The files already existed there, and moving them would be a separate repository-structure decision.
- Consequence: This is temporary pending user/project confirmation. If the repo root should contain these files, move them deliberately in a later pass.

## Decisions Still Needed

- Whether `project-file-structure-md/` becomes canonical or moves to repo root.
- Whether `accessibility_by_manifest/` and `src/pdf_accessibility/` remain separate, merge, or become layered.
- Whether `docs/pdf_spec_drafts/` needs an explicit historical index warning.
- Whether generated `test_outputs/` should be curated, regenerated, or ignored by default for planning.
