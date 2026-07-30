# Sector-Specific Role Determination Nuances

Brief cross-reference to sector-specific considerations affecting role determination. For full sector classification guidance, pair this with the sector analysis done during the risk-tier classification (Annex III area mapping by sector).

---

## Healthcare (Gesundheitswesen)

**Role complexity:** Medical AI often involves a multi-layered value chain:
- **GPAI model provider** (e.g., foundation model for medical NLP) → Art. 53 obligations
- **AI system provider** (e.g., medical software company) → Art. 16 provider obligations + MDR obligations
- **Medical device manufacturer** → Art. 25(3) quasi-provider if integrating AI into own device
- **Healthcare deployer** (hospital, clinic) → Art. 26 deployer obligations

**Key nuance:** Under MDR (EU) 2017/745, the entity placing the medical device on the market under their name bears manufacturer responsibility. If a hospital integrates an AI component into its own clinical workflow system and deploys under its own name, it may become both MDR manufacturer and AI Act provider (Art. 25(3)).

**Works council relevance:** In Germany, § 87(1) Nr. 6 BetrVG applies when AI monitors healthcare employees (e.g., staff performance tracking).

---

## Finance and Insurance (Finanz- und Versicherungswesen)

**Role complexity:** Financial sector often involves:
- **FinTech provider** developing credit scoring/underwriting AI → Provider
- **Bank/insurer deploying** third-party AI → Deployer
- **System integrator** customizing AI for financial institution → potential quasi-provider

**Key nuance:** Banks frequently customize vendor AI models (retraining on proprietary data, adjusting risk parameters). If customization constitutes substantial modification (wesentliche Veraenderung), the bank becomes quasi-provider under Art. 25(1)(b) despite intending to be "only" a deployer. This is particularly common in credit scoring where banks retrain models on their customer portfolios.

**Regulatory overlap:** Financial supervisors (BaFin, ECB SSM) already impose model governance requirements on banks — model risk management frameworks (e.g., SR 11-7 equivalent) may overlap with AI Act provider obligations.

---

## HR and Employment (Personalwesen und Beschaeftigung)

**Role complexity:** HR AI typically has a clear provider-deployer split:
- **HR tech vendor** (develops recruitment/evaluation AI) → Provider
- **Employer** (deploys AI in HR processes) → Deployer

**Key nuance:** Employers who significantly customize HR AI tools (e.g., training on internal performance data, adjusting evaluation criteria beyond provider's intended range) risk Art. 25(1)(b) quasi-provider status. The distinction between "configuration" (deployer remains) and "modification" (quasi-provider risk) is critical.

**Sector-specific triggers for quasi-provider:**
- Retraining candidate scoring model on company-specific historical hiring data → assess per [finetuning-assessment.md](finetuning-assessment.md)
- Changing evaluation criteria to include factors not intended by the provider → potential Art. 25(1)(c) purpose change
- White-labeling HR tool under employer's brand for internal or external use → Art. 25(1)(a)

---

## Law Enforcement (Strafverfolgung)

**Role complexity:** Law enforcement AI involves government-specific dynamics:
- **Technology vendor** (develops AI for law enforcement) → Provider
- **Law enforcement authority** (deploys AI) → Deployer
- **System integrator** (adapts AI for national requirements) → potential quasi-provider

**Key nuance:** Law enforcement agencies that adapt AI systems to national legal requirements (e.g., adjusting risk thresholds, integrating with national databases) must assess whether adaptations constitute substantial modification. National security adaptations may fall under Art. 2(3) exclusion, but dual-use systems (police + intelligence) require careful scope analysis.

**Procurement consideration:** Public procurement of AI for law enforcement should contractually clarify provider vs. deployer obligations from the outset, including Art. 25(2) original provider support duties.

---

## Education (Bildungswesen)

**Role complexity:** Education AI commonly involves:
- **EdTech provider** (develops learning/assessment AI) → Provider
- **Educational institution** (school, university) → Deployer
- **Ministry/authority** (procures AI for education system) → may be deployer or quasi-provider

**Key nuance:** Educational institutions that develop their own AI tools (e.g., university research group creating an AI grading system) become providers, not deployers — even for internal use, if the system is high-risk. Universities finetuning open-source models for educational assessment must assess quasi-provider risk per Art. 25.

**Additional consideration:** When a ministry mandates AI use across schools, the ministry may be the deployer (using under own authority) while individual schools are end-users. Role determination depends on who has authority over the deployment decision.
