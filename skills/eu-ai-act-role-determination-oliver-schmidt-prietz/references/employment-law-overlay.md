# Employment & Labor Law Overlay for AI Act Role Determination

Extracted from the cross-jurisdictional regulatory landscape reference. Covers the national employment law requirements that apply in addition to AI Act role obligations across 7 jurisdictions.

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
