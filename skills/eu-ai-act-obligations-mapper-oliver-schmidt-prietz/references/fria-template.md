# Fundamental Rights Impact Assessment — Template & Methodology (Art. 27)

## Process Profile

| Aspect | Detail |
|--------|--------|
| Legal basis | Art. 27 |
| Frequency | Before deployment (review periodically) |
| Time effort | 5/5 |
| Expertise required | 5/5 |
| AI competency | 3/5 |
| RACI | Legal=R, Compliance=A, HR/Operations=C |

*German: Grundrechte-Folgenabschaetzung (FRIA)*

**Cross-references:** [references/high-risk-deployer-obligations.md] (C2), [references/gdpr-crosswalk.md] (DPIA coordination)

---

## 1. Legal Basis & Scope

Art. 27 establishes a pre-deployment assessment obligation targeting the intersection of AI-driven decision-making and fundamental rights. Unlike a general risk assessment, the FRIA demands a rights-centred evaluation — examining how the system's outputs interact with individual entitlements protected under the EU Charter.

### Obligated Deployer Categories

| Category | Rationale | Examples |
|----------|-----------|----------|
| (a) Bodies governed by public law (oeffentlich-rechtliche Stellen) | Sovereign authority amplifies rights exposure | Municipal governments, public employment agencies, social insurance bodies |
| (b) Private entities providing public services (private Dienstleister im oeffentlichen Interesse) | Delegated public-service function carries equivalent responsibility | Outsourced welfare administration, privatised public transport screening |
| (c) Insurance risk assessment deployers (Annex III Nr. 5(b)) | Direct impact on access to financial protection | Insurers using AI for premium calculation or claim eligibility |
| (d) Social benefits eligibility deployers (Annex III Nr. 5(c)) | Determines access to subsistence-level support | Agencies assessing housing benefit, unemployment, disability support |

**Temporal trigger:** Assessment must be completed **before first deployment** (vor erstmaligem Einsatz). Periodic review whenever the system context materially changes — new population groups, expanded use cases, or updated model versions.

### Relationship to DPIA (Art. 26(9))

| Dimension | FRIA (Art. 27) | DPIA (Art. 35 GDPR) |
|-----------|---------------|---------------------|
| Protected interest | Full fundamental rights catalogue | Personal data and privacy |
| Legal framework | AI Act | GDPR |
| Scope | All affected persons, including non-data-subjects | Data subjects only |
| Output | Rights impact evaluation + mitigation plan | Privacy risk register + safeguards |
| Supervisory body | Market surveillance authority | Data protection authority |

The two instruments are **complementary, not duplicative**. A DPIA does not satisfy the FRIA requirement, and vice versa. They may share underlying analysis — see Section 5.

---

## 2. FRIA Content Requirements (Art. 27(1))

Art. 27(1) prescribes seven mandatory elements. Each is presented below with practical guidance and quality indicators.

### Element 1 — Deployer Process Description
**Requirement:** Describe the deployer's processes in which the high-risk AI system will be used.
- Map the end-to-end decision workflow: data intake, AI output, human decision, communication to affected person
- Identify which decisions the AI system influences, advises, or automates
- Quality check: [ ] Process flow included [ ] Decision points identified [ ] Advisory vs. determinative role clear

### Element 2 — Period and Frequency of Use
**Requirement:** State the intended timeframe and operational cadence.
- Define start date, planned duration, and conditions for discontinuation
- Specify continuous, batch, or on-demand operation; note seasonal variations
- Quality check: [ ] Start date and review schedule documented [ ] Reassessment conditions stated

### Element 3 — Affected Population Mapping
**Requirement:** Identify categories of natural persons and groups likely to be affected.
- Enumerate all population segments subject to AI-influenced decisions with estimated volumes
- Pay particular attention to vulnerable groups (Schutzbeduerfte Gruppen): minors, elderly, persons with disabilities, non-native speakers, low-income populations
- Include indirect effects — persons not directly assessed but affected (e.g., dependants of a benefit applicant)
- Quality check: [ ] All categories listed [ ] Vulnerable subgroups identified [ ] Indirect pathways described

