# Manifest Design

The manifest is the canonical intermediate representation for the system.

The master manifest is the system of record. Per-extractor manifests are
derivative evidence snapshots that make each tool's contribution inspectable.
They are useful for review and debugging, but they are not equally primary.

The project should keep the current `v0.1` manifest version unless there is an
explicit schema-breaking reason to change it. Near-term work should patch and
clarify the v0.1 spine.

## Layer Boundaries

Manifest fields should preserve four separate concerns:

- **Evidence**: what the source file or extractor literally reports.
- **Interpretation**: what the pipeline thinks the evidence means.
- **Review**: warnings, hard failures, confidence gaps, and manual-review flags.
- **Projection**: output intent and later output-specific decisions.

These concerns should not collapse into one blob. For example, a raw text span,
a normalized paragraph, a warning about reading order, and a future DOCX
paragraph decision are related, but they are not the same kind of fact.

## Merge Policy

The master manifest needs explicit merge rules. v0.1 does not need perfect
answers, but it should record the policy.

Minimum policy questions:

- What happens when extractors agree?
- What happens when extractors disagree?
- How are duplicate blocks, annotations, or metadata facts deduplicated?
- How does the schema distinguish `missing`, `unknown`, and `not_found`?
- Which extractors are preferred for which fact classes?
- How is confidence recorded?
- How are unresolved conflicts represented for review?

Current default extractor ownership:

- PyMuPDF: page geometry, practical text blocks, images, annotations, links
- pypdf: metadata, outlines, page labels, destinations, permissions, forms
- pikepdf: low-level objects, structure tree, MarkInfo, resources, streams
- pdfminer.six: layout text, typography, line and character evidence

The master manifest may prefer one extractor for a field while still preserving
conflicting or supporting evidence under extractor evidence.
