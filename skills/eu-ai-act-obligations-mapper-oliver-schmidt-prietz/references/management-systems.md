# Management Systems — Risk, Quality, Data, Post-Market Monitoring

## Overview

The AI Act requires several management systems for high-risk AI. These overlap with and can be aligned to existing management system standards (ISO 42001, ISO 27001, ISO 9001).

---

## Risk Management System — Art. 9

### Structure

```
RISK MANAGEMENT SYSTEM (Art. 9)

Phase 1: IDENTIFY
├── Known risks to health/safety/fundamental rights
├── Reasonably foreseeable risks
├── Risks from intended use
└── Risks from foreseeable misuse

Phase 2: ASSESS
├── Estimate likelihood (probability)
├── Estimate severity (impact)
├── Evaluate against acceptable risk levels
└── Consider cumulative effects

Phase 3: MITIGATE
├── Design measures (Art. 9(4)(a))
├── Information/training measures (Art. 9(4)(b))
├── Technical measures (Art. 9(4)(c))
└── Residual risk documentation (Art. 9(4)(d))

Phase 4: TEST
├── Pre-market testing (Art. 9(6))
├── Appropriate metrics (Art. 9(7))
├── Real-world conditions (Art. 9(8))
└── Bias testing

Phase 5: MONITOR
├── Post-market monitoring data (Art. 72)
├── Incident data (Art. 73)
├── Deployer feedback
└── Risk reassessment (periodic)
```

### Implementation Guidance

| Element | ISO 42001 Alignment | ISO 27001 Alignment |
|---------|---------------------|---------------------|
| Risk identification | Clause 6.1 | Clause 6.1.2 |
| Risk assessment | Clause 6.1 | Clause 6.1.2 |
| Risk treatment | Clause 6.1 | Clause 6.1.3 |
| Monitoring | Clause 9.1 | Clause 9.1 |
| Management review | Clause 9.3 | Clause 9.3 |

---

## Quality Management System — Art. 17

### Required Elements

| # | Element | Description | Art. 17 Ref |
|---|---------|-------------|-------------|
| 1 | Compliance strategy | Strategy for regulatory compliance | Art. 17(1)(a) |
| 2 | Design & development QC | Techniques, procedures, actions for design/development quality | Art. 17(1)(b) |
| 3 | Testing & validation | Pre-, during-, and post-development testing | Art. 17(1)(c) |
| 4 | Technical specifications | Standards and specifications applied | Art. 17(1)(d) |
| 5 | Data management | Systems for data collection, analysis, labeling, storage, filtering, mining, aggregation, retention | Art. 17(1)(e) |
| 6 | Risk management | Integration with Art. 9 risk management | Art. 17(1)(f) |
| 7 | Post-market monitoring | Integration with Art. 72 monitoring | Art. 17(1)(g) |
| 8 | Incident reporting | Procedures for Art. 73 serious incident reporting | Art. 17(1)(h) |
| 9 | Communication | With authorities, operators, customers | Art. 17(1)(i) |
| 10 | Resource management | Including supply chain management | Art. 17(1)(j) |
| 11 | Accountability framework | Documented accountability structure | Art. 17(1)(k) |

### ISO 42001 Alignment

ISO 42001:2023 (AI Management Systems) provides a comprehensive framework that aligns closely with Art. 17. Organizations with ISO 42001 certification have a strong foundation for AI Act QMS compliance.

| ISO 42001 Clause | AI Act Art. 17 Element |
|-------------------|----------------------|
| 4. Context of the organization | Compliance strategy |
| 5. Leadership | Accountability framework |
| 6. Planning | Risk management, compliance strategy |
| 7. Support | Resource management, competence |
| 8. Operation | Design & development, testing, data management |
| 9. Performance evaluation | Post-market monitoring, testing |
| 10. Improvement | Incident reporting, corrective actions |

**Always search for latest ISO 42001 implementation guidance for AI Act alignment.**

---

## Data Quality Management — Art. 10

### Framework

