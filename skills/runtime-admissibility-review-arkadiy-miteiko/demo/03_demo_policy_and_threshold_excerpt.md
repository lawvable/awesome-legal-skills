# Demo Policy and Threshold Excerpt

## Document Status

Anonymized demo document for testing the Runtime Admissibility Review Skill.

This document is fictional. It does not describe a real company, customer, employee, system, or transaction.

## Policy Title

Customer Refund and Fee-Waiver Policy  
Version: 3.2-demo  
Effective date: 2026-01-15  
Policy owner: Customer Operations  
Compliance reviewer: Customer Compliance Manager

## Low-Value Automated Approval Rule

A supervised AI workflow may approve a refund or fee waiver up to USD 50 only when every condition below is satisfied:

1. the customer account is in good standing;
2. the charge occurred within the prior 90 days;
3. the customer has not received more than one courtesy refund in the prior 180 days;
4. there is no open fraud flag;
5. there is no open dispute, complaint, chargeback, legal claim, or regulator inquiry;
6. the support ticket does not contain legal, regulatory, discrimination, vulnerability, hardship, or threat-of-complaint language;
7. the policy basis is clear;
8. all required evidence can be preserved;
9. no prior human reviewer denied the same request;
10. the agent does not communicate externally.

## Human Review Required

Human review is required for:

- amounts above USD 50;
- repeated refund requests;
- any complaint involving legal or regulatory language;
- any customer statement threatening regulator contact, legal action, or public complaint;
- hardship or vulnerable-customer indicators;
- suspected fraud;
- open disputes or chargebacks;
- unclear or incomplete evidence;
- contradictory records;
- cases outside policy examples;
- any exception request.

## Prohibited Automated Outcomes

The AI workflow may not:

- deny a refund request;
- send external communications;
- approve refunds above USD 50;
- approve exceptions outside policy;
- resolve a case that requires escalation;
- override a human decision;
- delete records;
- alter audit logs;
- proceed when required evidence cannot be captured.

## Evidence Required Before Automated Approval

Before approving a low-value refund or fee waiver, the record must contain:

- customer request;
- transaction ID;
- amount requested;
- charge date;
- account standing;
- prior refund history;
- fraud status;
- dispute or complaint status;
- policy condition applied;
- agent identity and version;
- timestamp;
- final determination;
- audit-log reference.

## Threshold Note

The USD 50 automated approval threshold is currently defined per request.

Policy owner has not yet confirmed whether multiple same-day requests should be aggregated.
