# ISO 27701:2025 Annex A — Complete Control Reference

ISO/IEC 27701:2025 contains **78 controls** in three tables:
- **A.1**: 31 controls for PII Controllers
- **A.2**: 18 controls for PII Processors
- **A.3**: 29 shared information security controls (both roles)

**Note on numbering:** Within each domain, .1 is the domain objective statement
(not a numbered control). Controls begin at .2. For example, A.1.2.1 is the
objective for the A.1.2 domain; controls run from A.1.2.2 onward.

---

## Table A.1 — PII Controller Controls (31 controls)

Organizations acting as PII controllers must implement all applicable A.1 controls
plus all A.3 controls (60 total).

---

### A.1.2 — Conditions for Collection and Processing (8 controls)

**Domain objective**: Ensure PII is collected and processed only under conditions
that establish a clear, documented legal basis and that processing is transparent
to relevant parties.

| Control ID | Control Name | Description | Common Gaps |
|-----------|--------------|-------------|-------------|
| A.1.2.2 | Identify and Document Purpose | Document the specific purposes for which PII is collected; purpose must be stated before collection begins | Vague or catch-all purpose statements; purposes undocumented in RoPA |
| A.1.2.3 | Identify Lawful Basis | Identify and document the lawful basis for each processing activity (consent, contract, legal obligation, vital interests, public task, legitimate interests) | No per-activity lawful basis mapping; LIA not completed for legitimate interest claims |
| A.1.2.4 | Determine Consent | Where consent is the lawful basis, define when and how consent will be obtained; ensure it meets the required standard (freely given, specific, informed, unambiguous) | Pre-ticked boxes; bundled consent; no record of when consent was obtained |
| A.1.2.5 | Obtain and Record Consent | Implement mechanisms to capture, record, and maintain proof of consent | No consent audit trail; inability to retrieve consent records for specific individuals |
| A.1.2.6 | Privacy Impact Assessment | Conduct PIAs / DPIAs for new or significantly changed processing activities; document findings and decisions | PIA process exists but not triggered consistently; no DPIA for high-risk processing |
| A.1.2.7 | Contracts with PII Processors | Ensure all PII processors are engaged under a written Data Processing Agreement (DPA) specifying obligations | Processor contracts missing; legacy contracts without GDPR-compliant DPA clauses |
| A.1.2.8 | Joint PII Controller | Where two organizations jointly determine purposes, document the joint controller arrangement and each party's obligations | Joint controller arrangement undocumented; responsibilities undefined |
| A.1.2.9 | Records of Processing PII | Maintain complete Records of Processing Activities (RoPA) covering all processing operations | RoPA incomplete, out of date, or not maintained; no process to update on system changes |

---

### A.1.3 — Obligations to PII Principals (10 controls)

**Domain objective**: Ensure PII principals can exercise their rights and are
provided with sufficient information about how their PII is processed.

| Control ID | Control Name | Description | Common Gaps |
|-----------|--------------|-------------|-------------|
| A.1.3.2 | Obligations to PII Principals | Establish and document the organization's obligations to PII principals and the mechanisms by which those obligations are met | No documented obligations register; rights not mapped to processes |
| A.1.3.3 | Information for PII Principals | Determine what information must be provided to PII principals before or at the point of collection | Privacy notice does not cover all required information elements |
| A.1.3.4 | Providing Information | Provide the required information to PII principals in a clear, accessible, and timely manner (typically via privacy notice) | Privacy notice not easy to find; information presented in complex legal language |
| A.1.3.5 | Modify or Withdraw Consent | Provide PII principals with a mechanism to modify or withdraw previously given consent, without detriment | No withdrawal mechanism; withdrawal treated as deletion rather than consent change |
| A.1.3.6 | Object to PII Processing | Provide mechanism for PII principals to object to processing (particularly for legitimate interest or direct marketing) | No documented objection process; no SLA for response |
| A.1.3.7 | Access, Correction or Erasure | Provide mechanism for PII principals to access their data, request correction of inaccuracies, or request erasure (right to erasure / right to be forgotten) | No DSR workflow; erasure requests not propagated to all systems |
| A.1.3.8 | Inform Third Parties | When PII is corrected or erased, inform relevant third parties to whom it was disclosed | No process to track and notify third parties after correction/erasure |
| A.1.3.9 | Providing Copy of PII | Provide PII principals with a copy of their PII upon request (right of access / right to data portability) | No automated or streamlined way to fulfil subject access requests |
| A.1.3.10 | Handling Requests | Establish a process for receiving, tracking, authenticating, and responding to all DSR types within required timescales | Requests handled ad hoc; no SLA tracking; identity verification process missing |
| A.1.3.11 | Automated Decision Making | Where automated decision-making with significant effects is used, disclose this and provide mechanisms for human review | Automated decisions undisclosed; no opt-out or appeal mechanism |

