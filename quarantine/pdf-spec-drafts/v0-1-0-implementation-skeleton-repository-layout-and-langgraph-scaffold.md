---
title: v0.1.0 Implementation Skeleton, Repository Layout, and LangGraph Scaffold
filename: v0-1-0-implementation-skeleton-repository-layout-and-langgraph-scaffold.md
type: specification
status: draft
created: 2026-04-21
updated: 2026-04-21
origin: chat
tags:
  - pdf
  - accessibility
  - tagged-pdf
  - langgraph
  - workflow
  - python
  - implementation
topics:
  - PDF accessibility
  - Tagged PDF
  - Python implementation
aliases:
  - PDF Accessibility Implementation Skeleton v0.1.0
sources: []
cssclasses: []
notes:
  - Uses frozen terminology and typed schema from earlier drafts
  - Keeps v0.1.0 narrow and buildable
---

# v0.1.0 Implementation Skeleton, Repository Layout, and LangGraph Scaffold

## Purpose

Turn the architecture and typed schema into a buildable Python project shape.

This draft locks:

- repository layout
- module boundaries
- LangGraph scaffold shape
- node placement
- reducer placement
- artifact persistence points
- checkpoint placement
- CLI entry point
- plug-in points for PDF/OCR/validator/write-back code

## Repository layout

```text
pdf_accessibility/
├── pyproject.toml
├── README.md
├── src/
│   └── pdf_accessibility/
│       ├── __init__.py
│       ├── config.py
│       ├── cli.py
│       ├── constants.py
│       ├── models/
│       ├── reducers/
│       ├── transition_guards/
│       ├── nodes/
│       ├── graph/
│       ├── services/
│       ├── persistence/
│       ├── writeback/
│       └── utils/
└── tests/
```

## Module responsibilities

### `models/`
Pure data models only.

### `reducers/`
Apply events to shared state.

### `transition_guards/`
Legal state-change checks.

### `nodes/`
Specialist node implementations.

### `graph/`
LangGraph-specific wiring.

### `services/`
Wrappers around concrete tools and external libraries.

### `persistence/`
Run folders, JSON writes, checkpoints, artifact manifests.

### `writeback/`
PDF output construction.

### `utils/`
Small reusable helpers.

## Concrete tool integration points

### PDF ingest and rendering
Library:
- PyMuPDF

Plug-in points:
- `services/pdf_ingest.py`
- `services/pdf_render.py`
- `services/pdf_native.py`

### OCR and layout
Libraries:
- OCRmyPDF
- PaddleOCR or equivalent layout parser

Plug-in points:
- `services/ocr.py`
- `services/vision.py`

### Validator
Library:
- veraPDF wrapper or subprocess adapter

Plug-in points:
- `services/validator.py`

### Tagged draft write-back
Libraries:
- pikepdf
- optionally PyMuPDF for inspection support

Plug-in points:
- `writeback/draft_writer.py`
- `writeback/structure_tree.py`
- `writeback/marked_content.py`
- `writeback/mcid.py`
- `writeback/parenttree.py`

## Minimal runtime flow

1. create run directory
2. build initial `DocumentState`
3. run setup nodes
4. run evidence nodes for active regions
5. run accessibility-review and planning nodes
6. run `behavior_check`
7. run `approval_gate`
8. if draft-write transition guard passes, run `write_tagged_draft`
9. run `validator_check`
10. if blockers exist, run `human_review`
11. apply review decisions if available
12. if finalization transition guard passes, run `finalize_accessible_output`

Every specialist node returns events. Every event batch goes through `apply_events`.

## LangGraph scaffold

### State adapter
```python
from typing import TypedDict
from pdf_accessibility.models.state import DocumentState


class GraphState(TypedDict):
    document: DocumentState
```

### Specialist node function shape
```python
from pdf_accessibility.models.events import NodeEvent
from pdf_accessibility.models.state import DocumentState


def some_node(document: DocumentState) -> list[NodeEvent]:
    events: list[NodeEvent] = []
    return events
```

### `apply_events` node
```python
from pdf_accessibility.models.state import DocumentState
from pdf_accessibility.models.events import NodeEvent
from pdf_accessibility.reducers.apply_events import apply_events


def apply_events_node(document: DocumentState, events: list[NodeEvent]) -> DocumentState:
    return apply_events(document, events)
```

### Workflow orchestrator node
The orchestrator chooses what runs next based on current state:
- region proposal
- evidence
- accessibility review
- tagging plan
- structure mapping
- behavior check
- approval gate
- write tagged draft
- validator check
- human review
- apply review decisions
- finalize accessible output

## Persistence points

### Run directory
Each run should get its own directory:

```text
runs/
└── {run_id}/
    ├── input.pdf
    ├── page_images/
    ├── checkpoints/
    ├── artifacts/
    ├── document_state.json
    ├── findings.jsonl
    ├── review_tasks.json
    ├── review_decisions.json
    ├── validator_findings.json
    ├── tagged_draft.pdf
    ├── finalization_status.json
    ├── accessible_output.pdf
    ├── artifact_manifest.json
    └── run_log.json
```

### Checkpoints
Checkpoint after:
- `ingest_pdf`
- `region_proposal`
- evidence passes
- `tagging_plan`
- `structure_mapping_plan`
- `write_tagged_draft`
- `validator_check`
- `apply_review_decisions`
- `finalize_accessible_output`

## Minimal CLI entry point

### Command shape
```bash
pdf-accessibility run /path/to/input.pdf --output-dir ./runs
```

### CLI responsibilities
- validate input path
- create run directory
- copy input PDF into run directory
- initialize `DocumentState`
- build graph
- invoke graph
- return final run summary

### CLI skeleton
```python
import typer
from pathlib import Path
from pdf_accessibility.persistence.runs import create_run
from pdf_accessibility.graph.build_graph import build_graph
from pdf_accessibility.models.state import DocumentState


app = typer.Typer()


@app.command()
def run(input_pdf: Path, output_dir: Path = Path("./runs")):
    run_ctx = create_run(input_pdf=input_pdf, output_dir=output_dir)
    document = initialize_document_state(run_ctx)
    graph = build_graph()
    result = graph.invoke({"document": document})
    typer.echo(result["document"].finalization_state.value)
```

## Minimum implementation sequence

Build in this order:

1. repository layout
2. models
3. reducers
4. transition guards
5. persistence helpers
6. `ingest_pdf`
7. `render_pages`
8. `region_proposal`
9. evidence nodes
10. `accessibility_review`
11. `tagging_plan`
12. `structure_mapping_plan`
13. `behavior_check`
14. `approval_gate`
15. `write_tagged_draft`
16. `validator_check`
17. `human_review`
18. `apply_review_decisions`
19. `finalize_accessible_output`
20. graph wiring
21. CLI
