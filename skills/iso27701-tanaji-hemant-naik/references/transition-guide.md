# ISO 27701:2019 → 2025 Transition Guide

Organizations certified under ISO 27701:2019 have until **October 2028** to transition
to the 2025 edition. This guide covers the key changes, gap analysis approach, and
the steps to a successful transition audit.

---

## Why the Standard Changed

ISO 27701:2019 was designed as an *extension* to ISO 27001:2013 and ISO 27002:2013.
When ISO 27001 and ISO 27002 were revised in 2022, ISO 27701 needed realignment.
Rather than publishing another extension, ISO decided to rebuild ISO 27701 as a
standalone Privacy Information Management System (PIMS) standard — removing the
mandatory ISO 27001 prerequisite and making privacy management accessible to
organizations that may not need or want a full ISMS.

---

## Structural Comparison

| Element | 2019 Edition | 2025 Edition |
|---------|-------------|-------------|
| Standard type | Extension of ISO 27001:2013 | Standalone PIMS standard |
| ISO 27001 prerequisite | Mandatory | Optional |
| HLS framework | Derived from ISO 27001 | Own Clauses 4–10 |
| Shared security guidance | Clause 6 — 90+ sub-clauses from ISO 27001/27002 | **Table A.3 — 29 rationalized controls** |
| Controller controls | Annex A (Clause 7) — 28 controls | **Table A.1 — 31 controls** |
| Processor controls | Annex B (Clause 8) — 16 controls | **Table A.2 — 18 controls** |
| Annex A purpose | Controller-specific controls | Privacy controls for PII controllers |
| Annex B purpose | Processor-specific controls | Implementation guidance (new) |
| Implementation guidance | Minimal inline | **Dedicated Annex B** |
| GDPR mapping | Annex D | Updated correspondence annex |
| Control ID format | Clause-based (7.x.x, 8.x.x) | Table-based (A.1.x.x, A.2.x.x, A.3.x) |
| Cloud/AI/IoT controls | Not explicitly covered | Added to 2025 control set |
| New controls | — | 3 additional controller; 2 additional processor |

---

## Control Mapping: 2019 → 2025

> **Note on 2019 control IDs:** ISO 27701:2019 used clause-based numbering (7.x.x for
> controllers, 8.x.x for processors). The IDs in the tables below reflect that scheme.
> For the authoritative, exhaustive control-by-control correspondence, consult
> **Annex F of ISO 27701:2025** directly — it contains the official mapping table
> between every 2019 and 2025 control.

### Shared Security Controls (Clause 6 → Table A.3)

In 2019, ISO 27701 incorporated all of ISO 27001/27002's control guidance into **Clause 6**,
resulting in 90+ sub-clauses covering security topics. Organizations needed an active ISO 27001
ISMS to satisfy these requirements.

In 2025, this was rationalized into **29 standalone controls in Table A.3**. These cover the
same security domains (access control, logging, cryptography, incident management, etc.) but
are now self-contained and implementable without ISO 27001.

**For organizations holding ISO 27001:2022:** Map your existing ISMS controls to A.3 in the
PIMS SoA — you are not implementing new controls, just cross-referencing existing evidence.

**For organizations without ISO 27001:** A.3 represents 29 controls that must now be
independently evidenced. This is the largest new gap for organizations transitioning
without an ISMS foundation.

### Controller Controls (Annex A → Table A.1)