```
DATA QUALITY MANAGEMENT

1. DATA GOVERNANCE POLICY
   ├── Design choices documented
   ├── Collection processes documented
   ├── Preparation operations documented
   └── Assumptions formulated

2. DATA QUALITY CRITERIA
   ├── Relevance — appropriate for intended purpose
   ├── Representativeness — reflects target population
   ├── Completeness — sufficient coverage
   ├── Accuracy — free of errors to best extent
   └── Timeliness — current and up-to-date

3. BIAS MANAGEMENT
   ├── Examination for biases (Art. 10(2)(f))
   ├── Gap identification (Art. 10(2)(g))
   ├── Mitigation measures
   └── Special categories processing (Art. 10(5))

4. DATA LIFECYCLE
   ├── Collection → Validation → Processing → Storage → Deletion
   ├── Version control
   ├── Audit trail
   └── Retention policies
```

### GDPR Alignment

Data quality management under Art. 10 aligns with GDPR principles:

| AI Act Art. 10 | GDPR Principle | GDPR Article |
|----------------|----------------|-------------|
| Data quality | Accuracy | Art. 5(1)(d) |
| Representativeness | Fairness | Art. 5(1)(a) |
| Bias management | Non-discrimination | Art. 5(1)(a) |
| Data minimization | Data minimization | Art. 5(1)(c) |
| Retention policies | Storage limitation | Art. 5(1)(e) |
| Data governance | Accountability | Art. 5(2) |

---

## Post-Market Monitoring — Art. 72

### Requirements

**Provider obligation:** Establish and document a post-market monitoring system in a manner that is proportionate to the nature and risks of the AI system.

### System Components

| Component | Description | Frequency |
|-----------|-------------|-----------|
| Data collection | Actively collect performance data from deployers | Ongoing |
| Performance analysis | Analyze system accuracy, reliability, performance | Regular |
| Incident tracking | Track and analyze incidents and near-misses | Ongoing |
| Risk reassessment | Feed monitoring data into risk management (Art. 9) | Periodic |
| Compliance evaluation | Evaluate continued compliance with requirements | Periodic |
| Corrective actions | Implement corrections based on monitoring data | As needed |
| Reporting | Report to authorities as required | Per Art. 72(3) |

### Post-Market Monitoring Plan

**Content (Art. 72(2)):**
- Description of data collection methodology
- Description of data analysis methodology
- Frequency of monitoring activities
- Criteria for triggering corrective actions
- Procedures for communicating with deployers
- Procedures for reporting to authorities

For a comprehensive deep-dive on post-market monitoring system design, data collection frameworks, analysis methodology, serious incident reporting procedures, and practical implementation guidance, see [references/post-market-monitoring.md](references/post-market-monitoring.md).

### Interaction with Deployer Obligations

Deployer contributions to post-market monitoring:
- Art. 26(5): Monitoring system operation and informing provider
- Art. 26(6): Retaining logs (available to provider on request)
- Art. 72(4): Providing post-market monitoring data to provider

---

## Incident Reporting — Art. 73

### Serious Incident Definition — Art. 3(49)

A serious incident means any incident or malfunctioning of an AI system that directly or indirectly leads to:
- (a) Death or serious damage to health of a person
- (b) Serious and irreversible disruption of management or operation of critical infrastructure
- (c) Breach of obligations under Union law intended to protect fundamental rights
- (d) Serious damage to property or the environment

### Reporting Timelines

| Severity | Timeline | Recipient |
|----------|----------|-----------|
| Death or serious health damage | Within 2 days of becoming aware | Market surveillance authority (where incident occurred) |
| Other serious incidents | Within 15 days of becoming aware | Market surveillance authority (where incident occurred) |
| Widespread harm | Immediately | Market surveillance authority + AI Office |

### Report Content

| Element | Description |
|---------|-------------|
| System identification | Provider name, system name, version, registration number |
| Incident description | What happened, when, where, who affected |
| Severity assessment | Death/health/infrastructure/rights/property/environment |
| Root cause (if known) | Technical, operational, or human factors |
| Corrective measures | Actions taken or planned |
| Contact information | Person responsible for follow-up |

---

## Implementation Priority Matrix

| Management System | Priority | Complexity | Existing Standard |
|-------------------|----------|------------|-------------------|
| Risk Management (Art. 9) | CRITICAL | High | ISO 31000, ISO 42001 |
| QMS (Art. 17) | HIGH | High | ISO 9001, ISO 42001 |
| Data Quality (Art. 10) | HIGH | Medium | ISO 8000, ISO 42001 |
| Post-Market Monitoring (Art. 72) | HIGH | Medium | ISO 42001 |
| Incident Reporting (Art. 73) | CRITICAL (procedure) | Medium | Existing incident response |
| Logging (Art. 12) | CRITICAL | Low-Medium | Existing IT logging |
