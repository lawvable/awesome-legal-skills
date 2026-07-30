# Output Templates — GPAI Code of Practice Compliance

Ready-to-use templates for GPAI compliance assessments. Fill in the bracketed fields with assessment-specific information.

---

## Table of Contents

1. [Compliance Gap Assessment](#template-1-compliance-gap-assessment)
2. [GPAI Compliance Memo](#template-2-gpai-compliance-memo)
3. [Executive Summary](#template-3-executive-summary)

---

## Template 1: Compliance Gap Assessment

### Header

| Field | Value |
|-------|-------|
| Assessment date | [Date] |
| Assessor | [Name/role] |
| GPAI model | [Model name and version] |
| Provider | [Entity name] |
| Provider status | [Provider / Downstream provider / Deployer] |
| Systemic risk | [Yes / No / Under assessment] |
| Code of Practice signatory | [Yes / No / Pending] |

### Transparency Chapter (All GPAI Providers)

| Measure | Requirement | Current Status | Gap | Priority | Remediation Action | Target Date |
|---------|------------|----------------|-----|----------|-------------------|-------------|
| 1.1 | Model Documentation Form completed | [Compliant / Partial / Non-compliant] | [Description] | [Critical / High / Medium / Low] | [Action] | [Date] |
| 1.2 | Downstream provider info process | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| 1.3 | Documentation integrity & security | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| Art. 53(1)(d) | Training data summary published | [Status] | [Gap] | [Priority] | [Action] | [Date] |

### Copyright Chapter (All GPAI Providers)

| Measure | Requirement | Current Status | Gap | Priority | Remediation Action | Target Date |
|---------|------------|----------------|-----|----------|-------------------|-------------|
| 1.1 | Copyright policy documented | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| 1.2 | Lawful access controls | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| 1.3 | Rights reservation compliance | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| 1.4 | Record-keeping | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| 1.5 | Output safeguards | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| 1.6 | Terms of service | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| 1.7 | Complaints handling | [Status] | [Gap] | [Priority] | [Action] | [Date] |

### Safety & Security Chapter (Systemic Risk Only)

*Skip this section if the model does not have systemic risk.*

| Commitment | Requirement | Current Status | Gap | Priority | Remediation Action | Target Date |
|-----------|------------|----------------|-----|----------|-------------------|-------------|
| 1 | Safety & Security Framework | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| 2 | Systemic risk identification | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| 3 | Systemic risk analysis | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| 4 | Risk acceptance determination | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| 5 | Safety mitigations | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| 6 | Security mitigations | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| 7 | Model Reports | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| 8 | Responsibility allocation | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| 9 | Serious incident reporting | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| 10 | Additional documentation | [Status] | [Gap] | [Priority] | [Action] | [Date] |

### DACH-Specific (if applicable)

| Area | Requirement | Current Status | Gap | Priority | Remediation Action | Target Date |
|------|------------|----------------|-----|----------|-------------------|-------------|
| Works council | Co-determination assessment | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| BNetzA readiness | Engagement with market surveillance | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| BSI alignment | Cybersecurity framework mapping | [Status] | [Gap] | [Priority] | [Action] | [Date] |
| Sector-specific | [BaFin / other regulator] | [Status] | [Gap] | [Priority] | [Action] | [Date] |

### Summary

| Category | Total measures | Compliant | Partial | Non-compliant |
|----------|---------------|-----------|---------|---------------|
| Transparency | [N] | [N] | [N] | [N] |
| Copyright | [N] | [N] | [N] | [N] |
| Safety & Security | [N] | [N] | [N] | [N] |
| DACH-specific | [N] | [N] | [N] | [N] |
| **Total** | **[N]** | **[N]** | **[N]** | **[N]** |

### Recommended priority order:
1. [Highest priority gap — action and timeline]
2. [Second priority gap — action and timeline]
3. [Third priority gap — action and timeline]

---

## Template 2: GPAI Compliance Memo

### [CONFIDENTIAL — PRIVILEGED ASSESSMENT]

**Re:** GPAI Code of Practice Compliance Assessment — [Model Name]
**Date:** [Date]
**Prepared by:** [Name/role]
**Reviewed by:** [Name/role]

---

#### 1. Scope and Purpose

This memo documents the compliance assessment of [Model Name] against the obligations set out in Articles 51–56 of Regulation (EU) 2024/1689 (EU AI Act) and the GPAI Code of Practice (Final Version, July 2025).

**Disclaimer:** This assessment provides compliance workflow support and does not constitute legal advice. Classification outcomes should be reviewed by qualified legal counsel.

#### 2. Provider Determination

| Question | Finding |
|----------|---------|
| Entity | [Name] |
| Role | [Provider / Downstream modifier / Deployer] |
| Model developed or placed on market under own name? | [Yes / No] |
| Significant modification of existing model? | [Yes / No — with reasoning] |
| EU market placement? | [Yes / No — describe distribution] |
| **Conclusion: GPAI model provider?** | **[Yes / No]** |

#### 3. Open-Source Exemption

| Question | Finding |
|----------|---------|
| Free and open-source licence? | [Yes / No — licence name] |
| Weights publicly available? | [Yes / No] |
| Architecture info publicly available? | [Yes / No] |
| Systemic risk (negating exemption)? | [Yes / No] |
| **Exemption applies?** | **[Full exemption / Partial / None]** |

If partial exemption: Art. 53(1)(a)–(b) obligations waived; Art. 53(1)(c)–(d) remain.

#### 4. Systemic Risk Classification

| Question | Finding |
|----------|---------|
| Training compute | [Estimated FLOPs] |
| Exceeds 10^25 FLOP threshold? | [Yes / No / Unknown] |
| Commission designation? | [Yes / No / Pending] |
| **Systemic risk classification** | **[Yes / No]** |

#### 5. Applicable Obligations

Based on the above analysis:

| Obligation tier | Applicable? | Source |
|----------------|------------|--------|
| Transparency (Art. 53(1)(a)–(b)) | [Yes / No — exemption] | Annex XI, XII |
| Copyright (Art. 53(1)(c)) | [Yes] | DSM Directive |
| Training data summary (Art. 53(1)(d)) | [Yes] | GPAI Template |
| Systemic risk obligations (Art. 55) | [Yes / No] | Code Ch. 3 |

#### 6. Compliance Status

[Summarise gap assessment findings — compliant areas, key gaps, critical issues]

#### 7. Key Assumptions

[List any assumptions made due to incomplete information]

#### 8. Recommendations

1. [Priority recommendation with timeline]
2. [Second recommendation]
3. [Third recommendation]

#### 9. Next Steps

- [ ] [Action item with owner and deadline]
- [ ] [Action item with owner and deadline]
- [ ] [Action item with owner and deadline]

---

## Template 3: Executive Summary

### GPAI Compliance — Executive Summary

**Model:** [Name and version]
**Provider:** [Entity]
**Assessment date:** [Date]
**Overall status:** [🟢 Compliant / 🟡 Gaps identified / 🔴 Significant non-compliance]

---

#### Provider Status
[Entity] is a GPAI model provider under the EU AI Act. The model [does / does not] have systemic risk.

#### Applicable Obligations
- **Transparency:** [Applicable / Exempt (open-source)]
- **Copyright:** Applicable (no exemption)
- **Safety & Security:** [Applicable (systemic risk) / Not applicable]

#### Code of Practice Status
[Entity] [is / is not] a signatory to the GPAI Code of Practice. [Implications of choice.]

#### Key Findings

| Area | Status | Critical gaps |
|------|--------|--------------|
| Transparency | [🟢/🟡/🔴] | [Brief description or "None"] |
| Copyright | [🟢/🟡/🔴] | [Brief description or "None"] |
| Safety & Security | [🟢/🟡/🔴/N/A] | [Brief description or "None"] |
| DACH-specific | [🟢/🟡/🔴/N/A] | [Brief description or "None"] |

#### Enforcement Timeline
- **Now:** GPAI obligations in effect since 2 August 2025
- **2 August 2026:** AI Office enforcement actions begin (current law; unchanged in 7 May 2026 provisional Digital Omnibus agreement)
- **2 August 2027:** Legacy GPAI model compliance deadline (models placed on market before 2 Aug 2025)

#### Top 3 Recommended Actions

| # | Action | Owner | Deadline | Impact |
|---|--------|-------|----------|--------|
| 1 | [Action] | [Owner] | [Date] | [Why this matters] |
| 2 | [Action] | [Owner] | [Date] | [Why this matters] |
| 3 | [Action] | [Owner] | [Date] | [Why this matters] |

#### Risk Exposure
**Maximum potential fines:**
- Systemic risk violations: €15M or 3% global annual turnover
- General GPAI violations: €7.5M or 1% global annual turnover

**Practical risk:** Non-signatories face increased regulatory scrutiny. Adherence to Code of Practice is a relevant factor in fine determination.

---

*Templates based on Regulation (EU) 2024/1689 and GPAI Code of Practice (Final Version, July 2025). Not legal advice.*
