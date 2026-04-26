---
title: PDF Pipeline Decisions
filename: pdf_pipeline_decisions.md
type: guide
status: draft
created: 2026-04-21
updated: 2026-04-21
origin: chat
tags:
  - pdf
  - pipeline
  - extraction
  - normalization
  - codex-handoff
topics: []
aliases: []
sources: []
notes:
  - Creation-only and controlled-pipeline reasoning was repeatedly clarified in the transcript
  - Avoid drifting back into remediation framing without explicit user direction
---

## Core pipeline shape

The transcript converged on this pipeline:

1. Input
2. Extract
3. Interpret / normalize
4. Attach review flags
5. Project to target output

This architecture applies whether the output is DOCX, PDF, Markdown, or something else.

## The important conceptual distinction

The assistant repeatedly drifted into **remediation/inference** language. The user repeatedly corrected that drift.

The preserved distinction is:

- **Creation / controlled pipeline**
  - semantics should be explicit upstream
  - tags and reading order should be emitted intentionally
  - accessibility structure should be deterministic where possible

- **Remediation / inference**
  - semantics must be guessed from visual evidence
  - heading-vs-bold-text is an inference problem
  - this is a different problem category

The user’s preferred reasoning frame in this transcript was the controlled-pipeline / deterministic-authoring side.

## What the pipeline is allowed to automate

In a controlled generation pipeline, code should be able to control:

- tags
- structure tree
- reading order
- heading levels
- list structure
- table structure and header relationships
- figure vs decorative handling
- metadata
- bookmarks/navigation
- many form semantics if forms later matter

The remaining non-fully-automatable parts are mostly content-quality questions such as:
- whether a title clearly identifies the document
- whether alt text is actually good
- whether a chart description is sufficient
- whether a wording choice is understandable

## Extraction strategy

The transcript settled on an adapter stack, not a one-library fantasy.

### Package roles
- **PyMuPDF** = first-pass page evidence and raw block extraction
- **pypdf** = metadata, navigation, security, and other document-level facts
- **pikepdf** = low-level PDF objects, content streams, and provenance
- **pdfminer.six** = richer text spans and typography/layout refinement

### Implementation order
This order was explicitly chosen:

1. PyMuPDF
2. pypdf
3. pikepdf
4. pdfminer.six

### Why PyMuPDF first
Because it gives the best single-package first-pass coverage:
- pages
- geometry
- text presence
- image-only suspicion
- annotations/links
- images/fonts on page
- practical raw block extraction
- xref/object/stream access

## Normalization strategy

Normalization is the real heart of the pipeline.

It should not be a library feature. It should be project code.

The code should take:
- page-level evidence
- raw block evidence
- style hints
- structure hints
- navigation hints
- low-level provenance

and convert them into semantic units such as:
- heading
- paragraph
- list
- list_item
- table
- table_row
- table_cell
- figure
- caption
- link
- note
- artifact
- unknown

with:
- page span
- reading order
- confidence
- semantic source quality
- warning flags

The transcript repeatedly emphasized that the user needs to work with normalized units, not raw PDF fragments.

## Warning / review model

Warnings are their own layer. They are not raw evidence and not normalized meaning.

The schema already supports warnings at:
- document level
- page level
- raw block level
- normalized block level

Examples that emerged in the transcript:
- `BOOKMARKS_MISSING`
- `TITLE_BAR_NOT_SET`
- `UNTAGGED_PAGE_CONTENT_PRESENT`
- `ANNOTATION_TAGGING_REVIEW`
- `FIGURE_DESCRIPTION_REVIEW`
- `TABLE_HEADERS_UNCERTAIN`
- `TABLE_STRUCTURE_IRREGULAR`
- `HEADING_NESTING_INVALID`
- `READING_ORDER_MANUAL_CHECK`
- `COLOR_CONTRAST_MANUAL_CHECK`

## Fail vs warn

The transcript did not finalize a formal fail/warn matrix, but the pattern is clear:

### Fail the build when
- required structural data is missing for controlled generation
- source-model fields that the generator depends on are absent
- forbidden features appear where the pipeline policy rejects them
- output invariants are violated

### Warn when
- interpretation is uncertain
- review is needed for content quality
- extractor evidence conflicts or is weak
- a document can proceed but should not be trusted blindly

In the earlier generator-spec reasoning, this principle appeared as:
- make what can be deterministic into hard rules
- isolate real human-review questions as warnings/review flags

## PDF → DOCX vs PDF → PDF

Both were discussed.

### PDF → DOCX
The current manifest name still points here.
The pipeline should:
- preserve evidence
- normalize semantics
- project to DOCX from normalized blocks, not raw extraction

### PDF → PDF
This was explored as:
- patch existing PDF
- rebuild new PDF from normalized model
- hybrid rebuild + low-level patch

The strongest conceptual direction for the user’s goals was the hybrid semantics-first rebuild plus validation and low-level patching.

## OCR / document AI branch

OCR or document AI does not replace the main pipeline.

It belongs in a conditional branch:

- born-digital PDF → native PDF extraction first
- scanned/image-heavy PDF → OCR/document AI branch
- mixed PDF → native parse where possible, OCR only where needed

That reasoning was tied to both the accessibility guidance and the package/model discussion.
