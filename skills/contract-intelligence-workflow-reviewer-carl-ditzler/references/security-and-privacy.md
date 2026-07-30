# Security And Privacy

This file governs the default security posture for contract uploads, cloud-source connections, and MCP-backed workflows.

## Core Rule

These controls reduce risk. They do not eliminate it.

OpenAI warns that connectors and remote MCP servers can expose sensitive data to models, permit read access to sensitive systems, enable actions in external services, and create prompt-injection risk. Anthropic similarly warns that custom connectors can access and act in external systems, may change behavior without warning, and are not fully immune to malicious behavior. Treat these controls as safeguards, not guarantees.

## Required User Notice

Before first connector use, first remote MCP use, or first contract upload in a new workspace, provide a concise notice that says:

- connected sources may expose sensitive contract data to the model or provider
- remote MCP servers and connectors may read from or take action in external systems
- prompt injection and unexpected tool behavior remain possible
- approvals, narrow scopes, and trusted connectors reduce risk but are not foolproof
- the skill will default to narrow file or folder scope, no local contract copies, conservative retention, and `suggest-only` outbound connector actions unless the user chooses otherwise

## Default Safe Settings

Use these defaults unless the user explicitly chooses otherwise:

- Approve only the minimum specific files or folders needed for the contract workflow
- Do not approve an entire drive, site, workspace, or repository when a narrower scope is possible
- Keep `write_local_contract_copies` off
- Keep outbound connector actions and notifications as `suggest-only` until the user explicitly approves stronger automation
- Treat custom or remote MCP servers as disallowed unless the user confirms they are trusted and reviewed
- Keep contract retention conservative and review saved artifacts at the end of the contract workflow
- Prefer enterprise or admin-managed connector policies when available

## Connector Scope Rules

- Prefer file-level approval for controlling playbooks and active contracts.
- If file-level approval is not practical, prefer one approved folder over a whole drive or whole site.
- Record the exact approved scope in `.contract-review/connectors.yaml`.
- If the user asks for broad access, warn that broader scope increases accidental disclosure and prompt-injection risk.

## Outbound Action Rules

- Drafting and packet preparation may proceed locally.
- Sending, posting, ticket creation, or state-changing actions through connectors should default to `suggest-only` or `approval-required`.
- Only move a write-capable connector action beyond `suggest-only` when the user has explicitly approved the connector, the destination, and the action mode.

## Retention And Cleanup Rules

- Do not persist full contract text by default.
- Keep saved artifacts limited to what is operationally necessary.
- When a contract is complete, remind the user to review whether local artifacts, cached derivatives, and connector authorizations should be retained or removed.
- If the user has requested conservative handling, recommend deleting contract-specific artifacts after the workflow is closed.

## Cross-Platform Rule

These settings are supported for both Codex and Claude because they are enforced through the skill workflow, saved configuration, and human approval gates rather than hidden product-specific memory.
