---
name: runtime-admissibility-review
description: Determines whether a specific AI-agent action, output, recommendation, or proposed commitment remains admissible for execution or institutional reliance under current authority, delegated scope, evidence, facts, policy, risk, escalation, and revocation conditions. Use this Skill before an enterprise or regulated AI agent executes, updates records, triggers workflows, communicates externally, or before an institution relies on an agentic output in a way that creates consequence.
category: Compliance & Regulatory
tags:
  - AI governance
  - agentic AI
  - runtime governance
  - admissibility review
  - delegated authority
  - execution control
  - legal operations
  - compliance
  - risk management
  - evidence sufficiency
  - escalation
  - audit trail
  - regulated industries
  - AI deployment
  - delegation audit
  - agent authority charter
  - reliance admissibility
  - consequence review
  - institutional reliance
  - human review
---

# Runtime Admissibility Review

## Purpose

This Skill helps legal, compliance, risk, product, operations, audit, and AI governance teams determine whether a specific AI-agent action, output, recommendation, or proposed commitment remains admissible at runtime before execution or before institutional reliance.

The purpose is not to decide whether an AI system was generally approved for deployment.

The purpose is narrower and more operational:

Determine whether this agent may take this specific action, or whether the institution may rely on this specific agentic output, under these current facts, with this authority, this delegated scope, this evidence, these constraints, this escalation posture, and this revocation status.

The Skill produces a structured Runtime Admissibility Determination that can be reviewed by legal, compliance, risk, audit, technical, and business stakeholders.

## Core Principle

Static authorization is not enough for agentic AI.

An AI agent may have been approved for a workflow, and a delegated task may initially fit within the authority envelope, but a specific action or later institutional reliance can become inadmissible because conditions changed.

Examples:

- the authority source expired;
- the policy changed;
- the action is outside scope;
- the reliance context is broader than the original delegation;
- the evidence is incomplete;
- a risk flag appeared;
- the customer, employee, patient, citizen, or counterparty context changed;
- the action now creates legal, financial, operational, regulatory, contractual, customer, employee, patient, citizen, market, public-sector, or reputational consequence;
- a human approval is required but missing;
- a revocation or suspension event occurred;
- the agent cannot preserve the required evidence trail;
- the output moved from informational support to institutional commitment.

The runtime question is:

"Even if the agent was previously authorized, is this action or institutional reliance still admissible now?"

## Relationship to Agent Authority Charter and Agentic Delegation Audit

This Skill is downstream from the Agent Authority Charter and complementary to Agentic Delegation Audit.

The Agent Authority Charter defines the agent's authority envelope before deployment: what was delegated, by whom, within which limits, under which evidence duties, and with what escalation, suspension, or revocation controls.

Agentic Delegation Audit tests whether a concrete delegated task fits within that authority envelope.

Runtime Admissibility Review asks the next question: even if the agent was properly authorized and the delegated task appears to fit the authority envelope, do current facts, scope, authority, evidence, policy, risk, escalation, revocation, or reliance conditions still permit the action or institutional reliance now?

The dependency structure is:

Agent Authority Charter -> Agentic Delegation Audit -> Runtime Admissibility Review -> Institutional Reliance / Consequence

The Skill can work without an uploaded Agent Authority Charter or Delegation Audit if the user provides enough context. If either artifact is available, use it as a primary input.

## Key Distinction

Do not collapse authorization and admissibility.

Authorization asks:

"Was the agent granted authority to operate in this workflow?"

Delegation review asks:

"Does this concrete delegated task fit within the agent's authority envelope?"

Runtime admissibility asks:

"May the agent take this specific action, or may the institution rely on this specific output, right now?"

An action may be authorized in general but inadmissible in the current state. A generated output may be useful as information but inadmissible for institutional reliance or consequence.

## Execution and Reliance Boundary

Runtime admissibility may apply at two closely related points:

1. Before execution - when an AI agent is about to act, update a record, trigger a workflow, communicate externally, or create operational consequence.

2. Before reliance - when an institution is about to rely on an agentic output, recommendation, classification, analysis, or generated artifact in a way that affects a person, transaction, legal position, regulatory duty, business decision, or institutional consequence.