| 2019 Reference | 2019 Control Name | 2025 Reference |
|---------------|-------------------|----------------|
| A.7.2.1 | Identify and document purpose | A.1.2.2 |
| A.7.2.2 | Identify lawful basis | A.1.2.3 |
| A.7.2.3 | Determine when and how consent is obtained | A.1.2.4 |
| A.7.2.4 | Obtain and record consent | A.1.2.5 |
| A.7.2.5 | Privacy impact assessment | A.1.2.6 |
| A.7.2.6 | Contracts with PII processors | A.1.2.7 |
| A.7.2.7 | Joint PII controller | A.1.2.8 |
| A.7.2.8 | Records related to processing PII | A.1.2.9 |
| A.7.3.1 | Determining information for PII principals | A.1.3.2, A.1.3.3 |
| A.7.3.2 | Providing information to PII principals | A.1.3.4 |
| A.7.3.3 | Mechanism to modify or withdraw consent | A.1.3.5 |
| A.7.3.4 | Mechanism to object to processing | A.1.3.6 |
| A.7.3.5 | Access, correction and erasure | A.1.3.7 |
| A.7.3.6 | Inform third parties | A.1.3.8 |
| A.7.3.7 | Providing copy of PII | A.1.3.9 |
| A.7.3.8 | Handling requests | A.1.3.10 |
| A.7.3.9 | Automated decision making | A.1.3.11 |
| A.7.4.1 | Limit collection | A.1.4.2 |
| A.7.4.2 | Limit processing | A.1.4.3 |
| A.7.4.3 | Accuracy and quality | A.1.4.4 |
| A.7.4.4 | PII minimization objectives | A.1.4.5 |
| A.7.4.5 | Temporary files | A.1.4.7 |
| A.7.5.1 | Basis for PII transfer | A.1.5.2 |
| A.7.5.2 | Countries for PII transfer | A.1.5.3 |
| A.7.5.3 | Records of transfer of PII | A.1.5.4 |
| A.7.5.4 | Records of PII disclosure to third parties | A.1.5.5 |
| A.7.5.5 | Notification of PII disclosure requests | → moved to A.2.5.5 (processor-focused) |
| — | New in 2025 | A.1.4.6 De-identification and Deletion |
| — | New in 2025 | A.1.4.8 Retention |
| — | New in 2025 | A.1.4.9 Disposal |
| — | New in 2025 | A.1.4.10 PII Transmission Controls |

### Processor Controls (Annex B → Table A.2)

| 2019 Reference | 2019 Control Name | 2025 Reference |
|---------------|-------------------|----------------|
| B.8.2.1 | Customer agreement | A.2.2.2 |
| B.8.2.2 | Organization's purposes | A.2.2.3 |
| B.8.2.3 | Marketing and advertising use | A.2.2.4 |
| B.8.2.4 | Infringing instruction | A.2.2.5 |
| B.8.2.5 | Customer obligations | A.2.2.6 |
| B.8.2.6 | Records of processing PII | A.2.2.7 |
| B.8.3.1 | Obligations to PII principals | A.2.3.2 |
| B.8.4.1 | Temporary files | A.2.4.2 |
| B.8.4.2 | Return, transfer or disposal | A.2.4.3 |
| B.8.5.1 | Basis for PII transfer | A.2.5.2 |
| B.8.5.2 | Countries for PII transfer | A.2.5.3 |
| B.8.5.3 | Records of PII disclosures | A.2.5.4 |
| B.8.5.4 | Notification of PII disclosure requests | A.2.5.5 |
| B.8.5.5 | Legally binding PII disclosures | A.2.5.6 |
| B.8.5.6 | Disclosure of subcontractors | A.2.5.7 |
| — | New in 2025 | A.2.4.4 PII Transmission Controls |
| — | New in 2025 | A.2.5.8 Engagement of a Subcontractor |
| — | New in 2025 | A.2.5.9 Change of Subcontractor |

### Security Controls (New: Table A.3)

The 2025 edition introduces **Table A.3** — 29 information security controls drawn
from ISO 27001/27002:2022 — which all organizations (controllers and processors) must
address in their SoA regardless of whether they hold ISO 27001 certification.

Organizations that already hold ISO 27001:2022 can reference their existing ISMS
controls as evidence for the A.3 requirements (the controls are aligned). Organizations
without ISO 27001 must demonstrate these controls independently.

---

## Gap Analysis for Transition

Run this gap analysis to identify what needs to change for the 2025 transition:

### Phase 1: Clause Structure Gap (Management System)

