# EDPB DPIA Template v1.0 (10 March 2026) — Field Specification

> Source: EDPB "Template for Data Protection Impact Assessment ('DPIA')", Version 1.0, adopted 10 March 2026, for public consultation.

This reference documents the complete EDPB template structure field-by-field for use by DPIA Sentinel when generating EDPB-format output.

---

## Section 0 — Overview of the Processing

### 0.1 Controller(s)

**Purpose:** Identify the GDPR controller with all necessary contact details. For joint controllers, clearly define each party's obligations and tasks (one table per controller). (¶0)

**Assessment phase:** Intake

**Prescribed structure:**

| Column | Content |
|--------|---------|
| Controller | Name/legal entity of the controller |
| Management units responsible for the processing inside the organisation | Internal departments/units involved |
| Main establishment/point of contact or representative | Primary contact or EU representative |
| Information about the DPO or similar function, if applicable | DPO name, contact details, role |

**Notes:**
- Joint controllers: one table per controller, adding a row to identify their respective obligations and tasks.
- Obligations/tasks definition must follow EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR.

---

### 0.2 Processor(s) and Sub-processor(s)

**Purpose:** Identify all processors and sub-processors involved in the processing with an unequivocal definition of their obligations and tasks per EDPB 07/2020. (¶1)

**Assessment phase:** Intake

**Prescribed structure:**

| Column | Content |
|--------|---------|
| # | Sequential number (1, 2, ... N) |
| Processor | Name of the processor or sub-processor |
| Definition of their obligations and tasks | Unequivocal description of what the processor does |

**Notes:**
- One row per processor/sub-processor.
- Task definition must be unequivocal per EDPB Guidelines 07/2020.

---

### 0.3 Name of the Processing

**Purpose:** Provide the internal name given to the processing (from the ROPA) and, if possible, the current version explaining the history of changes made to the processing in the past. (¶2)

**Assessment phase:** Intake

**Prescribed structure:**

| Column | Content |
|--------|---------|
| Internal name given to the processing | The name as it appears in the record of processing activities |
| Current version | Version identifier + history of changes made to the processing itself |

**Notes:**
- This is the version of the *processing activity*, not the version of the DPIA document (that goes in 0.5).

---

### 0.4 Planning of the Processing

**Purpose:** Provide estimated launch and end dates for the processing activity. (¶3-4)

**Assessment phase:** Intake

**Prescribed structure:**

| Column | Content |
|--------|---------|
| Estimated launch date | Date the processing is expected to begin |
| Estimated end date or expiration conditions | Date or conditions under which processing ends (if applicable, e.g. project with limited duration) |

**Notes:**
- End date is only required if the processing is temporary.

---

### 0.5 DPIA Technical Sheet

**Purpose:** Document the DPIA's own version history, the assessment team, reference materials, reasons for conducting the DPIA, scope, completion/validation dates, and publication intent. (¶5-11)

**Assessment phase:** Intake

**Prescribed structure:**

| Field | Content |
|-------|---------|
| Current version and version log | Version of the DPIA template + history of changes to the DPIA document itself (¶5) |
| Team involved in conducting this DPIA | Names, roles, tasks, responsibilities. RACI matrix recommended (¶6) |
| Guidelines, standards, codes of conduct and other reference materials | List of materials used to conduct this DPIA (¶7) |
| Reasons to conduct the DPIA | Checkbox groups — see below (¶8) |
| Scope of this DPIA | What has been considered and what has been left out, with justification for exclusions (¶9) |
| Completion date | Date the DPIA was completed (¶10) |
| Formal validation date | Date the DPIA was formally approved by a responsible official (Managing Director, CEO, etc.) (¶10) |
| Publication intent | Checkbox: No / Yes published (how?) / Yes shared externally (how?) (¶11) |

**Trigger reason checkboxes (multiple may be selected):**

*Group 1 — New processing, DPIA likely required due to high risk (Art. 35(3) GDPR mandatory):*

| Checkbox | Criterion |
|----------|-----------|
| ☐ | Systematic and extensive evaluation of personal aspects based on automated processing, including profiling, on which decisions producing legal effects or similarly significant effects are based |
| ☐ | Processing on a large scale of special categories of data (Art. 9(1)) or criminal convictions/offences data (Art. 10) |
| ☐ | Systematic monitoring of a publicly accessible area on a large scale |

*Group 2 — New processing, DPIA likely required under national law:*

| Checkbox | Criterion |
|----------|-----------|
| ☐ | National law requirement (provide explanation) |

*Group 3 — New processing, DPIA likely required following EDPB and national guidance:*