The Skill should not assume that prior authorization resolves either boundary. Authority before action and admissibility before reliance are complementary layers.

A properly authorized agent may still become inadmissible because facts changed, scope shifted, evidence became incomplete, authority was suspended, policy changed, risk conditions emerged, or the reliance context became more consequential than the original delegation allowed.

## When to Use This Skill

Use this Skill when the user asks to:

- review whether an AI agent may take a specific action;
- determine whether a proposed AI-agent action should proceed;
- evaluate an agent action before execution;
- evaluate whether an institution may rely on an agentic output, recommendation, analysis, classification, or generated artifact;
- check whether current facts still support action or reliance;
- decide whether an agent should escalate;
- assess whether evidence is sufficient for execution or reliance;
- determine whether human approval is required;
- review whether an agent may update a system of record;
- review whether an agent may send a communication;
- review whether an agent may approve, reject, escalate, block, refund, waive, flag, close, open, modify, route, or remediate a case;
- review whether an output has moved from informational support to institutional commitment;
- evaluate a runtime exception;
- determine whether a previously authorized action is still permissible;
- determine whether reliance conditions have changed after an output was generated;
- create an audit-ready pre-execution or pre-reliance determination.

Use this Skill even if the user phrases the request informally, such as:

- "Can the agent do this?"
- "Can we rely on this output?"
- "Should this action be allowed?"
- "Is this still okay to execute?"
- "Is this output safe to use?"
- "Does this need human approval?"
- "Should the agent escalate?"
- "Is the evidence enough?"
- "Can we let the agent update the record?"
- "Can this AI send the notice?"
- "Can this AI approve the refund?"
- "Can this AI close the case?"
- "Can the business use this recommendation?"
- "What should happen before execution?"
- "What should happen before we rely on this?"

## When Not to Use This Skill

Do not use this Skill to:

- provide legal advice or a legal opinion;
- approve production deployment of an AI system;
- replace legal, compliance, risk, privacy, security, audit, or regulator review;
- classify an AI system under a specific statute unless the user provides the relevant framework;
- create technical access-control code;
- perform cybersecurity testing;
- validate model performance;
- determine whether a vendor is generally acceptable;
- create a full enterprise AI policy;
- authorize an AI agent to act without institutional approval.

If the user asks for a final legal conclusion, state that the output is a governance drafting aid and must be reviewed by qualified counsel and the appropriate institutional authority.

## Definitions

### Agent

An AI-enabled system, workflow, tool, assistant, copilot, or autonomous or semi-autonomous software component that can read information, produce outputs, use tools, trigger workflows, update records, communicate, recommend actions, or execute actions.

### Proposed Action

The specific action, output, recommendation, proposed commitment, or reliance event under review at runtime.

Examples:

- approve a refund;
- deny a claim;
- update a customer record;
- send a notice;
- escalate a case;
- close a ticket;
- block a transaction;
- approve access;
- route an application;
- trigger remediation;
- generate a regulatory report;
- execute a workflow step.

### Standing Authority

The authority previously granted to the agent through a charter, policy, delegation matrix, pilot approval, system owner approval, contract, operating procedure, governance committee decision, or other institutional source.

### Runtime Admissibility

The determination that a specific proposed action may proceed at the time of execution, or that a specific agentic output may be relied on by the institution at the point of use, because current authority, delegated scope, facts, evidence, policy, risk, escalation, reliance, and revocation conditions permit it.

### Institutional Reliance

The institutional use of an agentic output, recommendation, classification, analysis, decision draft, or generated artifact in a way that affects a person, transaction, legal position, regulatory duty, business decision, record, workflow, customer, employee, patient, citizen, market, public-sector matter, contract, or institutional consequence.

### Reliance Context

The context in which the institution proposes to use, adopt, communicate, record, execute, or defend an agentic output. Reliance context may be informational, internal, advisory, operational, legal, regulatory, customer-facing, employee-facing, patient-facing, citizen-facing, contractual, financial, market-facing, or externally consequential.


### Current State

The facts and conditions at the time the action is proposed.

Current state may include:

- current user request;
- current case facts;
- current account status;
- current policy version;
- current jurisdiction;
- current risk flags;
- current evidence;
- current approvals;
- current system status;
- current revocation or suspension status;
- current incident status;
- current escalation history.

