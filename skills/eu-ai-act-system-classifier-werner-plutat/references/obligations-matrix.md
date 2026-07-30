# Obligations Matrix — Provider, Deployer, Importer, Distributor

## Table of Contents

1. [Role Definitions](#1-role-definitions)
2. [High-Risk AI Systems — Provider Obligations](#2-high-risk-ai-systems--provider-obligations)
3. [High-Risk AI Systems — Deployer Obligations](#3-high-risk-ai-systems--deployer-obligations)
4. [High-Risk AI Systems — Importer & Distributor Obligations](#4-high-risk-ai-systems--importer--distributor-obligations)
5. [Limited-Risk Systems — Transparency Obligations](#5-limited-risk-systems--transparency-obligations)
6. [GPAI Obligations by Role](#6-gpai-obligations-by-role)
7. [Horizontal Obligations (All Roles)](#7-horizontal-obligations-all-roles)
8. [Quick Reference Matrix](#8-quick-reference-matrix)
9. [When Roles Shift](#9-when-roles-shift)

---

## 1. Role Definitions

**Provider (Article 3(3)):** Natural or legal person that develops an AI system or GPAI model, or has one developed, and places it on the market or puts it into service under its own name or trademark.

**Deployer (Article 3(4)):** Natural or legal person that uses an AI system under its authority, except where the AI system is used in the course of a personal non-professional activity.

**Importer (Article 3(6)):** Natural or legal person established in the EU that places on the market an AI system from a third country.

**Distributor (Article 3(7)):** Natural or legal person in the supply chain, other than the provider or importer, that makes an AI system available on the EU market.

**Authorised representative (Article 3(5)):** Natural or legal person established in the EU appointed by a provider outside the EU to act on its behalf.

**Critical distinction:** If you buy an AI tool and use it in your business, you are typically the *deployer*. If you build or customise it and offer it to others, you may be the *provider*.

---

## 2. High-Risk AI Systems — Provider Obligations

Providers bear the heaviest compliance burden. Core obligations under Title III, Chapter 2:

| Obligation | Article | Practical Evidence |
|-----------|---------|-------------------|
| Risk management system | Art. 9 | Risk management file, hazard analysis, residual risk documentation |
| Data governance | Art. 10 | Dataset documentation, data quality metrics, bias evaluation |
| Technical documentation | Art. 11 | System architecture, model description, evaluation metrics |
| Record-keeping & logging | Art. 12 | Logging design, retention policy, automated log capabilities |
| Transparency to deployers | Art. 13 | Instructions for use, system capabilities and limitations |
| Human oversight design | Art. 14 | Oversight mechanisms, override capabilities, training materials |
| Accuracy, robustness, cybersecurity | Art. 15 | Testing results, cybersecurity assessment, performance metrics |
| Quality management system | Art. 17 | QMS procedures, internal audit records, corrective actions |
| Conformity assessment | Arts. 43–46 | Conformity assessment report, notified body opinion (if applicable) |
| EU declaration of conformity | Art. 47 | Signed declaration with all required information |
| CE marking | Arts. 48–49 | CE mark affixed to system or documentation |
| Registration in EU database | Art. 49 | Database registration before placing on market |
| Post-market monitoring | Art. 72 | Monitoring plan, data collection, trend analysis |
| Serious incident reporting | Art. 73 | Incident response procedure, reporting templates, timelines |

---

## 3. High-Risk AI Systems — Deployer Obligations

Deployers have significant but narrower obligations (Article 26):

| Obligation | Article | Practical Evidence |
|-----------|---------|-------------------|
| Use per instructions | Art. 26(1) | SOPs reflecting provider's instructions for use |
| Human oversight | Art. 26(2) | Trained reviewers, override protocols, escalation procedures |
| Input data relevance | Art. 26(4) | Data quality checks for inputs under deployer's control |
| Monitor operation | Art. 26(5) | Operational monitoring, anomaly detection |
| Keep logs | Art. 26(6) | Log retention (min. 6 months unless other law requires more) |
| Inform workers | Art. 26(7) | Worker notification before deployment of workplace AI |
| FRIA | Art. 27 | Fundamental rights impact assessment (public bodies + specific private uses) |
| Inform affected persons | Art. 26(11) | Notification to individuals subject to high-risk AI decisions |
| Cooperate with authorities | Art. 26(10) | Contact point, response procedures, data access protocols |

### Fundamental Rights Impact Assessment (FRIA) — Article 27

**Who must conduct one:**
- Public bodies and private entities providing public services using high-risk AI in categories 5(a)–(c) of Annex III (creditworthiness, essential services, certain insurance)
- Before putting the high-risk system into use

**FRIA contents:**
- Description of the deployer's processes where the AI system will be used
- Period and frequency of intended use
- Categories of affected natural persons and groups
- Specific risks of harm to those categories
- Human oversight measures
- Measures if risks materialise (complaint handling, redress)
- Notification to relevant data protection authority where applicable

---

## 4. High-Risk AI Systems — Importer & Distributor Obligations

### Importer Obligations (Articles 23–24)

Before placing a high-risk AI system on the EU market, importers must verify:
- [ ] Provider has carried out conformity assessment
- [ ] Technical documentation is prepared (Art. 11)
- [ ] System bears CE marking and EU declaration of conformity
- [ ] Provider has appointed an authorised representative (Art. 22)
- [ ] Instructions for use accompany the system (Art. 13)

**Ongoing duties:**
- Storage and transport conditions do not compromise compliance
- Keep a copy of the EU declaration of conformity
- Cooperate with market surveillance authorities
- Take corrective action or withdraw the system if non-compliance is identified

### Distributor Obligations (Article 25)

Before making a system available on the market:
- [ ] Verify CE marking and EU declaration of conformity
- [ ] Verify instructions for use and contact information
- [ ] Verify storage/transport conditions maintained

**Ongoing duties:**
- If non-compliance is suspected, do not make the system available until corrected
- Inform provider/importer and market surveillance authorities of non-compliance
- Cooperate with competent authorities

---

## 5. Limited-Risk Systems — Transparency Obligations

**Article 50** obligations shared between providers and deployers:

| Obligation | Responsible Party | Practical Implementation |
|-----------|------------------|------------------------|
| AI interaction disclosure | Provider + Deployer (whoever controls the interface) | UI notices, voice disclosures, call scripts |
| Deepfake/synthetic content labelling | Provider (generation) + Deployer (distribution) | Watermarking, metadata, content provenance |
| Emotion recognition disclosure | Deployer | Inform exposed individuals before use |
| Biometric categorisation disclosure | Deployer | Inform exposed individuals before use |

**Exception:** Disclosure not required where AI use is obvious from context for a reasonably well-informed person (e.g., clear AI avatar in a game).

---

## 6. GPAI Obligations by Role

| Obligation | GPAI Model Provider | Downstream System Provider | Deployer |
|-----------|--------------------|-----------------------------|---------|
| Technical documentation (Art. 53) | ✅ Prepare and maintain | Request and review | — |
| Information to downstream (Art. 53) | ✅ Provide | ✅ Use for system compliance | — |
| Training data summary (Art. 53) | ✅ Publicly available | Review and reference | — |
| Copyright policy (Art. 53) | ✅ Establish and comply | — | — |
| Systemic risk evaluation (Art. 55) | ✅ If classified | Request evidence | — |
| Incident reporting (Art. 55) | ✅ If systemic risk | Report system-level incidents (Art. 73) | Escalate incidents |
| Contract terms | Include AI Act clauses | Include AI Act clauses | Include AI Act clauses |

---

## 7. Horizontal Obligations (All Roles)

**AI Literacy (Article 4):** All providers and deployers must take measures to ensure that their staff and others involved in the operation and use of AI systems have a sufficient level of AI literacy. Applies since **2 February 2025**.

**Practical implementation:**
- Training programme for relevant staff
- Role-specific curriculum (developers, compliance, operations, management)
- Documentation of training completion
- Regular refresher training

---

## 8. Quick Reference Matrix

| Obligation | Provider | Deployer | Importer | Distributor |
|-----------|----------|----------|----------|-------------|
| Risk management (Art. 9) | ✅ | — | — | — |
| Data governance (Art. 10) | ✅ | — | — | — |
| Technical docs (Art. 11) | ✅ | — | Verify | — |
| Logging design (Art. 12) | ✅ | Keep logs | — | — |
| Instructions for use (Art. 13) | ✅ Produce | Follow | Verify | Verify |
| Human oversight (Art. 14) | ✅ Design | ✅ Operate | — | — |
| Accuracy/robustness (Art. 15) | ✅ | — | — | — |
| QMS (Art. 17) | ✅ | — | — | — |
| Conformity assessment (Art. 43) | ✅ | — | Verify | Verify |
| CE marking (Arts. 48–49) | ✅ Affix | — | Verify | Verify |
| Registration (Art. 49) | ✅ | ✅ (deployer reg.) | — | — |
| Post-market monitoring (Art. 72) | ✅ | — | — | — |
| Incident reporting (Art. 73) | ✅ | Escalate | Cooperate | Cooperate |
| FRIA (Art. 27) | — | ✅ (when required) | — | — |
| Worker notification (Art. 26(7)) | — | ✅ | — | — |
| AI literacy (Art. 4) | ✅ | ✅ | — | — |

---

## 9. When Roles Shift

Certain actions can change your role classification:

**You become a provider if you:**
- Put your name/trademark on an existing AI system (Article 25(1)(a))
- Make a substantial modification to a high-risk system (Article 25(1)(b))
- Modify the intended purpose of a system to make it high-risk (Article 25(1)(c))

**Practical implications:**
- Fine-tuning a GPAI model for a specific use case → you may become the provider of a new AI system
- Customising a vendor's AI tool significantly → assess whether the modification is "substantial"
- Rebranding a third-party AI tool → you assume provider obligations

**Key question:** Have you done more than merely configuring or deploying the system within its documented intended purpose?
