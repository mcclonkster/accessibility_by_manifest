---
title: v0.1.0 Implementation Spec Draft
filename: v0-1-0-implementation-spec-draft.md
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
  - implementation
topics:
  - PDF accessibility
  - Tagged PDF
  - LangGraph orchestration
aliases:
  - v0.1.0 implementation spec
sources: []
cssclasses: []
notes:
  - Narrow v0.1.0 scope
  - Shared-state, non-linear workflow
  - Real PDF output path required
---

# v0.1.0 implementation spec draft

## Purpose

Turn the v0.1.0 architecture into something buildable in Python with LangGraph:

- typed shared state
- typed claims
- typed review tasks
- bounded node contracts
- explicit commit blockers
- narrow scope only

## v0.1.0 scope lock

### Included

- born-digital PDFs first
- single-column documents
- headings
- paragraphs
- lists
- simple tables
- repeated headers/footers/page numbers as artifacts
- basic title/language handling
- validator pass/fail capture
- human review routing

### Excluded

- forms
- links as a special workflow
- tab-order for interactive documents
- formulas/math-heavy pages
- complex charts requiring rich descriptions
- complex multi-column layouts
- complex scanned documents
- broken existing tag trees as a reuse target

## Typed state schema

This is the minimum viable shared state for v0.1.0.

```python
from __future__ import annotations

from enum import Enum
from typing import Literal, Optional
from pydantic import BaseModel, Field


class Confidence(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ClaimStatus(str, Enum):
    PROPOSED = "proposed"
    SUPPORTED = "supported"
    CONTRADICTED = "contradicted"
    REVISED = "revised"
    COMMITTED = "committed"
    ESCALATED = "escalated"


class RegionStatus(str, Enum):
    UNSEEN = "unseen"
    EVIDENCE_COLLECTED = "evidence_collected"
    MEANING_INFERRED = "meaning_inferred"
    ACCESSIBILITY_INTERPRETED = "accessibility_interpreted"
    STRUCTURE_PLANNED = "structure_planned"
    ATTACHMENT_PLANNED = "attachment_planned"
    BEHAVIOR_CHECKED = "behavior_checked"
    COMMITTABLE = "committable"
    WRITTEN_TO_DRAFT = "written_to_draft"
    VALIDATED = "validated"
    ESCALATED = "escalated"
    COMPLETE = "complete"
```

The full draft schema in the chat also included `BBox`, `OCRSpan`, `NativeSpan`, `Claim`, `ReviewTask`, `ValidatorFinding`, `RegionState`, `PageState`, and `DocumentState`.

## Allowed claim types in v0.1.0

Keep the set small.

- `region_type_candidate`
- `main_flow_candidate`
- `secondary_flow_candidate`
- `caption_candidate`
- `artifact_candidate`
- `ocr_text_claim`
- `block_boundary_claim`
- `row_candidate`
- `column_candidate`
- `cell_candidate`
- `native_text_claim`
- `native_order_claim`
- `existing_structure_hint`
- `anchor_candidate`
- `required_semantic_role`
- `required_table_behavior`
- `required_artifact_behavior`
- `required_metadata`
- `alt_text_needed_flag`
- `decorative_flag`
- `heading_level_plan`
- `paragraph_plan`
- `list_plan`
- `table_plan`
- `figure_plan`
- `caption_plan`
- `document_hierarchy_plan`
- `marked_content_plan`
- `mcid_plan`
- `attachment_mapping_plan`
- `structure_node_plan`
- `behavior_objection`
- `machine_validation_failure`
- `machine_validation_warning`
- `reopen_request`
- `commit_permission`
- `commit_denial`
- `escalation_required`

## Node contracts

Each node reads from shared state and writes only approved artifacts.

### `ingest_pdf`

Reads:
- `source_path`

Writes:
- `document_id`
- `page_count`
- `pages`
- initial `regions` placeholders if a pre-pass is used
- `document_status`

Must not write:
- semantic claims
- validator findings
- review tasks

### `render_pages`

Reads:
- `source_path`
- page list

