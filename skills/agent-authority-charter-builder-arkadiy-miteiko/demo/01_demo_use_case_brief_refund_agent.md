# Demo Use Case Brief: Refund and Fee-Waiver Agent

## Document Status

Anonymized demo document for testing the Agent Authority Charter Builder Skill.

This document is fictional. It does not describe a real company, customer, employee, system, or transaction.

## Organization Context

Organization: Northstar Financial Services Ltd.  
Industry: Consumer financial services  
Operating region: United States and United Kingdom  
Business unit: Customer Operations  
Deployment stage: Proposed supervised pilot  
Regulated environment: Yes  
Primary stakeholders: Customer Operations, Compliance, Legal, Risk, AI Engineering, Internal Audit

## Proposed Agent

Agent name: Refund Review Agent  
Agent type: Semi-autonomous workflow agent  
Primary purpose: Review customer refund and fee-waiver requests and prepare or execute bounded actions based on internal policy.

## Workflow Description

Customers submit refund or fee-waiver requests through customer support channels. The Refund Review Agent will review the customer’s request, retrieve relevant account and transaction information, compare the facts against the internal refund policy, and recommend whether the refund or fee waiver should be approved.

The business team proposes that the agent may automatically approve low-value refunds up to USD 50 where all required policy conditions are satisfied.

## Systems Access

The agent may access:

- customer support ticketing system;
- transaction history system;
- account status system;
- prior refund history;
- internal refund and fee-waiver policy;
- CRM notes field.

The agent may not access:

- credit decisioning systems;
- collections systems;
- legal case management systems;
- employee HR systems;
- production audit-log modification tools;
- customer communication sending tools.

## Proposed Capabilities

The agent may:

- read customer support tickets;
- read transaction history;
- read account status;
- read prior refund history;
- retrieve the applicable refund policy;
- summarize the customer request;
- classify the request type;
- recommend approve, escalate, or insufficient information;
- draft an internal rationale;
- update the CRM with an internal note;
- automatically approve refunds up to USD 50 when all policy conditions are satisfied.

## Proposed Restrictions

The agent must not:

- deny a refund autonomously;
- send external communications to customers;
- approve refunds above USD 50;
- override a prior human decision;
- alter audit logs;
- delete records;
- access unauthorized systems;
- continue operating after suspension or revocation;
- make decisions involving complaints with legal, regulatory, discrimination, hardship, or vulnerable-customer language;
- approve any case involving suspected fraud or an open dispute.

## Proposed Escalation Conditions

The agent must escalate when:

- the requested refund exceeds USD 50;
- the customer has an open dispute;
- the account has a fraud flag;
- the customer appears to be vulnerable or in hardship;
- the support ticket mentions regulator, lawyer, complaint, discrimination, unfair treatment, hardship, disability, illness, death, unemployment, or similar sensitive terms;
- the policy basis is unclear;
- the account status is inconsistent across systems;
- prior refund history suggests potential abuse;
- transaction data is incomplete;
- the agent cannot preserve required evidence;
- the case is novel or outside the defined policy examples.

## Ownership

Business owner: Head of Customer Operations  
Technical owner: AI Engineering Lead  
Compliance owner: Customer Compliance Manager  
Legal owner: To be confirmed  
Risk owner: Operational Risk Lead  
Internal audit owner: To be confirmed

## Current Approval Status

The business owner has approved exploration of a supervised pilot.

Compliance review is required before the pilot.

Legal review is required before any production deployment.

Risk review is required before the agent can approve refunds automatically.

Security review is required before the agent receives system access.

## Known Open Questions

- Has the formal delegation-of-authority policy been updated to permit automated approvals?
- Who may suspend the agent during an incident?
- Where will evidence packs be stored?
- What is the required retention period for agent decision records?
- Is automatic approval permitted in all operating regions?
- Does the USD 50 threshold apply per request, per customer, per month, or per account?