| Checkbox | Criterion |
|----------|-----------|
| ☐ | Evaluation or scoring, including profiling and predicting |
| ☐ | Automated decision-making with legal or similar significant effect |
| ☐ | Systematic monitoring |
| ☐ | Sensitive data or data of a highly personal nature |
| ☐ | Data processed on a large scale |
| ☐ | Matching or combining datasets |
| ☐ | Data concerning vulnerable data subjects |
| ☐ | Innovative use or applying new technological or organisational solutions |
| ☐ | Processing that prevents data subjects from exercising a right or using a service or a contract |
| ☐ | Other (e.g. national list) — provide explanation |

*Group 4 — New processing, DPIA necessary or beneficial:*

| Checkbox | Criterion |
|----------|-----------|
| ☐ | DPO opinion or recommendation |
| ☐ | Data subjects' (or their representatives') opinion or recommendation |
| ☐ | Required by a code of conduct, standard, best practice, etc. |
| ☐ | Other (e.g. managing risk, demonstrating accountability, building trust) — provide explanation |

*Group 5 — Existing high-risk processing with changed risks:*

| Checkbox | Criterion |
|----------|-----------|
| ☐ | Data processing has changed |
| ☐ | The organisational or societal context for the processing activity has changed |

With narrative: "How?" explanation required.

**Notes:**
- More than one checkbox may be selected across all groups.
- Sensitive information (e.g. security details) should not be included in published versions (¶11).

---

## Section 1 — Systematic Description of the Processing

### 1.1.a Processed Personal Data

**Purpose:** List all processed personal data items with their type, data subject category, and identification of any special categories. (¶12)

**Assessment phase:** Description

**Prescribed structure:**

| Column | Content |
|--------|---------|
| # | Sequential number (1, 2, ... N) |
| Processed personal data (item or element) | Name/identifier of the data item |
| Explanation (data type, data subject category, additional details) | Type of data, which category of data subjects it relates to |
| Special category of personal data | Checkbox: No / Yes + sub-checkboxes (see below) |

**Special category sub-checkboxes (when "Yes" is selected):**

| Checkbox | Category |
|----------|----------|
| ☐ | Data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade union membership |
| ☐ | Genetic data |
| ☐ | Biometric data for the purpose of uniquely identifying a natural person |
| ☐ | Data concerning health |
| ☐ | Data concerning a natural person's sex life or sexual orientation |

**Notes:**
- Each data item gets its own row.
- The sequential numbers are cross-referenced by later sections (1.1.b, 1.1.c, 2.1.b, 2.2.a, 2.2.b).

---

### 1.1.b Purposes of the Processing

**Purpose:** Identify the specific and explicit reasons for processing the personal data, including the objectives the processing aims to achieve and how it contributes to that result. (¶13)

**Assessment phase:** Description

**Prescribed structure:**

| Column | Content |
|--------|---------|
| # | Sequential number (1, 2, ... N) |
| Purpose: specific and explicit reasons for processing the personal data | Description of purpose, including operational goals (business process, policy, UX, safety/security) |
| Personal data involved (considering personal data listed in 1.1.a) and justification | Cross-reference to 1.1.a items + justification of why those data items are needed for this purpose |

**Notes:**
- Each purpose gets its own numbered row.
- Purposes are cross-referenced by sections 2.1.a and 2.2.a.

---

### 1.1.c Secondary or Compatible Uses

**Purpose:** Identify any secondary or compatible uses of the data, applying the purpose limitation principle. State whether data from 1.1.a may be re-used for another purpose, under what conditions, and provide a compatibility assessment. (¶14)

**Assessment phase:** Description

**Prescribed structure:**

| Column | Content |
|--------|---------|
| # | Sequential number (1, 2, ... N) |
| Secondary or compatible uses of the data | Description of the secondary/compatible use |
| Personal data involved (considering personal data listed in 1.1.a), under what conditions and assessment of compatibility | Cross-reference to 1.1.a + conditions + compatibility assessment |

**Notes:**
- May refer to an existing compatibility analysis documented elsewhere.
- Cross-referenced by section 2.1.a (legal basis must cover secondary uses too).

---

### 1.1.d Nature, Scope and Context of the Processing

**Purpose:** Describe the nature (operations, technologies), scope (volume, scale, frequency, duration from data subject perspective), and context (use cases, business processes, relationship with data subjects, vulnerable groups) of the processing. (¶15-17)

**Assessment phase:** Description

**Prescribed structure:**

| Field | Content |
|-------|---------|
| Nature of the processing | How personal data will be handled: operations involved, technologies used (¶15) |
| Scope of the processing | Volume/scale (number of data subjects, data items), geographical and organisational reach, frequency or duration from data subject's perspective (per use/session, periodic, continuous/near-continuous, event-driven/occasional) (¶16) |
| Context of the processing | Use cases, supported business processes, status of controller, relationship with data subjects, data subject categories, potential vulnerable groups (¶17) |
| Is this a cross-border processing? | Checkbox: No / Yes (justification and details) |
| Is personal data going to be transferred to a recipient in a third country or international organisation? | Checkbox: No / Yes (justification and details) |

