# Report Case Studies — Sample Excerpts

Three sample report excerpts demonstrating how to fill key sections of the AI Act Compliance Assessment Report. Each excerpt illustrates a different classification scenario. Reference the full template in [report-template.md](report-template.md).

---

## Sample 1: High-Risk HR Screening — Report Sections 4-6

### Context
AI system: "TalentMatch Pro v3.2" — CV screening and candidate ranking tool for recruitment.
Organization: MegaCorp AG (deployer), TalentAI GmbH (provider).
Classification: High-risk (Annex III Nr. 4(a)).

---

### 4. Scope of Application

**4.1 Material Scope — AI System Determination (Art. 3(1))**

| # | Criterion | Met? | Reasoning |
|---|-----------|------|-----------|
| 1 | Machine-based operation | Yes | Cloud-based software with ML model processing |
| 2 | Degree of autonomy | Level 2-3 | Autonomously scores and ranks candidates; HR reviews results |
| 3 | Adaptability after deployment | Yes | Model incorporates hiring outcome feedback for scoring refinement |
| 4 | Explicit or implicit goals | Yes | Explicit goal: identify most suitable candidates per job requirements |
| 5 | Inference capability | Yes | Derives suitability scores through ML inference, not rule-based matching |
| 6 | Output generation | Yes | Generates ranking scores (1-100), candidate shortlists, and suitability recommendations |
| 7 | Environmental influence | Yes | Directly influences which candidates proceed to interview stage |

**Determination:** TalentMatch Pro IS an AI system under Art. 3(1).
**Confidence:** High — all 7 criteria clearly met. System exhibits inference-based scoring beyond simple keyword matching.

**4.2 Personal Scope — Role Determination**

| Aspect | Determination |
|---|---|
| Primary role | MegaCorp AG: Deployer (Betreiber) — Art. 3(4) |
| Legal basis | Art. 3(4) — uses AI system under own authority in professional capacity |
| Quasi-provider risk | None — system used as provided, within intended purpose, no rebranding |
| Art. 25 scenario | N/A — no modification, no rebranding, no purpose change |

MegaCorp AG licenses TalentMatch Pro from TalentAI GmbH and deploys it in its HR department for internal recruitment. The system is presented under TalentAI's branding ("Powered by TalentAI"). MegaCorp configures screening criteria within TalentAI's intended parameter range. No Art. 25 quasi-provider trigger identified.

**4.3 Territorial Scope**

| Aspect | Detail |
|---|---|
| Provider establishment | TalentAI GmbH — Berlin, Germany (EU) |
| Deployer establishment | MegaCorp AG — Munich, Germany (EU) |
| AI output used in EU | Yes — recruitment decisions affecting EU-based applicants |
| Territorial basis | Art. 2(1)(a) — provider and deployer established in EU |

---

### 5. Intended Purpose (Art. 3(12))

**Provider's documented intended purpose:**
Per TalentAI GmbH's operating instructions (v3.2, dated 15 Jan 2026): "TalentMatch Pro is intended for screening and ranking job applicants based on qualification matching, experience relevance, and skill assessment. The system is designed for use by human resources professionals as a decision-support tool. All system outputs require human review before hiring decisions."

**Actual deployment context:**
MegaCorp AG uses TalentMatch Pro to screen incoming applications for open positions across departments. HR recruiters review the system's top-ranked candidates and make interview decisions. The system processes CVs, cover letters, and application form data.

**Alignment assessment:**
Match — MegaCorp's actual use aligns with TalentAI's documented intended purpose. The system is used as a decision-support tool for recruitment with human oversight. No Art. 25(1)(c) implications identified.

---

### 6. Risk Classification

**6.1 Prohibited Practices Screening (Art. 5)**

| # | Category | Article | Applicable? | Reasoning |
|---|----------|---------|-------------|-----------|
| 1 | Subliminal/manipulative/deceptive | Art. 5(1)(a) | No | System does not manipulate candidates or recruiters |
| 2 | Exploitation of vulnerabilities | Art. 5(1)(b) | No | No targeting based on age, disability, or economic situation |
| 3 | Social scoring | Art. 5(1)(c) | No | Not operated by or on behalf of public authority for social scoring |
| 4 | Criminal risk prediction | Art. 5(1)(d) | No | Not related to criminal risk assessment |
| 5 | Facial recognition scraping | Art. 5(1)(e) | No | No facial recognition database creation |
| 6 | Emotion recognition (workplace) | Art. 5(1)(f) | No | System analyzes CVs, not emotions. No video interview analysis component |
| 7 | Biometric categorization | Art. 5(1)(g) | No | No biometric data processing |
| 8 | Real-time biometric ID | Art. 5(1)(h) | No | No biometric identification |

