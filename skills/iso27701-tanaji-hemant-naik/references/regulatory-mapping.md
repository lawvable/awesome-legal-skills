# ISO 27701:2025 — Regulatory & Framework Mapping

ISO/IEC 27701:2025 is designed to serve as a **compliance framework for multiple
privacy regulations simultaneously**. The standard's updated correspondence annexes
provide mappings to GDPR and other major privacy laws. This guide covers the most
commonly requested mappings.

---

## GDPR (EU General Data Protection Regulation)

ISO 27701:2025 provides the most detailed alignment with GDPR of any privacy
management standard. Its updated correspondence annex maps controls directly to
GDPR articles.

### Key GDPR Principles → ISO 27701 Controls

| GDPR Principle (Art. 5) | ISO 27701:2025 Controls |
|------------------------|------------------------|
| Lawfulness, fairness, transparency | A.1.2.3 (lawful basis), A.1.3.3–A.1.3.4 (transparency) |
| Purpose limitation | A.1.2.2 (document purpose), A.1.4.3 (limit processing) |
| Data minimisation | A.1.4.2 (limit collection), A.1.4.5 (PII minimisation) |
| Accuracy | A.1.4.4 (accuracy and quality), A.1.3.7 (correction) |
| Storage limitation | A.1.4.8 (retention), A.1.4.9 (disposal), A.1.4.6 (deletion) |
| Integrity and confidentiality | A.3.26 (cryptography), A.3.25 (logging), A.3.9 (access) |
| Accountability | A.1.2.9 (RoPA), SoA, privacy risk assessment, management review |

### GDPR Rights → ISO 27701 Controls

| GDPR Right | Article | ISO 27701:2025 Controls |
|-----------|---------|------------------------|
| Right to be informed | Art. 13–14 | A.1.3.3, A.1.3.4 |
| Right of access | Art. 15 | A.1.3.9, A.1.3.10 |
| Right to rectification | Art. 16 | A.1.3.7, A.1.3.8 |
| Right to erasure (right to be forgotten) | Art. 17 | A.1.3.7, A.1.4.6, A.1.4.9 |
| Right to restrict processing | Art. 18 | A.1.3.6, A.1.3.10 |
| Right to data portability | Art. 20 | A.1.3.9 |
| Right to object | Art. 21 | A.1.3.6 |
| Rights re: automated decision-making | Art. 22 | A.1.3.11 |

### GDPR Controller Obligations → ISO 27701 Controls

| GDPR Obligation | Article | ISO 27701:2025 Controls |
|----------------|---------|------------------------|
| Lawful basis for processing | Art. 6 | A.1.2.3 |
| Consent requirements | Art. 7 | A.1.2.4, A.1.2.5 |
| Special categories of data | Art. 9 | A.1.2.3, A.1.2.6, A.1.4.5 |
| Records of processing activities | Art. 30 | A.1.2.9 |
| Data protection by design and default | Art. 25 | A.1.4.2–A.1.4.10 |
| Joint controllers | Art. 26 | A.1.2.8 |
| Processor contracts | Art. 28 | A.1.2.7 |
| Data Protection Impact Assessment | Art. 35 | A.1.2.6 |
| Personal data breach notification | Art. 33–34 | A.3.11, A.3.12 |
| International transfers | Art. 44–49 | A.1.5.2–A.1.5.5 |

### GDPR Processor Obligations → ISO 27701 Controls

| GDPR Obligation | Article | ISO 27701:2025 Controls |
|----------------|---------|------------------------|
| Processing under contract | Art. 28(3) | A.2.2.2 |
| Processing only on instruction | Art. 28(3)(a) | A.2.2.3, A.2.2.5 |
| Confidentiality of processing | Art. 28(3)(b) | A.3.18, A.2.2.6 |
| Security measures | Art. 28(3)(c) | A.3 (all security controls) |
| Sub-processor controls | Art. 28(2), (4) | A.2.5.7–A.2.5.9 |
| Assist controller with rights | Art. 28(3)(e) | A.2.2.6, A.2.3.2 |
| Deletion or return at end | Art. 28(3)(g) | A.2.4.3 |
| Provide information to controller | Art. 28(3)(h) | A.2.2.6 |
| Records of processing activities | Art. 30(2) | A.2.2.7 |
| Notify controller of breaches | Art. 33(2) | A.3.11, A.3.12 |
| Law enforcement disclosure | Art. 28(3)(a) | A.2.5.5, A.2.5.6 |

