# SAP & SAR Guide

The Security Assessment Plan (SAP) and Security Assessment Report (SAR) are prepared
by the Third-Party Assessment Organization (3PAO), not the CSP. However, CSPs are
responsible for reviewing and approving both documents before submission.

> SAP and SAR templates updated December 2024. Always use current templates.

---

## Security Assessment Plan (SAP)

The SAP defines the planned scope, methodology, and testing approach.

### Key SAP Sections

1. **System Overview** — Brief description of the CSO and authorization boundary
2. **Assessment Scope** — Which controls will be tested and why (based on Control Selection Worksheet)
3. **Assessment Team** — 3PAO lead assessor, team members, roles
4. **Assessment Methods** — Interview, examine, test (per NIST 800-53A)
5. **Test Case Procedures** — Detailed test steps for each in-scope control (uses FedRAMP test case workbook)
6. **Schedule** — Assessment timeline, including freeze date for CSO changes
7. **Reporting** — Expected SAR format and delivery timeline

### Control Selection Process (CSP + 3PAO Joint)
Controls selected for assessment are determined using the **Annual Assessment Controls Selection Worksheet**, which has four tabs:
- **Rev 5 List of Controls** — All controls in the applicable baseline
- **Conditional Controls** — Controls that apply based on specific implementations
- **CSP-Specific Controls** — Selected by CSP based on system changes and ConMon activities
- **Inherited Controls** — Controls inherited from leveraged FedRAMP systems

All new or modified Rev 5 requirements must be tested. Other controls are selected based on:
- System changes since last assessment
- Open POA&M items
- ConMon activities and anomalies
- Three-year periodicity requirement (no control can go untested for 3+ years)

### CSP Review Tips for the SAP
- Verify the boundary described matches the SSP
- Confirm control selection is complete — missing required controls will cause delays
- Ensure test methods are appropriate for your environment
- Review schedule and confirm CSO can be frozen during testing window
- Confirm all CSP staff interviews are scheduled (ISSOs, engineers, ops)

---

## Security Assessment Report (SAR)

The SAR documents what the 3PAO actually found during testing.

### Key SAR Sections

1. **Executive Summary** — Overall risk posture, total findings by risk level
2. **System Description** — Confirmed boundary and architecture
3. **Assessment Results** — Per-control test results (Pass / Fail / Other than Satisfied)
4. **Findings** — Detailed description of each identified weakness
5. **Risk Exposure Table** — Aggregated risk view (recommended for agency customer review)
6. **3PAO Recommendation** — Authorization recommended / not recommended

### SAR Appendices

| Appendix | Content |
|---|---|
| A | Infrastructure Scan Results |
| B | Security Requirements Traceability Matrix (SRTM) — required for Low, Moderate, High |
| C | Web Application Scan Results |
| D | Database Scan Results |
| E | Risk Exposure Table (RET) |
| F | Penetration Test Results (for High; recommended for Moderate) |

### CSP Review Tips for the SAR
- **Cross-reference every finding with your SSP** — If a finding says a control is not implemented but your SSP describes an implementation, challenge the finding with evidence
- **Review risk ratings** — If you believe a finding's risk level is too high given mitigating factors, discuss with 3PAO (supports a future DR/RA)
- **Verify inherited control findings** — Gaps attributed to inherited controls may actually be the IaaS/PaaS provider's responsibility
- **Debrief presentation** — CSP and 3PAO prepare and upload a SAR debrief for agency AO review before the debrief meeting
- **Every SAR finding → POA&M row** — Begin building POA&M while reviewing SAR

---

## 3PAO Selection Guidance

- 3PAOs must be recognized by FedRAMP — check the FedRAMP Marketplace
- **A2LA R311 restriction**: A 3PAO that provided advisory services (e.g., helped write the SSP) cannot perform the assessment for that same CSO for 2 years
- Select a 3PAO with experience at your impact level (High is more specialized)
- Request references from other CSPs at similar baseline levels
- Clarify roles in writing: what does the CSP provide vs. what does the 3PAO produce?