---

### A.1.4 — Privacy by Design and by Default (9 controls)

**Domain objective**: Embed privacy principles into the design and operation of
systems and processes, ensuring PII is collected and processed only to the extent
necessary.

| Control ID | Control Name | Description | Common Gaps |
|-----------|--------------|-------------|-------------|
| A.1.4.2 | Limit Collection | Collect only the PII that is necessary for the stated purpose (data minimisation) | Collecting more fields than required "just in case"; no data minimisation review in product design |
| A.1.4.3 | Limit Processing | Process PII only for the stated purpose; prevent secondary use without additional legal basis | Processing PII for analytics or profiling beyond original purpose |
| A.1.4.4 | Accuracy and Quality | Implement controls to maintain accuracy of PII; provide mechanisms for correction | No data quality validation; no user self-service correction mechanism |
| A.1.4.5 | PII Minimisation | Apply systematic controls to minimise the amount of PII held and processed | No PII minimisation checklist in SDLC; fields not reviewed for necessity |
| A.1.4.6 | De-identification and Deletion | Implement de-identification and deletion procedures to remove PII when it is no longer needed | No automated deletion; PII retained indefinitely in test environments |
| A.1.4.7 | Temporary Files | Ensure temporary files containing PII are securely managed and deleted when no longer needed | Temp files, logs, and cache containing PII not covered by retention/deletion policy |
| A.1.4.8 | Retention | Define and implement data retention schedules for each PII category, aligned to legal obligations | No retention schedule; all data kept indefinitely; retention schedule not enforced technically |
| A.1.4.9 | Disposal | Securely dispose of PII at end of retention period; document disposal | No secure deletion process; PII disposed with general data |
| A.1.4.10 | PII Transmission Controls | Apply controls to protect PII in transit (encryption, secure channels, access controls) | PII transmitted over unencrypted channels; no controls on email transmission of PII |

---

### A.1.5 — PII Sharing, Transfer and Disclosure (4 controls)

**Domain objective**: Ensure that transfers of PII to third countries or international
organizations comply with applicable law, and that all transfers and disclosures
are documented.

| Control ID | Control Name | Description | Common Gaps |
|-----------|--------------|-------------|-------------|
| A.1.5.2 | Basis for PII Transfer | Identify and document the legal basis for each transfer of PII to a third country or international organization (adequacy decision, SCCs, BCRs, derogations) | Transfers to third countries without documented legal basis; SCCs not signed |
| A.1.5.3 | Countries for PII Transfer | Document the countries or international organizations to which PII is transferred | No transfer mapping; transfers via cloud providers not documented |
| A.1.5.4 | Records of PII Transfer | Maintain records of all PII transfers to third parties | Transfer log not maintained; no visibility into all third-party transfers |
| A.1.5.5 | Records of PII Disclosures | Maintain records of all disclosures of PII to third parties (including law enforcement requests) | Disclosure log not maintained; no record of ad hoc disclosures |

---

## Table A.2 — PII Processor Controls (18 controls)

Organizations acting as PII processors must implement all applicable A.2 controls
plus all A.3 controls (47 total).

