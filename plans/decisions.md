# Decisions

## Decision Log

### 2026-04-25: Centralize Architecture And Pipeline Reference In One Canonical Design Doc
- Decision: `docs/design/system_reference.md` is the single canonical architecture/reference document for the umbrella system.
- Rationale: The repo had drifted across multiple overlapping summaries: `README.md`, `PROJECT.md`, `project_intent.md`, `manifest_design.md`, `library_and_architecture_decisions.md`, and later plan language. That overlap kept reintroducing the wrong mental model. One canonical reference reduces conceptual drift while preserving narrower companion docs for intent, manifest design, library choices, and PDF-specific details.
- Consequence: `README.md` and `PROJECT.md` should point back to `docs/design/system_reference.md` instead of behaving like competing architecture explainers. Other design docs should remain narrower companion references rather than parallel top-level summaries.

### 2026-04-25: Reduce The Active Guidance Surface To A Minimum Set
- Decision: The active guidance surface should be limited to `docs/design/system_reference.md`, `AGENTS.md`, `README.md`, `plans/README.md`, `plans/start-to-finish-product-plan.md`, `plans/status.md`, `plans/tasks.md`, and `plans/decisions.md`, with `manifest_design.md` and `pdf_pipeline_decisions.md` as supporting technical companions.
- Rationale: Too many overlapping guidance files were still acting current at once, especially `PROJECT.md`, `PLAN.md`, `HANDOFF.md`, and older blueprint/control docs. That redundancy was actively causing conceptual drift and wasted navigation effort.
- Consequence: Stale guidance files were moved into `quarantine/project-guidance/`. Supporting docs are now labeled explicitly, and the active control/index files should stop pointing contributors at the quarantined set.

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

### 2026-04-26: Move Planning Control Into `plans/`
- Decision: Use `plans/` as the canonical planning, status, task, cleanup, and decision location.
- Rationale: The prior custom planning folder name made the repo look less professional and harder for future agents to navigate. Standard repo practice is to keep active plans under a clear `plans/` directory and historical material under a clear archive/quarantine surface.
- Consequence: Active tracking files are now `plans/status.md`, `plans/tasks.md`, `plans/decisions.md`, and `plans/cleanup-report.md`. The old project-guidance material is quarantined under `quarantine/project-guidance/`.

### 2026-04-24: Treat Generated Pipeline Run Outputs As Local Verification Artifacts By Default
- Decision: Newly generated run directories under `test_outputs/` should be ignored by default unless a specific output is deliberately curated as a fixture.
- Rationale: A generated manifest exceeded GitHub's 100 MB limit and blocked push even after later deletion from the working tree because the blob remained in local history. Casual tracking of run outputs creates repo-noise and push risk.
- Consequence: The repo now ignores `test_outputs/finreport25_manifest_run/` and `test_outputs/finreport25_workflow_runs/`. Existing tracked output artifacts still need a later review to decide what remains curated versus what should be removed from git.

### 2026-04-25: Treat Current `finreport25` Run Directories As Disposable Local Verification, Not Curated Fixtures
- Decision: The current `test_outputs/finreport25_manifest_run/` and `test_outputs/finreport25_workflow_runs/` directories should be treated as disposable local verification artifacts, not as curated fixtures to preserve in git.
- Rationale: The repo now ignores both paths, local reruns are already accumulating there, and the tracked state is visibly inconsistent: older workflow artifacts are deleted while newer reruns exist only locally. That is strong evidence that these directories are operational run output, not canonical regression fixtures. The only output surface that still plausibly behaves like intentionally curated fixture material is `test_outputs/not_public/`, which is already separated and should be evaluated independently rather than lumped in with casual reruns.
- Consequence: Keep the current tracked deletions for the older `finreport25` workflow-run artifacts. Do not treat new `finreport25` reruns as candidates for normal git tracking. Any future curated-output decision should target a narrower, explicitly documented fixture surface rather than the general `finreport25_*` run directories.

