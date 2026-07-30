---
name: "agent-authority-charter-builder-arkadiy-miteiko"
description: "Creates an Agent Authority Charter for enterprise or regulated AI agents before deployment. Use this Skill when a user needs to define what an AI agent is allowed to do, who delegated authority to it, what actions are permitted or prohibited, when human approval is required, what evidence must be preserved, and how the agent can be suspended, revoked, or escalated."
category: Compliance & Regulatory
tags:
  - AI governance
  - agentic AI
  - delegated authority
  - legal operations
  - compliance
  - risk management
  - audit trail
  - human review
  - regulated industries
  - AI deployment
metadata:
  author: "Arkadiy Miteiko"
  license: "agpl-3.0"
  version: "2026-06-20"
---

# Agent Authority Charter Builder

## Purpose

This Skill helps legal, compliance, risk, product, operations, and AI governance teams create an Agent Authority Charter before an AI agent is deployed into an enterprise or regulated workflow.

The purpose is not to decide whether an AI system is generally ethical, safe, or compliant. The purpose is narrower and more operational:

Define what institutional authority the agent has before it acts.

The Skill converts a proposed AI agent use case into a structured, reviewable governance artifact covering:

- agent identity;
- principal and delegation source;
- operational scope;
- permitted actions;
- prohibited actions;
- human approval rules;
- escalation triggers;
- evidence and audit requirements;
- suspension, revocation, and kill-switch conditions;
- deployment-readiness determination.

The final output should be suitable for review by legal, compliance, risk, security, business, audit, and technical stakeholders.

## Core Principle

An AI agent should not be governed only by what it can technically do.

It must be governed by what the institution has authorized it to do.

The charter must answer:

1. Who authorized the agent?
2. What is the agent allowed to do?
3. What is the agent forbidden from doing?
4. What conditions must be satisfied before action?
5. What human approvals are required?
6. What evidence must be preserved?
7. When must the agent stop and escalate?
8. Who can suspend, revoke, or amend the authority?
9. What happens if the agent exceeds scope?

## When to Use This Skill

Use this Skill when the user asks to:

- define the authority of an AI agent;
- prepare an AI agent for enterprise deployment;
- document agent permissions;
- create a governance artifact for an AI workflow;
- prepare for legal, compliance, risk, or audit review of an agent;
- distinguish between assistant, copilot, workflow automation, and agent authority;
- prepare a regulator-facing or internal AI pilot;
- define human approval, escalation, or kill-switch requirements;
- assess whether an agent should be permitted to take actions inside business systems;
- create an authority model for autonomous or semi-autonomous AI;
- review whether an AI agent can safely affect records, customers, transactions, workflows, or external commitments.

Use this Skill even if the user phrases the request informally, such as:

- “Can this agent approve things?”
- “What should we document before deploying this agent?”
- “Help me define what this AI is allowed to do.”
- “We need a governance charter for an internal agent.”
- “What permissions should this agent have?”
- “How do we make this agent safe for compliance review?”
- “What needs human approval?”
- “Where should we put escalation rules?”
- “Can this AI act on behalf of the company?”

## When Not to Use This Skill

Do not use this Skill to:

- provide legal advice or a legal opinion;
- approve an agent for deployment;
- classify an AI system under a specific statute unless the user provides the relevant legal framework;
- draft a full enterprise AI policy;
- perform cybersecurity testing;
- replace legal, compliance, risk, privacy, security, or regulator review;
- create technical access-control code;
- make final determinations about regulatory compliance;
- authorize an AI agent to operate.

If the user asks for legal conclusions, state that the output is a governance drafting aid and should be reviewed by qualified counsel and the appropriate institutional authority.

## Required Inputs

Collect as many of the following inputs as possible. If the user does not provide enough information, proceed with reasonable assumptions but mark missing items as “To be confirmed.”

### 1. Organization Context

- Organization name
- Industry
- Jurisdiction or operating region
- Regulated or non-regulated environment
- Business unit
- Relevant internal policies
- Relevant control environment
- Relevant regulatory obligations, if known

### 2. Agent Identity

- Agent name
- Agent purpose
- Agent type
- Business owner
- Technical owner
- Compliance owner
- Legal owner, if applicable
- Deployment environment
- Systems accessed

Possible agent types include:

- Informational Assistant
- Decision Support Copilot
- Workflow Preparation Agent
- Bounded Execution Agent
- Consequential Execution Agent
- Observer / Governance Agent
- Escalation / Control Agent
- Remediation Agent

### 3. Principal and Delegated Authority

Identify who or what delegates authority to the agent.

Authority may come from:

