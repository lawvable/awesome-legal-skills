# MCP Integrations

This file governs how to use connector or MCP-backed data sources in contract review.

## Applicability

MCP or connector integrations are useful for:

- pulling contracts from approved cloud drives
- retrieving playbooks, templates, clause banks, and prior deals
- loading approval policies or internal documentation
- creating approval tasks in workflow systems
- tracking the current negotiation packet across systems
- updating workflow state in approved contract systems
- delivering machine-readable action packets to approved downstream tools

## Setup Data To Capture

During setup, ask the user for:

- approved connector names
- a human-friendly alias for each source
- approved locations within each source
- what each source is allowed to provide
- whether local download is allowed
- whether the source may be used for precedent or only for the current contract
- whether the source may provide controlling playbook files
- whether extracted Markdown and normalized YAML may be saved from that source
- whether the approved scope is file-level, folder-level, or broader
- whether broad drive or site access is prohibited

Save that to `.contract-review/connectors.yaml`.
Save operational routing tools and permissions to `.contract-review/workflow-tools.yaml`.

## Recommended Connector Categories

- Cloud storage: Google Drive, Dropbox, Box, OneDrive, SharePoint
- Knowledge sources: internal wiki, policy libraries, clause banks, playbook repositories
- Workflow tools: ticketing, approval, or intake systems
- CLM or e-sign systems: agreement status, attachments, approval history
- Messaging or notification destinations that are approved for summaries or approval packets, such as Slack or email systems

## Approver Directory And Messaging Rules

- If a connector can expose a user directory, team roster, or identity picker, the skill may use it to resolve approver identities only when that connector is approved.
- If a Slack or messaging connector is not configured or does not expose user lookup, collect approver names, emails, Slack handles, or Slack user IDs manually.
- Do not assume that a Slack workspace or channel is approved merely because Slack is connected.
- Treat automated notifications as available only when both the connector and the destination are approved in `.contract-review/workflow-tools.yaml`.
- If the platform cannot send the notification directly, still prepare the approval packet and recipient list so the user can send it manually.

## Source Control Rules

- Never query a connector that has not been approved by the user.
- Never assume a folder, drive, site, or collection is approved just because the connector exists.
- Prefer specific files or narrow folders over full drives, sites, or workspaces.
- Treat broad connector scope as an explicit exception that requires user acknowledgment of increased security risk.
- Record provenance in the contract files for every externally sourced document used in the review.
- If a required document is unavailable through the connector, ask the user to upload it or share a permitted link.
- If the source is used for a playbook, record both the source file identifier and the derived playbook artifact locations.

## Remote MCP Trust Rules

- Do not use a custom or remote MCP server unless the user confirms it is trusted or organization-approved.
- If the server is third-party or newly introduced, warn that provider safeguards are not foolproof and that tool behavior may change outside the skill's control.
- Prefer organization-managed or vendor-official connectors over unknown third-party servers.

## Provenance Recording

For every external source used, record in `contract.yaml` or `document-map.md`:

- source alias
- connector type
- path or identifier
- purpose of use
- whether it was used as contract, playbook, precedent, or policy input

For playbook files, also record:

- whether the source became the controlling playbook
- where the extracted Markdown was saved
- where the normalized YAML was saved
- extraction confidence

## Connector Conflict Rules

If two connector sources conflict:

- prefer the source order saved in `.contract-review/config.yaml`
- if no priority is saved, ask the user which source controls
- do not silently merge contradictory versions

## Output Requirements

If MCP sources materially shaped the review, say so in the review status:

- which sources were used
- which sources were missing
- whether any unavailable source reduced confidence

If a workflow tool was used or prepared as the next step, include:

- destination alias
- action type
- whether human approval is still required
- whether the system resolved named recipients from the connector or used saved manual contacts
