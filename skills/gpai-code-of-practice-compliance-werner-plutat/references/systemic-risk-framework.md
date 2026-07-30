# Systemic Risk Framework — GPAI Code of Practice

Complete requirements for Safety & Security chapter (Commitments 1–10) applying to providers of GPAI models with systemic risk.

**Legal basis:** Article 55 of Regulation (EU) 2024/1689, operationalised through the Code of Practice Safety & Security chapter.

**Applies to:** Providers of GPAI models classified as having systemic risk under Article 51 (>10^25 FLOPs training compute or Commission designation). Currently ~5–15 companies worldwide.

---

## Table of Contents

1. [Systemic Risk Classification](#systemic-risk-classification)
2. [Commitment 1: Safety & Security Framework](#commitment-1-safety--security-framework)
3. [Commitment 2: Systemic Risk Identification](#commitment-2-systemic-risk-identification)
4. [Commitment 3: Systemic Risk Analysis](#commitment-3-systemic-risk-analysis)
5. [Commitment 4: Risk Acceptance Determination](#commitment-4-risk-acceptance-determination)
6. [Commitment 5: Safety Mitigations](#commitment-5-safety-mitigations)
7. [Commitment 6: Security Mitigations](#commitment-6-security-mitigations)
8. [Commitment 7: Model Reports](#commitment-7-model-reports)
9. [Commitment 8: Responsibility Allocation](#commitment-8-responsibility-allocation)
10. [Commitment 9: Serious Incident Reporting](#commitment-9-serious-incident-reporting)
11. [Commitment 10: Additional Documentation](#commitment-10-additional-documentation)
12. [Risk Categories (Appendix 1)](#risk-categories-appendix-1)
13. [Practical Compliance Steps](#practical-compliance-steps)

---

## Systemic Risk Classification

### Article 51 criteria:

| Path | Criterion | Threshold |
|------|-----------|-----------|
| Automatic presumption | Cumulative training compute | >10^25 FLOPs |
| Commission designation | High-impact capabilities or equivalent | Annex XIII criteria (capabilities, reach, reversibility, autonomy) |

### Contesting the presumption:
The Code of Practice notes that the Commission should establish "a rapid and reliable mechanism for model providers to contest the systemic risk presumption" for models exceeding 10^25 FLOPs. The Commission is also exploring thresholds based on capability-related factors rather than compute alone.

### Current systemic risk models (indicative):
Models from OpenAI (GPT-4+), Google (Gemini Ultra+), Anthropic (Claude 3+), Meta (Llama 3 405B+), and similar frontier models generally exceed the 10^25 FLOP threshold. The exact list evolves as new models are released and classified.

---

## Commitment 1: Safety & Security Framework

### Purpose:
Outline the systemic risk management processes and measures to ensure risks are acceptable.

### Measure 1.1: Creating the Framework
- Develop a state-of-the-art Safety & Security Framework **before** model release
- Framework must specify:
  - Evaluation triggers (when assessments are required)
  - Risk categories covered
  - Mitigation strategy approach
  - Forecasting methods for emerging risks
  - Organisational responsibilities

### Measure 1.2: Implementing the Framework
- Operationalise the Framework across the organisation
- Ensure all relevant teams understand and follow Framework procedures
- Integrate Framework into development and deployment workflows

### Measure 1.3: Updating the Framework
- Regular review and updates in response to:
  - New systemic risks identified
  - Serious incidents
  - Significant changes to model or deployment environment
  - Advances in safety evaluation methodologies
  - Regulatory guidance or standards developments

### Measure 1.4: Framework Notifications
- **Notify the AI Office** of the Framework
- Keep notification current with material changes

---

## Commitment 2: Systemic Risk Identification

### Measure 2.1: Systemic Risk Identification Process
- Follow a **structured process** to identify systemic risks:
  - Maintain a risk inventory
  - Conduct regular horizon scanning
  - Consult internal experts (safety, security, policy, domain experts)
  - Consult external experts (academia, civil society, downstream users)
  - Review reports on similar models and emerging threats

### Measure 2.2: Systemic Risk Scenarios
- Develop **concrete risk scenarios** for each identified risk:
  - Describe the causal chain from model capability to potential harm
  - Assess plausibility and severity
  - Identify affected populations and systems
  - Consider both intentional misuse and unintended consequences
  - Include scenarios for novel, unprecedented risks

---

## Commitment 3: Systemic Risk Analysis

Five analysis elements (may overlap and be applied recursively):

### Measure 3.1: Model-Independent Information
- Gather contextual information not specific to the model:
  - Threat landscape and adversary capabilities
  - Societal vulnerabilities
  - Regulatory environment
  - Existing protective infrastructure

### Measure 3.2: Model Evaluations
- Conduct state-of-the-art evaluations using standardised protocols:
  - **Adversarial testing** (red-teaming) to identify vulnerabilities
  - Capability evaluations against safety benchmarks
  - Stress testing under edge-case conditions
  - Third-party/independent evaluations where feasible
- Document all evaluation methodologies, results, and limitations

### Measure 3.3: Systemic Risk Modelling
- Model the potential systemic impact:
  - Propagation pathways
  - Interaction with other systems and societal structures
  - Scaling effects
  - Cascading failure scenarios

### Measure 3.4: Systemic Risk Estimation
- Estimate severity and likelihood for each identified risk:
  - Quantitative methods where feasible
  - Expert judgment and structured elicitation where quantification is not possible
  - Document confidence levels and uncertainty ranges

### Measure 3.5: Post-Market Monitoring
- **Continuous monitoring** after model deployment:
  - Track real-world use patterns and incidents
  - Monitor for capability discoveries and novel misuse vectors
  - Update risk assessments based on post-market evidence
  - Engage with user community for early warning signals

---

## Commitment 4: Risk Acceptance Determination

### Measure 4.1: Risk Acceptance Criteria
- **Define explicit acceptance criteria** before deployment:
  - Risk-tier framework (e.g., acceptable / conditional / unacceptable)
  - **Built-in safety margins** — criteria should not be at the exact boundary of acceptable risk
  - Criteria should cover both individual risks and aggregate risk profile
  - Regular review and update of criteria

### Measure 4.2: Proceed/Stop Decision
- Based on risk acceptance determination, decide whether to:
  - **Proceed** with development, market placement, or continued deployment
  - **Proceed with conditions** (additional mitigations, restricted access)
  - **Stop** — do not release or withdraw from market
- If risks are deemed **unacceptable**, immediate corrective action required
- Document the decision, reasoning, and any conditions applied

---

## Commitment 5: Safety Mitigations

Implement appropriate safety measures **throughout the entire model lifecycle**:

### Categories of safety mitigations:
- **Pre-deployment:** Alignment training, RLHF, refusal training, content filtering
- **Deployment controls:** Phased access, rate limiting, monitoring, usage policies
- **Output safeguards:** Filtering, watermarking, content classification
- **Downstream safeguards:** Guidance and tools for downstream providers/deployers
- **Ongoing:** Continuous monitoring, rapid response capabilities, model updates

### Lifecycle coverage:
- Training and development
- Pre-release evaluation
- Initial deployment
- Ongoing operation
- Model updates and fine-tuning
- End-of-life and decommissioning

---

## Commitment 6: Security Mitigations

Implement adequate cybersecurity protection for models and physical infrastructure.

### Exemption:
A model is **exempt** from this Commitment if its capabilities are inferior to at least one model whose parameters are publicly available for download.

### Security measures apply until:
- Model parameters are made publicly available for download, OR
- Model is securely deleted

### Required protections (aligned with Appendix 4):

#### Digital security:
- Access controls for model weights and training infrastructure
- Encryption of model assets at rest and in transit
- Secure development lifecycle
- Vulnerability management and patching
- Penetration testing and security audits

#### Physical security:
- Physical access controls for data centres and training infrastructure
- Environmental controls
- Hardware security for model-serving infrastructure

#### Operational security:
- Insider threat controls
- Security monitoring and logging
- Incident response procedures
- Supply chain security for training data and infrastructure

#### Model-specific security:
- Protection against model extraction attacks
- Adversarial robustness measures
- Secure API design and rate limiting

---

## Commitment 7: Model Reports

### Pre-market report to AI Office:

#### Measure 7.1: Model Description and Behaviour
- Architecture, capabilities, intended use
- Known limitations and failure modes

#### Measure 7.2: Risk Identification Summary
- Systemic risks identified (from Commitment 2)
- Risk scenarios developed

#### Measure 7.3: Risk Analysis Results
- Evaluation results, risk estimates
- Confidence levels and methodology

#### Measure 7.4: Mitigation Measures
- Safety and security mitigations implemented
- Residual risk assessment

#### Measure 7.5: Material Changes to Risk Landscape
- Any changes since previous reports
- Emerging risks or new information

#### Measure 7.6: Report Updates
- Keep Model Report **up-to-date** throughout model lifecycle
- Update for material changes in risk profile

#### Measure 7.7: Report Notifications
- **Notify AI Office** of Model Report before market placement
- Notify of material updates

### Practical notes:
- May reference other reports/notifications already provided to AI Office
- May create single report for multiple related models if risk assessment is interconnected
- **SME/SMC accommodation:** May reduce detail level proportionate to size and capacity constraints

---

## Commitment 8: Responsibility Allocation

### Measure 8.1: Clear Responsibilities
- Define responsibilities for systemic risk management **across all organisational levels**:
  - **Board/executive level:** Oversight and strategic direction
  - **Management level:** Risk ownership and resource allocation
  - **Operational level:** Day-to-day monitoring and response
  - **Assurance level:** Independent review and audit

### Measure 8.2: Appropriate Resources
- Allocate sufficient resources to risk management:
  - Personnel (safety teams, red teams, security)
  - Budget for evaluations and external audits
  - Tools and infrastructure for monitoring
  - Training and capability development

### Measure 8.3: Healthy Risk Culture
- Promote organisational risk culture:
  - Leadership commitment to safety
  - Open reporting without retaliation
  - **Whistleblower protections** for safety concerns
  - Regular safety training and awareness
  - Lessons learned from incidents and near-misses

---

## Commitment 9: Serious Incident Reporting

### Requirements:
- **Track and document** serious incidents throughout the model lifecycle
- **Report to AI Office** (and national competent authorities as applicable)
- **Without undue delay** — specific deadlines apply based on severity:
  - Incidents affecting **critical infrastructure:** Report within **2 days**
  - Other serious incidents: Report promptly, with initial notification followed by detailed report
- Reports must include:
  - Incident description and timeline
  - Model involvement assessment
  - Impact assessment (actual and potential)
  - Corrective measures taken or planned
- **Report updates:** Provide updates as new information becomes available
- **Retention:** Keep incident records for at least **5 years**
- **Resourcing:** Proportionate to severity and degree of model involvement

### What constitutes a "serious incident":
- Incidents resulting in death or serious damage to health, property, or environment
- Serious and irreversible disruption of critical infrastructure
- Serious breaches of fundamental rights
- Significant security incidents (model theft, unauthorised access with impact)

---

## Commitment 10: Additional Documentation

### Measure 10.1: Documentation
- Retain detailed records of all safety and risk management activities
- **Minimum retention:** 10 years
- Records must be sufficient to demonstrate compliance

### Measure 10.2: Public Transparency
- **Publish summarised versions** of Framework and Model Reports when necessary to reduce risks
- Exception: Publication not required if the model qualifies as "similarly safe or safer" (see Appendix 2)
- Summaries should be meaningful without compromising security-sensitive information

---

## Risk Categories (Appendix 1)

The Code of Practice identifies these systemic risk categories for structured identification:

| Category | Examples |
|----------|---------|
| CBRN risks | Assistance in creating chemical, biological, radiological, or nuclear weapons |
| Cyber risks | Automated vulnerability discovery, malware generation, attack scaling |
| Manipulation & disinformation | Large-scale persuasion campaigns, deepfake generation, election interference |
| Loss of control | Autonomous goal-pursuit, deceptive alignment, self-replication |
| Discrimination & bias | Systemic bias affecting protected groups at scale |
| Privacy risks | Training data extraction, re-identification, mass surveillance enablement |
| Concentration of power | Market concentration, democratic process undermining |
| Labour market disruption | Rapid displacement without transition support |
| Environmental risks | Excessive energy consumption, resource depletion |

---

## Practical Compliance Steps

### If You Can Only Do Three Things First

The Safety & Security chapter has 10 Commitments and dozens of measures. If resources are constrained, **these three create the foundation everything else builds on:**

1. **Commitment 1 (Safety & Security Framework)** — Without this, everything else is ad hoc. The Framework is the organisational backbone. It defines HOW you do risk management. Start here, even if the first version is imperfect — iterate.

2. **Commitment 2 + 3 (Risk Identification + Analysis)** — You cannot mitigate what you haven't identified. Run a structured risk identification workshop, develop scenarios, then analyse with evaluations (red-teaming, capability benchmarks). This produces the evidence base for everything downstream.

3. **Commitment 7 (Model Report)** — This is what the AI Office actually reads. It synthesises your Framework, risk assessment, and mitigations into a single document. Must be submitted before market placement. If enforcement begins and you don't have this, you're exposed.

**What can wait (briefly):** Commitments 8 (responsibility allocation) and 10 (additional documentation) are important but organisational — they formalise what should already be happening informally. Commitment 9 (incident reporting) needs a process, but the process can be lightweight initially and mature over time.

**What cannot wait:** Commitment 6 (security mitigations) — if your model weights can be stolen, nothing else matters. Ensure basic cybersecurity controls are in place from day one.

### For providers of systemic risk models:

1. **Assess current state** — map existing safety practices against all 10 Commitments
2. **Develop/update Safety & Security Framework** — the foundational document
3. **Conduct structured risk identification** — systematic, not ad hoc
4. **Run evaluations** — adversarial testing, capability evaluations, red-teaming
5. **Document risk acceptance decisions** — explicit criteria, documented reasoning
6. **Implement mitigations** — safety and security measures across the lifecycle
7. **Prepare Model Report** — comprehensive, before market placement
8. **Assign responsibilities** — clear RACI across the organisation
9. **Set up incident reporting** — processes, templates, escalation paths, deadlines
10. **Establish record-keeping** — 10-year retention for all safety activities

### Ongoing obligations:
- Post-market monitoring (continuous)
- Framework and Model Report updates (as conditions change)
- Incident tracking and reporting (ongoing)
- External evaluation engagement (periodic)
- Documentation maintenance (10-year rolling)

---

*Source: GPAI Code of Practice (Final Version, July 2025), Safety & Security Chapter; Regulation (EU) 2024/1689 Articles 51, 55; Appendices 1–4.*
