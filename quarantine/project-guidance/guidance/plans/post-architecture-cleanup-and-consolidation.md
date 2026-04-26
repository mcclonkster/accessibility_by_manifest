# Blueprint: Post-Architecture Cleanup And Consolidation

## Objective

The architecture blueprint is complete. The next phase is to reduce repo-surface
ambiguity without undoing the implemented layered architecture.

This follow-on plan is narrower:

1. refresh cleanup inventory against current repo state
2. decide generated-output and fixture policy
3. tighten historical/reference authority boundaries
4. resolve unclear ownership surfaces
5. perform only deliberate, reviewed cleanup actions

## Why This Exists

The main repo risk is no longer missing architecture. The remaining risk is
surface drift:

- cleanup notes that no longer match actual files
- historical/reference material that still looks active
- generated outputs that are partly ignored, partly tracked, and partly deleted
- unclear ownership of repo-local tooling and prototypes

## Invariants

- Do not undo the layered architecture:
  - `accessibility_by_manifest/` is the shared core
  - `src/pdf_accessibility/` is the first integrated workflow vertical
- Do not delete historical material casually.
- Do not treat generated outputs as canonical unless deliberately curated.
- Do not quarantine active product-direction material.
- Do not rewrite package ownership stories without code and doc evidence.

## Step 1: Refresh Cleanup Inventory

- Goal: make `QUARANTINE/`, cleanup notes, and tasks reflect the files that
  actually exist now.
- Focus:
  - `project-file-structure-md/QUARANTINE/README.md`
  - `project-file-structure-md/CLEANUP-REPORT.md`
  - `project-file-structure-md/TASKS.md`
- Verification:
```bash
cd /Users/computerk/github/accessibility_by_manifest
ls multi_agent_pdf_tagger_app.jsx
find project-file-structure-md/QUARANTINE -maxdepth 3 -print
```

## Step 2: Decide Generated-Output Policy

- Goal: decide which `test_outputs/` artifacts are curated fixtures and which
  are disposable local verification artifacts.
- Focus:
  - tracked deletions under `test_outputs/`
  - ignored rerun directories
  - any outputs still referenced as evidence in planning docs
- Verification:
```bash
cd /Users/computerk/github/accessibility_by_manifest
git status --short test_outputs
git check-ignore -v test_outputs/finreport25_manifest_run 2>/dev/null || true
```

## Step 3: Tighten Historical And Reference Boundaries

- Goal: keep `docs/design/` authoritative while preserving useful historical
  context in `docs/chats/`, `docs/pdf_spec_drafts/`, and `archive/`.
- Focus:
  - duplicated handoff bundle references
  - stale planning notes that still describe old doc authority problems as
    unresolved
- Verification:
```bash
rg -n "docs/chats|docs/design|historical|reference" \
  project-file-structure-md README.md PROJECT.md
```

## Step 4: Resolve Unclear Ownership Surfaces

- Goal: make an explicit keep/archive/investigate call for:
  - `.agents/`
  - `multi_agent_pdf_tagger_app.jsx`
  - any other repo-root prototypes or tooling bundles
- Verification:
```bash
cd /Users/computerk/github/accessibility_by_manifest
ls -d .agents multi_agent_pdf_tagger_app.jsx 2>/dev/null
```

## Step 5: Execute Deliberate Cleanup

- Goal: only after Steps 1-4 are explicit, perform the chosen file moves,
  deletions, archive actions, or doc demotions.
- Constraint: no broad destructive cleanup without an explicit decision record.
- Verification:
```bash
cd /Users/computerk/github/accessibility_by_manifest
git status --short
./.venv/bin/python -m pytest -q
```

## Exit Criteria

- cleanup inventory matches actual repo state
- generated-output policy is explicit
- historical/reference boundaries are current and credible
- unclear ownership surfaces have an explicit status
- cleanup actions are deliberate rather than reactive
