# AGENTS.md

Package-specific operating contract for `src/pdf_accessibility/`.

This package contains the current v0.1.0 PDF accessibility remediation workflow
inside the broader `accessibility_by_manifest` system. It is an implementation
slice of the umbrella architecture, not a separate product architecture.

## Purpose

The PDF slice must support a real local/open-first path:

```text
input PDF
-> evidence collection
-> accessibility review
-> structure planning
-> structure mapping
-> tagged draft output
-> internal validation/gating
-> human review
-> review decisions
-> replanning/remapping when needed
-> finalization
```

The workflow must terminate honestly as one of:

- `finalized`
- `needs_review`
- `write_blocked`

`needs_review` is not failure. It means the workflow refused to bluff past
unresolved work.

## v0.1.0 Scope

Supported first:

- born-digital PDFs
- mostly single-column layouts
- headings
- paragraphs
- lists
- simple tables
- repeated headers, footers, and page numbers as artifacts
- basic figures
- document title
- primary language
- tagged draft creation
- internal validation/gating
- human review
- finalization gating

Deferred beyond v0.1.0:

- forms
- links as a dedicated workflow
- logical tab order for interactive content
- formulas
- complex charts
- complex multi-column layouts
- difficult scanned documents
- advanced multilingual handling
- broken existing tag-tree reuse

Deferred support must still be detectable when practical. If a deferred feature
appears, emit a blocker, review task, or finalization limitation rather than
silently shipping as if it were handled.

## Claim Policy

For v0.1.0, `finalized` means the run passed this package's internal gates. It
does not mean:

- PDF/UA conformance
- WCAG conformance
- Section 508 conformance
- ADA/legal compliance
- external validator conformance

Customer-facing language may say that a run passed internal v0.1 checks and may
identify generated artifacts, review decisions, limitations, and unresolved
blockers. Do not claim a PDF is PDF/UA conforming, WCAG conforming, or fully
accessible unless explicit standards evidence, human-review coverage, and
validator results support that claim.

## Commands

Run these commands from the repository root.

Run the workflow:

```bash
PYTHONPATH=src ./.venv/bin/python -m pdf_accessibility.cli run test_inputs/finreport25.pdf --output-dir test_outputs/finreport25_workflow_runs
```

Rerun with operator inputs:

```bash
PYTHONPATH=src ./.venv/bin/python -m pdf_accessibility.cli run test_inputs/finreport25.pdf --output-dir test_outputs/finreport25_workflow_runs --review-decisions /path/to/review_decisions.json --ocr-recovery /path/to/ocr_recovery.json
```

Generate a review-decision template:

```bash
PYTHONPATH=src ./.venv/bin/python -m pdf_accessibility.cli template-review-decisions /path/to/run-dir
```

Useful targeted tests:

```bash
./.venv/bin/python -m pytest tests/pdf_accessibility/test_reducers.py -q
./.venv/bin/python -m pytest tests/pdf_accessibility/test_transition_guards.py -q
./.venv/bin/python -m pytest tests/pdf_accessibility/test_artifact_contract.py -q
./.venv/bin/python -m pytest tests/pdf_accessibility/test_cli_smoke.py -q
```

Run all PDF workflow tests:

```bash
./.venv/bin/python -m pytest tests/pdf_accessibility -q
```

## Package Map

- `models/`: typed state, events, findings, review tasks, review decisions,
  validator findings, workflow trace entries, and artifact records.
- `reducers/`: event application and derived snapshot recomputation.
- `transition_guards/`: legal state-change checks.
- `nodes/`: specialist workflow nodes that emit typed events.
- `graph/`: LangGraph wiring and fallback orchestration.
- `services/`: wrappers for concrete libraries and external tools.
- `persistence/`: checkpoints, manifests, JSON writes, run records, and logging.
- `writeback/`: tagged draft and final output construction.
- `utils/`: IDs, timestamps, paths, logging, and JSON helpers.

Do not blur these boundaries casually.

## Architecture Rules

- Use a shared-state, non-linear workflow.
- Nodes read the current snapshot and emit typed events.
- Nodes must not mutate shared state directly.
- Reducers are the only place shared state should be updated.
- Transition guards decide whether region, workflow, approval, draft-writing, and
  finalization transitions are legal.
- Validation, behavior checks, and human review may reopen earlier proposed
  decisions.
- Do not replace this with linear relay-race handoffs, free-form agent chat, or
  hidden state mutation.

Preferred node signature:

```python
def run(document: DocumentState) -> list[NodeEvent]:
    ...
```

## Node Responsibilities

Use these node names consistently:

- `ingest_pdf`: load source PDF, initialize run state, and bridge shared
  normalized evidence when available.
- `render_pages`: create page render evidence for layout, review, and OCR support.
- `region_proposal`: propose page regions without deciding final semantics alone.
- `vision_analysis`: add visual sidecar evidence when available; do not make final
  accessibility claims.
- `ocr_layout_analysis`: add OCR/layout recovery evidence for ambiguous or
  image-only regions/pages; do not imply full scanned-PDF remediation.
- `native_pdf_analysis`: extract native PDF facts such as text, metadata,
  structure, annotations, and version/profile signals.
- `accessibility_review`: turn evidence gaps into blockers and review tasks.
- `artifact_check`: classify repeated headers, footers, page numbers, and other
  likely artifacts.
- `caption_association`: associate captions with figures/tables when evidence is
  strong enough.
