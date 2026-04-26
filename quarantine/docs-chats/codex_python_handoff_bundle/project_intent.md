---
title: Project Intent
filename: project_intent.md
type: guide
status: draft
created: 2026-04-21
updated: 2026-04-21
origin: chat
tags:
  - pdf
  - accessibility
  - pipeline
  - codex-handoff
topics: []
aliases: []
sources: []
notes:
  - Built from the current chat transcript only
  - Focuses on conclusions, corrections, and clarified requirements
---

## Project Intent

This project is not a generic “convert PDFs” utility.

It is an attempt to build a **serious, inspectable, accessibility-aware document pipeline** that can take difficult source documents, preserve what the source literally contains, normalize that material into a structured intermediate representation, attach uncertainty and review flags, and then project that normalized structure into a target output.

The transcript focused most heavily on **PDF** as input and on a **manifest-centered pipeline** as the backbone.

## The real problem being solved

The user is trying to solve a problem that sits between three bad extremes:

- shallow file conversion that loses meaning
- brittle, opaque AI extraction that hides uncertainty
- manual remediation workflows that do not scale and do not preserve provenance

The target system should instead make it possible to:

- inspect what the PDF literally contains
- preserve extractor evidence
- distinguish source evidence from interpretation
- normalize the document into units that are actually workable
- attach warning and review requirements at the right layer
- project into a target format without pretending certainty where there is none

This is not just a “PDF to DOCX” converter. It is a **document evidence and normalization system** with accessibility and reviewability built in.

## Who the output is for

At least in v0.1, the outputs are for:

- the user as operator/reviewer
- future automation stages
- Codex or other code agents continuing the work
- downstream projection code
- human reviewers who need to inspect what is uncertain

That means the outputs should be **review artifacts and process artifacts first**, not polished end-user deliverables first.

## What “good enough” means for v0.1

For v0.1, “good enough” does not mean:

- perfect accessibility
- perfect semantic recovery
- full PDF/UA closure
- one-library completeness
- final production-ready document generation for every case

For v0.1, “good enough” means:

- there is a stable manifest contract
- the manifest can be populated from Python
- the pipeline can preserve raw evidence separately from normalized interpretation
- warnings and manual review points are explicit
- the system can handle real test PDFs without collapsing into opaque output
- the user can inspect the result and work with normalized blocks rather than raw PDF fragments

In other words, v0.1 is about **trustworthy infrastructure**, not final polish.

## What later versions would need

Later iterations can pursue:

- stronger normalization heuristics
- richer low-level provenance
- OCR/document-model integration
- better PDF → PDF projection
- better DOCX/Markdown projection quality
- stronger accessibility-rule coverage
- tighter validation against WCAG/PDF/UA/Word accessibility expectations

But those are later. The transcript consistently pushed toward building a **clear, inspectable, schema-driven spine first**.

## Important framing correction from the transcript

A major correction in the chat was that the assistant kept drifting into **remediation/inference of arbitrary PDFs**, while the user was repeatedly working in a **creation / controlled-pipeline / deterministic-authoring** frame.

That correction matters here too:

- the project is not only about guessing what an arbitrary PDF meant
- it is also about designing a pipeline where semantics can be explicit upstream and serialized intentionally downstream

The user strongly values deterministic control, exactness, and explicit semantic modeling wherever possible.

## Practical thesis

The project should be treated as:

- **evidence-preserving**
- **schema-centered**
- **accessibility-aware**
- **reviewable**
- **multi-stage**
- **not magic**

The best one-line description from the transcript is:

A system that separates:
- what the file literally gave us
- what we think it means
- how confident we are
- what output we plan to create