**Notes:**
- Cross-border processing: processing in context of establishments in more than one Member State, or processing substantially affecting data subjects in more than one Member State.
- International transfers: transfers to a third country or international organisation.

---

### 1.2 Functional Description

**Purpose:** Outline the processing in a structured way, decomposed into phases or stages. Describe the full data lifecycle including controller, processors and sub-processors. (¶18-19)

**Assessment phase:** Description

**Prescribed structure:**

| Column | Content |
|--------|---------|
| # | Sequential number (1, 2, ... N) |
| Processing phase or stage | Name/description of the phase |
| Type of operations | Checkboxes: ☐ Collection / ☐ Use / ☐ Storage / ☐ Sharing and Transfer / ☐ Deletion and Destruction |
| Explanation | Details of what happens in this phase, covering data lifecycle aspects |

**Data lifecycle aspects to cover per ¶19:**
- **Collection:** What data is collected, how, sources, information provided to data subjects.
- **Use:** Operations performed, technologies, automated decision-making/profiling, combination with other datasets.
- **Storage:** Where and how stored (physical, cloud, third-party), who has access.
- **Sharing and Transfer:** Sharing to third parties, transfers outside EU, legal mechanisms (SCCs, adequacy decisions).
- **Deletion and Destruction:** Criteria and procedures for secure deletion, methods for permanent erasure.

**Notes:**
- Should be supplemented with one or more data flow diagrams or similar figures.
- Processing phases here are cross-referenced by section 1.3.

---

### 1.3 Means of Processing, Supporting Assets and Underlying Architecture

**Purpose:** From the functional description in 1.2, explain the means of processing and provide an inventory of essential supporting assets. Assets are resources used to process personal data, representing vectors for both value and risk. (¶20)

**Assessment phase:** Asset Inventory

**Prescribed structure:**

| Column | Content |
|--------|---------|
| Processing phase or stage (considering the functional description under 1.2) | Cross-reference to 1.2 phases |
| Means of processing and supporting assets | List of assets grouped by type |
| Explanation | How each asset relates to the processing and risk |

**Asset type categories:**
- **Hardware, infrastructure, and network assets:** Servers, laptops, mobile devices, storage media, scanners, VPN gateways
- **Software:** Database engines, business applications
- **APIs and models:** API endpoints, ML/AI models
- **Personnel:** Users, administrators, developers, operators, support staff, decision-makers
- **Sites and premises:** Data centres, archives
- **Organisational assets:** Policies, procedures, contracts with processors/sub-processors

**Notes:**
- Include only assets essential for risk analysis, i.e. whose compromise would plausibly impact rights and freedoms in a non-trivial way (¶20).
- Focus on: assets directly storing/processing personal data, assets controlling access or protecting data, exposed/high-impact components (public-facing portals, APIs, data-sharing interfaces).
- Very small, generic, or easily substitutable elements do not need individual listing.
- Group by logical module, technical layer, or function. Keep detailed per-device/per-service inventory in separate technical documentation (¶20).
- Balance completeness and manageability.

---

### 1.4 Compliance with Approved Codes of Conduct

**Purpose:** Identify compliance with approved codes of conduct. Analyse the compliance obligation (if applicable) or the reasons that make compliance necessary or beneficial. (¶21)

**Assessment phase:** Description

**Prescribed structure:**

| Column | Content |
|--------|---------|
| # | Sequential number (1, 2, ... N) |
| Code of conduct | Name/reference of the applicable code of conduct |
| Explanation | Details of applicability and rationale |
| Compliance reason | Checkbox: ☐ Compliance is likely to be required (legal obligation) — Why? / ☐ Compliance is necessary or beneficial — Why? |

---

## Section 2 — Analysis of the Processing

### 2.1.a Legal Basis

**Purpose:** Analyse the legal basis of the processing in relation to each purpose (from 1.1.b) and each secondary/compatible use (from 1.1.c). For Art. 6(1)(f), conduct a balancing test (legitimate interest assessment). (¶22-23)

**Assessment phase:** Necessity

**Prescribed structure:**

| Column | Content |
|--------|---------|
| Purpose/use (considering 1.1.b on processing purposes and 1.1.c on secondary or compatible purposes) | Cross-reference to the specific purpose or secondary use |
| Legal basis (Article 6(1) GDPR) | Checkbox selection — see below |
| Justification | Reasoning; if Art. 6(1)(f), include LIA balancing test |

**Legal basis checkboxes (Art. 6(1) GDPR):**

