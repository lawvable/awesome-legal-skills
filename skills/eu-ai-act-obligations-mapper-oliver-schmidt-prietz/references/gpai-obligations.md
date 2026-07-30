# GPAI Model Provider Obligations — Art. 51-55

## Overview

General-purpose AI model providers have two tiers of obligations:
1. **Standard GPAI (Art. 53):** All GPAI model providers
2. **Systemic risk GPAI (Art. 53 + Art. 55):** Additional obligations for models with systemic risk

---

## Standard GPAI Obligations — Art. 53

### Obligation 1: Technical Documentation — Art. 53(1)(a)

**Obligation:** Draw up and keep up-to-date the technical documentation of the model, including its training and testing process and the results of its evaluation, which shall contain, at a minimum, the information set out in Annex XI.

**Annex XI content requirements:**
1. Model description (name, version, release date)
2. Training methodology and techniques
3. Design choices and assumptions
4. Training data description (sources, scope, characteristics)
5. Computational resources used (type, quantity, training time)
6. Energy consumption (known or estimated)
7. Evaluation results (benchmarks, metrics, known limitations)

| Aspect | Detail |
|--------|--------|
| Frequency | Before market + ongoing updates |
| Effort | 5/5 |
| RACI | Engineering=R, Legal=A, Management=I |

---

### Obligation 2: Information to Downstream Providers — Art. 53(1)(b)

**Obligation:** Draw up, keep up to date and make available information and documentation to providers of AI systems who intend to integrate the GPAI model into their AI systems. Without prejudice to intellectual property, the documentation shall include at minimum the elements set out in Annex XII.

**Annex XII content requirements:**
1. Capabilities and limitations (including foreseeable risks)
2. Suitability for specific tasks
3. Integration guidance for downstream providers
4. Technical requirements for operation

| Aspect | Detail |
|--------|--------|
| Frequency | Before integration + updates |
| Effort | 4/5 |
| RACI | Engineering=R, Product=A, Legal=C |

---

### Obligation 3: Copyright Compliance — Art. 53(1)(c)

**Obligation:** Put in place a policy to comply with Union law on copyright and related rights, and in particular to identify and comply with, including through state-of-the-art technologies, a reservation of rights expressed pursuant to Art. 4(3) of Directive (EU) 2019/790.

**What this means:**
- Implement opt-out mechanism for rights holders (text and data mining exception)
- Respect machine-readable opt-out signals (robots.txt with AI-specific directives)
- Document compliance policy
- Track and respect copyright reservations

| Aspect | Detail |
|--------|--------|
| Frequency | Continuous |
| Effort | 4/5 |
| RACI | Legal=R, Engineering=C, Management=A |

---

### Obligation 4: Training Data Summary — Art. 53(1)(d)

**Obligation:** Draw up and make publicly available a sufficiently detailed summary about the content used for training of the general-purpose AI model, according to a template provided by the AI Office (Annex XIa).

**Annex XIa template requires:**
- Description of training data sources
- Categories of data used
- Time periods of data
- Geographic/linguistic scope
- Summary of data governance measures

| Aspect | Detail |
|--------|--------|
| Frequency | Before market + updates |
| Effort | 3/5 |
| RACI | Engineering=R, Legal=A, Communications=C |

---

## Systemic Risk Additional Obligations — Art. 55

*Only for GPAI models classified with systemic risk per Art. 51.*

### Obligation 5: Model Evaluation — Art. 55(1)(a)

**Obligation:** Perform model evaluation in accordance with standardised protocols and tools reflecting the state of the art, including conducting and documenting adversarial testing (red teaming) of the model to identify and mitigate systemic risks.

**What this means:**
- Structured evaluation using standardized benchmarks
- Adversarial testing / red teaming (safety, misuse, bias, security)
- Document methodology and results
- Address identified risks before deployment

| Aspect | Detail |
|--------|--------|
| Frequency | Before deployment + periodic |
| Effort | 5/5 |
| RACI | Safety Team=R, Engineering=C, Management=A |

---

### Obligation 6: Systemic Risk Assessment & Mitigation — Art. 55(1)(b)

