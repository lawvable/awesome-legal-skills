# MDCG 2025-6: Medical Devices and the AI Act

Medical Device Coordination Group guidance on the interplay between the AI Act and EU medical device regulations (MDR/IVDR).

| Aspect | Detail |
|--------|--------|
| Institution | MDCG (Medical Device Coordination Group) |
| Date | 2025 |
| Source URL | https://health.ec.europa.eu/document/download/medical-devices-ai-act |
| NotebookLM Source ID | 34a006c8-... |

*German: MDCG 2025-6: Medizinprodukte und die KI-Verordnung*

---

## Introduction

This document (AIB 2025-1 / MDCG 2025-6) provides a first set of answers to frequently asked questions related to the joint application of the AI Act (AIA) and the Medical Devices Regulation (MDR) or In Vitro Diagnostic Medical Devices Regulation (IVDR) for manufacturers. It is primarily aimed at medical device manufacturers, notified bodies, and competent authorities.

The document has been endorsed by the Artificial Intelligence Board (AIB) and the Medical Device Coordination Group (MDCG). It is not a European Commission document and cannot be regarded as reflecting an official position. Only the Court of Justice of the European Union can give binding interpretations of Union law.

### Key Terminology

- **MDAI (Medical Device Artificial Intelligence):** AI systems used for medical purposes. All references also cover MDR Annex XVI products, accessories to medical devices, in vitro diagnostic medical devices, and accessories to IVD medical devices.
- **Manufacturer (MDR/IVDR):** Equivalent to "provider" under the AIA.
- **Deployer (AIA, Art. 3(4)):** A natural or legal person, public authority, agency, or other body using AI systems under their authority (excluding personal non-professional use). The AIA concept of "deployer" is not equivalent to "user" under MDR/IVDR (which means any healthcare professional or lay person who uses a device).

### Regulatory Relationship

The MDR and IVDR address risks related to medical device software but do not explicitly address risks specific to AI systems. The AIA complements the MDR/IVDR by introducing requirements to address hazards and risks for health, safety, and fundamental rights specific to AI systems. This means a simultaneous and complementary application of both the MDR/IVDR and the AIA for medical devices containing one or more high-risk AI systems.

In accordance with Article 8(2) AIA, manufacturers of MDAI have the option of integrating the necessary testing, reporting processes, information, and documentation required under the AIA into existing MDR/IVDR documentation and procedures. Manufacturers are strongly encouraged to use this flexibility, while ensuring full compliance with all applicable requirements.

---

## Scope of Application and Classification

### When Does the AIA Apply to Medical Device Software?

"Medical device software" (MDSW), per MDCG 2019-11, refers to software intended to fulfil a medical purpose as defined in Article 2(1) MDR or Article 2(2) IVDR. The AIA defines an AI system in Article 3(1) as a machine-based system designed to operate with varying levels of autonomy, that may exhibit adaptiveness after deployment, and that infers from its input how to generate outputs (predictions, content, recommendations, or decisions) that can influence physical or virtual environments.

### High-Risk Classification of MDAI

A MDAI is considered a high-risk AI system under Article 6(1) AIA if it meets both conditions:

1. The MDAI is a safety component, or the AI system is itself a medical device; **and**
2. The MDAI is subject to a third-party conformity assessment by a notified body under the MDR/IVDR.

#### Classification Table

| Classification | Notified Body Involved? | AIA High-Risk (Art. 6(1))? |
|---|---|---|
| MDR Class I (non-sterile, non-measuring, non-reusable surgical) | No | No |
| MDR Class I (sterile, measuring, reusable surgical) | Yes | Yes |
| MDR Class IIa, IIb, III | Yes | Yes |
| MDR Annex XVI | Yes | Yes |
| IVDR Class A (non-sterile) | No | No |
| IVDR Class A (sterile) | Yes | Yes |
| IVDR Class B, C, D | Yes | Yes |
| In-house device (Art. 5(5) MDR/IVDR) | No | No |

### AIA Classification Does Not Affect MDR/IVDR Risk Class

