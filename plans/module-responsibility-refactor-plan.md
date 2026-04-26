# Module Responsibility Refactor Plan

Supporting technical refactor plan.

This is the only active supporting refactor plan. It is subordinate to
[start-to-finish-product-plan.md](./start-to-finish-product-plan.md): do product
work first, and use this plan when product work exposes unclear module
boundaries, mixed responsibilities, or hard-to-test orchestration.

Do not use this plan to justify a broad cleanup pass before the v0.1.0 product
slice is credible.

Use this plan to improve Python module boundaries so the code reflects the
actual system mental model:

```text
inputs -> extract -> normalize -> make accessible -> review -> output
```

This plan is about **modules of responsibility**, not about forcing one stage
to equal one package or one file.

## Objective

Make the Python codebase more logical, maintainable, and effective by:

1. keeping responsibility boundaries explicit
2. reducing mixed-purpose orchestration modules
3. making typed handoff boundaries clearer
4. localizing side effects near edges
5. reducing misleading naming that still reflects older intermediate designs

## Standards

Applied from `python-code-quality`:

- readable names
- explicit boundaries
- focused functions
- typed interfaces
- specific errors
- simple data models
- controlled mutation
- local side effects

## Current High-Level Read

The code is already fairly modular, but several orchestration points still mix
too many responsibilities.

Good current responsibility areas:

- `accessibility_by_manifest/inputs/`
- `accessibility_by_manifest/manifest/`
- `accessibility_by_manifest/normalize/`
- `accessibility_by_manifest/review/`
- `accessibility_by_manifest/outputs/`
- `src/pdf_accessibility/writeback/`
- `src/pdf_accessibility/reducers/`
- `src/pdf_accessibility/transition_guards/`

Main problems:

- some entry modules act as stage facades **and** stage implementations
- some bridge modules both load, transform, and emit workflow events
- some workflow nodes cross multiple stage boundaries in one function
- some active node names and graph buckets still reflect older internal
  organization rather than the current system model
- placeholder nodes remain in the live graph and dilute the module story

## Responsibility Map

### Inputs

Current modules:

- `accessibility_by_manifest/cli/*.py`
- `accessibility_by_manifest/inputs/*/paths.py`
- `accessibility_by_manifest/inputs/*/config.py`

Keep:

- CLI argument parsing
- run discovery
- source selection
- input-specific config

Do not let inputs own:

- normalization
- review generation
- accessibility remediation logic

Assessment:

- mostly clean

### Extract

Current modules:

- `accessibility_by_manifest/inputs/pdf/extractors/*`
- `accessibility_by_manifest/inputs/pptx/extraction.py`
- parts of `accessibility_by_manifest/inputs/docx/__init__.py`

Keep:

- source-specific evidence extraction
- optional sidecar extraction
- provenance capture

Assessment:

- mostly clean
- strongest current modular area

### Manifest Assembly

Current modules:

- `accessibility_by_manifest/manifest/pdf_builder.py`
- `accessibility_by_manifest/manifest/docx_builder.py`
- `accessibility_by_manifest/manifest/pptx.py`
- `accessibility_by_manifest/manifest/pdf_validate.py`

Keep:

- canonical manifest assembly
- schema/shape validation
- extractor merge policy

Assessment:

- mostly clean
- keep separate from normalization

### Normalize

Current modules:

- `accessibility_by_manifest/normalize/pdf.py`
- `accessibility_by_manifest/normalize/docx.py`
- `accessibility_by_manifest/normalize/accessibility_model.py`
- `accessibility_by_manifest/normalize/*_accessibility_model.py`

Keep:

- source-specific normalization
- source-neutral normalized contract
- shared model bridges

Assessment:

- conceptually clean
- handoff model is real

### Review

Current modules:

- `accessibility_by_manifest/review/pdf.py`
- review-task parts of `src/pdf_accessibility/reducers/apply_events.py`
- review-decision template service

Keep:

- review-signal generation
- review-task modeling
- review-decision modeling
- review-resolution logic

Assessment:

- split across shared-core review generation and PDF remediation review
- acceptable, but naming should make the split explicit

### Make Accessible

Current modules:

- `src/pdf_accessibility/graph/*`
- `src/pdf_accessibility/nodes/*`
- `src/pdf_accessibility/services/*`
- `src/pdf_accessibility/writeback/*`

Keep:

- target-specific remediation logic
- structure planning
- mapping
- writeback legality
- validation/finalization control

Assessment:

- real and modular in broad strokes
- orchestration files still mix too many concerns

### Output

Current modules:

- `accessibility_by_manifest/outputs/*`
- `src/pdf_accessibility/nodes/finalize_accessible_output.py`
- `src/pdf_accessibility/nodes/write_accessible_html.py`
- `src/pdf_accessibility/persistence/artifacts.py`

Keep:

- manifest bundles
- debug evidence sidecars
- HTML writer
- final PDF artifacts
- run artifacts and reports

Assessment:

- mostly clean
- artifact persistence and final output logic are sensibly separated

