# Status

Active execution snapshot.

Use with:
- [system reference](../docs/design/system_reference.md)
- [product plan](../plans/start-to-finish-product-plan.md)
- [workflow rules](../AGENTS.md)

## Current Phase

- Product workflow hardening, with cleanup/consolidation now secondary.

## Current Overall Status

- The codebase is healthier than the old planning files implied.
- The architecture blueprint is complete and verified.
- The strongest current momentum is no longer cleanup. Recent turns materially
  improved the PDF workflow operator path:
  - honest validator/no-draft reporting
  - runnable review decisions
  - review-decision template generation
- Cleanup and consolidation still exist, but they are no longer the clearest
  immediate value compared with product workflow completion work.
- The repository now has an explicit umbrella pipeline architecture and one
  active deep product slice.
- The v0.1.0 PDF workflow should use `AGENTS.md` and `src/pdf_accessibility/`
  as its governing implementation path.
- Umbrella architecture reference now lives in
  `docs/design/system_reference.md`.
- PDF is the first active serious slice, with accessible PDF and accessible
  HTML as the current sibling outputs from the same workflow state.

## Current Health

- improving

Reason: the product workflow is materially more complete than before, and the
guidance surface has now been reduced, but figure handling still blocks a full
real-document operator loop.

## Verification This Pass

- Inventory covered source-relevant repo areas: `.agents/skills`, `AGENTS.md`, `README.md`, active `plans/`, `docs/design`, `docs/reference`, top-level `quarantine`, `accessibility_by_manifest`, `src/pdf_accessibility`, `tests`, `test_inputs`, `test_outputs`, and `archive`.
- Full test suite passed with `.venv/bin/python -m pytest`: 67 passed earlier in
  the cleanup pass, and subsequent architecture turns kept targeted suites green.
- Targeted v0.1.0 workflow tests now cover the integrated PDF path including
  shared-model bridge and HTML artifact handling.
- System `pytest tests/pdf_accessibility` is not reliable because system Python was missing `pikepdf`.

## What Changed Recently

- Active planning/control files now live in `plans/`.
- Official and PDF reference captures now live under `docs/reference/`.
- Historical chats, draft specs, old project guidance, old reference material,
  and non-project system files now live under top-level `quarantine/`.
- Root docs were reduced and re-anchored around one canonical system reference.
- The generated `finreport25` workflow run was inspected as evidence: it ends
  honestly in `needs_review` for the integrated PDF remediation implementation on a complex real
  document.
- The broader shared-core PDF path still produces master manifests,
  extractor-specific manifests, normalized views, and review artifacts for
  evidence inspection and bridge work.

## Active Blockers

- Some older specs use superseded terminology or node names; they cannot be
  read as current truth without the terminology freeze.
- The real `finreport25` operator loop can now clear document metadata,
  selected table review blockers, and OCR-required page blockers, but it still
  stops honestly on the larger remaining table set and figure-review blockers.

## Open Questions

- Should generated `test_outputs/` be curated, cleaned, or excluded from planning evidence except when explicitly named?
- Which legacy shared-core entry points should remain user-facing versus being
  framed as developer/debugging paths after doc alignment is complete?

## Next Planning Moves

1. Tighten figure-review decisions so meaningful/decorative figure outcomes can
   clear real blockers.
2. Decide whether the remaining table path needs richer structured input beyond
   human signoff alone.
3. Return to unresolved cleanup ownership surfaces only after the operator path
   handles figures as well as metadata, tables, and OCR.

## Next Checkpoint

- Trigger: after figure-review decisions land and are tried on `finreport25`.
- Purpose: confirm the human-in-the-loop workflow now covers the major current
  blocker classes in the real product slice.