| Checkbox | Basis |
|----------|-------|
| ☐ (a) | The data subject has given consent to the processing of his or her personal data for one or more specific purposes |
| ☐ (b) | The processing is necessary for the performance of a contract to which the data subject is party or in order to take steps at the request of the data subject prior to entering into a contract |
| ☐ (c) | The processing is necessary for compliance with a legal obligation to which the controller is subject |
| ☐ (d) | The processing is necessary in order to protect the vital interests of the data subject or of another natural person |
| ☐ (e) | The processing is necessary for the performance of a task carried out in the public interest or in the exercise of official authority vested in the controller |
| ☐ (f) | The processing is necessary for the purposes of the legitimate interests pursued by the controller or by a third party, except where such interests are overridden by the interests or fundamental rights and freedoms of the data subject which require protection of personal data, in particular where the data subject is a child |

**Notes:**
- One row per purpose/use from 1.1.b and 1.1.c.
- For Art. 6(1)(f): must include a legitimate interest assessment (LIA) with balancing test per EDPB Guidelines 1/2024.
- If the analysis relies on hypotheses about implemented measures or residual risks, these must be cross-referenced to the appropriate template sections.

---

### 2.1.b Reasons to Lift the Processing Prohibition

**Purpose:** For each special category data item identified in 1.1.a, identify and justify the reason that lifts the prohibition on processing under Art. 9(2) GDPR. (¶24)

**Assessment phase:** Necessity

**Prescribed structure:**

| Column | Content |
|--------|---------|
| Special category of personal data (item or element, considering 1.1.a) | Cross-reference to 1.1.a item(s) flagged as special category |
| Reasons to lift the processing prohibition (Article 9(2) GDPR) | Checkbox selection — see below |
| Justification | Reasoning for why the selected exception applies |

**Art. 9(2) checkboxes:**

| Checkbox | Reason |
|----------|--------|
| ☐ (a) | Explicit consent for one or more specified purposes (except where Union or Member State law provides the prohibition may not be lifted by the data subject) |
| ☐ (b) | Necessary for obligations/rights in employment and social security/protection law (authorised by Union or Member State law or collective agreement with appropriate safeguards) |
| ☐ (c) | Necessary to protect vital interests where data subject is physically or legally incapable of giving consent |
| ☐ (d) | Carried out by a not-for-profit body with political, philosophical, religious or trade union aim, relating solely to members/former members/regular contacts, not disclosed outside without consent |
| ☐ (e) | Data manifestly made public by the data subject |
| ☐ (f) | Necessary for establishment, exercise or defence of legal claims or courts acting in judicial capacity |
| ☐ (g) | Necessary for reasons of substantial public interest (Union or Member State law, proportionate, respecting essence of data protection right, with suitable safeguards) |
| ☐ (h) | Necessary for preventive/occupational medicine, working capacity assessment, medical diagnosis, health/social care provision/management (Union or Member State law or contract with health professional, subject to Art. 9(3) conditions) |
| ☐ (i) | Necessary for public interest in public health (cross-border health threats, quality/safety of healthcare/medicinal products/medical devices; Union or Member State law with suitable safeguards, in particular professional secrecy) |
| ☐ (j) | Necessary for archiving in public interest, scientific/historical research, or statistical purposes per Art. 89(1) (Union or Member State law, proportionate, respecting essence of data protection right, with suitable safeguards) |

**Notes:**
- Only required when special category data is identified in 1.1.a.
- One row per special category data item.

---

### 2.2.a Data Minimisation and Retention Periods

**Purpose:** Document in detail the justification to process each personal data item, identifying recipients and providing retention periods with justifications. (¶25)

**Assessment phase:** Necessity

**Prescribed structure:**

| Column | Content |
|--------|---------|
| Processed personal data (item or element, considering 1.1.a) | Cross-reference to 1.1.a |
| Justification of the need and relevance of the data | Why this data item is necessary and relevant |
| Recipients | Who receives this data |
| Justification | Why these recipients need the data |
| Retention period | How long the data is kept |
| Justification | Why this retention period is appropriate |

**Notes:**
- One row per data item from 1.1.a.
- Design choices must also be justified.

---

### 2.2.b Data Quality

**Purpose:** Provide data quality metrics, requirements, or thresholds for each data item. (¶26)

**Assessment phase:** Necessity

**Prescribed structure:**

| Column | Content |
|--------|---------|
| Processed personal data (item or element, considering table 1.1.a) | Cross-reference to 1.1.a |
| Quality metrics, requirements or thresholds | Specific accuracy/completeness/timeliness standards |
| Justification | Why these quality requirements are appropriate |

---

### 2.3.a Measures Supporting Compliance with Principles in Article 5(1)(a-f) GDPR

