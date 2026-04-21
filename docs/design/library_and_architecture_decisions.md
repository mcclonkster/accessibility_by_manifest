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
- **veraPDF**: optional external validator later, not an extractor

## Validator Boundary

Validation tools such as veraPDF should live outside extractors. A future
implementation should be a PDF validator layer that can run on source PDFs and
generated PDF outputs, recording validation evidence separately from extractor
evidence.

## Naming

`accessibility_by_manifest` is good enough. The more important work is schema
boundaries, adapter boundaries, merge logic, and normalization logic.
