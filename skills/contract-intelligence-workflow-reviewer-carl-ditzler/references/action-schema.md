# Action Schema

Use this file whenever the skill needs to recommend or prepare the next workflow step.

## Purpose

The review should not end with analysis only. Convert the current state of the contract into a clear next action that a human or automation layer can execute.

## Action Types

Use one primary action type:

- `request_missing_documents`
- `route_for_internal_review`
- `revise_contract`
- `prepare_redline_packet`
- `prepare_approval_packet`
- `open_research_task`
- `draft_business_summary`
- `draft_counterparty_message`
- `mark_signature_ready`
- `close_matter`

## Required Action Packet

Write `action-packet.yaml` using this schema:

```yaml
action_packet:
  action_type: ""
  current_state: ""
  next_state: ""
  why_now: ""
  confidence: "high|medium|low"
  blocking: true
  required_approvals: []
  destination:
    tool_alias: ""
    location: ""
    mode: "allowed|approval-required|suggest-only|none"
  recipients:
    resolved: []
    unresolved: []
  notification:
    method: "slack|email|ticket|manual|none"
    approved: false
  prerequisites: []
  artifacts:
    required: []
    generated: []
  notes: []
```

## Decision Rules

- Choose the smallest useful next action, not every possible action.
- If required information is missing, prefer `request_missing_documents`.
- If a specialist must review before progress, prefer `route_for_internal_review`.
- If legal changes are required, prefer `prepare_redline_packet` or `revise_contract`.
- If the contract is ready pending signoff, prefer `prepare_approval_packet` or `mark_signature_ready`.

## Output Rules

- State the recommended action in prose.
- Save the same result in the machine-readable action packet.
- If no automated action is permitted, still output the action as `suggest-only`.
