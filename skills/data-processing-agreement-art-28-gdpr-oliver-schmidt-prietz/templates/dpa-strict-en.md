# DPA Template — Tier 2 (Strict): 2021/915 Incorporated by Reference — English

## What this template is

A wrapper that **incorporates the unmodified Standard Contractual Clauses adopted by Commission Implementing Decision (EU) 2021/915** as the data-protection substance of the agreement, and adds a minimal commercial overlay (Section IV) for matters the Commission text does not address (governing law, notices, signatures, optional liability cap).

The compliance presumption under Art. 28(7) GDPR attaches to the unmodified Commission text. This wrapper is structured so that the presumption is preserved.

## When to use this template

Use Tier 2 (Strict) for **maximum regulator-defensible posture**:
- Public-sector engagement (controller is a public authority)
- Highly regulated sector (financial services, health, critical infrastructure)
- Post-incident remediation where the paper trail showing safe-harbor instrument is part of the corrective response
- Counterparty has explicitly requested 2021/915
- Any situation where the compliance presumption matters more than the commercial flexibility lost

For ordinary commercial DPA work, use **Tier 1** (`dpa-commercial-en.md`) or **Tier 3 — Hybrid** (`dpa-hybrid-en.md`).

## How to use this template

1. Load `references/2021-915-commission-text-en.md` for the clause-by-clause practitioner guide and OJ links.
2. Confirm the official OJ-EN text is the binding version. The text is at: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021D0915
3. Walk the **Choices** section below and lock in the Option/value selections.
4. Populate Annexes I–IV from intake.
5. Populate Section IV (commercial overlay).
6. Sign and execute.

The Commission text is **not reproduced** in this wrapper. It is incorporated by reference per Clause 1.2 below. This is a deliberate architectural choice — see the reference file for the rationale.

---

# DATA PROCESSING AGREEMENT

This **Data Processing Agreement** (the "**DPA**") is entered into on `{{EFFECTIVE_DATE}}` between:

**`{{CONTROLLER_NAME}}`**, a `{{CONTROLLER_LEGAL_FORM}}` registered under the laws of `{{CONTROLLER_JURISDICTION}}` with registered seat at `{{CONTROLLER_ADDRESS}}` and registration number `{{CONTROLLER_REG_NO}}` (the "**Controller**")

— and —

**`{{PROCESSOR_NAME}}`**, a `{{PROCESSOR_LEGAL_FORM}}` registered under the laws of `{{PROCESSOR_JURISDICTION}}` with registered seat at `{{PROCESSOR_ADDRESS}}` and registration number `{{PROCESSOR_REG_NO}}` (the "**Processor**", together with the Controller, the "**Parties**" and each a "**Party**").

## Recitals

A. The Parties have entered into `{{MAIN_AGREEMENT_TITLE}}` dated `{{MAIN_AGREEMENT_DATE}}` (the "**Main Agreement**") under which the Processor provides certain services to the Controller (the "**Services**").

B. In the course of providing the Services, the Processor processes personal data on behalf of the Controller within the meaning of Article 4(8) GDPR.

C. The Parties have agreed to govern their data-protection relationship by way of the Standard Contractual Clauses between controllers and processors set out in the Annex to **Commission Implementing Decision (EU) 2021/915** of 4 June 2021 (OJ L 199, 7.6.2021, p. 18) (the "**SCC-Decision**" and the "**SCCs**" respectively).

D. This DPA incorporates the SCCs by reference and adds a Section IV commercial overlay for matters the SCCs do not address.

## SECTION 1 — INCORPORATION OF THE SCCs

### 1.1 Incorporation by reference

The Parties hereby agree to and adopt the SCCs as set out in the Annex to the SCC-Decision in their entirety and without modification. The SCCs (Sections I, II, III and Annexes I, II, III, IV thereto) are incorporated into and form an integral part of this DPA. In case of conflict between this Section 1 and the SCCs, the SCCs prevail per Clause 4 of the SCCs.

### 1.2 Reference text

The Parties acknowledge that the binding text of the SCCs is the text published in the Official Journal of the European Union at OJ L 199, 7.6.2021, p. 18, accessible via https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021D0915. All EU language versions are equally authentic. In case of doubt about the binding text, the OJ text governs.

