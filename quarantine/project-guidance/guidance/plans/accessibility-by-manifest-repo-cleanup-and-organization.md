# Blueprint: Accessibility By Manifest Repo Cleanup And Organization

## Objective

Clean and organize the repository so contributors can tell:

- what code is active
- what material is historical
- what outputs are generated and should stay out of git
- which package path governs v0.1.0 PDF workflow work
- where planning and execution should happen next

This plan assumes **direct mode** because git is available but GitHub CLI is not installed in the current environment.

## Pre-Flight Snapshot

- Repository: `/Users/computerk/github/accessibility_by_manifest`
- Current branch: `main`
- Remote: `origin https://github.com/mcclonkster/accessibility_by_manifest.git`
- `gh`: unavailable
- Current planning surface: `project-file-structure-md/`
- Current governing workflow source: `AGENTS.md`
- Current active implementation tracks:
  - `accessibility_by_manifest/`
  - `src/pdf_accessibility/`

## Invariants

These must remain true throughout every step:

- Do not delete files casually based on age or location alone.
- Do not treat generated outputs as source of truth.
- Do not let cleanup work silently change v0.1.0 workflow scope.
- Keep `AGENTS.md` as the governing source for current v0.1.0 PDF workflow work unless a later explicit decision changes that.
- Preserve the ability to run `.venv/bin/python -m pytest`.
- Avoid repo-wide moves until package-boundary and planning-location decisions are explicit.

## Dependency Graph

```text
Step 1 -> Step 2 -> Step 5 -> Step 6
Step 1 -> Step 3 -> Step 6
Step 1 -> Step 4 -> Step 6
Step 5 -> Step 7
Step 6 -> Step 7
Step 7 -> Step 8
```

## Parallelism Summary

After Step 1:

- Step 3 and Step 4 can run in parallel.
- Step 5 should wait for Step 2 because fixture/output policy depends on the chosen planning and artifact rules.

## Anti-Patterns To Avoid

- Cleaning by vibe: deleting `archive/`, `.agents/`, or `test_outputs/` without explicit evidence.
- “Documentation cleanup” that accidentally decides architecture by wording alone.
- Tracking fresh generated artifacts to demonstrate success.
- Renaming or moving both active package trees in the same step.
- Fixing the push problem only in the working tree instead of removing the large blob from pushed history.
- Updating README before the package-relationship decision is written down.

## Step 1: Unblock Git History And Freeze Generated Run Output Boundaries

- Status: ready
- Model tier: default
- Depends on: none
- Parallelizable with: none
- Rollback: reset the local branch to `origin/main` and re-apply only the intended ignore-rule and planning changes

### Context Brief

The repo currently has a push blocker because a generated manifest over GitHub's 100 MB limit exists in local commits even though it was later removed from the working tree. The repo also now ignores the new `finreport25` run directories, but ignore rules do not rewrite history.

### Task List

1. Rewrite local history so the oversized `test_outputs/finreport25_manifest_run/finreport25_manifest.json` blob is absent from the commits being pushed.
2. Verify the blob is gone from `HEAD`.
3. Confirm the new ignore rules cover the generated run directories.
4. Record the result in the daily log.

### Write Scope

- `.gitignore`
- `project-file-structure-md/DAILY-2026-04-24.md`
- local git history only

### Verification

```bash
git status --short
git rev-list --objects HEAD | grep 'test_outputs/finreport25_manifest_run/finreport25_manifest.json'
git check-ignore -v test_outputs/finreport25_manifest_run/finreport25_manifest.json
```

### Exit Criteria

- The grep command prints nothing.
- The ignore rule resolves for the run directory path.
- The branch is pushable without the large-file rejection.

## Step 2: Canonicalize Repo Management Surfaces

- Status: ready
- Model tier: strongest
- Depends on: Step 1
- Parallelizable with: none
- Rollback: restore previous planning-file locations and add a redirect note instead of moving files

### Context Brief

The repo already uses `project-file-structure-md/` for planning, but that location is explicitly marked temporary. Before broader cleanup, the project needs a stable rule for where planning, logs, and future blueprint files live.

### Task List

1. Decide whether `project-file-structure-md/` remains canonical or whether planning files move to the repo root.
2. If the location changes, move the files in one focused step and add a short index/redirect note.
3. Add a durable convention for daily logs, plans, findings, and handoff files.
4. Update the decision and status files to reflect the chosen location.

