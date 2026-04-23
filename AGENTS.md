# AGENTS.md

## Repository purpose

This repository is building a **local/open-first PDF accessibility workflow**.

The product is **not** PDF analysis only. The workflow must support a real path from:

1. input PDF
2. evidence collection
3. accessibility review
4. structure planning
5. structure mapping
6. tagged draft output
7. validation
8. human review
9. review decisions
10. replanning / remapping when needed
11. finalization

The workflow must terminate honestly in one of these states:

- `finalized`
- `needs_review`
- `write_blocked`

Do not treat “good internal reasoning” as done.

---

## Current scope: v0.1.0

Keep v0.1.0 narrow.

### Supported in v0.1.0

- born-digital PDFs first
- mostly single-column documents
- headings
- paragraphs
- lists
- simple tables
- repeated headers, footers, and page numbers as artifacts
- basic figures
- document title
- primary language
- tagged draft creation
- validation
- human review
- finalization gating

### Deferred beyond v0.1.0

- forms
- links as a dedicated workflow
- logical tab order for interactive content
- formulas
- complex charts
- complex multi-column layouts
- difficult scanned documents
- advanced multilingual handling
- broken existing tag-tree reuse

Do not quietly expand scope.

---

## Frozen architecture decisions

### Workflow model

Use a **shared-state, non-linear workflow**.

- Nodes emit **typed events**.
- Reducers apply those events to **shared state**.
- **Transition guards** decide whether a state change is legal.
- The **workflow orchestrator** routes based on the resulting state.
- Validation, behavior checks, and human review can reopen earlier proposed decisions.

### LangGraph role

LangGraph is the workflow orchestration layer for v0.1.0.

Use it to coordinate specialist workflow nodes that share document state, emit typed events, and check one another's proposed decisions.

Specialist workflow nodes may focus on evidence extraction, normalization, artifact detection, caption association, structure mapping, validation, review, or writeback. They must not silently mutate state or claim final truth alone.

- deterministic evidence can challenge AI or heuristic claims
- validation can reopen structure mapping or writeback decisions
- behavior checks can block finalization
- human review can resolve, reject, or defer proposed decisions

The goal is coordinated accessibility remediation for existing PDFs, not isolated analysis or one-shot conversion.

Do **not** replace this with:

- linear relay-race handoffs
- free-form agent chat
- hidden state mutation inside nodes

### Output requirement

The workflow must support a real PDF artifact path:

- `tagged_draft.pdf` only when draft write is legal
- `validator_findings.json`
- `review_tasks.json`
- `review_decisions.json`
- `finalization_status.json`
- `accessible_output.pdf` only when finalization is legal

### Build strategy

Start small, make the narrow path work, then grow.

Do **not** build for every PDF class first.

---

## Frozen terminology

Use field-recognizable terms. Do not invent internal labels.

### Workflow terms

Use:
- workflow orchestrator
- shared state
- node
- edge
- interrupt
- checkpoint
- human review
- approval gate
- transition guard
- reducer
- blocker
- reopen
- finalization
- structured findings
- proposed decisions

Avoid:
- scheduler
- claim graph
- internal metaphors
- vague “agent debate” language

### PDF terms

Use:
- tagged PDF
- structure tree
- structure element
- marked content
- marked-content reference
- MCID
- ParentTree
- logical reading order
- artifact
- alt text
- document properties
- primary language

Avoid:
- attachment
- “attach the tag” as the main description
- generic linking metaphors

---

## Frozen node names

Use these names consistently unless there is a strong reason to change them:

- `ingest_pdf`
- `render_pages`
- `region_proposal`
- `vision_analysis`
- `ocr_layout_analysis`
- `native_pdf_analysis`
- `accessibility_review`
- `artifact_check`
- `caption_association`
- `tagging_plan`
- `document_consistency`
- `structure_mapping_plan`
- `behavior_check`
- `approval_gate`
- `write_tagged_draft`
- `validator_check`
- `human_review`
- `apply_review_decisions`
- `finalize_accessible_output`
- `workflow_orchestrator`

---

## Current repository shape

Keep this structure unless there is a concrete reason to change it:

```text
src/pdf_accessibility/
├── config.py
├── cli.py
├── constants.py
├── models/
├── reducers/
├── transition_guards/
├── nodes/
├── graph/
├── services/
├── persistence/
├── writeback/
└── utils/
```

