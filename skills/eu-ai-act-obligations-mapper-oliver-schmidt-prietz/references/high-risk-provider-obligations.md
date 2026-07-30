# High-Risk AI System — Provider Obligations (Art. 8-17)

## Legal Basis

Art. 8-17 AI Act — Requirements for high-risk AI systems and obligations of providers.

*German: Anforderungen an Hochrisiko-KI-Systeme und Pflichten der Anbieter*

---

## Chapter III, Section 2: Requirements (Art. 8-15)

### Art. 8 — Compliance with Requirements

Providers must ensure high-risk AI systems comply with all requirements in Section 2, taking into account the intended purpose and the generally acknowledged state of the art.

---

### Art. 9 — Risk Management System

**Obligation:** Establish, implement, document, and maintain a risk management system.

**The risk management system shall:**
1. Be a continuous iterative process running throughout the entire lifecycle
2. Require regular systematic updating
3. Include the following steps:
   - (a) Identification and analysis of known and foreseeable risks
   - (b) Estimation and evaluation of risks during intended use and foreseeable misuse
   - (c) Evaluation of risks arising from post-market monitoring data (Art. 72)
   - (d) Adoption of appropriate and targeted risk management measures

**Testing requirements (Art. 9(6-8)):**
- Testing against preliminary defined metrics and probabilistic thresholds
- Testing prior to placing on market or putting into service
- Testing shall be suitable to achieve the intended purpose

| Aspect | Detail |
|--------|--------|
| Frequency | Continuous lifecycle |
| Time effort | 4/5 |
| Expertise | 4/5 |
| RACI | Technical=R, Legal=A, Compliance=C |

---

### Art. 10 — Data and Data Governance

**Obligation:** High-risk AI systems using techniques involving training with data shall be developed on the basis of training, validation, and testing data sets that meet quality criteria.

**Requirements:**
1. Data governance and management practices covering:
   - (a) Design choices
   - (b) Data collection processes and origin
   - (c) Relevant data preparation operations (annotation, labeling, cleaning, enrichment)
   - (d) Formulation of assumptions about data
   - (e) Assessment of availability, quantity, and suitability of data
   - (f) Examination for possible biases
   - (g) Identification of data gaps and how to address them

2. Training, validation, and testing datasets shall be:
   - Relevant, sufficiently representative, and to the best extent free of errors
   - Complete in view of the intended purpose
   - Have appropriate statistical properties for the target population

3. Special categories of personal data (Art. 10(5)): May be processed strictly for bias detection and correction, subject to safeguards.

| Aspect | Detail |
|--------|--------|
| Frequency | Development + ongoing |
| Time effort | 5/5 |
| Expertise | 4/5 |
| RACI | Data Science=R, Legal/DPO=A, IT=C |

---

### Art. 11 — Technical Documentation

**Obligation:** Draw up technical documentation before placing on market or putting into service, keep it up to date.

**Content per Annex IV:**
1. General description of the AI system
2. Detailed description of elements and development process
3. Monitoring, functioning, and control of the AI system
4. Risk management system description
5. Description of changes through lifecycle
6. Harmonized standards or common specifications applied
7. EU declaration of conformity
8. Performance description (accuracy, robustness, cybersecurity)

| Aspect | Detail |
|--------|--------|
| Frequency | Before market + ongoing updates |
| Time effort | 5/5 |
| Expertise | 4/5 |
| RACI | Technical=R, Legal=A, QA=C |

---

### Art. 12 — Record-Keeping (Logging)

**Obligation:** High-risk AI systems shall technically allow for automatic recording of events (logs) throughout their lifetime.

**Logging must include at minimum:**
- Recording of period of use (start/end)
- Reference database against which input data is checked
- Input data for which the search has led to a match
- Identification of natural persons involved in verification of results

| Aspect | Detail |
|--------|--------|
| Frequency | Continuous (by design) |
| Time effort | 3/5 |
| Expertise | 3/5 |
| RACI | IT/Engineering=R, Legal=A |

---

### Art. 13 — Transparency and Provision of Information to Deployers

**Obligation:** Design and develop high-risk AI systems in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret the system's output and use it appropriately.

**Instructions for use must include:**
- Identity and contact details of provider
- Characteristics, capabilities, and limitations of performance
- Intended purpose
- Level of accuracy, robustness, and cybersecurity (Art. 15)
- Any known or foreseeable circumstances that may lead to risks
- Performance regarding persons/groups on which system is intended to be used
- Input data specifications
- Human oversight measures (Art. 14)
- Computational and hardware resources needed
- Description of logging capabilities (Art. 12)
- Expected lifetime and maintenance measures

| Aspect | Detail |
|--------|--------|
| Frequency | Before market placement |
| Time effort | 4/5 |
| Expertise | 4/5 |
| RACI | Technical=R, Legal=A, Product=C |