### Write Scope

- `project-file-structure-md/` or root planning files
- `plans/`
- `README.md` only if a location/index note is needed and the package-relationship decision is still unaffected

### Verification

```bash
find . -maxdepth 2 -type f \( -path './project-file-structure-md/*' -o -path './plans/*' \) | sort
rg -n "temporary planning location|canonical planning" project-file-structure-md README.md AGENTS.md
```

### Exit Criteria

- There is one explicit canonical planning location.
- A fresh contributor can discover the planning files in under one minute.

## Step 3: Mark Historical And Reference Material Explicitly

- Status: ready
- Model tier: default
- Depends on: Step 1
- Parallelizable with: Step 4
- Rollback: revert only the added marker/index docs

### Context Brief

The repo contains `archive/`, `docs/chats/`, and `docs/pdf_spec_drafts/`. Current findings already say these are historical or draft material unless explicitly promoted, but the repo surface still makes them look more active than they are.

### Task List

1. Add a short index or marker note clarifying that `archive/` and `docs/chats/` are historical/reference material.
2. Add a warning/index in `docs/pdf_spec_drafts/` that old node names and terminology may be superseded by `AGENTS.md`.
3. Make sure the wording is precise and does not imply deletion.

### Write Scope

- `archive/README.txt` or a sibling index note
- `docs/pdf_spec_drafts/` index note
- `README.md` only if needed for discoverability

### Verification

```bash
rg -n "historical|reference|superseded|AGENTS.md" archive docs/pdf_spec_drafts README.md
```

### Exit Criteria

- Historical areas are clearly labeled.
- No reader should mistake draft specs or archive scripts for current authority.

## Step 4: Decide And Codify The Relationship Between The Two Active Package Tracks

- Status: ready
- Model tier: strongest
- Depends on: Step 1
- Parallelizable with: Step 3
- Rollback: restore the prior decision files and avoid code/package moves

### Context Brief

The repo has two active-looking implementation tracks:

- `accessibility_by_manifest/` for broad manifest-first pipelines
- `src/pdf_accessibility/` for the narrow v0.1.0 PDF workflow scaffold

Current docs acknowledge both, but the long-term relationship is unresolved.

### Task List

1. Choose one of three paths:
   - remain separate
   - become layered (`accessibility_by_manifest` feeds `pdf_accessibility`)
   - merge gradually into one package
2. Record the decision in planning docs with concrete implications.
3. Convert the decision into explicit boundaries:
   - where new PDF workflow code goes
   - where broad manifest pipeline work goes
   - what is considered legacy or supporting infrastructure

### Write Scope

- `project-file-structure-md/DECISIONS.md`
- `project-file-structure-md/PLAN.md`
- `project-file-structure-md/STATUS.md`
- optionally `README.md` / `PROJECT.md` after the decision is stable

### Verification

```bash
rg -n "package relationship|remain separate|merge|layered|v0.1.0" project-file-structure-md README.md PROJECT.md
```

### Exit Criteria

- There is one explicit package-relationship decision.
- A fresh agent can tell where a new change belongs before opening files.

## Step 5: Curate Generated Output Policy And Tracked Fixtures

- Status: ready
- Model tier: default
- Depends on: Step 2
- Parallelizable with: none
- Rollback: restore any removed tracked artifacts from git history or reclassify them as curated fixtures

### Context Brief

The repo has large `test_outputs/` material plus tracked legacy outputs under `archive/test_outputs/`. Some of that content may be useful regression evidence, but right now the repo does not separate curated fixtures from disposable run outputs.

### Task List

1. Inventory tracked output artifacts under `test_outputs/` and `archive/test_outputs/`.
2. Classify each group as one of:
   - curated fixture
   - disposable generated run output
   - historical example
3. Move only the documentation/policy first; do not mass-delete in the same step unless the classification is obvious and low-risk.
4. Add or refine ignore rules so disposable run outputs stay local.

### Write Scope

- `.gitignore`
- `project-file-structure-md/FINDINGS.md`
- `project-file-structure-md/DECISIONS.md`
- optionally a quarantine/review note if specific tracked outputs should be removed later

### Verification

