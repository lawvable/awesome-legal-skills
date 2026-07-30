# DACH-Specific Considerations — Germany, Austria, Switzerland

## Table of Contents

1. [Germany — Overview](#1-germany--overview)
2. [Works Council Co-Determination (BetrVG)](#2-works-council-co-determination-betrvg)
3. [BaFin — Financial Services AI](#3-bafin--financial-services-ai)
4. [BSI — IT Security and Critical Infrastructure](#4-bsi--it-security-and-critical-infrastructure)
5. [BNetzA — Market Surveillance](#5-bnetza--market-surveillance-authority)
6. [Data Protection Overlay (DSGVO/BDSG)](#6-data-protection-overlay-dsgvobdsg)
7. [Sector-Specific Overlaps](#7-sector-specific-overlaps-germany)
8. [Austria — Key Differences](#8-austria--key-differences)
9. [Switzerland — Non-EU but Relevant](#9-switzerland--non-eu-but-relevant)
10. [Practical DACH Compliance Checklist](#10-practical-dach-compliance-checklist)

---

## 1. Germany — Overview

Germany has the largest AI deployment base in the DACH region and the most complex regulatory overlay. Key factors:

- **Strong works council rights** — most AI in employment contexts triggers co-determination
- **BaFin scrutiny** — AI in financial services faces model risk management expectations
- **BSI alignment** — cybersecurity requirements for AI in critical infrastructure
- **BNetzA designated as market surveillance authority** for AI systems (alongside sector-specific authorities)
- **Robust data protection enforcement** — Landesdatenschutzbehörden actively enforce

---

## 2. Works Council Co-Determination (BetrVG)

### Why This Matters

In Germany, virtually every AI system deployed in an employment context triggers works council (Betriebsrat) rights. Failing to involve the works council can render the deployment unlawful — independently of AI Act compliance.

### Relevant Provisions

**§87(1) No. 6 BetrVG — Technical monitoring:**
Co-determination right regarding the introduction and use of technical devices designed to monitor employee behaviour or performance.

- **Extremely broad interpretation by courts:** Covers any system that is *objectively capable* of monitoring, even if monitoring is not the intended purpose
- AI systems processing any employee data almost always trigger this
- Applies to: productivity analytics, attendance tracking, communication monitoring, task allocation systems, performance scoring

**§87(1) No. 1 BetrVG — Workplace conduct:**
May be triggered by AI systems that set behavioural rules or expectations (e.g., algorithmic task allocation with deadlines).

**§94 BetrVG — Personnel questionnaires and assessment principles:**
If the AI system effectively creates an evaluation framework for employees, works council co-determination applies.

**§95 BetrVG — Selection guidelines:**
If AI is used for hiring, promotions, transfers, or dismissals, the works council has co-determination rights over selection guidelines.

### Practical Steps

1. **Identify early:** Map all AI systems touching employee data to BetrVG triggers
2. **Involve works council before deployment** — not after. Late involvement can force rollback.
3. **Prepare a transparent system description:**
   - Purpose and function of the AI system
   - Data categories processed
   - How decisions/recommendations are generated
   - What human oversight exists
   - Purpose limitations and data retention
4. **Negotiate a Betriebsvereinbarung (works agreement):**
   - Scope and purpose limitations
   - Data processing details
   - Employee rights (access, objection, explanation)
   - Review and audit rights for the works council
   - Sunset/review clause
5. **Coordinate with DPO and IT security** — the Betriebsvereinbarung often also serves as a GDPR legal basis (Art. 88 GDPR / §26 BDSG)

### Common Pitfalls

- Deploying a "pilot" without works council involvement → the pilot is already subject to co-determination
- Assuming cloud-based AI tools are exempt → they are not; it's about the function, not the hosting
- Claiming the system "doesn't monitor" → if it's technically capable of monitoring, it triggers §87(1) No. 6

---

## 3. BaFin — Financial Services AI

### Regulatory Context

BaFin (Bundesanstalt für Finanzdienstleistungsaufsicht) supervises AI use in banking, insurance, and securities. Key expectations:

**MaRisk (Mindestanforderungen an das Risikomanagement):**
- Model risk management requirements apply to AI/ML models used in risk-relevant decisions
- Validation, monitoring, and governance requirements for all material models

**VAIT/BAIT/KAIT (IT supervisory requirements):**
- IT governance, information security, and outsourcing requirements apply to AI infrastructure
- Cloud-based AI services are subject to outsourcing rules

**DORA (Digital Operational Resilience Act):**
- ICT risk management requirements overlap with AI Act Article 15 (robustness, cybersecurity)
- Third-party ICT provider oversight applies to GPAI providers

### AI-Specific Expectations

- **Explainability:** BaFin expects that AI-driven decisions in regulated areas (credit, insurance, AML) can be explained to supervisors and, where required, to customers
- **Model validation:** Independent validation of AI models used in risk-sensitive processes
- **Audit trails:** Complete documentation of model development, validation, and ongoing performance
- **Bias monitoring:** Particularly for credit scoring and insurance pricing (discrimination law overlay)

### Practical Steps

- [ ] Map AI systems to BaFin-relevant processes (credit decisions, risk management, AML/KYC, insurance pricing)
- [ ] Ensure model risk management documentation meets MaRisk standards
- [ ] Implement explainability mechanisms appropriate to the use case
- [ ] Establish independent model validation for material AI models
- [ ] Document AI models in the IT inventory per BAIT/VAIT
- [ ] Address cloud/outsourcing requirements for external AI services

---

## 4. BSI — IT Security and Critical Infrastructure

### Regulatory Context

BSI (Bundesamt für Sicherheit in der Informationstechnik) sets IT security standards and oversees critical infrastructure operators.

**BSI-Gesetz and BSI-Kritisverordnung:**
- KRITIS operators must implement state-of-the-art IT security measures
- AI systems in KRITIS environments must meet these baseline security requirements

**IT-Grundschutz:**
- BSI's IT-Grundschutz framework provides security baselines that should inform AI Act Article 15 (cybersecurity) compliance
- Mapping AI-specific controls to IT-Grundschutz catalogues provides defensible evidence

**NIS2 Directive (transposed into German law):**
- Broader scope than KRITIS — covers "important" and "essential" entities
- IT security measures include AI systems within scope

### AI Security Alignment

Map AI Act Article 15 requirements to BSI standards:

| AI Act Requirement (Art. 15) | BSI Alignment |
|------------------------------|---------------|
| Cybersecurity measures | IT-Grundschutz baseline + sector-specific requirements |
| Resilience against attacks | Adversarial robustness testing, penetration testing |
| Unauthorised access prevention | Access management per IT-Grundschutz |
| Logging integrity | BSI log management standards |
| Incident response | KRITIS/NIS2 incident reporting + Art. 73 AI Act |

### Practical Steps

- [ ] Map AI systems to KRITIS/NIS2 scope
- [ ] Align AI security controls with IT-Grundschutz
- [ ] Conduct AI-specific threat modelling (adversarial attacks, data poisoning, model extraction)
- [ ] Integrate AI incident response with KRITIS/NIS2 reporting obligations
- [ ] Document security measures in both AI Act technical documentation and ISMS

---

## 5. BNetzA — Market Surveillance Authority

### Role Under the AI Act

The Bundesnetzagentur (Federal Network Agency) has been designated as a market surveillance authority for AI systems in Germany (alongside sector-specific authorities like BaFin for financial services).

**Responsibilities:**
- Market surveillance for AI systems placed on the German market
- Enforcement of AI Act requirements
- Cooperation with the EU AI Office and other national authorities
- Handling complaints about AI systems

### What This Means in Practice

- **Compliance inspections:** BNetzA may request technical documentation, conformity assessments, and evidence of compliance
- **Corrective measures:** Can order modifications, withdrawal, or recall of non-compliant AI systems
- **Reporting:** Market surveillance actions and outcomes will be reported to the EU AI Office
- **Contact point:** BNetzA serves as the primary AI Act contact for many market participants in Germany

### Practical Steps

- [ ] Register high-risk AI systems in the EU database (visible to BNetzA)
- [ ] Prepare compliance evidence packs accessible on request
- [ ] Establish internal contact point for market surveillance inquiries
- [ ] Monitor BNetzA guidance and publications on AI Act interpretation

---

## 6. Data Protection Overlay (DSGVO/BDSG)

### Parallel Obligations

The AI Act does not replace GDPR. In Germany, both DSGVO (GDPR) and BDSG create additional requirements:

**Key overlaps:**
- **Art. 22 GDPR (automated decision-making):** Prohibition on purely automated decisions with legal or significant effects — overlaps with AI Act human oversight requirements but is broader
- **Art. 35 GDPR (DPIA):** Data protection impact assessment required for high-risk processing — should be coordinated with AI Act risk management
- **§26 BDSG (employee data):** Employment-specific data processing rules complement works council rights
- **Art. 9 GDPR (special category data):** Processing biometric data, health data, etc. requires explicit legal basis — intersects with AI Act biometric provisions

**Practical integration:**
- Conduct DPIA and AI Act risk assessment in parallel (shared evidence base)
- Coordinate GDPR Art. 22 safeguards with AI Act human oversight requirements
- Map GDPR legal bases for AI training data to AI Act data governance requirements
- Align transparency obligations (GDPR Arts. 13–14 + AI Act Arts. 13, 50)

---

## 7. Sector-Specific Overlaps (Germany)

### Healthcare (SGB V, MDR)

- AI medical devices regulated under MDR + AI Act (Annex I)
- Gemeinsamer Bundesausschuss (G-BA) may set additional requirements for reimbursement
- DiGA (Digital Health Applications) fast-track has its own evidence requirements

### Insurance (VAG, Solvency II)

- BaFin supervises AI in insurance pricing and underwriting
- Discrimination law (AGG) constrains AI-driven risk differentiation
- AI Act high-risk classification for life/health insurance pricing (Annex III, category 5)

### Public Sector (VwVfG)

- §35a VwVfG: Fully automated administrative acts possible only where statute allows
- AI supporting administrative decisions must ensure lawful exercise of discretion
- Particular FRIA obligations for public deployers

### Telecommunications

- BNetzA dual role: telecom regulator + AI market surveillance
- AI in network management may be critical infrastructure (Annex III, category 2)

---

## 8. Austria — Key Differences

### Market Surveillance

- Austria designating its own national competent authority (implementation ongoing)
- RTR (Rundfunk und Telekom Regulierungs-GmbH) likely to have a role

### Works Council

- ArbVG (Arbeitsverfassungsgesetz) §96a: Works council consultation right for systems processing personal employee data
- Similar to German BetrVG but different procedural requirements
- Betriebsvereinbarung also common tool for AI deployment governance

### Data Protection

- DSB (Datenschutzbehörde) enforcement of GDPR
- Austrian DSGVO implementation with some national specificities
- Coordinate AI Act and GDPR compliance per Austrian practice

---

## 9. Switzerland — Non-EU but Relevant

### Territorial Scope

Switzerland is not in the EU, but the AI Act applies when:
- AI systems are placed on the EU market (including from Swiss providers)
- Output of AI systems is used in the EU
- Swiss companies deploying AI affecting EU individuals

### Practical Implications

- Swiss companies selling AI into the EU must comply as providers
- Swiss companies using AI that affects EU data subjects should assess deployer obligations
- **No equivalence framework** (unlike GDPR adequacy) — AI Act compliance is direct
- Swiss companies may need an EU authorised representative

### Swiss National Context

- Switzerland developing its own AI governance approach (currently principles-based)
- FINMA (financial regulator) has AI expectations analogous to BaFin
- Swiss DPA (FDPIC) enforces nDSG with AI-relevant provisions
- No equivalent of works council co-determination (different labour law framework)

---

## 10. Practical DACH Compliance Checklist

For each AI system deployed in the DACH region:

### Germany
- [ ] AI Act classification completed
- [ ] Works council involvement assessed (BetrVG §87, §94, §95)
- [ ] Betriebsvereinbarung negotiated where required
- [ ] DSGVO/BDSG compliance (DPIA, Art. 22, legal basis for training data)
- [ ] BaFin requirements mapped (if financial services)
- [ ] BSI/IT-Grundschutz alignment (if KRITIS or high-security)
- [ ] BNetzA registration and compliance evidence prepared
- [ ] Sector-specific requirements identified (MDR, VAG, VwVfG, etc.)

### Austria
- [ ] AI Act classification completed
- [ ] ArbVG §96a works council consultation assessed
- [ ] Austrian GDPR implementation specifics addressed
- [ ] National competent authority monitoring

### Switzerland
- [ ] Territorial scope assessment (does the AI Act apply?)
- [ ] If yes: full AI Act compliance as provider/deployer
- [ ] EU authorised representative appointed if required
- [ ] FINMA requirements mapped (if financial services)
- [ ] nDSG compliance coordinated with AI Act
