---
name: terminology-scope-check
description: Use before large edits, refactors, architecture changes, naming changes, scope-sensitive implementation work, or documentation updates to keep this repo aligned with frozen terminology, frozen node names, and v0.1.0 PDF accessibility scope.
metadata:
  short-description: Check terminology and scope
---

# Terminology and Scope Check

## When to use this skill

Use this skill before:

- large edits
- refactors
- new docs
- architecture changes
- naming changes
- scope-sensitive implementation work

## Goal

Keep the repo aligned with:

- frozen terminology
- v0.1.0 scope
- current architecture decisions

## Frozen workflow terms

Use:

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

## Frozen PDF terms

Use:

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

## Terms to avoid

- attachment
- scheduler
- seed regions
- claim graph
- internal metaphors
- vague “agent debate” wording

## Frozen node names

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

## Deferred beyond v0.1.0

- forms
- links as a dedicated workflow
- logical tab order for interactive content
- formulas
- complex charts
- complex multi-column layouts
- difficult scanned documents
- advanced multilingual handling
- broken existing tag-tree reuse

## Do not do

- do not broaden scope silently
- do not reintroduce deprecated labels
- do not rename frozen nodes casually
- do not treat unsupported content as if it were supported

## Quick checklist

Before finishing:

- Did any old banned term sneak back in?
- Did the change broaden scope?
- Did any node name drift?
- Did any PDF-standard term get replaced with a vague local label?
- Does the change still fit v0.1.0?
