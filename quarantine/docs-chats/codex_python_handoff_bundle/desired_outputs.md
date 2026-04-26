---
title: Desired Outputs
filename: desired_outputs.md
type: guide
status: draft
created: 2026-04-21
updated: 2026-04-21
origin: chat
tags:
  - outputs
  - docx
  - pdf
  - manifest
  - codex-handoff
topics: []
aliases: []
sources: []
notes:
  - Based on the current transcript only
  - Keeps output goals continuation-oriented rather than polished-marketing-oriented
---

## Inputs that matter first

The transcript focused overwhelmingly on **PDF**.

Other formats were mentioned in the abstract, but the active work here was around:
- PDF internals
- PDF accessibility
- Python extraction from PDFs
- PDF → DOCX
- PDF → PDF

The manifest currently names:
- `pdf_to_docx_accessibility_manifest`

So the practical input priority from this chat is:

1. **PDF first**
2. optional OCR/image branch for scanned/image-heavy PDFs
3. other formats later, if at all

## Outputs that matter first

### 1. JSON manifest
This is the most important first output.

Why:
- it preserves evidence
- it preserves interpretation
- it preserves warnings
- it preserves projection intent

The transcript repeatedly treated the manifest as the pipeline spine.

### 2. DOCX
DOCX is the first concrete projection target discussed in detail.

But the intended DOCX output is not “pretty Word document at all costs.”
It is better thought of as:
- a structured review artifact
- a downstream working document
- a human-usable projection of normalized content

### 3. PDF
PDF → PDF was explored later.
It matters, but it did not replace DOCX as the clearly anchored first output in this transcript.

### 4. Markdown
Markdown was discussed as a possible target or intermediate in some OCR/document-model contexts, but it was not developed as the main output target in this chat.

## Whether outputs are final documents or review artifacts

This is important.

For v0.1, the outputs are primarily **review artifacts and process outputs**, not guaranteed-final accessible deliverables.

That means:

- the manifest is definitely a process artifact
- the DOCX is likely a reviewable companion or normalized working document
- the PDF output, if pursued, should probably also be treated as an inspectable/generated artifact rather than assumed final without validation and review

## “Good enough” output behavior for v0.1

### Manifest
Good enough means:
- schema-valid
- evidence preserved
- normalized blocks present
- warnings attached
- projection intent explicit

### DOCX
Good enough means:
- headings, paragraphs, lists, tables, figures can be projected
- warning appendix or comments can preserve uncertainty
- page traceability can be preserved where useful
- output is reviewable and inspectable

### PDF
Good enough would mean:
- generated from normalized model
- structure and accessibility intent serialized intentionally
- validated afterward
- not claimed to be fully final just because it was generated

## Before/after logic

### Before
A difficult source PDF is:
- opaque
- page-fragmented
- hard to inspect semantically
- full of layout-specific noise
- difficult to review systematically

### After normalization
The pipeline should produce:
- document-level manifest
- page records
- raw evidence blocks
- normalized semantic blocks
- confidence values
- warning flags
- projected output instructions

### After projection
The target output should no longer be “raw PDF debris.”
It should be:
- a reviewable DOCX/PDF
- organized by normalized structure
- with uncertainty surfaced rather than hidden

## Example output philosophy

The transcript used `finreport25.pdf` as an example of a document that should end up not as “117 pages of PDF”, but as something closer to:

- 1 document
- 117 page records
- many raw evidence blocks
- fewer normalized semantic blocks
- each normalized block carrying role, order, confidence, and warnings

That is the intended output transformation.

## Open output question

The transcript did not fully lock whether Markdown should become a formal first-class projection target.

It is valuable as:
- OCR/toolkit output
- debugging output
- possible downstream artifact

But the clearly established first-class outputs in this chat are:
- JSON manifest
- DOCX projection
- possibly later PDF projection
