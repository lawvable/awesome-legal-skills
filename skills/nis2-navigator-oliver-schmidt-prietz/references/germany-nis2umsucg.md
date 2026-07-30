# German NIS2 Implementation — BSIG-neu / NIS2UmsuCG

## Legislative Status

**In force since 6 December 2025.** No transition periods.

- Bundestag passed NIS2UmsuCG: 13 November 2025
- Bundesrat approved: 21 November 2025
- Published in Bundesgesetzblatt: 5 December 2025
- Entry into force: 6 December 2025
- BSI portal (MUK) launched: 6 January 2026
- BSI registration deadline: 6 March 2026 (passed — late registration still possible and urgent)
- Nachweispflicht for besonders wichtige Einrichtungen: by December 2028

---

## Key § References (BSIG-neu)

| Topic | Provision | Equivalent in Directive |
|-------|-----------|----------------------|
| Definitions & scope | § 28 BSIG | Art. 2, 3 |
| Besonders wichtige Einrichtungen | § 28(1) BSIG | "Essential entities" Art. 3(1) |
| Wichtige Einrichtungen | § 28(2) BSIG | "Important entities" Art. 3(2) |
| Risk management measures | § 30 BSIG | Art. 21 |
| Incident reporting | § 32 BSIG | Art. 23 |
| Registration obligation | § 33 BSIG | Art. 3(3)-(4) |
| Nachweispflicht (proof of compliance) | § 34 BSIG | Art. 21(5) — DE goes further |
| Supervisory powers — besonders wichtig | § 35 BSIG | Art. 32 |
| Supervisory powers — wichtig | § 36 BSIG | Art. 33 |
| Management body obligations | § 38 BSIG | Art. 20 |
| Enforcement / fines | § 60 BSIG | Art. 34-36 |

---

## BSI Registration

### Portal & Process
- Portal: **muk.bsi.bund.de** (Mein Unternehmenskonto)
- Prerequisite: ELSTER-Organisationszertifikat
- Registration includes: Stammdaten, sector assignment (Sektorzuordnung), contact person (Kontaktstelle)
- Deadline: 6 March 2026 (3 months after entry into force) — **already passed**

### Required Information
- Organization name, address, legal form
- Sector and sub-sector classification
- Whether besonders wichtig or wichtig
- Designated contact person (24/7 reachable for incident reporting)
- IP ranges and domain names used for service provision

### Late Registration
Late registration is still possible and should be done immediately. Failure to register is independently sanctionable (§ 60 BSIG — Bußgeld). The BSI is expected to prioritize enforcement against entities that are neither registered nor have demonstrable compliance measures.

---

## § 30 BSIG — Risk Management Measures

The 10 measures in § 30(2) BSIG mirror Art. 21(2)(a)-(j) of the Directive. The German text uses "geeignete, verhältnismäßige und wirksame technische und organisatorische Maßnahmen" (appropriate, proportionate, and effective technical and organizational measures).

Key German-specific nuances:
- The measures must be implemented considering the "Stand der Technik" (state of the art) — § 30(1) BSIG
- Proportionality is assessed relative to: entity size, likelihood and severity of incidents, societal and economic impact of potential disruption
- § 30(3) BSIG: The BSI may issue sector-specific guidance ("Branchenspezifische Sicherheitsstandards") that can be used to demonstrate compliance. Check BSI website for published B3S.
- § 30(4) BSIG: Entities can propose sector-specific security standards to BSI for recognition

### B3S (Branchenspezifische Sicherheitsstandards)
Industry associations can develop and submit sector-specific security standards to the BSI. Where a recognized B3S exists for the entity's sector, it provides a concrete implementation blueprint and creates a rebuttable presumption of compliance if followed. Check current status at www.bsi.bund.de.

---

## § 32 BSIG — Incident Reporting

### Reporting Cascade

| Timeline | Report type | Content |
|----------|------------|---------|
| **≤ 24 hours** | Erstmeldung (initial notification) | Preliminary information: suspected incident, initial assessment, whether cross-border impact suspected |
| **≤ 72 hours** | Bestätigungsmeldung (confirming report) | Updated assessment, severity, impact, indicators of compromise if available |
| **≤ 1 month** | Abschlussbericht (final report) | Detailed incident description, root cause, mitigation measures taken, cross-border impact if applicable |

- Reporting goes to the **BSI** (not DPAs — those are for GDPR Art. 33)

### Reporting Channels (important distinction)

The correct reporting channel depends on the entity's registration and classification status:

| Entity status | Channel |
|--------------|---------|
| wE/bwE, already registered at BSI-Portal | BSI-Portal (portal.bsi.bund.de) |
| wE/bwE, NOT yet registered | MIP (Melde- und Informationsportal) |
| KRITIS operators | MIP (Melde- und Informationsportal) |

Ensure the entity knows which channel applies to them and has access credentials set up before an incident occurs.

### Dual reporting with GDPR
- Reporting via BSI-Portal (muk.bsi.bund.de) — entities not yet registered can use the temporary online form
- "Erheblicher Sicherheitsvorfall" (significant security incident) — threshold: incident that has or could have significant impact on service provision

### Interaction with GDPR Breach Notification
A single security incident may trigger both NIS2 and GDPR notification obligations:
- NIS2 → BSI (24h/72h/1 month)
- GDPR → Competent DPA (72h under Art. 33 GDPR)
- The timelines and recipients are different — ensure processes cover both
- If using Breach Sentinel skill: the NIS2 reporting obligation is a separate, parallel track

---

## § 38 BSIG — Management Body Obligations

### Training Requirement
- Management bodies ("Geschäftsleitungen") of besonders wichtige AND wichtige Einrichtungen must regularly undergo cybersecurity training (§ 38(3) BSIG)
- Training must be sufficient to identify risks, assess risk management practices, and understand their impact on services
- This is not delegable — the actual management body members must personally participate