Classification as high-risk under Article 6(1) AIA does not imply that a medical device falls in a higher risk class under the MDR/IVDR. Conversely, it is the MDR/IVDR classification that determines whether the AI system qualifies as high-risk under the AIA. The application of Article 5 AIA (prohibited practices) and Article 50 AIA (transparency obligations) does not depend on MDR/IVDR classification.

### MDR Annex XVI Devices

The AIA applies to devices covered by the MDR, including Annex XVI devices, if they are or contain an AI system and fulfil the conditions of Article 6(1) AIA (except non-invasive devices classified as Class I).

---

## Requirements

### Management Systems

#### Lifecycle Management (Q5)

Both the MDR/IVDR and AIA require manufacturers to manage the entire lifecycle of MDAI. The MDR/IVDR ensure the device remains safe and performant throughout use. The AIA reinforces this by requiring:

- Continuous review, oversight, and consistent performance throughout the lifecycle
- Post-market monitoring proportionate to the nature and risks of the AI system
- Design choices that allow natural persons to oversee the functioning of high-risk MDAI
- A risk management system as a continuous iterative process throughout the entire lifecycle
- Analysing deployer data or other sources on performance to assess continued compliance

For MDAI that continues to learn after deployment, the post-market monitoring system is key to ensuring continued performance and compliance, identifying emerging risks, and communicating updates to patients, professional users, deployers, and notified bodies.

#### Quality Management System (Q6)

Both frameworks emphasise quality management for safety and performance of MDAI:

- **MDR/IVDR:** Require manufacturers to establish, document, implement, maintain, and continually improve a quality management system proportionate to risk class and device type.
- **AIA (Art. 17):** Mandates quality management systems covering substantive requirements, procedural obligations, and at least thirteen aspects, implemented proportionately to the provider's organisation size.

The AIA quality management obligations are complementary to those under MDR/IVDR. Additional AIA requirements (data governance, record-keeping, transparency, human oversight) must be integrated. Manufacturers may include AIA quality management elements as part of the existing MDR/IVDR quality management system (Recital 81, Art. 8(2), Art. 17(3) AIA).

Harmonised European and international standards for quality management systems for high-risk MDAI are under development.

#### Risk Management (Q7)

All three frameworks require a continuous iterative risk management process throughout the device lifecycle, covering pre-market and post-market phases, aiming at identifying and mitigating risks to health, safety, and fundamental rights.

High-risk MDAI-specific risk management requirements include:

- Ongoing assessments of risks to fundamental rights, data biases, and system robustness
- Identification, analysis, and mitigation of risks in design, development, and deployment
- Training for deployers where appropriate
- Measures for safety and reliability in healthcare settings
- Comprehensive risk assessments with documented mitigation measures
- Continuous monitoring of system performance

Manufacturers may integrate Article 9 AIA risk management requirements into existing MDR/IVDR documentation and procedures (Recital 64 AIA). Risk reduction refers not only to organisational measures but also to specific actions during MDAI design and development.

### Data Governance

#### Data Governance Requirements (Q8)

- **MDR/IVDR:** Mandate that clinical data be robust, reliable, and derived from well-designed studies. Clinical/performance evaluation must be based on data representative of the intended use. Verification and validation procedures must be documented as part of clinical evidence.
- **AIA (Art. 10):** Provides further specifications for AI data and datasets. Includes a provision for exceptional processing of special categories of personal data (Art. 10(5)).

High-quality data sets for training, validation, and testing require appropriate data governance and management practices, fully compliant with GDPR, including transparency about the original purpose of data collection. Requirements may be met by using third parties offering certified compliance services (Recital 67 AIA).

Datasets must be relevant, sufficiently representative, free of errors to the best extent possible, and complete. Manufacturers must implement procedures for data transparency and integrity, examine data for possible biases, and maintain detailed documentation.

#### Bias Monitoring and Mitigation (Q9)

The AIA requires manufacturers to:

- Implement data governance practices with a view to possible biases affecting health, safety, fundamental rights, or leading to prohibited discrimination
- Implement measures to detect, prevent, and mitigate identified biases
- Maintain record-keeping and logging capabilities to facilitate traceability (e.g., identifying bias in training/validation/testing data)
- Ensure technical capabilities for automatic recording of events (logs) over the MDAI lifetime
- Analyse relevant deployer data as part of post-market monitoring to detect bias not originally identified in pre-market activities

#### AIA Data Type Definitions (Q10)

- **Training data** (Art. 3(29)): Data used for training an AI system through fitting its learnable parameters.
- **Validation data** (Art. 3(30)): Data for evaluating the trained AI system and tuning non-learnable parameters and learning processes.
- **Validation data set** (Art. 3(31)): A separate data set or part of the training data set, either as a fixed or variable split.
- **Testing data** (Art. 3(32)): Data for independent evaluation of the AI system to confirm expected performance before market placement.

#### Training, Validation, and Testing Data (Q11)

Data must be appropriate for the intended purpose and representative of the intended patient population. Data collection protocols must ensure that relevant characteristics (age, gender, sex, race, ethnicity, geography, medical condition), intended use environment, and measurement inputs are sufficiently represented in datasets of adequate size.

Under the AIA, datasets must be of high quality, sufficiently representative, free of errors to the best extent possible, complete for the intended purpose, include appropriate statistical properties, and be examined for biases. The AIA also requires measures to address data privacy, security, and transparency in collection and processing.

The European Commission will develop horizontal guidelines on the practical implementation of Article 10. CEN/CENELEC JTC 21 is developing harmonised standards on data and bias.

### Technical Documentation

#### Documentation Requirements (Q12)

The MDR/IVDR require detailed descriptions of software, architecture, data processing methods, and risk management strategies. The AIA requires additional documentation focusing on transparency and accountability, including risk assessments, data governance practices, and performance testing outcomes.

Documentation must include information about design, development, key design choices, functionality, performance characteristics, system architecture, computational resources, and intended use/purpose. Article 11(2) AIA indicates that a single set of technical documentation shall be drawn up for high-risk MDAI.

#### Notified Body Sampling for Technical Documentation (Q13)

Sampling rules under the governing conformity assessment procedure remain applicable. High-risk MDAI are governed by the applicable MDR/IVDR sampling rules. The MDR/IVDR require assessment of technical documentation for at least one representative device per generic device group (Class IIb/C) or per category (Class IIa/B) prior to issuing a certificate.

### Transparency and Human Oversight

#### Transparency Requirements (Q14)

The AIA and MDR/IVDR establish complementary transparency obligations for both manufacturers and deployers:

- **AIA:** Requires high-risk MDAI to be designed so that operation is sufficiently transparent for deployers to interpret outputs correctly and use the system appropriately, supported by clear instructions for use (Art. 13). High-risk MDAI interacting directly with natural persons must inform users they are interacting with an AI system (Art. 50). Deployers have obligations including informing providers and ensuring proper use (Art. 26).
- **MDR/IVDR:** Embed transparency within General Safety and Performance Requirements (GSPRs), requiring clear and accessible information on intended purpose, operation, and limitations. Software development must follow state of the art, incorporating lifecycle and risk management processes supporting traceability, documentation, and usability.

Transparency requirements are not optional design features but essential requirements to be addressed within the manufacturer's risk and quality management systems and verified through conformity assessment.

#### Transparency, Explainability, and Data Processing (Q15)

Transparency under the AIA should assist deployers in using the system and support informed decision making. Deployers should be able to make correct system choices, understand intended and precluded uses, and use the system correctly.

Data processing transparency includes obligations regarding data quality, management, and documentation. Training, validation, and testing data must be relevant, representative, free of errors and bias (to the extent possible), and sufficiently comprehensive.

The MDR/IVDR require manufacturers to provide comprehensive and comprehensible information regarding device performance and risks, including how AI components contribute to performance. The AIA expands and reinforces the MDR/IVDR principle that information to deployers must be clear, complete, and actionable, especially when decisions may impact health outcomes or fundamental rights.

