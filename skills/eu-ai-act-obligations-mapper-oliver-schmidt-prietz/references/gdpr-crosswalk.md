# AI Act — GDPR Obligation Crosswalk

## Overview

The AI Act and GDPR create overlapping obligations when AI systems process personal data. This reference maps the intersections and identifies where existing GDPR compliance skills can be leveraged.

---

## Primary Crosswalk Table

| AI Act Obligation | AI Act Article | GDPR Parallel | GDPR Article | Recommended Action | Trigger |
|------------------|---------------|---------------|-------------|----------------|---------|
| DPIA before deployment | Art. 26(9) | DPIA requirement | Art. 35 GDPR | Perform DPIA per Art. 35 GDPR | High-risk AI processing personal data |
| Inform affected persons | Art. 26(11) | Transparency | Art. 13/14 GDPR | Draft combined AI Act + GDPR transparency notice | Any AI system affecting natural persons |
| Data governance | Art. 10 | Data protection by design | Art. 25 GDPR | Conduct data inventory and governance review | AI system using personal data for training |
| Employee information | Art. 26(7) | Employee transparency | Art. 13/14 GDPR | Prepare employee AI transparency documentation | Workplace AI deployment |
| Incident reporting | Art. 26(5) s.3, Art. 73 | Breach notification | Art. 33/34 GDPR | Establish dual incident reporting procedure | Serious incident involving personal data |
| Provider as processor | N/A (contractual) | Processor obligations | Art. 28 GDPR | Review/extend processor agreement per Art. 28 GDPR | AI provider processes data on behalf of deployer |
| Bias monitoring with special data | Art. 10(5) | Special categories | Art. 9 GDPR | N/A | Using sensitive data for bias detection |
| Automated decision-making | Art. 14 (human oversight) | Automated decisions | Art. 22 GDPR | N/A | AI system making decisions with legal effects |
| Log retention | Art. 26(6) | Storage limitation | Art. 5(1)(e) GDPR | N/A | Logs containing personal data |
| Risk management | Art. 9 | Risk-based approach | Art. 32 GDPR | N/A | AI risk assessment overlapping security |

---

## Detailed Cross-References

### 1. DPIA — Art. 26(9) AI Act + Art. 35 GDPR

**AI Act requirement:**
> Deployers of high-risk AI systems shall use the information provided under Article 13 to carry out a data protection impact assessment under Article 35 of Regulation (EU) 2016/679 or Article 27 of Directive (EU) 2016/680 where applicable.

**Connection:**
- The AI Act explicitly requires DPIA for high-risk AI systems processing personal data
- The DPIA must incorporate AI-specific information from the provider (Art. 13)
- Must be completed BEFORE putting the system into service
- A single DPIA may cover both GDPR and AI Act requirements

**Skill suggestion:** "Consider performing a Data Protection Impact Assessment (DPIA) — the AI Act Art. 26(9) explicitly requires DPIA for high-risk AI systems processing personal data. The DPIA should incorporate the provider's Art. 13 information about system capabilities, accuracy, and limitations."

**DPIA AI-specific considerations:**
- AI system's accuracy and error rates (from Art. 13 information)
- Risk of biased outputs affecting data subjects
- Automated decision-making impact (Art. 22 GDPR)
- Special categories processing for bias monitoring (Art. 10(5))
- Log retention period vs. storage limitation principle

---

### 2. Transparency — Art. 26(11) AI Act + Art. 13/14 GDPR

**AI Act requirement:**
> Deployers shall inform natural persons who are subject to decisions taken or materially influenced by the high-risk AI system that they are subject to the use of the high-risk AI system.

**GDPR requirement (Art. 13(2)(f)/14(2)(g)):**
> The controller shall provide information about the existence of automated decision-making, including profiling, meaningful information about the logic involved, and the significance and envisaged consequences.

**Connection:**
- Both require informing data subjects about AI use
- AI Act adds obligation even when GDPR Art. 22 (automated decisions) does not apply
- Information may be combined in a single privacy notice
- Art. 50 transparency obligations may also apply (interaction disclosure, synthetic content)

**Skill suggestion:** "Consider preparing a combined AI Act/GDPR transparency notice — Art. 26(11) AI Act requires informing affected persons about the AI system. This overlaps with GDPR Art. 13/14 transparency. A single notice can address both."

---

### 3. Data Governance — Art. 10 AI Act + Art. 25 GDPR

**AI Act requirement:**
Training data must meet quality criteria: relevant, representative, error-free, complete.

**GDPR requirement (Art. 25):**
Data protection by design and by default.

