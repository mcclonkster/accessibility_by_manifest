# Quarantine

## Summary

This README records cleanup candidates for manual review only.

The cleanup audit that produced these candidates was non-destructive. This file
has now been refreshed against current repo state. It is a decision queue, not
proof that files were physically moved into quarantine.

Exceptions:

- `QUARANTINE/guidance/` contains guidance files that were deliberately moved
  out of the active navigation surface. Those moves were made to reduce
  duplicate authority, not because the files are unsafe to read.
- `QUARANTINE/plans/` contains plans that are no longer active execution
  guidance. Active planning now lives in `plans/start-to-finish-product-plan.md`,
  `plans/module-responsibility-refactor-plan.md`, and
  `plans/v0.1-product-acceptance-pack.md`.

Current cleanup themes:

- generated output is mixed with tracked repo content
- historical material is present but not always labeled strongly enough
- some document bundles appear duplicated
- some tracked tooling/prototype surfaces have unclear ownership

## Current Inventory Basis

This refresh is based on the actual current repo state:

- `project-file-structure-md/QUARANTINE/` now contains this README plus a
  `guidance/` subtree of frozen or demoted guidance files and a `plans/`
  subtree of frozen or demoted plan files
- there is no `project-file-structure-md/QUARANTINE/payloads/` directory
- `multi_agent_pdf_tagger_app.jsx` exists at the repo root
- older `finreport25` tracked artifacts are currently deleted from the working
  tree
- a newer ignored local run still exists under `test_outputs/finreport25_workflow_runs/`
- the generated-output policy is now explicit:
  - current `finreport25_manifest_run/` and `finreport25_workflow_runs/` are disposable local verification artifacts
  - `test_outputs/not_public/` is the only plausible curated-output surface and needs its own later decision
- the duplicated handoff bundle under `docs/chats/codex_python_handoff_bundle/`
  is currently present as tracked deletions in git status rather than as a
  moved quarantine payload

## Delete Manually

### Candidate 1
- Path: `test_outputs/finreport25_manifest_run/`
- Type: obsolete generated output
- Evidence: The old tracked manifest-first run is currently deleted from the working tree and its rerun path is ignored by `.gitignore`. This directory previously included a manifest large enough to exceed GitHub's file size limit in local history.
- Risk: Low to medium. These files are useful as short-term verification evidence, but they are generated artifacts rather than source artifacts. Deleting them from git should not remove implementation truth, but it may remove a convenient local comparison sample.
- Recommended action: Keep treating this as disposable local verification output. Do not restore it as tracked fixture material unless a later explicit fixture decision says otherwise.
- Decision status: delete manually

### Candidate 2
- Path: `test_outputs/finreport25_workflow_runs/`
- Type: obsolete generated output
- Evidence: The older tracked workflow run is currently deleted from the working tree, while a newer ignored local run still exists under this directory. That means the repo is currently mixing tracked-history cleanup with local rerun evidence.
- Risk: Low to medium. It contains useful run evidence, but it is generated output, not authoritative source code or design intent.
- Recommended action: Keep the tracked deletion for the older workflow run and continue treating newer reruns here as disposable local verification artifacts only.
- Decision status: delete manually

## Merge Manually

### Candidate 0
- Path: `project-file-structure-md/QUARANTINE/guidance/`
- Type: duplicate document
- Evidence: This subtree now contains formerly active guidance files that were creating redundant authority surfaces, including `PROJECT.md`, older planning/control docs, and completed blueprints.
- Risk: Low if left as frozen reference, medium if contributors keep treating it as active guidance.
- Recommended action: Keep it as frozen reference only. Do not move these files back into the active index unless a specific file is intentionally reactivated.
- Decision status: keep

### Candidate 3
- Path: `docs/chats/codex_python_handoff_bundle/`
- Type: duplicate document
- Evidence: The bundle overlaps strongly with `docs/design/` and its files are currently showing as tracked deletions in git status, which suggests cleanup has started but the canonical/reference decision is not yet recorded cleanly.
- Risk: Medium. The handoff bundle may preserve useful wording or intermediate context, so deleting it casually could remove context that has not been consciously preserved elsewhere.
- Recommended action: Keep the current tracked deletions. `docs/design/` is the canonical design-doc surface; if any missing wording becomes important later, merge it intentionally into `docs/design/` rather than restoring the duplicate bundle.
- Decision status: merge manually

### Candidate 4
- Path: `multi_agent_pdf_tagger_app.jsx`
- Type: unused draft
- Evidence: This file currently exists at the repo root and has been explicitly described as part of the direction the project is going in.
- Risk: Medium. It is easy to misclassify because it is not wired into a frontend app structure yet, but it may still be intentional forward direction.
- Recommended action: Do not treat this as quarantined. Keep it out of cleanup actions unless a later product-direction decision says otherwise.
- Decision status: investigate

