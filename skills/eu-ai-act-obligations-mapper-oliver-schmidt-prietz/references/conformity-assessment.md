# Conformity Assessment — Art. 43, Annex VI/VII

## 1. Overview

Art. 43 governs the conformity assessment procedure (Konformitaetsbewertung) that every high-risk AI system must pass before it may be placed on the Union market or put into service. It functions as the formal gate between development-phase obligations and market access: only a system that has demonstrably met all Chapter III, Section 2 requirements earns the right to bear CE marking and appear in the EU database.

*German: Konformitaetsbewertungsverfahren*

**Position in the provider compliance sequence:**

| Step | Obligation | Article | Dependency |
|------|-----------|---------|------------|
| 1 | Risk Management System | Art. 9 | Foundation for all subsequent steps |
| 2 | Data Governance | Art. 10 | Requires risk context from Step 1 |
| 3 | Technical Documentation | Art. 11 + Annex IV | Captures Steps 1-2 outputs |
| 4 | Accuracy, Robustness, Cybersecurity | Art. 15 | Validated through testing |
| 5 | **Conformity Assessment** | **Art. 43** | **Examines Steps 1-4 completeness** |
| 6 | EU Declaration of Conformity | Art. 47 + Annex V | Formalizes Step 5 outcome |
| 7 | CE Marking | Art. 48 | Affixed after Step 6 |
| 8 | EU Database Registration | Art. 49 | Final pre-market step |

The assessment is not a standalone audit exercise. It is a structured verification that all upstream obligations have been fulfilled to the standard required by the Regulation. Approaching it as a mere formality or checkbox procedure is a leading cause of delays and non-conformity findings.

Cross-references: [references/high-risk-provider-obligations.md], [references/management-systems.md], [references/compliance-roadmap.md]

| Aspect | Detail |
|--------|--------|
| Legal basis | Art. 43, Annex VI, Annex VII |
| Frequency | Before market placement + on substantial modification |
| Time effort | 4/5 |
| Expertise required | 4/5 |
| AI competency | 3/5 |
| RACI | Quality/Compliance=R, Management=A, Legal/Technical=C |

---

## 2. Track A: Internal Control (Annex VI)

### When It Applies

Track A is the default assessment path for the majority of high-risk AI systems classified under Annex III. Unless a system falls into one of the narrow categories that mandate third-party involvement (see Section 3), the provider may conduct the entire assessment using its own resources and personnel.

*German: Interne Kontrolle*

### Six-Step Procedure

The internal control procedure follows a defined sequence. Each step must be documented with sufficient detail to withstand scrutiny by market surveillance authorities (Marktaufsichtsbehoerden).

| Step | Activity | Verification Target | Key Evidence |
|------|----------|---------------------|--------------|
| 1 | Verify Quality Management System | Art. 17 QMS is established, documented, and actively maintained | QMS manual, process records, audit logs |
| 2 | Examine Technical Documentation | Annex IV documentation is complete, current, and internally consistent | Full documentation package per Annex IV sections 1-8 |
| 3 | Verify Design and Development Process | Development followed documented procedures; design choices are traceable | Design review records, version control history, change logs |
| 4 | Verify Post-Market Monitoring System | Art. 72 monitoring plan exists and is operationally ready | Monitoring plan document, data collection infrastructure, escalation procedures |
| 5 | Verify Risk Management System | Art. 9 risk management is continuous, covers all identified risks, and includes residual risk documentation | Risk register, treatment plans, testing protocols, residual risk acceptance records |
| 6 | Draw Conclusions | Overall conformity determination based on Steps 1-5 | Signed assessment report with per-step findings and final determination |

### Who Performs the Assessment

The provider's own quality or compliance team conducts the assessment. There is no requirement for organizational independence between the assessor and the development team, but establishing functional separation improves credibility. Organizations with an existing internal audit function (e.g., under ISO 9001 or ISO 42001) can leverage that capability.

### Documentation Requirements

