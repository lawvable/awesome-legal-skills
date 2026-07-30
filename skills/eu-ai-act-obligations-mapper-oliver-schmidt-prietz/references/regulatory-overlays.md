# Regulatory Overlays for AI Act Obligations

Extracted from the cross-jurisdictional regulatory landscape reference. Covers employment law, financial sector, and data protection overlay requirements that apply in addition to core AI Act obligations.

**Last verified:** March 2026. Always search for latest national implementation status.

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

## 4. Financial Sector Regulators

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

### 4.2 Austria — FMA

**Authority:** Finanzmarktaufsichtsbehörde

**AI-relevant expectations mirror BaFin (harmonized via SSM/ECB for significant banks):**
- Model risk management under Austrian Banking Act (BWG)
- FMA circular on IT risk management (analogous to BAIT)
- Insurance supervision under VAG — similar model governance expectations

### 4.3 Switzerland — FINMA

**Authority:** Eidgenössische Finanzmarktaufsicht

**AI-relevant frameworks:**
- **FINMA Circular 2023/1 "Operational Risks and Resilience":** Covers technology risks including AI/ML model governance
- **FINMA Circular 2017/1 "Corporate Governance":** Internal control framework applicable to AI governance
- Model risk management: FINMA expects banks to treat AI/ML models with at least the same rigor as traditional statistical models
- Outsourcing circular: AI-as-a-Service from third parties subject to outsourcing rules

**Key difference:** FINMA takes a principles-based, technology-neutral approach. No AI-specific rules, but existing risk management requirements apply fully to AI deployments.

### 4.4 France — ACPR & AMF

**ACPR (Autorité de Contrôle Prudentiel et de Résolution):**
- AI in banking: governance expectations align with EBA guidelines on ICT and security risk management
- AI in insurance: model governance under Solvabilité II (Solvency II) framework
- ACPR has published discussion papers on AI governance in financial services (2020, 2024)

**AMF (Autorité des Marchés Financiers):**
- AI in market operations: algorithmic trading rules (MiFID II Art. 17) — governance, testing, circuit breakers
- AI in investment advice: suitability requirements apply to AI-driven recommendations

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

### 4.6 Italy — Banca d'Italia, CONSOB & IVASS

**Banca d'Italia:** Model risk management under Circular 285 (Prudential Supervision) — applies to AI/ML credit models
**CONSOB:** AI in market operations — MiFID II algorithmic trading transposition
**IVASS:** AI in insurance — Regulation 38/2018 on corporate governance includes technology risk

### 4.7 Spain — BdE & CNMV

**BdE (Banco de España):** AI governance expectations under SSM framework; published supervisory expectations on cloud and technology risk
**CNMV (Comisión Nacional del Mercado de Valores):** AI in investment services — algorithmic trading and robo-advisory requirements under MiFID II transposition

### 4.8 Cross-Border: EU-Level Financial AI Requirements

| Framework | AI Relevance | Status |
|-----------|-------------|--------|
| **DORA (Regulation (EU) 2022/2554)** | ICT risk management for financial entities — AI systems are ICT services; testing, governance, and third-party management requirements apply | In force since 17 Jan 2025 |
| **EBA Guidelines on ICT and security risk management** | Covers AI model governance as part of ICT risk | Applicable |
| **EIOPA AI governance principles** | Insurance sector AI governance expectations | Published 2021, updated guidance expected |
| **ESMA Guidelines on algorithmic trading (MiFID II)** | Governance of AI in trading operations | Applicable |
| **ECB Guide on internal models** | AI/ML models for regulatory capital calculations — specific validation requirements | Applicable to significant banks |

---

## 5. Data Protection Overlay

### 5.1 GDPR Art. 22 — Automated Decision-Making

**Base rule:** Data subjects have the right not to be subject to decisions based solely on automated processing, including profiling, which produce legal or similarly significant effects.

**Per-country interpretation differences:**