---

### Art. 14 — Human Oversight

**Obligation:** Design and develop high-risk AI systems in such a way that they can be effectively overseen by natural persons during the period in which they are used.

**Human oversight measures must enable the individual to:**
- (a) Fully understand the capabilities and limitations of the system
- (b) Properly monitor the system's operation
- (c) Remain aware of automation bias
- (d) Correctly interpret the system's output
- (e) Decide not to use the system or to override/reverse output
- (f) Intervene in or interrupt the system (stop button)

| Aspect | Detail |
|--------|--------|
| Frequency | By design |
| Time effort | 4/5 |
| Expertise | 4/5 |
| RACI | Engineering=R, Legal=A, UX=C |

---

### Art. 15 — Accuracy, Robustness, and Cybersecurity

**Obligation:** Design and develop high-risk AI systems to achieve an appropriate level of accuracy, robustness, and cybersecurity, performing consistently throughout their lifecycle.

**Accuracy:** Declared in instructions for use, appropriate metrics.
**Robustness:** Resilient to errors, faults, or inconsistencies; technical and organizational measures for adversarial conditions.
**Cybersecurity:** Appropriate measures against unauthorized access, data poisoning, model manipulation, adversarial attacks.

| Aspect | Detail |
|--------|--------|
| Frequency | By design + ongoing testing |
| Time effort | 5/5 |
| Expertise | 5/5 |
| RACI | Engineering=R, Security=R, Legal=A |

---

## Provider Obligations (Art. 16-17)

### Art. 16 — Provider Obligations (Summary)

| # | Obligation | Article | Description |
|---|-----------|---------|-------------|
| 1 | Ensure compliance | Art. 16(a) | System meets all Chapter III, Section 2 requirements |
| 2 | Quality management system | Art. 16(b) + Art. 17 | Establish and maintain QMS |
| 3 | Technical documentation | Art. 16(c) + Art. 11 | Create and maintain per Annex IV |
| 4 | Keep logs | Art. 16(d) | When under their control |
| 5 | Conformity assessment | Art. 16(e) + Art. 43 | Before placing on market |
| 6 | Registration | Art. 16(f) + Art. 49 | Register in EU database |
| 7 | Corrective actions | Art. 16(g) | Take action if non-compliant |
| 8 | Inform authorities | Art. 16(h) | Inform of non-compliance and corrective actions |
| 9 | CE marking | Art. 16(i) + Art. 48 | Affix CE marking |
| 10 | Declaration of conformity | Art. 16(j) + Art. 47 | Draw up EU declaration |
| 11 | Cooperate with authorities | Art. 16(k) | Provide information and access |
| 12 | Accessibility requirements | Art. 16(l) | Comply with accessibility where applicable |
| 13 | Post-market monitoring | Art. 16(m) + Art. 72 | Establish monitoring system |

### Art. 17 — Quality Management System

**Obligation:** Put in place a quality management system ensuring compliance.

**QMS must include at minimum:**
1. Compliance strategy and procedures for conformity assessment
2. Techniques, procedures, and actions for design, development, and quality control
3. Testing and validation procedures (before, during, and after development)
4. Technical specifications and standards applied
5. Systems and procedures for data management (collection, analysis, labeling, storage, filtering, mining, aggregation, retention)
6. Risk management system (Art. 9)
7. Post-market monitoring system (Art. 72)
8. Procedures for serious incident reporting (Art. 73)
9. Communication with authorities, other operators, customers
10. Resource management (including supply chain management)
11. Accountability framework

| Aspect | Detail |
|--------|--------|
| Frequency | Continuous |
| Time effort | 5/5 |
| Expertise | 4/5 |
| RACI | Quality=R, Management=A, All=C |

---

## Conformity Assessment — Art. 43

### Two procedures depending on classification:

**Internal control (Annex VI):**
- For most Annex III high-risk systems
- Provider performs assessment internally
- No third-party involvement required

**Conformity assessment with notified body (Annex VII):**
- For biometric identification systems (Annex III Nr. 1)
- For systems covered by Annex I legislation requiring third-party assessment
- Notified body performs assessment

For detailed conformity assessment procedures (Track A internal control, Track B third-party assessment), decision matrix, EU Declaration content, and CE marking requirements, see [references/conformity-assessment.md](references/conformity-assessment.md).

For EU database registration process and required information fields, see [references/eu-database-registration.md](references/eu-database-registration.md).

### Timeline

| Milestone | Requirement |
|-----------|------------|
| Before market placement | Complete conformity assessment |
| Before market placement | Affix CE marking |
| Before market placement | Draw up EU declaration of conformity |
| Before market placement | Register in EU database |
| Ongoing | Maintain compliance |
| When non-compliant | Corrective actions + inform authorities |
