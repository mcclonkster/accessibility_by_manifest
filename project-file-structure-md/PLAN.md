# Plan

## Project Purpose

`accessibility_by_manifest` is a local/open-first document accessibility project with two active-looking implementation tracks that must be managed deliberately:

- `accessibility_by_manifest/`: manifest-first evidence pipelines for PPTX, PDF, DOCX, review artifacts, DOCX/Markdown projections, Adobe reference comparison, and optional local sidecar evidence.
- `src/pdf_accessibility/`: the narrow v0.1.0 PDF accessibility workflow scaffold required by `AGENTS.md`, with shared state, typed events, reducers, transition guards, workflow orchestration, tagged draft writeback, validator checks, human review, review decisions, and finalization gating.

For current v0.1.0 PDF remediation work, the authoritative product goal is the `src/pdf_accessibility/` workflow path:

```text
input PDF
-> evidence collection
-> accessibility review
-> structure planning
-> structure mapping
-> tagged draft output when legal
-> validation
-> human review
-> review decisions
-> replanning / remapping when needed
-> finalization only when legal
```

The workflow must terminate honestly as `finalized`, `needs_review`, or `write_blocked`.

## Planning Source Hierarchy

Use this order when sources disagree:

1. `AGENTS.md` governs v0.1.0 PDF workflow scope, terminology, node names, artifact rules, and architecture constraints.
2. `src/pdf_accessibility/` and `tests/pdf_accessibility/` show the current implementation reality for the v0.1.0 tagged PDF workflow scaffold.
3. `v0.1.0_plan.md` gives the practical build sequence for the v0.1.0 PDF workflow.
4. `project-file-structure-md/*.md` are the planning, status, task, findings, decision, and handoff files after this recovery pass.
5. `PROJECT.md`, `README.md`, and `docs/design/` describe the broader manifest-first project and the active `accessibility_by_manifest/` package.
6. `docs/pdf_spec_drafts/` are useful design history, but older names or superseded decision wording are superseded by `AGENTS.md` and the terminology freeze.
7. `docs/chats/` and `archive/` are historical context only unless a current plan explicitly promotes a point from them.
8. `test_outputs/` are evidence of previous runs, not source of truth.

## Scope In

- Make the v0.1.0 PDF workflow executable, honest, and testable for born-digital, mostly single-column PDFs.
- Preserve shared-state workflow architecture: nodes emit typed events; reducers apply state changes; transition guards decide legality; the workflow orchestrator routes from shared state.
- Keep writeback, validation, human review, review decisions, replanning/remapping, and finalization gating first-class.
- Maintain the `accessibility_by_manifest/` package as the existing manifest-first evidence pipeline unless a later decision explicitly merges or retires it.
- Use generated outputs and tests as evidence when updating project status, but do not let generated outputs override code/spec truth.

## Scope Out

- Do not broaden v0.1.0 into forms, dedicated links workflow, logical tab order for interactive content, formulas, complex charts, complex multi-column layouts, difficult scanned documents, advanced multilingual handling, or broken existing tag-tree reuse.
- Do not claim `accessible_output.pdf` exists or is final unless finalization is legal.
- Do not treat the older `docs/chats/` PDF.js/JavaScript branch as governing the current Python/LangGraph implementation.
- Do not treat `archive/` scripts as active implementation.

## Current Reality

- Full repo verification passed with `.venv/bin/python -m pytest`: 67 tests passed.
- `tests/pdf_accessibility/` passed: 34 tests covering artifact contracts, validator checks, reducers, review decisions, review thresholds, structure mapping, tagged draft writer, transition guards, and workflow routing.
- `src/pdf_accessibility/` has the expected module boundaries from `AGENTS.md`.
- `accessibility_by_manifest/` has active code and tests for PPTX, PDF, DOCX, normalization, review, output projections, Adobe comparison, and optional local AI/OCR sidecars.
- `test_outputs/pdf_accessibility_runs/finreport25_20260422T115228Z/` shows a real 117-page PDF workflow run ending in `needs_review` with 1328 normalized units, 269 review tasks, 222 unresolved blockers, no tagged draft, and no final output.
- `test_outputs/finreport25_manifest_output/` shows the manifest-first PDF pipeline processing `finreport25.pdf` into a v0.1 master manifest, extractor manifests, normalized view, review queue, and draft DOCX review artifact.

## Milestones

### Milestone 1: Planning Recovery Baseline
- Outcome: Planning files reflect the actual repository instead of placeholders.
- Acceptance criteria:
  - `PLAN.md`, `STATUS.md`, `TASKS.md`, `FINDINGS.md`, `DECISIONS.md`, and `HANDOFF.md` agree.
  - The dual-track implementation reality is explicit.
  - Source hierarchy and supersession rules are explicit.
