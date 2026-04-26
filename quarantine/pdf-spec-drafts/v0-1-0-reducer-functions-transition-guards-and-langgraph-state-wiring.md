---
title: v0.1.0 Reducer Functions, Transition Guards, and LangGraph State Wiring
filename: v0-1-0-reducer-functions-transition-guards-and-langgraph-state-wiring.md
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
  - reducers
  - transition-guards
topics:
  - PDF accessibility
  - Tagged PDF
  - Reducer design
aliases:
  - PDF Accessibility Reducer Functions v0.1.0
sources: []
cssclasses: []
notes:
  - Uses reducers for state application and transition guards for legal state changes
---

# v0.1.0 Reducer Functions, Transition Guards, and LangGraph State Wiring

## Purpose

Define how the workflow becomes executable without letting nodes mutate shared state directly.

This draft locks:

- reducer responsibilities
- event dispatch rules
- transition guards
- blocker computation
- artifact registration behavior
- LangGraph state application pattern

The governing rule is simple:

- nodes emit typed events
- reducers apply those events to shared state
- transition guards decide whether a state change is legal
- the workflow orchestrator routes based on the resulting state

## Core execution rule

Nodes do not directly mutate `DocumentState`.

Instead:

1. a node reads the current snapshot
2. the node emits one or more typed events
3. a reducer layer applies those events in a deterministic order
4. transition guards allow or deny state changes
5. the updated snapshot becomes the next LangGraph state

## Reducer inventory

- `apply_finding_event`
- `apply_region_status_event`
- `apply_workflow_state_event`
- `apply_finalization_state_event`
- `apply_review_task_event`
- `apply_review_resolution_event`
- `apply_validator_finding_event`
- `apply_artifact_registration_event`
- `apply_reopen_event`
- `apply_approval_event`
- `recompute_region_snapshot`
- `recompute_document_snapshot`
- `recompute_blockers`

## Event application order

1. finding events
2. validator-finding events
3. review-task creation or resolution events
4. artifact registration events
5. reopen events
6. approval events
7. region-status updates
8. workflow-state updates
9. finalization-state updates
10. recompute snapshot summaries
11. recompute blockers

## Event dispatcher

The draft included an `apply_events` dispatcher that:
- sorts events
- dispatches them to the correct reducer
- recomputes region summaries
- recomputes document summaries
- recomputes blockers

## Reducer summaries

### `apply_finding_event`
Adds a new finding, links it to a target region when applicable, and preserves support/contradiction/dependency links.

### `apply_region_status_event`
Moves one region to a new stage, but only if `can_transition_region()` allows it.

### `apply_workflow_state_event`
Moves the document workflow state through legal transitions using `can_transition_workflow()`.

### `apply_finalization_state_event`
Moves the document finalization state through legal transitions using `can_transition_finalization()`.

### `apply_review_task_event`
Creates a review task and links it to the target.

### `apply_review_resolution_event`
Marks an existing review task resolved.

### `apply_validator_finding_event`
Adds a validator finding and links it to a region if the target is known.

### `apply_artifact_registration_event`
Registers any written artifact, updates manifest history, and updates latest pointers.

### `apply_reopen_event`
Sends a target back to an earlier stage.

### `apply_approval_event`
Records that a region or document has been explicitly approved to move forward.

## Derived snapshot recomputation

### `recompute_region_snapshot`
Updates:
- `current_region_type`
- `current_accessibility_role`
- `current_structure_plan_status`
- `current_structure_mapping_status`

### `recompute_document_snapshot`
Updates:
- `stable_region_ids`
- `blocked_region_ids`
- `escalated_region_ids`
- `review_required`

### `recompute_blockers`
Derives blockers from:
- active `blocking_issue` findings
- open blocking review tasks
- validator errors

## Transition guards

### Region transition guard
Implemented as `can_transition_region(current, new)` using an allowed-transition map.

### Workflow transition guard
Implemented as `can_transition_workflow(current, new)` using an allowed-transition map.

### Region approval transition guard
Implemented as `can_approve_region(state, region_id)`.

A region may be approved only when:
- `current_region_type` exists
- `current_accessibility_role` exists
- `current_structure_plan_status == "ready"`
- `current_structure_mapping_status == "ready"`
- `blocking_issue_ids` is empty
- there is no active `behavior_objection`

### Draft-write transition guard
Implemented as `can_write_draft(state)`.

The document may write a tagged draft only when:
- at least one region is committable
- `document_title` exists
- `primary_language` exists
- workflow state is `DRAFT_READY`
- finalization state is not `WRITE_BLOCKED`

### Finalization transition guard
Implemented as `can_transition_finalization(state, new_finalization_state)`.

The document may finalize only when:
- tagged draft artifact exists
- no blocking validator findings remain
- no blocking review tasks remain
- workflow state is `VALIDATED` or `REVIEW_APPLIED`

## LangGraph wiring pattern

v0.1.0 should wire LangGraph in two layers:

### Layer 1. Specialist nodes
These nodes read snapshot state and emit `NodeEvent` lists.

### Layer 2. State application node
After every specialist node run, pass events through one shared reducer node:
- `apply_events`

Pattern:

```python
specialist_node -> apply_events -> workflow_orchestrator
```

## Recommended graph pattern

### Setup
- `ingest_pdf -> apply_events`
- `render_pages -> apply_events`
- `region_proposal -> apply_events`

### Evidence
- `vision_analysis -> apply_events`
- `ocr_layout_analysis -> apply_events`
- `native_pdf_analysis -> apply_events`

### Accessibility interpretation and planning
- `accessibility_review -> apply_events`
- `artifact_check -> apply_events`
- `caption_association -> apply_events`
- `tagging_plan -> apply_events`
- `document_consistency -> apply_events`
- `structure_mapping_plan -> apply_events`
- `behavior_check -> apply_events`
- `approval_gate -> apply_events`

### Output
- `write_tagged_draft -> apply_events`
- `validator_check -> apply_events`
- `human_review -> apply_events`
- `apply_review_decisions -> apply_events`
- `finalize_accessible_output -> apply_events`

### Control
- `apply_events -> workflow_orchestrator`

## Blocker derivation rules

### Region blocker derivation
A region is blocked if any of these are active:
- `blocking_issue` finding on the region
- open blocking review task on the region
- validator error linked to the region

### Document blocker derivation
The document is blocked from finalization if:
- any blocking review task is open
- any validator error is active
- required document properties are missing
- workflow state is `WRITE_BLOCKED`