### 1.3 Capacity in which the SCCs are concluded

The SCCs are concluded under Regulation (EU) 2016/679 (General Data Protection Regulation) only. The optional reference to Regulation (EU) 2018/1725 in Clause 1 of the SCCs is not adopted.

### 1.4 Choices made by the Parties

The Parties make the following choices in respect of the SCCs:

| Choice | Selection |
|---|---|
| Optional Docking Clause (Clause 5) | `{{ENABLED / NOT ENABLED — default: ENABLED}}` |
| Sub-processor authorisation regime (Clause 7.7) | `{{OPTION 1 (specific) / OPTION 2 (general) — default: OPTION 2}}` |
| Time period for sub-processor authorisation request / change notification | `{{30 days — default}}` |

## SECTION 2 — COMPLETED ANNEXES TO THE SCCs

The Annexes to the SCCs are completed as set out in **Schedule 1** (Annex I), **Schedule 2** (Annex II), **Schedule 3** (Annex III) and **Schedule 4** (Annex IV) of this DPA.

## SECTION 3 — INTERNATIONAL TRANSFERS (where applicable)

### 3.1 Acknowledgment

The Parties acknowledge that under Clause 1(f) of the SCCs, the SCCs do not by themselves cover transfers of personal data outside the EEA under Chapter V GDPR.

### 3.2 Transfer mechanism

`{{If transfers are in scope, complete Schedule 5 (International Transfers) and identify the mechanism: adequacy decision / Commission Implementing Decision (EU) 2021/914 SCCs / BCRs / derogation under Art. 49 GDPR. If no transfers, mark Schedule 5 "Not applicable" and delete Section 3 cross-references where they would be orphaned.}}`

## SECTION 4 — COMMERCIAL OVERLAY 💼

> 💼 *This Section 4 is permitted under Clause 2(b) of the SCCs. It addresses commercial matters the SCCs do not regulate. It is drafted so as not to contradict the SCCs. Modifications to this Section 4 by the Parties do not affect the compliance presumption attaching to the SCCs.*

### 4.1 Term

This DPA enters into force on the Effective Date and remains in force for the duration of the Services. It terminates automatically on termination of the Main Agreement, subject to provisions expressed to survive.

### 4.2 Termination for material breach

Either Party may terminate this DPA on thirty (30) days' written notice in case of material breach by the other Party of this DPA or of the SCCs that has not been cured within the notice period. Termination of this DPA on this basis entitles the terminating Party to terminate the corresponding portion of the Main Agreement on the same basis without penalty.

### 4.3 Liability allocation

`[ALT 1: controller-favorable]` Without prejudice to liability arising from breach of the SCCs, the Processor's aggregate liability for damages arising out of or in connection with this DPA, including breaches of applicable data-protection law and personal data breaches, shall be capped at an amount equal to two (2) times the fees paid or payable by the Controller under the Main Agreement in the twelve (12) months preceding the event giving rise to liability. This cap is in addition to (not in lieu of) the general liability cap under the Main Agreement and shall not apply to liability for (a) gross negligence or wilful misconduct, (b) breach of confidentiality, or (c) any liability that cannot be limited under applicable law.

`[ALT 2: processor-favorable]` The Parties' respective liability under this DPA is subject to the limitation and exclusion-of-liability provisions of the Main Agreement.

### 4.4 Cost allocation for assistance

`{{Routine assistance under Clauses 8 and 9 of the SCCs is included in the Service fees. Non-routine assistance (such as request volumes materially exceeding ordinary patterns or specialised data extractions) may be charged at the Processor's reasonable rates with the Controller's prior agreement.}}`

### 4.5 Notices

Notices under this DPA shall be given in writing to the addresses set out at the head of this DPA, or to such other address as a Party may notify to the other in writing. Notices shall be effective on receipt.

### 4.6 Amendments

Amendments to this DPA shall be in writing and signed by both Parties. Amendments to the incorporated SCCs are not permitted; only the Annexes may be updated as set out in Clause 2(a) of the SCCs.

### 4.7 Severability

If any provision of this Section 4 is held invalid or unenforceable, the remaining provisions shall continue in full force. Severability of any clause of the SCCs is governed by the SCCs themselves.

### 4.8 Governing law and jurisdiction