**Connection:**
- Art. 10 data quality requirements complement GDPR data quality principle (Art. 5(1)(d))
- Data governance framework must address both AI quality and privacy requirements
- Special categories processing (Art. 10(5)) requires GDPR Art. 9 legal basis
- Data minimization (GDPR) may conflict with representativeness (AI Act) — balance required

**Skill suggestion:** "Consider conducting a data inventory review — Art. 10 AI Act requires comprehensive data governance for AI training data. Your existing GDPR data inventory can serve as foundation."

---

### 4. Employee Information — Art. 26(7) AI Act + Art. 13/14 GDPR

**AI Act requirement:**
> Before putting into service or using a high-risk AI system at the workplace, deployers who are employers shall inform workers' representatives and the affected workers.

**GDPR requirement:**
Employees must be informed about processing of their personal data (Art. 13/14).

**Connection:**
- AI Act adds a specific workplace AI disclosure obligation
- Must inform works council/employee representatives (national labor law)
- Individual workers must also be informed
- Information can be integrated with existing employee privacy notices

**Skill suggestion:** "Consider preparing employee AI transparency documentation — Art. 26(7) requires informing employees about workplace AI. This complements your GDPR employee transparency obligations."

---

### 5. Incident Reporting — Art. 26(5)/73 AI Act + Art. 33/34 GDPR

**AI Act requirement:**
Report serious incidents to provider and market surveillance authority without undue delay.

**GDPR requirement:**
Report personal data breaches to supervisory authority within 72 hours (Art. 33) and to data subjects if high risk (Art. 34).

**Connection:**
- AI incident may simultaneously constitute a personal data breach
- Both reporting obligations must be fulfilled independently
- Different authorities: market surveillance (AI Act) vs. data protection authority (GDPR)
- Different timelines: 2/15 days (AI Act Art. 73) vs. 72 hours (GDPR Art. 33)
- An AI malfunction exposing personal data triggers both regimes

**Skill suggestion:** "If an AI incident involves personal data, consider establishing a dual AI Act/GDPR incident reporting procedure — you may have simultaneous AI Act and GDPR reporting obligations to different authorities."

---

### 6. Provider as Data Processor — Art. 28 GDPR

**Scenario:**
When a deployer uses a provider's AI system to process personal data, the provider may be a data processor under GDPR.

**Connection:**
- AI provider processing data on deployer's behalf → Art. 28 GDPR processor agreement needed
- Agreement should also cover AI Act obligations (Art. 25(2) cooperation, Art. 72 post-market monitoring data)
- Data quality requirements (Art. 10) may require data access terms in the agreement
- Log retention (Art. 26(6)) may involve provider-held data

**Skill suggestion:** "Consider reviewing your GDPR Art. 28 processor agreement — if the AI provider processes personal data on your behalf, the agreement should also address AI Act cooperation obligations (Art. 25(2))."

---

## Conflict Resolution

Where AI Act and GDPR obligations conflict:

| Conflict Area | AI Act Requires | GDPR Requires | Resolution |
|---------------|----------------|---------------|------------|
| Training data volume | Representativeness (more data) | Data minimization (less data) | Balance: minimum necessary for representative dataset |
| Special categories | Art. 10(5) allows for bias detection | Art. 9 restricts special categories | Art. 10(5) provides specific legal basis with safeguards |
| Log retention | 6 months minimum (Art. 26(6)) | Storage limitation (Art. 5(1)(e)) | AI Act creates legal basis for 6-month retention |
| Transparency detail | System capabilities/limitations | Meaningful information about logic | Combined notice meeting both requirements |
| Incident reporting | Market surveillance authority | Data protection authority | Report to both independently |

---

## Compliance Integration Checklist

| # | Action | AI Act | GDPR | Combined? |
|---|--------|--------|------|-----------|
| 1 | DPIA | Art. 26(9) | Art. 35 | YES — single DPIA covering both |
| 2 | Privacy notice | Art. 26(11) | Art. 13/14 | YES — combined notice |
| 3 | Employee notification | Art. 26(7) | Art. 13/14 | YES — combined with employee privacy notice |
| 4 | Data inventory | Art. 10 | Art. 30 ROPA | YES — extend ROPA with AI data governance |
| 5 | Processor agreement | N/A | Art. 28 | EXTEND — add AI Act provisions |
| 6 | Incident procedure | Art. 73 | Art. 33/34 | EXTEND — dual reporting procedure |
| 7 | Risk assessment | Art. 9 | Art. 32 | COMPLEMENT — separate but aligned |
| 8 | Training | Art. 4 | General awareness | EXTEND — add AI-specific modules |
