---
title: v0.1.0 Reducers, Finding Resolution Rules, and Artifact Contract
filename: v0-1-0-reducers-finding-resolution-rules-and-artifact-contract.md
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
topics:
  - PDF accessibility
  - Tagged PDF
  - Shared state
aliases:
  - PDF Accessibility Reducer Spec v0.1.0
sources: []
cssclasses: []
notes:
  - Uses findings and proposed decisions instead of claim graph language
  - Preserves append-only history plus replaceable snapshots
---

# v0.1.0 Reducers, Finding Resolution Rules, and Artifact Contract

## Purpose

Define how shared state changes safely inside the workflow.

This draft locks:

- reducer behavior
- finding lifecycle
- conflict and reopen rules
- artifact write contracts
- append-only versus replaceable data

## Governing state model

v0.1.0 uses two layers of state:

### 1. Current snapshot state
The current working view of the document.

Examples:
- current region status
- current document finalization state
- current list of blocking review tasks
- current path to the latest tagged draft

### 2. Append-only evidence and decision history
This preserves how the workflow got to the current state.

Examples:
- visual findings
- OCR findings
- native PDF findings
- proposed decisions
- contradictions
- review decisions
- validation findings

### Core rule
The workflow may update the current snapshot, but it must not destroy the history that explains why the snapshot looks the way it does.

## Standard entities

- `DocumentState`
- `PageState`
- `RegionState`
- `Finding`
- `ReviewTask`
- `ValidatorFinding`
- `ArtifactManifest`

## Reducer principles

Every reducer in v0.1.0 must follow these rules.

- **Deterministic**
- **Scope-limited**
- **Provenance-preserving**
- **No silent deletion**
- **Reopen is explicit**
- **Approval is explicit**

## Reducer set

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

## Finding classes

v0.1.0 should use a small, stable set of finding classes.

- evidence
- proposed decision
- contradiction
- blocking issue
- approval
- reopen request
- validator result
- review decision

## Finding resolution rules

### Rule 1: Evidence does not get overwritten
Evidence findings stay as historical facts about what a node reported at that time.

### Rule 2: Proposed decisions compete, not erase
If two proposed decisions disagree on the same target and same decision type:
- preserve both
- mark them as contradictory
- expose the conflict in current blockers
- do not auto-pick a winner without explicit workflow logic

### Rule 3: Support strengthens a proposed decision
A proposed decision becomes more stable when:
- multiple findings support the same value
- no active blocking contradiction remains
- dependencies are satisfied

### Rule 4: Contradiction reopens the smallest affected scope
Examples:
- a bad table cell order reopens mapping and possibly structure planning
- a wrong heading classification reopens semantics and tagging plan
- a validator finding on broken ParentTree mapping reopens structure mapping, not vision analysis

### Rule 5: Approval is gated
A proposed decision may become approved only when:
- dependencies are satisfied
- no blocking issue remains active
- the relevant gate node approves it

### Rule 6: Human review may resolve or reopen
Human review may:
- resolve a blocking issue
- confirm one proposed decision over another
- reopen an earlier stage

## Conflict handling rules

### Duplicate findings
If two findings are truly duplicates:
- preserve both source records
- allow an index layer to group them as duplicates
- do not collapse them into one source-less record

### Same target, different value
If two findings propose different values for the same decision type:
- mark active conflict
- surface blocker if the conflict is material
- route according to workflow logic

## Artifact contract

Every run must produce a versioned artifact set.

### Artifact 1. `document_state.json`
Type: snapshot

### Artifact 2. `findings.jsonl`
Type: append-only event log

### Artifact 3. `review_tasks.json`
Type: snapshot plus stable ids

### Artifact 4. `validator_findings.json`
Type: per-run validator snapshot

### Artifact 5. `tagged_draft.pdf`
Type: PDF draft artifact

### Artifact 6. `finalization_status.json`
Type: snapshot

### Artifact 7. `accessible_output.pdf`
Type: finalized PDF artifact

### Artifact 8. `artifact_manifest.json`
Type: artifact registry

## Append-only versus replaceable fields

### Append-only
- findings log entries
- validator-run records
- review-task creation records
- artifact history entries
- review decision events
- reopen events
- approval events

### Replaceable snapshot fields
- current region status
- current document status
- current finalization state
- current blocker lists
- latest artifact pointers
- current best-supported summaries

## Approval and finalization blocker thresholds

### Region may not be approved when
- a blocking contradiction is active
- a blocking issue is active
- structure plan is missing
- structure mapping is missing
- accessibility-behavior check is blocking

### Document may not be finalized when
- a blocking validator issue is active
- a blocking review task is active
- no tagged draft exists
- the current finalization state is `write_blocked`

## Minimal reducer safety rules for LangGraph implementation

1. Nodes emit events, not wholesale state replacements
2. The workflow orchestrator should trigger reducers, not act as a specialist
3. Region reopen should be stage-aware
4. Finalization should be impossible without explicit reducer state