**Purpose:** List measures supporting compliance with Art. 5(1)(a-f) GDPR principles, discuss their appropriateness and effectiveness, and describe implementation status. (¶27)

**Assessment phase:** Mitigations

**Prescribed structure:**

| Column | Content |
|--------|---------|
| Compliance with Article 5(1)(a-f) GDPR principles | Principle name (prescribed rows below) |
| List of supporting measures | Measures implemented or planned for this principle |
| Discussion of appropriateness and effectiveness | Why these measures are suitable and how well they work |
| Implementation status | Checkbox: ☐ Planned / ☐ Partially implemented / ☐ Implemented |

**Prescribed rows (one per principle):**

1. Fairness principle
2. Transparency principle
3. Purpose limitation principle
4. Data minimisation principle
5. Accuracy principle
6. Storage limitation principle
7. Integrity and confidentiality principle
8. Accountability principle

**Implementation status definitions (¶27):**
- **Planned:** The safeguard is only at the intention or design stage; identified as necessary but not yet deployed in production.
- **Partially implemented:** Some elements of the measure are in place, but important aspects are missing or incomplete.
- **Implemented:** The measure exists, is deployed, and is effectively operating in the live environment (not just on paper); there is evidence the control works as intended.

---

### 2.3.b Measures Supporting the Exercise of Data Subjects' Rights

**Purpose:** List measures supporting data subjects' rights, discuss their appropriateness and effectiveness, and describe implementation status. (¶28)

**Assessment phase:** Mitigations

**Prescribed structure:**

| Column | Content |
|--------|---------|
| Data subject rights | Right category (prescribed rows below) |
| List of supporting measures | Measures for this right |
| Discussion of appropriateness and effectiveness | Suitability and efficacy |
| Implementation status | Checkbox: ☐ Planned / ☐ Partially implemented / ☐ Implemented |

**Prescribed rows:**

1. Information to be provided to the data subjects (Articles 12, 13 and 14 GDPR)
2. Right of access and to data portability (Articles 15 and 20 GDPR)
3. Right to rectification and to erasure (Articles 16, 17 and 19 GDPR)
4. Right to object and to restriction of processing (Articles 18, 19 and 21 GDPR)
5. Right not to be subject to a decision based solely on automated processing (Article 22 GDPR)

---

### 2.3.c Measures Supporting Compliance with Other GDPR Requirements

**Purpose:** List measures supporting compliance with consent, processor relationships, and international transfers, discuss their appropriateness and effectiveness, and describe implementation status. (¶29)

**Assessment phase:** Mitigations

**Prescribed structure:**

| Column | Content |
|--------|---------|
| Compliance with other GDPR requirements | Requirement category (prescribed rows below) |
| List of supporting measures | Measures for this requirement |
| Discussion of appropriateness and effectiveness | Suitability and efficacy |
| Implementation status | Checkbox: ☐ Planned / ☐ Partially implemented / ☐ Implemented |

**Prescribed rows:**

1. Requirements on the provisions and withdrawal of consent (Article 7 GDPR)
2. Relationship with processors (Article 28 GDPR)
3. Safeguards relating to international transfer(s) (Chapter V GDPR)

---

### 2.3.d Measures Supporting Data Protection by Design and by Default

**Purpose:** List measures supporting data protection by design and by default (Art. 25 GDPR), discuss their appropriateness and effectiveness, and describe implementation status. (¶30)

**Assessment phase:** Mitigations

**Prescribed structure:**

| Column | Content |
|--------|---------|
| Data protection by design and by default (Article 25 GDPR) | Description of the DPbD measure |
| List of supporting measures | Specific measures |
| Discussion of appropriateness and effectiveness | Suitability and efficacy |
| Implementation status | Checkbox: ☐ Planned / ☐ Partially implemented / ☐ Implemented |

**Notes:**
- Multiple rows allowed (one per DPbD measure).
- Refers to EDPB Guidelines 4/2019 on Article 25.

---

### 2.3.e Measures Supporting Security of Processing

**Purpose:** List measures supporting security of processing (Art. 32 GDPR), discuss their appropriateness and effectiveness, and describe implementation status. (¶31)

**Assessment phase:** Mitigations

**Prescribed structure:**

| Column | Content |
|--------|---------|
| Security of processing (Article 32 GDPR) | Security domain or measure category |
| List of supporting measures | Specific measures |
| Discussion of appropriateness and effectiveness | Suitability and efficacy |
| Implementation status | Checkbox: ☐ Planned / ☐ Partially implemented / ☐ Implemented |

**Security domains to consider (Art. 32):**
- Pseudonymisation and encryption of personal data
- Ability to ensure ongoing confidentiality of processing systems and services
- Ability to ensure ongoing integrity of processing systems and services
- Ability to ensure ongoing availability and resilience of processing systems and services
- Ability to restore availability and access to personal data in a timely manner in the event of a physical or technical incident

