# Obligations Case Studies

Three worked examples walking through obligation mapping based on role and risk tier. Each case study references the obligation framework in the parent SKILL.md and supporting reference files.

---

## Case Study 1: Deployer Compliance Walkthrough — HR Screening AI

### Scenario
**RecruitCo GmbH** (Hamburg, 500 employees) deploys a third-party AI CV screening tool classified as high-risk (Annex III Nr. 4(a)). RecruitCo is a **deployer (Betreiber)** under Art. 3(4) — no quasi-provider triggers. The system has been in use since March 2026. RecruitCo has an existing GDPR compliance program and ISO 27001 certification but no AI-specific measures.

### Obligation-by-Obligation Walkthrough

#### Immediate Obligations (should already be in place)

**1. Use per operating instructions — Art. 26(1)**
| Aspect | Implementation |
|---|---|
| Status | Check: Has RecruitCo received and reviewed the provider's Gebrauchsanweisung (operating instructions)? |
| Action | Obtain complete operating instructions from provider. Ensure HR staff using the system follow them. Document receipt and review. |
| Effort | Low |

**2. Human oversight — Art. 26(2)**
| Aspect | Implementation |
|---|---|
| Status | Assign qualified persons to oversee AI system operation |
| Action | Designate specific HR staff as oversight persons. Ensure they: (a) understand system capabilities and limitations, (b) can interpret outputs correctly, (c) can decide not to use the system or override outputs, (d) can intervene or stop the system. Document designation and qualifications. |
| Effort | Medium |
| Existing leverage | ISO 27001 role assignment processes can be adapted |

**3. Input data relevance — Art. 26(4)**
| Aspect | Implementation |
|---|---|
| Status | Ensure input data (CVs, application data) is relevant to the intended purpose |
| Action | Define data quality standards for applicant data. Verify that only relevant data fields are processed. Check for data completeness and accuracy before system input. |
| Effort | Medium |

**4. Monitoring — Art. 26(5)**
| Aspect | Implementation |
|---|---|
| Status | Monitor system operation per operating instructions |
| Action | Establish monitoring process: track system availability, output quality, anomaly detection. Define criteria for "serious incident" per Art. 26(5) third sentence. Establish reporting procedure to provider and national authority. |
| Effort | Medium |
| Existing leverage | ISO 27001 monitoring processes can be extended |

**5. Log retention — Art. 26(6)**
| Aspect | Implementation |
|---|---|
| Status | Retain automatically generated logs for minimum 6 months |
| Action | Ensure system logging is active. Configure log storage for 6-month retention. Verify logs capture information specified in operating instructions. Ensure logs are accessible for authority requests. |
| Effort | Low |
| Critical note | Must be in place from day one — retroactive log creation is impossible |

#### Short-Term Obligations (within 3 months)

**6. DPIA — Art. 26(9)**
| Aspect | Implementation |
|---|---|
| Status | Must be completed before deployment (if not yet done, complete immediately) |
| Action | Conduct DPIA per Art. 35 GDPR. For HR AI: assess risks to applicant rights (discrimination, privacy, fairness). Document assessment and mitigation measures. Perform a DPIA per Art. 35 GDPR. |
| Effort | High |
| Existing leverage | GDPR DPIA process already established — extend to AI Act specifics |

**7. FRIA — Art. 27**
| Aspect | Implementation |
|---|---|
| Status | Required for specific private deployers of HR AI systems |
| Action | Conduct Fundamental Rights Impact Assessment. Focus on: non-discrimination (Art. 21 EU Charter), right to an effective remedy (Art. 47), presumption of innocence/defense rights if relevant. Document and submit to national authority upon request. |
| Effort | High |

**8. Employee/works council information — Art. 26(7)**
| Aspect | Implementation |
|---|---|
| Status | Must inform employee representatives before deployment |
| Action | Inform Betriebsrat (works council) per Art. 26(7) AI Act. In Germany: additionally fulfill § 87(1) Nr. 6 BetrVG co-determination requirement — works council has co-determination rights for AI systems monitoring employee behavior/performance. |
| Effort | Medium |
| Germany-specific | BetrVG co-determination goes beyond AI Act's information obligation |