### Element 4 — Specific Risks of Harm
**Requirement:** Identify specific risks of harm likely to impact the identified categories and groups.
- Assess risk per fundamental right (see Section 3 for the rights catalogue)
- Consider both false-positive and false-negative scenarios and their distinct harms
- Evaluate compounding effects and distinguish systemic from individual risks
- Quality check: [ ] Risks mapped to Charter rights [ ] Both error directions analysed [ ] Group-level disparity assessed

### Element 5 — Human Oversight Measures
**Requirement:** Describe human oversight measures as specified in the instructions for use.
- Reference the provider's Art. 14 human oversight specifications
- Describe how override authority is exercised in practice, not only on paper
- Document competence requirements for the oversight role per Art. 26(2)
- Quality check: [ ] Oversight model identified [ ] Override procedure documented [ ] Escalation path defined

### Element 6 — Risk Mitigation Measures
**Requirement:** Document measures taken to address identified risks, including internal governance.
- For each risk in Element 4, specify corresponding mitigation: technical safeguards, procedural controls, governance structures
- Where residual risk remains, document the rationale for accepting it
- Quality check: [ ] Each risk has a corresponding measure [ ] Measures are specific [ ] Governance structure documented

### Element 7 — Assessment Date and Validity Period
**Requirement:** Record the date of the assessment and the applicable period.
- State completion date and assessor(s); define validity period (max 24 months recommended)
- Specify reassessment triggers: model update, scope expansion, regulatory change, incident
- Quality check: [ ] Date and assessor recorded [ ] Validity period set [ ] Triggers enumerated

---

## 3. Assessment Methodology

### Fundamental Rights Catalogue for AI Impact Analysis

Rights from the EU Charter (Charta der Grundrechte der EU) with particular AI relevance:

| Right | Charter Art. | AI-Relevant Exposure | Typical Scenario |
|-------|-------------|---------------------|------------------|
| Human dignity (Menschenwuerde) | Art. 1 | Reduction of persons to data profiles | Scoring systems determining access to essential services |
| Non-discrimination (Nichtdiskriminierung) | Art. 21 | Proxy discrimination via training data bias | Eligibility model replicating historical biases |
| Private and family life (Privat- und Familienleben) | Art. 7 | Intrusive data collection and inference | Predictive analytics on household composition |
| Data protection (Datenschutz) | Art. 8 | Processing beyond legitimate purpose | Repurposing applicant data for risk profiling |
| Effective remedy (Recht auf wirksamen Rechtsbehelf) | Art. 47 | Opaque decision logic impeding contestation | Automated rejection without explainable rationale |
| Social security (Soziale Sicherheit) | Art. 34 | Wrongful denial of entitled benefits | False-negative eligibility determination |
| Freedom of expression (Meinungsfreiheit) | Art. 11 | Chilling effect through surveillance perception | Monitoring systems in public spaces |
| Workers' rights (Arbeitnehmerrechte) | Art. 27-31 | Algorithmic management undermining autonomy | AI-driven performance scoring, scheduling |

### Risk Severity and Likelihood Matrix

| | Negligible (1) | Low (2) | Moderate (3) | High (4) | Very high (5) |
|---|---|---|---|---|---|
| **Critical severity (5)** | Medium | High | Critical | Critical | Critical |
| **Major severity (4)** | Low | Medium | High | Critical | Critical |
| **Moderate severity (3)** | Low | Low | Medium | High | High |
| **Minor severity (2)** | Negligible | Low | Low | Medium | Medium |
| **Negligible severity (1)** | Negligible | Negligible | Low | Low | Medium |