**Notes:**
- Multiple rows allowed.
- Implementation status is mandatory: Planned / Partially implemented / Implemented.

---

## Section 3 — Considerations on Necessity and Proportionality

### 3.1 Impacts of the Processing on the Rights and Freedoms of Data Subjects

**Purpose:** Identify inherent-by-design risks: threats posed by the processing as designed and planned (even when everything works as intended), how they materialise, their risk sources, and their impacts on data subjects' rights and freedoms. (¶32)

**Assessment phase:** Inherent Risks (Track A)

**Prescribed structure:**

| Column | Content |
|--------|---------|
| # | Sequential number (1, 2, ... N) |
| Threats posed by the processing, as it has been designed and planned to be implemented (including technical, legal/contractual and organisational measures to mitigate risk(s)) | Description of the inherent-by-design threat |
| How can it be materialised? | Materialisation scenario |
| Risk sources (purpose, wrong design and weaknesses, exposures, etc.) | Origin/underlying cause: purpose of processing, design choices, weaknesses (e.g. unique identifiers, long retention), exposures |
| Impact on data subjects' rights and freedoms | Consequences: physical, material, or non-material damage (see Recital 75 GDPR) |

**Key definitions (¶32):**
- **Threat:** Any circumstance or event with the potential to adversely impact data subjects' rights and freedoms (e.g. linking, identifying, inaccuracy, data disclosure).
- **Risk source:** The origin from which a threat can materialise (e.g. purpose, wrong design, weaknesses, exposures).
- **Impact:** Consequences from threat materialisation, always considering data subjects' rights and freedoms.

**Notes:**
- These are risks that exist even if everything works exactly as designed and all actors follow the rules.
- Threats flow mainly from: processed personal data (1.1.a), purpose (1.1.b), nature/scope/context (1.1.d).
- Scenarios from this table are combined with 4.1.a scenarios in section 4.1.c (inherent risk assessment).

---

### 3.2 Assess the Necessity of the Processing

**Purpose:** Evaluate if the envisaged processing is effective and the least intrusive for data subjects' rights and freedoms. Provide evidence of alternatives considered. (¶33)

**Assessment phase:** Necessity + Proportionality

**Prescribed structure:** Narrative field.

**Content requirements:**
- Demonstrate the processing works as intended (at least to the appropriate/required level).
- Evaluate least-intrusiveness.
- Provide evidence concerning different considered alternatives and their effectiveness in achieving the purpose.
- Provide justification.

**Notes:**
- Necessity is a pre-condition for proportionality (must be established before 3.3).

---

### 3.3 Assess the Proportionality of the Processing

**Purpose:** Discuss the importance of the processing and its potential benefits vs. its impact on data subjects' rights and freedoms. Conduct a balance of advantages vs. disadvantages. (¶34)

**Assessment phase:** Necessity + Proportionality

**Prescribed structure:** Narrative field.

**Content requirements:**
- Discuss importance of the processing and its potential benefits for the data subject, the organisation, and collectively.
- Compare potential impacts on rights/freedoms (from 3.1) with advantages resulting from the processing.
- Balance advantage/disadvantage, benefit/cost.
- Answer: "Is the processing envisaged to fulfil the purpose a proportionate response to the need, given the limitations to data protection and privacy rights?"
- Provide evidence and justification with complete and updated information.

**Notes:**
- Necessity (3.2) is a pre-condition for proportionality.
- References EDPS "Guidelines on assessing the proportionality of measures that limit the fundamental rights to privacy and to the protection of personal data."

---

## Section 4 — Risk Assessment and Management

### 4.1.a Impacts Caused by Non-Default, Accidental, Unlawful, or Abnormal Events

**Purpose:** Identify operational/cybersecurity threats: how non-default, accidental, unlawful, or abnormal events pose threats to data subjects' rights and freedoms. These materialise when something does not go as intended (unlike 3.1 which covers by-design risks). (¶35)

**Assessment phase:** Inherent Risks (Track B)

**Prescribed structure:**

| Column | Content |
|--------|---------|
| # | Sequential number (1, 2, ... N) |
| Threats posed by malfunctions and deviations from design and default, threats to data confidentiality, integrity and availability (related to cybersecurity), etc. | Description of the operational/security threat |
| How can it be materialised? | Materialisation scenario |
| Risk sources (exposures and errors, vulnerabilities etc.) | Root causes: software bugs, misconfigurations, wrong access rights, operational errors, lack of maintenance, insider abuse, external attacks |
| Impacts on data subjects' rights and freedoms | Consequences |