**9. Inform affected persons — Art. 26(11)**
| Aspect | Implementation |
|---|---|
| Status | Must inform natural persons subject to AI decision-making |
| Action | Inform job applicants that AI is used in the screening process. Options: (a) include in job posting, (b) include in application form, (c) include in privacy notice. Must be timely, clear, and before the AI system processes their data. |
| Effort | Medium |
| GDPR leverage | Extend existing Art. 13/14 GDPR privacy notices |

**10. Register deployment — Art. 49(3)**
| Aspect | Implementation |
|---|---|
| Status | Register use of high-risk system in EU database |
| Action | Register as deployer in the EU AI database. Provide: system identification, provider details, intended use, deployment scope. |
| Effort | Low |

#### Ongoing Obligations

**11. AI competence — Art. 4**
| Aspect | Implementation |
|---|---|
| Status | Continuous training obligation |
| Action | Develop AI literacy training for: (a) HR staff using the system, (b) management overseeing deployment, (c) IT staff maintaining infrastructure. Document training delivered. Refresh periodically. |
| Effort | Medium |

**12. Authority cooperation — Art. 26(12)**
| Aspect | Implementation |
|---|---|
| Status | Must cooperate with national competent authority |
| Action | Designate point of contact for authority inquiries. Ensure logs and documentation are accessible. Be prepared to demonstrate compliance. |
| Effort | Low |

### Summary Dashboard

| Category | Count | Immediate | Short-term | Ongoing |
|---|---|---|---|---|
| Technical measures | 4 | 4 | 0 | 0 |
| Organizational measures | 6 | 1 | 4 | 1 |
| Impact assessments | 2 | 0 | 2 | 0 |
| **Total** | **12** | **5** | **6** | **1** |

---

## Case Study 2: Provider QMS Setup — Credit Scoring AI

### Scenario
**CreditScore AI Ltd** (Dublin) develops and provides a credit scoring AI system to banks across the EU. The system is classified as high-risk (Annex III Nr. 5(a)). CreditScore AI is the **provider (Anbieter)** under Art. 3(3). The company has 80 employees, existing ISO 27001 certification, and is starting AI Act compliance from scratch.

### Provider Obligation Overview

As a high-risk AI system provider, CreditScore AI must comply with Art. 16 and the full Chapter III, Section 2 requirements. See [high-risk-provider-obligations.md](high-risk-provider-obligations.md) for the complete obligation set.

### Critical Management Systems Required

**1. Risk Management System — Art. 9**

| Aspect | Implementation |
|---|---|
| Scope | Continuous, iterative process throughout AI system lifecycle |
| Key elements | (a) Identify and analyze known/foreseeable risks, (b) estimate and evaluate risks from use/misuse, (c) evaluate risks from post-market monitoring data, (d) adopt appropriate risk management measures |
| Credit scoring specific | Discrimination risk (protected characteristics), accuracy degradation, data drift, model robustness, explainability |
| Effort | 5/5 — foundational system |
| ISO 27001 leverage | Risk assessment methodology can be adapted; extend scope to AI-specific risks |

**2. Data Governance — Art. 10**

| Aspect | Implementation |
|---|---|
| Scope | Training, validation, and testing datasets |
| Key elements | (a) Design choices for datasets, (b) data collection and origin, (c) preprocessing operations, (d) data labeling, (e) relevance/representativeness assessment, (f) bias examination, (g) gap identification |
| Credit scoring specific | Ensure training data is representative across demographics. Art. 10(5): permitted to process special category data (ethnicity, gender) for bias detection purposes under strict safeguards. |
| Effort | 5/5 |

**3. Quality Management System (QMS) — Art. 17**

