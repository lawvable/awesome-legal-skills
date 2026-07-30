# Demo Delegation of Authority Matrix

## Document Status

Anonymized demo document for testing the Agent Authority Charter Builder Skill.

This document is fictional. It does not describe a real company, customer, employee, system, or transaction.

## Purpose

This matrix defines who may authorize actions related to customer refunds, fee waivers, and AI-agent-assisted customer operations workflows.

## Authority Matrix

| Action | Authorized Role | Threshold | Conditions | Notes |
|---|---|---:|---|---|
| Review customer refund request | Customer Operations Reviewer | Any amount | Internal use only | May review facts and policy basis |
| Recommend refund approval | Customer Operations Reviewer or approved AI workflow | Any amount | Recommendation only | Does not create payment approval |
| Approve courtesy refund | Customer Operations Reviewer | Up to USD 100 | Must satisfy policy | Human approval required above automated threshold |
| Approve automated refund | Approved AI workflow | Up to USD 50 | Must satisfy all low-value policy conditions | Pilot approval required |
| Approve refund above USD 100 | Customer Operations Manager | Up to USD 500 | Must document rationale | Requires human approval |
| Approve refund above USD 500 | Head of Customer Operations | No preset limit | Requires business rationale | Compliance review may be required |
| Deny refund request | Customer Operations Reviewer | Any amount | Must document rationale | Automated denial not permitted |
| Handle legal/regulatory complaint | Legal or Compliance | Any amount | Must be escalated | AI may summarize only |
| Handle suspected fraud | Fraud Operations | Any amount | Must be escalated | AI may not approve refund |
| Suspend AI agent authority | Head of Customer Operations, Compliance Manager, or AI Engineering Lead | N/A | Incident, audit failure, policy failure, or control concern | Immediate suspension permitted |
| Revoke AI agent authority | AI Governance Committee | N/A | Material incident, policy change, audit failure, or expired pilot | Requires documented decision |
| Approve production deployment | AI Governance Committee | N/A | Legal, Compliance, Risk, Security, and Business approval required | Pilot results must be reviewed |

## Delegation Notes

The proposed Refund Review Agent may only exercise automated approval authority if:

1. the AI Governance Committee approves the pilot;
2. the approved threshold is USD 50 or less;
3. the customer account is in good standing;
4. no dispute, fraud flag, vulnerable-customer signal, or legal/regulatory language is present;
5. the agent preserves the required evidence record;
6. the agent escalates all exceptions;
7. Compliance approves the operating controls;
8. Security approves system access;
9. Risk approves monitoring and incident handling.

## Open Delegation Issues

- The AI Governance Committee has not yet approved production deployment.
- The pilot approval date is not documented.
- The legal owner has not been assigned.
- The exact evidence-retention period is not documented.
- The USD 50 threshold has not been confirmed as per request, per account, per customer, or per month.
