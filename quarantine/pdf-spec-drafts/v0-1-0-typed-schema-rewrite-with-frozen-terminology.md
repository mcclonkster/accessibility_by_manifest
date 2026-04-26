---
title: v0.1.0 Typed Schema Rewrite with Frozen Terminology
filename: v0-1-0-typed-schema-rewrite-with-frozen-terminology.md
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
  - schema
topics:
  - PDF accessibility
  - Tagged PDF
  - Typed state
aliases:
  - PDF Accessibility Typed Schema v0.1.0
sources: []
cssclasses: []
notes:
  - Uses frozen terminology from the terminology contract
  - Keeps v0.1.0 narrow and output-oriented
---

# v0.1.0 Typed Schema Rewrite with Frozen Terminology

## Purpose

Define the typed state, typed findings, typed events, and node I/O contracts for v0.1.0.

This draft locks:

- the shared state model
- the finding model
- the review-task model
- the validator-finding model
- the artifact-manifest model
- the event model each node may emit
- the node input and output contract

## Scope reminder

v0.1.0 remains limited to:

- born-digital PDFs first
- mostly single-column documents
- headings
- paragraphs
- lists
- simple tables
- repeated headers, footers, and page numbers as artifacts
- basic figures
- document title
- primary language
- tagged draft creation
- validation
- human review
- finalization gating

## Design rules

1. Nodes do not rewrite the whole document state directly.
2. Reducers update the current snapshot state and preserve append-only history.
3. A finding is not truth. It is a typed specialist output.
4. Approval and finalization are explicit events, not silent implications.
5. Every meaningful state change must be reconstructable from the event and finding history.

## Enums

The draft defined:

- `Confidence`
- `FindingClass`
- `FindingStatus`
- `RegionStatus`
- `WorkflowState`
- `FinalizationState`
- `ReviewPriority`
- `ReviewTaskStatus`
- `ValidatorSeverity`
- `ArtifactStatus`

## Geometry and content models

- `BBox`
- `OCRSpan`
- `NativeSpan`

## Finding model

The `Finding` model includes:

- `finding_id`
- `target_id`
- `finding_type`
- `finding_class`
- `proposed_value`
- `confidence`
- `evidence_refs`
- `supports`
- `contradicts`
- `depends_on`
- `status`
- `source_node`
- `rationale`
- `created_at`
- `superseded_by`
- `closed_reason`

## Review-task model

The `ReviewTask` model includes issue types like:

- `heading_vs_paragraph`
- `table_headers`
- `table_cell_order`
- `caption_association`
- `artifact_decision`
- `decorative_vs_meaningful`
- `structure_mapping_uncertainty`
- `validator_followup`

## Validator-finding model

The `ValidatorFinding` model includes:

- `validator_run_id`
- `finding_id`
- `severity`
- `code`
- `message`
- `target_id`
- `likely_root_cause`
- `created_at`

## Artifact models

The draft defined:

- `ArtifactRecord`
- `OutputArtifacts`
- `ArtifactManifest`

## Page, region, and document snapshot models

The draft defined:

- `RegionState`
- `PageState`
- `DocumentState`

Key `RegionState` snapshot fields:

- `current_region_type`
- `current_accessibility_role`
- `current_structure_plan_status`
- `current_structure_mapping_status`

Key `DocumentState` fields:

- `document_title`
- `primary_language`
- `workflow_state`
- `finalization_state`
- `review_required`
- blocker lists
- `output_artifacts`
- `artifact_manifest`

## Event model

The draft defined these event types:

- `AddFindingEvent`
- `UpdateRegionStatusEvent`
- `UpdateWorkflowStateEvent`
- `UpdateFinalizationStateEvent`
- `AddReviewTaskEvent`
- `ResolveReviewTaskEvent`
- `AddValidatorFindingEvent`
- `RegisterArtifactEvent`
- `ReopenTargetEvent`
- `ApproveTargetEvent`

## Node I/O contract

Each node may emit only a constrained subset of events.

Examples:
- `vision_analysis` may emit evidence findings about region type or flow role.
- `accessibility_review` may emit proposed decisions about accessibility roles or required behavior.
- `structure_mapping_plan` may emit findings about marked-content plans, MCID mapping plans, structure mapping plans, and ParentTree mapping plans.
- `approval_gate` may emit approval or blocking findings.
- `write_tagged_draft` may emit artifact-registration and state-update events.
- `finalize_accessible_output` may emit final artifact-registration and finalization events.

## Minimal finding-type registry

The draft froze a minimal allowed finding registry including:

- region proposal and classification types
- OCR/layout findings
- native PDF findings
- accessibility-role findings
- structure-plan findings
- structure-mapping findings
- behavior findings
- approval/finalization findings

## Minimal schema rules

- A region may not be approved for write-back without current type, current accessibility role, structure plan, structure mapping plan, and no active blocking behavior issue.
- A document may not be finalized without a tagged draft artifact, no blocking validator findings, no blocking review tasks, and a legal finalization transition.
- Every artifact path stored in `OutputArtifacts` must also exist in `ArtifactManifest.latest`.
