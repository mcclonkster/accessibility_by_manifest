# Library and Architecture Decisions

The codebase is organized by pipeline role, not by input/output converter pair.

Current top-level package boundaries:

- `inputs/`: source-specific extraction adapters
- `manifest/`: manifest builders, schema, and validation
- `outputs/`: manifest writing and output projections
- `pipelines/`: orchestration from input through manifest to outputs
- `cli/`: command-line entry points
- `util/`: shared helpers

## PDF Library Roles

- **PyMuPDF**: first-pass page evidence, geometry, text blocks, images,
  annotations, links, fonts
- **pypdf**: metadata, outlines, page labels, named destinations, permissions,
  form helpers
- **pikepdf**: low-level PDF objects, streams, MarkInfo, structure tree,
  resources, object provenance
- **pdfminer.six**: layout text, typography, line evidence, character evidence
- **Docling**: optional whole-document AI parser sidecar for reading-order,
  heading, table, figure, and artifact hints; evidence only, not canonical
- **python-doctr**: optional targeted OCR sidecar for pages already detected as
  image-only; evidence only, review-required, and not a replacement for
  deterministic extraction
- **veraPDF**: optional external validator later, not an extractor

Other AI parser candidates remain later evaluation targets:

- **MinerU**: promising whole-document parser, but review license and runtime
  footprint before integration
- **marker-pdf**: promising whole-document parser, but GPL licensing makes direct
  embedding a separate decision
- **olmOCR**: useful OCR/VLM fallback for scanned or image-heavy PDFs
- **nougat-ocr**: niche academic-paper parser, not a first choice for financial
  reports

## Validator Boundary

Validation tools such as veraPDF should live outside extractors. A future
implementation should be a PDF validator layer that can run on source PDFs and
generated PDF outputs, recording validation evidence separately from extractor
evidence.

## Naming

`accessibility_by_manifest` is good enough. The more important work is schema
boundaries, adapter boundaries, merge logic, and normalization logic.