#### Accountability (Q16)

- **MDR/IVDR:** Require documentation and clinical/performance evaluation, clear information to users including how embedded software components contribute to device functionality, and descriptions of how inputs are processed and outputs are generated.
- **AIA (Art. 13):** Introduces explicit transparency obligations. High-risk MDAI must be designed so deployers understand how the system functions and reaches its outputs, including information on characteristics, capabilities, limitations, and support for output interpretability.

These obligations enable traceability of changes, informed use, and post-market control mechanisms that reinforce safe and trustworthy deployment.

#### Usability Engineering (Q17)

All three regulations require manufacturers to apply usability engineering principles. The MDR/IVDR require elimination or reduction of risks related to use errors, with regard to user knowledge and training needs. AI systems in healthcare should be designed with user-centric principles. Documentation of usability engineering processes and outcomes is required.

#### Human Oversight (Q18)

The AIA sets a legal obligation on manufacturers to design and develop AI systems with appropriate human oversight mechanisms. Key requirements:

- Systems must be designed with in-built operational constraints that cannot be overridden by the system itself and must be responsive to the human operator (Art. 14)
- Human intervention in critical decision-making processes is required
- Oversight measures must be commensurate with risks, level of autonomy, and context of use
- Clearly defined and documented human oversight mechanisms and appropriate instructions for use are necessary
- Healthcare professionals and institutions must be enabled to provide appropriate supervision

#### Human Oversight as Risk Management (Q19)

Human oversight serves as both a design/operational requirement and a risk mitigating factor. Manufacturers must, in order of priority:

1. Eliminate or reduce risks through safe design and manufacture
2. Include alarms where appropriate for risks that cannot be eliminated
3. Provide information for safety

For MDAI, specific considerations apply regarding the level of human oversight appropriate to the risk level. For example, in robotic surgical intervention, a healthcare professional oversees the operation but the software design should not allow human intervention in critical parts that would leave the patient at risk. These considerations must be part of the risk assessment and management.

#### Informed Consent (Q20)

- **MDR/IVDR:** Informed consent is explicitly required for clinical investigations and performance studies (Art. 69 MDR, Art. 59 IVDR).
- **AIA:** Introduces additional transparency obligations extending to general deployment of high-risk AI systems, including requirements on human oversight (Art. 14) and transparency (Art. 13) that reinforce the need to provide deployers and affected persons with sufficient information about capabilities, limitations, and risks.

#### Traceability (Q21)

Traceability operates in two interrelated dimensions:

1. **Device traceability (MDR/IVDR):** Traceability throughout the supply chain and lifecycle, including Unique Device Identification (UDI), registration, and post-market surveillance.
2. **Functional traceability (AIA, Art. 12):** Logging and documentation of system performance and behaviour throughout the lifecycle to support monitoring. The EU declaration of conformity must include AI system name, type, and unambiguous reference for identification and traceability.

### Accuracy, Robustness, and Cybersecurity

#### Cybersecurity Measures (Q22)

All three regulations require robust cybersecurity in pre-market and post-market stages. Key requirements:

- Prevent unauthorised access, cyberattacks, exploits, and manipulation
- Ensure operational resilience
- Implement technical solutions to address AI-specific vulnerabilities (Art. 15 AIA)
- Secure AI-specific assets (training data sets, trained models) and underlying ICT infrastructure
- Secure data transmission and storage
- Prevent data and model poisoning
- Detect and respond to cybersecurity incidents
- Conduct risk assessments for cybersecurity vulnerabilities

Cybersecurity is part of the essential requirements for high-risk AI systems and must be integrated into the risk management system, quality management system, and conformity assessment. All three regulations require safety and security risk considerations from early design through the entire lifecycle.

Medical devices and IVDs are out of scope of the Cyber Resilience Act (Regulation (EU) 2024/2847).

---

## Clinical / Performance Evaluation and Testing

### AIA Performance Evaluation Criteria (Q23)

