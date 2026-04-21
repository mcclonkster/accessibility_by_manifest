---
title: Manifest Design
filename: manifest_design.md
type: guide
status: draft
created: 2026-04-21
updated: 2026-04-21
origin: chat
tags:
  - manifest
  - schema
  - pdf
  - accessibility
  - codex-handoff
topics: []
aliases: []
sources: []
notes:
  - Built from the current chat transcript plus the uploaded v0.1 manifest files
  - The key point is to keep v0.1 and patch it, not version-bump casually
---

## Status

The current manifest is **v0.1** and should remain **v0.1** unless the user explicitly changes that decision.

This was corrected explicitly in the transcript after an earlier casual drift toward treating a Python-native patch as a new version.

## Why the manifest is central

The manifest is the canonical intermediate representation for the pipeline.

It matters because it preserves four different things that should not be collapsed into one blob:

- what the PDF literally gave us
- what the pipeline thinks it means
- how confident the pipeline is
- what output the pipeline plans to create

That separation is one of the strongest settled decisions in the transcript.

## Existing v0.1 spine to preserve

The top-level structure is already considered good and should be preserved:

- `source_package`
- `target_package`
- `run_config`
- `document_summary`
- `document_metadata`
- `document_accessibility`
- `document_navigation`
- `document_security`
- `document_interactivity`
- `document_warning_entries`
- `page_entries`
- `raw_block_entries`
- `normalized_block_entries`
- `projected_target`

The transcript repeatedly treated this spine as the right architecture.

## Canonical field categories

### Evidence fields
These describe what the source or extractor literally gave us.

Typical examples:
- document-level metadata
- page-level observed source facts
- text spans / raw blocks
- annotation evidence
- structure hints
- content-stream evidence
- object refs / xref / low-level provenance

### Interpretation fields
These describe what the pipeline thinks the evidence means.

Typical examples:
- `interpreted_role`
- `heading_level`
- `list_kind`
- `role_confidence`
- `semantic_source_quality`
- `reading_order_index`
- `reading_order_basis`

### Review fields
These mark uncertainty, risk, or manual-review needs.

Typical examples:
- `warning_entries`
- `warning_code`
- `warning_scope`
- `warning_severity`
- `manual_review_required`

### Projection fields
These describe intended output mapping, not source truth.

Typical examples:
- `target_style`
- `target_heading_text`
- `target_list_kind`
- `target_table_id`
- `projection_status`

## Current problem: the manifest is PDF.js-shaped

This is one of the main schema issues already discussed.

The manifest was created around what PDF.js exposes, so some evidence fields are too tightly coupled to PDF.js concepts.

The transcript explicitly identified that the Python version should be **extractor-neutral**, not a “Python reimplementation of PDF.js field names”.

## Proposed v0.1 patch direction

Keep the spine. Patch the PDF.js-shaped evidence fields.

### Renames
- `text_items` → `text_spans`
- `operator_evidence` → `content_stream_evidence`
- `viewport` → `page_geometry`
- `operator_list_present` → `content_stream_parsed`

### Additions
- extractor provenance at document/page/block level
- per-extractor raw evidence namespaces
- stable object references where available
- xref / stream refs where available
- richer structure hints that can carry object- and tag-path provenance

### Principle
The manifest should not force one extractor’s worldview onto all evidence.

Instead, each adapter should contribute raw evidence in a package-appropriate way, and the normalized layer should unify it.

## Example extractor-neutral pattern

The transcript repeatedly moved toward a structure like:

```json
{
  "extractor_provenance": {
    "primary_extractor": "pymupdf",
    "secondary_extractors": ["pypdf", "pikepdf", "pdfminer.six"]
  },
  "extractor_evidence": {
    "pymupdf": {},
    "pypdf": {},
    "pikepdf": {},
    "pdfminer": {}
  }
}
```

This pattern was not finalized into schema text, but it is the clearest developed direction.

## What must not happen

- Do not overwrite raw evidence with normalized conclusions.
- Do not build the schema around one extractor only.
- Do not treat v0.1 patching as a casual version bump.
- Do not let the projection layer leak backward into evidence or interpretation.

## Guiding schema philosophy

The best continuation rule from the transcript is:

- extractor outputs go into evidence fields
- your code owns interpretation fields
- your review rules own warning fields
- your output projector owns projection fields

That should govern any schema edits.
