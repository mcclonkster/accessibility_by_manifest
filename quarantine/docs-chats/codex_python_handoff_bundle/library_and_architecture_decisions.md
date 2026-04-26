---
title: Library and Architecture Decisions
filename: library_and_architecture_decisions.md
type: guide
status: draft
created: 2026-04-21
updated: 2026-04-21
origin: chat
tags:
  - python
  - architecture
  - libraries
  - codex-handoff
topics: []
aliases: []
sources: []
notes:
  - This file captures package roles, ownership boundaries, and architecture decisions from the transcript
---

## Package roles

The transcript eventually converged on a clean role split.

- **WeasyPrint** = semantic document generator
- **PyMuPDF** = direct page author / manipulator and strongest first-pass PDF extractor
- **pikepdf** = low-level PDF objects, streams, and internals
- **pypdf** = document-level metadata/navigation/security/helper operations
- **veraPDF** = machine validation
- **pdfminer.six** = text/layout refinement
- **pdfplumber** = debugging and layout-aware extraction support
- **OCRmyPDF** = OCR support only

The user repeatedly pushed back against vague “closest” language, so this role map became the more concrete answer.

## Why PyMuPDF first

PyMuPDF was selected as the first extractor adapter because it gives the widest useful first-pass coverage for the manifest:

- page count and document opening
- page geometry
- text layer presence
- image-only suspicion
- practical text block extraction
- annotations and links
- images and fonts on pages
- xref/object/stream access when needed

That makes it the best starting point for a working Python-native v0.1 manifest.

## What pypdf should own

The transcript repeatedly pointed toward pypdf as the clean owner of document-level facts such as:

- metadata
- outline/bookmarks
- named destinations
- page labels
- page layout / page mode
- permissions/security flags

It is not the main semantic generator and not the low-level stream tool.

## What pikepdf should own

pikepdf should own the lower-level PDF layer:

- raw objects
- stream dictionaries
- content streams
- name trees
- MarkInfo / tagged/struct tree detection
- lower-level provenance
- object refs / xref / stream refs
- deep PDF plumbing

This is where the transcript repeatedly used “PDF plumbing” in a non-handwavy sense.

## What pdfminer.six should own

pdfminer.six should be the refinement layer for:

- character-level text evidence
- font names/sizes
- typography-based heuristics
- richer text spans
- layout-based normalization hints

It is not the first extractor and not the writer.

## What python-docx should own

This was discussed indirectly through the DOCX projection step.

python-docx should own:
- headings/paragraphs
- list projection
- tables
- figures/captions as DOCX structures
- comments
- core properties
- warning appendix or comment projection

It should not own extraction or semantic interpretation.

## Unified CLI vs separate adapters

The transcript did not fully lock the final CLI/module architecture, but it strongly leaned toward:

- **separate extractor adapters**
- one manifest builder / validator
- one normalizer
- one warning engine
- one projector per output family

In other words:
- unified pipeline
- modular adapters

not one giant extractor-specific blob.

A likely architecture is:
- one unified CLI
- separate adapters under the hood

## Repository shape proposed in the transcript

A proposed shape included:

- `manifest/`
- `extractors/`
- `normalize/`
- `review/`
- `projectors/`
- `util/`
- tests
- CLI entry point

This is valuable as a starting direction but was not finalized as a locked tree.

## Naming decisions

### `accessibility_by_manifest`
This exact name was not deeply justified in the transcript, so it should not be treated as settled.

What is settled is the architecture principle behind that sort of name:
- the manifest is central
- accessibility-related reasoning should be visible in the manifest
- evidence, interpretation, warnings, and projection should all attach to the manifest rather than living in isolated extractor outputs

### Module/package names
The transcript did not fully settle long-term naming.
What does seem stable:
- adapters should remain separate
- manifest should remain central
- normalization and review should be explicit modules, not hidden utility code

## Tools discussed but not adopted as core

### OCR/document AI models
The transcript discussed:
- PaddleOCR
- Surya
- olmOCR
- Nougat
- docTR
- GOT-OCR 2.0
- EasyOCR
- TrOCR
- keras-ocr

But none of these became part of the immediate first implementation step.
They remain conditional extraction tools for scanned/image-heavy inputs.

### Libraries not suitable as the main core
The transcript repeatedly clarified that no single library does all of:
- semantic generation
- page authoring
- low-level control
- validation

So the project should not be designed around finding a one-library answer.

## Practical architecture principle

The transcript’s clearest architecture rule is:

- adapters collect evidence
- the manifest stores evidence
- the normalizer interprets evidence
- the review engine flags uncertainty
- the projector emits targets

That is the architecture to preserve.
