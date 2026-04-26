# Run Observability Schema

This document defines the local run-record contract for `pdf_accessibility`.

## Run Folder

Each serious run should contain:

```text
<run_dir>/
  manifest.json
  command.txt
  config.json
  environment.txt
  git.txt
  status.json
  notes.md

  inputs/
    manifest.json

  outputs/
    manifest.json

  metrics/
    summary.json
    timings.csv

  logs/
    execution.log
    debug.log
    events.jsonl
    run_explanation.log
```

## Status Lifecycle

`status.json` uses these lifecycle values:

- `queued`
- `running`
- `completed`
- `failed`
- `interrupted`
- `abandoned`

Workflow outcome is tracked separately through:

- `document_status`
- `finalization_state`
- `terminal_state`

Example:

```json
{
  "run_id": "finreport25_20260426T153708Z",
  "run_status": "completed",
  "started_at": "2026-04-26T15:37:08.231000+00:00",
  "ended_at": "2026-04-26T15:37:50.079000+00:00",
  "duration_ms": 41848,
  "exit_code": 0,
  "document_status": "needs_review",
  "finalization_state": "needs_review",
  "blocker_count": 101,
  "terminal_state": "needs_review"
}
```

## Metrics

`metrics/summary.json` is the compact numeric summary for the run. It should include:

- run id
- document status
- finalization state
- counts for pages, normalized units, findings, review tasks, review decisions, validator findings, blockers
- blocker counts by issue code
- warning count
- error count
- total duration in milliseconds
- node count

`metrics/timings.csv` records per-node timings with:

- `node_name`
- `action`
- `started_at`
- `ended_at`
- `duration_ms`
- `event_count`
- `before_status`
- `after_status`
- `before_finalization_state`
- `after_finalization_state`
- `reason`

## Structured Event Stream

`logs/events.jsonl` is the machine-readable event stream. It is the preferred source for tooling, comparison, and downstream parsing.

Each line is one JSON object with stable fields.

### Core Fields

- `@timestamp`
- `message`
- `log.level`
- `log.logger`
- `service.name`
- `event.dataset`
- `process.pid`
- `run.id`
- `run.dir`

### Event Fields

Important events may also include:

- `event.action`
- `node.name`
- `event.count`
- `duration.ms`
- `document.status.before`
- `document.status.after`
- `finalization.state.before`
- `finalization.state.after`
- `blocker.count.before`
- `blocker.count.after`
- `review.task.count.before`
- `review.task.count.after`
- `skip.reason`
- `artifact.path`
- `ai.provider`
- `error.message`

The field names are intentionally stable and machine-oriented. Human-readable interpretation belongs in:

- `logs/execution.log`
- `logs/debug.log`
- `run_explanation.md`

## Run Manifest

`manifest.json` is the run-record index. It points to:

- command/config/env/git files
- log files
- metrics files
- input/output manifests
- artifact manifest

This makes the run folder usable as a local, reproducible run record rather than a loose pile of files.