The internal control assessment must produce a documented record containing:
- Identification of the AI system assessed (name, version, unique reference)
- Date and scope of the assessment
- Per-step findings with supporting evidence references
- Any non-conformities identified and corrective actions taken
- Final conformity determination with rationale
- Name and signature of the responsible person

Retention period: 10 years after the last unit of the AI system is placed on the market (Art. 18(1)).

---

## 3. Track B: Third-Party Assessment (Annex VII)

### When Third-Party Involvement Is Required

Track B applies in two situations:

| Trigger | Legal Basis | Practical Scope |
|---------|------------|-----------------|
| Biometric identification systems (real-time and post) | Art. 43(1) second subparagraph, Annex III Nr. 1 | Remote biometric identification, biometric categorization, emotion recognition systems used for identification |
| AI embedded in products subject to existing EU harmonization legislation | Art. 43(3), Annex I legislation | AI components in medical devices, machinery, toys, radio equipment, etc. where existing product legislation already mandates notified body involvement |

*German: Konformitaetsbewertung durch benannte Stelle*

### Notified Body Involvement

A notified body (benannte Stelle) is a conformity assessment body designated by a Member State under Art. 28 and notified to the Commission. Only bodies listed in the NANDO database may perform AI Act assessments.

**Notified body competency requirements (Art. 31):**
- Technical knowledge of AI systems and relevant standards
- Independence from the provider and from economic interests
- Impartiality and absence of conflicts of interest
- Professional liability insurance
- Personnel with AI-specific competence and assessment experience

### Application and Assessment Process

```
TRACK B — ASSESSMENT SEQUENCE

Step 1: SELECT NOTIFIED BODY
├── Check NANDO database for designated bodies
├── Verify scope of designation covers system category
└── Confirm availability and timeline

Step 2: SUBMIT APPLICATION
├── Formal application with system identification
├── Full Annex IV technical documentation
├── QMS documentation per Art. 17
└── Description of intended purpose and deployment context

Step 3: BODY EXAMINES APPLICATION
├── Completeness check (may request supplements)
├── Assess whether QMS route or technical documentation route
└── Agree assessment plan, timeline, and fees

Step 4: ASSESSMENT EXECUTION
├── QMS assessment (Art. 43(3) option 1): examine QMS adequacy + sample technical documentation review
├── OR Technical documentation assessment (Art. 43(3) option 2): full examination of technical documentation + adequacy of design/development controls
└── On-site visit(s) if required

Step 5: CERTIFICATE ISSUANCE
├── Certificate valid for period specified (typically 5 years)
├── Certificate scope and conditions documented
├── Provider notified of surveillance requirements
└── Certificate details reported to notifying authority
```

### Art. 43(3): Choice Between Two Assessment Modes

For systems requiring Track B, the provider may choose between:

| Mode | Focus | Advantage | Consideration |
|------|-------|-----------|---------------|
| QMS Assessment | Examines quality management system as a whole, with technical documentation sampling | Efficient for providers with mature QMS; single certificate covers process | Requires robust, well-documented QMS already in place |
| Technical Documentation Assessment | Examines specific system documentation in full detail | Suitable for single-system providers or new entrants | Must be repeated for each system variant |

### Cost Considerations

Notified body fees are not regulated at EU level and vary by complexity, assessment mode, and body. Indicative cost drivers:

- System complexity and novelty of AI techniques used
- Volume and completeness of submitted documentation
- Number of on-site assessment days required
- Surveillance and certificate maintenance fees (annual)
- Geographic location of the notified body

Art. 62 (measures for small-scale providers and start-ups) directs the AI Office and national authorities to consider proportionate fee structures for SMEs, but fee reductions are discretionary, not guaranteed.

---

## 4. Decision Matrix

### Track Assignment by System Category

