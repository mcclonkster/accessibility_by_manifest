# Cleanup Report

Updated after reorganizing:

- `docs/`
- `plans/`
- the prior custom planning/control folder
- `reference/`

## Current Project Shape

The repository now has a professional repo-guidance layout:

- `AGENTS.md`: repo/package agent operating contract.
- `docs/design/`: active architecture and design documentation.
- `docs/reference/`: standards, official sources, and PDF technical reference.
- `plans/`: active product plan, supporting refactor plan, acceptance gate,
  status, tasks, decisions, and cleanup report.
- `quarantine/`: historical, superseded, under-labeled, or non-project material
  removed from active guidance.

## Actions Taken

- Moved active project-control files into `plans/`:
  - `status.md`
  - `tasks.md`
  - `decisions.md`
  - `cleanup-report.md`
- Added `plans/README.md` as the active planning index.
- Added `docs/README.md` and `docs/reference/README.md` indexes.
- Moved official source captures into `docs/reference/official/`.
- Moved PDF/PDF accessibility reference captures into `docs/reference/pdf/`.
- Moved historical chat transcripts into `quarantine/docs-chats/`.
- Moved superseded PDF spec drafts into `quarantine/pdf-spec-drafts/`.
- Moved old project-guidance/control material into
  `quarantine/project-guidance/`.
- Moved the old under-labeled `reference/` directory into
  `quarantine/reference/`.
- Promoted the runtime PDF manifest schema out of quarantine into
  `accessibility_by_manifest/manifest/schemas/` because validation code depends
  on it.
- Moved `.DS_Store` out of active docs into `quarantine/system-files/`.

## Keep Active

- `AGENTS.md`
- `README.md`
- `docs/design/`
- `plans/README.md`
- `plans/start-to-finish-product-plan.md`
- `plans/module-responsibility-refactor-plan.md`
- `plans/v0.1-product-acceptance-pack.md`
- `plans/project_overview.md`
- `plans/pdf-manifest-evidence-sizing-policy.md`
- `plans/status.md`
- `plans/tasks.md`
- `plans/decisions.md`

## Supporting Reference Only

- `docs/reference/official/`
- `docs/reference/pdf/`

Reference material can support standards lookup and implementation research, but
it is not active planning or current instruction.

## Quarantined

- `quarantine/docs-chats/`
- `quarantine/pdf-spec-drafts/`
- `quarantine/project-guidance/`
- `quarantine/reference/`
- `quarantine/system-files/`

Quarantined files are preserved for history and recovery. They should not guide
new work unless a specific point is promoted back into active docs or plans.

## Remaining Cleanup Questions

1. Decide whether any `test_outputs/not_public/` material should become curated
   fixtures or remain private/local evidence.
2. Decide the explicit product status of `.agents/` and
   `multi_agent_pdf_tagger_app.jsx`.
3. Keep generated run outputs out of the active docs/plans cleanup decision
   unless a future task explicitly targets generated artifacts.

## Current Recommendation

Treat cleanup as secondary now. The active guidance surface is small enough to
resume product work from:

1. `plans/start-to-finish-product-plan.md`
2. `plans/module-responsibility-refactor-plan.md`
3. `plans/v0.1-product-acceptance-pack.md`
4. `docs/design/system_reference.md`
5. `AGENTS.md`
6. `src/pdf_accessibility/AGENTS.md`
