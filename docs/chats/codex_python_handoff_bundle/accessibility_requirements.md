---
title: Accessibility Requirements
filename: accessibility_requirements.md
type: guide
status: draft
created: 2026-04-21
updated: 2026-04-21
origin: chat
tags:
  - accessibility
  - pdf
  - pdf-ua
  - wcag
  - codex-handoff
topics: []
aliases: []
sources: []
notes:
  - This file preserves the standards logic and conceptual distinctions developed in the transcript
  - It is not a complete external compliance memo
---

## Accessibility framing from the transcript

The transcript established that “accessible PDF” is not one flat checkbox. It is a combination of:

- source structure
- real text
- tags / structure tree
- reading order
- figures and text alternatives
- tables and headers
- links/navigation
- metadata like title and language
- annotations and other interactive elements where present
- validation
- manual review for the parts software cannot settle

The uploaded accessibility sources consistently reinforced:
- start with accessible source structure
- preserve accessibility on export
- image-only PDFs need OCR
- tags and reading order matter
- automated checks are not enough on their own

## WCAG logic preserved in the transcript

The key WCAG-level conclusions that matter for implementation were:

- code can control many structural/mechanical things
- code cannot fully prove content-quality questions such as:
  - whether a heading really describes the section well
  - whether link purpose is actually clear
  - whether alt text is truly equivalent
  - whether instructions are understandable

This distinction came up repeatedly when the assistant tried to overstate what code can settle.

## PDF/UA and Matterhorn logic

The transcript spent substantial time on the Matterhorn Protocol.

### Preserved conclusion
The Matterhorn conditions that “usually require human judgment” are partly a limitation of what a **validator can prove from a finished file**, not only a limitation of what a **controlled generator can enforce**.

That matters because the user wants deterministic control in a controlled generation pipeline.

The assistant developed:
- a list of the “human judgment” rows
- a classification of which become deterministic in a controlled generator
- a generator requirements spec intended to make many of them deterministic by construction

That work is useful and should not be lost.

## Controlled generation vs generic validation

A critical preserved distinction:

- **Generic validation**
  - asks what can be proven from the file after the fact
  - many checks remain “human judgment”

- **Controlled generation**
  - owns the source model
  - owns the serializer
  - can require assets and metadata upfront
  - can reject unsupported patterns before build
  - can turn many “human judgment” conditions into deterministic build-time guarantees

This distinction was central to the user’s reasoning and should shape future implementation.

## Manual review rules

The transcript repeatedly reinforced that some review will remain necessary.

The likely manual-review areas include:
- title quality
- alt text quality
- complex chart/figure descriptions
- reading-order sanity in difficult cases
- contrast issues
- representation choice for hard visual content

The system should therefore support:
- explicit warning objects
- `manual_review_required`
- block/page/document-level review visibility
- review artifacts rather than pretending certainty

## Color and contrast

Color contrast was repeatedly treated as a likely manual-check area rather than something the early pipeline should claim to solve automatically, especially for PDFs that already exist and contain rich visual content.

For controlled generation, contrast can be more enforceable upstream, but the transcript did not settle a numeric implementation policy beyond recognizing it as a real accessibility dimension.

## Alt text conventions

The transcript converged on these practical principles:

- figures and non-text content need alternatives
- decorative content should be artifacted rather than described
- some figure-like content needs `ActualText` or text treatment rather than generic figure alt text
- the existence of an alt text field is not the same as alt text quality
- chart/diagram description quality remains a human-review question unless tightly templated

## Word / DOCX accessibility expectations

The transcript did not develop Word accessibility standards as deeply as PDF accessibility, but the projection logic clearly assumes that DOCX output should preserve:

- heading hierarchy
- paragraphs
- list structure
- tables
- figures/captions
- comments or appendix for review flags
- core properties / title metadata where applicable

The role of DOCX in this conversation is mainly as a **reviewable structured output**, not as a magically solved accessibility target.

## Practical accessibility principle from the transcript

The best compact principle to preserve is:

Build systems that make structural accessibility deterministic where possible, and isolate the remaining human-judgment questions as explicit review items rather than burying them.
