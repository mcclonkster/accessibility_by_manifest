# Project

`accessibility_by_manifest` is a manifest-centered document accessibility pipeline. Its core architecture is:

```text
input -> manifest -> output
```

Instead of building separate one-off converters like `pdf_to_docx` or `pptx_to_docx`, the project separates concerns:

- **Inputs** extract as much source evidence as possible.
- **Manifests** preserve that evidence in a structured, inspectable form.
- **Outputs** will later read from manifests to generate accessible formats like DOCX, Markdown, PDF, reports, or review bundles.

The current active inputs are:

- PPTX
- PDF
- DOCX

The current active PDF extractors are:

- PyMuPDF
- pypdf
- pikepdf
- pdfminer.six

The PDF pipeline writes both a master manifest and one filtered manifest per extractor.

## Scope Expansion

We broadened the project from a narrow converter into a manifest-centered accessibility pipeline.

The original code was organized around specific workflows, effectively things like:

```text
pptx_to_docx
pdf_to_docx
```

That made the input and output feel welded together. The problem is that the project goal is not just "convert this file to that file." The goal is to extract, preserve, inspect, normalize, review, and eventually project accessibility evidence across formats.

So we reorganized around this architecture:

```text
input -> manifest -> output
```

That means:

- **Inputs** are responsible for extracting evidence from source files.
- **Manifests** preserve the canonical structured record for the document: evidence, interpretation, warnings, review needs, and projection intent.
- **Outputs** are downstream projections that read from the manifest.

The current package layout reflects that split:

```text
accessibility_by_manifest/
  inputs/
    pdf/
    pptx/
  manifest/
  outputs/
  pipelines/
  cli/
  util/
```

This is the important conceptual shift:

- The old unit of work was the converter.
- The new unit of work is the manifest.

For PDF specifically, we also broadened from a single extractor pass into a multi-extractor evidence model. The PDF input now uses:

- **PyMuPDF** for page geometry, text blocks, images, annotations, links, fonts
- **pypdf** for metadata, outlines, page labels, destinations, permissions, forms
- **pikepdf** for low-level PDF objects, MarkInfo, structure tree, resources, content streams
- **pdfminer.six** for layout text, typography, line evidence, and character evidence

The pipeline writes:

- one **master manifest**
- one filtered manifest per extractor

The master manifest is canonical. The per-extractor manifests are derivative evidence snapshots, useful for debugging and comparison, but not equal systems of record.

Adobe-exported reference files, when present beside a source PDF, are also comparison evidence. They show how Adobe interpreted the same original PDF across export modes such as DOCX, HTML, XML, print PDF, PostScript, and image assets. The pipeline should learn from where those references succeed and where they fail, but they are not ground truth and do not replace the master manifest.

DOCX can also be processed as its own input. That is especially useful for Adobe-exported DOCX references because it lets the project inspect both the editable `python-docx` object model and the lower-level WordprocessingML package directly: ordered body blocks, stories, paragraphs, runs, tables, cells, styles, numbering, settings, relationships, media, drawings, headers, footers, sections, and raw package XML counts.

We also split the project conceptually into four hard layers:

```text
evidence -> interpretation -> review -> projection
```

That distinction matters because raw source facts, inferred structure, manual-review warnings, and output decisions are different kinds of information. The code and schema should not collapse them together.

The broader project vision is now:

- preserve as much source evidence as possible
- keep extractor evidence traceable
- normalize evidence into usable document structure
- make uncertainty explicit
- support human review
- project from manifests into DOCX, Markdown, reports, and eventually accessible PDF
- compare against Adobe reference exports when available, without treating them as canonical
- keep validators like veraPDF as optional external validation layers, not extractors

Early outputs are review artifacts first, not assumed final accessible deliverables by default.

So the project is no longer a set of paired workflows like `pdf_to_docx`. It is now a modular accessibility system where inputs, manifests, and outputs can evolve independently.

## Purpose

The purpose is to create a reliable accessibility workflow where document structure, source evidence, warnings, and output decisions are explicit rather than hidden inside a conversion script.

The master manifest is the canonical structured record for the document. It preserves evidence, interpretation, warnings, review needs, and projection intent. Extractor manifests are derivative evidence snapshots: useful for inspection, debugging, and comparison, but not equal systems of record. That distinction keeps the project from becoming a pile of partial truths.

For example, a PDF can be processed into:

- one master accessibility manifest
- separate extractor manifests showing what each tool saw
- later normalized reading-order blocks
- later accessible DOCX, Markdown, or review reports

This makes the project better suited for messy real-world documents because we can compare evidence from multiple extractors instead of trusting one library blindly.

## Architectural Boundaries

The project keeps four layers separate:

- **Evidence**: what a source file or extractor literally reports.
- **Interpretation**: what the pipeline infers from that evidence.
- **Review**: warnings, failures, confidence gaps, and manual-review requirements.
- **Projection**: intent and later output-specific decisions.

These boundaries should drive schema work, module layout, merge logic, and output behavior.

## Project Goals

1. Build around `input -> manifest -> output`, not input/output pair workflows.

2. Extract as much source evidence as possible first, then remove unnecessary fields later if needed.

3. Keep PDF extraction modular by input type and extractor:
   - PyMuPDF for page geometry, text blocks, images, annotations, links
   - pypdf for metadata, outlines, page labels, destinations, permissions, forms
   - pikepdf for low-level PDF objects, structure tree, MarkInfo, resources, content streams
   - pdfminer.six for layout text, typography, line/character evidence

4. Produce a master manifest that combines extractor evidence as the canonical merged record.

5. Produce per-extractor manifests as derivative evidence snapshots so each tool’s contribution can be inspected independently.

6. Preserve enough evidence to support later normalization:
   - reading order
   - headings
   - paragraphs
   - tables
   - figures
   - annotations
   - form fields
   - structure tags
   - OCR/image-only warnings

7. Support accessible output generation from manifests, especially:
   - DOCX
   - Markdown
   - review reports
   - eventually accessible PDF output

8. Keep validators like veraPDF as optional external validation layers, not extractors.

9. Make the codebase readable and modular:
   - `inputs/`
   - `manifest/`
   - `outputs/`
   - `pipelines/`
   - `cli/`
   - `util/`

10. Keep the workflow testable and reproducible from the repo-local virtual environment.

11. Keep manifest version `v0.1` unless there is an explicit reason to version-bump. Current work should patch and clarify the v0.1 spine rather than casually creating a new schema version.

12. Define merge policy early, including agreement, disagreement, duplicate evidence, missing versus unknown versus not-found, confidence weighting, and unresolved conflicts.

13. Early outputs are review artifacts first, not assumed final accessible deliverables by default.

14. Treat Adobe-exported reference files as comparison evidence that can guide normalization and projection work, not as source truth.

15. Support DOCX as an input manifest source so Adobe DOCX exports and later native DOCX files can be inspected with the same manifest-first discipline.

Current project status should be checked from the repo, because generated outputs and local reference files may change during active pipeline work.

## Living Design Docs

The first-class project design docs live in `docs/design/`:

- `project_intent.md`
- `manifest_design.md`
- `pdf_pipeline_decisions.md`
- `accessibility_requirements.md`
- `desired_outputs.md`
- `library_and_architecture_decisions.md`
