# Overview of Guidelines for GPAI Models

Overview of published and upcoming guidelines applicable to general-purpose AI models, including law enforcement implications.

| Aspect | Detail |
|--------|--------|
| Institution | artificialintelligenceact.eu |
| Date | 2025 |
| Source URL | https://artificialintelligenceact.eu/gpai-guidelines-overview/ |
| NotebookLM Source ID | 16578060-... |

*German: Ubersicht der Leitlinien fur KI-Modelle mit allgemeinem Verwendungszweck*

---

On 18 July 2025, the European Commission published draft Guidelines clarifying key provisions of the EU AI Act applicable to General Purpose AI (GPAI) models. The Guidelines provide interpretive guidance on the definition and scope of GPAI models, related lifecycle obligations, systemic risk criteria, and notification duties for providers. Once translated into all EU languages, the Guidelines will be formally adopted and carry legal and operational relevance for AI providers.

## Definition and Scope

### Definition of GPAI Models

The Guidelines expand on the statutory definition of GPAI in the AI Act, introducing key thresholds and criteria for classification:

**Compute threshold:** A GPAI model is defined as any model trained using more than 10^23 FLOPs (floating point operations) and capable of generating language (text/audio), text-to-image, or text-to-video outputs.

**Functional generality requirement:** Models that exceed the 10^23 FLOPs threshold but are specialised (e.g., for transcription, image upscaling, weather forecasting, or gaming) are excluded if they lack general capabilities across a broad range of tasks.

**Technical clarifications:**

- Compute is understood as a combined measure of model size (parameters) and training dataset size
- A model with approximately 1 billion parameters trained on substantial datasets would typically meet this compute threshold
- The Commission has opted for a single estimable compute threshold over listing specific tasks or capabilities

### Model Lifecycle and Obligations

Once a model qualifies as a GPAI model, lifecycle-wide obligations under the AI Act apply from the start of its pre-training run and extend to all subsequent development phases, including post-market modifications.

Obligations include:

- **Documentation:** Must be maintained and updated, and provided to downstream providers and, upon request, to the AI Office or national competent authorities
- **Training data summary:** Providers must publish a summary using the yet-to-be-issued AI Office template
- **Copyright policy:** Must address copyright compliance and may apply across all models

## GPAI Models with Systemic Risk

Any model trained using 10^25 FLOPs or more is presumed to have high-impact capabilities and may be classified as systemic-risk GPAI.

### Additional Obligations

- Comprehensive risk assessment and mitigation throughout the lifecycle, including model evaluations
- Robust cybersecurity measures
- Serious Incident tracking and reporting

### Designation Pathways

- **Automatic presumption:** Based on FLOPs threshold
- **Discretionary designation:** By the Commission, including following alerts from the scientific panel

### Mandatory Notifications

Providers must notify the Commission within two weeks of reasonably foreseeing or reaching the 10^25 FLOPs threshold. Notifications must include:

- Compute estimates
- Estimation methodologies (including approximations)

### Rebuttal Process

- Providers may contest the systemic risk classification by supplying robust evidence (e.g., benchmark results, scaling laws) that the model does not present systemic risk
- The Commission may accept or reject rebuttals with reasons
- Obligations remain in effect during review

### Reassessment Rights

- Initial reassessment may be requested by providers six months post-designation
- A second reassessment request is allowed after a further six months if the first is unsuccessful

### Ongoing Duty to Update

If the rebuttal was based on materially changed or incomplete/incorrect information, the provider must renotify the Commission.

## Determining the GPAI Model Provider

### Single Entity Development

- If Entity A develops and places a GPAI model on the EU market, Entity A is the provider
- If Entity B develops the model for Entity A, but Entity A places it on the market, Entity A remains the provider

### Repository Hosting

Uploading a model to a repository (e.g., hosted by Entity C) does not transfer provider status. Entity A remains the provider.

### Consortium Development

In the case of GPAI models developed by or for a consortium, the provider is typically the coordinator or the consortium itself, depending on the facts and contractual arrangements.

## Upstream and Downstream Responsibility Allocation

### Upstream Providers

If an upstream actor first makes the model available to any downstream actor on the EU market, that actor is the provider and must meet GPAI provider obligations.

### Downstream System Integrators

If a downstream actor incorporates the GPAI model into an AI system and places the system on the EU market, they are a system provider and must meet obligations relevant to AI systems.

### Non-EU Origin Models

If a model is made available outside the EU but is later incorporated into a system placed on the EU market, the model is considered placed at that point. The upstream actor is the provider unless they have explicitly excluded EU use. In such cases, the downstream actor becomes the provider.

## Downstream Modifiers: When They Become Providers