- named executive owner;
- business process owner;
- legal department;
- compliance department;
- risk function;
- internal AI governance committee;
- board-approved policy;
- contract;
- regulator-approved pilot;
- system owner;
- workflow-specific operating procedure.

If the source of authority is unclear, mark the charter as not deployment-ready.

### 4. Operational Scope

Identify:

- business process or workflow;
- systems the agent may access;
- tools the agent may use;
- data the agent may read;
- data the agent may write, change, or modify;
- transactions or records the agent may affect;
- internal users the agent may serve;
- external parties the agent may interact with;
- geographic limits;
- customer, product, transaction, or risk limits;
- time limits or pilot limits.

### 5. Permitted Actions

Define what the agent may do:

- without human approval;
- only with human approval;
- only during a pilot;
- only below a threshold;
- only for a specific class of users, cases, customers, or transactions.

Examples of permitted actions:

- retrieve information;
- summarize documents;
- classify records;
- prepare recommendations;
- draft communications;
- update internal notes;
- initiate a workflow;
- approve low-risk cases within a threshold;
- reject incomplete submissions;
- escalate exceptions;
- notify a human reviewer;
- generate an evidence pack.

### 6. Prohibited Actions

Define what the agent may not do.

Examples of prohibited actions:

- bind the organization contractually;
- approve credit, insurance, hiring, benefits, medical, legal, financial, or disciplinary decisions without review;
- make external statements on behalf of the organization;
- override human decisions;
- alter audit logs;
- delete records;
- access unauthorized systems;
- create new authority for itself;
- act outside its defined workflow;
- continue operating after suspension or revocation;
- make decisions involving protected characteristics unless specifically authorized and legally reviewed;
- act where the policy basis is ambiguous.

### 7. Action Tiers

Classify each agent action into one of the following authority tiers.

#### Tier 0 — Observe Only

The agent may read, summarize, classify, or flag information. It may not alter records, trigger workflows, make decisions, communicate externally, or create business consequences.

#### Tier 1 — Prepare

The agent may draft, structure, recommend, or queue actions for human review. It may not execute the action without human approval.

#### Tier 2 — Execute Bounded Internal Action

The agent may perform low-risk internal actions within clearly defined thresholds. The action must be logged and reversible where possible.

#### Tier 3 — Execute Consequential Action with Human Approval

The agent may prepare or initiate consequential actions only after explicit human approval. The approval must be preserved as part of the evidence record.

#### Tier 4 — Prohibited or Reserved Authority

The agent may not perform these actions. They require human, legal, compliance, board, regulator, or other institutional authority.

## Drafting Workflow

Follow this process when creating the charter.

### Step 1 — Identify the Agent’s Institutional Role

Determine whether the agent is assisting a human or exercising delegated authority.

Ask:

- Is the agent producing information only?
- Is it changing records?
- Is it triggering workflows?
- Is it approving or rejecting something?
- Is it communicating externally?
- Is it creating legal, financial, operational, customer, employee, patient, citizen, market, or reputational consequence?

Classify the agent as:

- Informational Assistant
- Decision Support Copilot
- Workflow Preparation Agent
- Bounded Execution Agent
- Consequential Execution Agent
- Observer / Governance Agent
- Escalation / Control Agent

### Step 2 — Define the Delegation Chain

The charter should never say “the agent is authorized” without identifying who or what authorized it.

Document:

- principal delegating authority;
- source of delegation;
- approving body or person;
- effective date;
- expiration or review date;
- conditions of authority;
- unresolved authority gaps.

If authority is unclear, state:

“Not ready — authority source not established.”

### Step 3 — Separate Capability from Authority

The agent may be technically capable of many actions. Only some actions are institutionally authorized.

Create a table with three columns:

| Technical Capability | Authorized Use | Required Control |
|---|---|---|

Example:

| Technical Capability | Authorized Use | Required Control |
|---|---|---|
| Send email | Draft only, no autonomous send | Human approval required |
| Update CRM | Add internal note only | Log entry required |
| Approve refund | Up to approved threshold only | Evidence pack required |
| Deny claim | Not authorized unless specifically approved | Human decision required |

### Step 4 — Assign Authority Tiers

Classify each action into Tier 0 through Tier 4.

Use conservative classification when the facts are unclear.

Any action involving legal, financial, medical, employment, credit, insurance, public-sector, customer-harm, or external commitment consequence should default to Tier 3 or Tier 4 unless the user provides a specific approved threshold and authority source.

### Step 5 — Define Human Approval Rules

For each action requiring human approval, define:

- approver role;
- approval method;
- approval record;
- required rationale;
- timeout rule;
- fallback if approver is unavailable;
- whether approval applies to one action, one case, a batch, or a time-bound operating period.