| System Category | Assessment Track | Legal Basis | Rationale |
|----------------|-----------------|-------------|-----------|
| Annex III Nr. 1 — Biometric identification | Track B (Annex VII) | Art. 43(1) second subparagraph | Elevated fundamental rights impact; independent verification required |
| Annex III Nr. 2 — Critical infrastructure management | Track A (Annex VI) | Art. 43(2) default | Internal control sufficient under standard risk profile |
| Annex III Nr. 3 — Education and vocational training | Track A (Annex VI) | Art. 43(2) default | Internal control sufficient under standard risk profile |
| Annex III Nr. 4 — Employment, workers management | Track A (Annex VI) | Art. 43(2) default | Internal control sufficient under standard risk profile |
| Annex III Nr. 5 — Essential services access | Track A (Annex VI) | Art. 43(2) default | Internal control sufficient under standard risk profile |
| Annex III Nr. 6 — Law enforcement | Track A (Annex VI) | Art. 43(2) default | Internal control sufficient under standard risk profile |
| Annex III Nr. 7 — Migration, asylum, border control | Track A (Annex VI) | Art. 43(2) default | Internal control sufficient under standard risk profile |
| Annex III Nr. 8 — Administration of justice | Track A (Annex VI) | Art. 43(2) default | Internal control sufficient under standard risk profile |
| Annex I product — existing EU harmonization legislation | Follows existing product legislation | Art. 43(3) | Integrated with sector-specific conformity assessment |
| GPAI model integrated as high-risk component | Track A (unless biometrics) | Art. 43(2) | Provider of downstream system bears assessment responsibility |

### Boundary Analysis: Track A vs. Track B Determination

| Factor | Points to Track A | Points to Track B |
|--------|-------------------|-------------------|
| System function | Non-biometric Annex III use case | Biometric identification (any form) |
| Regulatory context | No existing EU product legislation applies | Annex I legislation with third-party assessment requirement |
| Provider maturity | Established QMS and internal audit capability | Irrelevant — Track B is mandatory when triggered |
| Harmonized standards | Applied voluntarily (strengthens internal case) | May be required by notified body assessment |
| System modification | Minor updates within intended purpose | Irrelevant to track selection (but triggers re-assessment) |

---

## 5. EU Declaration of Conformity (Art. 47)

### Required Content Elements (Annex V)

The EU declaration of conformity (EU-Konformitaetserklaerung) is a formal document through which the provider assumes sole legal responsibility for the system's compliance. It must contain:

| # | Element | Description | Guidance |
|---|---------|-------------|----------|
| 1 | AI system identification | System name, type, version, and any additional unambiguous reference | Use consistent naming across all compliance documents; include software version identifiers |
| 2 | Provider identification | Legal name and registered address of the provider | Must match trade register entry; include contact address for regulatory correspondence |
| 3 | Sole responsibility statement | Explicit declaration that the document is issued under the provider's sole responsibility | Standard formulation; do not dilute with qualifying language |
| 4 | System description | Description of the AI system and unique reference allowing traceability | Should enable a market surveillance authority to identify the exact system version |
| 5 | Intended purpose | Statement of the system's intended purpose as defined by the provider | Must align with technical documentation and instructions for use |
| 6 | Conformity statement | Declaration that the system conforms with Chapter III, Section 2 requirements | Reference specific articles (Art. 8-15) and any delegated or implementing acts applied |
| 7 | Standards and specifications | Harmonized standards or common specifications applied, with references | Full standard reference numbers and publication dates |
| 8 | Notified body details | Name, number, and certificate reference of notified body (if Track B) | Only applicable for systems assessed under Annex VII; omit section for Track A systems |
| 9 | Formal execution | Place, date, and signature of responsible person | Signatory must have legal authority to bind the provider |
| 10 | Supplementary information | Any additional information relevant to compliance | May include derogations, transitional provisions applied, or scope limitations |

### Language and Update Requirements

- **Language:** The declaration must be provided in the official language(s) required by each Member State where the system is placed on the market or put into service. For multi-country deployments, this may require multiple language versions.
- **Currency:** The declaration must be kept up to date throughout the system's market presence. Any change to the system, its intended purpose, or the applicable standards requires review and potential update.
- **Retention:** Retain for at least 10 years after the last unit of the AI system is placed on the market (Art. 47(5)).
- **Availability:** Must be made available to market surveillance authorities upon request, together with the full technical documentation.

