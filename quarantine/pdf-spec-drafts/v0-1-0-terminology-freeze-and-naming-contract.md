---
title: v0.1.0 Terminology Freeze and Naming Contract
filename: v0-1-0-terminology-freeze-and-naming-contract.md
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
  - terminology
topics:
  - PDF accessibility
  - Tagged PDF
  - Workflow naming
aliases:
  - PDF Accessibility Terminology Freeze v0.1.0
sources: []
cssclasses: []
notes:
  - Freezes field-recognizable terminology before deeper implementation work
---

# v0.1.0 Terminology Freeze and Naming Contract

## Purpose

Freeze the naming layer before deeper implementation work.

This contract exists to prevent:

- internal-only labels
- drifting terminology across drafts
- verbose node names that read badly in code
- PDF-spec language getting mixed up with workflow language

## Naming layers

This project uses three naming layers.

### 1. PDF standards language

Use this language when talking about PDF correctness, write-back mechanics, and accessibility structure.

Frozen PDF terms:

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
- table structure
- heading structure
- list structure
- figure
- caption

### 2. Workflow language

Use this language when talking about orchestration, control flow, and multi-agent cooperation.

Frozen workflow terms:

- workflow
- shared state
- node
- edge
- workflow orchestrator
- routing
- interrupt
- checkpoint
- validator
- human review
- approval gate
- blocker
- reopen
- retry
- finalization
- structured findings
- proposed decisions

### 3. Code identifier language

Use shorter, readable names in code.

Rules:
- short
- readable
- stable
- unsurprising
- close enough to the domain language without becoming clumsy

## Frozen node names

### Intake and setup
- `ingest_pdf`
- `render_pages`
- `region_proposal`

### Evidence nodes
- `vision_analysis`
- `ocr_layout_analysis`
- `native_pdf_analysis`

### Accessibility interpretation nodes
- `accessibility_review`
- `artifact_check`
- `caption_association`

### Planning nodes
- `tagging_plan`
- `document_consistency`
- `structure_mapping_plan`

### Quality-control nodes
- `behavior_check`
- `approval_gate`

### Output nodes
- `write_tagged_draft`
- `validator_check`
- `human_review`
- `finalize_accessible_output`

### Control nodes
- `workflow_orchestrator`
- `apply_review_decisions`

## Node-name replacement map

- `seed_regions` → `region_proposal`
- `vision_analyze_region` → `vision_analysis`
- `ocr_layout_analyze_region` → `ocr_layout_analysis`
- `native_pdf_analyze_region` → `native_pdf_analysis`
- `accessibility_semantics_review` → `accessibility_review`
- `artifact_repetition_check` → `artifact_check`
- `caption_association_check` → `caption_association`
- `tagging_plan_region` → `tagging_plan`
- `document_consistency_check` → `document_consistency`
- `structure_content_mapping_plan_region` → `structure_mapping_plan`
- `accessibility_behavior_check_region` → `behavior_check`
- `approval_gate_region` → `approval_gate`
- `validator_check_document` → `validator_check`
- `human_review_router` → `human_review`

## Frozen state-object names

- `DocumentState`
- `PageState`
- `RegionState`
- `Finding`
- `ReviewTask`
- `ValidatorFinding`
- `ArtifactManifest`
- `OutputArtifacts`
- `FinalizationState`

## Frozen artifact names

- `input.pdf`
- `document_state.json`
- `findings.jsonl`
- `review_tasks.json`
- `review_decisions.json`
- `validator_findings.json`
- `tagged_draft.pdf`
- `finalization_status.json`
- `accessible_output.pdf`
- `artifact_manifest.json`
- `run_log.json`

## Frozen workflow-state values

Document-level:
- `pending`
- `evidence_in_progress`
- `planning_in_progress`
- `draft_ready`
- `draft_written`
- `validated`
- `needs_review`
- `review_applied`
- `write_blocked`
- `finalized`

Region-level:
- `unseen`
- `evidence_collected`
- `meaning_inferred`
- `accessibility_reviewed`
- `structure_planned`
- `mapping_planned`
- `behavior_checked`
- `committable`
- `written_to_draft`
- `validated`
- `escalated`
- `complete`

## Preferred phrases in prose

Prefer:
- shared state
- structured findings
- proposed decision
- blocking issue
- approval gate
- human review
- structure mapping
- structure tree
- marked content
- logical reading order
- tagged draft
- finalize accessible output

Avoid:
- attachment
- scheduler
- router as the main term for human review
- seed regions
- claim graph
- semantic truth engine

## Freeze decision

The following names are now frozen for v0.1.0 and should be used going forward.
