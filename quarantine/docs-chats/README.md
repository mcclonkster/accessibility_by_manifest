# Chats

This directory contains chat transcripts, handoff bundles, and extracted
reference material.

These files are useful as provenance and context, but they are not the current
authority for repo behavior, architecture, or contributor guidance.

Use this directory for:

- transcript review
- historical context
- rationale recovery when a decision needs provenance

Do not use this directory as:

- the canonical design-doc surface
- the current implementation spec
- the contributor onboarding path

Current authority order:

1. `AGENTS.md`
2. `project-file-structure-md/`
3. `docs/design/` for current design notes
4. active code and tests

If a transcript or handoff bundle conflicts with `AGENTS.md`,
`project-file-structure-md/`, or `docs/design/`, treat the chat material as
historical reference rather than current instruction.

The old `codex_python_handoff_bundle/` material should not be treated as a
parallel canonical design-doc set. Where it duplicated active design notes, the
cleanup direction is to keep `docs/design/` authoritative rather than restore
the duplicate bundle casually.
