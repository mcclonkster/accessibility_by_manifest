# Accessibility by Manifest

Manifest-centered accessibility pipelines move documents through:

1. input-specific extraction
2. normalized accessibility evidence
3. output-specific projection

The core code path is `input -> manifest -> output`. Each input adapter writes
evidence into a manifest, and each output adapter reads from that manifest. That
keeps the architecture flexible: PPTX, PDF, DOCX, Markdown, and later PDF output
can share the same normalization contract instead of becoming one-off
input/output converters.

Shared orchestration lives in `accessibility_by_manifest.pipeline`. Input
adapters live in `accessibility_by_manifest.inputs`, output adapters live in
`accessibility_by_manifest.outputs`, and compatibility entry points wire those
modules into the shared lifecycle.

Project intent and architecture decisions are tracked as living docs in
`docs/design/`.

## Input: PPTX

Extract one PowerPoint deck, or a folder of decks, into accessibility manifests
and review artifacts.

Recommended use from this folder:

```bash
python -m accessibility_by_manifest.cli.pptx "/path/to/deck-or-folder" --output-dir "/path/to/output-folder" --overwrite --require-slide-images
```

Shorter form, if your shell is already using the project virtualenv:

```bash
python3 -m accessibility_by_manifest.cli.pptx "/path/to/deck-or-folder" --output-dir "/path/to/output-folder" --overwrite --require-slide-images
```

The package attempts to re-run itself with the project virtualenv if plain
`python3` does not have the required packages installed.

Outputs for each deck:

- companion DOCX
- slides DOCX
- slides Markdown with Markdown image syntax
- JSON manifest
- YAML manifest
- extract report
- review notes
- review report
- rendered slide images, when rendering succeeds

Useful options:

```bash
--output-dir "/path/to/output"
--no-recursive
--no-slide-images
--require-slide-images
--dry-run
--overwrite
```

Slide-image rendering is optional by default, but use `--require-slide-images`
for normal production runs. If LibreOffice or `pdftoppm` fails without that
flag, the pipeline continues with text extraction and records warnings.

External render prerequisites:

- LibreOffice at `/Applications/LibreOffice.app/Contents/MacOS/soffice`, or
  `soffice` on `PATH`
- `pdftoppm` at `/opt/homebrew/bin/pdftoppm`, or `pdftoppm` on `PATH`

The generated DOCX files include one rendered slide image per slide, alt text on
those images, extracted slide text as real Word paragraphs, visual-description
notes when metadata exists, review warnings, and style color normalization for
black text on white backgrounds.

## Input: PDF

Extract first-pass PDF evidence into the `pdf_accessibility_manifest`
v0.1 JSON shape. The PDF input path runs PyMuPDF, pypdf, pikepdf, and
pdfminer.six, then writes both a master manifest and one filtered manifest per
extractor. DOCX projection for PDFs is not implemented yet.

Recommended use from this folder:

```bash
python -m accessibility_by_manifest.cli.pdf "/path/to/pdf-or-folder" --output-dir "/path/to/output-folder" --overwrite
```

Outputs for each PDF:

- master JSON manifest
- extractor-specific JSON manifests under `{pdf_stem}_extractor_manifests/`

The PDF extractors populate:

- source PDF facts and SHA-256 fingerprint
- document metadata, XMP presence, page labels, outlines, named destinations,
  viewer preferences, permissions, form evidence, and JavaScript/XFA signals
- document-level text/image/annotation/form counts
- page geometry, page object dictionaries, resources, content-stream refs, and
  page-level extractor evidence
- annotations and links
- raw text blocks with bounding boxes, span text, font/style hints, and
  pdfminer character-level evidence
