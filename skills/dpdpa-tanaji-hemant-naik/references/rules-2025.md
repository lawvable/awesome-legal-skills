# DPDP Rules, 2025 — Rule-by-Rule Reference

Digital Personal Data Protection Rules, 2025. Notified: 13 November 2025.
Effective date: 13 May 2027 (18-month transition). 23 Rules total.

Published by the Ministry of Electronics and Information Technology (MeitY) under
Section 35 of the Digital Personal Data Protection Act, 2023.

---

## Overview: Rules Structure

| Chapter | Rules | Subject Matter |
|---------|-------|---------------|
| Chapter I | Rules 1–2 | Preliminary (title, definitions) |
| Chapter II | Rules 3–5 | Notice and consent |
| Chapter III | Rule 6 | Personal data breach notification |
| Chapter IV | Rule 7 | Security safeguards |
| Chapter V | Rules 8–9 | Data retention and erasure |
| Chapter VI | Rules 10–12 | Children's personal data |
| Chapter VII | Rules 13–15 | Significant Data Fiduciary obligations |
| Chapter VIII | Rules 16–18 | Data processing agreements |
| Chapter IX | Rules 19–21 | Data Protection Board procedure |
| Chapter X | Rules 22–23 | Miscellaneous |

---

## Rule 1 — Short Title and Commencement

**Rule 1(1):** These Rules are called the Digital Personal Data Protection Rules, 2025.

**Rule 1(2):** Coming into force on the date of publication in the Official Gazette (13 November 2025). Full compliance obligations under the Rules apply from 13 May 2027 (18-month transition, confirmed at commencement).

