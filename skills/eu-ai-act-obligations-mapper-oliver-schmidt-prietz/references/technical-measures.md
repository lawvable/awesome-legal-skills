# Technical Measures — Art. 9, 10, 12, 14, 15

## Overview

Technical measures are the design and implementation requirements that must be built into high-risk AI systems. These primarily apply to **providers** (who must design and develop them) but also affect **deployers** (who must understand and operate within them).

---

## Art. 9 — Risk Management System

### Requirements

The risk management system is a **continuous iterative process** throughout the entire lifecycle:

**Step 1: Risk identification and analysis (Art. 9(2)(a))**
- Identify known and reasonably foreseeable risks to health, safety, or fundamental rights
- Consider risks when system is used in accordance with intended purpose
- Consider risks from foreseeable misuse

**Step 2: Risk estimation and evaluation (Art. 9(2)(b))**
- Estimate likelihood and severity of identified risks
- Evaluate risks during intended use AND foreseeable misuse
- Consider interaction effects with other systems or environments

**Step 3: Post-market risk evaluation (Art. 9(2)(c))**
- Evaluate risks based on data from post-market monitoring (Art. 72)
- Incorporate incident reports, user feedback, monitoring data

**Step 4: Risk management measures (Art. 9(2)(d))**
- Adopt appropriate and targeted measures to address risks
- Consider state of the art and proportionality
- Document residual risks and communicate them to deployers

### Testing Requirements (Art. 9(6)-(8))

| Requirement | Description |
|-------------|-------------|
| Appropriate metrics | Define metrics suitable for intended purpose |
| Probabilistic thresholds | Set preliminary performance thresholds |
| Pre-market testing | Test before placing on market |
| Real-world conditions | Test under conditions reflecting actual deployment |
| Bias testing | Test for potential discriminatory impacts |

### Implementation Checklist

| # | Action | Frequency | Responsibility |
|---|--------|-----------|----------------|
| 1 | Establish risk management framework | One-time | Provider |
| 2 | Identify risks (intended use) | Before market + ongoing | Provider |
| 3 | Identify risks (foreseeable misuse) | Before market + ongoing | Provider |
| 4 | Estimate risk severity and likelihood | Before market + periodic | Provider |
| 5 | Design mitigation measures | Before market | Provider |
| 6 | Test mitigation effectiveness | Before market + periodic | Provider |
| 7 | Document residual risks | Before market + updates | Provider |
| 8 | Communicate risks to deployers | Before market + updates | Provider |
| 9 | Monitor post-market data | Ongoing | Provider + Deployer |
| 10 | Update risk assessment | Periodic (recommend annually) | Provider |

---

## Art. 10 — Data and Data Governance

### Data Quality Requirements

**Training, validation, and testing datasets must be:**
1. **Relevant** — appropriate for the intended purpose
2. **Sufficiently representative** — reflect the target population
3. **Free of errors** — to the best extent possible
4. **Complete** — in view of the intended purpose

### Data Governance Framework

| # | Requirement | Description | Article |
|---|------------|-------------|---------|
| 1 | Design choices | Document decisions about data selection and preparation | Art. 10(2)(a) |
| 2 | Collection processes | Document data collection methodology and sources | Art. 10(2)(b) |
| 3 | Preparation operations | Document annotation, labeling, cleaning, enrichment | Art. 10(2)(c) |
| 4 | Assumptions | Formulate and document assumptions about data | Art. 10(2)(d) |
| 5 | Availability assessment | Assess data availability, quantity, suitability | Art. 10(2)(e) |
| 6 | Bias examination | Examine data for possible biases | Art. 10(2)(f) |
| 7 | Gap identification | Identify data gaps and address them | Art. 10(2)(g) |

### Special Categories of Personal Data — Art. 10(5)

Processing special categories (Art. 9 GDPR) is permitted **strictly** for:
- Bias monitoring
- Bias detection
- Bias correction

**Conditions:**
- Appropriate safeguards for fundamental rights
- Technical limitations on re-use
- Security measures
- Data minimization

---

## Art. 12 — Record-Keeping (Logging)

### Design Requirements

High-risk AI systems must technically allow automatic recording of events throughout their lifetime.

**Minimum logging capabilities:**

| Log Element | Description |
|-------------|-------------|
| Period of use | Start and end time of each use instance |
| Reference database | Database against which input data is checked |
| Input data matching | Input data that led to a match |
| Person identification | Natural persons involved in result verification |

### Retention

- Deployer must retain logs for **minimum 6 months** (Art. 26(6))
- Provider must design system to enable log retention
- Logs must be available to authorities upon request

---

## Art. 14 — Human Oversight

### Design Requirements

The system must enable natural persons to:

| # | Capability | Description |
|---|-----------|-------------|
| (a) | Understand | Fully understand capabilities and limitations |
| (b) | Monitor | Properly monitor system operation |
| (c) | Awareness | Remain aware of automation bias |
| (d) | Interpret | Correctly interpret system output |
| (e) | Override | Decide not to use, override, or reverse output |
| (f) | Intervene | Intervene in or interrupt system operation |

### Human Oversight Approaches

**Human-in-the-loop (HITL):** Human verifies every output before action.
**Human-on-the-loop (HOTL):** Human monitors operation and can intervene.
**Human-in-command (HIC):** Human has authority to override at any time.

The appropriate level depends on the risk and context of the AI system.

---

## Art. 15 — Accuracy, Robustness, and Cybersecurity

### Accuracy

| Requirement | Description |
|-------------|-------------|
| Appropriate level | Accuracy suitable for intended purpose |
| Declared metrics | Accuracy levels declared in instructions for use |
| Relevant metrics | Use appropriate metrics for the specific AI system type |
| Consistent performance | Throughout lifecycle, not just at deployment |

### Robustness

| Requirement | Description |
|-------------|-------------|
| Error resilience | Resilient to errors, faults, inconsistencies |
| Technical measures | Technical redundancy, fail-safe mechanisms |
| Organizational measures | Backup procedures, fallback processes |
| Adversarial resilience | Resilient to adversarial conditions (Art. 15(5)) |

### Cybersecurity

| Requirement | Description |
|-------------|-------------|
| Unauthorized access | Protection against unauthorized third-party access |
| Data poisoning | Protection against training data manipulation |
| Model manipulation | Protection against model parameter tampering |
| Adversarial inputs | Protection against adversarial examples (Art. 15(5)) |
| Supply chain | Security of AI system supply chain |