**Minimum mandatory threat identification:**
- Illegitimate access to personal data
- Undesired modification of personal data
- Disappearance of personal data

**Typical risk sources (¶35):**
- Software bugs
- Misconfigurations
- Wrong access rights
- Operational errors (sending data to wrong recipient, wrong dataset used, forgotten de-provisioning)
- Lack of maintenance (unpatched vulnerabilities, outdated components)
- Insider abuse (staff exceeding authorised use)
- External attacks (phishing, ransomware)

**Notes:**
- These threats are different from 3.1: they materialise when there is a deviation from intended/compliant state or when there are malicious actors.
- Scenarios from this table are combined with 3.1 scenarios in section 4.1.c (inherent risk assessment).

---

### 4.1.b Method

**Purpose:** Explain the risk assessment and management methodology. Provide information necessary to understand and interpret the risk assessment outputs. (¶36)

**Assessment phase:** Inherent Risks (Track A+B)

**Prescribed structure:** Narrative field.

**Content requirements:**
- Likelihood levels and their meanings (often a 2 to 5 level scale)
- Severity levels and their meanings (often a 2 to 5 level scale)
- Risk metrics (how risk level is calculated)
- How risks are prioritised
- Risk acceptance levels/thresholds
- If an established method is used, provide link to external source

**Notes:**
- Risk level typically = likelihood x severity, using qualitative scales (e.g. low/medium/high) (¶37).
- A risk in data protection may be deemed non-acceptable even with low likelihood if severity is very high (footnote 9).

---

### 4.1.c Inherent Risk Assessment

**Purpose:** Combine threats from 3.1 (by-design) and 4.1.a (operational) into a unified inherent risk assessment. Estimate likelihood and severity, identify modulating factors, determine risk level, and assess acceptability. (¶37-40)

**Assessment phase:** Inherent Risks (Track A+B)

**Prescribed structure:**

| Column | Content |
|--------|---------|
| # | Sequential number (1, 2, ... N) |
| Risks to the data subject's rights and freedoms (include scenarios laid out in the first column in 3.1 and 4.1.a) | Risk scenario description (from 3.1 + 4.1.a) |
| Likelihood | Likelihood level per method in 4.1.b |
| Severity | Severity level per method in 4.1.b |
| Modulating factors | Characteristics that increase or decrease likelihood/severity without being the primary threat source |
| Risk level | Calculated per method in 4.1.b (typically likelihood x severity) |
| Discuss whether the risk is acceptable or not | Acceptability assessment against thresholds defined in 4.1.b |

**Modulating factors (¶37):**
- *Aggravating (upward):* Very large number of data subjects, high data sensitivity, data subjects in dependency/vulnerability (children, patients, workers, migrants), high exposure to external adversaries.
- *Mitigating (downward):* Design choices and measures from section 2.3.

**Notes:**
- Inherent risk = risk level assigned assuming the baseline/initial set of planned measures (¶37).
- Non-acceptable risks must be clearly identified — they require additional mitigation before processing can proceed (¶39).
- Can be supplemented with diagrams, charts, maps, priority lists, etc. (¶40).

---

### 4.2.a Additional Mitigating Measures

**Purpose:** Detail additional (not initially planned) measures to manage specific unacceptable risks from 4.1.c. Describe implementation status and discuss appropriateness and effectiveness. (¶41)

**Assessment phase:** Mitigations + Residual Risk

**Prescribed structure:**

| Column | Content |
|--------|---------|
| # | Sequential number (1, 2, ... N) |
| Technical, legal/contractual and organisational measures | Description of the additional measure |
| Mitigated risks (considering 4.1.c) | Cross-reference to risk(s) from 4.1.c that this measure addresses |
| Discussion of appropriateness and effectiveness | Why the measure is suitable and how well it works |
| Implementation status | Checkbox: ☐ Planned / ☐ Partially implemented / ☐ Implemented |

**Notes:**
- Include all types of measures: compliance with Art. 5 principles, data subject rights, other GDPR requirements, DPbD, and security measures (same categories as section 2.3).
- These are additional measures beyond the baseline measures already documented in section 2.3.

---

### 4.2.b Residual Risk Assessment

**Purpose:** Reassess risks after applying the additional mitigating measures from 4.2.a. Determine residual risk levels and acceptability. (¶42-43)

**Assessment phase:** Mitigations + Residual Risk

**Prescribed structure:**

| Column | Content |
|--------|---------|
| # | Sequential number (1, 2, ... N) |
| Reassessed risks to the data subject's rights and freedoms | Risk scenario (from 4.1.c) |
| Additional mitigating measures that apply | Cross-reference to measure(s) from 4.2.a |
| Residual likelihood | Updated likelihood after additional measures |
| Residual severity | Updated severity after additional measures |
| Residual risk level | Calculated residual risk level |
| Discuss whether the risk is acceptable or not | Acceptability assessment |

