# POA&M Guide

The Plan of Action & Milestones (POA&M) is SSP Appendix O. It documents all known
security weaknesses and the CSP's plan to remediate them. The POA&M is a living
document — updated monthly during continuous monitoring.

> Always use the official FedRAMP POA&M template.

---

## POA&M Row Fields (Required)

| Field | Description |
|---|---|
| POA&M Item ID | Unique identifier (e.g., V-001, F-001) |
| Controls | NIST 800-53 Rev 5 control ID(s) affected |
| Weakness Name | Brief name of the finding |
| Weakness Description | Detailed description of the gap or vulnerability |
| Point of Contact | Person/team responsible for remediation |
| Resources Required | Tools, budget, staff needed |
| Overall Remediation Plan | How the weakness will be fixed |
| Original Detection Date | When was this first identified? |
| Scheduled Completion Date | Target remediation date (must meet SLA) |
| Milestone Changes | Track date/description changes |
| Status | Open / Closed / Risk Adjusted / Vendor Dependency |
| Comments | Additional context |
| Auto-Approve | Flag for auto-closures by 3PAO |
| Deviation Request Approved | Yes/No — for DRs approved by AO |
| Risk Rating (Original) | Critical / High / Moderate / Low |
| Risk Adjustment | If risk-adjusted, new risk level and justification |
| False Positive | Yes/No |
| Operational Requirement | Yes/No (if deviation is operational necessity) |

---

## FedRAMP Remediation SLAs

| Risk Rating | Remediation Deadline (from identification) |
|---|---|
| Critical (where distinguished from High) | ≤ 30 calendar days — prioritize immediately |
| High | 30 calendar days |
| Moderate | 90 calendar days |
| Low | 180 calendar days |

Source: FedRAMP Continuous Monitoring Performance Management Guide. Missing SLAs is one of the most common ConMon findings. Track carefully.

---

## POA&M Item Types

### Standard Finding (F-)
- Identified by 3PAO during assessment or annual assessment
- Must be remediated within SLA

### Vendor Dependency (VD-)
- Remediation depends on a third-party (OS vendor, SaaS tool, IaaS provider)
- Must document: vendor name, tracking ID (CVE or vendor ticket), expected fix date
- 3PAO validates VDs during annual assessment
- AO must agree to accept the VD; CSP must have compensating controls

### Deviation Request (DR-)
Three subtypes:
1. **False Positive (FP)**: Finding is not actually a vulnerability — provide evidence
2. **Risk Adjustment (RA)**: Vulnerability exists but risk is lower due to mitigating factors — must quantify
3. **Operational Requirement (OR)**: Vulnerability cannot be fixed without breaking functionality — must document business justification and compensating controls

All DRs require agency AO approval before being marked as such in the POA&M.

---

## POA&M Writing Tips

1. **One finding, one row** — Do not bundle multiple vulnerabilities into a single POA&M item
2. **Be specific about CVEs** — For vulnerability scan findings, always include CVE IDs
3. **Milestone dates must be realistic** — Overpromising and missing milestones is a finding in itself
4. **Closed items need evidence** — When closing an item, document the evidence of remediation (scan result, configuration screenshot, date)
5. **Inventory sheet is required** — The POA&M template includes an inventory tab; keep it current
6. **Match to SAR findings** — Every finding in the SAR must appear in the POA&M; reviewers cross-reference these

---

## POA&M During Initial Authorization vs. ConMon

**Initial Authorization:**
- POA&M documents residual risks from the 3PAO assessment (SAR findings not remediated before ATO)
- Agency AO reviews and accepts residual risk as part of granting ATO
- Moderate/High risk items may block ATO if not remediated or deviation-approved

**Continuous Monitoring:**
- POA&M updated monthly
- Submitted to agency AO(s) monthly
- Open items must show active progress (milestone updates)
- Stale POA&M items (no updates, missed milestones) can trigger suspension of ATO
