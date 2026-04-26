---
title: v0.1.0 Package Choices, Dependency Contract, and Plug-in Implementation Plan
filename: v0-1-0-package-choices-dependency-contract-and-plug-in-implementation-plan.md
type: specification
status: frozen-supporting-reference-only
created: 2026-04-21
updated: 2026-04-21
origin: chat
tags:
  - pdf
  - accessibility
  - tagged-pdf
  - python
  - dependencies
topics:
  - PDF accessibility
  - Tagged PDF
  - Dependency planning
aliases:
  - PDF Accessibility Dependency Plan v0.1.0
sources: []
cssclasses: []
notes:
  - Locks the small local/open-first stack for v0.1.0
---

# FROZEN SUPPORTING REFERENCE ONLY: v0.1.0 Package Choices, Dependency Contract, and Plug-in Implementation Plan

This file is no longer an active plan.

Use instead:

- [../../../plans/start-to-finish-product-plan.md](../../../plans/start-to-finish-product-plan.md)
  for active product execution
- [../../../plans/module-responsibility-refactor-plan.md](../../../plans/module-responsibility-refactor-plan.md)
  for supporting technical refactor work
- [../../../src/pdf_accessibility/AGENTS.md](../../../src/pdf_accessibility/AGENTS.md)
  for current package-level workflow rules

## Why This File Is Frozen

This draft is useful historical context for dependency thinking, but several
choices now conflict with the active v0.1.0 implementation:

- `ocrmypdf` is deferred, not required, for the current v0.1.0 workflow
- `verapdf` is deferred, not required, for current finalization
- current validation means internal structural, behavioral, and gating checks
- external PDF/UA validation must not be implied by a v0.1.0 `finalized` state
- OCR recovery currently uses an operator/manual recovery path rather than
  requiring OCRmyPDF as a runtime dependency

Do not update this file as execution state changes. If a dependency decision
becomes active again, move that decision into the active product plan,
`src/pdf_accessibility/AGENTS.md`, or `pyproject.toml` as appropriate.

## Historical Draft Content

## Package strategy

For v0.1.0, the stack should stay small, local, and boring.

The safest base is:

- LangGraph for orchestration, persistence, checkpoints, and interrupts
- Pydantic for typed state, typed events, and validation
- PyMuPDF for PDF ingest, page rendering, native text/object extraction, and simple table work
- pikepdf for low-level PDF surgery and metadata work
- OCRmyPDF as the OCR layer for scanned or image-only PDFs
- veraPDF as the validator

That is enough to build the v0.1.0 path without dragging in a giant framework pile.

## Exact dependency decision

### Required Python packages

- `langgraph`
- `pydantic`
- `pymupdf`
- `pikepdf`
- `typer`

### Required external tools

- `ocrmypdf`
- `verapdf`

## Optional packages for v0.1.0

### `pymupdf4llm`
Use only if the base PyMuPDF extraction plus simple heuristics are not good enough for region proposal and reading-order hints.

### `PaddleOCR` / `PP-StructureV3` / `PaddleX`
Useful, but should not be a base dependency for v0.1.0. Stronger layout/table/reading-order features come at a higher install and environment cost.

## Packages not to add in v0.1.0

- a database layer
- Celery / Redis / job queue tooling
- a web framework
- AG2
- OpenAI Agents SDK
- CrewAI
- a second orchestration framework on top of LangGraph
- a second OCR stack besides OCRmyPDF plus the optional Paddle path

## Version-floor recommendation

- `pydantic >= 2.13, < 3`
- `pymupdf >= 1.27.2, < 2`
- `pikepdf >= 10.5, < 11`

And current external-tool baselines:
- `ocrmypdf 17.4.x`
- current installed `verapdf` with PDF/UA-2 and WTPDF 1.0 profile support

## Dependency contract by service

### `services/pdf_ingest.py`
Owns:
- opening PDFs
- counting pages
- extracting coarse document metadata

Dependency:
- `pymupdf` only

### `services/pdf_render.py`
Owns:
- rendering pages to images

Dependency:
- `pymupdf` only

### `services/pdf_native.py`
Owns:
- native text spans
- blocks
- ordering hints
- links
- annotations
- basic object inspection

Dependency:
- `pymupdf` only

### `services/ocr.py`
Owns:
- OCR pass for scanned PDFs or image-only regions

Dependency:
- OCRmyPDF as the default runtime tool

Fallback rule:
- if OCRmyPDF is unavailable, downgrade to born-digital-only mode and mark scanned OCR paths unsupported for that run

### `services/vision.py`
Owns:
- region proposal support
- visual classification support
- optional AI document parsing support

Default dependency:
- no heavy required package beyond rendered page images and local heuristics from PyMuPDF output

Optional dependency:
- `pymupdf4llm` first
- PaddleOCR/PP-StructureV3 later if needed

Fallback rule:
- if no optional parser is installed, run the v0.1.0 minimal path with coarse region proposal, PyMuPDF text blocks, simple heuristics, and explicit escalation for ambiguous layout cases

### `services/tagging.py`
Owns:
- the abstraction between workflow state and PDF write-back internals

Dependencies:
- `pikepdf` required
- `pymupdf` optional for extra inspection

### `services/validator.py`
Owns:
- validator subprocess execution
- result normalization

Dependency:
- `verapdf` CLI only

Fallback rule:
- if veraPDF is unavailable, the workflow may still write a tagged draft, but it must block finalization and mark validation unavailable as a blocking issue

### `services/review.py`
Owns:
- file I/O for review tasks and review decisions

Dependencies:
- standard library only

## Metadata and document properties

The metadata path should be owned by `pikepdf`, not PyMuPDF.

That makes pikepdf the correct home for:
- document title
- primary language
- synchronized metadata updates during write-back/finalization

## Security and trust assumptions

OCRmyPDF should only be used on PDFs you trust.

Hard rule:
- OCR and write-back workers run only on trusted PDFs or inside an isolated execution environment.

## Recommended `pyproject.toml` dependency groups

### Core
- `langgraph`
- `pydantic`
- `pymupdf`
- `pikepdf`
- `typer`

### Optional local layout
- `pymupdf4llm`

### Optional advanced layout AI
- `paddlex`
- whatever Paddle/PaddleOCR runtime the chosen PP-StructureV3 path requires

### Dev
- `pytest`
- `ruff`
- `mypy`

## What seems most likely to work consistently

For v0.1.0, the most stable package plan is:

- LangGraph + Pydantic
- PyMuPDF
- pikepdf
- OCRmyPDF
- veraPDF
- optional PyMuPDF4LLM
- defer PaddleX / PP-StructureV3 unless the simpler stack proves insufficient