> **Practical note:** The 18-month transition period runs from 13 November 2025. During transition, organisations should treat the Rules as operative for planning and system design — implementing compliance programmes so they are ready by 13 May 2027. Delay risks are significant given system changes required (notice redesign, consent infrastructure, age-gate systems for children's data, breach notification pipelines).

---

## Rule 2 — Definitions

Incorporates definitions from the Act (Section 2) with supplementary procedural definitions:

| Term | Definition |
|------|-----------|
| **Consent record** | Documented evidence of valid consent including timestamp, mechanism, notice version presented, and the specific purpose consented to |
| **Data Auditor** | A qualified independent auditor registered with the Board for the purpose of conducting SDF data audits under Rule 14 |
| **Digital footprint** | The set of persistent identifiers, behavioural traces, and inferred attributes associated with a Data Principal arising from digital interactions |
| **Prescribed period** | The period specified in the relevant Rule or Schedule for fulfilling a specific obligation |

---

## Rule 3 — Notice to Data Principal

**Source authority:** Section 5 of the Act.

### Rule 3(1) — Content Requirements

The notice must contain all of the following:

1. **Identity and contact details** of the Data Fiduciary — full legal name, registered address, email or web contact
2. **Categories of personal data** sought to be collected — described in plain, non-technical language
3. **Specified purpose** — each purpose stated separately; generic purposes ("business operations") are insufficient
4. **Processing activities** — brief description of how the data will be used for each stated purpose
5. **Recipients** — categories of Processors and other Data Fiduciaries who will receive the data; identify by category if not by name
6. **Retention period** — either a fixed period or the criteria for determining retention (e.g., "until withdrawal of consent" or "for the period required by law + 3 years")
7. **Data Principal rights** — summary of rights under Sections 11, 12, 13, and 14; how to exercise each
8. **Complaint mechanism** — steps to submit a grievance to the Data Fiduciary; Board complaint escalation pathway
9. **Withdrawal procedure** — how to withdraw consent; the mechanism; what happens to data and processing after withdrawal

### Rule 3(2) — Format Requirements

- Plain language — assessed against comprehension by an average literate adult, not a legal professional
- Standalone document — independent of T&Cs, product descriptions, or service agreements
- Retrievable at any time — permanently accessible via platform or website even after consent is given or service is engaged
- Must not be more complex than necessary — a notice that requires a legal degree to comprehend fails the plain language test

### Rule 3(3) — Language

- Notice must be provided in English by default
- On request by the Data Principal, the Data Fiduciary must provide the notice in the language the Data Principal requests, **provided that language is in the Eighth Schedule of the Constitution of India**
- The Eighth Schedule contains 22 scheduled languages including Hindi, Bengali, Tamil, Telugu, Kannada, Malayalam, Gujarati, Marathi, Punjabi, Urdu, and others

**Practical implication:** Organisations with Indian user bases should plan for multi-language notice delivery, particularly for consumer-facing applications where the user base spans multiple linguistic regions.

### Rule 3(4) — Existing Data Notices

Data Fiduciaries processing data collected before commencement must issue a Rule 3(1)-compliant notice within the **prescribed period** after the Act comes into force. The specific period is to be notified by MeitY; monitor the Official Gazette. Do not rely on any specific number of months until confirmed by notification.

> **Note:** Section 5(2) of the Act uses the term "prescribed period" without specifying a duration. The period is set in the Rules (or a schedule thereto) and has not been publicly confirmed as of April 2026. Advise clients to treat the existing-data notice obligation as active from 13 May 2027 at the latest, and ideally begin notice issuance well before that deadline.

---

## Rule 4 — Consent

**Source authority:** Section 6 of the Act.

### Rule 4(1) — Consent Mechanism

Consent must be obtained through a clear affirmative action:
- Digital: button click, checkbox activation, explicit tap — all accompanied by a statement describing the purpose
- Written: signed statement for non-digital or paper-based interactions
- **Not acceptable:** Pre-filled checkboxes, silence, continued use of a service, inaction

### Rule 4(2) — Granularity

- Separate consent must be obtained for each distinct purpose
- Bundling consent for multiple purposes into a single action is permitted **only where purposes are genuinely interdependent** — the burden of demonstrating interdependence lies on the Fiduciary
- Consent for optional or additional features must be obtained separately from consent for core service functionality

### Rule 4(3) — Consent Records

Data Fiduciaries must maintain consent records containing:
- Data Principal identifier (sufficient to link to the individual's account/record)
- Timestamp of consent
- Notice version presented at time of consent (version ID or hash)
- Mechanism through which consent was given (button click, signed form, etc.)
- Specific purpose(s) consented to
- Withdrawal timestamp and mechanism (when applicable)

Consent records must be retained for the duration of the processing engagement and for the prescribed period thereafter.

### Rule 4(4) — Withdrawal Mechanism

- Digital withdrawal must be achievable in **no more steps than consent was given**
- If consent was given by a single button click, withdrawal must be achievable by a single equivalent action (e.g., toggle off, single-click revoke)
- Withdrawal mechanism must be clearly visible and accessible — not hidden in account settings deep navigation

---

## Rule 5 — Consent Managers

**Source authority:** Section 6(3) of the Act.

### Rule 5(1) — Registration

Consent Managers must be registered with the Data Protection Board before operating.

**Eligibility:**
- Body corporate incorporated in India
- Net worth requirements: minimum ₹[prescribed amount] — verify against gazette notification
- No conflicts of interest between the Consent Manager and Data Fiduciaries on its platform

### Rule 5(2) — Technical Requirements

Consent Managers must implement:
- Interoperable technical standards for consent record exchange with Data Fiduciaries
- Secure authentication mechanisms for Data Principals accessing the platform
- Audit trails for all consent actions (give, modify, withdraw) with timestamps

### Rule 5(3) — Data Principal Interface

Consent Managers must provide Data Principals with:
- A consolidated view of all consents given across Data Fiduciaries on the platform
- Ability to give, review, modify, and withdraw individual consents from a single interface
- Notifications when Data Fiduciaries process data pursuant to existing consents

### Rule 5(4) — Liability

- Consent Managers are liable for inaccurate consent records resulting from their platform errors
- Data Fiduciaries retain primary liability to Data Principals for processing — engaging a Consent Manager does not transfer liability
- Consent Managers must carry appropriate professional indemnity insurance

---

## Rule 6 — Personal Data Breach Notification

**Source authority:** Section 8(6) of the Act.

### Rule 6(1) — Notification to Board

**Timeline:** Within **72 hours** of the Data Fiduciary becoming aware of a breach.

**Form:** Notification submitted via the Board's prescribed digital portal (Board portal to be established and notified).

**Content of initial notification:**

| Field | Required Content |
|-------|----------------|
| Fiduciary identity | Full legal name, registration details, DPO/responsible officer contact |
| Nature of breach | Type of incident: ransomware, insider leak, misconfiguration, third-party compromise, etc. |
| Data categories affected | Categories of personal data involved (not necessarily exhaustive list) |
| Approximate volume | Estimated number of records and Data Principals affected |
| Detection timeline | When breach was detected and how |
| Immediate measures | Containment actions taken at time of notification |
| Likely consequences | Reasonably foreseeable harm to affected Data Principals |
| Investigation status | Whether investigation is ongoing and expected completion |

### Rule 6(2) — Supplementary Notification

Where the initial notification is incomplete due to ongoing investigation, the Fiduciary must submit supplementary notifications as further information becomes available.

**Board direction:** The Board may direct the Fiduciary to provide specific additional information within a specified period.

### Rule 6(3) — Data Principal Notification

The Board may direct the Fiduciary to notify affected Data Principals. Board-directed notification must:
- Describe the breach in terms accessible to the average Data Principal
- State what personal data was affected
- State what action the Data Principal should consider taking (e.g., change passwords, monitor financial accounts)
- Provide a dedicated contact point for affected Data Principal queries

### Rule 6(4) — Processor Breach Notification

Data Processors must notify the Data Fiduciary **promptly** (within 24 hours — to allow Fiduciary to meet the 72-hour Board notification deadline) upon detecting or becoming aware of a breach affecting data processed on the Fiduciary's behalf.

### Rule 6(5) — Recordkeeping

Fiduciaries must maintain records of all breaches (including near-misses) for a minimum of 3 years, available for Board inspection.

---

## Rule 7 — Security Safeguards

**Source authority:** Section 8(3) of the Act.

### Rule 7(1) — Technical Safeguards

Data Fiduciaries must implement:

| Safeguard | Specification |
|-----------|--------------|
| **Encryption in transit** | TLS 1.2 minimum for all personal data transmission; TLS 1.3 recommended |
| **Encryption at rest** | AES-256 or equivalent for stored personal data |
| **Access control** | Role-based access control (RBAC); principle of least privilege; privileged access management for administrative accounts |
| **Access logging** | Immutable logs of all access to personal data: user, timestamp, data accessed, action performed |
| **Log retention** | Access logs retained for minimum 2 years |
| **Pseudonymisation** | Applied where technically feasible and operationally consistent with processing purpose |
| **Vulnerability management** | Regular vulnerability assessments (at minimum annual penetration testing; quarterly scans for SDFs) |
| **Patch management** | Critical security patches applied within prescribed timelines (30 days for critical CVEs) |

### Rule 7(2) — Organisational Safeguards

| Safeguard | Specification |
|-----------|--------------|
| **Privacy by Design** | Personal data protection considered at system design stage, not as afterthought |
| **Data minimisation** | Collect only what is necessary for the specified purpose; delete or anonymise when no longer needed |
| **Staff training** | All staff with access to personal data trained on DPDPA obligations annually |
| **Vendor management** | All Data Processors bound by Rule 7-equivalent obligations in contract |
| **Incident response plan** | Documented and tested breach response plan including Rule 6 notification workflow |
| **Internal audit** | Annual internal review of security safeguard adequacy |

### Rule 7(3) — Risk-Proportionate Safeguards

Safeguards must be proportionate to:
- Volume of personal data processed
- Sensitivity of personal data categories
- Potential harm to Data Principals from a breach
- Technical and financial capacity of the Data Fiduciary

**Note for small organisations:** The proportionality principle permits smaller organisations to implement safeguards commensurate with their scale — but this is not a relaxation of the encryption and access control baseline requirements. These apply regardless of size.

---

## Rule 8 — Retention Period

**Source authority:** Section 8(7) of the Act.

### Rule 8(1) — Default Retention Standard

Personal data must be erased when:
1. The specified purpose for which it was collected is fulfilled
2. Consent is withdrawn and no other lawful basis applies
3. The Data Principal exercises the Section 12(3) erasure right and no refusal ground applies

### Rule 8(2) — Retention Schedule

Data Fiduciaries must maintain a documented data retention schedule covering:
- Each category of personal data processed
- The retention period or retention criteria for each category
- The lawful basis for retention beyond purpose fulfilment (statutory requirement, legal claims, etc.)
- The deletion method and timeline upon reaching retention limit

### Rule 8(3) — Periodic Purge Review

Data Fiduciaries must conduct periodic reviews (at minimum annually) of data holdings to identify and erase data that has exceeded its retention period.

---

## Rule 9 — Erasure by Processor

**Source authority:** Section 8(7) of the Act.

Data Processors must:
1. Erase all personal data received from the Data Fiduciary upon termination of the processing engagement
2. Confirm erasure in writing within the prescribed period
3. Ensure that all sub-processors also erase the data and provide equivalent confirmations
4. Maintain records of erasure for 2 years after the engagement

---

## Rule 10 — Processing of Children's Personal Data: Standards

**Source authority:** Section 9 of the Act.

### Rule 10(1) — Age Verification

Before collecting any personal data from a Data Principal who may be a child (under 18), Data Fiduciaries must:
1. Implement an age-determination mechanism at the point of data collection
2. Where the mechanism indicates the Data Principal is under 18, collect verifiable parental consent (Rule 12) before proceeding
3. Not collect any personal data beyond what is necessary to conduct the age-check and parental consent verification

### Rule 10(2) — Prohibited Data Processing

The following are absolutely prohibited for children (no consent can validate these):
1. Tracking of geolocation data
2. Persistent identifiers that track activity across sessions or platforms
3. Behavioural analytics that build individual profiles of the child
4. Targeting of any advertisement based on the child's personal data or inferred characteristics
5. Collection of sensitive personal data beyond what is strictly necessary for the service (health data, biometric data, etc.) without specific Board approval

### Rule 10(3) — Age-Appropriate Design

Data Fiduciaries operating services accessible to children must implement:
- Privacy-by-default settings that offer the highest level of protection without any action by the child or parent
- Simplified notice for children — language comprehensible to a child of the expected age range
- Prohibition on features that could expose children to harm or exploitation

### Rule 10(4) — Exemptions

Where the Central Government has issued a notification under Section 9(3) exempting certain Data Fiduciaries (educational institutions, health providers, safety apps, etc.) from specific Section 9(1) requirements, the exemption applies only to the extent specified. Exemptions must be narrowly construed — where doubt exists, apply the full Section 9 standard.

---

## Rule 11 — Consent Manager for Children

Where parental consent is given through a Consent Manager, the Consent Manager must verify that:
1. The consenting individual is the parent or lawful guardian of the child
2. The consenting individual is 18 years of age or older
3. The verification is recorded in a manner that can be audited

---

## Rule 12 — Verifiable Parental Consent Mechanisms

**Source authority:** Section 9(1) of the Act.

**Approved verification methods:**

### Method 1: DigiLocker Authentication
- Parent/guardian authenticates via DigiLocker using a government-issued ID (Aadhaar, PAN, passport, etc.)
- Authentication confirms: (a) identity of the adult; (b) their relationship to the child (where linked records exist)
- Data Fiduciary receives a confirmation token — not the underlying ID document

### Method 2: Government-Issued Token
- Any digital token prescribed by the Central Government as a verified identity credential
- Central Government may notify additional acceptable tokens over time — monitor MeitY updates

### Method 3: Existing Verified Relationship
- Where the Data Fiduciary has already conducted KYC or equivalent identity verification for the parent/guardian in a prior relationship
- The Fiduciary must confirm: (a) that the prior verification is still current and valid; (b) that the person consenting is the same individual whose identity was verified
- Cannot be used if the prior verification is more than [prescribed period] old or if the Fiduciary has any reason to doubt the relationship

### Method 4: Virtual Token (anonymised)
- Token issued by a MeitY-registered entity that provides an anonymised confirmation of: (a) adult age; (b) parental relationship
- Token does not expose the parent's identity to the Data Fiduciary — privacy-preserving verification
- Preferred method for consumer platforms seeking to minimise parental data collection

**Data minimisation in verification:**
The verification process itself must not collect more personal data than necessary to confirm adult age and parental relationship. Retaining a copy of the government ID beyond the verification transaction is not permitted.

---

## Rule 13 — Significant Data Fiduciary: Additional Obligations

**Source authority:** Section 10 of the Act.

### Rule 13(1) — SDF Designation Criteria (supplementary to Section 10)

In addition to the statutory criteria (Section 10), the Central Government considers:

| Factor | Indicators |
|--------|-----------|
| Data volume | Processing data of more than [notified threshold] Data Principals |
| Sensitivity profile | Processing sensitive personal data (financial, health, biometric, geolocation) at scale |
| Interconnection | Serving as a data intermediary or platform operator for multiple other Data Fiduciaries |
| Market dominance | Systemic importance as a digital platform or service |
| Cross-border exposure | Processing data of Indian Data Principals in jurisdictions with weak data protection |

### Rule 13(2) — DPO Requirements

| Requirement | Standard |
|-------------|----------|
| Residency | Must reside in India at all times during tenure |
| Qualifications | Legal, technical, or compliance background in data protection; specific minimum qualifications to be notified |
| Independence | Must have functional independence — not subject to instructions from the Fiduciary that would compromise compliance obligations |
| Access | Must have direct access to the Fiduciary's Board of Directors or equivalent governance body |
| Resources | Must be provided adequate staff, budget, and systems to perform the role |
| Terms | Appointment, remuneration, and removal governed by service agreement; removal only for cause |

### Rule 13(3) — DPIA Requirements

The annual Data Protection Impact Assessment must be conducted by the SDF's internal privacy function (or an external expert engaged for this purpose) and must cover:

1. **Processing activity register** — updated catalogue of all processing activities during the year
2. **Legal basis review** — confirmation that all processing has a valid lawful basis
3. **Rights exercise analysis** — data on Section 11–14 requests: volume, nature, response rate, resolution rate
4. **Complaint analysis** — grievances received, root causes identified, remediation actions taken
5. **Safeguard assessment** — review of whether Rule 7 safeguards remain adequate; gap identification
6. **Processor compliance** — audit of Data Processor contract compliance; confirmation that Rule 16 obligations are being met
7. **Children's data compliance** (if applicable) — audit of age verification and prohibition compliance
8. **New technology assessment** — any new processing technologies, AI systems, or automated decision-making introduced during the year and their data protection implications
9. **Risk register update** — updated risk assessment with residual risk ratings and treatment plans

**Submission:** DPIA report submitted to the Board annually within [prescribed period] of year-end.

### Rule 13(4) — Data Audit Requirements

**Auditor eligibility:**
- Registered with the Board's panel of Data Auditors
- Independent of the SDF and its group companies
- No conflict of interest with the SDF's business activities

**Audit scope:**
- Full compliance audit against all Act and Rules obligations
- Review of DPIA quality and completeness
- Assessment of breach notification history and response adequacy
- Verification of DPO role and independence
- Assessment of Data Principal rights request fulfilment
- Review of Processor agreements and sub-processing chain

**Audit report:** Submitted to the Board. The Board publishes a summary register of SDF audits (specific findings remain confidential to the Board).

### Rule 13(5) — Data Localisation Implementation

Upon Central Government notification of a data localisation requirement:
- SDFs have [prescribed period] to achieve compliance
- Must be able to demonstrate that specified data categories are stored only on infrastructure physically located in India
- Cloud deployments: data residency in Indian availability zones required; no replication to non-Indian regions for notified data categories

---

## Rule 14 — Data Auditor Registration

**Registration with Board:**
- Applicants must meet minimum qualification and experience criteria
- Criteria include: professional qualifications in information security, data protection, law, or related fields; minimum years of experience; continuing professional development requirements
- Registration is valid for [prescribed period]; renewable upon continued compliance with qualification standards

**Code of conduct:**
- Data Auditors are bound by a Board-prescribed code of conduct
- Must maintain professional independence; must not accept instructions from SDFs on audit scope or findings
- Must maintain confidentiality of SDF's proprietary information while reporting compliance findings to the Board

---

## Rule 15 — Consent Manager Registration (Extended)

See Rule 5. Additional requirements for Consent Managers registered with the Board:

- Annual compliance certification submitted to Board
- Technical interoperability audit of the consent platform
- Financial stability certification (maintaining minimum net worth throughout registration period)
- Incident reporting: any data breach affecting consent records must be reported to the Board within 24 hours

---

## Rule 16 — Data Processing Agreements

**Source authority:** Section 8(1) of the Act.

### Rule 16(1) — Mandatory Contract Requirements

Written contracts with Data Processors must include:

| Clause | Minimum Content |
|--------|----------------|
| **Processing instructions** | Processor may only process data strictly in accordance with Fiduciary's written instructions; no independent processing |
| **Purpose limitation** | Processing restricted to specified purposes in the contract; no secondary use |
| **Security obligations** | Processor must implement safeguards meeting or exceeding Rule 7 standards |
| **Sub-processing** | Sub-processors may not be engaged without prior written approval of the Fiduciary; sub-processors must be bound by equivalent contract terms |
| **Audit rights** | Fiduciary has right to audit Processor's compliance at reasonable notice; Processor must cooperate and provide access |
| **Assistance obligations** | Processor must assist Fiduciary in fulfilling Data Principal rights requests (access, correction, erasure) where Processor holds the relevant data |
| **Breach notification** | Processor must notify Fiduciary within 24 hours of detecting any breach; must provide all Rule 6 information available |
| **Erasure/return on termination** | Processor must erase or return all personal data on termination; must confirm erasure in writing within [prescribed period] |
| **Confidentiality** | Processor must bind all staff processing data to confidentiality obligations |
| **Liability** | Parties agree on indemnity arrangements; noting that the Fiduciary remains primarily liable to Data Principals |

### Rule 16(2) — Processor Register

Data Fiduciaries must maintain a register of all current Data Processors and sub-processors containing:
- Legal name and contact details
- Countries where processing takes place
- Categories of personal data processed
- Contract execution date and term
- Data categories subject to cross-border transfer (if any)

Register must be available for Board inspection.

### Rule 16(3) — Existing Contracts

Contracts executed before commencement of the Act must be brought into compliance with Rule 16(1) within [prescribed period] of commencement. Where existing contracts are framework agreements, amendments may be effected by addendum.

---

## Rule 17 — Board Complaint Procedure

### Rule 17(1) — Complaint Prerequisites

Before filing a complaint with the Board, the Data Principal must:
1. Have submitted a grievance to the Data Fiduciary under Section 13
2. Have waited for the Data Fiduciary's response for at least the prescribed period (or the Fiduciary's response is unsatisfactory)

### Rule 17(2) — Complaint Form and Content

Board complaints must be submitted via the Board's digital portal and must include:
- Identity of the complainant (Data Principal)
- Identity of the respondent (Data Fiduciary)
- Description of the alleged violation
- Evidence of prior grievance submission to the Fiduciary and its outcome
- Relief sought

### Rule 17(3) — Confidentiality

The Board may conduct proceedings in camera where the data at issue is sensitive. Parties may request confidential treatment of commercially sensitive information.

---

## Rule 18 — Board Proceedings

### Rule 18(1) — Natural Justice

Board proceedings must comply with principles of natural justice:
- Both parties have the right to be heard
- Right to examine and respond to evidence
- Impartial adjudication

### Rule 18(2) — Evidence and Discovery

The Board has power to:
- Require Data Fiduciaries to produce records, contracts, and consent records
- Require Data Processors to provide information relevant to proceedings
- Commission technical assessments by independent experts

### Rule 18(3) — Summary Proceedings

For complaints below a prescribed threshold (minor violations; small compensation sought), the Board may adopt a summary procedure with shorter timelines and simplified evidence rules.

---

## Rule 19 — Alternate Dispute Resolution

**Source authority:** Section 29 of the Act.

Board-facilitated mediation/conciliation:
- Available at the Board's discretion or on joint request of parties
- Mediator appointed from Board's panel of qualified mediators
- Settlement agreements have the force of a Board order
- ADR proceedings confidential — cannot be used in evidence in subsequent litigation

---

## Rule 20 — Voluntary Undertaking

**Source authority:** Section 30 of the Act.

A Data Fiduciary may offer a voluntary undertaking to the Board:
- Specifying the violation or potential violation
- Committing to specific remediation actions and timelines
- Agreeing to monitoring by the Board during remediation

Board may accept, modify, or reject the undertaking. If accepted:
- Breach of undertaking attracts penalty up to ₹50 crore
- Accepted undertaking does not bar Board from further action if breach occurs

---

## Rule 21 — Appeal to TDSAT

**Source authority:** Section 27 of the Act.

- Appeals to TDSAT must be filed within [prescribed period] of the Board's order
- TDSAT may stay the Board's order pending appeal on application showing prima facie case and balance of convenience
- TDSAT proceedings governed by TDSAT's own rules of procedure

---

## Rule 22 — Fees

Prescribed fees for Board proceedings, Consent Manager registration, and Data Auditor registration are specified in the Schedule to the Rules. Fees subject to periodic revision by MeitY notification.

---

## Rule 23 — Protection of Actions Taken in Good Faith

Board members, officers, and Data Auditors are not liable for actions taken in good faith in exercise of their functions under the Act and Rules. Good faith is presumed unless shown otherwise.

---

## Summary: Key Implementation Timelines

| Milestone | Date |
|-----------|------|
| Rules notified | 13 November 2025 |
| Full compliance deadline | 13 May 2027 |
| Existing data notice deadline | Within the **prescribed period** after commencement — specific timeframe to be notified; monitor MeitY gazette |
| Existing Processor contract update | Within prescribed period of commencement |
| Board portal operational | To be notified by Board |
| First SDF designations expected | 2026–2027 (anticipated; not yet issued as of April 2026) |

> **Monitoring requirement:** Several provisions reference amounts, timelines, and criteria "to be prescribed" by notification or Schedule. These are published via MeitY's Official Gazette and the Board's website. Organisations should maintain a monitoring programme for these supplementary notifications as they are issued throughout the transition period.
