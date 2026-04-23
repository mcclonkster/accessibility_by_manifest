---
title: v0.1.0 Output, Write-Back, and Finalization Spec
filename: v0-1-0-output-write-back-and-finalization-spec.md
type: specification
status: draft
created: 2026-04-21
updated: 2026-04-21
origin: chat
tags:
  - pdf
  - accessibility
  - tagged-pdf
  - output
  - finalization
topics:
  - PDF accessibility
  - Tagged PDF
  - Output workflow
aliases:
  - v0.1.0 output spec
sources: []
cssclasses: []
notes:
  - Locks the real PDF output path
  - Draft, validation, review, and finalization are first-class
---

# v0.1.0 output, write-back, and finalization spec

## Purpose

Lock the part that matters most:

**the system must produce a real PDF output path that can end in an accessible PDF, not just good internal analysis.**

For v0.1.0, the product is not “claims about a PDF.” It is a controlled workflow that can produce:

1. a tagged PDF draft
2. a validation result
3. a review task set for unresolved issues
4. a reviewed/finalized status
5. and, when unresolved blockers are cleared, a final accessible PDF output

## Governing output requirement

Every run must end in one of these document states:

1. **Finalized**
   - A tagged PDF exists.
   - Blocking validator failures are cleared.
   - Blocking review issues are cleared.
   - The document is eligible to be treated as the current best accessible output.

2. **Needs review**
   - A tagged PDF draft exists.
   - One or more blocking semantic or validation issues remain.
   - The system must not present the draft as final.

3. **Write-blocked**
   - The system could not safely produce a tagged draft because the structure/mapping state was too unstable.
   - Review tasks must explain why.

## Required output artifacts

### Always required

- `input.pdf`
- `document_state.json`
- `claims.json`
- `review_tasks.json`
- `run_log.json`

### Required when draft writing succeeds

- `tagged_draft.pdf`
- `validation_report.json`
- `finalization_status.json`

### Required when finalized

- `accessible_output.pdf`
- `finalization_status.json`

### Optional but strongly recommended

- `region_debug.json`
- `page_debug.json`
- `validator_trace.json`
- `review_decisions.json`

## Document lifecycle

### Phase 1. Intake
1. Open input PDF.
2. Classify document at a coarse level.
3. Render pages.
4. Initialize shared state.

### Phase 2. Evidence collection
1. Run vision analysis.
2. Run OCR/layout analysis.
3. Run native PDF inspection.
4. Store all evidence in shared state.

### Phase 3. Interpretation
1. Infer region meaning.
2. Infer accessibility requirements.
3. Check caption associations.
4. Check artifact/repetition patterns.

### Phase 4. Planning
1. Create structure plans.
2. Create document-level consistency claims.
3. Create mapping plans.
4. Run behavior checks.

### Phase 5. Region commit gating
1. Decide whether each region is committable.
2. Reopen unstable regions.
3. Escalate unresolved regions when retry limit is reached.

### Phase 6. Draft write-back
1. Write committed structure into a tagged draft PDF.
2. Save `tagged_draft.pdf`.
3. Record exactly which regions were written and which were omitted or escalated.

### Phase 7. Validation
1. Run validator on `tagged_draft.pdf`.
2. Save validator findings.
3. Map validator findings back to document state where possible.

### Phase 8. Review routing
1. Convert unresolved issues into review tasks.
2. Mark the run as:
   - finalized
   - needs review
   - write-blocked

### Phase 9. Finalization
1. If no blocking issues remain, promote the reviewed result to `accessible_output.pdf`.
2. If blocking issues remain, do not finalize.

## Write-back contract

v0.1.0 must contain a real write-back path.

### Write-back must do

1. create or update the document-level structure representation
2. write approved structure/mapping work into a tagged draft PDF
3. preserve the original PDF separately
4. record what was written and what was not

### Write-back must not do

1. invent semantics during the write step
2. silently resolve unresolved objections
3. mark the draft final automatically
4. overwrite the only copy of the source PDF

### Minimum write-back output for v0.1.0

At minimum, write-back must support the v0.1.0 scope items:

- headings
- paragraphs
- lists
- simple tables
- artifacts
- basic figures
- title/language metadata path

If a region is outside scope, the writer must:
- omit finalization for that region
- create review tasks
- keep the document honest

## Validation rules

Validation happens after draft writing.

Validation must:
- run against the tagged draft PDF
- save machine-verifiable failures and warnings
- map findings back to document, page, region, or mapping plan where possible
- update finalization state

Validation must not:
- declare semantic correctness on its own
- override unresolved human-judgment problems
- finalize the document by itself

## Finalization rules

A document may be finalized only when all of these are true:

1. `tagged_draft.pdf` exists
2. no blocking machine-validation failures remain
3. no blocking review tasks remain open
4. no region with a required output role is still unresolved in a way that invalidates the document-level result
5. finalization status is explicitly set to `finalized`

When finalized, the system produces:

- `accessible_output.pdf`
- `finalization_status.json`

## Meaning of “accessible at the end” for v0.1.0

For v0.1.0, “accessible at the end” means:

1. the system can produce a tagged PDF draft
2. the draft can be validated
3. unresolved issues are turned into explicit review tasks
4. the system can distinguish clearly between:
   - draft only
   - needs review
   - finalized output
5. the system only emits `accessible_output.pdf` when blocking issues are cleared

It does not mean:

- fully automatic, universal PDF remediation
- no human review
- full support for all PDF accessibility cases
- perfection on forms, formulas, complex charts, or other deferred content classes
