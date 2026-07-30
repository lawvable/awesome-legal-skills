# GPAI Model Obligations — Articles 51–56

## Table of Contents

1. [What Is a GPAI Model](#1-what-is-a-gpai-model)
2. [GPAI Provider Obligations (Article 53)](#2-gpai-provider-obligations-article-53)
3. [Systemic Risk (Articles 54–56)](#3-gpai-models-with-systemic-risk-articles-5456)
4. [Open-Source GPAI Models](#4-open-source-gpai-models)
5. [Downstream Provider Responsibilities](#5-downstream-provider-responsibilities)
6. [Practical Assessment Checklist](#6-practical-assessment-checklist)

---

## 1. What Is a GPAI Model

**Article 3(63):** A GPAI model is an AI model — including when trained with a large amount of data using self-supervision at scale — that displays significant generality, is capable of competently performing a wide range of distinct tasks regardless of how it is placed on the market, and can be integrated into a variety of downstream systems or applications.

**Practical indicators:**
- Sold or distributed as a model or API usable for many applications (not a single narrow task)
- Used as a base/foundation model fine-tuned for diverse downstream uses
- Broad capability claims and general instruction-following ability
- Examples: GPT-4, Claude, Gemini, Llama, Mistral, and their fine-tuned derivatives

**What is NOT a GPAI model:**
- A narrow classification model trained for one specific task (e.g., fraud detection on one dataset)
- A traditional ML model for a single prediction (e.g., churn prediction)
- Rule-based systems or expert systems without learned generality

**Key distinction:** GPAI obligations attach to the *model provider*, independently of whether downstream applications are high-risk, limited-risk, or minimal-risk. A minimal-risk chatbot using GPT-4 still means OpenAI must meet GPAI obligations.

---

## 2. GPAI Provider Obligations (Article 53)

All GPAI model providers placing models on the EU market must:

### 2.1 Technical Documentation

Prepare and maintain technical documentation of the model, including training and testing process and results. Make it available to the AI Office on request.

**Practical content (Annex XI):**
- Model architecture description and computational resources used
- Training methodology, data sources, and preprocessing
- Evaluation and testing results, known limitations
- Energy consumption information

### 2.2 Information for Downstream Providers

Provide information and documentation to downstream AI system providers to enable them to:
- Understand capabilities and limitations of the model
- Comply with their own obligations (e.g., if building a high-risk system on the GPAI)

**Practical content:**
- Model card or equivalent documentation
- Intended and foreseeable uses and misuses
- Performance benchmarks and limitations
- Integration guidance

### 2.3 Copyright Compliance Policy

Establish a policy to comply with EU copyright law, including:
- Identification and respect of rights reservations (opt-outs under the text and data mining exception)
- Making available a sufficiently detailed summary of training data content

**Practical content:**
- Documented opt-out compliance process
- Training data summary (publicly available per Article 53(1)(d))
- Process for handling copyright complaints

### 2.4 Training Data Summary

Draw up and make publicly available a sufficiently detailed summary about the content used for training the GPAI model.

**Note:** The EU AI Office is developing a template for this summary. Until available, providers should prepare a good-faith summary covering data types, sources, volumes, and any known provenance information.

---

## 3. GPAI Models with Systemic Risk (Articles 54–56)

### 3.1 When Systemic Risk Applies

A GPAI model is classified as having systemic risk if:

**Automatic classification (Article 51(2)):**
- The cumulative amount of compute used for training exceeds **10^25 FLOPs** (floating point operations)
- This threshold may be updated by the Commission via delegated acts

**Designation by the EU AI Office:**
- Based on criteria including: high-impact capabilities, wide reach across the internal market, number of registered users, or specific dangerous capabilities
- The provider can present arguments against designation

**Current models likely meeting the threshold:** Frontier models from major providers (GPT-4+, Gemini Ultra, Claude Opus-class, etc.)

### 3.2 Additional Obligations for Systemic Risk Models (Article 55)

On top of all Article 53 obligations, providers of systemic risk GPAI models must:

**Model evaluation and adversarial testing:**
- Perform model evaluations in accordance with standardised protocols
- Conduct adversarial testing to identify and mitigate systemic risks
- Track, document, and report systemic risks without undue delay

**Serious incident reporting:**
- Report serious incidents and possible corrective measures to the AI Office and relevant national authorities without undue delay

**Cybersecurity:**
- Ensure adequate cybersecurity protections for the model and its physical infrastructure

**Risk mitigation:**
- Take appropriate measures to mitigate identified systemic risks

### 3.3 Codes of Practice

The EU AI Office facilitates the drawing up of codes of practice (Article 56) that detail obligations, including:
- Identifying relevant systemic risks
- Applying risk mitigation measures
- Establishing common evaluation and testing methodologies

Compliance with an approved code of practice creates a presumption of conformity. Providers can demonstrate compliance by alternative means but must demonstrate equivalent protection.

---

## 4. Open-Source GPAI Models

**Lighter obligations (Article 53(2)):** Providers of GPAI models released under a free and open-source licence need only:
- Draw up and make publicly available a sufficiently detailed summary of training data
- Establish and comply with a copyright policy

They are exempt from the full technical documentation and downstream information obligations — **unless** the model is classified as having systemic risk, in which case **all** obligations apply regardless of open-source status.

**Qualifying licences:** Must allow access, use, modification, and distribution of the model. The term "free and open-source" is intended broadly but the AI Office may issue guidance on qualifying licences.

**Practical implication:** Downloading and deploying an open-source GPAI model does not make your organisation the GPAI provider (the original model provider retains that role). However, if you substantially modify the model, you may become a provider of a new GPAI model.

---

## 5. Downstream Provider Responsibilities

Even if you are not a GPAI model provider, you have practical responsibilities:

### 5.1 Vendor Due Diligence

- Request and review the GPAI provider's Article 53 documentation
- Verify the training data summary is publicly available
- Assess whether the model is classified as systemic risk

### 5.2 Contractual Allocation

- Include AI Act compliance obligations in vendor agreements
- Specify data access, incident response cooperation, and update commitments
- Address liability allocation for downstream non-compliance
- Require notification if the model's systemic risk classification changes

### 5.3 If Building a High-Risk System on GPAI

When you build a high-risk AI system using a GPAI model:
- You are the provider of the AI *system* (with full Title III obligations)
- The GPAI model provider has GPAI-specific obligations
- Ensure you can fulfil your system-level obligations (risk management, data governance, transparency) with the information provided by the GPAI model provider
- If the GPAI provider's documentation is insufficient, this is a compliance risk to flag and address contractually

---

## 6. Practical Assessment Checklist

When a system uses a GPAI model:

- [ ] Identify the GPAI model(s) used and their provider(s)
- [ ] Confirm whether the provider is established in the EU or has an authorised representative
- [ ] Check if the model is classified as systemic risk (compute threshold or AI Office designation)
- [ ] Request Article 53 documentation (model card, training data summary, capability docs)
- [ ] Review the publicly available training data summary
- [ ] Assess copyright compliance evidence (opt-out policy)
- [ ] If systemic risk: request evidence of model evaluation, adversarial testing, incident reporting
- [ ] Update vendor contracts with AI Act compliance clauses
- [ ] Map downstream obligations — if your system is high-risk, you need the GPAI documentation to meet your own compliance requirements
- [ ] Monitor for updates — the EU AI Office may reclassify models or update thresholds

**Timeline:** GPAI obligations apply from **2 August 2025**. Existing GPAI models placed on the market before this date must comply by **2 August 2027**.