**Severity calibration:** Critical = irreversible harm (loss of essential services, systemic discrimination); Major = significant but recoverable; Moderate = meaningful inconvenience requiring active remedy; Minor = temporary, easily correctable; Negligible = no appreciable impact.

### Proportionality Framework

| Risk Profile | Assessment Depth | Typical Effort |
|-------------|-----------------|----------------|
| Critical / systemic reach (>10,000 persons) | Full assessment with external expert review | 40-80 hours |
| High / significant population segment | Comprehensive internal assessment | 20-40 hours |
| Moderate / limited population | Standard assessment with focused risk analysis | 10-20 hours |

---

## 4. Worked Example — Municipal Social Benefits Eligibility System

**Scenario:** A German municipality (Gemeinde) deploys an AI system to pre-screen Wohngeld (housing benefit) applications. The system generates an eligibility probability score (0-100) per application. Cases scoring below 40 are flagged for intensive manual review. All final decisions remain with a case worker (Sachbearbeiter/in).

**Element 1 — Process:** Applicants submit forms to the Wohnungsamt. The AI ingests income, household size, rent burden, and employment data to produce the eligibility score. The score determines review sequence and attention level, not the outcome itself.

**Element 2 — Period/Frequency:** Deployment from 01.07.2026. Daily batch processing. Annual volume: ~8,000 applications. Reassessment by 30.06.2027.

**Element 3 — Affected population:** Low-income households applying for Wohngeld. Vulnerable subgroups: single-parent families (30% of pool), elderly pensioners on minimum income, refugees with limited German proficiency, persons with disabilities. Indirect effects: ~2.4 household members per application on average.

**Element 4 — Risks:**

| Risk | Right | Severity | Likelihood | Priority |
|------|-------|----------|------------|----------|
| Systematic under-scoring of non-standard households (multi-generational) leading to wrongful denial | Social security (Art. 34) | Critical (5) | Moderate (3) | Critical |
| Proxy discrimination against migration-background applicants via postcode or employment-pattern features | Non-discrimination (Art. 21) | Major (4) | High (4) | Critical |
| Reduced processing attention for low-scoring cases creating de facto automated rejection | Effective remedy (Art. 47) | Major (4) | Moderate (3) | High |
| Privacy-intrusive inference from combined household data fields | Private life (Art. 7) | Moderate (3) | Moderate (3) | Medium |

**Element 5 — Oversight:** Human-on-the-loop model. Every application receives a final human decision. Oversight person (Fachbereichsleitung Soziales) reviews aggregate scoring patterns weekly. Case workers retain override authority. Escalation: anomalous patterns reported to DPO and department head within 48 hours.

**Element 6 — Mitigation:**

| Risk | Mitigation | Responsible |
|------|-----------|-------------|
| Under-scoring non-standard households | Quarterly bias audit on household-type subgroups; override-rate monitoring | IT + Legal |
| Proxy discrimination | Feature audit removing postcode-correlated proxies; annual fairness review | External auditor + Legal |
| De facto automated rejection | Mandatory case-worker attestation; random sample review of low-score outcomes | Compliance |
| Privacy-intrusive inference | Data minimisation review; limit features to statutory Wohngeld criteria | DPO |

Governance: cross-functional AI Oversight Committee (Fachausschuss KI-Einsatz) meets quarterly to review monitoring reports and authorise continued deployment.

**Element 7 — Date/Validity:** Completed 15.05.2026 by Head of Legal, DPO, Head of Social Services. Valid until 30.06.2027. Early reassessment triggers: model retrain, >15% shift in applicant demographics, substantiated discrimination complaint, regulatory guidance update.

---

## 5. FRIA-DPIA Coordination Table

### Overlap and Divergence