### Approval of Measures
- Management body must approve the risk management measures under § 30 BSIG (§ 38(1))
- Must oversee their implementation
- Cannot fully delegate this to CISO/IT — oversight responsibility remains with management body

### Personal Liability
- **§ 38(2) BSIG creates explicit personal liability** of management body members for damages arising from failure to fulfill § 30 obligations
- This is a German addition — many other Member States have not implemented such explicit personal liability
- The liability applies to the management body members personally, not just to the entity
- This provision is a powerful argument for securing management engagement and budget

### Practical Implications
- The BSI explicitly recommends appointing at least 2 persons to coordinate information security within the organization — this is a practical prerequisite for meeting § 30 obligations
- Document management body training (dates, topics, attendees)
- Document management body approval of risk management measures
- Establish regular management reporting cadence on cybersecurity posture
- Consider D&O insurance coverage for NIS2 liability

---

## § 34 BSIG — Nachweispflicht (Proof of Compliance)

### Who and When
- Applies to **besonders wichtige Einrichtungen** only (not wichtige Einrichtungen)
- Must provide evidence of compliance to BSI within **3 years** of entry into force → **deadline: December 2028**
- Evidence can include: audits, certifications, security assessments

### Accepted Evidence
- ISO 27001 certification (if scope covers NIS2-relevant systems and processes)
- BSI IT-Grundschutz certification
- Sector-specific certifications (B3S-based)
- Audit reports from qualified auditors
- Self-assessments may not be sufficient alone for besonders wichtige Einrichtungen

### Practical Recommendation
Start planning the Nachweis path early:
- If ISO 27001 certified → verify scope alignment with NIS2 obligations
- If not certified → consider whether to pursue certification (efficient for Nachweispflicht) or compile evidence through alternative means
- Budget for audit/certification costs
- Timeline: begin preparation no later than mid-2027 to meet December 2028 deadline

---

## Enforcement & Sanctions (§ 60 BSIG)

### Fines

| Entity category | Maximum fine |
|----------------|-------------|
| Besonders wichtige Einrichtungen | €10M or 2% of worldwide annual turnover (whichever is higher) |
| Wichtige Einrichtungen | €7M or 1.4% of worldwide annual turnover (whichever is higher) |

### Supervisory Approach
- **Besonders wichtige Einrichtungen (§ 35):** Proactive supervision — BSI can conduct audits, inspections, on-site investigations, request evidence, issue binding instructions
- **Wichtige Einrichtungen (§ 36):** Reactive supervision — BSI acts on evidence of non-compliance, incident reports, or third-party information
- BSI can issue Anordnungen (binding orders) requiring specific remediation measures with deadlines
- In extreme cases: BSI can prohibit persons from exercising management functions (temporary management ban)

### Expected BSI Enforcement Priorities (2026)
Based on publicly available BSI guidance, expected early enforcement focus:
1. Entities that have not registered (most visible non-compliance)
2. Entities that fail to report significant incidents
3. Entities with no demonstrable risk management measures
4. KRITIS operators who were already regulated — higher expectations for immediate compliance

---

## KRITIS-Dachgesetz Interaction

The KRITIS-Dachgesetz (CER Directive implementation) addresses physical resilience of critical infrastructure and is separate from NIS2/BSIG-neu. Key points:

- KRITIS-Dachgesetz covers physical security; BSIG-neu covers cybersecurity
- KRITIS operators are automatically besonders wichtige Einrichtungen under BSIG-neu
- Some entities may be subject to both KRITIS-Dachgesetz (physical resilience) and BSIG-neu (cyber resilience)
- The KRITIS-Dachgesetz **entered into force on 17 March 2026** — track separately

---

## DORA Interaction (Financial Sector)

For financial sector entities, the Digital Operational Resilience Act (DORA, Regulation (EU) 2022/2554) acts as lex specialis to NIS2:

- Financial entities subject to DORA are excluded from NIS2 Art. 21 (risk management measures) and Art. 23 (incident reporting)
- However, NIS2 cooperation and information-sharing provisions still apply
- ICT third-party service providers to financial entities remain under NIS2 unless themselves financial entities
- The BSI's #nis2know Infopaket "DORA und NIS-2" provides German-specific guidance on the interaction
- Commission Guidelines on NIS2/DORA relationship (September 2023) clarify the Article 4 lex specialis rule

---

## Pending: Commission NIS2 Amendment Proposal (January 2026)

On 20 January 2026, the Commission proposed targeted amendments to NIS2. These are NOT yet in force but should be monitored as they signal the direction of travel:

**Key proposed changes:**
- **Certification-based compliance**: EU cybersecurity certification schemes could serve as evidence of Art. 21 compliance
- **New small midcap category**: To reduce compliance burden for smaller entities
- **Scope clarifications**: Electricity (>1MW threshold), healthcare, hydrogen, chemicals
- **Expanded scope**: Digital/business wallet providers, submarine infrastructure operators, dual-use infrastructure
- **Harmonized supply chain guidance**: EU-level guidance on the level of detail for supplier questionnaires, reducing cascading burden
- **Enhanced ransomware reporting**: Specific data points (attack vector, ransom demands, payments) reportable to authorities
- **Maximum harmonization for implementing acts**: Where Commission adopts implementing acts under Art. 21, Member States cannot impose additional technical requirements

**Timeline:** Expected adoption late 2026 or 2027, then 12-month transposition into national law

**Practical advice:** These amendments do not change current obligations. Entities should comply with the BSIG-neu as currently in force. However, awareness of the proposed changes is valuable for strategic planning, particularly regarding certification pathways and supply chain simplification.
