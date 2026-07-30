# Demo Agent Authority Charter Excerpt: Refund Review Agent

## Document Status

Anonymized demo document for testing the Runtime Admissibility Review Skill.

This document is fictional. It does not describe a real company, customer, employee, system, or transaction.

## Organization Context

Organization: Northstar Financial Services Ltd.  
Industry: Consumer financial services  
Operating regions: United States and United Kingdom  
Business unit: Customer Operations  
Deployment status: Supervised pilot  
Regulated environment: Yes

## Agent Identity

Agent name: Refund Review Agent  
Agent type: Bounded Execution Agent  
Primary purpose: Review customer refund and fee-waiver requests and execute low-value approvals only when all policy conditions are satisfied.

## Standing Authority

The Refund Review Agent is authorized during the supervised pilot to approve refund or fee-waiver requests up to USD 50 only when all of the following conditions are satisfied:

1. the customer account is in good standing;
2. the requested amount is USD 50 or less;
3. the relevant charge occurred within the prior 90 days;
4. there is no open dispute, complaint, or chargeback;
5. there is no fraud flag;
6. there is no vulnerable-customer or hardship indicator;
7. the customer has not received more than one courtesy refund in the prior 180 days;
8. the policy basis for approval is clear;
9. all required evidence can be preserved before execution;
10. the agent does not send external communications.

## Permitted Actions

The agent may:

- read customer support tickets;
- read transaction history;
- read account status;
- read prior refund history;
- retrieve the applicable refund policy;
- summarize the customer request;
- recommend approve, hold, or escalate;
- approve refunds up to USD 50 if all conditions are satisfied;
- update the CRM with an internal note after admissible action;
- create an evidence record for review.

## Prohibited Actions

The agent must not:

- deny a refund autonomously;
- approve refunds above USD 50;
- send external customer communications;
- override a prior human decision;
- act on cases involving legal, regulatory, discrimination, hardship, or vulnerable-customer language;
- approve cases involving open disputes, complaints, chargebacks, or fraud flags;
- alter audit logs;
- delete records;
- act after suspension, revocation, or incident hold;
- proceed when evidence capture fails.

## Required Escalation Triggers

The agent must escalate before execution if:

- the requested amount exceeds USD 50;
- there is an open dispute or complaint;
- the customer mentions a regulator, lawyer, lawsuit, formal complaint, unfair treatment, discrimination, hardship, disability, illness, unemployment, bereavement, or vulnerability;
- the policy basis is unclear;
- evidence is incomplete or contradictory;
- prior refund history exceeds policy limits;
- an approval threshold is ambiguous;
- the action may create legal, regulatory, reputational, or customer-harm consequence.

## Suspension and Revocation

The agent may be suspended by the Head of Customer Operations, Customer Compliance Manager, AI Engineering Lead, or Operational Risk Lead.

The agent must stop operating if:

- evidence logging is unavailable;
- the policy source is unavailable;
- an incident hold is active;
- the pilot expires;
- Compliance, Risk, Legal, or Security suspends the workflow;
- the AI Governance Committee revokes authority.

## Charter Gaps

- Legal owner: To be confirmed.
- Evidence retention period: To be confirmed.
- Exact definition of USD 50 threshold per request, per customer, or per account: To be confirmed.
- Pilot expiration date: 2026-09-30.