This DPA is governed by the law of `{{GOVERNING_LAW}}`. The courts of `{{VENUE}}` have exclusive jurisdiction.

### 4.9 Order of precedence

In case of conflict between this Section 4 and the SCCs (Sections I–III + Annexes I–IV), the SCCs prevail per Clause 4 of the SCCs. In case of conflict between this DPA (including the SCCs) and the Main Agreement on data-protection matters, this DPA prevails.

## Signatures

For the **Controller**:
Name: ___________________
Position: ___________________
Date: ___________________
Signature: ___________________

For the **Processor**:
Name: ___________________
Position: ___________________
Date: ___________________
Signature: ___________________

---

# Schedule 1 — Annex I to the SCCs (List of Parties)

| Role | Name | Address | Contact person | Signature and date |
|---|---|---|---|---|
| Controller | `{{CONTROLLER_NAME}}` | `{{CONTROLLER_ADDRESS}}` | `{{CONTROLLER_CONTACT}}` | (signed at end of DPA) |
| Processor | `{{PROCESSOR_NAME}}` | `{{PROCESSOR_ADDRESS}}` | `{{PROCESSOR_CONTACT}}` | (signed at end of DPA) |

# Schedule 2 — Annex II to the SCCs (Description of the Processing)

**Subject matter**: `{{SUBJECT_MATTER}}`

**Duration**: For the duration of the Services under the Main Agreement, plus any post-termination period required for return or deletion of personal data under Clause 10 of the SCCs.

**Nature of the processing**: `{{NATURE — e.g. collection, storage, hosting, organisation, structuring, retrieval, transmission, deletion}}`

**Purpose(s)**: `{{PURPOSE — controller's purpose; not the processor's commercial purpose}}`

**Categories of personal data**:
- `{{Identifiers (e.g. name, employee ID)}}`
- `{{Contact data (e.g. email, phone)}}`
- `{{Other categories as relevant}}`
- Special categories under Art. 9 GDPR: `{{yes / no — if yes, specify}}`
- Personal data relating to criminal convictions and offences under Art. 10 GDPR: `{{yes / no}}`

**Categories of data subjects**:
- `{{e.g. employees, customers, prospects, end users}}`

**Frequency of the processing**: `{{continuous / periodic / one-off}}`

**Retention**: `{{e.g. tied to main agreement, plus post-termination return/delete period}}`

# Schedule 3 — Annex III to the SCCs (Technical and Organisational Measures)

The Processor implements the following measures to ensure a level of security appropriate to the risk, in accordance with Art. 32 GDPR and Clause 7.4 of the SCCs.

## 1. Pseudonymisation and encryption (Art. 32(1)(a))
- **Encryption in transit**: TLS 1.2 or higher.
- **Encryption at rest**: AES-256 or equivalent; keys managed in a key-management service with rotation.
- **Pseudonymisation**: where compatible with the purpose, with key segregation.

## 2. Confidentiality, integrity, availability, resilience (Art. 32(1)(b))
- **Access control**: role-based, least-privilege, logged and reviewed.
- **Authentication**: multi-factor for systems processing personal data.
- **Network segmentation**: production segregated from development and test.
- **Change management**: documented process for changes affecting personal data.
- **Vulnerability management**: regular scanning and patching.
- **Monitoring**: 24/7 monitoring of availability and security events.
- **Incident response**: documented plan with defined roles.

## 3. Restoration (Art. 32(1)(c))
- **Backups**: encrypted, segregated, tested for restoration.
- **Retention**: not exceeding `{{30–90 days}}`.
- **Disaster recovery**: documented plan with defined RTO and RPO.

## 4. Regular testing (Art. 32(1)(d))
- **Penetration testing**: annually by qualified independent third parties.
- **Internal audits**: regular.
- **Certifications**: `{{e.g. ISO/IEC 27001, SOC 2 Type II, BSI C5 — list with certification body}}`.

## 5. Personnel measures
- **Confidentiality**: written confidentiality undertakings.
- **Training**: data-protection and security training on hire and at least annually.
- **Data protection contact**: `{{name and contact}}`.

## 6. Sub-processor oversight
- **Due diligence**: documented.
- **Contracts**: imposing data-protection obligations no less stringent than those in the SCCs.
- **Periodic review** of sub-processor compliance.