The AIA mandates accuracy, robustness, and cybersecurity for high-risk MDAI. It specifically requires testing against prior-defined metrics and probabilistic thresholds to ensure consistent performance for the intended purpose (Art. 9(8)). This includes validation of AI training pipelines covering design, manufacturing, data collection, preprocessing, model training, and quality management processes.

### Clinical (MDR) or Performance (IVDR) Evaluation Requirements (Q24)

Manufacturers must validate MDAI outputs through rigorous clinical or performance evaluation. Requirements include:

- Software verification and validation to ensure MDAI meets specified requirements
- Clinical validation demonstrating safety and accurate, reliable, clinically relevant outputs
- AIA-specific validation of transparency, human oversight, accuracy, robustness, and cybersecurity
- Verification that high-risk MDAI does not infringe on fundamental rights
- Testing under various conditions with documented evaluation processes and continuous monitoring
- Generation of clinical evidence including clinical benefit within the intended patient population

For MDAI that continues to learn after market placement, the AIA introduces pre-determined changes as an additional consideration for clinical/performance evaluation (Art. 43(4)).

Guidance on pre-determined change control plans is under development at the International Medical Device Regulators Forum (IMDRF).

### Clinical Investigations and Performance Studies (Q25)

Where high-risk MDAI undergoes a clinical investigation or performance study, this constitutes real-world testing under the AIA (Art. 60(1)). Real-world testing of high-risk AI systems is permitted prior to market placement provided it is in accordance with applicable Union or national laws, including MDR and IVDR requirements. Article 60(1), third subparagraph, explicitly states this is "without prejudice to Union or national law on the testing in real-world conditions of high-risk AI systems that are medical devices or in vitro diagnostic medical devices."

### Generating Clinical Evidence (Q26)

The MDR/IVDR require clinical evidence through clinical/performance evaluations, which may include clinical investigations and clinical performance studies. This involves designing studies to evaluate performance, reliability, and clinical impact, with specific requirements for study design, data collection, and statistical analysis.

---

## Conformity Assessment

### Applicable Conformity Assessment Procedures (Q27)

- **High-risk MDAI under Art. 6(1):** The conformity assessment procedure is determined by the MDR/IVDR. Where both AIA Annexes I and III apply, Annex I alone prevails.
- **High-risk MDAI under Art. 6(2) in Annex III points 2-9:** Follows the AIA Annex VI procedure (internal control, no notified body involvement).
- **High-risk MDAI under Art. 6(2) in Annex III point 1:** Follows Art. 43(1) AIA conformity assessment procedures.

Example: An AI emergency triage system qualifying as MDAI follows the Art. 6(1) conformity assessment, requiring compliance with both MDR/IVDR and AIA. An AI biometric categorisation system under Annex III Section 1(b) AIA must comply only with the AIA and undergo Art. 43(1) conformity assessment.

### Demonstrating Conformity to Both Frameworks (Q28)

Most MDAI are classified as Class IIa (MDR), Class B (IVDR), or above, requiring a notified body for quality management system audit, technical documentation review, and inspections. Under Art. 43(3) AIA, the AIA requirements of Articles 8-15 and specific Annex VII provisions (points 4.3, 4.4, 4.5, and the fifth paragraph of 4.6) must be assessed as part of the MDR/IVDR conformity assessment procedure.

---

## Substantial Modification / Significant Change

### Alignment of Substantial Modification Concepts (Q29)

"Substantial modification" is an autonomous concept under the AIA (Art. 3(23)). Under Art. 43(4), high-risk MDAIs that have undergone conformity assessment must undergo a new assessment in the event of a substantial modification, regardless of whether the modified system is further distributed or continues with the current deployer.

The Commission will develop guidelines on substantial modification provisions (Art. 96(1)(c)). An assessment of application to medical devices will be necessary once published.

### Changes Not Constituting Substantial Modification (Q30)

High-risk MDAI that continues to learn after market placement may have a pre-determined changes plan checked during conformity assessment (Art. 43(4)). Changes pre-determined by the manufacturer and assessed at initial conformity assessment, included in AIA Annex IV point 2(f) technical documentation, do not constitute a substantial modification.

