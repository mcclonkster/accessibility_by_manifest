# Project Intent

Supporting reference only.

Canonical system reference:

- [system_reference.md](./system_reference.md)

This file is the original high-level intent note. Use the system reference for
the current umbrella architecture and stage boundaries.

This project is a manifest-first, evidence-first document accessibility pipeline.
It is not a converter-first project, and it is specifically not a renamed
`pdf_to_docx` workflow.

The durable unit of work is the manifest:

```text
input -> manifest -> output
```

Inputs extract evidence. Manifests preserve evidence, interpretation, review
state, and projection intent. Outputs read from manifests.

For v0.1, the project should optimize for trustworthy infrastructure:

- working manifest pipelines
- schema-valid output
- preserved source evidence
- usable normalized blocks
- explicit warnings and manual-review flags
- reproducible runs from the repo-local environment

It should not optimize yet for perfect accessibility closure, perfect semantic
recovery, one-package completeness, or final polished outputs for every case.

PDF is the first serious input. PPTX remains supported and useful, but active
new design work should prioritize PDF unless the scope is explicitly reopened.