### 2026-04-25: Treat `docs/design/` As The Sole Canonical Design-Doc Surface And Keep Duplicate Handoff Material Out Of Active Docs
- Decision: `docs/design/` is the sole canonical in-repo design-doc surface. The tracked deletions from the old chat handoff bundle should remain as cleanup, not be restored as a parallel authority surface.
- Rationale: The chat transcript material is clearly historical notes, while `docs/design/` already contains the overlapping design-doc set with aligned root-doc references. Restoring the deleted handoff bundle would recreate the exact duplicate-authority problem the cleanup pass is trying to remove.
- Consequence: Future design-doc references should point to `docs/design/`. Chat transcript material now lives in `quarantine/docs-chats/`. If any wording from the deleted handoff bundle is still valuable later, it should be intentionally merged into `docs/design/` rather than restored as a second canonical bundle.

### 2026-04-24: Use A Layered Package Relationship, Not A Merge-Now Or Separate-Unrelated Story
- Decision: Treat `accessibility_by_manifest/` and `src/pdf_accessibility/` as layered parts of one repository, not as unrelated parallel products and not as an immediate merge candidate.
- Rationale: `pyproject.toml` packages both `accessibility_by_manifest*` and `pdf_accessibility*` in one distribution and exposes separate console scripts for each path. The codebases are largely independent today, but their responsibilities are complementary rather than contradictory: `accessibility_by_manifest/` handles broad evidence extraction, normalization, and projection work, while `src/pdf_accessibility/` owns the narrow v0.1.0 shared-state remediation workflow with draft/validation/finalization rules.
- Consequence: New broad manifest/evidence pipeline work should continue in `accessibility_by_manifest/`. New v0.1.0 workflow-state, review-loop, writeback, validator, and finalization work should go in `src/pdf_accessibility/`. Future integration should happen through deliberate interfaces and reuse, not by collapsing the package trees prematurely.

### 2026-04-24: Use Many Inputs -> Shared Normalized Accessibility Model -> Many Format-Specific Accessibility Workflows As The Architecture North Star
- Decision: The repository should converge toward a broad architecture of many inputs feeding one shared normalized accessibility model, which then feeds many format-specific accessibility workflows.
- Rationale: The repo already has broad input and normalization code in `accessibility_by_manifest/`, a first format-specific workflow in `src/pdf_accessibility/`, and a newly explicit shared contract in `accessibility_by_manifest/normalize/accessibility_model.py`. Making that architecture explicit prevents the system from drifting into either “PDF-only everywhere” or “every format gets its own disconnected pipeline.”
- Consequence: PDF is the first active serious slice, not the limit of the architecture. Near-term product work should prioritize PDF input leading to accessible PDF and accessible HTML as sibling outputs from the same normalized model. Future DOCX, HTML, PPTX, and other workflows should consume the shared normalized model rather than cloning extraction/normalization logic.

### 2026-04-24: Close The Shared-Architecture Blueprint And Start A Narrower Cleanup/Consolidation Plan
- Decision: Treat `plans/shared-normalized-accessibility-workflow-architecture.md` as complete and move follow-on planning into a narrower cleanup/consolidation blueprint.
- Rationale: The architecture blueprint’s eight steps are now implemented: shared contract, bridges, PDF workflow integration, shared projection helpers, honest PDF finalization path, HTML sibling output, and aligned root docs. The remaining repo risk is surface ambiguity and stale cleanup inventory, not missing architecture work.
- Consequence: Follow-on planning should focus on generated-output policy, historical/reference boundaries, unclear ownership surfaces, and deliberate cleanup actions rather than extending the architecture blueprint.

### 2026-04-24: Keep The PDF Master Manifest Compact By Default While Preserving Deep Evidence Elsewhere
- Decision: The PDF path should remain evidence-rich, but the default master manifest should not inline the heaviest rebuild/debug payloads for every block by default.
- Rationale: Current measurements on `finreport25` show that the master manifest reaches about 115 MB, with `raw_block_entries` alone contributing about 54 MB. The largest contributors are `pdfminer.six` per-character `chars` arrays and `pymupdf` raw native block payloads. The design docs support keeping the master manifest canonical while using per-extractor manifests and optional deeper evidence surfaces for inspection/debugging. The DOCX path already uses this pattern with `include_rebuild_payloads=False` by default.
- Consequence: The next implementation pass should preserve compact evidence and provenance in the master manifest, move richer extractor-native payloads into per-extractor outputs where appropriate, and add optional debug/rebuild outputs for the heaviest payloads.

## Decisions Still Needed

- Whether any subset of `test_outputs/not_public/` should be formalized as curated fixtures, historical examples, or private regression evidence.
