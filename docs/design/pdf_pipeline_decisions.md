# PDF Pipeline Decisions

PDF is the active first serious input for the project.

The PDF pipeline should remain:

```text
PDF input -> extractor evidence -> master manifest -> derivative views -> outputs
```

Current extractor order:

1. PyMuPDF
2. pypdf
3. pikepdf
4. pdfminer.six

PyMuPDF remains the right first adapter because it gives the fastest useful path
to page count, geometry, text-layer detection, image-only suspicion,
annotations, links, images, fonts, and raw blocks.

pypdf layers document-level metadata, navigation, security, and forms.

pikepdf layers low-level PDF object evidence, MarkInfo, structure tree
detection, resources, and content-stream evidence.

pdfminer.six layers richer layout, typography, line evidence, and character
evidence.

## v0.1 Direction

The PDF work should stay on v0.1 and patch the existing schema. Do not create a
new version just because Python evidence differs from PDF.js-shaped evidence.
Instead, make the v0.1 schema extractor-neutral enough to hold Python-native
evidence cleanly.

## Fixtures

Real PDFs should drive the work. `finreport25.pdf` is the main current fixture
because it exercises large-document behavior, multiple extractor views, tagged
PDF evidence, image evidence, and review-worthy complexity.

## Rebuild-Critical Gaps

There are two different kinds of missing information.

### Source-Layer Extraction Gaps

These are facts the extractors can often pull and the manifest should preserve
when available:

- document catalog language, such as `/Lang`
- usable structure-tree evidence, not only `struct_tree_detected`
- MCID, parent-tree, and structure-element linkage
- richer raw outline/bookmark object evidence
- concrete annotation records with subtype, rect, contents, URL, destination,
  and raw extractor payload
- content-stream payloads or parsed operator models, where the manifest needs
  rebuild-grade fidelity
- embedded asset payloads or extracted asset references for images, form
  XObjects, font programs, and ToUnicode maps
- parsed XMP metadata fields, not only `xmp_present`

### Interpretation, Normalization, And Review Gaps

These are not extractor failures. They belong to later layers:

- normalized headings
- normalized paragraphs
- normalized tables
- normalized figures
- reading-order indexes
- semantic table header relationships
- review warnings and manual-review decisions

The current extractor layer already preserves a large amount of evidence. The
next major project layer is interpretation: turning evidence into normalized,
reviewable document structure without pretending the extractor layer solved
semantic recovery by itself.