Not all modifications trigger provider obligations for downstream actors. Minor changes typically do not reclassify a modifier as a GPAI provider.

### Threshold for Reclassification

A downstream actor becomes the new GPAI provider if the training compute used for the modification exceeds one-third of that used to train the original model:

- 1/3 of 10^23 FLOPs or more for all GPAI models
- 1/3 of 10^25 FLOPs or more for GPAI models with systemic risk

### Scope of Obligations

- Only modification-specific obligations apply: documentation, training data summary, and copyright policy relate only to the additional compute and data
- However, if modifying a systemic-risk GPAI model, the downstream actor must comply fully with all systemic risk obligations, including notification to the Commission

## Open Source Models: Exemptions and Conditions

Open source GPAI providers benefit from limited exemptions under the AI Act:

- No obligation to provide documentation to downstream providers or, upon request, to the AI Office or national authorities

### Non-Exempt Requirements

- Must comply with training data summary and copyright policy requirements
- If designated as a GPAI model with systemic risk, they must fully meet all applicable obligations, including systemic risk management, model evaluations, incident reporting, and cybersecurity

### Qualifying as Open Source

To qualify as open source under the AI Act, the model must be released under a free and open-source licence that permits use, access, modification, and redistribution, and does not impose restrictions such as:

- Non-commercial or research-only use
- Prohibition on redistribution
- User-size thresholds
- Mandatory commercial licensing for certain uses

### Permissible Restrictions

- Credit/attribution requirements
- Distribution under the same or compatible licence
- Reasonable and proportionate safeguards against high-risk use (e.g., public safety), provided they are non-discriminatory

### Monetisation and Loss of Open Source Status

A GPAI model loses open source exemptions if monetisation is present. Indicators include:

- **Commercial licensing models:** Dual-licensing (e.g., free for academic use, paid for commercial use); pay-to-access support, maintenance, or updates; hosted access subject to fees or advertising revenue
- **Functional dependency on paid services:** If users must pay to access essential functionality or security features
- **Personal data processing:** Processing user data in connection with access, use, or modification may constitute monetisation, unless solely for non-commercial security purposes

**Not considered monetisation:** Offering optional premium services or support without restricting free access to the model and its core functionality.

## Implementation

### Code of Practice

- Signing the Code of Practice is voluntary, but it can help providers demonstrate compliance with the AI Act's obligations for GPAI models
- The Code is not a harmonised standard, so signing it does not create an automatic presumption of compliance
- The Commission will monitor signatories' adherence to the Code
- Opting out of any chapter (transparency, copyright, or safety/security) means providers cannot rely on the Code to show compliance in that area
- Signatories may benefit from greater trust and potentially lower fines
- Non-signatories must independently demonstrate compliance, including through detailed explanations or gap analyses, and should expect more scrutiny from the AI Office

### Enforcement and Oversight

- The AI Office will adopt a collaborative and risk-based enforcement model
- Informal cooperation is encouraged during training phases
- Providers of systemic-risk GPAI models are expected to proactively report and engage with the AI Office
- While obligations kick in on 2 August 2025, the AI Office does not have full enforcement powers until 2 August 2026, by which time they may request information, order model recalls, mandate mitigations, or impose fines
- For models placed before 2 August 2025, providers will have until 2 August 2027 to comply. Retraining or "unlearning" will not be required if technically or economically infeasible, provided this is justified in documentation
- Models placed after 2 August 2025 must aim to comply on placement. New entrants, particularly systemic-risk model developers, will receive support to ease compliance

### Review of Guidelines

The Commission may update or withdraw these guidelines based on:

- Experience with implementation
- Enforcement outcomes
- Market and technological developments
- Court of Justice of the EU (CJEU) rulings

Stakeholders -- including providers, regulators, researchers, and civil society -- will be invited to contribute to updates via consultations and workshops.

## Annex: Training Compute -- Definitions and Estimation Methods

### Definition

Training compute is the total compute used to train a model and assess whether it meets systemic-risk GPAI thresholds:

- For non-systemic-risk models: compute used for parameter updates
- For systemic-risk assessment: all cumulative training compute counts

### Inclusions

- All compute contributing to model capabilities, including forward passes for synthetic data generation (even discarded data)
- Compute for weight merging or initialisation using pre-trained models

### Exclusions

Compute for:

- Publicly available synthetic data
- Diagnostic/evaluation tasks
- Failed experiments or research-only runs
- Auxiliary model training (e.g., reward models)
- Activation recomputation for memory savings

### Estimation Methods

- Cover both hardware- and architecture-based approaches
- Estimate must be accurate within plus or minus 30%, with documentation of assumptions and uncertainties