- `tagging_plan`: propose target structure, roles, and output intent.
- `document_consistency`: check cross-page and cross-region consistency.
- `structure_mapping_plan`: map proposed structure to PDF writeback mechanics.
- `behavior_check`: block finalization when user-facing behavior is still unsafe.
- `approval_gate`: enforce required review and transition-guard checks.
- `write_tagged_draft`: write candidate tagged PDF output only when draft writing
  is legal.
- `validator_check`: run internal validation/gating checks and record findings.
- `human_review`: expose unresolved tasks without resolving them implicitly.
- `apply_review_decisions`: apply explicit reviewer decisions through reducers.
- `finalize_accessible_output`: finalize only outputs earned by current state.
- `workflow_orchestrator`: route nodes based on shared state and guards.

## Terminology

Use field-recognizable terms:

- tagged PDF
- structure tree
- structure element
- marked content
- marked-content reference
- MCID
- ParentTree
- logical reading order
- artifact
- alt text
- document properties
- primary language
- workflow orchestrator
- shared state
- node
- edge
- interrupt
- checkpoint
- human review
- approval gate
- transition guard
- reducer
- blocker
- reopen
- finalization
- structured findings
- proposed decisions

Avoid vague internal metaphors such as “agent debate,” “claim graph,” or
“attach the tag” as the main description.

## Required Outputs

Required JSON/log artifact classes:

- `document_state.json`
- `findings.jsonl`
- `review_tasks.json`
- `review_decisions.json`
- `validator_findings.json`
- `finalization_status.json`
- `operator_guide.json`
- `artifact_manifest.json`
- `run_log.json`

Conditional PDF artifacts:

- `tagged_draft.pdf`, only when draft write is legal.
- `accessible_output.pdf`, only when finalization is legal.

Conditional sibling/handoff artifacts:

- `accessible_output.html`, only when generated from supported normalized state.
- `run_explanation.md`, only when the optional explainer step is enabled and
  succeeds.

Do not confuse:

- `tagged_draft.pdf`: candidate PDF writeback artifact.
- `accessible_output.pdf`: PDF-slice final output after internal gates.
- `accessible_output.html`: sibling HTML output from the normalized model.
- alternate-version guidance: product/handoff recommendation, not proof that a
  conforming alternate version has been fully produced and validated.

## Validation And Finalization

Validation findings must distinguish:

- internal structural/gating checks
- machine-verifiable external checks, when an external validator is integrated
- human-review-required checks
- waived or deferred checks

Each validator finding must preserve stable `finding_id`, `target_ref`,
`message`, `severity`, `blocking`, and `resolved` fields. Add fields such as
standard, criterion, evidence source, and check type deliberately when standards
mapping becomes part of the model.

Blocking validation findings must prevent finalization unless an explicit reducer
rule or review decision resolves them. A clean internal validator report must not
be described as PDF/UA, WCAG, Section 508, ADA, or legal conformance.

Before relying on tagged PDF writeback for broader claims, require a
proof-of-capability spike that writes or modifies a minimal tagged PDF with
document title, primary language, structure tree, marked content, MCIDs, and
ParentTree entries that can be inspected by an independent tool.

## Human Review

Human review must be actionable, not advisory prose.

Review tasks must identify task ID, issue code, severity, target reference,
reason, suggested action when known, evidence/confidence context, blocking
effect, and source finding IDs when applicable.

Review decisions must identify decision ID, target review task, decision type,
reviewer value or reviewed status, note/rationale when needed, reviewer, and
resolution status or blocked reason.

Do not convert human attention into finalization progress unless the decision
actually resolves the blocker and the output path still has enough structure to
proceed.

## Stable IDs

Use deterministic IDs where possible for documents, pages, regions, blocks,
tables, figures, structure proposals, findings, review tasks, review decisions,
validator findings, and artifacts.

Do not use list positions alone as durable identifiers. If an ID must be derived
from extraction order, include enough source context in `target_ref` or payload
to reconcile it on rerun.

## OCR, AI, And Privacy

- OCR output is evidence, not structure.
- OCR must not by itself establish reading order, headings, table semantics, alt
  text, or final accessibility.
- Full remediation of difficult scanned documents remains deferred.
- AI/model outputs are sidecar evidence or explanations unless a reducer,
  transition guard, validator, or human decision makes them actionable.
- Do not send customer PDF content, OCR text, page images, logs, or run artifacts
  to external services unless an explicit feature flag and user-approved provider
  configuration enable that path.
- Logs should be useful for debugging without dumping unnecessary full document
  text or sensitive customer content.

## Source-Document Triage

When evidence suggests a source document may exist or be safer to remediate
directly, record that in findings or operator guidance. Direct PDF remediation is
not always the best path when an editable DOCX, PPTX, HTML, InDesign, or other
source file is available. This is triage/report guidance only; it does not expand
v0.1.0 scope to source-format remediation.

## Skills

Load repo-local skills for specialized procedures:

- `.agents/skills/pdf-workflow-state/SKILL.md` for reducers, events, guards,
  blockers, state transitions, and replay behavior.
- `.agents/skills/pdf-writeback-output/SKILL.md` for tagged PDF writeback,
  structure tree, MCID, ParentTree, draft/final gates, and output claims.
- `.agents/skills/terminology-scope-check/SKILL.md` for terminology, conformance
  language, v0.1 scope, and deferred blockers.

## Definition Of Done

A change in this package is done only when it preserves or improves:

- input PDF path
- structured findings
- shared state update
- tagged draft output path
- validator path
- review-task path
- finalization control
- handoff evidence for blocked direct-PDF cases

Run focused tests for the changed area. Do not claim the workflow is done if it
cannot preserve the path toward real PDF-slice output artifacts and required
umbrella handoff evidence.