---

### A.2.2 — Conditions for Collection and Processing (6 controls)

| Control ID | Control Name | Description | Common Gaps |
|-----------|--------------|-------------|-------------|
| A.2.2.2 | Customer Agreement | Process PII only in accordance with documented instructions from the PII controller; ensure a written DPA is in place | Processing PII outside contract scope; no DPA in place for all controllers |
| A.2.2.3 | Organisation's Purposes | Do not process PII for the processor's own purposes; processing is limited to what is specified by the controller | Using controller PII for own analytics, product training, or marketing |
| A.2.2.4 | Marketing and Advertising | Do not use PII processed on behalf of a controller for marketing or advertising without explicit authorization | Using customer data for cross-marketing between controller clients |
| A.2.2.5 | Infringing Instruction | Notify the controller if an instruction would infringe applicable privacy law; do not execute infringing instructions | No process to review and escalate potentially infringing controller instructions |
| A.2.2.6 | Customer Obligations | Assist the controller in meeting its obligations to PII principals (e.g., DSRs, DPIAs, breach notification) | No defined process to support controller's DSR fulfilment within contractual timeframes |
| A.2.2.7 | Records of Processing PII | Maintain records of all processing activities carried out on behalf of each controller | No per-controller processing records; single combined log not sufficient |

---

### A.2.3 — Obligations to PII Principals (1 control)

| Control ID | Control Name | Description | Common Gaps |
|-----------|--------------|-------------|-------------|
| A.2.3.2 | Obligations to PII Principals | Where the processor interacts with PII principals, fulfil the obligations defined by the controller; redirect inquiries to the controller where appropriate | Processor staff unaware of how to handle DSR inquiries received directly |

---

### A.2.4 — Privacy by Design and by Default (3 controls)

| Control ID | Control Name | Description | Common Gaps |
|-----------|--------------|-------------|-------------|
| A.2.4.2 | Temporary Files | Ensure temporary files created during processing on behalf of a controller are managed and deleted per agreed schedules | Temporary processing files retained beyond task completion |
| A.2.4.3 | Return, Transfer or Disposal of PII | Upon termination of the processing agreement, return all PII to the controller or securely dispose of it as instructed | No offboarding procedure; PII retained after contract end |
| A.2.4.4 | PII Transmission Controls | Apply controls to protect PII in transit during processing operations | PII transmitted without encryption between processor subsystems |

---

### A.2.5 — PII Sharing, Transfer and Disclosure (8 controls)

| Control ID | Control Name | Description | Common Gaps |
|-----------|--------------|-------------|-------------|
| A.2.5.2 | Basis for PII Transfer | Identify and document the legal basis for any transfer of PII to a third country or international organization | Sub-processor transfers not mapped to legal transfer mechanism |
| A.2.5.3 | Countries for PII Transfer | Document the countries or international organizations to which PII is transferred during processing | Data residency commitments made but not enforced; sub-processor locations undocumented |
| A.2.5.4 | Records of PII Disclosures | Maintain records of all disclosures of PII to third parties | Disclosure log not maintained at processor level |
| A.2.5.5 | Notification of PII Disclosure Requests | Notify the controller when a third party requests disclosure of PII (e.g., law enforcement) before disclosing, where legally permitted | No process to notify controllers of government/law enforcement access requests |
| A.2.5.6 | Legally Binding PII Disclosures | Where legally compelled to disclose PII (e.g., court order), notify the controller where legally permitted and record the disclosure | Disclosures made without notifying controller; no legal review process |
| A.2.5.7 | Disclosure of Subcontractors | Disclose to the controller the identity and location of all sub-processors used | Sub-processor list not maintained or shared with controllers |
| A.2.5.8 | Engagement of a Subcontractor | Obtain controller authorization before engaging a new sub-processor; flow down equivalent data protection obligations | Sub-processors engaged without controller authorization; no data protection clauses in sub-processor contracts |
| A.2.5.9 | Change of Subcontractor | Notify the controller in advance of any changes to sub-processors; provide the controller opportunity to object | Controllers not notified of sub-processor changes; no prior notice mechanism |

