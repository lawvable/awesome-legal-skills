# Human Approval Gates

Use this file before recommending or executing any outward-facing or system-changing action.

## Actions That Require Human Approval

Treat these as approval-gated unless the saved configuration explicitly says otherwise:

- sending a counterparty email
- sending a redline packet externally
- sending an internal Slack message, direct message, email, or ticket through an external connector
- changing contract status to signature-ready or closed
- creating or updating an approval task in an external system
- routing to a destination outside the approved tool list
- persisting contract-specific sensitive content beyond the current contract folder

## Actions That May Be Suggest-Only

Unless the user has explicitly approved automation:

- prepare drafts
- prepare machine-readable action packets
- prepare approval packets
- prepare summaries
- suggest state transitions

## Gate Check

Before outputting a next action, answer:

1. Is the action internal or external?
2. Does the action change system state?
3. Is the destination approved in saved configuration?
4. Is the action mode `allowed`, `approval-required`, or `suggest-only`?
5. Which human approvers must sign off first?
6. Are the recipients resolved to approved names or connector identities?

If any answer is unresolved, classify the action as `approval-required`.
