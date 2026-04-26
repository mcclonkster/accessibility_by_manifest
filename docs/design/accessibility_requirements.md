# Accessibility Requirements

Supporting reference only.

The project should treat accessibility as structured evidence plus reviewable
decisions, not as a single pass/fail checkbox.

Important document concerns include:

- real text versus image-only pages
- reading order
- headings and document structure
- lists
- tables and header relationships
- figures and text alternatives
- links and annotations
- metadata such as title and language
- form fields, if present
- tags and structure tree evidence
- warnings and manual review
- optional validation evidence later, such as veraPDF

Automation can enforce many structural and mechanical requirements, especially
in controlled generation. It cannot fully prove content-quality questions such
as whether alt text is good, whether a heading is descriptive, or whether link
purpose is understandable.

The project should use a clear issue model:

- **Hard fail**: the run cannot produce a trustworthy artifact.
- **Warning**: the run can continue, but the condition matters.
- **Manual review required**: software cannot responsibly settle the question.

Early outputs should be review artifacts first. They should not imply final
accessibility closure unless a later validation and review process supports
that claim.