| Country | DPA | Key Position on Art. 22 + AI |
|---------|-----|------------------------------|
| **DE** | BfDI + 16 state DPAs (Landesdatenschutzbeauftragte) | Strict interpretation: AI systems making decisions about individuals almost always trigger Art. 22. Conference of Data Protection Authorities (DSK) position: meaningful human involvement requires genuine ability to override, not rubber-stamping |
| **AT** | DSB (Datenschutzbehörde) | Aligns with German strict position; Austrian Supreme Court (OGH) has recognized broad applicability of Art. 22 |
| **CH** | EDÖB (Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter) | nDSG Art. 21: Similar right to human review for automated individual decisions; not identical to GDPR Art. 22 but functionally equivalent |
| **FR** | CNIL | Most developed AI-specific guidance: 2024 AI Compliance Guide; practical recommendations on training data, purpose limitation, fairness testing; CNIL sandbox for AI data protection questions |
| **NL** | AP (Autoriteit Persoonsgegevens) | Published algorithmic risk assessment framework (Toetsingskader); active enforcement in AI context (SyRI case — landmark ruling against government algorithmic profiling) |
| **IT** | Garante per la Protezione dei Dati Personali | Active enforcement: Garante actions against Clearview AI, ChatGPT temporary ban (2023), food delivery rider algorithmic management cases; strong focus on AI transparency |
| **ES** | AEPD (Agencia Española de Protección de Datos) | Operates GDPR sandbox (Sandbox RGPD); published guidelines on AI and data protection; supportive stance combined with clear enforcement framework |

### 5.2 DPIA Coordination (Art. 35 GDPR + AI Act)

The AI Act introduces a **dual assessment obligation** for high-risk AI systems processing personal data:

| Assessment | Legal Basis | Scope | Coordination Point |
|-----------|-------------|-------|-------------------|
| **DPIA** (Data Protection Impact Assessment) | Art. 35 GDPR | Personal data processing risks | Must be completed before processing |
| **FRIA** (Fundamental Rights Impact Assessment) | Art. 27 AI Act | Broader fundamental rights (not just data protection) | Required for certain deployers of high-risk AI |
| **AI Act Risk Management** | Art. 9 AI Act | AI system lifecycle risks | Continuous process for providers |

**Practical coordination:**
- Art. 26(9) AI Act explicitly requires deployers of high-risk AI to use information from the provider (Art. 13) to conduct the DPIA
- DPIA and FRIA can be combined into a single assessment process but must address all required elements from both regulations
- Member States may designate that existing DPIA procedures satisfy some AI Act requirements

### 5.3 National DPA AI-Specific Guidance

| DPA | Key AI Guidance Documents | Practical Relevance |
|-----|--------------------------|---------------------|
| **CNIL (FR)** | "AI: Compliance Guide" (2024); Position on training data; Recommendation on AI in recruitment; AI regulatory sandbox outputs | Most comprehensive DPA AI guidance in Europe |
| **AP (NL)** | "Toetsingskader Algoritmes" (Algorithmic Assessment Framework); Government Algorithm Register requirements | Framework for systematic algorithmic accountability |
| **Garante (IT)** | Various enforcement decisions (Clearview AI, ChatGPT, Deliveroo, Foodinho); Decalogo AI (10 principles for AI) | Strong enforcement precedent for AI systems |
| **AEPD (ES)** | "Adecuación al RGPD de tratamientos que incorporan IA"; GDPR Sandbox outputs; AESIA coordination framework | Practical compliance toolkit approach |
| **BfDI/DSK (DE)** | Hamburg DPA position paper on LLMs (2023); DSK resolution on AI and data protection; State DPA enforcement actions | Detailed technical positions on LLM training data |
| **DSB (AT)** | Guidance aligned with DSK positions; enforcement focus on employer AI use | Employment AI enforcement focus |
| **EDÖB (CH)** | Guidance on nDSG application to AI; position on automated decisions | Adapted for non-EU framework |
