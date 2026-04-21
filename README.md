# Accessibility by Manifest

Manifest-centered accessibility workflows for moving documents through:

1. input-specific extraction
2. normalized accessibility evidence
3. output-specific projection

The core idea is that each input adapter writes evidence into a manifest, and
each output adapter reads from that manifest. That keeps the workflow flexible:
PPTX, PDF, DOCX, Markdown, and later PDF output can share the same normalization
contract instead of becoming one-off converters.

## PPTX to DOCX

Convert one PowerPoint deck, or a folder of decks, into DOCX accessibility
review artifacts.

Recommended use from this folder:

```bash
/Users/computerk/Library/CloudStorage/Dropbox/0_VSCode/.venv/bin/python -m pptx_to_docx_accessibility "/path/to/deck-or-folder" --output-dir "/path/to/output-folder" --overwrite --require-slide-images
```

Shorter form, if your shell is already using the project virtualenv:

```bash
python3 -m pptx_to_docx_accessibility "/path/to/deck-or-folder" --output-dir "/path/to/output-folder" --overwrite --require-slide-images
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
- remediation report
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
flag, the workflow continues with text extraction and records warnings.

External render prerequisites:

- LibreOffice at `/Applications/LibreOffice.app/Contents/MacOS/soffice`, or
  `soffice` on `PATH`
- `pdftoppm` at `/opt/homebrew/bin/pdftoppm`, or `pdftoppm` on `PATH`

The generated DOCX files include one rendered slide image per slide, alt text on
those images, extracted slide text as real Word paragraphs, visual-description
notes when metadata exists, review warnings, and style color normalization for
black text on white backgrounds.

## PDF to DOCX Manifest

Extract first-pass PDF evidence into the `pdf_to_docx_accessibility_manifest`
v0.1 JSON shape. This milestone uses PyMuPDF first and writes a schema-valid
manifest. DOCX projection for PDFs is not implemented yet.

Recommended use from this folder:

```bash
/Users/computerk/Library/CloudStorage/Dropbox/0_VSCode/.venv/bin/python3 -m pdf_to_docx_accessibility "/path/to/pdf-or-folder" --output-dir "/path/to/output-folder" --overwrite
```

Outputs for each PDF:

- JSON manifest

The first PyMuPDF pass populates:

- source PDF facts and SHA-256 fingerprint
- partial document metadata
- document-level text/image/annotation/form counts
- page geometry and page-level evidence
- annotations and links
- raw text blocks with bounding boxes, span text, and basic style hints

Deferred adapters:

- pypdf for canonical metadata, outlines, page labels, named destinations, page
  mode/layout, and permissions
- pikepdf for MarkInfo, structure tree detection, content-stream evidence, and
  lower-level object provenance
- pdfminer.six for richer text spans and typography evidence
