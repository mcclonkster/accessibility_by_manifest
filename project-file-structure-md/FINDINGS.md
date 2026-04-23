# Findings

## Question Addressed In This Pass

- What does the repository actually contain, and what must the planning documents say before they can be used as reliable project sources of truth?

## Source-Grounded Findings

### Finding 1
- Finding: `AGENTS.md` is the strongest governing source for current v0.1.0 PDF workflow work.
- Source: `AGENTS.md`
- Confidence: high
- Notes: It freezes v0.1.0 scope, terminology, node names, module boundaries, artifact rules, node contracts, reducer/transition guard rules, and definition of done.

### Finding 2
- Finding: `src/pdf_accessibility/` implements the v0.1.0 PDF accessibility workflow scaffold described by `AGENTS.md`.
- Source: `src/pdf_accessibility/`
- Confidence: high
- Notes: It contains models, events, reducers, transition guards, nodes, graph wiring, persistence, services, writeback, and utilities.

### Finding 3
- Finding: `accessibility_by_manifest/` remains active implementation, not archive.
- Source: `accessibility_by_manifest/`, `README.md`, `PROJECT.md`, `tests/`
- Confidence: high
- Notes: It supports manifest-first PPTX, PDF, DOCX, normalization, review, output projections, Adobe comparison, and local sidecar evidence paths.

### Finding 4
- Finding: The two implementation tracks have different centers of gravity.
- Source: `AGENTS.md`, `PROJECT.md`, `README.md`, `src/pdf_accessibility/`, `accessibility_by_manifest/`
- Confidence: high
- Notes: `accessibility_by_manifest/` is broad input -> manifest -> output infrastructure. `src/pdf_accessibility/` is the narrow shared-state v0.1.0 tagged PDF workflow with finalization gating.

### Finding 5
- Finding: Full repo tests currently pass in the repo-local virtual environment.
- Source: `.venv/bin/python -m pytest`
- Confidence: high
- Notes: 67 tests passed on 2026-04-22. System Python is not reliable for this repo because it lacked `pikepdf` during an earlier targeted test run.

### Finding 6
- Finding: `test_outputs/pdf_accessibility_runs/finreport25_20260422T115228Z/` demonstrates honest `needs_review` termination on a real 117-page PDF.
- Source: `test_outputs/pdf_accessibility_runs/finreport25_20260422T115228Z/run_log.json`
- Confidence: high
- Notes: The run recorded 117 pages, 1328 normalized units, 269 review tasks, 222 unresolved blockers, no tagged draft, and no accessible output.

### Finding 7
- Finding: The broader manifest-first PDF pipeline has produced a substantial `finreport25` output set.
- Source: `test_outputs/finreport25_manifest_output/`
- Confidence: high
- Notes: The master manifest reports 117 pages, 4311 raw blocks, 1402 normalized blocks, 112 normalized tables, 69 review entries, and extractor evidence from deterministic and optional sidecar sources.

### Finding 8
- Finding: A generated no-draft `validator_findings.json` can be misleading.
- Source: `test_outputs/pdf_accessibility_runs/finreport25_20260422T115228Z/validator_findings.json`, `src/pdf_accessibility/persistence/artifacts.py`
- Confidence: high
- Notes: The file says the internal validator passed while checking a `tagged_draft.pdf` path even though no tagged draft exists in that run. Planning should treat this as an implementation task.

### Finding 9
- Finding: Older draft specs contain superseded names and terminology.
- Source: `docs/pdf_spec_drafts/`, `AGENTS.md`, `.agents/skills/terminology-scope-check/SKILL.md`
- Confidence: high
- Notes: Examples include old node names such as `artifact_repetition_check`, `tagging_plan_region`, `validator_check_document`, and `human_review_router`. `AGENTS.md` and the terminology freeze supersede these.

### Finding 10
- Finding: `archive/` is historical and should not drive current planning without explicit promotion.
- Source: `archive/README.txt`, `archive/project-current-state-report.md`
- Confidence: high
- Notes: Archive material describes earlier PPTX/DOCX script work and chat-extracted artifacts. It is useful context, not current authority.

## Synthesis

The project is not empty or merely conceptual. It has substantial working code and tests. The immediate failure was planning governance: placeholder project files made it impossible to know what was authoritative without re-reading the repo.

The safest current planning model is:

- `AGENTS.md` governs v0.1.0 PDF tagged workflow constraints.
- `src/pdf_accessibility/` is the current implementation for that workflow.
- `accessibility_by_manifest/` remains the broader manifest-first system.
- `docs/pdf_spec_drafts/`, `docs/chats/`, and `archive/` are supporting/historical unless explicitly promoted.

## Conflicts Or Disagreements

- `PROJECT.md` and `README.md` describe the broader manifest-first package as the project center, while `AGENTS.md` describes the current repository purpose as a local/open-first PDF accessibility workflow with a different package layout under `src/pdf_accessibility/`.
- Older draft specs include stale node names and superseded decision wording that conflicts with the frozen terminology.
- Generated validator output can imply a pass in a no-draft run, which conflicts with the artifact/finalization honesty rules.

## What Remains Unknown

- Whether `project-file-structure-md/` should remain the canonical location for project management files.
- Whether the two active implementation tracks should remain separate long-term.
- How much of the broader manifest-first PDF evidence should be integrated into `src/pdf_accessibility/` for v0.1.0.
- Whether generated `test_outputs/` should be curated or rebuilt before being cited in future planning.

## What Planning Should Know Next

- Do not start new implementation from `docs/pdf_spec_drafts/` without checking `AGENTS.md` and current code first.
- Do not use generated output files as proof of current behavior unless the command that produced them is known or rerun.
- Use `.venv/bin/python`, not system Python, for verification.
- Treat `needs_review` as a valid terminal state for real documents in v0.1.0.

## Follow-Up Research Needed

- No external research is needed for the immediate planning recovery.
- Internal research is needed to decide how to reconcile `accessibility_by_manifest/` with `src/pdf_accessibility/`.
