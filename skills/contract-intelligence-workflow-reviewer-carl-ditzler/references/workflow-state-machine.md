# Workflow State Machine

Use this file to track where the contract is in the lifecycle and what state transition is appropriate.

## States

- `setup`
- `intake`
- `triage`
- `review`
- `redline`
- `negotiation`
- `internal_approvals`
- `signature_ready`
- `closed`

## State Meanings

- `setup`: global workspace configuration is still missing or incomplete
- `intake`: documents and business context are being gathered
- `triage`: a limited first-pass screen is underway
- `review`: substantive clause analysis is in progress
- `redline`: drafting revisions or fallback language are being prepared
- `negotiation`: open issues and fallback positions are being managed
- `internal_approvals`: the contract is waiting on legal or business approvals
- `signature_ready`: blockers are cleared and the package is ready for execution
- `closed`: the review workflow is complete

## Allowed Transitions

- `setup -> intake`
- `intake -> triage`
- `intake -> review`
- `triage -> intake`
- `triage -> review`
- `review -> redline`
- `review -> internal_approvals`
- `redline -> negotiation`
- `redline -> internal_approvals`
- `negotiation -> redline`
- `negotiation -> internal_approvals`
- `internal_approvals -> redline`
- `internal_approvals -> signature_ready`
- `signature_ready -> closed`

## State Update Rules

- Do not move to `review` until intake minimums are met.
- Do not move to `redline` until the priority model is applied.
- Do not move to `internal_approvals` until the approval table is built.
- Do not move to `signature_ready` if there are unresolved blocking approvals or material unresolved issues.
- If the user only wants a summary on incomplete inputs, remain in `triage`.

## Required Workflow State File

Save `workflow-state.yaml` with:

```yaml
workflow_state:
  current_state: ""
  previous_state: ""
  recommended_next_state: ""
  blockers: []
  rationale: []
  last_updated_stage: ""
```