| Dimension | FRIA (Art. 27) | DPIA (Art. 35 GDPR) | Overlap |
|-----------|---------------|---------------------|---------|
| Affected population mapping | Required (Element 3) | Required (data subjects) | High — same analysis, different framing |
| Risk identification | Fundamental rights risks | Privacy and data protection risks | Partial — FRIA broader in scope |
| Mitigation measures | Rights-focused safeguards | Privacy safeguards and security | Partial — technical measures often shared |
| Process description | AI workflow documentation | Processing activity description | High — near-identical input |
| Legal basis analysis | Not required | Required (Art. 6 GDPR) | None |
| DPO consultation | Not mandated | Required where risk is high | Low |
| Supervisory notification | Market surveillance authority | Data protection authority | None — different authorities |

### Single-Process Approach

Running FRIA and DPIA as a unified assessment reduces effort and avoids contradictory conclusions:

**Phase 1 — Shared Foundation:** Document the AI system and decision process (satisfies Element 1 + DPIA processing description). Map all affected persons / data subjects (Element 3 + DPIA scope). Define period and frequency (Element 2 + DPIA temporal scope).

**Phase 2 — Parallel Risk Analysis:** FRIA track assesses each fundamental right per the Charter catalogue. DPIA track assesses data protection risks per GDPR principles (lawfulness, purpose limitation, minimisation, accuracy, storage limitation, security).

**Phase 3 — Unified Mitigation:** Develop measures addressing both rights and privacy risks simultaneously. Flag tensions between rights protection and data minimisation (e.g., collecting demographic data for fairness monitoring).

**Phase 4 — Separate Documentation:** Produce standalone FRIA (for market surveillance authority) and DPIA (for data protection authority). Cross-reference shared analysis sections to maintain consistency.

---

## 6. Output Template

### Fillable FRIA Document Structure

```
FUNDAMENTAL RIGHTS IMPACT ASSESSMENT — Art. 27 AI Act

DEPLOYER IDENTIFICATION
Organisation:
Category: [ ] Public body  [ ] Private/public service  [ ] Annex III 5(b)  [ ] Annex III 5(c)
Contact person:                          Department:

AI SYSTEM IDENTIFICATION
System name / provider:
EU database registration number:         Annex III classification:
Provider instructions for use version:

ELEMENT 1 — PROCESS DESCRIPTION
[Workflow, decision points, human involvement]

ELEMENT 2 — PERIOD AND FREQUENCY
Start date:          Duration:          Cadence:          Review schedule:

ELEMENT 3 — AFFECTED POPULATION
Categories:          Volume:          Vulnerable subgroups:          Indirect effects:

ELEMENT 4 — SPECIFIC RISKS OF HARM
[Per risk: description, affected Charter right, severity, likelihood, priority tier]

ELEMENT 5 — HUMAN OVERSIGHT MEASURES
Model:          Oversight person(s):          Override procedure:          Escalation path:

ELEMENT 6 — RISK MITIGATION MEASURES
[Per risk: measure, responsible party, timeline]
Internal governance arrangements:

ELEMENT 7 — DATE AND VALIDITY
Assessment date:          Assessor(s):          Valid until:          Reassessment triggers:

SIGN-OFF
Responsible person (name, role):          Date:          Signature:
```

### Quality Checklist

| # | Criterion | Status |
|---|-----------|--------|
| 1 | All seven mandatory elements addressed with substantive content | [ ] |
| 2 | Affected population includes vulnerable subgroups with specific identification | [ ] |
| 3 | Each identified risk mapped to a specific EU Charter right | [ ] |
| 4 | Risk severity and likelihood assessed using structured methodology | [ ] |
| 5 | Every risk has at least one corresponding mitigation measure | [ ] |
| 6 | Human oversight arrangements are concrete and operationally realistic | [ ] |
| 7 | Assessment validity period does not exceed 24 months | [ ] |
| 8 | Reassessment triggers include model updates, scope changes, and incidents | [ ] |
| 9 | Internal governance structure for ongoing monitoring documented | [ ] |
| 10 | DPIA coordination addressed — integrated process or cross-referenced standalone | [ ] |