### Evidence Sufficiency

The degree to which the available evidence is complete, current, relevant, consistent, traceable, and preserved well enough to support the proposed action.

### Constraint

A rule, policy, threshold, condition, prohibition, escalation requirement, approval requirement, legal restriction, compliance obligation, technical control, or business limitation that governs whether the action may proceed.

### Escalation Trigger

A condition requiring the agent to stop, hold, route, or refer the matter to a human, team, governance process, or control owner before execution.

## Required Inputs

Collect as many of the following inputs as possible. If the user does not provide enough information, proceed with reasonable assumptions but mark missing items as "To be confirmed."

### 1. Proposed Action

- What action is the agent about to take?
- What system, record, workflow, case, customer, employee, patient, citizen, transaction, counterparty, or asset will be affected?
- Is the action internal only or externally visible?
- Is the action reversible?
- Does the action create legal, financial, operational, customer, employee, patient, citizen, market, public-sector, or reputational consequence?
- Is the action a recommendation, draft, internal update, external communication, approval, denial, escalation, block, remediation, payment, or other execution step?

### 2. Agent Identity

- Agent name
- Agent type
- Agent owner
- Business owner
- Technical owner
- Compliance owner
- Legal owner, if applicable
- Deployment environment
- Agent version or configuration
- Workflow or use case

Possible agent types include:

- Informational Assistant
- Decision Support Copilot
- Workflow Preparation Agent
- Bounded Execution Agent
- Consequential Execution Agent
- Observer / Governance Agent
- Escalation / Control Agent
- Remediation Agent

### 3. Authority Source

Identify the source of standing authority.

Possible sources include:

- Agent Authority Charter;
- delegation-of-authority matrix;
- internal policy;
- operating procedure;
- business owner approval;
- compliance approval;
- legal approval;
- risk approval;
- security approval;
- AI governance committee decision;
- board-approved policy;
- contract;
- regulator-approved pilot;
- system owner approval.

If the authority source is missing or unclear, mark the action as not admissible or requiring escalation, depending on severity.

### 4. Scope

Identify the scope of the agent's authority.

- workflow scope;
- action scope;
- system scope;
- data scope;
- user scope;
- customer or counterparty scope;
- jurisdictional scope;
- time or pilot scope;
- monetary or risk threshold;
- product or service scope;
- exclusion list.

### 5. Current Facts

Collect the facts that exist at the time of proposed execution.

Examples:

- request amount;
- customer status;
- employee status;
- account standing;
- transaction history;
- fraud flag;
- open dispute;
- complaint status;
- vulnerability indicator;
- regulatory language;
- prior approvals;
- prior denials;
- data completeness;
- policy version;
- incident status;
- system health;
- evidence availability.

### 6. Evidence Available

Identify the evidence supporting or constraining the action.

Examples:

- user request;
- source records;
- policy excerpt;
- authority charter;
- delegation matrix;
- approval record;
- transaction data;
- account status;
- support ticket;
- compliance flag;
- system log;
- audit log;
- model output;
- tool output;
- human review note;
- exception record;
- risk signal.

### 7. Human Approval Status

Identify:

- whether human approval is required;
- who must approve;
- whether approval has been obtained;
- whether approval is documented;
- whether approval is action-specific, case-specific, batch-specific, or time-bound;
- whether the approver had authority;
- whether approval is current or expired.

### 8. Escalation History

Identify whether:

- the case was previously escalated;
- a human reviewer already decided;
- the agent is attempting to override a human decision;
- the action involves a repeated exception;
- unresolved escalations remain open;
- a regulator, customer, employee, patient, citizen, or counterparty complaint is involved.

### 9. Revocation or Suspension Status

Determine whether:

- the agent is currently approved to operate;
- authority has expired;
- authority has been suspended;
- authority has been revoked;
- an incident triggered a hold;
- a policy source is unavailable;
- evidence logging is unavailable;
- a system control failed;
- a kill-switch condition is active.


### 10. Reliance / Consequence Context

Determine whether the institution will rely on the output, recommendation, analysis, classification, or action.

Identify:

- whether reliance is informational, internal, operational, external, legal, regulatory, financial, customer-facing, employee-facing, patient-facing, citizen-facing, contractual, market-facing, or public-sector;
- whether reliance creates consequence;
- whether the reliance context matches the original delegated scope;
- whether the output has moved from informational support to institutional commitment;
- whether the evidence is sufficient for reliance, not merely for generation;
- whether reliance requires legal, compliance, risk, business, technical, audit, regulator, or human review;
- whether the output should be qualified, escalated, refused, or withheld from execution.

## Runtime Admissibility Chain

Apply the following chain in order.

### Step 1 - Identify the Action Under Review

Describe the precise action the agent proposes to take.

Avoid vague descriptions.

Weak:

"The agent will handle the case."

Strong:

"The agent proposes to approve a USD 42 refund, update the CRM with the approval rationale, and mark the support ticket as resolved."

### Step 2 - Classify the Consequence Level

Classify the proposed action by consequence.

#### Consequence Level 0 - Informational

The agent only reads, summarizes, labels, or explains information. No record, workflow, decision, communication, or external reliance is created.

#### Consequence Level 1 - Preparatory

The agent drafts, recommends, queues, or structures an action for human review. The action does not execute without human approval.

#### Consequence Level 2 - Internal Reversible Action

The agent updates an internal record or workflow in a way that is low-risk, logged, and reversible.

#### Consequence Level 3 - Bounded Execution

The agent executes a bounded action inside an approved threshold and control environment.

#### Consequence Level 4 - Consequential Execution

The agent affects legal, financial, customer, employee, patient, citizen, market, regulatory, public-sector, contractual, external, or reputational interests.

#### Consequence Level 5 - Prohibited or Reserved Action

The action is prohibited for the agent or reserved to a human, legal, compliance, board, regulator, court, licensed professional, or other institutional authority.

### Step 3 - Verify Standing Authority

Determine whether the agent has standing authority for the workflow and action class.

Ask:

- Does the agent have a documented authority source?
- Does the authority source cover this workflow?
- Does the authority source cover this action type?
- Does the authority source cover this system?
- Does the authority source cover this jurisdiction?
- Does the authority source cover this value or risk threshold?
- Is the authority still effective?
- Has the authority expired, been suspended, or been revoked?

If no clear authority source exists, default to not admissible for execution actions.

### Step 4 - Perform Scope Check

Determine whether the action is inside the agent's approved scope.

Check:

- workflow scope;
- action scope;
- system scope;
- data scope;
- user or customer scope;
- monetary threshold;
- risk threshold;
- jurisdiction;
- time window;
- pilot boundary;
- prohibited-action list.

If the action is outside scope, classify it as not admissible or prohibited.

### Step 5 - Perform Current-State Check

Determine whether current facts still satisfy the conditions required for execution.

Check for changed or disqualifying conditions, including:

- new complaint;
- new dispute;
- fraud flag;
- security flag;
- vulnerable-party signal;
- protected-class or discrimination risk;
- legal or regulatory language;
- threshold exceedance;
- contradictory records;
- incomplete data;
- prior human denial;
- open escalation;
- incident hold;
- policy update;
- jurisdiction change;
- expired approval;
- failed control;
- unavailable evidence system.

If a disqualifying current-state condition exists, require escalation or deny admissibility.

### Step 6 - Perform Evidence Sufficiency Check

Assess whether the evidence is sufficient for the proposed action.

Evaluate evidence against these criteria:

- relevance;
- completeness;
- consistency;
- freshness;
- provenance;
- traceability;
- policy linkage;
- authority linkage;
- approval record;
- auditability;
- preservation status.

Evidence is insufficient if:

- material facts are missing;
- source records conflict;
- the policy basis is unclear;
- the authority source is missing;
- the required approval is missing;
- evidence cannot be preserved;
- the audit trail cannot identify who or what acted;
- the action would depend on unsupported inference;
- the record cannot survive legal, compliance, risk, audit, or regulator review.

### Step 7 - Perform Reliance / Consequence Check

Determine whether the institution will rely on the agentic output, recommendation, analysis, classification, or proposed action in a way that creates consequence.

Ask:

