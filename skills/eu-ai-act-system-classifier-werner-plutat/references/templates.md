# Output Templates — Classification Deliverables

## Table of Contents

1. [Classification Memo](#1-classification-memo)
2. [Risk Register Entry](#2-risk-register-entry)
3. [Executive Summary](#3-executive-summary)
4. [Usage Notes](#4-usage-notes)

---

## 1. Classification Memo

Use this template for the formal legal/compliance assessment. This is the primary record.

```markdown
# AI Act Classification Memo

## System Information

| Field | Value |
|-------|-------|
| **System name** | [Name of the AI system] |
| **Version/Release** | [Version identifier] |
| **Provider** | [Legal entity name, country] |
| **Deployer** | [Legal entity name, country] |
| **Assessment date** | [YYYY-MM-DD] |
| **Assessor** | [Name, role] |
| **Review date** | [YYYY-MM-DD — recommended within 12 months or upon material change] |

## System Description

**Intended purpose:** [What the system is designed to do]

**Inputs:** [Data types and sources]

**Outputs:** [Decisions, recommendations, scores, content, etc.]

**Affected persons:** [Who is affected by the system's outputs — employees, customers, citizens, etc.]

**Deployment geography:** [Where the system operates and who it affects in the EU]

**GPAI model dependency:** [If applicable: model name, provider, version]

## Classification Decision Tree

### Step 1 — Scope
- [ ] System is placed on the EU market or put into service in the EU
- [ ] No exclusion applies (military, national security, pure research)
- **Role determination:** Provider / Deployer / Importer / Distributor

**Finding:** [In scope / Out of scope — with reasoning]

### Step 2 — Prohibited Practices (Article 5)
For each Article 5 category, document the assessment:

| Category | Applicable? | Reasoning |
|----------|------------|-----------|
| Manipulation/deception | Yes / No | [Brief reasoning] |
| Exploitation of vulnerabilities | Yes / No | [Brief reasoning] |
| Social scoring | Yes / No | [Brief reasoning] |
| Individual predictive policing | Yes / No | [Brief reasoning] |
| Untargeted facial image scraping | Yes / No | [Brief reasoning] |
| Emotion recognition workplace/education | Yes / No | [Brief reasoning] |
| Biometric categorisation (sensitive) | Yes / No | [Brief reasoning] |
| Real-time remote biometric ID (law enforcement) | Yes / No | [Brief reasoning] |

**Finding:** [Not prohibited / Prohibited under Article 5(1)(x) — stop if prohibited]

### Step 3 — High-Risk Assessment

**Annex I (regulated product):**
- Product regime: [MDR / Machinery / Aviation / N/A]
- Safety component: [Yes / No]
- Third-party conformity assessment: [Yes / No]

**Annex III (use case):**
- Matching category: [Category number and name, or N/A]
- Decision impact: [How the AI influences decisions in the identified domain]

**Article 6(3) exception claimed:** [Yes / No]
- If yes: [Detailed reasoning why the exception applies]

**Finding:** [High-risk (Annex I/III, category X) / Not high-risk]

### Step 4 — GPAI Assessment
- GPAI model used: [Yes / No]
- Model: [Name, provider]
- Systemic risk classification: [Yes / No / Unknown]
- Article 53 documentation available: [Yes / No / Partial]

**Finding:** [GPAI obligations apply / Do not apply]

### Step 5 — Limited Risk (Article 50)
- AI interaction requiring disclosure: [Yes / No]
- Deepfake/synthetic content: [Yes / No]
- Emotion recognition: [Yes / No]
- Biometric categorisation: [Yes / No]

**Finding:** [Article 50 transparency obligations apply / Do not apply]

### Step 6 — Final Classification

| Classification | Result |
|---------------|--------|
| **Risk level** | [Prohibited / High-Risk / Limited Risk / Minimal Risk] |
| **Article basis** | [Specific articles and annexes] |
| **GPAI overlay** | [Yes — Articles 51–56 / No] |
| **Role** | [Provider / Deployer / Importer / Distributor] |

## Key Obligations

[List the specific obligations that apply based on the classification and role. Reference the obligations matrix.]

## Compliance Deadline

[Applicable deadline based on the current-law timeline — e.g., "2 August 2026 for Annex III high-risk systems". If the user is planning long-horizon work, also note the 7 May 2026 provisional Digital Omnibus agreement that would shift Annex III to 2 December 2027 if formally adopted, while making clear the agreement is not yet binding law.]

## Assumptions and Gaps

[Document any assumptions made due to incomplete information, and flag information gaps that need resolution]

## Recommendations

1. [Specific next steps]
2. [Outstanding items to resolve]
3. [Escalation needs]

## DACH-Specific Considerations

[If deployed in Germany/Austria/Switzerland, note applicable national requirements — works council, BaFin, BSI, etc.]

---

**Disclaimer:** This classification memo provides compliance workflow support and does not constitute legal advice. Classification should be reviewed by qualified legal counsel.
```

---

## 2. Risk Register Entry

Use this template for each AI system's entry in the organisation's AI risk register.

```markdown
## AI Risk Register Entry

| Field | Value |
|-------|-------|
| **Register ID** | [AI-YYYY-NNN] |
| **System name** | [Name] |
| **Provider** | [Entity] |
| **Business owner** | [Name, department] |
| **Compliance owner** | [Name, department] |
| **Classification** | [Prohibited / High-Risk / Limited / Minimal] |
| **Risk level** | [Prohibited / High-Risk (Annex I) / High-Risk (Annex III, Cat. X) / Limited / Minimal] |
| **GPAI dependency** | [Model name or N/A] |
| **Article basis** | [e.g., Annex III Cat. 4 (Employment)] |
| **Role** | [Provider / Deployer] |
| **Deployment geography** | [Countries] |
| **Affected persons** | [Employee / Customer / Citizen / Patient] |
| **Compliance deadline** | [Date] |
| **Status** | [Not started / In progress / Compliant / Non-compliant / Under review] |

### Key Obligations

| Obligation | Status | Owner | Due date | Evidence |
|-----------|--------|-------|----------|----------|
| [e.g., Risk management system] | [Status] | [Name] | [Date] | [Link/reference] |
| [e.g., Technical documentation] | [Status] | [Name] | [Date] | [Link/reference] |
| [e.g., Human oversight] | [Status] | [Name] | [Date] | [Link/reference] |
| [e.g., FRIA] | [Status] | [Name] | [Date] | [Link/reference] |
| [e.g., Works council agreement] | [Status] | [Name] | [Date] | [Link/reference] |

### Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| [e.g., Non-compliance fine] | [H/M/L] | [€ range] | [Action] |
| [e.g., Works council challenge] | [H/M/L] | [Deployment blocked] | [Action] |
| [e.g., Data quality issue] | [H/M/L] | [Accuracy degradation] | [Action] |

### Review History

| Date | Reviewer | Finding | Action |
|------|----------|---------|--------|
| [Date] | [Name] | [Finding] | [Action taken] |

### Next Review Date: [YYYY-MM-DD]
```

---

## 3. Executive Summary

Use this template for leadership communication. One page maximum.

```markdown
# AI Act Classification — Executive Summary

**System:** [Name]
**Date:** [YYYY-MM-DD]
**Prepared by:** [Name, role]

## Classification Result

**Risk level: [HIGH-RISK / LIMITED RISK / MINIMAL RISK]**
**Legal basis:** [e.g., Annex III, Category 4 — Employment]
**Our role:** [Provider / Deployer]

## What This Means

[2–3 sentences explaining the practical impact. E.g., "As the deployer of a high-risk AI system in the employment category, we must implement human oversight, conduct a fundamental rights impact assessment, and maintain operational logs. The compliance deadline is 2 August 2026 in current law. A 7 May 2026 provisional Digital Omnibus agreement would shift this to 2 December 2027 if formally adopted; not yet adopted, so plan against current law."]

## Key Obligations

| # | Obligation | Deadline | Effort estimate | Owner |
|---|-----------|----------|----------------|-------|
| 1 | [e.g., Human oversight procedures] | [Date] | [Days/weeks] | [Dept] |
| 2 | [e.g., FRIA completion] | [Date] | [Days/weeks] | [Dept] |
| 3 | [e.g., Works council agreement] | [Date] | [Days/weeks] | [Dept] |
| 4 | [e.g., Vendor compliance verification] | [Date] | [Days/weeks] | [Dept] |

## Penalty Exposure

**Maximum fine for non-compliance:** [€ amount or % turnover]

## DACH-Specific Requirements

[1–2 sentences on German/Austrian-specific obligations if applicable]

## Recommended Next Steps

1. [Action — with timeline]
2. [Action — with timeline]
3. [Action — with timeline]

## Decision Required

[If leadership approval is needed: clearly state what decision is being requested]

---

*This assessment provides compliance workflow support and does not constitute legal advice.*
```

---

## 4. Usage Notes

### When to Use Which Template

| Deliverable | Audience | When |
|------------|----------|------|
| **Classification Memo** | Legal, compliance, internal audit | Every classification — this is the formal record |
| **Risk Register Entry** | Compliance team, risk management | After classification — maintains the living register |
| **Executive Summary** | C-suite, board, business leadership | High-risk or prohibited findings requiring executive attention |

### Formatting Guidance

- Fill in all fields. Use "N/A" or "Not applicable" rather than leaving blanks.
- For assumptions, be explicit about what was assumed and what evidence would resolve the assumption.
- Date all assessments and set review dates (minimum annually, or upon material system changes).
- Link to supporting evidence (risk management files, technical documentation, test results) rather than duplicating content.

### Quality Checks Before Finalising

- [ ] Every Article citation verified against Regulation (EU) 2024/1689
- [ ] All eight Article 5 categories explicitly assessed (even if clearly N/A)
- [ ] GPAI assessment included even if no GPAI model is used
- [ ] DACH-specific considerations addressed if deployed in Germany/Austria/Switzerland
- [ ] Compliance deadline correctly identified per the timeline
- [ ] Assumptions and gaps clearly flagged
- [ ] Disclaimer included
