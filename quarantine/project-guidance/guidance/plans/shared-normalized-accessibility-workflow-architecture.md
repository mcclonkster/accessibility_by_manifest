# Blueprint: Many Inputs -> Shared Normalized Accessibility Model -> Many Format-Specific Accessibility Workflows

## Status

- Overall status: completed on 2026-04-24
- Completion note: all eight planned steps have been implemented and verified in
  code, tests, and root/planning docs. Follow-on work should use a narrower
  cleanup/consolidation plan rather than extending this architecture blueprint.

## Objective

Reorganize the repository around this architecture:

```text
many inputs
-> shared normalized accessibility model
-> many format-specific accessibility workflows
```

The immediate product slice remains:

- PDF input
- accessible PDF output
- accessible HTML output

But the architecture must remain broad enough to support multiple inputs and
multiple output-specific accessibility workflows without cloning the same logic
per format.

This blueprint assumes **direct mode** because git is available but GitHub CLI
is not installed in the current environment.

## Pre-Flight Snapshot

- Repository: `/Users/computerk/github/accessibility_by_manifest`
- Current branch: `main`
- Remote: `origin https://github.com/mcclonkster/accessibility_by_manifest.git`
- `gh`: unavailable
- Existing broad package: `accessibility_by_manifest/`
- Existing narrow PDF workflow: `src/pdf_accessibility/`
- Current shared contract artifact: `accessibility_by_manifest/normalize/accessibility_model.py`
- Current planning/control surface: `project-file-structure-md/`

## Architecture Intent

The repository should converge toward three clear layers:

1. `inputs + extraction`
   - source-specific adapters for PDF, DOCX, PPTX, later HTML and others
2. `shared normalized accessibility model`
   - source-neutral structural units, provenance, review tasks, and projection hints
3. `format-specific accessibility workflows`
   - PDF workflow now
   - HTML workflow next
   - later DOCX and others

The normalized accessibility model is the contract boundary.

## Invariants

These must remain true throughout every step:

- Do not collapse the architecture into “PDF-only” thinking.
- Do not duplicate extraction/normalization logic across workflow packages.
- Keep the normalized accessibility model source-neutral.
- Keep projection hints advisory, not final truth.
- Keep review/task state explicit rather than hidden in workflow code.
- Preserve the ability to run `.venv/bin/python -m pytest`.
- Do not mass-move packages until the bridge layer is real and tested.
- Do not bolt HTML generation directly into PDF writeback as a side effect.

## Dependency Graph

```text
Step 1 -> Step 2 -> Step 3 -> Step 4 -> Step 6 -> Step 8
Step 2 -> Step 5 -> Step 7 -> Step 8
Step 3 -> Step 5
Step 4 -> Step 7
```

## Parallelism Summary

After Step 2:

- Step 3 and Step 5 can proceed in parallel.
- Step 4 must wait for Step 3 because the PDF workflow bridge depends on the
  normalized contract and bridge mapping.
- Step 6 must wait for Step 4 because the PDF vertical should be the first real
  consumer of the new bridge.
- Step 7 must wait for Step 5 and Step 4 because HTML needs both the shared
  model and the PDF workflow integration lessons.

## Anti-Patterns To Avoid

- Rebranding the repo in docs without changing the actual integration points.
- Treating `pdf_accessibility` as the shared core instead of a downstream
  workflow.
- Letting the normalized model become PDF-shaped.
- Moving files before deciding which package owns them.
- Building HTML as a PDF-specific side effect instead of an output workflow.
- Preserving both old and new normalization paths indefinitely.
- Introducing a second shared model beside the one just added.

## Step 1: Ratify The Architecture North Star In Repo Planning Files

- Status: completed
- Model tier: strongest
- Depends on: none
- Parallelizable with: none
- Rollback: restore previous planning wording and keep the architecture goal in
  the new blueprint only

### Context Brief

The repo currently has a layered-package decision and a shared-model artifact in
code, but the broad architecture target is still implicit. Before implementation
work spreads, the repo needs one explicit statement that the system is many
inputs -> shared normalized accessibility model -> many output-specific
accessibility workflows.

### Task List

1. Record the architecture north star in the decision and planning surfaces.
2. Clarify that PDF is the current active vertical, not the architecture limit.
3. Clarify that HTML is a sibling output workflow, not a PDF-only side effect.

### Write Scope

- `project-file-structure-md/DECISIONS.md`
- `project-file-structure-md/PLAN.md`
- `project-file-structure-md/STATUS.md`
- `project-file-structure-md/DAILY-*.md`

### Verification

```bash
rg -n "many inputs|shared normalized accessibility model|format-specific accessibility workflows|HTML" \
  project-file-structure-md
```

### Exit Criteria

- The architecture north star is explicit in planning files.
- A fresh contributor can tell PDF is the first vertical, not the whole system.

