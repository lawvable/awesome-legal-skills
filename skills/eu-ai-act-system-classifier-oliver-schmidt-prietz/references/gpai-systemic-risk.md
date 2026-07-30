# General-Purpose AI Models & Systemic Risk — Art. 3(63-66), Art. 51-55

## Definitions

### General-Purpose AI Model (GPAI) — Art. 3(63)

*German: KI-Modell mit allgemeiner Zweckbestimmung*

> 'general-purpose AI model' means an AI model, including where such an AI model is trained with a large amount of data using self-supervision at scale, that displays significant generality and is capable of competently performing a wide range of distinct tasks regardless of the way the model is placed on the market, and which can be integrated into a variety of downstream systems or applications, except AI models that are used for research, development or prototyping activities before they are placed on the market.

**Key characteristics:**
- Trained with large amounts of data
- Self-supervised learning at scale
- Significant generality (not narrow-purpose)
- Capable of performing wide range of distinct tasks
- Can be integrated into downstream systems/applications
- Placed on the market (excludes R&D prototypes)

**Examples:**
- Large language models (GPT-4, Claude, Gemini, Llama, Mistral)
- Large multimodal models (image+text, audio+text)
- Foundation models intended for broad downstream use

### General-Purpose AI System — Art. 3(66)

> 'general-purpose AI system' means an AI system which is based on a general-purpose AI model and which has the capability to serve a variety of purposes, both for direct use as well as for integration in other AI systems.

### GPAI Model with Systemic Risk — Art. 3(65)

> 'general-purpose AI model with systemic risk' means a general-purpose AI model that has high impact capabilities evaluated on the basis of appropriate technical tools and methodologies, including indicators and benchmarks.

---

## Systemic Risk Classification — Art. 51

### Presumption of Systemic Risk — Art. 51(2)

A GPAI model is **presumed** to have systemic risk when:

> The cumulative amount of computation used for its training measured in floating point operations (FLOPs) is **greater than 10^25**.

**10^25 FLOPs threshold:**
- This is the current quantitative benchmark
- Commission may update this threshold via delegated act (Art. 51(2) second subparagraph)
- Threshold should be adjusted in light of technological developments

**Always search for latest threshold updates — the Commission may revise this number.**

### Classification by Commission Decision — Art. 51(1)

The Commission may designate a GPAI model as having systemic risk, ex officio or based on:
- Alert from the scientific panel (Art. 68)
- Information from the GPAI model provider

**Criteria for designation (Annex XIII):**

| Criterion | Description |
|-----------|-------------|
| Number of parameters | Total parameter count of the model |
| Quality/size of dataset | Volume and quality of training data |
| Computation for training | FLOPs used (see threshold above) |
| Input/output modalities | Number and type of modalities (text, image, audio, video, code) |
| Benchmarks and evaluations | Performance on standardized benchmarks and state-of-the-art evaluations |
| High-impact capabilities | Including capabilities comparable to most advanced models |
| Reach to end-users | Number of registered/active end-users |
| Cross-border reach | Availability across EU Member States |

### Systemic Risk Assessment Questions

Ask the following to determine systemic risk:

**Q1: Computational scale**
> "What is the approximate computational budget used for training this model, measured in FLOPs? Is it above 10^25 FLOPs?"

**Q2: Model capabilities**
> "Does this model exhibit high-impact capabilities — i.e., capabilities matching or exceeding the most advanced generally available models in any modality?"

**Q3: Reach and deployment**
> "How many end-users does this model serve? Is it deployed across multiple EU Member States?"

**Q4: Commission designation**
> "Has the EU Commission or AI Office specifically designated this model as having systemic risk?"

---

## GPAI Provider Obligations — Art. 53 (Standard GPAI)

All GPAI model providers must comply with Art. 53(1):

| Obligation | Article | Description |
|-----------|---------|-------------|
| Technical documentation | Art. 53(1)(a) | Draw up and keep up-to-date technical documentation (Annex XI) |
| Information to downstream | Art. 53(1)(b) | Provide information and documentation to downstream AI system providers |
| Copyright policy | Art. 53(1)(c) | Implement policy to comply with EU copyright law, including opt-out mechanisms |
| Training data summary | Art. 53(1)(d) | Publish sufficiently detailed summary of training data content (Annex XIa template) |

### Annex XI — Technical Documentation for GPAI Models

Required documentation includes:
- Model description (architecture, training methodology, design choices)
- Training data description (sources, scope, curation, preprocessing)
- Computational resources used (hardware, training time, FLOPs)
- Evaluation methodology and results
- Energy consumption information
- Known limitations and risks

---

## GPAI with Systemic Risk — Additional Obligations — Art. 55

Providers of GPAI models with systemic risk must **additionally**:

| Obligation | Article | Description |
|-----------|---------|-------------|
| Model evaluation | Art. 55(1)(a) | Perform model evaluation, including adversarial testing (red teaming) |
| Risk assessment & mitigation | Art. 55(1)(b) | Assess and mitigate possible systemic risks |
| Incident tracking & reporting | Art. 55(1)(c) | Track, document, and report serious incidents to AI Office and national authorities |
| Cybersecurity protection | Art. 55(1)(d) | Ensure adequate level of cybersecurity protection for model and infrastructure |

### Codes of Practice — Art. 56

**GPAI Code of Practice** (published 10 July 2025, endorsed by Commission + AI Board 1 August 2025):
- Covers three chapters: (i) transparency, (ii) copyright, (iii) safety and security
- Chapters (i) and (ii) apply to all GPAI model providers; chapter (iii) applies to systemic risk models
- Provides detailed implementation guidance for Art. 53 and 55 obligations
- Compliance with Code of Practice creates presumption of compliance with obligations
- Not legally binding, but endorsed via adequacy decisions — practical compliance path

**Always search for the latest version of the GPAI Code of Practice.**

---

## GPAI and High-Risk Systems — Interaction

### When GPAI model is integrated into high-risk system:

```
GPAI Model Provider → Art. 53 obligations (+ Art. 55 if systemic risk)
         │
         ▼
AI System Provider (integrates GPAI) → Full high-risk obligations (Art. 8-17)
         │
         ▼
Deployer → Art. 26 deployer obligations
```

**Key principle:** The GPAI model provider's obligations are separate from the high-risk system obligations. The system provider who integrates a GPAI model into a high-risk system bears the full Art. 8-17 obligations.

### When GPAI model IS the system (direct deployment):

If a GPAI model is deployed directly as an AI system (e.g., ChatGPT deployed to end users):
- The GPAI model provider is also the AI system provider
- Both Art. 53 (GPAI) and Art. 16 (provider) obligations apply
- If the system falls under Annex III, full high-risk obligations apply

---

## Assessment Output Format

```
GPAI Assessment

Model/System:        [name]
GPAI Model:          [Yes/No]
Training FLOPs:      [value / unknown]
Systemic Risk:       [Yes — threshold / Yes — Commission designation / No / Unknown]

Applicable obligations:
- Art. 53 (standard GPAI):     [Yes/No]
- Art. 55 (systemic risk):     [Yes/No]
- Code of Practice:            [Applicable / Not yet binding]
- Open-source partial exemption: [Art. 53(2) applicable / Not applicable]

Recommendation: [description of applicable obligation set]
```

---

## Timeline

| Date | Obligation |
|------|-----------|
| 2 Aug 2025 | GPAI obligations apply (Art. 53, 55) — 12 months after entry into force |
| Ongoing | Code of Practice updates and Commission delegated acts |
| TBD | Possible FLOP threshold revision via delegated act |