- Will the institution rely on the output, recommendation, or action?
- Will reliance create legal, financial, operational, regulatory, contractual, customer, employee, patient, citizen, market, public-sector, or reputational consequence?
- Is the reliance context the same as the original delegated scope?
- Has the output moved from informational support to institutional commitment?
- Is the evidence sufficient for reliance, not merely for generation?
- Does reliance require legal, compliance, risk, business, technical, audit, regulator, or human review?
- Should the output be qualified, escalated, refused, or withheld from execution?

If the proposed reliance is more consequential than the original authority, scope, evidence, or approval supports, require escalation, human approval, qualification, or a not-admissible determination.

### Step 8 - Perform Constraint Check

Identify all constraints that apply.

Constraints may include:

- policy conditions;
- approval thresholds;
- prohibited actions;
- escalation rules;
- regulatory restrictions;
- contract terms;
- data protection requirements;
- retention obligations;
- role-based access restrictions;
- customer protection rules;
- operational-risk controls;
- audit requirements;
- incident holds;
- geographic or product limits;
- pilot limits;
- reliance limitations.

If a constraint conflicts with the proposed action or reliance, the action or reliance is not admissible unless the constraint allows human approval or exception handling and that approval has been obtained.

### Step 9 - Perform Escalation Trigger Check

Determine whether any escalation trigger is active.

Common escalation triggers include:

- missing authority;
- ambiguous policy basis;
- conflicting instructions;
- customer harm risk;
- employee impact;
- patient or citizen impact;
- financial threshold exceeded;
- legal or regulatory consequence;
- external communication;
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
- prior human denial;
- open dispute;
- vulnerable-party signal;
- complaint language;
- regulatory inquiry;
- reliance beyond the original delegation;
- incident hold.

If an escalation trigger is active, the action may not proceed autonomously and the output should not be relied on for consequence without the required review.

### Step 10 - Perform Revocation and Kill-Switch Check

Determine whether the agent's authority or operating condition has been suspended, revoked, or placed on hold.

The action or reliance is not admissible if:

- authority has expired;
- authority was revoked;
- authority was suspended;
- pilot authorization expired;
- incident hold is active;
- evidence logging failed;
- policy source is unavailable;
- required control is unavailable;
- kill-switch condition is active;
- system owner has disabled the workflow;
- a regulator or internal authority has required suspension.

### Step 11 - Determine Runtime Admissibility

Choose one determination.

#### Admissible

The action or reliance is within authority, within delegated scope, supported by sufficient evidence, permitted under current conditions, and no escalation or revocation trigger is active.

#### Admissible with Controls

The action or reliance may proceed only if specific controls are applied, such as logging, evidence preservation, threshold confirmation, qualified reliance language, notice to reviewer, or post-action sampling.

#### Human Approval Required

The action or reliance may proceed only after a qualified human approver reviews and approves the action or reliance.

#### Hold Pending Evidence

The action or reliance may not proceed until specified missing evidence is obtained or conflicting records are resolved.

#### Escalate Before Execution or Reliance

The action or reliance must be routed to a specified human, team, control owner, legal, compliance, risk, fraud, security, audit, regulator, or governance process before execution or institutional use.

#### Not Admissible

The action or reliance may not proceed because authority, delegated scope, evidence, policy, approval, reliance, or current-state conditions are not satisfied.

#### Prohibited

The action is outside the agent's permitted authority or the reliance is outside the permitted institutional use and must not be executed or relied on by the agent or institution.

## Decision Rules

### Rule 1 - No Authority, No Execution

If the agent lacks a clear authority source for the proposed action, the action is not admissible for autonomous execution.

### Rule 2 - Authorization Is Not Admissibility

Do not treat prior deployment approval as permission to take every action inside the workflow.

### Rule 3 - Delegation Fit Is Not Runtime Clearance

Do not treat a task's initial fit within the authority envelope as proof that the current action or reliance remains admissible.

### Rule 4 - Current State Controls the Decision

If current facts differ from the conditions assumed in the standing authority, evaluate the current facts.

### Rule 5 - Evidence Failure Blocks Execution or Reliance

If the evidence required to justify and audit the action or reliance cannot be preserved, the action is not admissible for autonomous execution and the output is not admissible for institutional reliance.