## Step 2: Freeze The Shared Normalized Accessibility Contract

- Status: completed
- Model tier: strongest
- Depends on: Step 1
- Parallelizable with: none
- Rollback: keep the contract file internal/experimental and avoid consuming it
  yet

### Context Brief

The repo now has a first explicit shared contract in
`accessibility_by_manifest/normalize/accessibility_model.py`, but no current
code path fully depends on it yet. This step hardens that contract so all future
bridges and workflows target the same schema.

### Task List

1. Review the current contract against existing normalized IR and workflow
   state.
2. Add any missing fields needed for:
   - document identity
   - provenance
   - review tasks
   - table structures
   - projection hints
3. Decide which fields are required vs optional.
4. Add focused tests locking the contract shape and intended semantics.

### Write Scope

- `accessibility_by_manifest/normalize/accessibility_model.py`
- `accessibility_by_manifest/normalize/__init__.py`
- `tests/test_accessibility_model.py`

### Verification

```bash
./.venv/bin/python -m pytest tests/test_accessibility_model.py -q
```

### Exit Criteria

- The shared contract is explicit in code.
- Required/optional fields are test-locked.
- There is one obvious model for downstream workflows to consume.

## Step 3: Build Source-To-Contract Bridges In The Shared Core

- Status: completed
- Model tier: strongest
- Depends on: Step 2
- Parallelizable with: Step 5
- Rollback: keep legacy normalized outputs in place and ship the bridges as
  additive only

### Context Brief

The shared core already extracts and normalizes PDF, DOCX, and PPTX evidence,
but it does not yet standardize those outputs into the new shared normalized
accessibility contract. This step builds the bridge layer without changing the
PDF workflow yet.

### Task List

1. Add bridge/conversion functions from existing normalized outputs into the new
   contract.
2. Start with PDF and DOCX; leave PPTX either bridged or explicitly deferred,
   but do not leave the contract PDF-only.
3. Keep the existing manifest and IR outputs available during the transition.
4. Add tests that prove existing normalization results can be represented in the
   shared contract.

### Write Scope

- `accessibility_by_manifest/normalize/`
- possibly new adapter modules such as:
  - `normalize/pdf_accessibility_model.py`
  - `normalize/docx_accessibility_model.py`
- tests under `tests/`

### Verification

```bash
./.venv/bin/python -m pytest tests/test_pdf_normalization.py tests/test_docx_manifest_pipeline.py -q
```

### Exit Criteria

- PDF and DOCX can both produce the shared normalized accessibility model.
- The contract remains source-neutral.

## Step 4: Bridge The Shared Model Into The PDF Workflow Vertical

- Status: completed
- Model tier: strongest
- Depends on: Step 3
- Parallelizable with: none
- Rollback: feature-flag the bridge and preserve the legacy PDF node path

### Context Brief

`src/pdf_accessibility/` currently recreates a thinner version of extraction,
region proposal, artifact inference, normalization, and review. The PDF
workflow should instead consume the shared normalized model and focus on PDF
orchestration, planning, writeback, validation, and finalization.

### Task List

1. Add a bridge service in `src/pdf_accessibility/services/`.
2. Map shared normalized model fields into `DocumentState`.
3. Replace or bypass the current thin normalization path:
   - `native_pdf_analysis`
   - `region_proposal`
   - `accessibility_review`
   - `artifact_check`
4. Preserve later PDF-specific nodes for structure planning, writeback,
   validation, and finalization.
5. Add focused tests for the bridge behavior.

### Write Scope

- `src/pdf_accessibility/services/`
- `src/pdf_accessibility/nodes/`
- `src/pdf_accessibility/models/`
- `tests/pdf_accessibility/`

### Verification

```bash
./.venv/bin/python -m pytest tests/pdf_accessibility -q
```

### Exit Criteria

- The PDF workflow consumes the shared normalized model rather than rebuilding a
  second normalization path.
- PDF workflow tests still pass.

## Step 5: Separate Shared Output Projection Helpers From PDF-Specific Writeback

- Status: completed
- Model tier: default
- Depends on: Step 2
- Parallelizable with: Step 3
- Rollback: keep new projection helpers additive and continue using legacy
  output code where necessary

### Context Brief

The repo currently mixes shared output ideas with PDF-specific writeback logic.
This step clarifies that the shared core owns reusable projection helpers while
the PDF vertical owns PDF-specific tagged-PDF mechanics.

### Task List

1. Identify output helpers that are genuinely shared across formats.
2. Keep PDF tagging/writeback in `src/pdf_accessibility/writeback/`.
3. Move or add shared projection helpers in `accessibility_by_manifest/outputs/`
   if they can be reused by multiple workflows.
4. Record which output responsibilities are shared vs vertical-specific.

### Write Scope

- `accessibility_by_manifest/outputs/`
- `src/pdf_accessibility/writeback/`
- tests for shared vs PDF-specific responsibilities

