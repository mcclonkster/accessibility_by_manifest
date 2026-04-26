**Project Definition**
`accessibility_by_manifest` is a local/open-first document accessibility remediation system. The architecture is:

```text
inputs -> extract -> normalize -> make accessible -> review -> output
```

The umbrella system is multi-format, but the current v0.1 product slice is PDF-first: take a PDF, extract evidence, normalize it into shared accessibility structure, run the PDF remediation workflow, expose honest blockers, accept human decisions, and emit earned outputs only when legal/safe. See [system_reference.md](/Users/computerk/github/accessibility_by_manifest/docs/design/system_reference.md:13) and [start-to-finish-product-plan.md](/Users/computerk/github/accessibility_by_manifest/plans/start-to-finish-product-plan.md:9).

**Purpose**
The purpose is not “PDF analysis” or “AI autotagging.” It is an evidence-backed remediation workflow that can produce a defensible handoff bundle: accessible PDF where feasible, accessible HTML as a sibling/alternate output where appropriate, review artifacts, validation findings, unresolved blockers, logs, and operator guidance.

**Goals**
- Build a real v0.1 PDF product path: `PDF -> accessible PDF` and `PDF -> accessible HTML`.
- Keep the workflow honest: `finalized`, `needs_review`, or `write_blocked`, with no fake conformance claims.
- Use deterministic extraction, normalization, reducers, transition guards, validation, and run records as the spine.
- Use AI/OCR/vision as sidecar evidence or explanations, not as unreviewed final truth.
- Let humans resolve ambiguous blockers for tables, figures, OCR, title/language, reading order, and structure.
- Preserve enough evidence for customer-facing reports and future conforming alternate-version guidance.

**What’s Done**
- The architecture has been centralized around the umbrella model in [system_reference.md](/Users/computerk/github/accessibility_by_manifest/docs/design/system_reference.md:141).
- Root and package agent instructions were split correctly: root repo contract plus PDF package contract in [src/pdf_accessibility/AGENTS.md](/Users/computerk/github/accessibility_by_manifest/src/pdf_accessibility/AGENTS.md:1).
- Shared normalized accessibility model and bridge into `src/pdf_accessibility/` exist.
- The PDF workflow has typed state, events, reducers, guards, nodes, persistence, writeback, validation, review decisions, and finalization control.
- Simple PDFs can finalize and emit `tagged_draft.pdf`, `accessible_output.pdf`, and `accessible_output.html`.
- Blocked complex PDFs now produce `review_decisions_template.json`, `ocr_recovery_template.json`, `operator_guide.json`, logs, metrics, and honest next-step guidance.
- OCR recovery for `IMAGE_ONLY_PAGE_OCR_REQUIRED` is implemented as a human/operator recovery path.
- Table and figure review paths now have tests for actionable decisions and blocker reduction.
- Optional run explanation exists as a post-run feature, not a workflow dependency.
- Canonical focused verification passed: `39 passed, 5 warnings`.

**In Progress**
- Product hardening around the real operator loop.
- Making complex PDFs like `finreport25` reduce blockers materially without pretending to finalize.
- Keeping table review, figure review, OCR recovery, writeback, validator findings, and operator guidance coherent.
- Strengthening `accessible_output.html` from “emitted artifact” toward a credible sibling output.
- Aligning docs/instructions with the current mental model so agents stop treating PDF as a separate product.

**Left Before v0.1.0 Done**
- Run a fresh clean `finreport25` workflow after deleted test outputs and record current blocker counts/artifacts.
- Confirm the current complex-document loop still materially improves blockers in real run artifacts, not only unit tests.
- Tighten remaining table structure/writeback boundaries so human table signoff cannot imply finalizable structure when the writeback path lacks enough information.
- Keep figure review actionable on real `finreport25`, not just fixtures.
- Add or confirm blocker detection for deferred features: links/annotations, forms, encrypted PDFs, complex layouts, difficult scans.
- Strengthen the customer handoff report contract: allowed claims, unresolved blockers, validation status, human review status, alternate-output guidance, and publication guidance.
- Keep final claim discipline explicit: internal `finalized` is not PDF/UA/WCAG/ADA conformance.
- Lock the v0.1 acceptance pack with one simple finalized PDF path and one complex honestly-blocked-but-improved PDF path. See [v0.1-product-acceptance-pack.md](/Users/computerk/github/accessibility_by_manifest/plans/v0.1-product-acceptance-pack.md:1).

**Definition Of Done For v0.1.0**
v0.1.0 is done when a newcomer can run the PDF workflow, see a simple born-digital PDF finalize end to end, see a complex PDF stop honestly with actionable next steps, apply review/OCR decisions, rerun, and observe real blocker reduction without any false accessibility or conformance claims.