### Step 6 — Define Escalation Logic

The charter must specify when the agent must stop and escalate.

Escalation triggers may include:

- missing authority;
- ambiguous policy basis;
- conflicting instructions;
- unusual transaction size;
- customer harm risk;
- legal or regulatory consequence;
- financial threshold exceeded;
- sensitive personal data;
- protected class or discrimination risk;
- evidence gap;
- model uncertainty;
- tool failure;
- contradictory records;
- suspected fraud;
- security concern;
- request to override a control;
- repeated failed attempts;
- novel fact pattern;
- external commitment risk;
- pending litigation or complaint;
- regulator inquiry;
- adverse customer outcome.

Write escalation rules in operational language.

Good example:

“The agent must escalate if the requested refund exceeds the approved threshold, if the customer account has an open dispute, or if the agent cannot identify a policy basis for the action.”

Weak example:

“The agent should escalate when the matter is risky.”

### Step 7 — Define Evidence Requirements

For each action tier, define minimum evidence.

Suggested baseline:

| Tier | Minimum Evidence |
|---|---|
| Tier 0 | Timestamp, request, source records, generated output |
| Tier 1 | Timestamp, request, source records, draft or recommendation, reviewer identity |
| Tier 2 | Timestamp, authority source, constraints applied, action taken, affected record, audit log |
| Tier 3 | Tier 2 evidence plus human approval, approval rationale, escalation history |
| Tier 4 | Prohibited action log, denial reason, escalation record |

Evidence should include:

- user request or triggering event;
- agent identity;
- agent version or configuration;
- authority source;
- policy or rule basis;
- input records reviewed;
- constraints applied;
- tools used;
- decision path;
- human approvals;
- escalation events;
- final action taken;
- timestamp;
- audit trail location;
- revocation status at time of action.

### Step 8 — Define Suspension, Revocation, and Kill-Switch Conditions

The charter must define when the agent’s authority must be suspended or revoked.

Examples:

- policy change;
- regulatory change;
- data source failure;
- model drift;
- tool malfunction;
- repeated erroneous actions;
- unauthorized access attempt;
- unresolved incident;
- audit failure;
- revoked owner approval;
- expired pilot authorization;
- unexplained behavior;
- evidence logging failure;
- escalation failure;
- material change in use case.

Define:

- who can suspend the agent;
- who can revoke authority;
- emergency stop conditions;
- post-incident review process;
- effect of revocation on pending actions;
- notification obligations;
- logging requirements;
- remediation responsibilities;
- reinstatement conditions.

### Step 9 — Determine Deployment Readiness

Choose one readiness status:

- Ready for limited internal testing
- Ready for supervised pilot
- Ready for production with controls
- Not ready — authority gaps remain
- Not ready — legal/compliance review required
- Not ready — prohibited use case

Use the conservative status when facts are incomplete.

## Required Output Format

When using this Skill, produce the following artifact.

# Agent Authority Charter

## 1. Charter Metadata

- Charter title:
- Version:
- Date:
- Status:
- Organization:
- Business unit:
- Jurisdiction:
- Industry:
- Prepared for:
- Prepared by:
- Review required by:

Status options:

- Draft
- Pending Legal Review
- Pending Compliance Review
- Pending Risk Review
- Pending Security Review
- Approved
- Suspended
- Revoked

## 2. Agent Identity

- Agent name:
- Agent type:
- Agent purpose:
- Business owner:
- Technical owner:
- Compliance owner:
- Legal owner:
- Deployment environment:
- Systems accessed:
- External parties affected, if any:

## 3. Authority Source

- Principal delegating authority:
- Source of delegation:
- Approval body:
- Effective date:
- Expiration or review date:
- Conditions of authority:
- Authority gaps or unresolved items:

## 4. Institutional Role Classification

Classify the agent as one of:

- Informational Assistant
- Decision Support Copilot
- Workflow Preparation Agent
- Bounded Execution Agent
- Consequential Execution Agent
- Observer / Governance Agent
- Escalation / Control Agent

Explain why.

## 5. Operational Scope

Describe the workflow in which the agent may operate.

Include:

- permitted workflow;
- permitted users;
- permitted data sources;
- permitted systems;
- permitted tools;
- geographic or jurisdictional limits;
- customer or transaction limits;
- temporal or pilot limits;
- exclusions.

## 6. Capability vs. Authority Matrix

| Technical Capability | Authorized Use | Required Control |
|---|---|---|

## 7. Permitted Actions

| Action | Authority Tier | Human Approval Required? | Conditions | Evidence Required |
|---|---:|---|---|---|

## 8. Prohibited Actions

| Prohibited Action | Reason | Required Escalation |
|---|---|---|