**Obligation:** Assess and mitigate possible systemic risks, including their sources, that may stem from the development, the placing on the market, or the use of general-purpose AI models with systemic risk.

**What this means:**
- Identify potential systemic risks (misuse at scale, critical infrastructure, public safety)
- Develop mitigation measures
- Document risk assessment
- Implement safeguards proportionate to identified risks

| Aspect | Detail |
|--------|--------|
| Frequency | Before deployment + ongoing |
| Effort | 5/5 |
| RACI | Safety=R, Legal=A, Policy=C |

---

### Obligation 7: Incident Tracking & Reporting — Art. 55(1)(c)

**Obligation:** Keep track of, document, and report to the AI Office and, as appropriate, to national competent authorities, without undue delay, relevant information about serious incidents and possible corrective measures to address them.

**What this means:**
- Establish incident tracking system
- Define criteria for "serious incident"
- Report to EU AI Office without undue delay
- Document incidents and corrective measures
- Inform national authorities as appropriate

| Aspect | Detail |
|--------|--------|
| Frequency | Event-driven |
| Effort | 4/5 |
| RACI | Safety=R, Legal=A, Engineering=C |

---

### Obligation 8: Cybersecurity — Art. 55(1)(d)

**Obligation:** Ensure an adequate level of cybersecurity protection for the general-purpose AI model with systemic risk and the physical infrastructure of the model.

**What this means:**
- Protect model weights and parameters
- Secure training infrastructure
- Prevent unauthorized access to model
- Protection against data poisoning and model manipulation
- Physical and logical security measures

| Aspect | Detail |
|--------|--------|
| Frequency | Continuous |
| Effort | 5/5 |
| RACI | Security=R, Engineering=C, Management=A |

---

## GPAI Code of Practice — Art. 56

**Published:** 10 July 2025 | **Endorsed:** 1 August 2025 (Commission + AI Board adequacy decisions)

The GPAI Code of Practice provides detailed implementation guidance for Art. 53 and 55 obligations. Compliance with the Code creates a **presumption of compliance** with the obligations. The Code is not legally binding, but endorsed via adequacy decisions — it presents a practical compliance path.

**Three chapters:**
- (i) Transparency — applies to all GPAI providers
- (ii) Copyright — applies to all GPAI providers
- (iii) Safety and security — applies to systemic risk GPAI providers

**Important:** Always search for the latest version of the Code of Practice, as it is periodically updated.

---

## Open-Source Partial Exemption — Art. 53(2)

GPAI models released under free and open-source licenses are exempted from:
- Art. 53(1)(a) — Technical documentation
- Art. 53(1)(b) — Information to downstream providers

**Still required even with exemption:**
- Art. 53(1)(c) — Copyright compliance
- Art. 53(1)(d) — Training data summary (publicly available)
- All Art. 55 obligations if systemic risk applies

**The exemption does NOT apply to GPAI models with systemic risk.**

---

## Summary: GPAI Obligations Matrix

| # | Obligation | Article | Standard GPAI | Systemic Risk GPAI | Open-Source GPAI |
|---|-----------|---------|--------------|-------------------|-----------------|
| 1 | Technical documentation | Art. 53(1)(a) | Required | Required | Exempted |
| 2 | Info to downstream | Art. 53(1)(b) | Required | Required | Exempted |
| 3 | Copyright compliance | Art. 53(1)(c) | Required | Required | Required |
| 4 | Training data summary | Art. 53(1)(d) | Required | Required | Required |
| 5 | Model evaluation | Art. 55(1)(a) | — | Required | — (unless systemic) |
| 6 | Systemic risk mitigation | Art. 55(1)(b) | — | Required | — (unless systemic) |
| 7 | Incident reporting | Art. 55(1)(c) | — | Required | — (unless systemic) |
| 8 | Cybersecurity | Art. 55(1)(d) | — | Required | — (unless systemic) |

---

## Timeline

| Date | Effective |
|------|-----------|
| 2 Aug 2025 | All GPAI obligations (Art. 51-55) |
| 2 Aug 2025 | GPAI Code of Practice applicable |
| Ongoing | AI Office may update systemic risk thresholds |