---

## Table A.3 — Shared Information Security Controls (29 controls)

Applies to **all organizations** (controllers and processors). These are information
security controls selected from the ISO 27001/27002:2022 framework, adapted to
support privacy protection.

| Control ID | Control Name | Privacy Relevance |
|-----------|--------------|------------------|
| A.3.3 | Information Security Policies | Policies must explicitly address privacy and PII protection |
| A.3.4 | Security Roles | Define privacy-relevant security roles; ensure DPO / privacy officer interactions |
| A.3.5 | Classification of Information | PII must be classified appropriately to drive correct handling controls |
| A.3.6 | Labelling of Information | Label PII-containing assets so handling controls are applied consistently |
| A.3.7 | Information Transfer | Controls on transferring PII between systems, people, and organizations |
| A.3.8 | Identity Management | Manage identities of all personnel with access to PII systems |
| A.3.9 | Access Rights | Restrict access to PII on a need-to-know / least-privilege basis |
| A.3.10 | Supplier Agreements | Supplier/vendor contracts must include appropriate privacy and data protection clauses |
| A.3.11 | Incident Management | Privacy breaches must be identified, reported, and managed within required timeframes |
| A.3.12 | Security Incident Response | Incident response plans must cover personal data breaches; GDPR 72-hour notification must be built in |
| A.3.13 | Legal and Regulatory Requirements | Identify and comply with all applicable privacy laws and regulations |
| A.3.14 | Protection of Records | Records containing PII must be protected against unauthorized access, loss, or destruction |
| A.3.15 | Independent Review | Periodic independent review of PIMS and privacy controls (internal or external audit) |
| A.3.16 | Compliance with Policies | Monitor and verify compliance with privacy policies and procedures |
| A.3.17 | Security Awareness and Training | Privacy training must be included in security awareness; role-based privacy training for high-risk roles |
| A.3.18 | Confidentiality Agreements | All personnel with access to PII must sign confidentiality / NDA agreements |
| A.3.19 | Clear Desk and Clear Screen | PII-containing physical documents and screen displays must be protected when unattended |
| A.3.20 | Storage Media | Removable media containing PII must be controlled; disposal must be secure |
| A.3.21 | Secure Disposal of Equipment | Equipment that held PII must be securely wiped before disposal or reuse |
| A.3.22 | User Endpoint Devices | Endpoints with access to PII must have appropriate security controls (encryption, MDM, screen lock) |
| A.3.23 | Secure Authentication | Strong authentication controls for systems processing PII; MFA recommended |
| A.3.24 | Information Backup | Backups of PII-containing systems must be protected with equivalent controls to primary systems |
| A.3.25 | Logging | Access to and processing of PII must be logged; logs must be protected against tampering |
| A.3.26 | Use of Cryptography | Encryption at rest and in transit for PII; key management procedures |
| A.3.27 | Secure Development Life Cycle | Privacy by design embedded in SDLC; privacy requirements defined before development begins |
| A.3.28 | Application Security | Applications processing PII must be tested for security vulnerabilities (including input validation, authentication) |
| A.3.29 | Secure System Architecture | System architecture must segregate PII and support principle of least privilege |
| A.3.30 | Outsourced Development | Privacy and security requirements must be flowed into outsourced development contracts |
| A.3.31 | Test Information | Live PII must not be used in test environments without authorization and equivalent controls |

---

## Control Counts Summary

| Table | Role | Controls | Combined with A.3 |
|-------|------|----------|-------------------|
| A.1 | PII Controller only | 31 | 31 + 29 = **60** |
| A.2 | PII Processor only | 18 | 18 + 29 = **47** |
| A.1 + A.2 | Both controller and processor | 49 | 49 + 29 = **78** |
| A.3 | All organizations | 29 | Always included |
