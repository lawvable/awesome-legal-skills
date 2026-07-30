# Organizational Measures — Information, Documentation, Training, Reporting

## Overview

Organizational measures cover the non-technical obligations: information duties, documentation requirements, training obligations, registration, and authority cooperation.

---

## Information Duties

### Art. 13 — Transparency to Deployers (Provider Obligation)

Provider must provide deployers with comprehensive information via instructions for use:

| # | Information Element | Article |
|---|-------------------|---------|
| 1 | Provider identity and contact details | Art. 13(3)(a) |
| 2 | Characteristics, capabilities, and limitations | Art. 13(3)(b) |
| 3 | Intended purpose | Art. 13(3)(b)(i) |
| 4 | Accuracy, robustness, cybersecurity level | Art. 13(3)(b)(ii) |
| 5 | Known circumstances creating risks | Art. 13(3)(b)(iii) |
| 6 | Performance for specific persons/groups | Art. 13(3)(b)(iv) |
| 7 | Input data specifications | Art. 13(3)(b)(v) |
| 8 | Human oversight measures | Art. 13(3)(c) |
| 9 | Computational/hardware resources needed | Art. 13(3)(d) |
| 10 | Expected lifetime and maintenance | Art. 13(3)(e) |
| 11 | Logging capabilities | Art. 13(3)(f) |

---

### Art. 26(11) — Information to Affected Persons (Deployer Obligation)

**Obligation:** Inform natural persons subject to decisions made or materially influenced by the high-risk AI system.

**Required information:**
- That an AI system is being used
- How the system influences decisions affecting them
- Meaningful information about the logic involved
- Contact point for questions

**Timing:** Before or at the time the system is used.

**Overlap with GDPR:** Art. 13/14 GDPR require information about automated decision-making (Art. 22 GDPR). The AI Act obligation is additional and complementary.

**RACI:**
| Role | Responsibility |
|------|---------------|
| Legal | R (draft notices) |
| Communications | A (ensure delivery) |
| Business | C (identify affected persons) |
| DPO | C (verify GDPR alignment) |

---

### Art. 26(7) — Employee Information (Deployer Obligation)

**Obligation:** Before putting into service or using a high-risk AI system at the workplace, deployers who are employers shall inform workers' representatives and the affected workers.

**What to inform about:**
- That AI system will be used in the workplace
- Nature and scope of AI system deployment
- How the system affects workers
- Rights and obligations related to the system

**National labor law considerations:**
- Germany: Betriebsrat co-determination (BetrVG § 87(1) Nr. 6)
- France: Comité social et économique (CSE) information/consultation
- Other Member States: Check national works council/employee representation rules

---

## Documentation Obligations

### Art. 11 — Technical Documentation (Provider Obligation)

**Content per Annex IV:**

| Section | Content |
|---------|---------|
| 1 | General description of the AI system |
| 2 | Detailed description of development process elements |
| 3 | Monitoring, functioning, and control description |
| 4 | Risk management system description |
| 5 | Changes throughout lifecycle |
| 6 | Standards and specifications applied |
| 7 | EU declaration of conformity |
| 8 | Performance description (accuracy, robustness, cybersecurity) |

**Retention:** 10 years after last AI system is placed on market.

---

### Art. 18 — Documentation Availability (Provider Obligation)

**Obligation:** Keep documentation available for national competent authorities for 10 years.

| Document | Retention |
|----------|-----------|
| Technical documentation (Art. 11) | 10 years |
| QMS documentation (Art. 17) | 10 years |
| Conformity assessment documentation | 10 years |
| EU declaration of conformity | 10 years |
| Logs (deployer) | Minimum 6 months |

---

### Art. 49 — Registration (Provider and Deployer Obligation)

**EU Database registration requirements:**

| Actor | Obligation | Article |
|-------|-----------|---------|
| Provider (high-risk) | Register system before market placement | Art. 49(1) |
| Provider (Art. 6(3) non-high-risk) | Register system and Art. 6(3) assessment | Art. 49(2) |
| Deployer (public sector) | Register use before deployment | Art. 49(3) |
| GPAI provider | Register model with AI Office | Art. 49(4) |

---

## Training Obligations

### Art. 4 — AI Competence (All Actors)

**Content of AI literacy training should cover:**

| Topic | Description | Target Audience |
|-------|-------------|-----------------|
| AI basics | What AI is, how it works at high level | All staff |
| System-specific training | How the specific AI system works | Operators and oversight persons |
| Limitations awareness | Understanding what AI cannot do | All users |
| Bias awareness | Recognizing potential biases | Operators and decision-makers |
| Rights awareness | Understanding affected persons' rights | Legal, HR, customer-facing staff |
| Incident recognition | When to escalate issues | All staff interacting with AI |
| Ethical considerations | Responsible AI use principles | All staff |

### Art. 26(2) — Oversight Person Training (Deployer Obligation)

Persons assigned to human oversight must have:
- **Competence:** Understanding of the AI system and its outputs
- **Training:** System-specific training on operation and oversight
- **Authority:** Power to override, intervene, or stop the system
- **Support:** Organizational resources to fulfill oversight role

---

## Reporting Obligations

### Art. 26(5) Third Sentence — Incident Reporting (Deployer)

**Trigger:** Deployer has reasons to consider the AI system may present a risk.

**Actions required:**
1. Inform provider or distributor — without undue delay
2. Inform market surveillance authority — without undue delay
3. Suspend use of the system

### Art. 73 — Serious Incident Reporting (Provider)

**Trigger:** Provider becomes aware of a serious incident.

**Definition of serious incident (Art. 3(49)):**
- Death or serious damage to health
- Serious and irreversible disruption of management/operation of critical infrastructure
- Breach of fundamental rights obligations

**Actions required:**
1. Report to market surveillance authority of Member State where incident occurred
2. Report without undue delay (within 15 days at latest, 2 days for death/serious injury)
3. Include: system identification, incident description, corrective measures

### Art. 72 — Post-Market Monitoring (Provider)

**Obligation:** Establish and document a post-market monitoring system proportionate to the nature of the AI system.

**System must include:**
- Actively and systematically collecting data on performance
- Using data from deployers (via Art. 26 obligations)
- Evaluating continuous compliance with requirements
- Feeding into risk management system (Art. 9)

---

## Authority Cooperation

### Art. 26(12) — Deployer Cooperation

Deployer must cooperate with national competent authorities in any action related to the high-risk AI system.

### Art. 21 — General Cooperation Obligation

All actors (providers, deployers, importers, distributors) must cooperate with market surveillance authorities upon reasoned request.

**What cooperation includes:**
- Providing information and documentation
- Granting access to AI system (including source code where necessary)
- Providing access to logs and monitoring data
- Facilitating testing and inspection