| Aspect | Implementation |
|---|---|
| Scope | Organization-wide quality management for AI development and operation |
| Key elements | (a) Compliance strategy and regulatory compliance concept, (b) design/development techniques and procedures, (c) quality control procedures, (d) test/validation procedures, (e) technical specifications and standards, (f) data management and governance, (g) risk management, (h) post-market monitoring, (i) incident reporting, (j) communication with authorities, (k) record-keeping, (l) resource management, (m) accountability framework |
| Credit scoring specific | Include model validation procedures, back-testing protocols, documentation of model decisions |
| Effort | 5/5 — comprehensive organizational setup |
| ISO 27001 leverage | QMS structure from ISO 27001 provides foundation. Consider ISO 42001 (AI Management System) alignment |

**4. Post-Market Monitoring — Art. 72**

| Aspect | Implementation |
|---|---|
| Scope | Active monitoring throughout system lifetime |
| Key elements | Collect and analyze data on system performance, identify compliance issues, trigger corrective actions |
| Credit scoring specific | Monitor prediction accuracy, discrimination metrics, drift detection, false positive/negative rates by demographic |
| Effort | 4/5 |

### Technical Documentation — Art. 11 + Annex IV

| Required Element | Content |
|---|---|
| General description | System description, intended purpose, versions, hardware/software requirements |
| Detailed description | Development process, design choices, architecture, algorithms, training methodology |
| Monitoring and control | Human oversight measures, monitoring capabilities, control mechanisms |
| Risk management | Risk assessment results, risk management measures |
| Changes and modifications | Change log, impact assessment for changes |
| Standards applied | List of harmonized standards and common specifications used |
| EU Declaration of Conformity | Full conformity declaration |
| Post-market monitoring plan | Monitoring methodology, data collection, analysis plan |

### Conformity Assessment — Art. 43

| Aspect | Credit Scoring |
|---|---|
| Assessment type | Self-assessment per Art. 43(2) — Annex III systems (most) allow internal control per Annex VI |
| Required before | Placing on market or putting into service |
| CE marking | Required — Art. 48 |
| EU Declaration of Conformity | Required — Art. 47, Annex V |
| EU database registration | Required — Art. 49(1) provider registration + Art. 49(2) system registration |

### Implementation Priority Roadmap

| Phase | Timeline | Actions |
|---|---|---|
| **Phase 1** | Month 1-2 | Establish QMS framework, designate roles (Art. 17), begin risk management (Art. 9) |
| **Phase 2** | Month 2-4 | Data governance (Art. 10), technical documentation (Art. 11), develop testing protocols |
| **Phase 3** | Month 4-6 | Implement monitoring systems (Art. 72), complete risk assessment, train staff |
| **Phase 4** | Month 6-8 | Conduct conformity assessment (Art. 43), prepare EU Declaration of Conformity, CE marking |
| **Phase 5** | Month 8+ | Register in EU database (Art. 49), establish post-market monitoring, ongoing compliance |

### Key Takeaway
Provider obligations for high-risk AI are substantial — the QMS requirement alone (Art. 17) requires organization-wide process changes. For a credit scoring provider, the combination of Art. 9 (risk management), Art. 10 (data governance with bias monitoring), Art. 17 (QMS), and Art. 72 (post-market monitoring) creates a comprehensive compliance framework. Existing ISO 27001 provides a foundation but is insufficient alone. Consider ISO 42001 alignment.

---

## Case Study 3: GPAI Model Provider Obligations

### Scenario
**FoundationAI** (Paris, 200 employees) develops and releases "EuroLLM-70B," a 70-billion parameter large language model trained on multilingual European data. The model is offered via API and downloadable weights. Training used approximately 5 × 10^23 FLOPs. The model is NOT classified as having systemic risk (below 10^25 threshold). No Commission designation.

### GPAI Classification

| Criterion | Assessment |
|---|---|
| GPAI model (Art. 3(63))? | **Yes** — trained with large data, self-supervised, significant generality, capable of wide range of tasks |
| Training FLOPs | 5 × 10^23 — below 10^25 threshold |
| Systemic risk (Art. 51)? | **No** — below FLOP threshold, no Commission designation |
| Open-source? | Partially — weights downloadable but commercial license restricted |

**Classification:** Standard GPAI model — Art. 53 obligations apply. Art. 55 (systemic risk) does NOT apply.

### Obligation-by-Obligation Walkthrough

