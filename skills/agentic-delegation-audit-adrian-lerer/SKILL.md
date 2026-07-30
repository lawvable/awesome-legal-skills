---
name: "lawve-agentic-delegation-audit-ignacio-adrian-lerer"
description: "Use when a lawyer, legal team, or client needs to assess AI agents that can act on someone's behalf: send messages, search, draft, file, pay, delete, connect to accounts, use tools, or rely on external data. Produces a practical delegation, oversight, accountability, and control audit for legal operations."
metadata:
  author: "Ignacio Adrián Lerer"
  license: "agpl-3.0"
  version: "2026-06-05"
---

# Lawve Agentic Delegation Audit

Use this skill to help lawyers evaluate whether an AI agent workflow is safe enough to use in legal or business operations.

Core idea:

```text
When AI only answers, the user evaluates an output.
When AI acts, the user delegates authority.
Delegated authority needs controls, logs, revocation, and accountability.
```

## Use When

- A client wants to use an AI agent for legal, compliance, business, or administrative work.
- A product, law firm, or legal ops team is connecting an agent to email, files, CRM, court portals, payments, messaging, calendars, databases, browser tools, or code execution.
- A lawyer needs to explain the risks of agentic AI in practical governance terms.
- A workflow may send, file, delete, approve, purchase, publish, sign, deploy, or change access.
- A system claims to be "autonomous", "agentic", "assistant with tools", "AI employee", "legal copilot", or "workflow agent".

## Do Not Use For

- Pure doctrinal legal research with no agentic action.
- Final legal opinions without jurisdiction-specific legal review.
- Technical implementation of an agent runtime.
- Approving production use of an agent without evidence, logs, and controls.

## Intake

Collect only what is necessary:

- What task does the agent perform?
- Who is the human principal?
- Who deploys or operates the agent?
- What systems, accounts, files, channels, or tools can it access?
- What actions can it take without step-by-step approval?
- Which actions are irreversible, external, financial, legal, confidential, or reputation-sensitive?
- What logs exist and who can read them?
- How can the user pause, revoke, appeal, or correct the agent?
- What data can influence the agent, including emails, webpages, chats, files, tickets, and prompts?

## Audit Steps

1. **Classify the autonomy level**
   - `answer_only`: produces information only.
   - `draft_only`: drafts but does not send or change records.
   - `approval_gated_actor`: acts only after explicit approval.
   - `policy_bounded_actor`: acts within predefined limits.
   - `long_running_actor`: continues across time, sessions, or triggers.

2. **Map delegated authority**
   - Name the principal.
   - Name the deployer/operator.
   - List what authority the agent has.
   - Separate read, draft, internal write, external write, financial, legal-sensitive, and privileged actions.

3. **Check observability**
   - Can the user see what the agent did?
   - Are tool calls and external actions logged?
   - Are logs understandable by a non-developer?
   - Are source data and model inference separated?

4. **Check control and revocation**
   - Can the user pause the agent?
   - Can permissions be narrowed?
   - Can access be revoked quickly?
   - Are irreversible actions previewed before execution?

5. **Check accountability**
   - Who is responsible if harm occurs?
   - Is responsibility split across vendor, deployer, user, professional, and client?
   - Is there a human review point before legal reliance or external action?

6. **Check attack surface**
   - Can untrusted content influence the agent?
   - Does the agent process emails, webpages, chats, documents, tickets, or social posts as instructions?
   - Are external content and system instructions separated?
   - Are prompt injection, data exfiltration, and tool misuse considered?

7. **Apply legal uncertainty gate**
   - Use `PASS`, `ESCALATE`, or `BLOCK` for downstream legal/business reliance.
   - Do not hide material uncertainty in disclaimer text.

## Output

Use this compact format:

```markdown
## Agentic Delegation Audit

### Verdict
PASS | NEEDS CONTROLS | BLOCK

### Why
[2-5 sentences]

### Delegated Authority
- Principal:
- Deployer/operator:
- Autonomy level:
- Systems/tools:
- Highest-risk action:

### Control Checklist
- Permission scope: adequate | weak | missing
- Human approval before external/legal/financial action: yes | partial | no
- User-readable logs: yes | partial | no
- Revocation/pause: yes | partial | no
- Prompt-injection/data-boundary controls: yes | partial | no
- Accountability owner: clear | partial | unclear

### Required Controls
- [control 1]
- [control 2]
- [control 3]

### Legal Reliance Gate
PASS | ESCALATE | BLOCK

### Next Step
[smallest practical next step]
```

## Decision Rules

- `PASS`: agent is draft-only or tightly approval-gated, logs are clear, permissions are scoped, and no material legal/client risk remains unmanaged.
- `NEEDS CONTROLS`: agent may be useful, but missing controls prevent safe operational reliance.
- `BLOCK`: agent can perform external, legal, financial, confidential, destructive, or privileged actions without adequate approval, logging, revocation, or accountability.