### Verification

```bash
rg -n "tagged_draft|accessible_output|projection_hints|html_tag_hint|pdf_structure_role_hint" \
  accessibility_by_manifest src/pdf_accessibility
```

### Exit Criteria

- Shared output helpers are no longer confused with PDF-specific writeback.
- PDF-specific tagged-PDF logic remains isolated in the PDF vertical.

## Step 6: Make PDF The First Fully Integrated Format-Specific Workflow

- Status: completed
- Model tier: strongest
- Depends on: Step 4
- Parallelizable with: none
- Rollback: keep the bridge in place but gate new workflow routing behind a
  config flag

### Context Brief

Once the PDF workflow consumes the shared model, it becomes the first real
proof that the architecture works. This step is about making the PDF vertical
the canonical product slice without narrowing the whole architecture to PDF.

### Task List

1. Confirm the end-to-end PDF path is:
   - PDF input
   - shared extraction/normalization
   - PDF-specific orchestration
   - PDF-specific QA
   - accessible PDF output
2. Fix any artifact honesty issues revealed by the new bridge.
3. Keep terminal-state rules honest: `finalized`, `needs_review`,
   `write_blocked`.
4. Add one canonical smoke-test path for the PDF workflow.

### Write Scope

- `src/pdf_accessibility/`
- `tests/pdf_accessibility/`
- root docs only after the path is real

### Verification

```bash
./.venv/bin/python -m pytest tests/pdf_accessibility -q
PYTHONPATH=src ./.venv/bin/python -m pdf_accessibility.cli test_inputs/finreport25.pdf --output-dir test_outputs/finreport25_workflow_runs
```

### Exit Criteria

- PDF is the first fully integrated workflow vertical.
- The repo has one clear PDF product path.

## Step 7: Add An HTML Accessibility Workflow As A Sibling Consumer

- Status: completed
- Model tier: strongest
- Depends on: Step 5 and Step 4
- Parallelizable with: none
- Rollback: keep HTML generation as an internal preview artifact rather than a
  formal workflow

### Context Brief

Accessible HTML is a desired sibling output, but it should be built as its own
consumer of the shared normalized model, not as a PDF writeback side effect.

### Task List

1. Add a first HTML accessibility workflow or projection path that consumes the
   shared normalized model.
2. Reuse shared projection helpers where appropriate.
3. Keep HTML-specific semantics in the HTML workflow, not in the shared model.
4. Add tests for representative heading/paragraph/table/figure output.
5. Register HTML artifacts explicitly in workflow outputs.

### Write Scope

- `accessibility_by_manifest/outputs/` and/or a new `src/html_accessibility/`
  package, depending on how much orchestration HTML needs
- tests for HTML output behavior

### Verification

```bash
./.venv/bin/python -m pytest tests -q -k "html or accessibility_model"
```

### Exit Criteria

- HTML is a sibling workflow/output path, not an accidental PDF appendage.
- The architecture now has one input-to-many-workflow proof.

## Step 8: Align Entrypoints, Docs, And Cleanup With The New Architecture

- Status: completed
- Model tier: default
- Depends on: Step 6 and Step 7
- Parallelizable with: none
- Rollback: leave old docs in place with explicit migration notes

### Context Brief

Once the architecture is real in code, the repo surface must stop telling the
older split story. Contributors need one clear explanation of how the layers fit
and where new work belongs.

### Task List

1. Update `README.md` and `PROJECT.md` to describe the three-layer architecture.
2. Clarify the user-facing entry points and the developer/internal ones.
3. Retire or downgrade duplicate legacy flows only after the new path is
   proven.
4. Revisit quarantine candidates that were only ambiguous because the
   architecture was unclear.

### Write Scope

- `README.md`
- `PROJECT.md`
- planning/control docs
- cleanup notes

### Verification

```bash
rg -n "input -> manifest -> output|pdf_accessibility|normalized accessibility model|HTML" README.md PROJECT.md project-file-structure-md
./.venv/bin/python -m pytest
```

### Exit Criteria

- The docs match the code.
- A fresh contributor can explain the architecture after reading the root docs.

## Adversarial Review Notes

This plan intentionally avoids:

- a big-bang package merge
- immediate PDF-only narrowing
- adding HTML before the shared model and PDF bridge are real
- mass cleanup before ownership is explicit

The main execution risk is leaving both the old and new normalization paths live
too long. Step 4 and Step 6 should be treated as convergence steps, not just
additive layering.

## Plan Mutation Protocol

If execution reveals missing detail:

- **Split** a step when a write scope or verification scope becomes too large.
- **Insert** a step when a new hard dependency appears.
- **Reorder** only if dependency edges are updated in this plan.
- **Abandon** a step only by writing a short reason into the daily log and
  marking the replacement path.

Do not silently mutate the plan by implementing around it.