## Archive Manually

### Candidate 5
- Path: `docs/chats/`
- Type: stale document
- Evidence: This directory holds chat transcripts, tavern exports, and handoff material. Current planning files already treat `docs/chats/` as historical/supporting context rather than current authority.
- Risk: Medium. It may contain valuable research rationale, but it is easy for contributors to mistake it for active design documentation.
- Recommended action: Archive manually as explicit historical reference if the project wants a cleaner main docs surface, but do not delete without checking whether specific transcripts are still cited.
- Decision status: investigate

## Investigate

### Candidate 6
- Path: `.agents/`
- Type: unclear ownership
- Evidence: `.agents/` contributes 114 tracked files, including skills, agent configs, helper scripts, fixtures, and tests. It is not part of the Python package entry points in `pyproject.toml`, but it is referenced as repo-local tooling context in `AGENTS.md` and planning files.
- Risk: High. Removing or relocating it without a deliberate decision could break the team’s agent workflow or erase useful local operating conventions.
- Recommended action: Investigate whether `.agents/` is intentionally repo-scoped tooling, a vendored shared toolkit, or something that should live outside this product repo.
- Decision status: investigate

### Candidate 7
- Path: `archive/`
- Type: confusing directory
- Evidence: `archive/` contains its own `pyproject.toml`, historical scripts, test inputs, test outputs, JSON/YAML artifacts, and reports. Existing findings already say it is historical and should not drive current planning, but its executable-looking structure can still confuse contributors.
- Risk: High. It may contain the only copy of earlier workflow history or legacy examples, so deletion is risky. The main issue is clarity, not mere age.
- Recommended action: Investigate whether `archive/` should remain in-repo with stronger labeling, be reduced to a slimmer historical subset, or be moved out later as a deliberate archival action.
- Decision status: investigate

### Candidate 8
- Path: `archive/test_outputs/`
- Type: obsolete generated output
- Evidence: This directory contains tracked generated DOCX, Markdown, JSON, YAML, and PNG output from an archived PPTX/DOCX workflow. It is historical output rather than active implementation.
- Risk: Medium. These files may serve as legacy examples or regression evidence for the archived workflow, so deletion without review could lose useful historical context.
- Recommended action: Investigate whether a minimal curated subset should remain while the rest is removed manually from git later.
- Decision status: investigate

### Candidate 12
- Path: `test_outputs/not_public/`
- Type: investigate fixture surface
- Evidence: This is the only output area that still looks intentionally separated from casual reruns. It contains multiple workflow-output directories and private artifacts rather than a single ad hoc rerun.
- Risk: Medium. It may represent curated private fixtures or useful regression evidence, but the repo has not yet recorded whether it is canonical, historical, or merely convenient local storage.
- Recommended action: Investigate separately from the disposable `finreport25_*` run directories. Do not let the broader generated-output cleanup accidentally sweep this surface away without an explicit fixture policy.
- Decision status: investigate

## Keep

### Candidate 9
- Path: `accessibility_by_manifest/`
- Type: keep
- Evidence: This package is active implementation with current code, tests, and documented CLI paths. It is not a cleanup target.
- Risk: High if mistakenly treated as legacy.
- Recommended action: Keep. Do not collapse or archive without the explicit package-relationship decision.
- Decision status: keep

### Candidate 10
- Path: `src/pdf_accessibility/`
- Type: keep
- Evidence: This is the current v0.1.0 PDF workflow implementation path governed by `AGENTS.md`, with targeted tests and active planning relevance.
- Risk: High if mistakenly treated as duplicate or prototype code.
- Recommended action: Keep. Use the package-relationship decision before any structural move.
- Decision status: keep

### Candidate 11
- Path: `docs/design/`
- Type: keep
- Evidence: These are the strongest in-repo design docs outside the planning surface and are less ambiguous than `docs/chats/` and `docs/pdf_spec_drafts/`.
- Risk: Medium if mixed up with duplicate/historical bundles, but low if kept as canonical design docs.
- Recommended action: Keep as the sole canonical in-repo design-doc surface. Prefer this directory over duplicated handoff bundles when deciding canonical design documentation.
- Decision status: keep

## Decisions Log

- 2026-04-24: Non-destructive cleanup pass recorded candidates only. No file deletions, moves, renames, or history rewrites were performed.
- 2026-04-24: Cleanup inventory refreshed against actual repo state. This file is now a current decision queue rather than a placeholder pointing at nonexistent quarantine payloads.
- 2026-04-25: `docs/design/` was explicitly ratified as the sole canonical design-doc surface. The duplicate `docs/chats/codex_python_handoff_bundle/` deletions should remain rather than be restored casually.
- 2026-04-26: Moved two inactive plan files into `QUARANTINE/plans/`: the old root `v0.1.0_plan.md` and the frozen dependency-contract draft.