## 9. Human Approval Rules

Define:

- actions requiring approval;
- approver role;
- approval method;
- approval record;
- timeout rule;
- fallback if approver unavailable.

## 10. Escalation Triggers

| Trigger | Required Agent Behavior | Escalation Recipient | Evidence to Preserve |
|---|---|---|---|

## 11. Evidence and Audit Requirements

Define:

- minimum evidence for each action;
- audit trail requirements;
- storage location;
- retention period, if known;
- audit owner;
- required logs;
- evidence format;
- exception handling.

## 12. Suspension, Revocation, and Kill-Switch

Define:

- who may suspend the agent;
- who may revoke authority;
- emergency stop triggers;
- pending-action treatment;
- post-revocation review;
- notification obligations;
- remediation obligations;
- reinstatement conditions.

## 13. Residual Risk and Open Issues

| Issue | Risk Level | Owner | Required Resolution |
|---|---|---|---|

Risk levels:

- Low
- Medium
- High
- Deployment-blocking

## 14. Deployment Readiness Determination

Choose one:

- Ready for limited internal testing
- Ready for supervised pilot
- Ready for production with controls
- Not ready — authority gaps remain
- Not ready — legal/compliance review required
- Not ready — prohibited use case

Include a short rationale.

## 15. Authority Risk Summary

Provide a short summary of the main authority risks, including:

- unclear delegation;
- excessive scope;
- insufficient human approval;
- weak evidence trail;
- unclear escalation;
- missing kill-switch;
- legal or compliance review gaps;
- external consequence risk.

## 16. Missing Information

List all important missing information as “To be confirmed.”

## 17. Deployment Blockers

List any issues that prevent deployment.

If none are identified, state:

“No deployment blockers were identified based on the information provided, but this does not constitute legal, compliance, risk, or security approval.”

## 18. Recommended Review Owners

Recommend which stakeholders should review the charter:

- Legal
- Compliance
- Risk
- Security
- Privacy
- Internal Audit
- Business Owner
- Technical Owner
- AI Governance Committee
- Regulator
- Other

## 19. Human Review Notice

Add this notice at the end of every charter:

“This Agent Authority Charter is a governance drafting aid. It does not constitute legal advice, regulatory approval, or final institutional authorization. Deployment should be reviewed by the appropriate legal, compliance, risk, security, technical, and business authorities.”

## Quality Standards

The output must be:

- specific enough to guide deployment;
- clear enough for legal, compliance, and risk review;
- operational enough for technical teams;
- conservative where authority is unclear;
- explicit about delegation, scope, escalation, evidence, and revocation;
- free of unsupported legal conclusions;
- structured as a reusable governance artifact.

Avoid vague language such as:

- “The agent should act responsibly.”
- “The agent should comply with laws.”
- “The agent should be safe.”
- “The agent should escalate when needed.”
- “The agent should use good judgment.”

Replace vague language with specific authority, threshold, evidence, and escalation rules.

## Deployment-Readiness Rule

If the agent can create legal, financial, operational, customer, employee, patient, citizen, market, public-sector, or external consequence, and the user has not identified a clear authority source, mark the charter:

“Not ready — authority source not established.”

## Conservative Default Rule

If information is incomplete, choose the more restrictive authority tier.

If a proposed action could bind the organization, affect a person’s rights, change money movement, alter legal status, affect regulated records, or create external reliance, classify it as Tier 3 or Tier 4 unless the user provides a clear authority source and approved threshold.

## Final Response Behavior

When returning the charter, include:

1. The full Agent Authority Charter.
2. A short Authority Risk Summary.
3. A list of missing information.
4. A list of deployment blockers.
5. Recommended review owners.

Do not overstate certainty. Do not state that the agent is approved unless the user has provided an actual approval source.

## Example User Request

“We are deploying an AI agent to review customer refund requests. It can read support tickets, check order history, recommend a refund decision, and update the CRM. It should approve small refunds automatically but escalate larger ones.”

## Example Response Outline

The assistant should produce an Agent Authority Charter that:

- identifies the refund agent as a Bounded Execution Agent if automatic low-value refunds are permitted;
- classifies recommendations as Tier 1;
- classifies CRM updates as Tier 2;
- classifies automatic refunds as Tier 2 only if an approved threshold exists;
- classifies larger refunds as Tier 3;
- prohibits denial of complex or disputed claims without human review;
- requires escalation for open disputes, vulnerable customers, suspected fraud, unclear policy basis, or threshold exceedance;
- requires evidence of request, order history, policy basis, threshold, action taken, approval if any, and audit log;
- marks the charter not deployment-ready if the refund threshold or authority source is missing.
