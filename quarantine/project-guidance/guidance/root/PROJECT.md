# Project

Canonical architecture reference:

- [docs/design/system_reference.md](./docs/design/system_reference.md)

This file is now the shorter repo-level summary.

`accessibility_by_manifest` should be understood as one umbrella accessibility
system organized by pipeline role:

```text
inputs -> extract -> normalize -> make accessible -> review -> output
```

The code layout is still transitional. The role-based pipeline above is the
conceptual truth to optimize toward.

## Purpose

The goal is to build a reliable accessibility system where:

- source evidence stays explicit and traceable
- extraction is evidence-first
- normalization produces reusable accessibility structure
- review and uncertainty stay explicit
- accessibility remediation can target multiple output formats
- outputs are only emitted when the workflow has earned them

## Current Product Slice

The current serious slice is still PDF:

- PDF input is the first active serious input
- accessible PDF is the primary near-term output
- accessible HTML is a sibling output from the same workflow state
- DOCX and PPTX remain part of the umbrella system, but not the current deepest
  remediation focus

## Entrypoints

The repo intentionally exposes both umbrella-pipeline entry points and the
current integrated PDF remediation entry point.

- `pdf-accessibility`
  The main integrated PDF workflow. Use this when the goal is real remediation
  output and honest terminal states such as `finalized` or `needs_review`.
- `accessibility-manifest-pdf`
  Shared-core PDF extraction and normalization. Useful for evidence inspection,
  bridge work, debugging, and source-specific pipeline development.
- `accessibility-manifest-docx`
  Shared-core DOCX extraction and normalization.
- `accessibility-manifest-pptx`
  Shared-core PPTX extraction and normalization.
- `accessibility-vision-alt-text`
  Optional local sidecar alt-text generation.

## Current Code Mapping

Current implementation is split across two main locations:

- `accessibility_by_manifest/`
  Most input, extraction, normalization, manifest, and shared-output code.
- `src/pdf_accessibility/`
  The current PDF remediation workflow implementation.

That current split is an implementation reality, not the conceptual boundary to
preserve forever.

## Design Boundaries

The architecture must keep these concerns distinct:

- **Evidence**
- **Interpretation**
- **Review**
- **Projection**

See the system reference for the full stage-by-stage explanation.

## Current Near-Term Goals

1. Keep the role-based architecture clear in docs and code.
2. Keep the PDF workflow moving toward real accessible-output completion.
3. Preserve evidence richness without bloating default artifacts.
4. Keep review loops honest and usable on real documents.
5. Strengthen multi-format accessibility output from the same normalized
   structure.

## Living Design Docs

The first-class project reference doc is
`docs/design/system_reference.md`.

The companion design docs live in `docs/design/`.

Active planning and cleanup control lives in `project-file-structure-md/`.

For the governed v0.1.0 PDF workflow rules, use `AGENTS.md`.
