# Demo AI Agent Risk Review Notes

## Document Status

Anonymized demo document for testing the Agent Authority Charter Builder Skill.

This document is fictional. It does not describe a real company, customer, employee, system, or transaction.

## Review Context

The proposed Refund Review Agent is intended to reduce manual handling of routine refund and fee-waiver requests. The business case depends on allowing the agent to approve low-value refunds automatically during a supervised pilot.

The review team identified several authority, evidence, escalation, and operational-risk issues that must be addressed before deployment.

## Key Risks

### 1. Authority Ambiguity

The business team has proposed automated approval authority up to USD 50, but it is not yet clear whether the formal delegation-of-authority policy permits an AI workflow to exercise this authority.

Risk level: High  
Suggested owner: Legal and Compliance  
Potential blocker: Yes

### 2. Threshold Ambiguity

The USD 50 threshold is defined as a maximum refund amount, but the policy does not state whether the threshold applies per request, per account, per customer, per calendar month, or per incident.

Risk level: Medium  
Suggested owner: Customer Operations and Compliance  
Potential blocker: Yes for pilot; definitely for production

### 3. Escalation Reliability

The agent must escalate vulnerable-customer, fraud, dispute, legal, regulatory, hardship, and policy-ambiguity cases. The current design does not yet specify how those signals will be detected or tested.

Risk level: High  
Suggested owner: AI Engineering and Compliance  
Potential blocker: Yes

### 4. Evidence Storage

The use case requires a clear evidence pack for every automated approval. The storage location, retention period, audit owner, and review cadence have not yet been finalized.

Risk level: High  
Suggested owner: Internal Audit and Operational Risk  
Potential blocker: Yes

### 5. Human Override

The business team expects human reviewers to override or reverse automated approvals where needed. The current workflow does not yet define who may reverse the approval, how quickly, and how reversal should be documented.

Risk level: Medium  
Suggested owner: Customer Operations  
Potential blocker: No for limited testing; yes for production

### 6. Audit-Log Protection

The agent is not intended to alter audit logs, but system permissions have not yet been reviewed to confirm the agent lacks write access to audit-log systems.

Risk level: High  
Suggested owner: Security and AI Engineering  
Potential blocker: Yes

### 7. Customer Communications

The agent must not send external communications. The proposed design allows the agent to draft rationale notes, but there is a risk that future workflow integration could connect those drafts to outbound customer messaging.

Risk level: Medium  
Suggested owner: Product and Legal  
Potential blocker: No if outbound communication access is technically blocked

### 8. Policy Drift

The internal refund policy may change. The agent’s policy reference must be version-controlled, and the agent must stop operating if the policy source is unavailable or outdated.

Risk level: Medium  
Suggested owner: Compliance and AI Engineering  
Potential blocker: No for supervised pilot if monitoring exists

## Recommended Controls

- Limit the first pilot to internal users only.
- Require human review for all denials.
- Require human review for all refunds above USD 50.
- Block external communications.
- Block audit-log modification.
- Require evidence capture before automated approval.
- Suspend the agent if evidence logging fails.
- Suspend the agent if policy reference is unavailable.
- Review all automated approvals weekly during pilot.
- Conduct pre-deployment testing for escalation triggers.
- Assign legal owner before production deployment.
- Assign audit owner before pilot deployment.

## Initial Readiness View

Recommended status: Not ready — authority gaps remain.

Reason: The use case is plausible for a supervised pilot, but the delegation source, threshold interpretation, evidence-retention requirements, and escalation-testing method remain unresolved.
