# NZISM Classification Framework & Control Applicability

This reference file details the New Zealand Government Information Classification System (ISCS) and how classification levels determine which NZISM controls apply. Use it when advising on classification decisions, control scoping, or handling requirements for a given system.

---

## NZ Government Information Classification System (ISCS)

The ISCS provides a standardised way to classify government information based on the potential harm that could result from unauthorised disclosure.

### Classification Levels

| Level | Marker | Description | Potential Harm from Unauthorised Disclosure |
|-------|--------|-------------|---------------------------------------------|
| **Unclassified** | U | Non-sensitive government information; suitable for public release | Nil or negligible |
| **In-Confidence** | IC | Business-sensitive; restricted to those with a need to know | Could embarrass the agency or individual; breach of trust |
| **Sensitive** | SEN | Sensitive matters requiring careful handling | Release could cause embarrassment or disadvantage to NZ interests |
| **Restricted** | R | Officially classified; limited NZ government access only | Could harm NZ government interests or operations |
| **Confidential** | C | Significantly sensitive; carefully controlled | Significant harm to NZ national interests |
| **Secret** | S | Highly sensitive; very strictly controlled | Serious harm to NZ national interests or international relationships |
| **Top Secret** | TS | Most sensitive classification | Exceptionally grave harm to NZ national interests |

> **Note:** "Sensitive" is sometimes used as a handling caveat in addition to a classification level. Agencies should refer to current GCSB/NCSC NZ guidance for precise current usage of each marker.

---

## Control Applicability by Classification

Controls in the NZISM are marked to indicate which classification levels they apply to. Systems at higher classification levels inherit all controls from lower levels.

### Baseline Controls (Unclassified / In-Confidence)

These controls apply to **all** NZ Government systems regardless of classification:

| Domain | Key Controls |
|--------|-------------|
| Governance | Information security policy; CISO appointment; risk management process |
| Physical | Building access controls; visitor management; clear desk |
| Personnel | Background checks; security awareness training; AUP |
| Information | Basic classification labelling; secure email practices |
| Infrastructure | Asset inventory; patch management (30-day window for critical); hardened configurations |
| Network | Firewall; DNS filtering; email security (SPF/DKIM/DMARC) |
| Access Control | Unique accounts; least privilege; password policy |
| Authentication | Complex passwords; account lockout |
| Audit & Logging | System and application logging; 90-day retention |
| Backup | Regular backups; tested for restoreability |
| Incident Management | Incident response plan; reporting procedure |

---

### Restricted Controls (in addition to baseline)

Systems handling **Restricted** information must additionally implement:

| Domain | Additional Controls |
|--------|-------------------|
| Physical | Dedicated secure zones for server equipment; access logging |
| Cryptography | Encryption at rest for Restricted data; TLS 1.2+ for all data in transit |
| Access Control | MFA for all remote access; privileged account separation |
| Audit & Logging | Enhanced logging of privileged actions; 12-month log retention |
| Third-Party Suppliers | NZISM-equivalent contractual controls; security assessment of suppliers |
| Certification | Formal Certification & Accreditation (C&A) required before system go-live |
| Cloud | Cloud risk assessment required; data residency assessment |
| Mobility | MDM enrollment mandatory; remote wipe capability |
| Backup | Off-site backup with appropriate classification controls |

**C&A Requirement:** All systems handling Restricted information must be formally certified and accredited by an Accrediting Authority before go-live.

---

### Confidential Controls (in addition to Restricted)

Systems handling **Confidential** information must additionally implement:

| Domain | Additional Controls |
|--------|-------------------|
| Physical | Secure rooms with approved access control; CCTV; security guards where appropriate |
| Cryptography | AES-256 encryption at rest mandatory; NCSC NZ approved cipher suites only; HSM for key storage preferred |
| Network | Dedicated network segments; no internet-facing systems without approved gateway |
| Access Control | Background vetting required for all administrators; biometric or hardware token authentication |
| Audit & Logging | Real-time security monitoring; SIEM; tamper-evident log storage |
| Third-Party Suppliers | Offshore processing prohibited without Accrediting Authority approval |
| Incident Management | Immediate NCSC NZ notification for any incident involving Confidential data |

---

### Secret and Top Secret Controls

Systems handling **Secret** or **Top Secret** information are subject to the most stringent controls and require direct engagement with GCSB/NCSC NZ for accreditation:

| Domain | Additional Controls |
|--------|-------------------|
| Physical | Purpose-built secure facilities; TEMPEST assessment and mitigation required |
| Cryptography | GCSB-approved cryptographic equipment and key management |
| Network | Air-gapped or dedicated encrypted networks; no connectivity to lower-classification networks |
| Personnel | Full security vetting to Secret or Top Secret level for all users and administrators |
| Accreditation | Direct GCSB involvement in accreditation process |
| Supply Chain | Only GCSB-approved suppliers for system components |

> Agencies planning Secret or Top Secret systems must engage with NCSC NZ / GCSB early in the design process.

---

## Classification Decision Guide

Use this guide when helping agencies determine the appropriate classification:

**Ask these questions:**
1. What information does the system store, process, or transmit?
2. Who needs access to this information?
3. What is the potential harm from unauthorised disclosure?
4. What legal or regulatory obligations apply (Privacy Act 2020, Official Information Act 1982)?
5. Does the system connect to or integrate with higher-classification systems?

**Key principles:**
- **Classify at the highest level** of any information the system holds
- **Aggregation risk** — combining multiple Unclassified data sets may produce Restricted-level information
- **System classification** is determined by the most sensitive data it ever processes — even if most data is lower
- **Downgrading** requires formal approval and evidence that higher-classification data has been removed

---

## Handling Requirements by Classification

### Labelling
- All documents, emails, and files must carry the classification marking (e.g., RESTRICTED, IN-CONFIDENCE)
- Email subject lines and footers must include the classification
- Automated labelling tools are preferred for consistency

### Transmission
| Classification | Acceptable Transmission Methods |
|---------------|-------------------------------|
| Unclassified / IC | Standard email, public cloud storage |
| Sensitive / Restricted | Encrypted email (TLS); encrypted file transfer; VPN for system-to-system |
| Confidential | NCSC NZ approved encrypted channel; no standard email |
| Secret / Top Secret | GCSB-approved cryptographic equipment only |

### Storage
| Classification | Storage Requirements |
|---------------|---------------------|
| Unclassified / IC | Standard agency systems with access controls |
| Restricted | Encrypted at rest; classified storage areas |
| Confidential | Encrypted at rest (AES-256); physically secured server rooms |
| Secret / TS | GCSB-accredited storage media and facilities |

### Disposal
| Classification | Disposal Method |
|---------------|----------------|
| Unclassified / IC | Standard electronic deletion; cross-cut shredding for paper |
| Restricted | Certified electronic data wiping (NIST 800-88 or equivalent); cross-cut shredding |
| Confidential+ | Degaussing + physical destruction of media; certificate of destruction required |
| Secret / TS | Destruction under GCSB-approved procedures; witnessed and certified |

---

## Certification & Accreditation Timeline

| Phase | Activity | Typical Duration |
|-------|---------|-----------------|
| 1. Prepare | Develop SSP, risk register, security controls documentation | 4–8 weeks |
| 2. Certify | Independent security assessment against NZISM controls | 2–4 weeks |
| 3. Remediate | Address findings; update POA&M | 2–6 weeks |
| 4. Accredit | Accrediting Authority review and ATO sign-off | 1–2 weeks |
| 5. Monitor | Continuous monitoring; periodic re-certification | Ongoing |

**Re-certification triggers:**
- Major system change (new integrations, hosting migration, significant architecture change)
- Significant security incident
- Classification level change
- Periodic re-certification (typically every 1–3 years depending on risk)

---

## Relevant NZ Legislative and Policy Context

| Instrument | Relevance |
|-----------|----------|
| **NZISM** | Mandatory security controls framework for NZ government agencies |
| **Privacy Act 2020** | Governs personal information; agencies must conduct Privacy Impact Assessments (PIAs) |
| **Official Information Act 1982 (OIA)** | Governs release of government information; classification informs OIA decisions |
| **Public Records Act 2005** | Governs retention and disposal of government records |
| **Protective Security Requirements (PSR)** | DPMC framework for physical, personnel, and information security; NZISM sits under PSR for information security |
| **NZ Government Cloud Computing Risk & Resilience Guide** | NCSC NZ guidance on cloud service adoption |
| **Cyber Security Strategy 2019** | NZ Government's strategic direction for cybersecurity |
