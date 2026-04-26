# Tasks

Active work queue.

## Active

- [ ] Task: Make figure review blockers actionable
  - Owner: Codex
  - Next action: add real figure review decision types and prove them on `finreport25`.
  - Notes: Metadata, selected table blockers, and OCR-required page blockers now have real operator paths. Figure blockers are the next product gap.

- [ ] Task: Refactor mixed-responsibility Python orchestration modules
  - Owner: Codex
  - Next action: execute Step 1 of `plans/module-responsibility-refactor-plan.md` by thinning `accessibility_by_manifest/inputs/pdf/__init__.py`.
  - Notes: Use the module-responsibility refactor plan as the implementation sequence. Focus on splitting mixed orchestration, not on cosmetic package churn.

## Blocked

## Waiting

## Next

- [ ] Task: Decide explicit status of `.agents/` and `multi_agent_pdf_tagger_app.jsx`
  - Why next: cleanup notes still describe unclear ownership while the actual repo now treats these surfaces differently.
  - Notes: Do not quarantine active product-direction material. `multi_agent_pdf_tagger_app.jsx` currently exists at repo root.

## Done

- [x] Task: Read project-planning skill
  - Completed on: 2026-04-22
  - Notes: Used to repair `PLAN.md`, `STATUS.md`, `DECISIONS.md`, and `HANDOFF.md`.

- [x] Task: Read repo-local workflow guardrails
  - Completed on: 2026-04-22
  - Notes: Used `pdf-workflow-state`, `pdf-writeback-output`, and `terminology-scope-check`.

- [x] Task: Run full repo tests
  - Completed on: 2026-04-22
  - Notes: `.venv/bin/python -m pytest` passed 67 tests.

- [x] Task: Declare project management file location canonical
  - Completed on: 2026-04-24
  - Notes: Superseded on 2026-04-26. Active planning/control now lives in `plans/`; old project-guidance material lives in `quarantine/project-guidance/`.

- [x] Task: Decide package relationship
  - Completed on: 2026-04-24
  - Notes: Chosen relationship is layered, not merge-now and not unrelated parallel tracks. `accessibility_by_manifest/` remains the broader evidence/extraction layer; `src/pdf_accessibility/` remains the v0.1.0 workflow/remediation layer.

- [x] Task: Add explicit historical markers for reference directories
  - Completed on: 2026-04-24
  - Notes: Superseded by the 2026-04-26 repository reorganization. Historical chats and draft specs now live under `quarantine/`; reference captures live under `docs/reference/`.

- [x] Task: Update README/PROJECT to match implemented architecture
  - Completed on: 2026-04-24
  - Notes: Root docs now reflect the shared-core plus current PDF remediation implementation, current entrypoints, and accessible HTML as a sibling output path.

- [x] Task: Refresh cleanup inventory against actual repo state
  - Completed on: 2026-04-24
  - Notes: `QUARANTINE/README.md`, `CLEANUP-REPORT.md`, and `TASKS.md` now reflect that there is no quarantine payload directory, `multi_agent_pdf_tagger_app.jsx` is present at repo root, and the current `finreport25` cleanup issue is a mix of tracked deletions plus ignored rerun output.

- [x] Task: Decide generated-output policy for current `finreport25` artifacts
  - Completed on: 2026-04-25
  - Notes: `test_outputs/finreport25_manifest_run/` and `test_outputs/finreport25_workflow_runs/` are now treated as disposable local verification artifacts, not curated fixtures. Any future fixture decision should focus separately on `test_outputs/not_public/`.

- [x] Task: Decide canonical status of the old chat handoff bundle
  - Completed on: 2026-04-25
  - Notes: `docs/design/` is now the sole canonical design-doc surface. The tracked deletions under the duplicate handoff bundle should remain as cleanup rather than be restored as a second authority surface.

- [x] Task: Fix validator/no-draft artifact honesty
  - Completed on: 2026-04-25
  - Notes: `validator_findings.json` now reports `validation_state: skipped`, `draft_available: false`, and `passed: false` when no tagged draft exists. The validator node, persistence snapshot, and workflow tests were updated together.

- [x] Task: Make review decisions runnable end to end
  - Completed on: 2026-04-25
  - Notes: The PDF workflow can now accept `--review-decisions`, seed `review_decisions_input.json`, apply document-level decisions during the same run, rerun the structure-planning tail, and finalize when those decisions clear the blockers. Focused workflow, CLI, and reducer tests were added and passed.

- [x] Task: Generate review-decision templates from review tasks
  - Completed on: 2026-04-25
  - Notes: Added a `template-review-decisions` CLI command that reads `review_tasks.json` and writes `review_decisions_template.json` with actionable `decisions` and separate `manual_only_tasks` for issues that should not get misleading auto-fix templates.

- [x] Task: Auto-write review-decision templates for `needs_review` runs and try the real `finreport25` loop
  - Completed on: 2026-04-25
  - Notes: The snapshot/artifact layer now writes `review_decisions_template.json` automatically for unresolved `needs_review` runs, registers it in `artifact_manifest.json`, and removes it from finalized runs. Focused artifact/workflow/CLI tests passed. On a real `finreport25` run, the template was emitted automatically; a rerun with a real title decision resolved `pdf_review_0001_document_title_missing` while correctly leaving OCR/table/figure blockers active.

- [x] Task: Implement OCR recovery path for `IMAGE_ONLY_PAGE_OCR_REQUIRED`
  - Completed on: 2026-04-26
  - Notes: Added CLI support for `--ocr-recovery`, seeded run-local `ocr_recovery_input.json`, and implemented `ocr_layout_analysis` so manual OCR recovery text is loaded as workflow evidence, registered as an artifact, and resolves matching `IMAGE_ONLY_PAGE_OCR_REQUIRED` tasks. Focused OCR/review/workflow tests passed. On a real `finreport25` rerun, the page 75 and page 94 OCR blockers resolved while the run still ended honestly in `needs_review`.

- [x] Task: Reduce active guidance surface and move stale guides to quarantine
  - Completed on: 2026-04-25
  - Notes: Added `docs/design/system_reference.md` as the single architecture reference, trimmed the active index to a minimum set, marked companion docs as supporting reference only, and moved stale planning/control/root guidance files into `quarantine/project-guidance/`.

- [x] Task: Reorganize active docs, plans, reference, and quarantine surfaces
  - Completed on: 2026-04-26
  - Notes: Active tracking moved into `plans/`; official and PDF references moved under `docs/reference/`; historical chats, draft specs, old project guidance, old reference material, and non-project system files moved under top-level `quarantine/`.

- [x] Task: Audit Python module boundaries against the system mental model
  - Completed on: 2026-04-25
  - Notes: Used the `python-code-quality` standard to map current modules to pipeline responsibilities, identify mixed-responsibility orchestration points, and write `plans/module-responsibility-refactor-plan.md` as the concrete migration sequence.

## Resume Notes

- If restarting, do this first: read `../docs/design/system_reference.md`, `status.md`, `tasks.md`, `decisions.md`, and `../AGENTS.md`.
- Re-open these files first: `../README.md`, `../plans/start-to-finish-product-plan.md`, `../AGENTS.md`, `src/pdf_accessibility/graph/build_graph.py`, `src/pdf_accessibility/persistence/artifacts.py`.
- Watch out for: stale draft-spec terminology, generated output that is useful but not authoritative, and accidental expansion beyond v0.1.0.