- Dependencies: repo inventory, specs, implementation inspection, generated-output inspection, full test run.
- Risks: planning docs may still miss details hidden in untracked/generated artifacts.
- Expected checkpoint output: current project management files can be used as the first planning source after `AGENTS.md`.

### Milestone 2: Reconcile Active Implementation Tracks
- Outcome: Decide how `accessibility_by_manifest/` and `src/pdf_accessibility/` should relate.
- Acceptance criteria:
  - One documented decision says whether they remain separate, merge gradually, or one becomes legacy.
  - CLI names and README guidance make the distinction clear.
  - Tests continue to pass for both tracks.
- Dependencies: current package layout, `pyproject.toml`, README, workflow specs.
- Risks: accidental duplicate concepts, two sources of truth for PDF evidence, user confusion.
- Expected checkpoint output: updated decision record and any required README/project doc edits.

### Milestone 3: Stabilize v0.1.0 Workflow Spine
- Outcome: The `src/pdf_accessibility/` workflow reliably produces required JSON artifacts and honest terminal states.
- Acceptance criteria:
  - Required artifacts are registered and written for every run.
  - `tagged_draft.pdf` appears only when draft write is legal.
  - `accessible_output.pdf` appears only when finalization is legal.
  - `validator_findings.json` does not imply a nonexistent draft passed validation.
  - Reopen/replanning path after review decisions is explicit.
- Dependencies: reducers, transition guards, persistence, graph routing, writeback, validator.
- Risks: current persistence writes validator status even when no draft was validated; review-decision routing is still minimal.
- Expected checkpoint output: targeted tests for terminal states, draft/no-draft validator reporting, and review-decision reroute.

### Milestone 4: Improve Narrow Normalization And Review
- Outcome: v0.1.0 normalization and review tasks are useful enough for mostly single-column born-digital PDFs.
- Acceptance criteria:
  - Headings, paragraphs, lists, simple tables, repeated headers/footers/page numbers as artifacts, basic figures, title, and primary language are handled within the stated scope.
  - Review tasks are meaningful and not just a dump of uncertainty.
  - Complex table and figure blockers remain honest.
- Dependencies: deterministic evidence extraction, region proposal, artifact check, accessibility review, structure mapping.
- Risks: `finreport25` shows many table/review blockers; scope pressure toward complex financial tables is high.
- Expected checkpoint output: updated tests and at least one run summary showing fewer noisy review tasks without unsafe finalization.

### Milestone 5: Tagged Draft And Validation Hardening
- Outcome: The draft writer and internal validator support tiny/simple H/P cases reliably and fail honestly elsewhere.
- Acceptance criteria:
  - Document title and primary language are written when ready.
  - MarkInfo, StructTreeRoot, marked content, MCIDs, and ParentTree are written for supported simple H/P cases.
  - Unsupported tables, figures, lists, annotations, links, and complex content streams block finalization rather than being silently skipped.
  - `writeback_report.json` clearly separates planned, written, skipped, and unsupported writeback.
- Dependencies: structure mapping plan, MCID planning, ParentTree planning, marked content writer, internal validator.
- Risks: full PDF/UA-grade writeback remains outside current implementation; external veraPDF is deferred.
- Expected checkpoint output: expanded writer/validator tests and documented limitations in artifacts.

### Milestone 6: Human Review Loop
- Outcome: Review decisions can resolve simple blockers and trigger replanning/remapping when needed.
- Acceptance criteria:
  - `review_decisions.json` template is usable.
  - Title/language/alt-text/decorative-figure decisions resolve eligible tasks.
  - Non-resolvable blockers remain blocked.
  - Structure mapping reruns after decisions that affect document properties or readiness.
- Dependencies: reducer review-decision logic, apply-review node, graph routing, persistence.
- Risks: current workflow loads file-based decisions but has limited reroute behavior.
- Expected checkpoint output: review-decision loop tests and a sample run applying decisions.

## Risks

- Dual active packages can create conflicting project truth.
- Old spec drafts contain superseded terms and old node names.
- Generated outputs include useful evidence but can become stale quickly.
- `test_outputs/` is large and should not be treated as curated documentation.
- Full accessibility finalization is not proven by internal tests.
- System Python may not have required dependencies; use `.venv/bin/python`.

## Dependencies

- Required Python packages in `pyproject.toml`: `langgraph`, `pydantic`, `PyMuPDF`, `pikepdf`, `pypdf`, `pdfminer.six`, `typer`, plus the broader manifest pipeline dependencies.
- Optional sidecars in current broader package: Docling and doctr paths are present but must remain evidence-only unless explicitly promoted.
- External veraPDF is deferred for v0.1.0.

## Next Checkpoint

- Trigger: after the planning recovery files are reviewed.
- What should be true: either accept `project-file-structure-md/` as the current planning-doc location or decide to move these files to the repository root before further planning depends on them.
