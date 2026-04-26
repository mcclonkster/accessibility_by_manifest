---
title: v0.1.0 LangGraph Wiring, Interrupts, and Finalization Path
filename: v0-1-0-langgraph-wiring-interrupts-and-finalization-path.md
type: specification
status: draft
created: 2026-04-21
updated: 2026-04-21
origin: chat
tags:
  - pdf
  - accessibility
  - tagged-pdf
  - langgraph
  - workflow
topics:
  - PDF accessibility
  - Tagged PDF
  - LangGraph orchestration
aliases:
  - PDF Accessibility Workflow Graph v0.1.0
sources: []
cssclasses: []
notes:
  - Corrected to use field-recognizable terms
  - Uses structure mapping instead of attachment language
---

# v0.1.0 LangGraph Wiring, Interrupts, and Finalization Path

## Purpose

Turn the v0.1.0 design into an actual LangGraph-shaped workflow that:

- starts from an input PDF
- produces a tagged draft PDF
- validates that draft
- routes unresolved issues to human review
- only produces a finalized accessible output when blockers are cleared

## Top-level workflow shape

The workflow has four major lanes:

- intake and evidence
- accessibility interpretation and planning
- write-back and validation
- human review and finalization

The workflow is non-linear. Findings from validation, accessibility behavior checks, document-consistency checks, and human review can reopen earlier proposed decisions.

## v0.1.0 LangGraph node list

### Intake and setup
- `ingest_pdf`
- `render_pages`
- `region_proposal`

### Evidence nodes
- `vision_analysis`
- `ocr_layout_analysis`
- `native_pdf_analysis`

### Accessibility interpretation nodes
- `accessibility_semantics_review`
- `artifact_repetition_check`
- `caption_association_check`

### Planning nodes
- `tagging_plan_region`
- `document_consistency_check`
- `structure_content_mapping_plan_region`

### Quality-control nodes
- `accessibility_behavior_check_region`
- `approval_gate_region`

### Output nodes
- `write_tagged_draft`
- `validator_check_document`
- `human_review_router`
- `finalize_accessible_output`

### Control nodes
- `workflow_orchestrator`
- `apply_review_decisions`

## Allowed edges

### Setup edges
- `ingest_pdf -> render_pages`
- `render_pages -> region_proposal`
- `region_proposal -> workflow_orchestrator`

### Evidence edges
For each active region:
- `workflow_orchestrator -> vision_analysis`
- `workflow_orchestrator -> ocr_layout_analysis`
- `workflow_orchestrator -> native_pdf_analysis`

These three may run in parallel.

### Accessibility interpretation edges
- `vision_analysis -> accessibility_semantics_review`
- `ocr_layout_analysis -> accessibility_semantics_review`
- `native_pdf_analysis -> accessibility_semantics_review`

- `vision_analysis -> artifact_repetition_check`
- `native_pdf_analysis -> artifact_repetition_check`

- `vision_analysis -> caption_association_check`
- `ocr_layout_analysis -> caption_association_check`

### Planning edges
- `accessibility_semantics_review -> tagging_plan_region`
- `artifact_repetition_check -> tagging_plan_region`
- `caption_association_check -> tagging_plan_region`

- `tagging_plan_region -> document_consistency_check`
- `tagging_plan_region -> structure_content_mapping_plan_region`

- `document_consistency_check -> structure_content_mapping_plan_region`

### Quality-control edges
- `structure_content_mapping_plan_region -> accessibility_behavior_check_region`
- `accessibility_behavior_check_region -> approval_gate_region`

### Write and validate edges
- `approval_gate_region -> workflow_orchestrator`
- `workflow_orchestrator -> write_tagged_draft`
- `write_tagged_draft -> validator_check_document`
- `validator_check_document -> human_review_router`
- `validator_check_document -> workflow_orchestrator`

### Human review and finalization edges
- `human_review_router -> workflow_orchestrator`
- `workflow_orchestrator -> apply_review_decisions`
- `apply_review_decisions -> workflow_orchestrator`
- `workflow_orchestrator -> finalize_accessible_output`

## Forbidden edges

- `vision_analysis -> write_tagged_draft`
- `ocr_layout_analysis -> write_tagged_draft`
- `native_pdf_analysis -> write_tagged_draft`
- `accessibility_semantics_review -> finalize_accessible_output`
- `validator_check_document -> finalize_accessible_output`
- `human_review_router -> finalize_accessible_output`
- any direct agent-to-agent chat edge outside shared state plus workflow orchestration

## Interrupt points

### Interrupt 1: before draft write
Trigger when:
- there are unresolved high-priority contradictions
- a region is borderline committable
- the workflow is about to write a draft with material omissions

### Interrupt 2: after validation
Trigger when:
- the validator reports blocking failures
- the validator passes but accessibility behavior checks or semantic review still have blockers

### Interrupt 3: before finalization
Trigger every time before `finalize_accessible_output`.

Checks:
- no blocking validator failures
- no blocking review tasks
- finalization state is legal
- output artifact path is ready

## Human review re-entry path

1. `human_review_router` creates review tasks.
2. Document state becomes `needs_review`.
3. Human resolves one or more review tasks.
4. Review decisions are stored in `review_decisions.json`.
5. `apply_review_decisions` converts those decisions into:
   - updated findings
   - resolved blockers
   - reopen requests where needed
6. `workflow_orchestrator` routes only the affected regions or subgraphs back into the workflow.
7. The document either:
   - returns to planning
   - returns to structure mapping
   - returns to validation
   - or becomes eligible for finalization

## Retry policy

### Region-level automatic retries
- maximum 2 automatic reopen and revision cycles per region per issue class

### Document-level automatic retries
- maximum 2 validator-driven mechanical repair loops before routing to human review

## Finalization rules

`finalize_accessible_output` may run only when:

- `tagged_draft.pdf` exists
- the validator has no blocking failures
- no blocking review tasks remain
- no required region remains unresolved in a way that invalidates the document-level result
- finalization state is one of:
  - `validated`
  - `review_applied`

### Finalization writes
- `accessible_output.pdf`
- updated `finalization_status.json`
- updated `document_state.json`
