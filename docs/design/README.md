# Design Docs

This directory is the canonical in-repo design-doc surface.

Canonical architecture reference:

- [system_reference.md](./system_reference.md)
  The single current overview for system shape, stage boundaries, and the
  relationship between manifests, review, accessibility work, and outputs.

Use `docs/design/` for:

- current design rationale
- architecture notes that still guide implementation
- longer-lived design context that complements `AGENTS.md` and
  `plans/`

Do not use older handoff bundles or chat transcripts as equal authority when
they overlap with this directory.

Use the remaining design docs here as focused companion references rather than
parallel architecture summaries:

- `project_intent.md`
- `manifest_design.md`
- `library_and_architecture_decisions.md`
- `pdf_pipeline_decisions.md`
- `run_observability_schema.md`
- `desired_outputs.md`
- `accessibility_requirements.md`

Use this authority split:

1. `docs/design/system_reference.md` for umbrella architecture and stage
   boundaries
2. `AGENTS.md` for narrow v0.1.0 PDF workflow rules
3. `plans/` for active execution tracking and decisions
4. active code and tests for implementation reality

If older material in `quarantine/`, `archive/`, or `docs/reference/` conflicts
with these files, treat the older/reference material as historical context
rather than current instruction.
