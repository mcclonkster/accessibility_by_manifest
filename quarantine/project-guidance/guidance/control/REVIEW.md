# Review

## What was reviewed

- [start-to-finish-product-plan.md](/Users/computerk/github/accessibility_by_manifest/plans/start-to-finish-product-plan.md:1)
- Current implementation and operator-loop reality in `src/pdf_accessibility/`
- The sequencing, logic, scope control, and practical product path implied by the plan

## Review target

- File, artifact, task, milestone, or checkpoint:
  Full start-to-finish product plan after:
  - architecture completion
  - runnable review decisions
  - automatic review-decision template emission
  - first real `finreport25` operator-loop demonstration

## What the review checked

- sequencing
- logic
- scope control
- whether the plan reaches a real v0.1.0 product without unnecessary detours

## Strengths

- The plan is now explicitly product-first instead of cleanup-first.
- The sequencing generally matches code reality:
  - architecture first
  - honest/runnable workflow second
  - real blocker-clearing work next
- Scope control is materially better than before. The plan does not quietly expand beyond the v0.1.0 PDF wedge.
- The plan correctly centers the next value on real blocker classes from `finreport25` rather than more repo-surface work.
- The plan preserves the broader architecture while keeping PDF as the first active vertical.

## Issues found

### Issue 1
- Issue:
  The plan does not yet make a sharp enough distinction between "a human reviewed this table" and "the workflow now has enough structured information to write or finalize that table safely."
- Why it matters:
  A table review decision that merely clears a blocker could let the workflow look more complete without actually improving the writeback path or the downstream accessible outputs.
- Severity:
  high
- Suggested next move:
  Tighten Phase 2.1 so table decisions either:
  - produce explicit structured input the workflow can use, or
  - only clear the review blocker while still leaving finalization blocked when writeback support is insufficient.

### Issue 2
- Issue:
  The plan still needs one explicit v0.1.0 product acceptance gate, not just phase-by-phase progress.
- Why it matters:
  Without a single concrete acceptance pack, the project can keep improving locally without a crisp "this is now a real product slice" threshold.
- Severity:
  medium
- Suggested next move:
  Add one explicit product acceptance checkpoint near the end of the plan that requires:
  - one simple born-digital PDF that finalizes end to end
  - one complex real PDF like `finreport25` that clearly improves through the human loop
  - one canonical focused test command for the product slice

### Issue 3
- Issue:
  The plan is reasonable about OCR scope, but OCR remains the most likely place for scope explosion.
- Why it matters:
  If OCR turns into "solve scanned PDFs generally," the project will drift out of v0.1.0 and stall.
- Severity:
  medium
- Suggested next move:
  Keep the OCR step constrained to one explicit operator path for `IMAGE_ONLY_PAGE_OCR_REQUIRED`, such as sidecar text ingestion or a narrowly-scoped manual recovery artifact, and do not broaden beyond that in the next phase.

## Open questions

- Should table decisions in v0.1.0 be purely human signoff, or should they carry minimal structured table metadata that downstream writeback/HTML paths can consume?
- What is the smallest acceptable OCR-recovery artifact for v0.1.0 that moves real documents forward without creating a second large subsystem?

## Recommendation

Use one:
- needs more work before verification

## Notes for handoff

- The plan is directionally strong and worth following.
- This audit turn already tightened Phase 2.1 and added an explicit product
  acceptance pack to the plan.
- The remaining caution is OCR scope control, not a need for another broad
  replanning pass.
- The next implementation turn should still be table-blocker work, but with the writeback/finalization implications made explicit.