**Result:** No prohibited practice identified.

**6.2 High-Risk Assessment**

**6.2.1 Annex I — Product Safety**
TalentMatch Pro is a standalone SaaS platform, not a component of a physical product and not covered by Annex I EU harmonization legislation.
**Result:** Not applicable.

**6.2.2 Annex III — Application-Based**

| # | Category | Applicable? | Sub-category | Reasoning |
|---|----------|-------------|-------------|-----------|
| 1 | Biometrics | No | — | No biometric processing |
| 2 | Critical infrastructure | No | — | HR is not critical infrastructure |
| 3 | Education & training | No | — | Not used in education context |
| 4 | Employment & workers | **Yes** | **Nr. 4(a)** | System intended for recruitment — screening and filtering applications, evaluating candidates |
| 5 | Essential services | No | — | Not credit, insurance, or emergency services |
| 6 | Law enforcement | No | — | Not law enforcement context |
| 7 | Migration & border | No | — | Not migration context |
| 8 | Justice & democracy | No | — | Not judicial or democratic process |

**Result:** Applicable — **Annex III Nr. 4(a)** (employment, workers management — recruitment)

**6.2.3 Art. 6(3) Exception Analysis**

| Condition | Assessment | Met? |
|---|---|---|
| (a) Narrow procedural task | System ranks and scores candidates based on multi-factor analysis — this is substantive, not narrow/procedural | No |
| (b) Improving completed human activity | Human has not yet made a decision — system precedes human assessment | No |
| (c) Detecting decision patterns | System generates new scores, does not analyze existing human decisions | No |
| (d) Preparatory task | System could be argued as preparatory — but it generates rankings that effectively pre-select candidates. The scoring materially influences which candidates are considered. | No (borderline) |

**Profiling re-exception check:** System evaluates personal aspects of individual natural persons (qualifications, experience, skills) → profiling under Art. 4(4) GDPR → **Art. 6(3) exception is independently blocked by profiling re-exception.**

**Result:** Exception does NOT apply — system is **HIGH-RISK** under Art. 6(2), Annex III Nr. 4(a).

---

## Sample 2: Non-High-Risk Art. 6(3) Documentation

### Context
AI system: "DocSort v2.1" — document categorization tool for incoming immigration applications.
Organization: ImmigrationTech BV (provider).
The system scans incoming applications, extracts key data fields (name, date, application type), and routes them to the correct department. It does NOT evaluate, rank, or assess applications.

---

### Art. 6(4) Non-High-Risk Assessment Documentation

**System name:** DocSort v2.1
**Version:** 2.1.3
**Provider:** ImmigrationTech BV (The Hague, Netherlands)
**Intended purpose:** Automated categorization and routing of incoming immigration applications based on document type and content extraction.
**Annex III category triggered:** Nr. 7(b) — AI for examination of applications relating to migration, asylum, and border control.
**Assessment date:** 12 January 2026
**Prepared by:** [Legal Counsel, ImmigrationTech BV]

**Art. 6(3) condition fulfilled: (a) — Narrow procedural task**

**Analysis:**
DocSort v2.1 performs a narrow, well-defined procedural task: it categorizes incoming documents by type (visa application, residence permit renewal, asylum claim, family reunification) and extracts structured data fields (applicant name, date of birth, application reference number, document type) for routing to the appropriate processing department.

The system:
- Performs document classification and data extraction ONLY
- Does NOT evaluate the merit, quality, or eligibility of any application
- Does NOT score, rank, or prioritize applicants
- Does NOT influence the substantive assessment of applications
- Could reasonably be performed by a simple classification algorithm (rule-based routing with OCR)

The task is procedural (sorting/routing) rather than substantive (evaluating/deciding). It is equivalent to a digital mailroom function.

**Significant Risk of Harm Assessment:**

| Question | Answer | Reasoning |
|---|---|---|
| Can output affect health? | No | Document routing does not impact health |
| Can output affect safety? | No | Routing has no safety implications |
| Can output affect fundamental rights? | Low | Incorrect routing could delay processing, but human staff correct misrouted documents. System does not deny or grant applications. |
| Materially influence outcomes? | No | Application assessment is performed entirely by human officers after routing |
| Severity if errors? | Low | Misrouted document causes processing delay, not wrong decision |
| Persons affected? | High volume (thousands) but low impact per individual |

