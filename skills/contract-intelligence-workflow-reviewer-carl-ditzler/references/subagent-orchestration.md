# Sub-Agent Orchestration

Use this file only when the platform supports sub-agents and the user or platform policy allows delegation.

## Objective

Sub-agents can improve speed and coverage, but only if their work is bounded and synchronized through shared contract artifacts.

## Canonical Shared Inputs

Before delegating, create:

- one canonical `intake.yaml`
- one canonical `document-map.md`
- one canonical `priority-profile.yaml`

All sub-agents must work from those artifacts, not from separate ad hoc summaries.

## Recommended Agent Split

### Intake Agent

Responsibility:

- normalize intake
- identify missing docs
- draft `intake.yaml`

### Playbook Agent

Responsibility:

- normalize playbook, templates, fallback language, and prior deals
- draft `playbook.normalized.yaml`

### Contract Map Agent

Responsibility:

- identify clause families
- list exhibits and incorporated documents
- check definitions and cross-references
- update `document-map.md`

### Review Agent

Responsibility:

- perform clause-by-clause comparison
- draft issue candidates in `issues.csv`

### Redline Agent

Responsibility:

- draft preferred and fallback edits in `redlines.md`

### QA Agent

Responsibility:

- run failure-mode checks
- check consistency across issues, redlines, and approvals
- draft `qa-report.md`

## Delegation Rules

- Delegate only bounded, file-scoped tasks.
- Keep one owner for each artifact to avoid merge conflicts.
- Do not let sub-agents invent independent priorities or approval rules.
- The lead reviewer must integrate and resolve contradictions.
- Final legal judgment stays with the lead reviewer.

## When Not To Use Sub-Agents

Do not use sub-agents when:

- the platform does not support them
- the user has not allowed them
- the contract is too small to justify orchestration
- the document is so sensitive that the user wants a single-agent review only

## Maximum Useful Parallelism

In most contract reviews, 3 to 5 bounded sub-agents is enough. More than that usually creates integration overhead unless the contract is very large.
