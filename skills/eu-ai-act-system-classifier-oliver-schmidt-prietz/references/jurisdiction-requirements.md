# Jurisdiction-Specific Requirements for AI Act Classification

Extracted from the cross-jurisdictional regulatory landscape reference. Covers national authorities, employment law overlay, selected financial regulators, and critical infrastructure requirements relevant to AI classification decisions.

**Last verified:** March 2026. Always search for latest national implementation status.

---

## 2. National Competent Authorities Matrix

| Dimension | DE | AT | CH | FR | NL | IT | ES |
|-----------|----|----|----|----|----|----|-----|
| **Designated AI Authority** | BNetzA (Bundesnetzagentur) — designated as market surveillance authority for AI | BMK (Bundesministerium für Klimaschutz) — coordination; specific authority designation pending | N/A (non-EU; voluntary alignment via bilateral agreements) | DGE (Direction Générale des Entreprises, Ministry of Economy) — coordinating role | RDI (Rijksinspectie Digitale Infrastructuur) — lead authority expected | AgID (Agenzia per l'Italia Digitale) + ACN (Agenzia per la Cybersicurezza Nazionale) — dual-authority model | SEDIA (Secretaría de Estado de Digitalización e Inteligencia Artificial) — coordinating; AESIA operational |
| **Market Surveillance** | BNetzA + sector-specific authorities (BaFin for finance, BfArM for medical devices) | Sector-specific authorities under existing product safety legislation | SECO (Staatssekretariat für Wirtschaft) for product safety; no AI-specific mandate | DGCCRF (Direction Générale de la Concurrence) — consumer product safety + sector authorities | NVWA + sector inspectorates + RDI | MISE (Ministry of Economic Development) market surveillance authorities | AESIA (Agencia Española de Supervisión de Inteligencia Artificial) — created by RD 729/2023 |
| **Notifying Authority** | DAkkS (Deutsche Akkreditierungsstelle) — accreditation of conformity assessment bodies | AA (Akkreditierung Austria) | SAS (Schweizerische Akkreditierungsstelle) | COFRAC (Comité Français d'Accréditation) | RvA (Raad voor Accreditatie) | ACCREDIA (Ente Italiano di Accreditamento) | ENAC (Entidad Nacional de Acreditación) |
| **National AI Strategy Body** | BMBF (AI Strategy) + Plattform Lernende Systeme | AIT (Austrian Institute of Technology) advisory role | SATW (Schweizerische Akademie der Technischen Wissenschaften) + BAKOM | CNNUM (Conseil National du Numérique) + INRIA | AINed (national AI coalition) + NLAIC | Comitato Interministeriale per la Transizione Digitale | Plan Nacional de IA + ENIA (Estrategia Nacional de IA) |
| **AI Sandbox** | Planned — BNetzA coordination | Under development with BMK | Not applicable (non-EU framework) | Operational since 2021 (CNIL data protection sandbox; AI-specific sandbox under PFIA) | Under development (with ACM/AP/AFM collaboration) | Under development with AgID | Operational — AESIA regulatory sandbox (one of first in EU, launched 2022) |
| **Implementation Legislation Status** | Draft AI Act implementation law (KI-Durchführungsgesetz) in preparation — expected 2026 | In preparation; awaiting EU implementing acts for detailed provisions | No direct implementation required; bilateral MRA discussions for market access | Implementation via existing regulatory framework + decree; Senate report Dec 2024 on AI Act readiness | Implementation via existing frameworks; adaptation of specific sectoral laws | Legislative decree under preparation; national AI strategy updated Jan 2025 | RD-ley 729/2023 pre-positioned AESIA; full implementation legislation in preparation |

### Key Observations

- **Spain (AESIA)** is the most advanced — operational supervisory agency since 2023, regulatory sandbox active
- **Germany (BNetzA)** confirmed as market surveillance lead, but implementation law still pending
- **France** leverages existing institutional capacity (CNIL, DGCCRF) rather than creating new authority
- **Switzerland** is outside the EU but relevant for organizations deploying cross-border; voluntary alignment for market access
- **Italy** chose dual-authority model splitting digital (AgID) and cybersecurity (ACN) responsibilities

---

## 3. Employment & Labor Law Overlay

AI systems in the workplace face a **dual regulatory layer**: EU AI Act obligations plus national employment law requirements that often go further.

### 3.1 Germany — BetrVG Co-Determination

**Primary legislation:** Betriebsverfassungsgesetz (BetrVG) — Works Constitution Act

**Critical provisions:**

| BetrVG Section | Requirement | AI Relevance | Co-Determination Type |
|----------------|-------------|--------------|----------------------|
| **§87(1) Nr. 6** | Co-determination on technical monitoring devices | Any AI system that can monitor employee behavior or performance | **Mandatory co-determination** — employer cannot introduce without works council consent |
| **§87(1) Nr. 7** | Health and safety measures | AI systems affecting work pace, ergonomics, stress | Mandatory co-determination |
| **§90** | Notification on workplace changes | Introduction of AI systems changing work processes | Information + consultation (not consent) |
| **§94** | Personnel questionnaires | AI-based assessment criteria for employees | Mandatory co-determination on content |
| **§95** | Selection guidelines | AI-driven recruitment, promotion, or termination criteria | Mandatory co-determination |
| **§111** | Operational changes | Large-scale AI deployment replacing jobs | Negotiation of social plan (Sozialplan) |

**Practical steps for BetrVG compliance:**

1. **Early works council involvement:** Notify before procurement decision, not after deployment
2. **Betriebsvereinbarung (works agreement):** Negotiate written agreement covering:
   - Scope: which AI systems, which employee data
   - Purpose limitation: what the AI may and may not be used for
   - Transparency: how employees are informed about AI use
   - Human oversight: when and how human review occurs
   - Data retention: alignment with GDPR Art. 17 and AI Act Art. 26(6)
   - Dispute resolution: process for challenging AI-based decisions
3. **Technical expert (§80(3)):** Works council may engage external experts at employer expense to assess AI systems
4. **Einigungsstelle (conciliation board):** If no agreement reached, binding arbitration — can block deployment

**Common pitfalls in practice:**
- Deploying AI "as a pilot" without works council consultation — co-determination applies from day one
- Claiming AI is not a "monitoring device" because monitoring is not its primary purpose — §87(1) Nr. 6 applies whenever monitoring is technically *possible*, not only when intended
- Using provider's standard configuration without works council review — configuration parameters themselves may require co-determination
- Failing to update Betriebsvereinbarung when AI system is updated or retrained

### 3.2 Austria — ArbVG Consultation Rights

**Primary legislation:** Arbeitsverfassungsgesetz (ArbVG) — Labor Constitution Act

| ArbVG Section | Requirement | AI Relevance |
|---------------|-------------|--------------|
| **§96(1) Nr. 3** | Works council consent for systems that affect human dignity | AI monitoring, profiling, automated evaluation systems |
| **§96a(1) Nr. 1** | Consent for processing of employee personal data | AI systems processing employee data |
| **§91(2)** | Information on planned changes | Introduction of new AI technology |
| **§92a** | Proposal rights on employment security | AI-driven automation affecting jobs |

**Key difference from Germany:** Austrian law explicitly ties co-determination to *human dignity* (Menschenwürde), creating a broader trigger than the German technical monitoring device formulation. Any AI system that could affect employee dignity requires works council consent.

### 3.3 Switzerland — OR/ArG Framework

**Primary legislation:** Obligationenrecht (OR) + Arbeitsgesetz (ArG)

| Provision | Requirement | AI Relevance |
|-----------|-------------|--------------|
| **OR Art. 328** | Employer duty to protect employee personality rights | Limits on employee surveillance and profiling |
| **OR Art. 328b** | Data processing limited to employment relationship suitability | Purpose limitation for employee AI data |
| **ArG Art. 6** | Health protection, including psychological health | AI systems affecting work pace or stress |
| **DSG Art. 21** (nDSG) | Automated individual decisions — right to human review | Employee right to contest AI decisions |

**Key difference:** No co-determination equivalent. Swiss law provides *information rights* and personality protection but no works council consent mechanism. The new Data Protection Act (nDSG/revDSG, in force since 1 September 2023) adds automated decision-making protections that partially compensate.

### 3.4 France — Code du Travail

**Primary legislation:** Code du Travail (Labor Code)

| Provision | Requirement | AI Relevance |
|-----------|-------------|--------------|
| **L. 2312-38** | CSE (Comité Social et Économique) must be consulted on introduction of new technology | AI system deployment requires prior consultation |
| **L. 2312-37** | CSE information on technology introduction plans | Employer must provide detailed information on AI systems |
| **L. 1222-4** | Employee monitoring transparency | Employees must be informed before monitoring, including AI-based |
| **L. 1121-1** | Proportionality of employee restrictions | AI monitoring must be proportionate to legitimate aim |
| **L. 1222-3** | Prior employee notification of monitoring methods | AI-based evaluation methods must be communicated |

**Platform workers (L. 7342-8 et seq., strengthened by Loi du 21 juin 2023):** Algorithmic management transparency requirements — platform workers have right to meaningful explanation of algorithmic decisions affecting their activity allocation, pricing, and account status.

### 3.5 Netherlands — WOR (Wet op de Ondernemingsraden)

**Primary legislation:** Works Councils Act (WOR)

| Provision | Requirement | AI Relevance |
|-----------|-------------|--------------|
| **Art. 27(1)(l)** | Works council consent for employee monitoring systems | AI-based monitoring, performance tracking |
| **Art. 27(1)(k)** | Consent for personnel registration systems | AI systems recording employee data |
| **Art. 25(1)(k)** | Advisory right on major technology changes | Introduction of AI systems significantly affecting employees |
| **Art. 31(1)** | General information right | Right to information on AI systems used in workplace |

**Key strength:** Dutch works councils have explicit **consent rights** (instemmingsrecht) for monitoring technology. The employer cannot introduce AI monitoring without works council agreement, similar to German co-determination.

**AP (Autoriteit Persoonsgegevens) — Data Protection Authority:** Has published specific guidance on algorithms in the workplace, including a practical framework for assessing algorithmic systems (Toetsingskader Algoritmes).

### 3.6 Italy — Statuto dei Lavoratori

**Primary legislation:** Legge 300/1970 (Statuto dei Lavoratori — Workers' Statute)

| Provision | Requirement | AI Relevance |
|-----------|-------------|--------------|
| **Art. 4 (as amended by D.Lgs. 151/2015)** | Remote monitoring restrictions — employer may only use remote monitoring systems for: (1) organizational/production needs, (2) workplace safety, (3) asset protection | AI monitoring systems must fit one of these justifications; prior agreement with trade union or authorization from labor inspectorate (Ispettorato del Lavoro) required |
| **Art. 8** | Prohibition on investigating employee opinions | AI may not be used to infer political, religious, or trade union opinions |
| **D.Lgs. 104/2022 (Decreto Trasparenza)** | Employer must inform employees about automated decision-making or monitoring systems | Specific disclosure requirements for AI systems affecting employment |

**Critical for AI deployers:** Art. 4 requires either a **trade union agreement** (accordo sindacale) or **labor inspectorate authorization** before deploying any AI monitoring system. Penalty for violation: criminal sanctions (contravvenzione).

### 3.7 Spain — Estatuto de los Trabajadores + Platform Worker Rules

**Primary legislation:** Estatuto de los Trabajadores (ET) + Real Decreto-ley 9/2021

| Provision | Requirement | AI Relevance |
|-----------|-------------|--------------|
| **ET Art. 64(4)(d)** | Works council information right on parameters of algorithms | Must be informed about AI algorithms affecting working conditions |
| **ET Art. 20.3** | Employer monitoring right, subject to proportionality and dignity | AI monitoring must respect dignity and proportionality |
| **RD-ley 9/2021 Art. 1** | Algorithmic transparency for platform workers ("Ley Rider") | Platform companies must provide workers' legal representatives with algorithms affecting working conditions |
| **LOPDGDD Art. 89** | Digital rights in the workplace | Digital privacy rights for employees, including limitations on AI monitoring |

**Spain's "Ley Rider" (RD-ley 9/2021)** is Europe's first specific legislation on algorithmic transparency for platform workers. Requires disclosure of:
- Parameters, rules, and instructions used by algorithms
- How algorithms affect working conditions, access to work, and performance evaluation
- This must be provided to workers' legal representatives, not just individual workers

### 3.8 Cross-Jurisdiction Summary: Workplace AI Deployment

```
┌─────────────────────────────────────────────────────────────────┐
│ WORKPLACE AI DEPLOYMENT — DUAL COMPLIANCE LAYER                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Layer 1: EU AI Act                                            │
│  ├── Art. 26(7): Inform employees about AI use                 │
│  ├── Annex III Nr. 4: Employment AI → high-risk                │
│  ├── Art. 5(1)(f): Emotion recognition → prohibited            │
│  └── Art. 27: FRIA for certain deployers                       │
│                                                                 │
│  Layer 2: National Employment Law                              │
│  ├── DE: Betriebsvereinbarung required (§87 BetrVG)            │
│  ├── AT: Dignity-based consent (§96 ArbVG)                     │
│  ├── CH: Personality protection (OR Art. 328)                  │
│  ├── FR: CSE consultation (L. 2312-38)                         │
│  ├── NL: Works council consent (Art. 27 WOR)                   │
│  ├── IT: Trade union agreement or inspectorate auth (Art. 4)   │
│  └── ES: Algorithm disclosure to worker reps (RD-ley 9/2021)   │
│                                                                 │
│  ⚠ National law often requires action BEFORE deployment         │
│  ⚠ AI Act obligations are IN ADDITION to national law           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Financial Sector Regulators (Selected)

### 4.1 Germany — BaFin

**Authority:** Bundesanstalt für Finanzdienstleistungsaufsicht

**AI-relevant frameworks:**
- **MaRisk (Mindestanforderungen an das Risikomanagement):** Model risk management requirements applicable to AI/ML models in credit, market risk, and operational risk
- **BAIT (Bankaufsichtliche Anforderungen an die IT):** IT governance for banks — covers AI model development, validation, and monitoring
- **VAIT (Versicherungsaufsichtliche Anforderungen an die IT):** Equivalent for insurance
- **KAIT (Kapitalverwaltungsaufsichtliche Anforderungen an die IT):** Equivalent for capital management

**BaFin expectations for AI in finance:**
- Model governance: documentation, validation, ongoing monitoring (parallels AI Act Art. 9, 11-12)
- Explainability: material AI/ML-driven decisions must be explainable to supervisors
- Outsourcing: AI services from third-party providers subject to outsourcing requirements (§25b KWG)
- Consumer protection: AI-driven product recommendations and pricing must comply with conduct rules

**AI Act interaction:** Financial sector AI (credit scoring, insurance pricing) triggers both BaFin regulatory requirements AND AI Act Annex III Nr. 5 high-risk obligations. Dual compliance required.

### 4.3 Switzerland — FINMA

**Authority:** Eidgenössische Finanzmarktaufsicht

**AI-relevant frameworks:**
- **FINMA Circular 2023/1 "Operational Risks and Resilience":** Covers technology risks including AI/ML model governance
- **FINMA Circular 2017/1 "Corporate Governance":** Internal control framework applicable to AI governance
- Model risk management: FINMA expects banks to treat AI/ML models with at least the same rigor as traditional statistical models
- Outsourcing circular: AI-as-a-Service from third parties subject to outsourcing rules

**Key difference:** FINMA takes a principles-based, technology-neutral approach. No AI-specific rules, but existing risk management requirements apply fully to AI deployments.

### 4.5 Netherlands — DNB & AFM

**DNB (De Nederlandsche Bank):**
- Published supervisory expectations on responsible use of AI (2019, updated 2023)
- Focus on explainability, fairness, and accountability in AI-driven decisions
- Specific attention to bias in credit and insurance models

**AFM (Autoriteit Financiële Markten):**
- Published guidance on algorithmic decision-making (2021)
- Focus on consumer protection in AI-driven financial products
- Active in European discussions on AI in finance

**Key strength:** Netherlands has the most developed regulatory position on algorithmic accountability in financial services among the jurisdictions covered.

---

## 6. Critical Infrastructure & Cybersecurity

### 6.1 Germany — BSI Framework

**Authority:** Bundesamt für Sicherheit in der Informationstechnik (BSI)

| Framework | AI Relevance |
|-----------|-------------|
| **BSI-Gesetz (BSIG)** | Critical infrastructure operators must report AI-related security incidents |
| **IT-Grundschutz** | Baseline security standards — AI systems in critical infrastructure must meet these |
| **KRITIS-Verordnung (BSI-KritisV)** | Defines critical infrastructure thresholds — AI safety components in these sectors trigger Annex III Nr. 2 |
| **BSI TR-03183** | Technical requirement for software bill of materials — applicable to AI components |

**KRITIS sectors overlap with AI Act Annex III Nr. 2:** Energy, water, food, IT/telecom, health, finance, transport — AI safety components in these sectors face both KRITIS and AI Act obligations.

### 6.2 NIS2 Transposition Status

**NIS2 Directive (EU) 2022/2555** — strengthens cybersecurity for essential and important entities. AI systems in covered sectors face NIS2 + AI Act dual requirements.

| Country | NIS2 Transposition Status (March 2026) | Lead Authority |
|---------|----------------------------------------|----------------|
| **DE** | NIS2UmsuCG (NIS-2-Umsetzungs- und Cybersicherheitsstärkungsgesetz) — delayed past Oct 2024 deadline; in legislative process | BSI |
| **AT** | NISG 2024 (Netz- und Informationssystemsicherheitsgesetz) — adopted | BMI + sector CERTs |
| **CH** | ISG (Informationssicherheitsgesetz) — own framework, not NIS2 bound; voluntary alignment | NCSC |
| **FR** | Transposition in progress via existing ANSSI framework adaptation | ANSSI |
| **NL** | Cyberbeveiligingswet — transposition in progress | NCSC-NL |
| **IT** | D.Lgs. transposing NIS2 adopted (2024) | ACN |
| **ES** | Transposition in progress; existing ENS (Esquema Nacional de Seguridad) provides baseline | CCN-CERT + INCIBE |

### 6.3 Sector-Specific Overlap

| Sector | EU Legislation | AI Act Annex | NIS2 | Key Dual Obligations |
|--------|---------------|-------------|------|---------------------|
| Energy | Electricity Regulation, Renewables Directive | Annex III Nr. 2 | Essential entity | AI grid management: safety component + cybersecurity |
| Transport | ITS Directive, Railway Safety Directive | Annex III Nr. 2 + Annex I Nr. 17-18 | Essential entity | AI traffic management: high-risk + NIS2 resilience |
| Health | Medical Device Regulation | Annex I Nr. 11-12 + Annex III Nr. 1c/5b | Essential entity | AI diagnostics: product safety + NIS2 + data protection |
| Digital Infrastructure | eIDAS, EU cloud services | Annex III Nr. 2 | Essential entity | AI in cloud/telecom: critical infrastructure + NIS2 |
| Finance | CRD, PSD2, DORA | Annex III Nr. 5a/5b | Essential entity | AI credit/insurance: high-risk + DORA + NIS2 |