**Overall harm assessment:** No significant risk of harm identified. Errors result in processing delays that are correctable by human staff. The system does not materially influence application outcomes.

**Profiling Exclusion Confirmation:**

| Indicator | Present? | Reasoning |
|---|---|---|
| Uses personal data | Yes | Extracts names, dates from applications |
| Evaluates personal aspects | **No** | System categorizes documents, not persons. Does not assess performance, reliability, behavior, etc. |
| Analyzes/predicts individual characteristics | **No** | Classification is based on document type, not individual attributes |
| Individual-level assessment | **No** | No assessment of individuals — only document classification |

**Profiling determination:** No profiling. System processes personal data for identification/routing purposes only, not for evaluating personal aspects of individuals.

**Registration:** Registered in EU database per Art. 49(2) — Reference: [EU-DB-2026-XXXXX]

**Conclusion:** DocSort v2.1 falls within Annex III Nr. 7(b) but qualifies for the Art. 6(3) exception under condition (a) — narrow procedural task. The system is classified as NOT high-risk. This documentation is maintained per Art. 6(4) and available to national competent authorities upon request.

---

## Sample 3: Minimal-Risk Chatbot Assessment

### Context
AI system: "ShopAssist" — e-commerce product recommendation chatbot.
Organization: RetailCo S.r.l. (deployer, Milan).
Provider: ChatBot Solutions Ltd (provider, Dublin).

---

### Abbreviated Assessment

**AI System Determination (Art. 3(1)):** YES — GPT-based conversational AI with inference capability, output generation, and environmental influence (recommendations affect purchase decisions).

**Risk Classification Summary:**

| Step | Result |
|---|---|
| Art. 5 Prohibited Practices | None identified — product recommendations are not manipulative (transparent commercial context) |
| Annex I Product Safety | Not applicable — standalone software, not a product under Annex I legislation |
| Annex III Application-Based | Not applicable — e-commerce product recommendations do not fall under any Annex III category |
| Art. 6(3) Exception | N/A — no Annex III trigger to except from |
| GPAI | System uses GPAI model (GPT-based) — GPAI obligations fall on ChatBot Solutions Ltd as system provider integrating the GPAI model. OpenAI bears Art. 53 obligations as GPAI model provider. RetailCo as deployer: no GPAI-specific obligations |
| Art. 50 Transparency | **Art. 50(1) triggered** — system interacts directly with natural persons (chatbot) |
| Art. 50(2) | **Triggered** — system generates synthetic text content |

**Classification:** Minimal risk with Art. 50 transparency obligations.

**Applicable Obligations:**

| # | Obligation | Legal Basis | Responsible | Status |
|---|---|---|---|---|
| 1 | AI interaction disclosure | Art. 50(1) | RetailCo (deployer) + ChatBot Solutions (provider) | Provider must design system for disclosure; deployer must ensure disclosure is active |
| 2 | Synthetic content marking | Art. 50(2) | ChatBot Solutions (provider) | Must implement machine-readable marking on generated text |
| 3 | AI competence | Art. 4 | Both provider and deployer | Train staff on AI system capabilities and limitations |

**Implementation Notes:**
- Art. 50(1): Add clear disclosure at start of chat interaction: "Sie kommunizieren mit einem KI-System / You are communicating with an AI system"
- Art. 50(2): Implement metadata tagging or watermarking on generated responses per Commission guidelines on AI-generated content marking
- Art. 4: Brief staff training for RetailCo customer service team on chatbot capabilities, limitations, and escalation procedures

**Key Flags:**
- Monitor for scope creep: if ShopAssist is later used for credit decisions, insurance recommendations, or employment-related tasks, reclassification would be required
- GPAI model updates: if the underlying GPT model is updated to a version with systemic risk (>10^25 FLOPs), GPAI obligations escalate

---

## Using These Samples

These excerpts demonstrate the level of detail expected in different classification scenarios:

1. **High-risk reports** (Sample 1) require comprehensive analysis of every classification step, detailed Art. 6(3) exception analysis, and full obligation mapping
2. **Art. 6(3) exception documentation** (Sample 2) requires standalone Art. 6(4) documentation demonstrating why the exception applies — record which exception limb (a)-(d) is met, the harm assessment, and confirmation that the system performs no profiling
3. **Minimal-risk assessments** (Sample 3) can be abbreviated but must still document the classification reasoning and identify applicable Art. 50 obligations

Always use the full report template from [report-template.md](report-template.md) as the starting framework.