| Gap Area | 2019 Issue | 2025 Requirement |
|----------|-----------|-----------------|
| Own Clause 4–10 | Borrowed from ISO 27001 | PIMS must have own documented clause evidence |
| PIMS Scope (4.3) | May have been part of ISMS scope | Standalone PIMS scope document required |
| Privacy Policy (5.2) | May have been embedded in IS Policy | Dedicated privacy policy recommended |
| Privacy risk assessment (6.1) | Extension of ISMS risk process | PIMS must have documented privacy risk methodology |
| Standalone SoA (6.1) | Part of ISMS SoA | Standalone PIMS SoA required if not co-located |
| Internal audit (9.2) | May have been part of ISMS audit | PIMS audit scope must be explicitly defined |
| Management review (9.3) | Part of ISMS management review | PIMS review inputs/outputs must be explicit |

### Phase 2: Controller Control Gaps (A.1 vs 2019 Annex A)

New controls in A.1 not in 2019 Annex A:
- **A.1.4.6 De-identification and Deletion** — Is there a documented de-identification and deletion process?
- **A.1.4.8 Retention** — Are retention schedules defined per data category?
- **A.1.4.9 Disposal** — Is secure disposal documented and enforced?
- **A.1.4.10 PII Transmission Controls** — Are controls on PII transmission documented?

### Phase 3: Processor Control Gaps (A.2 vs 2019 Annex B)

New controls in A.2 not in 2019 Annex B:
- **A.2.4.4 PII Transmission Controls** — Transmission controls at processor level
- **A.2.5.8 Engagement of a Subcontractor** — Is there a formal authorization process for new sub-processors?
- **A.2.5.9 Change of Subcontractor** — Is the controller notified in advance of sub-processor changes?

### Phase 4: Security Control Gap (Clause 6 → A.3)

The 2019 Clause 6 contained 90+ sub-clauses drawing from ISO 27001/27002. These are now
rationalized into 29 discrete controls in Table A.3. This is a restructuring, not wholesale
new requirements — but organizations must now address A.3 explicitly in their PIMS SoA.

If the organization **holds ISO 27001:2022**:
- Map existing ISMS controls to the corresponding A.3 controls
- Document the mapping in the PIMS SoA (e.g., "A.3.25 Logging — fully implemented via
  ISMS control A.8.15/A.8.16; see evidence reference [SIEM-001]")
- No new implementation work should be required for existing ISMS holders

If the organization does **not** hold ISO 27001:2022:
- Review all 29 A.3 controls against current security practices
- Any gaps must be implemented and evidenced independently
- This is the single largest new work area for non-ISMS organizations

---

## Transition Audit Steps

Certification bodies will typically require:

1. **Gap analysis** against 2025 requirements (documented)
2. **Updated PIMS documentation**:
   - Revised PIMS Scope
   - Updated or new standalone Privacy Policy
   - Revised privacy risk assessment to include new controls
   - New standalone PIMS Statement of Applicability (including A.3)
   - Updated Records of Processing Activities
3. **Evidence of new controls**:
   - Retention schedules and enforcement (A.1.4.8–A.1.4.9)
   - Sub-processor authorization and notification process (A.2.5.8–A.2.5.9)
   - A.3 security controls (if not ISO 27001 certified)
4. **Transition audit** — typically a focused assessment on the gap areas; full
   recertification not usually required if the gap is well-managed
5. **Updated SoA** reflecting 2025 control IDs (A.1.x, A.2.x, A.3.x)

---

## Recommended Transition Timeline (for October 2028 Deadline)

| Phase | Target | Actions |
|-------|--------|---------|
| Months 1–3 | Gap analysis complete | Run full 2019→2025 gap assessment; produce gap register |
| Months 3–6 | Documentation updated | Revise scope, policy, risk assessment, SoA |
| Months 6–12 | New controls implemented | Address A.1.4.6–A.1.4.10, A.2.5.8–A.2.5.9, A.3 controls |
| Month 12+ | Internal audit | Internal audit against 2025 requirements |
| Month 18–24 | Transition audit | Engage certification body for transition audit |
| Before October 2028 | Transition complete | New 2025 certificate issued |

> **Recommendation**: Do not wait until 2027 to begin. Certification bodies will
> face high demand as the deadline approaches.
