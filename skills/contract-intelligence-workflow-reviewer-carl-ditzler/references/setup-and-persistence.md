# Setup And Persistence

This file governs first-run setup, persistent memory, and reusable workspace configuration for contract review.

## Purpose

The goal is to avoid asking the same organizational questions every time while keeping confidential deal content out of long-lived memory by default.

Use a dual-layer model:

- `CLAUDE.md` is the Claude-facing summary of durable instructions and preferences.
- `.contract-review/` is the cross-platform source of truth for both Claude and Codex.

If both exist and conflict, `.contract-review/` controls. Update `CLAUDE.md` to match.

## First-Run Detection

Enter Setup Mode when any of these are true:

- `.contract-review/config.yaml` does not exist
- `.contract-review/connectors.yaml` does not exist
- `.contract-review/approvals.yaml` does not exist
- `CLAUDE.md` does not exist and the user wants Claude compatibility
- The user says setup has changed

## What To Ask The User

Ask for setup information in short batches. Do not dump the full questionnaire at once unless the user asks for a complete form.

### Batch 1: Organization Defaults

- Organization or business unit name
- Default represented party
- Typical contract types reviewed
- Default user role or team
- Default risk posture
- Whether the team is usually reviewing its own paper or counterparty paper

### Batch 2: Playbook And Source Locations

- Where standard templates live
- Where playbooks, clause banks, fallback language, and prior deals live
- Preferred comparison source order
- Whether prior agreements may be used as fallback precedent
- Whether playbooks will be uploaded directly, fetched from approved cloud sources, or both
- Whether original playbook files may be copied locally
- Preferred derived playbook format order: source Markdown, normalized YAML, or both

### Batch 3: Approval Routing

- Legal approver names and contact details
- Finance approver names and contact details
- Security approver names and contact details
- Privacy approver names and contact details
- Procurement approver names and contact details
- Product or engineering approver names and contact details
- Compliance approver names and contact details
- Insurance or risk approver names and contact details
- Executive approver names and contact details
- Which approvals are blocking versus advisory
- Preferred notification path for each approver: Slack, email, ticket, or manual
- Slack user ID, Slack handle, or channel when Slack notifications are approved
- Escalation contacts or fallback approvers
- Whether contract-specific approvers should override the saved defaults

### Batch 4: Filesystem And Output Preferences

- Workspace path for contract folders
- Whether to save contract artifacts automatically
- Preferred file formats
- Naming convention for contract folders
- Whether to save negotiation drafts and approval packets

### Batch 5: MCP Connectors

- Which connectors are approved for use
- Alias for each connector or source
- Which specific files or folders are approved
- Whether any broader drive, site, or collection access is truly necessary
- Whether uploads or fetched files may be written locally
- Whether connector data may be used as playbook or precedent input
- Whether enterprise or admin-managed connector controls are available and should govern approvals

### Batch 5B: Workflow Tools And Actions

- Which workflow tools are approved for routing tasks or changing status
- Which destinations may receive summaries, approval packets, or redline instructions
- Which actions are `allowed`, `approval-required`, or `suggest-only`
- Whether the system may update contract state automatically
- Whether the system may draft but not send external communications
- Whether Slack, email, ticketing, or other messaging tools may be used for internal notifications
- Whether the tool may resolve users from a connector directory instead of manual entry
- Whether the tool may send direct messages, channel posts, or create tickets automatically
- Whether outbound write actions should remain `suggest-only` by default

### Batch 6: Memory, Confidentiality, And Sub-Agents

- What may be stored persistently
- What must never be stored
- Contract retention preferences
- Whether counterparty memory may be retained
- Whether sub-agents may be used
- Maximum number of parallel sub-agents
- Which tasks may be delegated

### Batch 7: Research And Drafting Preferences

- Approved research sources
- Citation requirement level
- Whether summaries should be business-facing, legal-facing, or both
- Preferred drafting style for redlines, memos, emails, and issue summaries
- Preferred machine-readable payload formats

## Save Targets

Save the answers into these files:

- `.contract-review/config.yaml`
- `.contract-review/connectors.yaml`
- `.contract-review/workflow-tools.yaml`
- `.contract-review/approvals.yaml`
- `.contract-review/memory-policy.yaml`
- `CLAUDE.md`

For active work, create contract-specific files under `.contract-review/contracts/<contract-slug>/`.
For reusable playbooks, create playbook-specific files under `.contract-review/playbooks/<playbook-slug>/`.

## Required File Semantics

### `.contract-review/config.yaml`

Global defaults for:

- organization profile
- contract-review defaults
- filesystem preferences
- sub-agent preferences
- output preferences
- playbook ingestion preferences

### `.contract-review/connectors.yaml`

Approved connector list, alias names, approved source locations, and allowed use cases.

This file should also record which connectors may provide controlling playbook files.
Record the narrowest approved scope possible and whether broad drive or site access is prohibited.

### `.contract-review/workflow-tools.yaml`

Approved operational tools, routing destinations, directory sources, messaging permissions, and permitted automation actions.

Unless the user explicitly chooses otherwise, outbound connector actions should default to `suggest-only`.

### `.contract-review/approvals.yaml`

Approver identities, functions, escalation triggers, blocking status, and preferred notification targets.

The setup approver map is a default baseline only; contract-specific approvers and routing must still be confirmed during intake and review.

### `.contract-review/memory-policy.yaml`

What may be persisted, what may never be persisted, retention rules, and whether counterparty memory is allowed.

This file should also reflect whether contract-specific artifacts should be reviewed for deletion or retention when the contract is closed.

### `CLAUDE.md`

A concise operational summary for Claude that mirrors:

- organization defaults
- approver map
- storage locations
- connector aliases
- memory restrictions
- sub-agent rules
- workflow action restrictions
- research and drafting preferences
- playbook ingestion preferences

Do not place large tables, raw contracts, or contract-specific confidential facts in `CLAUDE.md`.

## Update Rules

- Never overwrite existing setup silently if the user may care about the difference.
- Merge new answers into existing files.
- Preserve unchanged values.
- Record unknown values as `unknown`, not fabricated guesses.
- If the user gives a contract-specific override, save it in the contract folder, not the global config.
- Treat the saved approver map as a default baseline only. Confirm contract-specific approvers and overrides during intake when the contract requires them.

## What Not To Persist By Default

Do not save these unless the user explicitly authorizes it:

- Full contract text
- Personal data
- Privileged legal advice tied to a specific contract
- Opposing counsel tactics from a live contract
- Pricing or deal terms marked confidential for one-off use

## Required Security Disclosure

Before first upload, first connector use, or first remote MCP use in a workspace, deliver the notice described in [security-and-privacy.md](security-and-privacy.md).

## Claude And Codex Compatibility Rule

Both Claude and Codex should read `.contract-review/` first. Claude may additionally read `CLAUDE.md`. When updating persistent memory, update both when applicable so either tool can resume the workflow later.