Writes:
- `PageState.image_path`
- basic `page_classification`

Must not write:
- semantic claims
- attachment plans

### `vision_analyze_region`

Reads:
- page image
- region bbox
- prior visual claims

Writes:
- `region_type_candidate`
- `main_flow_candidate`
- `secondary_flow_candidate`
- `caption_candidate`
- `artifact_candidate`
- `visual_notes`

Must not write:
- final tag plan
- MCIDs
- validator findings

### `ocr_layout_analyze_region`

Reads:
- page image
- region bbox

Writes:
- `ocr_text_claim`
- `block_boundary_claim`
- `row_candidate`
- `column_candidate`
- `cell_candidate`
- `RegionState.ocr_spans`

Must not write:
- final semantic role
- structure plan
- commit decisions

### `native_pdf_analyze_region`

Reads:
- source PDF
- page number
- region bbox

Writes:
- `native_text_claim`
- `native_order_claim`
- `existing_structure_hint`
- `anchor_candidate`
- `RegionState.native_spans`

Must not write:
- final accessibility meaning
- behavior objections unless tied to raw object order evidence

### `accessibility_interpret_region`

Reads:
- vision claims
- OCR/layout claims
- native PDF claims

Writes:
- `required_semantic_role`
- `required_table_behavior`
- `required_artifact_behavior`
- `required_metadata`
- `alt_text_needed_flag`
- `decorative_flag`

Must not write:
- MCIDs
- raw PDF object plans
- final commit decision

### `tagging_plan_region`

Reads:
- accessibility interpretation claims
- caption claims
- artifact claims

Writes:
- `heading_level_plan`
- `paragraph_plan`
- `list_plan`
- `table_plan`
- `figure_plan`
- `caption_plan`
- `document_hierarchy_plan`
- `structure_node_plan`

Must not write:
- MCIDs
- validator pass/fail
- human review tasks

### `attachment_plan_region`

Reads:
- structure node plan
- native anchor candidates
- region bbox
- native spans

Writes:
- `marked_content_plan`
- `mcid_plan`
- `attachment_mapping_plan`

Must not write:
- semantic reclassification unless explicitly posting `reopen_request`
- final document validator result

### `behavior_check_region`

Reads:
- structure plan
- attachment plan
- accessibility requirements

Writes:
- `behavior_objection`
- `commit_permission`
- `commit_denial`
- `reopen_request`

Must not write:
- raw PDF objects
- validator findings

### `write_tagged_draft`

Reads:
- only regions with `commit_permission`
- document metadata candidates

Writes:
- tagged PDF draft
- `draft_output_path`
- region status updates

Must not write:
- new semantic claims
- new review tasks
- new region classifications

## Commit blocker rules

### Region-level blockers

- contradictory high-confidence `region_type_candidate` claims
- unresolved `required_semantic_role`
- unresolved table header or cell-order dispute
- unresolved caption association
- missing `attachment_mapping_plan`
- high-confidence `behavior_objection`
- explicit `commit_denial`

### Document-level blockers

- missing document title candidate
- missing primary language candidate
- unresolved heading hierarchy contradiction
- unresolved repeated furniture decision
- any blocking `machine_validation_failure`

## Review task schema

Review tasks answer questions like:

- “Confirm whether the first row is table headers.”
- “Confirm whether this line is a section heading or paragraph text.”
- “Confirm whether the footer should be artifacted.”
- “Confirm whether this image is decorative or meaningful.”

## Minimal test corpus for v0.1.0

### Include

- 5 simple syllabi or handouts
- 5 simple reports with headings and lists
- 5 simple tables
- 3 clean OCRable scans
- 2 files with repeated footer/header furniture

### Exclude

- forms
- equations
- dense charts
- brochures
- two-column reports
- badly malformed PDFs

## Deferred items list

Explicitly out of scope for v0.1.0:

- forms
- links as a dedicated workflow
- logical tab order for interactive controls
- formulas
- complex charts
- multi-column logic
- continued tables across pages
- multilingual scoped language changes beyond a simple document-level setting
- reuse of broken existing tag trees
