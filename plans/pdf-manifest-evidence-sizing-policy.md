# Plan: PDF Manifest Evidence Sizing Policy

## Objective

Keep the PDF extraction path evidence-rich while making the default master
manifest practically usable.

The rule is:

- extract as much as possible
- preserve high-value evidence
- avoid serializing the same evidence multiple times in the default master
  manifest
- keep deeper raw payloads available in extractor-specific or opt-in debug
  surfaces

## Why This Is Needed

Measured on the current `finreport25` fixture:

- `test_outputs/not_public/finreport25_manifest_output/finreport25_manifest.json`
  is about `114,723,042` bytes
- `raw_block_entries` alone account for about `54 MB`
- inside `raw_block_entries`:
  - `pdfminer.six` `text_items` account for about `42.7 MB`
  - `pymupdf` `extractor_evidence` account for about `6.0 MB`
  - `pymupdf` `text_items` account for about `1.3 MB`

The file is large because the default master manifest currently inlines:

- `pdfminer.six` per-line `chars` arrays with bbox/font metadata
- `pymupdf` `raw_block` payloads inside per-block `extractor_evidence`

That is deeper than the default canonical artifact needs to be.

## Design Basis

This policy is supported by current repo design and implementation:

- The master manifest is canonical, while per-extractor manifests are derivative
  evidence snapshots for inspection/debugging.
- The schema should keep evidence, interpretation, review, and projection from
  collapsing into one blob.
- Near-term outputs are review-oriented artifacts.
- The DOCX path already uses the right pattern:
  keep checksums/metadata in the default manifest and only inline rebuild
  payloads when `include_rebuild_payloads` is enabled.

## Policy

### Default Master Manifest

The default master manifest should keep:

- document-level conformance-relevant facts
- document/page/block provenance
- compact raw block text
- compact bbox and style summaries
- normalized blocks and tables
- review entries and warnings
- compact extractor summaries per page and per block
- enough source references for bridge and downstream workflow use

The default master manifest should not inline heavy rebuild/debug payloads for
every block by default.

### Per-Extractor Manifests

Per-extractor manifests are the right place for richer extractor-native payloads
that remain useful for debugging and inspection but do not need to live in the
default canonical artifact.

### Optional Debug/Rebuild Sidecars

The heaviest payloads should be available through explicit opt-in sidecars,
mirroring the existing DOCX `include_rebuild_payloads` approach.

## Keep / Move / Gate Table

### `pdfminer.six`

#### Keep In Master

- block `text`
- block `bbox`
- line-level or block-level text summaries when compact
- `style_hints`
- per-block counts:
  - `line_count`
  - `char_count`
  - `fonts`
- provenance:
  - extractor name
  - source ref
  - block id

#### Move To Per-Extractor Manifest

- richer `text_items` than the master needs, if still useful for inspection
- non-essential line-level detail that is meaningful for debugging but not for
  routine canonical review

#### Gate Behind Optional Debug/Rebuild Output

- per-character `chars` arrays
- per-character bbox/font/advance/upright details

Reason:
- this is the single largest size contributor in the current manifest
- it is valuable evidence, but not default-master evidence

### `pymupdf`

#### Keep In Master

- block `text`
- compact `text_items`
- block `bbox`
- compact `style_hints`
- per-block summaries:
  - `block_type`
  - `block_number`
  - `line_count`
- useful per-page summaries:
  - text block count
  - image block count
  - annotation/widget counts
  - page geometry

#### Move To Per-Extractor Manifest

- richer span-level details beyond the compact master view
- large page-native payloads that help debugging but are not needed by default

#### Gate Behind Optional Debug/Rebuild Output

- `raw_block`
- any full native `page.get_text("dict")`-shaped payload fragments

Reason:
- current `raw_block` embedding is a second major source of duplication
- the same block is already represented elsewhere in a more compact form

### `pikepdf`

#### Keep In Master

- document-level structure/MarkInfo/resource summaries
- object-presence facts relevant to PDF/UA checks
- compact page-level summaries

#### Move To Per-Extractor Manifest

- fuller object/resource breakdowns useful for low-level inspection

#### Gate Behind Optional Debug/Rebuild Output

- rebuild-grade content-stream payloads or object dumps

Reason:
- docs explicitly mention rebuild-grade fidelity as useful in some cases, but
  not as a blanket default for every routine run

### `pypdf`

#### Keep In Master

- metadata
- outlines
- page labels
- named destinations
- permissions
- forms summary

#### Move Or Gate

- only if specific raw low-level payloads become large later

Reason:
- this extractor is not currently the size problem

### AI / OCR Sidecars

#### Keep In Master

- review-relevant summary facts
- references to sidecar evidence
- warnings that sidecar evidence exists and requires review

#### Keep In Sidecar Artifacts

- raw parser exports
- heavy parser-native JSON dumps

Reason:
- current design already treats Docling and doctr as evidence-only sidecars

## Proposed Implementation Shape

### New PDF Config Controls

Add PDF controls analogous to DOCX rebuild payload handling.

Suggested shape:

- `include_rebuild_payloads: bool = False`
- `include_char_level_evidence: bool = False`
- `extractor_payload_mode: str = "compact"`

Possible modes:

- `compact`
  default master manifest stays compact
- `extractor`
  richer payloads allowed in per-extractor manifests
- `debug`
  sidecar/rebuild payloads emitted

### Output Surface

Keep the current outputs and add optional debug/rebuild outputs only when
requested.

Default:

- master manifest
- normalized manifest
- review queue
- per-extractor manifests

Optional:

- `*_debug_evidence/` or similar sidecar directory for:
  - char-level dumps
  - raw native block payloads
  - rebuild-grade object/content-stream payloads

## Field-Level Implementation Rules

1. Slim data where it is produced, not only where it is written.
2. Preserve `block_id`, `source_ref`, extractor name, and counts even when deep
   payloads move out.
3. If heavy payloads move out of the master manifest, provide a stable
   reference path or hash where useful.
4. Keep the bridge into `NormalizedAccessibilityDocument` working from the
   compact master manifest.
5. Do not make the master manifest PDF/UA-useless in the name of size.

## First Implementation Cut

Implement the smallest high-value reduction first:

1. remove `pdfminer.six` per-character `chars` arrays from the default master
   manifest
2. remove `pymupdf` `raw_block` from the default master manifest
3. preserve compact line/block summaries and provenance
4. keep richer evidence in extractor outputs or optional sidecars

This should cut the largest waste without changing the overall architecture.

## Verification Plan

### Code/Behavior Checks

- current PDF manifest tests still pass
- normalization still works
- bridge into `pdf_accessibility` still works
- extractor manifests still remain useful

### Size Checks

Use `finreport25.pdf` as the regression fixture.

Check:

- master manifest size before/after
- extractor manifest size before/after
- normalized/review outputs still present

### Acceptance Criteria

- the default master manifest becomes materially smaller
- evidence needed for normalization/review remains present
- deeper evidence is still available in extractor/debug surfaces
- the policy is consistent with the existing DOCX rebuild-payload pattern