---

## 6. CE Marking (Art. 48)

*German: CE-Kennzeichnung*

### Application Rules

CE marking signifies that the AI system has undergone conformity assessment and meets applicable Union requirements. Its application follows specific rules:

| Rule | Requirement | Detail |
|------|-------------|--------|
| Timing | Before placing on market | No system may be marketed or put into service without valid CE marking |
| Visibility | Visible, legible, and indelible | Must be clearly perceptible without special tools or effort |
| Placement | On the AI system itself | Where physical affixing is impractical, on packaging or accompanying documentation |
| Size | Minimum 5 mm height | Standard CE proportions per Regulation (EC) No 765/2008 |
| Digital marking | Permitted for digital-only systems | Art. 48(3) — digital CE marking acceptable when system has no physical form |
| Accuracy | Standard CE proportions | Distortion or modification of the marking is prohibited |

### Interaction with Product-Level CE Marking

Where an AI system is a component of a product that already bears CE marking under existing Union harmonization legislation (e.g., medical devices under MDR, machinery under Machinery Regulation):

- The AI-specific CE marking supplements but does not replace the existing product CE marking
- A single CE marking may cover both the product legislation and AI Act requirements, provided the declaration of conformity references all applicable legislation
- The product's notified body and the AI Act notified body may be different entities; coordination of assessment timelines is the provider's responsibility

### Consequences of Improper Marking

Affixing CE marking without a valid conformity assessment, or affixing misleading markings, constitutes a direct violation subject to administrative fines under Art. 99(4) — up to EUR 7.5 million or 1% of global annual turnover for undertakings.

---

## 7. Timeline and Sequencing

### Pre-Market Gate

The conformity assessment must be fully completed before any of the following market actions:

- Placing on the market (making available on the Union market for the first time)
- Putting into service (first use for intended purpose)
- Making available on the market (any supply for distribution or use)

There is no provisional or conditional market access. A system that has not completed assessment may not be deployed even in pilot or limited-release configurations, unless within an Art. 57 regulatory sandbox.

### Re-Assessment Triggers

| Trigger | Legal Basis | Scope of New Assessment |
|---------|------------|------------------------|
| Substantial modification | Art. 43(4) | Full new conformity assessment required |
| Change of intended purpose | Art. 43(4), read with Art. 3(12) | Full new conformity assessment — change of purpose may reclassify the system |
| New harmonized standards published | Art. 43(4) | Assessment against updated standards; scope depends on materiality of standard changes |
| Provider role transfer (Art. 25) | Art. 25(1)(b) | New provider (quasi-provider) must perform own conformity assessment |

### Substantial Modification Analysis

Art. 43(4) ties re-assessment to "substantial modification" — a change not foreseen by the provider at the time of the initial conformity assessment that affects the system's compliance with requirements or alters the intended purpose. Key indicators:

| Indicator | Likely Substantial | Likely Not Substantial |
|-----------|-------------------|----------------------|
| Retraining on fundamentally different data distribution | Yes — alters performance characteristics | — |
| Bug fix within existing intended purpose | — | No — does not alter compliance posture |
| Extension to new use case or sector | Yes — may change classification entirely | — |
| Hyperparameter tuning within validated ranges | — | No — within documented design envelope |
| Architecture change (e.g., model swap) | Yes — alters technical basis of compliance evidence | — |
| UI/UX changes without logic modification | — | No — does not affect core system behavior |

Cross-reference: [references/high-risk-provider-obligations.md] for Art. 25(1)(b) quasi-provider obligations when modifications are performed by a party other than the original provider.

### Documentation Retention

| Document | Retention Period | Legal Basis |
|----------|-----------------|-------------|
| Conformity assessment records | 10 years after last market placement | Art. 18(1) |
| EU declaration of conformity | 10 years after last market placement | Art. 47(5) |
| Technical documentation | 10 years after last market placement | Art. 18(1) |
| Notified body certificate | Duration of certificate validity + 10 years | Art. 18(1) |
| QMS records referenced in assessment | 10 years after last market placement | Art. 18(1) |

