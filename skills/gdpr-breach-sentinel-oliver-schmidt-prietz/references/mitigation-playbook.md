# Mitigation Playbook

After the risk assessment, generate a **tailored mitigation playbook** specific to the incident. Do NOT use a rigid template structure. Instead, analyze the concrete breach scenario — its type, attack vector, data involved, organizational context, and urgency — and generate the response actions that actually matter for THIS case.

## Playbook Design Principles

1. **Case-driven, not category-driven.** Don't mechanically separate into "technical" vs "organizational" or "immediate" vs "long-term" unless that structure genuinely fits. Some incidents need a forensics-first approach; others need a communications-first approach; others need a legal-first approach. Structure the playbook around what matters most.

2. **Prioritize by impact, not by convention.** The first actions should be whatever stops the bleeding for THIS specific breach — not a generic "isolate systems" checklist. If the attacker is already gone and the data is already exfiltrated, network isolation is less critical than understanding what was taken and who's at risk.

3. **Be specific.** Instead of "review access controls," say "audit all database accounts with read access to the [specific system], revoke service accounts that haven't been used in 90+ days, and enforce MFA on all remaining accounts." Tailor every action to the facts.

4. **Include the WHY.** For each action, briefly explain why it matters for this case. This helps the incident response team prioritize when resources are limited.

5. **Account for dependencies.** Some actions block others. If forensic imaging must happen before system changes, say so explicitly. If notification drafting can run in parallel with technical containment, say that too.

6. **Think about what the SA will ask.** Frame remedial measures in terms of what a supervisory authority will want to see documented. SAs frequently ask: "What did you do immediately? Why didn't you do X? What have you changed to prevent recurrence?"

## Playbook Output Format

Present the playbook as a prioritized, sequenced action plan with:
- **Action item** — specific, concrete, and tailored to the case
- **Rationale** — why this matters for this specific breach
- **Priority** (Critical / High / Medium)
- **Owner** (specific role, not just "IT")
- **Deadline** (relative to T0, realistic for the action)
- **Dependencies** (what must happen first, or what can run in parallel)
- **Status** field (Pending / In Progress / Complete)

Group actions in whatever structure best fits the case — this might be by workstream (Forensics / Legal / Communications / Hardening), by timeline, by system, or by stakeholder. Choose the structure that makes the playbook most actionable for the user's situation.

## Reference: Common Action Categories

Draw from these as relevant — but only include what applies to the specific case, and always customize:

**Containment & Forensics:** System isolation, credential revocation, evidence preservation, IOC sweeps, access log audits, attack vector analysis, lateral movement assessment

**Data & Impact Scoping:** Identifying exactly what data was compromised, mapping affected individuals, assessing downstream risks (identity theft, discrimination, blackmail, financial fraud)

**Legal & Regulatory:** SA notification preparation, subject notification drafting, law enforcement engagement, legal privilege considerations, DPA contractual obligation review, insurance notification

**Communication:** Internal stakeholder briefing, employee/works council communication, customer communication, media response preparation, support channel setup for affected individuals

**Hardening & Prevention:** Vulnerability remediation, encryption implementation, access control tightening, monitoring enhancement, detection rule creation, security architecture review

**Governance & Documentation:** Root cause analysis, DPIA review/update, Art. 30 records update, incident response procedure revision, training needs assessment, lessons learned documentation