See [gpai-obligations.md](gpai-obligations.md) for the full framework.

**1. Technical Documentation — Art. 53(1)(a) + Annex XI**

| Aspect | Implementation |
|---|---|
| Status | Must be completed before placing model on market |
| Action | Prepare documentation per Annex XI: model description (EuroLLM-70B architecture, training methodology, 70B parameters), training data description (European multilingual corpus, sources, scope), computational resources (hardware, 5×10^23 FLOPs, training time), evaluation results (benchmarks, metrics), energy consumption, known limitations |
| Effort | 5/5 — comprehensive technical documentation |
| Key risk | Must be sufficiently detailed for downstream providers to assess high-risk compliance |

**2. Information to Downstream Providers — Art. 53(1)(b) + Annex XII**

| Aspect | Implementation |
|---|---|
| Status | Must be available before downstream integration |
| Action | Prepare documentation per Annex XII: capabilities and limitations (including foreseeable risks per domain), integration guidance for downstream AI system providers, technical requirements (API specifications, hardware requirements, latency), suitability assessments per use case category. Critical: warn downstream providers about potential high-risk use cases (e.g., "If used for credit scoring, the downstream system provider bears full Annex III obligations"). |
| Effort | 4/5 |
| Key consideration | This documentation enables downstream providers to fulfill their own compliance obligations — insufficient information creates value chain liability |

**3. Copyright Compliance — Art. 53(1)(c)**

| Aspect | Implementation |
|---|---|
| Status | Continuous obligation |
| Action | Implement copyright policy: (a) document all training data sources and copyright status, (b) implement opt-out mechanism for rights holders per Art. 4(3) Directive (EU) 2019/790, (c) respect machine-readable opt-out signals (robots.txt, ai.txt), (d) establish process for rights holder complaints, (e) document compliance measures taken |
| Effort | 4/5 |

**4. Training Data Summary — Art. 53(1)(d) + Annex XIa**

| Aspect | Implementation |
|---|---|
| Status | Must be publicly available |
| Action | Publish training data summary per Annex XIa template: data source categories (web crawl, books, academic papers, news, legal texts, etc.), languages represented, time periods, geographic scope, data governance measures applied, data size statistics. Must be "sufficiently detailed" — not a vague overview |
| Effort | 3/5 |

### GPAI Code of Practice — Art. 56

| Aspect | Status |
|---|---|
| Code published | 10 July 2025 [verify] |
| Compliance benefit | Presumption of compliance with Art. 53 obligations |
| Action | Review Code of Practice and map to implemented measures. Document compliance. If Code is followed, this simplifies enforcement interactions. |

### Open-Source Partial Exemption Assessment

FoundationAI's model has downloadable weights but a restricted commercial license → does Art. 53(2) partial exemption apply?

| Criterion | Met? | Reasoning |
|---|---|---|
| Weights publicly accessible | Yes | Downloadable |
| Architecture fully disclosed | Yes | Published |
| Unrestricted use (private + commercial) | **No** | Commercial license restricted |

**Result:** Art. 53(2) exemption does NOT apply — commercial restriction fails the "free and open-source" test. All four Art. 53(1) obligations apply in full.

### Value Chain Responsibility

When downstream providers integrate EuroLLM-70B into high-risk systems:

```
FoundationAI (GPAI provider)        → Art. 53 obligations
       │
       ▼
Downstream AI system provider       → Art. 8-17 (if high-risk)
(e.g., CreditScore AI Ltd)             Uses FoundationAI's Art. 53(1)(b)
       │                               documentation for conformity assessment
       ▼
Deployer (e.g., EuroBank SA)        → Art. 26 deployer obligations
```

### Key Takeaway
Standard GPAI obligations (Art. 53) are significant but manageable — technical documentation, downstream information, copyright compliance, and training data transparency. The critical aspect is the downstream information obligation (Art. 53(1)(b)): GPAI providers must give downstream integrators sufficient information to fulfill their own high-risk compliance. This creates a value chain responsibility where the GPAI provider's documentation quality directly affects downstream compliance capabilities.
