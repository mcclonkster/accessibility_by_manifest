---
name: pdf-workflow-state
description: Use when working on the PDF accessibility workflow's shared state, typed events, reducers, transition guards, blocker recomputation, workflow status changes, finalization state, or LangGraph state application patterns in this repo.
metadata:
  short-description: Maintain PDF workflow state
---

# PDF Workflow State

## When to use this skill

Use this skill when working on:

- typed state models
- typed events
- reducers
- transition guards
- blocker recomputation
- workflow-state changes
- finalization-state changes
- LangGraph state application patterns
- workflow trace entries

## Goal

Keep the workflow state:

- deterministic
- append-only where history matters
- explicit about blockers
- explicit about approvals
- explicit about finalization
- explicit about workflow routing decisions
- safe for reopen paths

## Core rules

- Nodes emit typed events.
- Reducers apply those events.
- Transition guards decide whether movement is legal.
- The workflow orchestrator routes from recomputed state.
- Do not let specialist nodes mutate shared state directly.
- Preserve versioned artifacts and blocker derivation.
- Record workflow routing decisions in `workflow_trace` rather than hiding them in ad hoc logs.

## Priority modules

1. `models/`
2. `reducers/`
3. `transition_guards/`
4. `graph/`

## Output expectations

Changes in this area should preserve or improve:

- typed event flow
- reducer determinism
- blocker recomputation
- workflow trace accuracy
- reopen behavior
- approval and finalization control

## Do not do

- do not redesign the workflow model
- do not add unsupported v0.1.0 content classes
- do not hide blockers
- do not let finalization bypass validator or review blockers
- do not let nodes directly rewrite the full document snapshot

## Quick checklist

Before finishing:

- Are nodes still event-oriented?
- Are reducers still the only state writers?
- Are transition guards still explicit?
- Are blockers still derived centrally?
- Are run/skip routing decisions visible in `workflow_trace` and `run_log.json`?
- Is finalization still impossible with blocking issues active?
