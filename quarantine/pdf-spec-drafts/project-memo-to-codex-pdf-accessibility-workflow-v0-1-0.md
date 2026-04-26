---
title: Project Memo to Codex — PDF Accessibility Workflow v0.1.0
filename: project-memo-to-codex-pdf-accessibility-workflow-v0-1-0.md
type: memo
status: draft
created: 2026-04-21
updated: 2026-04-21
origin: chat
tags:
  - codex
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
  - Codex Handoff — PDF Accessibility
sources: []
cssclasses: []
notes:
  - Current working handoff for Codex
  - v0.1.0 is intentionally narrow
  - The governing requirement is a real PDF output path, not just analysis
---

# Project memo to Codex

## Purpose

Continue the PDF accessibility project from the current design state without restarting the architecture conversation from scratch.

This project is building a local/open-first PDF accessibility workflow that must end in a real PDF output path:

- `tagged_draft.pdf`
- validation output
- review tasks for unresolved issues
- finalized accessible output only when blockers are cleared

The work is currently at the point where the architecture, naming, typed schema, reducer model, workflow graph shape, repository skeleton, and dependency plan have been drafted.

The next implementation work should proceed from those decisions, not reopen them casually.

## Governing requirement

The project is not just a parser, analyzer, or accessibility checker.

The system must support a real end-to-end path:

1. ingest PDF
2. collect evidence
3. infer accessibility structure
4. plan structure and structure-to-content mapping
5. write a tagged draft PDF
6. validate the draft
7. route unresolved issues to review
8. finalize only when blockers are cleared

A run must terminate honestly in one of these states:

- finalized
- needs review
- write blocked

Do not let “good internal reasoning” count as done.

## Core project position

### 1. Shared-state, non-linear workflow

The system is not a linear relay race of agents.

It is a shared-state workflow where specialist nodes:

- emit structured findings
- contradict earlier proposed decisions when needed
- reopen only the smallest affected scope
- do not directly mutate shared state

Reducers apply events. Transition guards decide whether movement is legal. The workflow orchestrator routes based on the resulting state.

### 2. Accessible PDF requirements drive the architecture

The workflow has to account for:

- structure tree
- structure elements
- marked content
- MCID mapping
- ParentTree mapping
- logical reading order
- artifacts
- title and language properties
- validation
- human review

### 3. Start small, then grow

v0.1.0 is intentionally narrow.

Do not build for every PDF class right now.

### 4. Use field-recognizable terminology

The user explicitly rejected internal-only labels.

Do not reintroduce terms like:

- attachment
- scheduler
- seed regions
- claim graph

Use the frozen vocabulary.

## Frozen terminology

### Workflow terms
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

### PDF terms
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

### Frozen node names
- `ingest_pdf`
- `render_pages`
- `region_proposal`
- `vision_analysis`
- `ocr_layout_analysis`
- `native_pdf_analysis`
- `accessibility_review`
- `artifact_check`
- `caption_association`
- `tagging_plan`
- `document_consistency`
- `structure_mapping_plan`
- `behavior_check`
- `approval_gate`
- `write_tagged_draft`
- `validator_check`
- `human_review`
- `apply_review_decisions`
- `finalize_accessible_output`
- `workflow_orchestrator`

## v0.1.0 supported scope

### Included
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

### Deferred beyond v0.1.0
- forms
- links as a dedicated workflow
- logical tab order for interactive content
- formulas
- complex charts
- complex multi-column layouts
- difficult scanned documents
- advanced multilingual handling
- broken existing tag-tree reuse

## Immediate next work for Codex

Implement the project skeleton and the first code scaffold.

Specifically:

1. create the repository structure
2. create the typed model modules
3. create the event models
4. create the reducer modules
5. create the transition-guard modules
6. create the LangGraph scaffold
7. create service stubs
8. create the CLI skeleton
9. create artifact persistence helpers
10. create minimal tests for reducers and guards

Do not start by implementing every PDF feature. Start by making the narrow workflow executable.

## Recommended build order

1. `models/`
2. `reducers/`
3. `transition_guards/`
4. `persistence/`
5. `nodes/` stubs
6. `graph/`
7. `cli.py`
8. tests for:
   - reducer behavior
   - transition guards
   - artifact registration
   - blocker recomputation
9. only then begin the concrete PDF/OCR/write-back adapters

## Minimal done criteria for the next coding phase

The next phase is successful if Codex can produce a runnable scaffold that:

- accepts one input PDF
- creates a run directory
- initializes typed shared state
- runs through a minimal graph path
- emits structured findings
- applies reducers
- registers artifacts
- blocks illegal transitions
- supports a tagged-draft placeholder path
- supports validator and review placeholders
- preserves the real PDF output requirement in the design

## Decision log summary

These project decisions are effectively locked for now:

- LangGraph is the orchestration framework
- v0.1.0 is intentionally narrow
- the workflow must end in a real PDF output path
- terminology is frozen
- nodes emit events
- reducers apply state
- transition guards control legal movement
- write-back, validation, human review, and finalization are first-class
- scope grows only after the narrow version works