### How ISO 27701 Certification Supports GDPR Compliance

ISO 27701 certification does not automatically mean GDPR compliance — GDPR also
requires specific legal bases, DPO appointment in certain cases, supervisory authority
registration, and so on. However, certification provides:

- **Documented evidence** of privacy controls for regulatory investigations
- **Accountability evidence** (Art. 5(2)) — demonstrating controls are in place
- **Recognized framework** — supervisory authorities view ISO 27701 favorably
- **DPA evidence** — SoA and control documentation can support DPIA requirements

---

## UK GDPR

The UK GDPR (retained from EU GDPR post-Brexit) maintains near-identical requirements
to EU GDPR. The same ISO 27701:2025 control mappings apply. The UK ICO has stated
that ISO 27701 can be used as a Privacy Seal mechanism under UK GDPR Article 42.

**Key UK-specific consideration**: The UK's International Data Transfer Agreement
(IDTA) and UK Addendum to SCCs are different from EU mechanisms. A.1.5.2 must
reference the appropriate UK transfer mechanism.

---

## CCPA / CPRA (California)

The California Consumer Privacy Act (CCPA) and its amendment (CPRA) share many
concepts with GDPR but have distinct requirements.

| CCPA/CPRA Right or Obligation | ISO 27701:2025 Controls |
|------------------------------|------------------------|
| Right to know (categories and specific pieces) | A.1.3.9, A.1.3.10 |
| Right to delete | A.1.3.7, A.1.4.6, A.1.4.9 |
| Right to opt-out of sale/sharing | A.1.3.6, A.1.2.3 |
| Right to correct | A.1.3.7, A.1.4.4 |
| Right to limit use of sensitive PI | A.1.4.2, A.1.4.5 |
| Right to non-discrimination | Not directly covered — process design |
| Privacy notice (at collection) | A.1.3.3, A.1.3.4 |
| Data minimisation | A.1.4.2, A.1.4.5 |
| Service provider contracts | A.1.2.7 (equivalent to DPA) |
| CPRA risk assessments | A.1.2.6 (PIA/DPIA) |
| Contractor obligations | A.2 (processor controls) |

**CCPA/CPRA notes**:
- CCPA uses "consumer", "business", "service provider", "contractor", "third party"
  — map these to ISO 27701's "PII principal", "PII controller", "PII processor"
- CPRA's "sensitive personal information" category requires additional restrictions
  (maps to A.1.4.2, A.1.4.5)
- CPRA's mandatory risk assessments and cybersecurity audits align with A.1.2.6
  and A.3.15

---

## LGPD (Brazil — Lei Geral de Proteção de Dados)

Brazil's LGPD (effective August 2020) closely mirrors GDPR in structure.

| LGPD Obligation | ISO 27701:2025 Controls |
|----------------|------------------------|
| Legal basis (Art. 7, 11) | A.1.2.3 |
| Consent requirements (Art. 7–9) | A.1.2.4, A.1.2.5 |
| Transparency / privacy notice (Art. 9, 18) | A.1.3.3, A.1.3.4 |
| Data rights (Art. 18–20) | A.1.3.5–A.1.3.11 |
| Data minimisation (Art. 6) | A.1.4.2, A.1.4.5 |
| Data protection by design (Art. 46, 49) | A.1.4.2–A.1.4.10 |
| Security measures (Art. 46) | A.3 (security controls) |
| DPA / operator contracts (Art. 37–40) | A.1.2.7, A.2 |
| Incident notification (Art. 48) | A.3.11, A.3.12 |
| International transfers (Art. 33–36) | A.1.5.2–A.1.5.5 |
| DPO (Encarregado) appointment (Art. 41) | Clause 5 (roles and responsibilities) |

---

## PIPEDA (Canada)

Canada's Personal Information Protection and Electronic Documents Act (PIPEDA) is
structured around 10 Fair Information Principles. ISO 27701:2025 aligns well.

