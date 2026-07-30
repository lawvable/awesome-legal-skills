# NIST CSF 2.0 — Implementation Tiers

Source: NIST Cybersecurity Framework 2.0, Section 3.2 (February 2024)

---

## Overview

Implementation Tiers describe the degree to which an organization's cybersecurity risk management practices exhibit the characteristics defined in the CSF. They provide context for how an organization views cybersecurity risk management and the processes in place to manage risk.

**Key principles:**
- Tiers are **not maturity levels** — there is no requirement to advance to Tier 4
- Tier selection should reflect the organization's goals, legal/regulatory requirements, and risk reduction objectives
- Moving to a higher tier is appropriate only when it would reduce cybersecurity risk at a justifiable cost
- Organizations should operate at the tier appropriate for their risk environment — not the highest achievable tier

---

## The Four Tiers

### Tier 1 — Partial

**Risk Management Process**: Cybersecurity risk management practices are not formalised, and risk is managed in an ad hoc and sometimes reactive manner. Prioritisation of cybersecurity activities may not be directly informed by organisational risk objectives, the threat environment, or business/mission requirements.

**Integrated Risk Management Program**: There is limited awareness of cybersecurity risk at the organisational level. The organisation implements cybersecurity risk management on an irregular, case-by-case basis due to varied experience or information gained from outside sources. The organisation may not have processes that enable cybersecurity information to be shared within the organisation.

**External Participation**: The organisation does not understand its role in the larger ecosystem with respect to either its dependencies or dependents. The organisation does not have the processes in place to participate in coordination or collaboration with other entities.

**Diagnostic indicators of Tier 1:**
- No formal cybersecurity policy exists or it has not been approved by leadership
- Asset inventories are incomplete or inconsistently maintained
- Risk assessments are performed reactively (after incidents, not proactively)
- No defined roles or responsibilities for cybersecurity
- Incident response is ad hoc with no documented plan
- Supply chain risks are not considered

---

### Tier 2 — Risk-Informed

**Risk Management Process**: Risk management practices are approved by management but may not be established as organisational-wide policy. The prioritisation of cybersecurity activities and protection needs is directly informed by organisational risk objectives, the threat environment, or business/mission requirements.

**Integrated Risk Management Program**: There is an awareness of cybersecurity risk at the organisational level, but an organisation-wide approach to managing cybersecurity risk has not been established. Cybersecurity information is shared within the organisation on an informal basis. Consideration of cybersecurity in organisational objectives and programs may occur at some but not all levels of the organisation.

**External Participation**: The organisation knows its role in the larger ecosystem with respect to its own dependencies, but has not formalised its capabilities to interact and share information externally.

**Diagnostic indicators of Tier 2:**
- Cybersecurity policy exists and is management-approved, but inconsistently followed
- Risk assessments are performed but not on a regular schedule
- Asset inventory is maintained but may have gaps
- Roles for cybersecurity exist but accountability is not enforced
- Incident response plan exists but has not been tested
- Supply chain risk considered for some but not all suppliers

---

### Tier 3 — Repeatable

**Risk Management Process**: The organisation's risk management practices are formally approved and expressed as policy. Cybersecurity practices are regularly updated based on the application of risk management processes to changes in business/mission requirements and a changing threat and technology landscape.

**Integrated Risk Management Program**: There is an organisation-wide approach to managing cybersecurity risk. Risk-informed policies, processes, and procedures are defined, implemented as intended, and reviewed. Consistent methods are in place to respond effectively to changes in risk. Personnel possess the knowledge and skills to perform their appointed roles and responsibilities. The organisation consistently and accurately monitors cybersecurity risk of assets.

**External Participation**: The organisation understands its dependencies and dependents in the larger ecosystem and may contribute to the community's broader understanding of risks. It collaborates with and receives information from supply chain partners, which enables prioritisation and validation of cybersecurity risk management activities.

