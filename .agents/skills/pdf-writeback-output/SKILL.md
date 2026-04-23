---
name: pdf-writeback-output
description: Use when working on tagged PDF draft writing, structure tree output, structure mapping, marked content, MCIDs, ParentTree entries, artifact registration, validator-to-output flow, finalization gating, or accessible PDF output paths in this repo.
metadata:
  short-description: Maintain PDF writeback output
---

# PDF Write-Back and Output Path

## When to use this skill

Use this skill when working on:

- tagged draft writing
- structure tree work
- structure mapping
- marked content
- MCID mapping
- ParentTree mapping
- artifact output registration
- finalization output logic
- validator-to-output flow

## Goal

Preserve the real PDF output path:

- `tagged_draft.pdf` only when draft write is legal
- `validator_findings.json`
- `review_tasks.json`
- `review_decisions.json`
- `finalization_status.json`
- `accessible_output.pdf` only when finalization is legal

## Core rules

- Never overwrite the source PDF in place.
- A tagged draft may exist before finalization, but only after draft write is legal.
- `accessible_output.pdf` must only be written after finalization is legal.
- Preserve artifact history in the manifest.
- Use PDF-standard language in code comments and specs:
  - structure tree
  - structure element
  - marked content
  - MCID
  - ParentTree
  - logical reading order
  - artifact

## Priority modules

1. `writeback/`
2. `nodes/write_tagged_draft.py`
3. `nodes/validator_check.py`
4. `nodes/finalize_accessible_output.py`
5. `services/internal_validator.py`
6. `persistence/`

## Output expectations

Changes in this area should preserve or improve:

- draft output creation
- manifest registration
- validator integration
- review decision integration
- finalization gating
- honest handling of `needs_review` and `write_blocked`

## Do not do

- do not drift into analysis-only output
- do not mark drafts as final by default
- do not replace PDF-standard terms with homemade ones
- do not write final output while blockers remain
- do not treat machine validation as the entire accessibility story

## Quick checklist

Before finishing:

- Is the source PDF preserved?
- Is every written artifact registered?
- Can the workflow distinguish draft from final output?
- Are `review_decisions.json` and review blockers preserved in the output path?
- Are finalization blockers still enforced?
- Is the write-back language still aligned with PDF standards terminology?