Such pre-determined changes should not be understood as changes to the certified device under MDR Annex IX Section 4.10 or IVDR Annex IX Section 4.11. They must be:

- Clearly specified at the time of conformity assessment
- Adaptable to the device's evolving nature
- Documented in technical documentation with initial performance expectations and mechanisms for validating and managing post-market changes
- Included in the change management procedure

Guidance on pre-determined change control plans is under development at IMDRF.

### Transitional Rules for Existing MDAI (Q31)

> **AI Omnibus 2026 postponement applied.** The dates below reflect the AI Omnibus postponement. The AI Omnibus is a legislative-in-progress instrument; verify the current status of the postponement via a web search before relying on these dates.

The date of application for Annex I high-risk AI system obligations is **2 August 2028** *(Omnibus-postponed from 2 August 2027)*:

- **Placed on market before 2 August 2028:** AIA obligations (including Annex I high-risk) apply only if significant design changes occur on or after 2 August 2028.
- **Placed on market on or after 2 August 2028:** Full AIA obligations apply, including Annex I high-risk requirements.

Article 111(2) AIA applies to high-risk AI systems with significant design changes as of 2 December 2027 *(Omnibus-postponed from 2 August 2026)*, but because Art. 6(1) only applies as of 2 August 2028 *(Omnibus-postponed from 2 August 2027)*, medical device AI systems are not classified as high-risk prior to that date. Article 111(2) is assumed to apply by analogy for significant changes on or after 2 August 2028.

---

## Post-Market Monitoring

### Post-Market Surveillance Requirements (Q32)

Both frameworks require manufacturers to establish and implement post-market monitoring and surveillance systems, including:

- Systematic collection and analysis of device performance data
- Risk analysis and adverse events assessment and reporting
- Corrective and preventive actions
- A vigilance system for reporting to regulatory authorities and users
- Regular updates to risk and quality management systems based on monitoring and regulatory feedback

### Continuous Performance Monitoring (Q33)

- **MDR/IVDR:** Post-market surveillance systems to monitor performance and safety after market placement.
- **AIA (Art. 72):** Post-market monitoring plan to actively and systematically collect, document, and analyse performance data through the MDAI lifetime, ensuring continuous compliance with Articles 8-15. Must be proportionate to the technology and risks.

### New Dimensions from the AIA (Q34)

The AIA introduces the need to detect interactions with other AI systems, including other devices and software. Deployers are required to monitor operation (Art. 26) and inform the manufacturer where relevant (Art. 72).

The Commission will adopt an implementing act with a template for the post-market monitoring plan by 2 February 2026 (Art. 72(3)). Necessary elements may be integrated into existing MDR/IVDR post-monitoring plans provided an equivalent level of protection is achieved (Art. 72(4)).

---

## Other Questions

### In-House MDAI (Q35)

In-house medical devices manufactured and used only within health institutions are not subject to third-party conformity assessment (provided Art. 5(5) conditions are met). Therefore, such MDAI are not classified as high-risk AI systems. However, other AIA obligations still apply, including but not limited to prohibited practices.

The AIB and MDCG will provide further guidance on appropriate requirements for in-house MDAI.

### AI Training Requirements for Deployers (Q36)

Manufacturers must ensure training of deployers when appropriate as part of risk management to ensure appropriate use, reduce foreseeable misuse, and enable oversight during deployment. Key obligations:

- **AIA (Art. 13):** Transparency and provision of information for deployers. Instructions for use should assist deployers and support informed decision making (Recital 72).
- **Human oversight (Art. 14):** Natural persons assigned to oversight must understand capabilities and limitations and be able to duly monitor. Manufacturers should advise on education and training for sufficient understanding of MDAI output interpretability.
- **AI literacy (Art. 4):** Manufacturers and deployers must ensure a sufficient level of AI literacy for staff and other persons dealing with AI system operation and use, considering technical knowledge, experience, education, training, context of use, and the persons or groups affected.
