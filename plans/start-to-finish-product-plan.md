# Start-To-Finish Product Plan

Active product plan.

This is the single active product execution plan for v0.1.0. Use it with:

- [project_overview.md](./project_overview.md)
- [v0.1-product-acceptance-pack.md](./v0.1-product-acceptance-pack.md)
- [../docs/design/system_reference.md](../docs/design/system_reference.md)
- [../src/pdf_accessibility/AGENTS.md](../src/pdf_accessibility/AGENTS.md)

Do not treat older root or draft plans as active instructions. They are frozen
supporting references only.

## Project Definition

`accessibility_by_manifest` is a local/open-first document accessibility
remediation system.

The umbrella architecture is:

```text
inputs -> extract -> normalize -> make accessible -> review -> output
```

The current v0.1.0 product slice is PDF-first:

```text
PDF input
-> extract evidence
-> normalize into shared accessibility structure
-> run the PDF remediation workflow
-> expose blockers honestly
-> accept human review/OCR decisions
-> emit earned PDF and HTML outputs
```

The repo is not conceptually PDF-only. PDF is the first serious implementation
slice because PDFs are the hardest and most urgent format.

## Purpose

The product is not a PDF parser, OCR wrapper, or AI autotagging demo.

It is an evidence-backed remediation workflow that produces defensible output
artifacts and handoff evidence:

- accessible PDF where feasible
- accessible HTML as a sibling/alternate output path where appropriate
- structured evidence
- review tasks and review decisions
- validator findings
- unresolved blockers
- run logs and run records
- operator guidance

The workflow must not bluff. It should stop as `needs_review` or `write_blocked`
when the system lacks enough evidence, structure, validation, or human decision
coverage to finalize safely.

## Goals

- Build a real v0.1 PDF product path: `PDF -> accessible PDF` and
  `PDF -> accessible HTML`.
- Keep terminal states honest: `finalized`, `needs_review`, or `write_blocked`.
- Use deterministic extraction, normalization, reducers, transition guards,
  validation, and run records as the spine.
- Use OCR, AI vision, and AI reasoning as sidecar evidence or explanations, not
  as unreviewed final truth.
- Let humans resolve ambiguous blockers for tables, figures, OCR, title/language,
  reading order, and structure.
- Preserve enough evidence for customer-facing reports and future
  conforming-alternate-version guidance.
- Keep claim discipline explicit: internal `finalized` is not PDF/UA, WCAG, ADA,
  Section 508, or legal conformance.

## Current State

Done:

- The umbrella architecture is centralized in
  [system_reference.md](../docs/design/system_reference.md).
- Root and package agent instructions are split correctly:
  - [../AGENTS.md](../AGENTS.md)
  - [../src/pdf_accessibility/AGENTS.md](../src/pdf_accessibility/AGENTS.md)
- Shared normalized accessibility model exists.
- Shared-core bridge into `src/pdf_accessibility/` exists.
- The PDF workflow has typed state, typed events, reducers, transition guards,
  nodes, graph orchestration, persistence, writeback, validation, review
  decisions, and finalization control.
- Simple PDFs can finalize and emit:
  - `tagged_draft.pdf`
  - `accessible_output.pdf`
  - `accessible_output.html`
- Blocked complex PDFs produce:
  - `review_decisions_template.json`
  - `ocr_recovery_template.json` when OCR recovery is needed
  - `operator_guide.json`
  - logs, metrics, and honest next-step guidance
- OCR recovery for `IMAGE_ONLY_PAGE_OCR_REQUIRED` is implemented as a
  human/operator recovery path.
- Table and figure review paths have tests for actionable decisions and blocker
  reduction.
- Optional run explanation exists as a post-run feature flag, not a workflow
  dependency.
- Canonical focused verification recently passed:
  - `39 passed, 5 warnings`

In progress:

- Product hardening around the real operator loop.
- Proving complex PDFs like `finreport25` reduce blockers materially in fresh run
  artifacts, not only tests.
- Keeping table review, figure review, OCR recovery, writeback, validator
  findings, and operator guidance coherent.
- Strengthening `accessible_output.html` from emitted artifact toward credible
  sibling output.
- Aligning docs and instructions so agents stop treating PDF as a separate
  product.

Known remaining risks:

- Table signoff must not imply finalizable table structure when writeback lacks
  enough structure.
- Figure review must stay actionable on real `finreport25`, not just fixtures.
- Deferred feature detection still needs to be confirmed for links/annotations,
  forms, encrypted PDFs, complex layouts, and difficult scans.
- Customer handoff report language still needs a clearer contract for allowed
  claims, unresolved blockers, validation status, review status, alternate-output
  guidance, and publication guidance.

## Invariants

- Do not collapse the architecture into PDF-only everywhere.
- Do not treat `src/pdf_accessibility/` as a standalone product architecture.
- Do not claim final output when the workflow is still blocked.
- Do not claim PDF/UA, WCAG, ADA, Section 508, or legal conformance from internal
  v0.1.0 finalization alone.
- Do not trade evidence quality for superficial output speed.
- Do not keep returning to cleanup/doc work when product blockers are clearer.
- Keep the shared core and current PDF remediation implementation layered rather
  than duplicative.

## Phase 0: Architecture And Core Spine

Status: done.

Delivered:

- umbrella system reference
- shared normalized accessibility model
- shared PDF and DOCX bridges
- integrated PDF remediation implementation
- HTML sibling output
- root/package agent instruction split
- aligned active docs

Exit criteria:

- architecture exists in code, tests, and active docs

## Phase 1: Make The PDF Workflow Honest And Runnable

Status: done enough for v0.1.0 continuation.

Delivered:

- honest terminal states
- honest validator/no-draft reporting
- review decisions runnable in the same run
- review-decision template generation
- automatic template emission on `needs_review`
- OCR recovery template path
- operator guide
- run logs and run-record artifacts

Remaining:

- refine artifact/operator ergonomics only when they remove real product
  friction

Exit criteria:

- a blocked run leaves the human with an honest usable next step

## Phase 2: Prove The Complex-PDF Operator Loop

Status: active.

Outcome:

- a real complex document can reduce blockers materially through review/OCR
  decisions without pretending to finalize

Work:

1. Run a fresh clean `finreport25` workflow and record current blocker counts and
   generated artifacts.
2. Apply a representative combined operator input set:
   - title/language decision where needed
   - table review decision
   - figure alt-text or decorative decision
   - OCR recovery text for image-only pages where present
3. Rerun and confirm blocker count drops honestly.
4. Confirm unresolved blockers remain visible and finalization does not occur
   unless the writeback path has enough structure.

Acceptance criteria:

- untreated `finreport25` stops honestly in `needs_review`
- run folder includes actionable templates and `operator_guide.json`
- combined rerun materially reduces blockers
- blocker reduction is visible in persisted artifacts
- the workflow still refuses to finalize if structural blockers remain

## Phase 3: Strengthen Tagged Draft Writeback

Status: partially done, still narrow.

Outcome:

- supported simple structures produce stronger tagged drafts, while unsupported
  cases stop for concrete reasons

Work:

- lock supported simple structures:
  - headings
  - paragraphs
  - simple lists
  - simple tables within accepted scope
  - document title
  - primary language
- keep unsupported cases explicit:
  - unresolved complex tables
  - unsupported figures
  - unsupported annotations/links
  - unsupported content-stream situations
- keep `writeback_report.json` clear about:
  - planned
  - written
  - skipped
  - unsupported

Acceptance criteria:

- simple scoped documents finalize reliably
- complex documents stop for concrete, inspectable reasons
- internal validator and finalization agree with writeback reality

## Phase 4: Strengthen Accessible HTML As A Sibling Output

Status: started, not mature.

Outcome:

- HTML is not merely emitted; it is credible for the supported simple structure
  slice

Work:

- improve projection from the shared normalized model
- improve tables and figures in HTML output
- preserve artifact omission and reading order
- keep HTML policy local to the HTML output path

Acceptance criteria:

- finalized simple PDF runs produce useful `accessible_output.html`
- HTML output is tested on headings, paragraphs, lists, simple tables, and basic
  figures
- HTML is not described as a conforming alternate version unless the handoff
  report can support that claim

## Phase 5: Customer Handoff Contract

Status: not yet mature.

Outcome:

- a run produces enough evidence for a customer/operator to understand what was
  remediated, what remains unresolved, and what should be published

Work:

- define report sections:
  - source summary
  - output artifacts
  - internal validation status
  - human review status
  - unresolved blockers
  - known limitations
  - alternate-output guidance
  - publication guidance
- define allowed claim language:
  - internal v0.1.0 gates passed
  - generated accessible-output candidate
  - unresolved blockers remain
  - external conformance not claimed
- keep logs and artifacts useful without dumping unnecessary sensitive content

Acceptance criteria:

- a newcomer can inspect a run folder and understand the status without reading
  code
- customer-facing language remains honest and non-overclaiming

## Phase 6: Lock v0.1.0 Product Readiness

Status: final phase.

Outcome:

- the repo has a credible first product slice, not just a promising workflow

Work:

- define one simple born-digital PDF that finalizes end to end
- define one complex real PDF such as `finreport25` that improves materially
  through the human review loop without pretending to finalize
- keep the active acceptance gate in
  [v0.1-product-acceptance-pack.md](./v0.1-product-acceptance-pack.md)
- keep the canonical focused verification command current
- tighten user-facing docs:
  - quickstart
  - operator loop
  - v0.1 limits
  - meaning of `needs_review`

Acceptance criteria:

- simple success path works
- complex honest-stop path works
- operator loop improves real artifacts
- terminal and run artifacts tell the human what to do next

## Definition Of Done For v0.1.0

v0.1.0 is done when a newcomer can:

1. Run the PDF workflow.
2. See a simple born-digital PDF finalize end to end.
3. See a complex PDF stop honestly with actionable next steps.
4. Apply review/OCR decisions.
5. Rerun and observe real blocker reduction.
6. Inspect output artifacts, validation status, logs, and operator guidance.
7. Understand what is safe to claim and what is not.

Done does **not** mean universal PDF remediation. It means the narrow workflow is
executable, honest, stable, and demonstrably useful.

## Immediate Next Turn

Run a fresh clean `finreport25` workflow and compare the current real output to
the v0.1 acceptance pack:

1. Record untreated blocker count and generated artifacts.
2. Confirm templates and `operator_guide.json` are present.
3. Apply a small combined review/OCR input set if available.
4. Confirm blocker reduction is persisted.
5. Confirm finalization remains blocked if unresolved structural blockers remain.
