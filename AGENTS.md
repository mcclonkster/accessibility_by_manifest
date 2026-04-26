# AGENTS.md

Repo-wide operating contract for coding agents.

This repository builds `accessibility_by_manifest`: a local/open-first document
accessibility pipeline organized as:

```text
inputs -> extract -> normalize -> make accessible -> review -> output
```

The current v0.1 product slice is PDF-first, but the repo is not conceptually
PDF-only. Package-specific PDF workflow rules live in
[`src/pdf_accessibility/AGENTS.md`](./src/pdf_accessibility/AGENTS.md).

## Authoritative Docs

- Umbrella architecture: [`docs/design/system_reference.md`](./docs/design/system_reference.md)
- Active product plan: [`plans/start-to-finish-product-plan.md`](./plans/start-to-finish-product-plan.md)
- v0.1 acceptance gate: [`plans/v0.1-product-acceptance-pack.md`](./plans/v0.1-product-acceptance-pack.md)
- Run-record schema: [`docs/design/run_observability_schema.md`](./docs/design/run_observability_schema.md)
- PDF package contract: [`src/pdf_accessibility/AGENTS.md`](./src/pdf_accessibility/AGENTS.md)

Do not treat archived/quarantined docs as equal authority unless the user
explicitly asks for historical context.

## Repo Map

- `accessibility_by_manifest/`: shared input, extraction, normalization, review,
  and output/projection code.
- `src/pdf_accessibility/`: current integrated PDF remediation workflow.
- `tests/pdf_accessibility/`: focused tests for the PDF workflow.
- `tests/`: shared manifest, normalization, output, and CLI tests.
- `docs/design/`: active architecture/reference docs.
- `plans/`: active product and implementation plans.
- `.agents/skills/`: repo-local task procedures.

## Setup Commands

Run commands from the repository root unless a task says otherwise.

Use the project virtualenv when present:

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install -e .
```

If dependencies are already installed, do not reinstall just to inspect docs or
make a small edit.

## Run Commands

Integrated PDF workflow:

```bash
PYTHONPATH=src ./.venv/bin/python -m pdf_accessibility.cli run test_inputs/finreport25.pdf --output-dir test_outputs/finreport25_workflow_runs
```

PDF workflow with human inputs:

```bash
PYTHONPATH=src ./.venv/bin/python -m pdf_accessibility.cli run test_inputs/finreport25.pdf --output-dir test_outputs/finreport25_workflow_runs --review-decisions /path/to/review_decisions.json --ocr-recovery /path/to/ocr_recovery.json
```

Generate a review-decision template from a run folder:

```bash
PYTHONPATH=src ./.venv/bin/python -m pdf_accessibility.cli template-review-decisions /path/to/run-dir
```

Shared-core PDF manifest extraction:

```bash
PYTHONPATH=. ./.venv/bin/python -m accessibility_by_manifest.cli.pdf test_inputs/finreport25.pdf --output-dir test_outputs/finreport25_manifest_run --overwrite
```

## Test Commands

Run targeted tests first when changing a narrow area:

```bash
./.venv/bin/python -m pytest tests/pdf_accessibility/test_reducers.py -q
./.venv/bin/python -m pytest tests/pdf_accessibility/test_transition_guards.py -q
./.venv/bin/python -m pytest tests/pdf_accessibility/test_artifact_contract.py -q
./.venv/bin/python -m pytest tests/pdf_accessibility/test_cli_smoke.py -q
```

Run the PDF workflow suite when changing `src/pdf_accessibility/`:

```bash
./.venv/bin/python -m pytest tests/pdf_accessibility -q
```

Run the full suite when changing shared contracts, normalization, or outputs:

```bash
./.venv/bin/python -m pytest -q
```

Preferred repo verification command:

```bash
scripts/verify.sh -q
```

Use `PYTHON=/path/to/python scripts/verify.sh -q` to force a specific Python
interpreter.

No repo-wide lint or typecheck command is currently configured in `pyproject.toml`.
Do not invent one; add it only as an explicit project task.

## Repo-Wide Rules

- Preserve the role-based architecture: inputs, extract, normalize, make
  accessible, review, output.
- Do not collapse `accessibility_by_manifest/` and `src/pdf_accessibility/` into a
  product split. The former is shared core; the latter is the current PDF
  implementation slice.
- Do not broaden v0.1 scope silently.
- Do not claim accessibility, WCAG, Section 508, ADA, or PDF/UA conformance unless
  the workflow has explicit standards evidence, review coverage, and validator
  results sufficient for that claim.
- Do not send customer PDFs, page images, OCR text, logs, or run artifacts to
  external services unless an explicit feature flag and user-approved provider
  configuration enable that path.
- Never overwrite source documents in place.
- Register generated artifacts in the run manifest when working in run folders.

## When To Load Skills

Repo-local skills live under `.agents/skills/`.

- Use `.agents/skills/pdf-workflow-state/SKILL.md` for reducers, typed events,
  transition guards, blocker recomputation, and workflow state.
- Use `.agents/skills/pdf-writeback-output/SKILL.md` for tagged PDF writeback,
  structure tree, MCID, ParentTree, draft/final output gates, and output claims.
- Use `.agents/skills/terminology-scope-check/SKILL.md` for frozen terminology,
  conformance language, scope boundaries, and deferred-feature blockers.
- Use testing/code-quality skills only when the task directly calls for them or
  the user mentions them.

## Definition Of Done

A change is done only when:

- It preserves the umbrella architecture and package boundaries.
- It uses the nearest relevant `AGENTS.md` and active plan docs.
- It includes or updates focused tests when behavior changes.
- The relevant command above has been run, or the skipped check is explained.
- It does not fake finalization, conformance, or customer-ready accessibility.
