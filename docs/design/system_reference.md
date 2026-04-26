# System Reference

This is the canonical architecture and reference document for
`accessibility_by_manifest`.

Use this file when you need the current system shape, stage boundaries, or the
intended relationship between inputs, manifests, review, accessibility
transformation, and outputs.

Companion docs in `docs/design/` should go deeper on a specific concern. They
should not compete with this file as parallel architecture overviews.

## Core Shape

The system should be understood as a role-based pipeline:

```text
inputs -> extract -> normalize -> make accessible -> review -> output
```

That is the cleanest working model for the project.

It is consistent with the older design backbone:

```text
input -> manifest -> output
```

The `manifest` middle is not one undifferentiated blob. It carries distinct
layers that the repo already names explicitly:

- **Evidence**: what the source file or extractor literally reports.
- **Interpretation**: what the system thinks that evidence means.
- **Review**: warnings, blockers, confidence gaps, and human-review state.
- **Projection**: output intent and target-specific accessibility decisions.

## Stage Definitions

### 1. Inputs

Inputs are source-document adapters.

Examples:
- PDF
- DOCX
- PPTX
- HTML
- later formats as explicitly added

Inputs are responsible for locating source files, identifying source format, and
handing them off to source-aware extraction.

### 2. Extract

Extraction gathers as much useful source evidence as possible without pretending
that extraction alone solved accessibility.

Examples of extracted evidence:
- text blocks
- geometry
- metadata
- outlines
- links and annotations
- images and assets
- structure-tree facts
- OCR sidecar evidence
- AI parser sidecar evidence

The extractor layer is evidence-first. It preserves provenance and should keep
deep evidence available, even when the default canonical artifact stays compact.

### 3. Normalize

Normalization turns source-specific evidence into reusable accessibility
structure.

This is where the system derives source-neutral units such as:
- headings
- paragraphs
- lists
- tables
- figures
- artifacts
- document metadata
- reading order
- review flags

Normalization is the handoff point that prevents every downstream path from
reinventing extraction logic.

### 4. Make Accessible

This stage performs target-specific accessibility transformation and remediation.

It can operate in multiple target formats from the same normalized structure.

Examples:
- accessible PDF work
- accessible HTML work
- later DOCX/PPTX/other accessible-output work

This is where the system applies target-specific logic rather than merely
describing source evidence.

### 5. Review

Review is both:
- an explicit operator-facing stage
- and a cross-cutting state that begins earlier in the pipeline

Review includes:
- uncertainty flags
- blockers
- manual-review tasks
- approval decisions
- recovery inputs such as OCR text or reviewed table/figure decisions

The key rule is honesty:
- unresolved review must stay visible
- human decisions must be explicit
- clearing review uncertainty must not fake output legality

### 6. Output

Outputs are the emitted artifacts that the system can stand behind at the end of
the current workflow state.

Examples:
- accessible PDF
- accessible HTML
- manifests
- extractor manifests
- debug sidecars
- review tasks
- review-decision templates
- validator findings

Outputs should reflect what the workflow has actually earned, not what it hopes
is true.

## Current Implementation Mapping

The conceptual system is one umbrella: `accessibility_by_manifest`.

The current code layout is still transitional.

Today:
- `accessibility_by_manifest/` contains most input, extraction, normalization,
  manifest, and shared output/projection code.
- `src/pdf_accessibility/` contains the current PDF remediation workflow code
  for review loops, writeback, validation, and finalization.

That current file layout should not be mistaken for the intended conceptual
boundary. The conceptual boundary is the pipeline role boundary above, not a
product split.

## Current Product Slice

The architecture is broad, but the current most-developed product slice is:

```text
PDF input
-> PDF extraction
-> normalization
-> accessibility remediation
-> review loop
-> accessible PDF / accessible HTML output
```

That is the active serious slice, not the whole architecture.

## PDF-Specific Notes

PDF is the current first serious input.

Its extraction path remains intentionally multi-extractor:
- PyMuPDF
- pypdf
- pikepdf
- pdfminer.six

Optional sidecars may contribute additional evidence:
- Docling for whole-document comparison hints
- doctr for targeted OCR on image-only pages

Those sidecars are evidence inputs. They do not replace the deterministic
extractor spine automatically.

## Evidence Contract

The PDF path currently uses three evidence layers:

1. **master manifest**
   compact canonical evidence for routine downstream use
2. **extractor manifests**
   medium-detail single-extractor views for inspection and debugging
3. **debug sidecars**
   opt-in heavy payloads for rebuild/debug use

That layering exists to preserve deep evidence without turning the default
canonical artifact into an unusable giant dump.

## Design Rules

1. Organize by pipeline role, not by converter pair.
2. Keep evidence, interpretation, review, and projection distinct.
3. Preserve provenance.
4. Avoid redoing extraction work in downstream accessibility stages.
5. Do not let PDF-specific implementation details redefine the umbrella system.
6. Do not claim final output until review and writeback legality are actually
   satisfied.

## Companion Design Docs

Use these as supporting references:

- [project_intent.md](./project_intent.md)
  Original high-level intent and v0.1 posture.
- [manifest_design.md](./manifest_design.md)
  Manifest and layer-boundary details.
- [library_and_architecture_decisions.md](./library_and_architecture_decisions.md)
  Package-role and library-role decisions.
- [pdf_pipeline_decisions.md](./pdf_pipeline_decisions.md)
  PDF-specific extraction and interpretation notes.
- [desired_outputs.md](./desired_outputs.md)
  Output goals and artifact direction.
- [accessibility_requirements.md](./accessibility_requirements.md)
  Accessibility target constraints.