### Module boundaries

- `models/`: typed state, events, findings, review tasks, review decisions, validator findings, workflow trace entries, artifacts
- `reducers/`: event application and derived snapshot recomputation
- `transition_guards/`: legal state-change checks
- `nodes/`: specialist workflow nodes that emit events
- `graph/`: LangGraph wiring and orchestration
- `services/`: wrappers for concrete libraries and external tools
- `persistence/`: checkpoints, manifests, JSON writes, run folders
- `writeback/`: tagged draft and final output construction
- `utils/`: ids, timestamps, paths, logging

Do not blur these boundaries casually.

---

## Dependency plan

### Required now

- `langgraph`
- `pydantic`
- `pymupdf`
- `pikepdf`
- `typer`

### Optional now

- `pymupdf4llm`, for local layout/text experiments when useful

### Deferred

- `ocrmypdf`, for scanned/image-heavy handling
- `verapdf`, for external PDF/UA validation

Use heavier layout/OCR/AI stacks later only if the simpler stack proves insufficient.

Do not add extra orchestration frameworks on top of LangGraph for v0.1.0.

---

## Node contract

Nodes must follow this rule:

- read the current snapshot
- emit typed events
- do not mutate shared state directly

Preferred node signature:

```python
def run(document: DocumentState) -> list[NodeEvent]:
    ...
```

State changes belong in reducers, not specialist nodes.

---

## Reducer and transition-guard rules

### Reducers

Reducers are the only place where shared state should be updated.

They must be:
- deterministic
- scope-limited
- provenance-preserving

### Transition guards

Use transition guards for legal state changes, including:

- region transitions
- workflow transitions
- approval
- draft writing
- finalization

Do not bypass transition guards.

---

## Artifact rules

Every run must preserve artifact history.

Required JSON/log artifact classes:

- `document_state.json`
- `findings.jsonl`
- `review_tasks.json`
- `review_decisions.json`
- `validator_findings.json`
- `finalization_status.json`
- `artifact_manifest.json`
- `run_log.json`

Conditional PDF output artifact classes:

- `tagged_draft.pdf`, only when draft write is legal
- `accessible_output.pdf`, only when finalization is legal

### Important rules

- Never overwrite the source PDF in place.
- Register every written artifact in the manifest.
- `tagged_draft.pdf` must exist only when draft write is legal.
- `accessible_output.pdf` must exist only when finalization is legal.
- A tagged draft may exist while the document still needs review.

---

## Working rules for Codex

### Before changing code

1. Read the nearest relevant spec files first.
2. Preserve the frozen terminology.
3. Preserve the v0.1.0 scope boundary.
4. Prefer the smallest change that moves implementation forward.

### During implementation

- Keep the narrow one-PDF path working.
- Keep write-back, validation, review, and finalization first-class.
- Keep node logic simple and event-oriented.
- Keep reducers and transition guards explicit and testable.
- Prefer local/open tools already selected for the stack.

### When uncertain

- Do not invent missing architecture casually.
- Do not broaden support silently.
- Add a TODO or draft note rather than pretending a hard problem is solved.

### Stop and surface uncertainty

Stop and explain the issue before continuing when:

- the requested change would expand v0.1.0 scope
- output would be mislabeled as finalized
- writeback mechanics are underspecified
- validator or finalization logic conflicts with frozen rules
- a naming change would break frozen terminology

---

## Skills

Repo-local skill playbooks live in:

```text
.agents/skills/
```

Current repo-local skill playbooks are:

- `pdf-workflow-state`
- `pdf-writeback-output`
- `terminology-scope-check`

When a task clearly matches one of these procedures, read the relevant `SKILL.md` directly before implementing. Do this even if the runtime does not auto-register repo-local skills as available Codex skills.

---

## Testing and verification

Prioritize tests for:

- reducer behavior
- transition guards
- blocker recomputation
- artifact registration
- workflow routing
- finalization gating

At minimum, changes that affect state logic should include targeted tests.

Do not claim the workflow is done if it cannot yet preserve the path toward real PDF output artifacts.

---

## Definition of done for v0.1.0 work

A change is only done when it preserves or improves the actual workflow path:

- input PDF
- structured findings
- shared state update
- tagged draft output path
- validator path
- review-task path
- finalization control

For v0.1.0, “done” does **not** mean universal remediation. It means the narrow workflow is executable, honest, and stable.