```bash
git ls-files test_outputs archive/test_outputs
git check-ignore -v test_outputs/finreport25_manifest_run/finreport25_manifest.json
```

### Exit Criteria

- The repo has a written policy for generated outputs.
- Curated fixtures are intentional; disposable run outputs are not casually tracked.

## Step 6: Fix Artifact Honesty In The v0.1.0 Workflow

- Status: ready
- Model tier: default
- Depends on: Steps 2, 3, and 4
- Parallelizable with: none
- Rollback: revert the code and tests for validator/persistence behavior only

### Context Brief

Current findings show that `validator_findings.json` can imply a successful validation even when no tagged draft exists. That undermines the repo’s core honesty rule for workflow artifacts.

### Task List

1. Update `src/pdf_accessibility` persistence/validator artifact logic so no-draft runs do not emit misleading validator pass signals.
2. Add or adjust targeted tests for:
   - no draft written
   - draft written and validated
   - final output absent unless finalization is legal
3. Re-run the targeted `tests/pdf_accessibility` suite.

### Write Scope

- `src/pdf_accessibility/persistence/`
- possibly `src/pdf_accessibility/nodes/validator_check.py`
- `tests/pdf_accessibility/`

### Verification

```bash
.venv/bin/python -m pytest tests/pdf_accessibility -q
```

### Exit Criteria

- No-draft runs do not claim a validator pass.
- Artifact contracts match actual workflow routing.

## Step 7: Align Contributor-Facing Docs With The Cleaned Structure

- Status: ready
- Model tier: default
- Depends on: Steps 5 and 6
- Parallelizable with: none
- Rollback: revert doc-only changes

### Context Brief

After the planning location, historical markers, package relationship, and output policy are settled, the public-facing docs need to reflect the cleaned repo shape so new contributors do not relearn the same confusion.

### Task List

1. Update `README.md` to explain:
   - active package tracks
   - where planning lives
   - how generated outputs should be treated
2. Update `PROJECT.md` to match the chosen package relationship and current workflow direction.
3. Add a short “start here” path for new contributors.

### Write Scope

- `README.md`
- `PROJECT.md`
- possibly `AGENTS.md` if contributor navigation needs clarification without changing scope

### Verification

```bash
rg -n "start here|planning|generated outputs|pdf_accessibility|accessibility_by_manifest" README.md PROJECT.md AGENTS.md
```

### Exit Criteria

- Repo entry docs no longer fight the implementation reality.
- New contributors can identify active code and historical material quickly.

## Step 8: Optional Structural Consolidation Pass

- Status: optional
- Model tier: strongest
- Depends on: Step 7
- Parallelizable with: none
- Rollback: revert structural moves and keep the documented dual-track arrangement

### Context Brief

Only start this step if the package-relationship decision in Step 4 requires actual file/module moves. Do not begin structural consolidation while the repo is still stabilizing its governance and output policy.

### Task List

1. Move or merge modules only according to the Step 4 decision.
2. Keep the change set small enough to verify with tests and docs in one pass.
3. Add transitional import shims only if needed.

### Write Scope

- package directories
- imports
- tests
- docs

### Verification

```bash
.venv/bin/python -m pytest
```

### Exit Criteria

- The repo structure matches the chosen architecture.
- No stale package narrative remains in docs or tests.

## Plan Mutation Protocol

If conditions change:

- **Split a step** when a step grows beyond one focused PR or one uninterrupted session.
- **Insert a step** when a new dependency is discovered that blocks a later step cleanly.
- **Skip a step** only when its exit criteria have already been satisfied by another step, and record why.
- **Reorder steps** only if the dependency graph is updated in the plan file first.
- **Abandon a step** only with a replacement decision written into `DECISIONS.md` and reflected in `STATUS.md`.

Every mutation must update:

- this plan file
- the current daily log
- `project-file-structure-md/TASKS.md`

## Manual Adversarial Review

Sub-agent adversarial review was not used here because this harness only allows delegation when the user explicitly requests sub-agents. Local review checklist applied instead:

- Is the push-blocker cleanup separated from broader repo refactors? yes
- Are historical-material labeling and package-relationship decisions separated? yes
- Does any step require a repo move before governance is settled? no
- Are generated outputs treated as policy/governance first, deletion second? yes
- Is there a narrow code-fix lane for the validator/no-draft honesty bug? yes