## Modules To Keep As-Is

- `accessibility_by_manifest/inputs/pdf/extractors/*`
- `accessibility_by_manifest/manifest/*`
- `accessibility_by_manifest/normalize/accessibility_model.py`
- `accessibility_by_manifest/review/pdf.py`
- `accessibility_by_manifest/outputs/html.py`
- `src/pdf_accessibility/reducers/*`
- `src/pdf_accessibility/transition_guards/*`
- `src/pdf_accessibility/writeback/*`

These already reflect focused responsibility well enough.

## Modules To Split

### 1. `accessibility_by_manifest/inputs/pdf/__init__.py`

Current problem:

- one function currently runs extraction, manifest build, normalize, review,
  and validation

Target:

- keep it as a thin facade only

Split into internal helpers or sibling modules:

- `run_pdf_extractors(...)`
- `build_pdf_manifest(...)`
- `normalize_pdf_manifest(...)`
- `review_pdf_manifest(...)`
- `validate_pdf_manifest(...)`

Why:

- clearer stage boundaries
- easier unit testing
- easier later reuse outside the current facade

### 2. `src/pdf_accessibility/services/manifest_bridge.py`

Current problem:

- loads shared manifest
- converts to shared normalized model
- translates into workflow-specific data
- emits workflow events

Target split:

- shared manifest loader
- shared-model loader
- workflow translation adapter
- event-emission adapter

Why:

- reduces knowledge coupling
- makes the shared-model boundary more explicit
- easier to test transformation independently from event emission

### 3. `src/pdf_accessibility/nodes/ocr_layout_analysis.py`

Current problem:

- reads recovery file
- registers artifact
- merges page evidence
- creates normalized units
- creates regions
- resolves review tasks

Target split:

- OCR recovery input loader
- OCR evidence merger
- OCR normalization adapter
- OCR review-resolution helper

Why:

- one node can still orchestrate these pieces, but should not implement all of
  them inline

## Modules To Rename Conceptually

These may not need immediate file moves, but the code should stop treating them
as the conceptual truth.

### `ManifestPipeline`

Current issue:

- good low-level utility, but the name sounds like the whole system pipeline

Target:

- keep class if useful
- treat it explicitly as a **manifest-bundle pipeline primitive**, not the full
  system architecture

### `setup_nodes`, `evidence_nodes`, `planning_nodes` in `build_graph.py`

Current issue:

- bucket names reflect older internal organization

Target:

- rename buckets toward responsibility:
  - `input_nodes`
  - `recovery_and_evidence_nodes`
  - `remediation_nodes`
  - `review_nodes`
  - `output_nodes`

Why:

- the graph should speak the same mental model as the rest of the system

## Nodes To Remove From The Live Path Or Mark More Explicitly

### `render_pages.py`

Current issue:

- active graph node, but still a placeholder

Target:

- either implement it
- or remove it from the live graph until needed

### `vision_analysis.py`

Current issue:

- returns no events

Target:

- either implement it
- or remove it from the live graph until needed

## Dependency Rules

These rules should govern future refactors:

1. `inputs` may depend on config/path helpers, not on remediation state logic.
2. `extract` may depend on source-specific libraries, not on final output
   legality.
3. `manifest` may depend on extracted evidence, not on target-specific writeback.
4. `normalize` may depend on evidence and manifest structure, not on PDF draft
   writer internals.
5. `review` may depend on normalized structure and evidence, not on final output
   file writing.
6. `make accessible` may consume normalized and reviewable structure, but should
   not reimplement extraction.
7. `output` may consume normalized/remediated state, but heavy debug evidence
   should remain optional and isolated.

## Execution Order

### Step 1: Thin The Shared PDF Facade

Change:

- split `accessibility_by_manifest/inputs/pdf/__init__.py` into clear staged
  helpers without changing behavior

Verification:

- PDF manifest tests still pass

### Step 2: Split The Manifest Bridge

Change:

- separate load / transform / event emission responsibilities

Verification:

- bridge tests still pass
- workflow ingestion still passes

### Step 3: Split OCR Recovery Responsibilities

Change:

- keep the node, but move mixed logic into helpers/services

Verification:

- OCR recovery tests still pass

### Step 4: Rename Workflow Graph Buckets

Change:

- update internal graph organization names
- do not change behavior

Verification:

- workflow tests still pass

### Step 5: Remove Or Implement Placeholder Nodes

Change:

- either implement or remove `render_pages` and `vision_analysis` from the live
  graph

Verification:

- graph tests and CLI smoke tests still pass

## Non-Goals

- do not do a giant package move first
- do not rewrite the whole codebase around perfect stage directories
- do not break working product paths in order to make the tree prettier
- do not force a merge of all PDF workflow code into one package during this
  pass

## Success Criteria

The refactor is successful when:

1. major orchestration files are thinner
2. transformation boundaries are typed and explicit
3. side effects are closer to edges
4. live graph names match current mental model better
5. placeholder nodes no longer dilute the active workflow story
6. the product path still works end to end
