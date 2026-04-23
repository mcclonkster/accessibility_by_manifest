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
extractor. It also writes normalized and review-only JSON views plus a draft
DOCX projection from the normalized manifest.

Recommended use from this folder:

```bash
python -m accessibility_by_manifest.cli.pdf "/path/to/pdf-or-folder" --output-dir "/path/to/output-folder" --overwrite
```

Outputs for each PDF:

- run log at `{pdf_stem}.log`
- master JSON manifest
- extractor-specific JSON manifests under `{pdf_stem}_extractor_manifests/`
- normalized manifest view
- review queue view
- draft DOCX review artifact
- Adobe reference comparison JSON/Markdown, when same-stem Adobe exports are
  present beside the input PDF

Optional whole-document AI parser sidecars can be enabled explicitly:

```bash
python -m accessibility_by_manifest.cli.pdf "/path/to/pdf" --output-dir "/path/to/output-folder" --overwrite --ai-parser docling
```

The default is `--ai-parser none`. When Docling is requested, the pipeline runs
it as sidecar evidence only and writes artifacts under
`{pdf_stem}_ai_parser_outputs/docling/`. Docling output is not canonical and does
not replace PyMuPDF, pypdf, pikepdf, or pdfminer.six evidence.

Optional targeted OCR can also be enabled for image-only pages:

```bash
python -m accessibility_by_manifest.cli.pdf "/path/to/pdf" --output-dir "/path/to/output-folder" --overwrite --ocr-parser doctr
```

The default is `--ocr-parser none`. The `doctr` OCR sidecar lazy-loads the
optional `python-doctr` package and only runs on pages already flagged as
image-only by deterministic extraction. OCR text is recorded as review-required
sidecar evidence under `extractor_evidence["doctr"]`; it does not replace the
deterministic extractor spine.

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
- optional Docling reading-order, heading, table, figure, and artifact hints
  when `--ai-parser docling` is used
- optional doctr OCR text evidence for image-only pages when
  `--ocr-parser doctr` is used

The terminal prints a concise status summary. Detailed phase, extractor,
normalization, review, output, and failure information is written to the `.log`
file in the PDF's output folder.

If Adobe-exported reference files are placed next to the source PDF with the
same stem, the PDF pipeline writes `{pdf_stem}_adobe_reference_comparison.json`
and `{pdf_stem}_adobe_reference_comparison.md` in that PDF's output folder.
Recognized references include `{pdf_stem}.docx`, `{pdf_stem}.html`,
`{pdf_stem}.xml`, `{pdf_stem}_files/`, `{pdf_stem}_print_pdf.pdf`,
`{pdf_stem}-1_print_postscript.ps`, and matching files in `images/`.

These Adobe exports are comparison evidence only. They show how Adobe
interpreted the original PDF across export modes, which helps identify where
the pipeline should learn from Adobe successes and failures. They are not
canonical ground truth and do not replace the master manifest.

## Input: DOCX

Extract first-pass DOCX evidence into a DOCX input manifest:

```bash
python -m accessibility_by_manifest.cli.docx "/path/to/docx-or-folder" --output-dir "/path/to/output-folder" --overwrite
```

Outputs for each DOCX:

- run log at `{docx_stem}.log`
- DOCX JSON manifest at `{docx_stem}_docx_manifest.json`
- normalized source-neutral IR at `{docx_stem}_docx_normalized_ir.json`

The DOCX manifest records both the `python-docx` object-model view and the
lower-level WordprocessingML/package view. It includes package parts,
relationships, core and extended properties, settings, styles, numbering,
sections, stories, headers, footers, media, drawings, hyperlinks, body blocks in
source order, body paragraphs/runs, and body tables/cells. It also keeps raw
package XML tag counts so Adobe-exported DOCX files can be compared against
Adobe HTML/XML references and PDF-derived manifests without pretending any one
export is canonical.

The normalized IR is the structure view that later accessible DOCX/PDF outputs
should read. It turns DOCX evidence into source-neutral nodes such as headings,
paragraphs, list items, tables, figures, artifacts, and sections while retaining
source references, confidence, review flags, and projection hints.

## Optional Local Vision Alt Text

Draft alt text can be generated with a local vision model. This is optional
sidecar evidence for a later DOCX repair plan; it should not be treated as
human-reviewed accessibility completion.

With Ollama:

```bash
python -m accessibility_by_manifest.cli.vision_alt_text "/path/to/docx-or-images" --provider ollama --model llava --output "/path/to/alt_text.json" --overwrite
```

With LM Studio's OpenAI-compatible local server:

```bash
python -m accessibility_by_manifest.cli.vision_alt_text "/path/to/docx-or-images" --provider lmstudio --model "qwen2.5-vl" --output "/path/to/alt_text.json" --overwrite
```

Inputs can be an image file, a folder of images, or a DOCX file. For DOCX input,
the tool extracts `word/media/*` images before sending them to the local model.
The report records generated alt text, image kind, confidence, review notes,
provider/model metadata, and any errors.
