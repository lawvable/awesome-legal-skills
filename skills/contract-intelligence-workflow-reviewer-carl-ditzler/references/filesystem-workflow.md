# Filesystem Workflow

This file defines the reusable on-disk structure for contract review work.

## Workspace Structure

Use this structure in the active workspace:

```text
.contract-review/
  config.yaml
  connectors.yaml
  workflow-tools.yaml
  approvals.yaml
  memory-policy.yaml
  playbooks/
    <playbook-slug>/
      metadata.yaml
      source.md
      normalized.yaml
  contracts/
    <contract-slug>/
      contract.yaml
      intake.yaml
      document-map.md
      playbook.normalized.yaml
      playbook-comparison.csv
      priority-profile.yaml
      workflow-state.yaml
      issues.csv
      redlines.md
      negotiation-plan.md
      approval-routing.md
      approval-routing.json
      action-packet.yaml
      review-summary.json
      research-notes.md
      drafting-output.md
      metrics.yaml
      qa-report.md
```

## Source Of Truth

- Global reusable settings live in `.contract-review/`.
- Reusable playbook artifacts live under `.contract-review/playbooks/`.
- Contract-specific facts live only in that contract folder.
- `CLAUDE.md` is a concise mirror, not the system of record.

## Contract Folder Rules

Create a contract folder when:

- a contract review actually begins
- the user asks to save the review
- the review needs resumability across sessions

Suggested slug format:

`YYYY-MM-DD-counterparty-contract-type-short-name`

## Playbook Folder Rules

Create a playbook folder when:

- the user uploads a playbook file
- the user connects an approved cloud playbook file
- a new controlling playbook needs to be normalized for reuse

Suggested slug format:

`team-or-company-playbook-short-name`

## Required Playbook Files

### `metadata.yaml`

Source provenance, extraction method, source format, and extraction confidence.

### `source.md`

Readable Markdown extraction of the playbook for model use and human verification.

### `normalized.yaml`

Canonical structured playbook used for comparison and scoring.

## Required Contract Files

### `contract.yaml`

High-level contract metadata:

- contract name
- counterparty
- represented party
- contract type
- review mode
- status
- document locations

### `intake.yaml`

The normalized intake record from the intake form.

### `document-map.md`

Agreement title, parties, exhibits, referenced external docs, missing docs, and key structural notes.

### `playbook.normalized.yaml`

The merged clause playbook used for this contract.

### `playbook-comparison.csv`

Clause-by-clause playbook comparison with status, deviation score, impact band, color label, likely impact, and confidence.

### `priority-profile.yaml`

The top priorities, role adjustments, and required internal reviewers.

### `issues.csv`

A structured issue log with one row per issue.

### `redlines.md`

Preferred edits and fallback language.

### `negotiation-plan.md`

Must-win issues, tradeables, leverage notes, and counterparty rationale.

### `approval-routing.md`

Which functions must review or approve and why.

### `approval-routing.json`

The same approval routing in machine-readable form for automation, including named approvers, contact paths, notification mode, and unresolved recipients.

### `workflow-state.yaml`

Current lifecycle state, previous state, allowed transitions, blocker list, and next state recommendation.

### `action-packet.yaml`

Machine-readable next-step payload for workflow automation.

### `review-summary.json`

Structured summary of the current review result, blockers, and next action.

### `research-notes.md`

Clause-specific research output when research mode is used.

### `drafting-output.md`

Contract drafting, approval memo, email draft, or summary deliverable when drafting mode is used.

### `metrics.yaml`

Cycle-time and workflow metrics for the contract.

### `qa-report.md`

Failure-mode results, QA verdict, and benchmark summary.

## Write Rules

- Save after setup if global config is new or changed.
- Save playbook artifacts when a playbook is uploaded, fetched, or re-normalized.
- Save after intake if contract tracking is enabled.
- Save again after review, after negotiation planning, and after QA.
- Do not write files the user has opted out of.
- Do not write fetched or uploaded contracts to disk unless the user permits local copies.
- When the contract is closed, review whether contract-specific artifacts should be retained or deleted under the saved memory and retention policy.

## Resume Rules

On a later session:

1. Load `.contract-review/config.yaml`
2. Load the relevant contract folder if one exists
3. Ask only for missing updates
4. Continue the workflow from the latest saved stage

## Minimal CSV Columns For `issues.csv`

Use these columns:

```text
clause_reference,status,risk,issue_summary,why_it_matters,recommended_position,suggested_redline,acceptable_fallback,approver_or_reviewer,confidence,notes
```

## Minimal CSV Columns For `playbook-comparison.csv`

Use these columns:

```text
clause_reference,playbook_status,deviation_score,impact_band,color_label,likely_impact,why_it_matters,recommended_response,confidence,notes
```
