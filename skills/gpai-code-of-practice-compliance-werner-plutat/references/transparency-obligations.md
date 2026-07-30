# Transparency Obligations — GPAI Code of Practice

Complete requirements for Transparency chapter (Commitment 1, Measures 1.1–1.3) and the mandatory GPAI Training Data Summary Template.

**Legal basis:** Article 53(1)(a)–(b), Annexes XI and XII of Regulation (EU) 2024/1689.

**Applies to:** All GPAI model providers placing models on the EU market, EXCEPT providers of free and open-source models (Article 53(2)) — unless the model has systemic risk.

---

## Table of Contents

1. [Commitment 1: Documentation](#commitment-1-documentation)
2. [Measure 1.1: Model Documentation](#measure-11-model-documentation)
3. [Measure 1.2: Providing Information](#measure-12-providing-information)
4. [Measure 1.3: Quality, Integrity, Security](#measure-13-quality-integrity-security)
5. [Model Documentation Form](#model-documentation-form)
6. [GPAI Training Data Summary Template](#gpai-training-data-summary-template)
7. [Practical Compliance Steps](#practical-compliance-steps)

---

## Commitment 1: Documentation

Signatories commit to:
- Drawing up and keeping up-to-date model documentation (Measure 1.1)
- Providing relevant information to downstream providers and the AI Office (Measure 1.2)
- Ensuring quality, security, and integrity of documented information (Measure 1.3)

---

## Measure 1.1: Model Documentation

**Before placing a GPAI model on the EU market**, providers must prepare comprehensive documentation addressing all elements in the Model Documentation Form.

### Key requirements:
- Documentation must be **kept current** — reflect material changes throughout the model's lifecycle
- **Retention period:** Minimum 10 years after initial market placement
- Documentation must be **prepared before** the model is made available, not retroactively
- Updates required for material changes in architecture, training data, capabilities, or intended use

### What constitutes a "material change":
- Significant architecture modifications
- Major retraining with new data sources
- Expansion of model capabilities or supported modalities
- Changes to intended use cases or known limitations
- Security-relevant updates

---

## Measure 1.2: Providing Information

### To the AI Office:
- **Contact details** must be publicly available for the AI Office to request documentation
- Upon request, deliver the **latest documentation version** within the designated timeframe
- The AI Office may request information ex officio or on behalf of national competent authorities
- Requests will state legal basis and purpose and be limited to what is strictly necessary

### To downstream providers:
- Deliver necessary documentation **within 14 days** of request (unless legitimate delay exists)
- Documentation must enable downstream providers to:
  - Understand model capabilities and limitations
  - Comply with their own AI Act obligations (e.g., for high-risk AI systems using the GPAI model)
- Include clarifications as needed

### Public release:
- **Encouraged** (not mandatory) as a means of enhancing overall transparency
- Providers should consider what can be publicly released without compromising trade secrets

---

## Measure 1.3: Quality, Integrity, Security

- Documentation must be **accurate** — providers bear responsibility for precision
- Documentation must be **protected from unauthorised modification**
- **Secure storage** required to demonstrate regulatory compliance
- Internal processes needed to verify ongoing accuracy and completeness

---

## Model Documentation Form

The standardised form covers these categories. Each item is marked for its intended audience: downstream providers (DP), AI Office (AO), or national competent authorities (NCA).

### 1. Licensing & Distribution
- Licence type and terms
- Distribution channels (API, download, integrated product)
- Access conditions and restrictions
- **Audience:** DP, AO

### 2. Model Identification
- Model name and version
- Release date
- Provider entity name and contact information
- Previous versions and changelog
- **Audience:** DP, AO

### 3. Technical Specifications
- Model architecture (type, size, parameter count)
- Input and output formats and modalities
- Maximum context length
- Training framework and infrastructure
- **Audience:** DP, AO

### 4. Intended and Approved Use Cases
- Intended purpose and use cases
- Known limitations and failure modes
- Use cases explicitly not supported or prohibited
- **Audience:** DP, AO

### 5. Integration Dependencies
- Supported platforms and operating environments
- Hardware/software requirements
- API specifications (if applicable)
- **Audience:** DP

### 6. Training Methodology
- Training approach and design rationale
- Pre-training, fine-tuning, and RLHF/alignment details
- Evaluation protocols and benchmark results
- **Audience:** AO, NCA (upon request)

### 7. Dataset Details
- Data sources (public datasets, proprietary data, web-scraped data, synthetic data, user data)
- Data types, scope, and volume
- Data curation and filtering processes
- Bias assessment and mitigation measures
- Copyright compliance measures for training data
- **Audience:** AO, NCA (upon request)

### 8. Compute and Energy
- Training compute (total FLOPs)
- Training hardware and infrastructure
- Energy consumption during training
- Inference compute and energy estimates
- **Audience:** AO, NCA (upon request)

**Note:** The Commission's recommended word limits are typically 200–300 words per field — brief, high-level summaries rather than exhaustive technical documentation.

---

## GPAI Training Data Summary Template

**Separate from the Code of Practice** — this is a mandatory disclosure under Article 53(1)(d).

**Key difference:** The training data summary must be **made publicly available**, not just provided upon request.

The GPAI Template (published by Commission, 24 July 2025) requires:

### Required disclosures:
1. **General model information** — quantity and types of data used (text vs. images vs. audio)
2. **List of data sources** — identification of:
   - Public datasets
   - Private/proprietary datasets
   - User data
   - Web-scraped data (with scope description)
   - Synthetic data
3. **Compliance measures** — steps taken to:
   - Remove illegal content from training data
   - Respect copyright and related rights
   - Handle rights reservations (robots.txt, opt-outs)

### Publication requirements:
- Must be published using the template provided by the AI Office
- Must be sufficiently detailed to give meaningful transparency
- Must not require disclosure of trade secrets — but the summary must still be informative

---

## Practical Compliance Steps

### For new models (released after 2 August 2025):
1. Complete the Model Documentation Form before market placement
2. Complete and publish the GPAI Training Data Summary Template
3. Establish process for handling AI Office and downstream provider requests
4. Set up documentation version control and 10-year retention
5. Designate responsible person/team for documentation maintenance
6. Create internal process for identifying and documenting material changes

### For existing models (released before 2 August 2025):
- **Deadline:** 2 August 2027 to bring documentation into compliance
- Begin gap assessment now — documentation requirements are substantial
- Prioritise: training data summary (public), then model documentation form

### Common gaps:
- Incomplete training data provenance records
- Missing compute and energy consumption data (especially for older models)
- No structured process for downstream provider information requests
- Documentation not version-controlled or securely stored
- No formal material change assessment process

---

## Edge Cases and Practical Considerations

### Multi-model systems:
If a provider offers multiple related models (e.g., different sizes of the same family), separate documentation is required for each model placed on the market, though common elements can be cross-referenced.

### Models modified after release:
If a model is significantly updated post-release, documentation must be updated. If the update constitutes a new model placement, fresh documentation may be required.

### Downstream provider obligations:
Downstream providers integrating GPAI models into high-risk AI systems need sufficient information from the GPAI model provider to fulfil their own AI Act obligations. This creates a practical dependency — GPAI model providers should anticipate and facilitate these information needs.

### Information that may be withheld:
- Trade secrets and confidential business information (Article 78)
- Information that would compromise model security
- But: withholding must not undermine the purpose of the transparency obligations

---

*Source: GPAI Code of Practice (Final Version, July 2025), Regulation (EU) 2024/1689 Articles 53(1)(a)–(b)(d), Annexes XI and XII.*
