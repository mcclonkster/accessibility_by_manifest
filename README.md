# Accessibility by Manifest

## First Run

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install -e .
scripts/verify.sh -q
```

Run the current PDF workflow:

```bash
PYTHONPATH=src ./.venv/bin/python -m pdf_accessibility.cli run test_inputs/finreport25.pdf --output-dir test_outputs/finreport25_workflow_runs
```

Clean local generated artifacts without touching source:

```bash
scripts/clean-local-artifacts.sh
scripts/clean-local-artifacts.sh --apply
```

Add `--include-venvs` only when you intentionally want to remove local virtual
environments too.

Active repo guide only:

- architecture truth: [docs/design/system_reference.md](./docs/design/system_reference.md)
- run observability contract:
  [docs/design/run_observability_schema.md](./docs/design/run_observability_schema.md)
- active product plan:
  [plans/start-to-finish-product-plan.md](./plans/start-to-finish-product-plan.md)
- active v0.1 acceptance gate:
  [plans/v0.1-product-acceptance-pack.md](./plans/v0.1-product-acceptance-pack.md)
- active execution status:
  [plans/status.md](./plans/status.md)

Canonical architecture reference:

- [docs/design/system_reference.md](./docs/design/system_reference.md)

The repository is best understood as a role-based accessibility pipeline:

1. inputs
2. extract
3. normalize
4. make accessible
5. review
6. output

The current code layout is transitional, but the conceptual umbrella is one
system: `accessibility_by_manifest`.

The shared core lives in `accessibility_by_manifest/`. It owns input adapters,
evidence extraction, normalization, review signals, and shared projection
helpers.

The first fully integrated format-specific workflow lives in
`src/pdf_accessibility/`. It consumes the shared normalized model and drives the
current PDF remediation path:

1. PDF input
2. shared extraction and normalization
3. PDF-specific accessibility orchestration
4. PDF QA and finalization gating
5. accessible PDF and accessible HTML artifacts

That means the repository is broader than PDF, but PDF is the first active
serious slice. Accessible HTML is a sibling output path from the same resolved
structure, not a separate ingestion pipeline.

## Entrypoints

Use these entry points based on what you are trying to do:

- `pdf-accessibility`
  The current user-facing integrated workflow for PDF remediation. This is the
  main path for `PDF -> accessible PDF` with `accessible HTML` as a sibling
  output when finalization is legal.
- `accessibility-manifest-pdf`
  Shared-core PDF extraction and normalization. Useful for debugging, evidence
  inspection, bridge development, and source-specific pipeline work.
- `accessibility-manifest-docx`
  Shared-core DOCX extraction and normalization.
- `accessibility-manifest-pptx`
  Shared-core PPTX extraction and normalization.
- `accessibility-vision-alt-text`
  Optional local sidecar alt-text generation.

Use `AGENTS.md` for the governed v0.1.0 PDF workflow rules. Use `plans/` for
active planning, status, task, cleanup, and decision tracking. Use
`docs/design/system_reference.md` for the canonical architecture/reference
story.

## Current Product Path

The current v0.1 product entrypoint is the PDF workflow CLI:

```bash
PYTHONPATH=src ./.venv/bin/python -m pdf_accessibility.cli run "/path/to/input.pdf" --output-dir "/path/to/runs"
```

The terminal now prints the operator-facing run summary directly:

- `run_dir`
- `document_status`
- `finalization_state`
- `blocker_count`
- `review_decisions_template`
- `ocr_recovery_template`
- `primary_next_step`

For finalized simple documents, that summary ends with `primary_next_step: none`.
For blocked runs, it points at the next template file to fill.

Each run directory is also now a proper run record. The current contract is in
[docs/design/run_observability_schema.md](./docs/design/run_observability_schema.md)
and includes:

- `status.json`
- `manifest.json`
- `environment.txt`
- `git.txt`
- `metrics/summary.json`
- `metrics/timings.csv`
- `logs/execution.log`
- `logs/debug.log`
- `logs/events.jsonl`

## Operator Loop

The current PDF workflow is meant to be used like this:

1. run the workflow
2. read the CLI summary or open `operator_guide.json`
3. fill `review_decisions_template.json` if present
4. fill `ocr_recovery_template.json` if present
5. rerun with:

```bash
PYTHONPATH=src ./.venv/bin/python -m pdf_accessibility.cli run "/path/to/input.pdf" --output-dir "/path/to/runs" --review-decisions "/path/to/review_decisions.json" --ocr-recovery "/path/to/ocr_recovery.json"
```

The workflow stays honest:

- if blockers are resolved, it can finalize and emit:
  - `accessible_output.pdf`
  - `accessible_output.html`
- if blockers remain, it stops in `needs_review` and leaves the next operator step behind in the run directory

## Real Example: finreport25

The current real complex-PDF demo path is `test_inputs/finreport25.pdf`.

An untreated run currently produces an operator guide like:

- blocker count around `101`
- `review_decisions_template.json` present
- `ocr_recovery_template.json` present
- `primary_next_step: fill_review_decisions`

After a real combined rerun using:

- one title decision
- one table review decision
- one figure alt-text decision
- OCR recovery text for pages `75` and `94`

the blocker count dropped from `101` to `29`, and the OCR template disappeared
because those OCR blockers were actually cleared.

That is the current proof that the operator loop is real, even though the
document still honestly remains in `needs_review`.

## v0.1 Limits

What currently works best:

- simple born-digital PDFs
- document title and primary language remediation
- flat simple list HTML/PDF output
- human-reviewed table, figure, and OCR blocker reduction

What still remains narrow:

- complex table writeback/finalization
- broad figure completion on complex reports
- annotation/link writeback
- complex content-stream situations

So `needs_review` is not a failure state by itself. It means the workflow found
real unresolved work and refused to bluff past it.

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
- optional debug evidence JSON under `{pdf_stem}_debug_evidence/` when deep
  payload flags are enabled
- normalized manifest view
- review queue view
- draft DOCX review artifact
- Adobe reference comparison JSON/Markdown, when same-stem Adobe exports are
  present beside the input PDF

### PDF Evidence Layers

The PDF output path now uses three evidence layers:

1. master manifest
   compact canonical evidence for routine use, normalization, review, and
   downstream workflow bridges
2. extractor manifests
   medium-detail single-extractor views that are richer than the master manifest
   but still human-inspectable
3. debug evidence sidecars
   opt-in heavy payloads for rebuild/debug work, such as `pdfminer.six`
   character arrays and PyMuPDF `raw_block` payloads

The default run keeps the master manifest practical. If you need the heaviest
payloads, request them explicitly:

```bash
python -m accessibility_by_manifest.cli.pdf "/path/to/pdf" --output-dir "/path/to/output-folder" --overwrite --include-rebuild-payloads --include-char-level-evidence
```

Those flags do not make the master manifest huge again. They write the heaviest
payloads into debug sidecars instead.

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