---

## 8. Practical Guidance

### Common Pitfalls

| # | Pitfall | Why It Occurs | Mitigation |
|---|---------|---------------|------------|
| 1 | Starting assessment before technical documentation is complete | Schedule pressure; misunderstanding of dependency chain | Establish documentation readiness gate before assessment kickoff |
| 2 | Insufficient risk management maturity | Risk management treated as one-time exercise rather than continuous system | Verify Art. 9 risk management system has completed at least one full cycle before assessment |
| 3 | Treating assessment as checkbox exercise | Compliance-minimization mindset; lack of quality culture | Frame assessment as internal quality assurance, not external burden |
| 4 | Forgetting post-market monitoring readiness | Monitoring system not yet operational at time of assessment | Include Art. 72 monitoring plan operability in assessment scope |
| 5 | Declaration of conformity with incomplete content | Template used without adapting to specific system | Validate declaration against all 10 Annex V elements before signing |
| 6 | Neglecting language requirements for declaration | Assumption that English-only is sufficient | Identify target Member States early; prepare translations proactively |
| 7 | Conflating product CE marking with AI CE marking | Assumption that existing product compliance covers AI requirements | Verify AI Act requirements are separately addressed even if product already has CE marking |
| 8 | No procedure for substantial modification assessment | Changes deployed without evaluating re-assessment obligation | Establish change control process with conformity assessment impact screening |

### Internal Control Quality Checklist

Before finalizing the Track A assessment, verify:

| # | Check Item | Status |
|---|-----------|--------|
| 1 | QMS manual is current and covers all Art. 17 elements | _ |
| 2 | Technical documentation covers all 8 Annex IV sections | _ |
| 3 | Risk management system has been through at least one complete cycle (identify-assess-mitigate-test-monitor) | _ |
| 4 | Data governance measures per Art. 10 are documented and evidenced | _ |
| 5 | Human oversight measures per Art. 14 are designed, documented, and tested | _ |
| 6 | Accuracy, robustness, and cybersecurity levels per Art. 15 are measured and documented | _ |
| 7 | Post-market monitoring plan per Art. 72 is finalized and infrastructure is operational | _ |
| 8 | Logging capabilities per Art. 12 are implemented and verified | _ |
| 9 | Instructions for use per Art. 13 are complete and provided to deployers | _ |
| 10 | All non-conformities found during assessment have documented corrective actions with closure evidence | _ |

### Finding Notified Bodies

- **NANDO database:** The Commission's New Approach Notified and Designated Organisations database lists all notified bodies by legislative area. Once AI Act designations begin, NANDO will include bodies notified under Art. 28-36.
- **Member State notifications:** Each Member State designates a notifying authority (Art. 28) responsible for assessing and notifying conformity assessment bodies.
- **Selection criteria:** Beyond formal designation, evaluate the body's experience with AI systems, responsiveness, geographic reach, and assessment timeline availability.
- **Timing consideration:** The pool of notified bodies for AI Act assessments is expected to be limited initially. Early engagement is advisable for providers requiring Track B assessment.

### SME Considerations

Art. 62 directs national authorities and the AI Office to account for the interests and needs of small-scale providers and start-ups:

| Measure | Source | Practical Impact |
|---------|--------|-----------------|
| Proportionate fees for conformity assessment | Art. 62(1) | Reduced notified body fees where Member States implement fee guidance |
| Priority access to AI regulatory sandboxes | Art. 57 + Art. 62 | Sandbox testing may partially substitute for standalone assessment preparation |
| Simplified documentation for SMEs | Commission implementing acts (expected) | Potential for streamlined Annex IV templates — monitor AI Office publications |
| AI Office guidance materials | Art. 62(2) | Dedicated SME compliance guidance and templates |

Cross-references: [references/compliance-roadmap.md] for timeline integration, [references/organizational-measures.md] for documentation retention details