**Notes:**
- Residual risk = risk remaining after the controller has reflected on unacceptable risks, added additional measures, and assessed how far those measures reduce inherent risk (¶42).
- Can be supplemented with visual aids (diagrams, charts, maps, priority lists) (¶43).

---

### 4.2.c Plan

**Purpose:** Provide the implementation plan for additional measures, including activities, responsibilities, timelines, and monitoring/review schedules. (¶44)

**Assessment phase:** Mitigations + Residual Risk

**Prescribed structure:** Narrative field.

**Content requirements:**
- Specific activities needed to implement the new measures
- Responsible team/persons
- Timelines
- How risks will be monitored, reviewed, and updated once processing is carried out
- Links to external documentation or annexes with details

---

## Section 5 — Involvement of Interested Parties

### 5.1 DPO Advice

**Purpose:** Document the DPO's (or similar function's) opinion, conclusions, and recommendations concerning the envisaged processing, and explain how their advice was implemented. (¶45-46)

**Assessment phase:** Art. 36 Check

**Prescribed structure:** Narrative field.

**Content requirements:**
- DPO's opinion, conclusions and recommendations (e.g. input on risks and mitigation) (¶45)
- Actions taken following DPO's advice through the DPIA process and planning (¶46)
- Answer the question: "How has the controller implemented the DPO's advice?"

---

### 5.2 Views of Data Subjects or Their Representatives

**Purpose:** Document data subjects' (or their representatives') opinions, conclusions, and recommendations, and explain their participation in the DPIA process. (¶47-48)

**Assessment phase:** Art. 36 Check

**Prescribed structure:** Narrative field.

**Content requirements:**
- Data subjects' (or their representatives') opinion, conclusions and recommendations (¶47)
- Explanation of their participation in the DPIA process (¶48)
- If data subjects did not participate: explain why it was not considered appropriate or why it was not possible

---

## Section 6 — Conclusion and Decision

**Purpose:** Conclude with the decision on data processing viability based on the full assessment. (¶49-50)

**Assessment phase:** Documentation

**Prescribed structure:** Four mutually exclusive checkbox outcomes:

| Checkbox | Decision | Description |
|----------|----------|-------------|
| ☐ | REJECTED | The processing must be abandoned (risks unacceptable, required tests cannot be passed, advised by DPO/data subjects/SA, etc.) |
| ☐ | CONSULTATION | The processing will be consulted with the SA — select sub-reason(s) below |
| ☐ | APPROVED | The processing may proceed immediately. Residual risks are acceptable and there is no national law requiring consultation or prior authorisation (Art. 36(5) GDPR) |
| ☐ | CONDITIONALLY APPROVED | The processing may proceed only after specified conditions are met |

**CONSULTATION sub-reasons:**

| Checkbox | Reason |
|----------|--------|
| ☐ (a) | The data controller cannot find sufficient measures to reduce the risks to an acceptable level (residual risks are still high) and does not wish to abandon the processing |
| ☐ (b) | National law requires the controller to consult with, and/or obtain prior authorisation from, the SA in relation to processing for performance of a task in the public interest, including social protection and public health (Article 36(5) GDPR) |

**CONDITIONALLY APPROVED conditions:**

| Field | Content |
|-------|---------|
| Condition 1 | Description of condition that must be met |
| Condition 2 | Description of condition that must be met |
| ... | Additional conditions as needed |

**Optional justification:** Narrative field to explain/justify the decision made (¶50).

**Notes:**
- Conditional approval conditions may link to previous template sections (e.g. measures in 4.2).

---

## Assessment Phase Cross-Reference

| EDPB Section | DPIA Sentinel Phase | Data Source |
|---|---|---|
| 0 Overview | Intake | User-provided controller/processor info |
| 1.1 Description | Description | User-provided processing details |
| 1.2 Functional | Description | Data lifecycle analysis |
| 1.3 Assets | Asset Inventory | User-provided + guided inventory |
| 1.4 Codes of conduct | Description | User-provided |
| 2.1 Lawfulness | Necessity | Legal basis analysis |
| 2.2 Minimisation | Necessity | Data minimisation review |
| 2.3 Measures | Mitigations | Compliance measures inventory |
| 3 Necessity/Proportionality | Necessity + Proportionality | Upstream gate analysis |
| 4.1 Risk Assessment | Inherent Risks (Track A+B) | Risk identification + scoring |
| 4.2 Action Plan | Mitigations + Residual Risk | Mitigation planning |
| 5 Interested Parties | Art. 36 Check | DPO + data subject consultation |
| 6 Conclusion | Documentation | Final verdict |