### Rule 6 - Human Approval Must Be Specific Enough

Generic approval is insufficient for consequential actions or reliance unless the authority source clearly allows batch, role-based, or policy-bound approval.

### Rule 7 - Escalation Overrides Automation

If an escalation trigger is active, the agent must stop or route the matter as required.

### Rule 8 - Revocation Overrides Everything

If authority is suspended, revoked, expired, or subject to an incident hold, the action or reliance is not admissible.

### Rule 9 - Conservative Default

If the facts are incomplete, classify the action or reliance more restrictively.

### Rule 10 - Consequence Raises the Threshold

If the action or reliance affects legal, financial, customer, employee, patient, citizen, market, regulatory, contractual, public-sector, or external interests, require stronger authority, evidence, approval, and auditability.

### Rule 11 - Reliance Requires Its Own Review

An output that is acceptable for informational support may still be inadmissible for institutional reliance if the institution proposes to use it to create consequence.

### Rule 12 - Prohibited Means Prohibited

If the action or reliance is prohibited by the charter, policy, delegation matrix, or control environment, do not convert it into an admissible action through conditions. Escalate or deny admissibility.

## Required Output Format

When using this Skill, produce the following artifact.

# Runtime Admissibility Determination

## 1. Determination Metadata

- Determination title:
- Date:
- Status:
- Organization:
- Business unit:
- Agent name:
- Agent type:
- Workflow:
- Proposed action or reliance event:
- Prepared for:
- Prepared by:
- Review required by:

Status options:

- Draft
- Pending Evidence
- Pending Human Approval
- Pending Legal Review
- Pending Compliance Review
- Pending Risk Review
- Admissible
- Admissible with Controls
- Escalate Before Execution or Reliance
- Not Admissible
- Prohibited

## 2. Proposed Action or Reliance Under Review

Describe the action or reliance event precisely.

Include:

- action, output, recommendation, or reliance requested;
- system or workflow affected;
- record, case, transaction, customer, employee, patient, citizen, counterparty, or asset affected;
- whether the action or reliance is internal or external;
- whether the action is reversible;
- whether the output is being used for informational support or institutional commitment;
- expected consequence;
- time sensitivity.

## 3. Consequence Classification

Classify the action or reliance as:

- Consequence Level 0 - Informational
- Consequence Level 1 - Preparatory
- Consequence Level 2 - Internal Reversible Action
- Consequence Level 3 - Bounded Execution
- Consequence Level 4 - Consequential Execution
- Consequence Level 5 - Prohibited or Reserved Action

Explain why.

## 4. Standing Authority Review

| Authority Question | Finding | Evidence / Source | Gap |
|---|---|---|---|

Questions to answer:

- Is there a documented authority source?
- Does it cover this agent?
- Does it cover this workflow?
- Does it cover this action type?
- Does it cover this reliance context?
- Does it cover this system?
- Does it cover this jurisdiction?
- Does it cover this threshold?
- Is it current?
- Has it been suspended or revoked?

## 5. Scope Review

| Scope Dimension | In Scope? | Basis | Notes |
|---|---|---|---|

Scope dimensions:

- workflow;
- action type;
- reliance context;
- system;
- data;
- user or customer class;
- monetary threshold;
- risk threshold;
- jurisdiction;
- time or pilot boundary;
- prohibited-action list.

## 6. Current-State Review

| Current-State Factor | Finding | Effect on Admissibility |
|---|---|---|

Current-state factors may include:

- complaint status;
- dispute status;
- fraud flag;
- vulnerability indicator;
- legal or regulatory language;
- threshold status;
- data completeness;
- policy version;
- prior human decision;
- open escalation;
- incident status;
- system health;
- evidence logging status;
- reliance context.

## 7. Evidence Sufficiency Review

| Evidence Item | Available? | Current? | Consistent? | Preserved? | Notes |
|---|---|---|---|---|---|

Then provide an evidence sufficiency conclusion:

- Sufficient
- Sufficient with controls
- Insufficient pending specified evidence
- Insufficient and blocking

## 8. Reliance / Consequence Review

| Reliance Question | Finding | Effect on Admissibility |
|---|---|---|

Questions to answer:

- Will the institution rely on the output, recommendation, or action?
- Will reliance create legal, financial, operational, regulatory, contractual, customer, employee, patient, citizen, market, public-sector, or reputational consequence?
- Is the reliance context the same as the original delegated scope?
- Has the output moved from informational support to institutional commitment?
- Is the evidence sufficient for reliance, not merely for generation?
- Does reliance require legal, compliance, risk, business, technical, audit, regulator, or human review?
- Should the output be qualified, escalated, refused, or withheld from execution?

## 9. Constraint and Policy Check

| Constraint | Applies? | Satisfied? | Effect |
|---|---|---|---|

Include:

- policy conditions;
- approval thresholds;
- prohibited actions;
- escalation rules;
- data or privacy restrictions;
- audit requirements;
- operational controls;
- pilot limitations;
- reliance limitations;
- revocation or suspension conditions.

## 10. Escalation Trigger Review

| Trigger | Active? | Required Action | Escalation Recipient |
|---|---|---|---|

If any escalation trigger is active, state that autonomous execution is not admissible and institutional reliance is not admissible without the required review.

## 11. Human Approval Review

- Is human approval required?
- Required approver role:
- Has approval been obtained?
- Is approval documented?
- Is approval specific to this action or reliance?
- Is approval current?
- Is approval sufficient?
- Approval gap, if any:

## 12. Revocation, Suspension, and Kill-Switch Review

| Control Condition | Status | Effect |
|---|---|---|

Check:

- authority expiration;
- suspension status;
- revocation status;
- incident hold;
- policy-source availability;
- evidence-logging availability;
- system-control availability;
- kill-switch trigger;
- pilot status.

## 13. Runtime Admissibility Decision

Choose one:

- Admissible
- Admissible with Controls
- Human Approval Required
- Hold Pending Evidence
- Escalate Before Execution or Reliance
- Not Admissible
- Prohibited

Provide a concise rationale.

## 14. Required Controls Before Execution or Reliance

List any required controls before the action may proceed or the output may be relied on.

Examples:

- preserve evidence pack;
- obtain named human approval;
- confirm threshold;
- verify policy version;
- resolve contradictory record;
- qualify reliance language;
- block external communication;
- route to compliance;
- route to legal;
- route to fraud operations;
- route to audit;
- route to regulator or public-sector authority;
- create audit log;
- confirm revocation status;
- confirm system access boundaries.

## 15. Execution / Reliance Instruction

Choose one:

- Proceed
- Proceed only with specified controls
- Proceed only after human approval
- Hold pending evidence
- Escalate before execution or reliance
- Do not execute
- Do not rely
- Prohibited for agent execution or institutional reliance

## 16. Evidence Record to Preserve

List the evidence that must be preserved for audit and review.

Include:

- triggering request;
- agent identity;
- agent version or configuration;
- authority source;
- applicable policy;
- current-state facts;
- reliance context;
- evidence reviewed;
- constraints applied;
- escalation triggers checked;
- approval record;
- final determination;
- action taken or withheld;
- reliance accepted, qualified, or refused;
- timestamp;
- reviewer identity, if any;
- audit log location.

## 17. Missing Information

List all missing information as "To be confirmed."

## 18. Blockers

List any blockers preventing autonomous execution or institutional reliance.

If none are identified, state:

"No blockers were identified based on the information provided, but this does not constitute legal, compliance, risk, security, or institutional approval."

## 19. Recommended Review Owners

Recommend review owners as applicable:

- Legal
- Compliance
- Risk
- Security
- Privacy
- Internal Audit
- Business Owner
- Technical Owner
- AI Governance Committee
- Fraud Operations
- Customer Operations
- Human Resources
- Clinical Owner
- Public-Sector Authority
- Regulator
- Other

## 20. Human Review Notice

Add this notice at the end of every determination:

"This Runtime Admissibility Determination is a governance drafting aid. It does not constitute legal advice, regulatory approval, or final institutional authorization. The proposed action or reliance should be reviewed by the appropriate legal, compliance, risk, security, technical, business, audit, or regulatory authority before execution or institutional reliance where required."

## Quality Standards

The output must be:

- specific to the proposed action;
- grounded in the current facts provided;
- explicit about authority, scope, evidence, constraints, escalation, and revocation;
- conservative where facts are incomplete;
- operational enough for technical and workflow teams;
- clear enough for legal, compliance, risk, and audit review;
- free of unsupported legal conclusions;
- structured as a pre-execution governance artifact.

Avoid vague language such as:

- "The agent should act responsibly."
- "The agent should comply with laws."
- "The agent should escalate if risky."
- "The evidence seems fine."
- "The agent is probably allowed to do this."
- "This is low risk."

Replace vague language with specific findings:

- authority source identified or missing;
- action inside or outside scope;
- evidence sufficient or insufficient;
- escalation trigger active or inactive;
- approval obtained or missing;
- revocation status clear or unclear;
- decision admissible, conditional, held, escalated, not admissible, or prohibited.

## Conservative Default Rules

Apply these defaults unless the user provides contrary evidence.

### Missing Authority

If standing authority is missing, unclear, expired, suspended, or revoked, the action is not admissible for autonomous execution.

### Missing Evidence

If required evidence is missing or cannot be preserved, hold the action pending evidence.

### Conflicting Records

If material records conflict, escalate before execution.

### External Communication

If the agent proposes to communicate externally, require explicit authority and human approval unless the authority source specifically permits autonomous communication.

### Denial or Adverse Decision

If the agent proposes to deny, reject, terminate, suspend, discipline, block, report, or otherwise make an adverse decision affecting a person or organization, require human approval unless explicitly authorized.

### Regulated or Sensitive Context

If the action involves financial services, insurance, healthcare, employment, education, housing, public benefits, credit, law enforcement, immigration, children, vulnerable persons, protected characteristics, sensitive personal data, or regulated records, apply heightened scrutiny.

### Reliance Creates Consequence

If an output, recommendation, classification, or analysis will be relied on to affect a person, transaction, legal position, regulatory duty, customer, employee, patient, citizen, public-sector matter, contract, or business decision, review reliance admissibility separately from generation quality.

### Irreversible or Hard-to-Reverse Action

If the action is irreversible or difficult to reverse, require human approval or escalation.

### Human Override

If a human has already decided the matter, the agent may not override that decision unless the authority source explicitly permits it.

### Active Complaint or Dispute

If there is an active complaint, dispute, legal claim, regulator inquiry, fraud concern, or sensitive-party signal, require escalation.

### Control Failure

If policy access, evidence logging, audit logging, or required system controls fail, the action is not admissible for autonomous execution.

## Example User Request

"Please conduct a Runtime Admissibility Review for a refund agent that wants to approve a USD 42 refund. The agent has authority to approve refunds up to USD 50 when the customer is in good standing, there is no open dispute, no fraud flag, and the policy basis is clear. The customer has one prior refund in the last 180 days. The policy says more than one courtesy refund in 180 days requires human review. The agent can update the CRM note but cannot send customer communications."

## Example Response Outline

The assistant should produce a Runtime Admissibility Determination that:

- identifies the proposed action as approving a USD 42 refund and updating the CRM;
- classifies the refund approval as bounded execution or consequential execution depending on the user's facts;
- confirms that the amount is within the USD 50 threshold;
- identifies the prior-refund rule as a constraint;
- determines whether the customer already has more than one courtesy refund in 180 days;
- holds or escalates if the rule is ambiguous;
- prohibits external communication if not authorized;
- requires evidence of request, transaction, policy basis, account standing, dispute status, fraud status, prior refund history, and final determination;
- reviews whether the institution may rely on the refund recommendation or CRM update as institutional consequence;
- concludes with one of the allowed decisions: admissible, admissible with controls, human approval required, hold pending evidence, escalate before execution or reliance, not admissible, or prohibited.

## Final Response Behavior

When returning the determination, include:

1. The full Runtime Admissibility Determination.
2. A concise admissibility decision.
3. The reason the action or reliance may proceed, must be held, must be escalated, is not admissible, or is prohibited.
4. Missing information.
5. Required controls before execution or reliance.
6. Recommended review owners.

Do not overstate certainty. Do not state that an action is legally approved. Do not state that institutional reliance is legally approved. Do not state that an agent is institutionally authorized unless the user provides the authority source.
