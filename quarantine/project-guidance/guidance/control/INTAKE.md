# Intake

## Purpose

Use this file to capture new incoming work before it becomes part of the active project.

## Current intake items

### Item 1
- Type: improvement
- Short title: Align project management artifacts with implemented v0.1.0 PDF accessibility scaffold
- Source: User request on 2026-04-22 to run project-intake on `accessibility_by_manifest`
- Why it matters: The repository has both concrete v0.1.0 workflow direction in `AGENTS.md` and `v0.1.0_plan.md` and an implemented `src/pdf_accessibility/` scaffold with typed state, typed events, reducers, transition guards, persistence, writeback modules, LangGraph/fallback orchestration, and targeted tests. The project management files were placeholders before this intake pass, so they do not yet reflect the actual implemented state.
- Requested outcome: Classify the request and identify the correct next artifact for turning the existing v0.1.0 implementation and specs into maintained project structure.
- Urgency: normal
- Triage decision: move into project planning
- Notes: This intake item should not silently become active implementation work. Static inspection found `src/pdf_accessibility/models`, `reducers`, `transition_guards`, `nodes`, `graph`, `persistence`, `writeback`, and `services`, plus `tests/pdf_accessibility`. Verification with `.venv/bin/python -m pytest tests/pdf_accessibility` passed 34 tests. The next pass should use project planning to populate `PLAN.md` from the implemented scaffold and existing repository specs while preserving the frozen v0.1.0 scope, terminology, node names, artifact rules, tagged draft output path, validator path, human review path, and finalization gating.

No other active intake items are recorded.

## Intake categories

Use one:
- bug
- feature
- improvement
- cleanup
- decision needed
- research needed
- other

## Triage decisions

### Decision log
- 2026-04-22 Item 1:
  - Triage outcome: move into project planning
  - Reason: Initial intake classified the request as project-structure work rather than implementation work.
- 2026-04-22 Item 1 follow-up verification:
  - Triage outcome: still move into project planning
  - Reason: The request is about organizing project state, not implementing code. Existing specs and `src/pdf_accessibility/` already define and partially implement the narrow v0.1.0 PDF accessibility workflow. The smallest correct next artifact is an updated `PLAN.md` grounded in the real scaffold and passing targeted tests, followed by `STATUS.md`/`HANDOFF.md` maintenance as needed.

## Open questions

- Should `project-file-structure-md/` remain the canonical location for project management artifacts, or should the planning file set move to the repository root?

## Next intake review

- Date: after the user reviews the planning recovery pass
- Owner: project maintainer