| PIPEDA Principle | ISO 27701:2025 Controls |
|-----------------|------------------------|
| 1. Accountability | Clause 5 (leadership), management review, SoA |
| 2. Identifying purposes | A.1.2.2, A.1.2.9 |
| 3. Consent | A.1.2.3, A.1.2.4, A.1.2.5 |
| 4. Limiting collection | A.1.4.2, A.1.4.5 |
| 5. Limiting use, disclosure, retention | A.1.4.3, A.1.4.8, A.1.5.4 |
| 6. Accuracy | A.1.4.4, A.1.3.7 |
| 7. Safeguards | A.3 (security controls) |
| 8. Openness | A.1.3.3, A.1.3.4 |
| 9. Individual access | A.1.3.9, A.1.3.10 |
| 10. Challenging compliance | A.1.3.10 (handling requests), Clause 10 |

**Note**: Canada's Bill C-27 (Consumer Privacy Protection Act — CPPA) will replace
PIPEDA when enacted. ISO 27701:2025 alignment will carry over as CPPA shares GDPR-
influenced principles.

---

## PDPA (Singapore) and PDPA (Thailand)

Both PDPAs are GDPR-influenced and align well with ISO 27701:2025.

**Singapore PDPA key mappings:**
| Singapore PDPA Obligation | ISO 27701:2025 Controls |
|--------------------------|------------------------|
| Consent obligation | A.1.2.3, A.1.2.4, A.1.2.5 |
| Purpose limitation | A.1.2.2, A.1.4.3 |
| Notification obligation | A.1.3.3, A.1.3.4 |
| Access and correction obligations | A.1.3.9, A.1.3.7 |
| Accuracy obligation | A.1.4.4 |
| Protection obligation | A.3 (security controls) |
| Retention limitation | A.1.4.8, A.1.4.9 |
| Transfer limitation | A.1.5.2–A.1.5.5 |
| Data breach notification | A.3.11, A.3.12 |

**Thailand PDPA** follows a similar structure to EU GDPR and Singapore PDPA.
The same control mappings apply.

---

## ISO 27001:2022 Integration

ISO 27701:2025 is designed to work alongside ISO 27001:2022 even though it no longer
requires it. When implementing both:

- A.3 security controls can reference the organization's ISO 27001 ISMS controls
  directly — no need to implement security controls twice
- The ISO 27001 SoA and PIMS SoA can be maintained as separate documents or as a
  combined document with role-based tabs
- Risk assessments can be linked: ISMS risk assessment focuses on security risks;
  PIMS risk assessment focuses on harm to PII principals
- Internal audits can be combined for efficiency if scoped correctly
- Management reviews can be combined with a dedicated privacy section

**Key integration points:**
| ISO 27701 Requirement | ISO 27001 Evidence That Can Be Referenced |
|----------------------|------------------------------------------|
| A.3.3 (IS Policies) | IS Policy (ISO 27001 Clause 5.2) |
| A.3.9 (Access Rights) | Access control policy and records (A.5.15–5.18) |
| A.3.11–A.3.12 (Incidents) | Incident response policy and records (A.5.24–5.28) |
| A.3.26 (Cryptography) | Cryptography policy (A.8.24) |
| A.3.27 (Secure SDLC) | Secure development policy (A.8.25–8.32) |
| A.3.25 (Logging) | Logging and monitoring controls (A.8.15–8.16) |

---

## Framework Comparison Summary

| Framework | Geographic Scope | Legally Binding? | ISO 27701 Alignment |
|-----------|-----------------|-----------------|---------------------|
| GDPR | EU/EEA | Yes — mandatory law | Excellent (dedicated correspondence annex) |
| UK GDPR | United Kingdom | Yes — mandatory law | Excellent (same as EU GDPR) |
| CCPA/CPRA | California, USA | Yes — mandatory law | Good (most rights and obligations covered) |
| LGPD | Brazil | Yes — mandatory law | Excellent (closely mirrors GDPR) |
| PIPEDA | Canada | Yes — mandatory law | Good (principles-based alignment) |
| PDPA (Singapore) | Singapore | Yes — mandatory law | Good |
| PDPA (Thailand) | Thailand | Yes — mandatory law | Good |
| ISO 27001:2022 | Global | Voluntary standard | Direct integration supported |