## 7. Sensitive data (Clause 7.5 SCCs) — only where applicable
`{{If Schedule 2 indicates Art. 9 / Art. 10 data, complete this section. Otherwise mark "Not applicable".}}`
- Mandatory pseudonymisation where technically feasible.
- Enhanced access controls (need-to-know with documented justification).
- Segregated processing environments.
- Enhanced logging and monitoring with extended log retention.
- Sub-processor flow-down requires equivalent enhanced measures.

## 8. Measures to assist the Controller (Clauses 8 and 9 SCCs)

### 8.1 Data subject rights (Clause 8 SCCs)
- Forwarding obligation: requests received directly from data subjects forwarded to Controller within `{{5}}` Business Days.
- Assistance with access, rectification, erasure, restriction, portability, objection: provided within `{{10}}` Business Days of Controller's request, or such shorter period as Controller's statutory deadlines reasonably require.

### 8.2 Personal data breach notification (Clause 9 SCCs)
- Processor notifies Controller of any personal data breach without undue delay and in any event within `{{48}}` hours of becoming aware.
- Initial notification includes the Art. 33(3) GDPR information set to the extent reasonably available; follow-up information provided as it becomes available.

### 8.3 DPIA / prior consultation (Art. 35–36 GDPR)
- Information necessary to support Controller's DPIA provided on request.

# Schedule 4 — Annex IV to the SCCs (List of Sub-processors)

`[Option A — populated]`

| # | Sub-processor (legal name) | Registered seat | Location of processing | Processing activity | Categories of data | Safeguards (if outside EEA) |
|---|---|---|---|---|---|---|
| 1 | `{{Sub-processor 1}}` | `{{Seat}}` | `{{Location}}` | `{{Activity}}` | `{{Data}}` | `{{Mechanism}}` |
| ... | | | | | | |

`[Option B — none at signing]`

The Processor confirms that no sub-processors are engaged at the date of this DPA. The Processor shall comply with Clause 7.7 of the SCCs (Option `{{1 / 2}}` as selected in Section 1.4) before engaging any sub-processor.

# Schedule 5 — International Transfers (only if applicable)

`{{If transfers are in scope, identify the recipient(s), country/ies, role, and Chapter V mechanism. Refer to Commission Implementing Decision (EU) 2021/914 (Module 2 or 3 as applicable), populate its Annexes I.A / I.B / I.C / II / III, and reference any TIA conducted under Clause 14 of those SCCs. If no transfers, mark "Not applicable".}}`

---

# Drafting Notes (delete before signature)

- Confirm Controller and Processor legal names, addresses, registration numbers, and signatories.
- Verify the binding OJ-EN text against `references/2021-915-commission-text-en.md` clause map and the actual OJ link before signing.
- Lock in Section 1.4 choices (docking, sub-processor option, time period).
- Populate Schedule 1 (Annex I), Schedule 2 (Annex II), Schedule 3 (Annex III), Schedule 4 (Annex IV).
- For sensitive data (Art. 9 / Art. 10): complete Schedule 3 Section 7.
- For international transfers: complete Schedule 5 and ensure 2021/914 SCCs are executed alongside.
- Choose `[ALT 1]` or `[ALT 2]` in Section 4.3 (liability) per perspective.
- Confirm governing law and venue in Section 4.8.

# Practitioner's note (for OneZero Legal client deliverables)

This template uses Commission Implementing Decision (EU) 2021/915 incorporated by reference, with the Annexes completed as Schedules to this DPA and a minimal commercial Section IV overlay. The compliance presumption under Art. 28(7) GDPR attaches to the unmodified SCCs.

The principal advantage of Tier 2 (Strict) is the safe-harbor effect — useful for engagements where the supervisory authority is likely to scrutinise. The trade-offs are commercial: Section 4 is deliberately thin, the Hierarchy clause (Clause 4 SCCs) silently disables conflicting main-agreement provisions, and there is no flexibility on Section II clauses.

For situations needing a stronger commercial Section III (term, termination for convenience, transition, sophisticated liability allocation), use Tier 3 (Hybrid) instead — same Section I + II safe-harbor benefit, with a negotiated Section III replacement under Clause 2(b) SCCs.