**Diagnostic indicators of Tier 3:**
- Formal cybersecurity policy is enforced organisation-wide
- Risk assessments are conducted on a regular, defined schedule
- Asset inventory is comprehensive and actively maintained
- Defined roles with accountability metrics; performance reviewed
- Incident response plan is documented, tested, and updated
- Third-party risk is formally assessed for all critical suppliers
- Cybersecurity metrics are reported to leadership

---

### Tier 4 — Adaptive

**Risk Management Process**: The organisation adapts its cybersecurity practices based on previous and current cybersecurity activities, including lessons learned and predictive indicators derived from previous and current cybersecurity activities. Through a process of continuous improvement incorporating advanced cybersecurity technologies and practices, the organisation actively adapts to a changing threat and technology landscape and responds in a timely and effective manner to evolving, sophisticated threats.

**Integrated Risk Management Program**: There is an organisation-wide approach to managing cybersecurity risk that uses risk-informed policies, processes, and procedures to address potential cybersecurity events. Cybersecurity risk management is part of the organisational culture and evolves from an awareness of previous activities and continuous awareness of activities on organisational systems and networks. The organisation can quickly and efficiently account for new knowledge to continuously improve security practices and integrate into risk management practices.

**External Participation**: The organisation receives, generates, and reviews prioritised information that informs continuous analysis of its risks as the threat and technology landscapes evolve. The organisation shares that information internally and externally on a routine basis. The organisation uses real-time or near real-time information to understand and consistently act upon supply chain risks throughout the technology product and service lifecycle. The organisation communicates proactively, using formal and informal mechanisms, to develop and maintain strong supply chain relationships.

**Diagnostic indicators of Tier 4:**
- Cybersecurity risk management is embedded in organisational culture
- Threat intelligence is operationalised and feeds real-time risk decisions
- Continuous monitoring with automated anomaly detection
- Lessons learned from incidents systematically improve controls
- Active participation in information sharing communities (ISACs, etc.)
- Supply chain risk managed in real time across the full lifecycle
- Cybersecurity KPIs drive leadership strategy decisions

---

## Tier Assessment Guide

When assessing an organisation's current tier, evaluate these three dimensions:

### Dimension 1: Risk Management Process
Ask:
- Is cybersecurity risk management ad hoc (Tier 1), management-approved (Tier 2), policy-formalised (Tier 3), or continuously adapting (Tier 4)?
- Are risk assessments conducted reactively, periodically, or continuously?
- Is there a documented risk management methodology consistently applied?

### Dimension 2: Integrated Risk Management Program
Ask:
- Is cybersecurity risk managed in silos or integrated into enterprise risk management?
- Does cybersecurity risk information flow to leadership on a regular basis?
- Are cybersecurity objectives aligned with business objectives?

### Dimension 3: External Participation
Ask:
- Does the organisation know which external entities it depends on and which depend on it?
- Does the organisation participate in threat intelligence sharing?
- Is supply chain risk actively managed across all critical third parties?

---

## Tier Advancement Guidance

Advancing tiers requires sustained investment. Common barriers and enablers:

| From → To | Common Barriers | Key Enablers |
|-----------|----------------|-------------|
| 1 → 2 | No leadership buy-in, no budget | Tie first risk assessment to a business event (audit, incident, M&A) |
| 2 → 3 | Inconsistent enforcement, siloed teams | Embed cybersecurity in HR processes; create organisation-wide policy with enforcement |
| 3 → 4 | Technology and process gaps, culture | Implement threat intelligence feeds; automate monitoring; build continuous improvement loops |

**Recommended starting sequence for Tier 1 → 2 transition:**
1. GV.OC-01 — Document the organisational mission and cybersecurity context
2. GV.RM-01, GV.RM-02 — Establish risk management objectives and risk tolerance
3. ID.AM-01, ID.AM-02 — Build asset inventories
4. GV.RR-02 — Define cybersecurity roles and responsibilities
5. GV.PO-01 — Establish and communicate a cybersecurity policy
6. ID.RA-03, ID.RA-04 — Perform an initial risk assessment
