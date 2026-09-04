---
name: eu-ai-act-high-risk-implementation-readiness
description: Assess and operationalize implementation readiness for high-risk AI systems under the EU AI Act Annex III, including provider and deployer obligations, conformity assessment, post-market monitoring, and EU database registration. Use when users say things like “we classified this as high-risk, what now?”, “build an EU AI Act readiness plan”, “assess our Annex III compliance gaps”, “what do providers/deployers of high-risk AI need to implement?”, “prepare for conformity assessment”, or “create a high-risk AI implementation roadmap.”
---

# EU AI Act High-Risk Implementation Readiness

Use this skill when a system has already been classified as potentially high-risk under the EU AI Act and the user now needs to understand what must actually be implemented, documented, assigned, tested, and governed.

If the system has **not** yet been classified, use the **EU AI Act System Classifier** first.

This skill is designed as a **practical readiness assessment and implementation navigator** for:
- **Providers** of high-risk AI systems
- **Deployers** of high-risk AI systems
- Internal legal, compliance, product, engineering, security, risk, procurement, and management teams
- Especially **DACH-based organizations** preparing for real operational compliance work before the high-risk obligations apply

> Important timing note: Annex III high-risk obligations apply from **2 December 2027** and Annex I product-integrated high-risk obligations from **2 August 2028**. The Digital Omnibus simplification package amending the EU AI Act was adopted on 8 July 2026 and published in the Official Journal on 24 July 2026 as Regulation (EU) 2026/1744, entering into force on 27 July 2026; it deferred these dates from 2 August 2026 and 2 August 2027 respectively. Article 50 transparency obligations and the start of Commission GPAI enforcement powers were not deferred and continue to apply from 2 August 2026. Build against these enacted dates. The substance also moved in places: the same regulation amended Art. 10 and inserted Art. 4a. Article 4a(1) creates an exceptional bias-detection and correction basis for high-risk providers, subject to six safeguards. Article 4a(2) separately covers providers and deployers of other AI systems and models and deployers of high-risk AI systems, but only where processing is strictly necessary for biases likely to affect health or safety, negatively affect fundamental rights, or cause prohibited discrimination, and all paragraph 1 safeguards are applied; it creates no duty to conduct bias detection or correction. The regulation also amended Art. 11(1) (simplified technical documentation for SMEs and SMCs, which notified bodies must accept), Art. 17(2) and Art. 63(1) (quality-management proportionality and simplification), Art. 25(2) and (4) (provider-switch cooperation), Art. 43(3) (conformity-assessment routing, and sectoral notified bodies must apply for designation by 28 January 2028), Annex VIII Section B points 7 and 9 deleted (Art. 49(2) itself is unamended; the deletion reduces the information submitted for Art. 6(3) registrations), and Art. 72(3) (post-market monitoring template replaced by Commission guidance due 2 September 2027).

---

## What this skill does

This skill helps the user answer five practical questions:

1. **Are we really in scope as high-risk?**
2. **What obligations apply to us as provider, deployer, or both?**
3. **What evidence and documentation should already exist?**
4. **How ready are we today - RED, AMBER, or GREEN?**
5. **What do we need to do next, in what order, and who should own it?**

It covers operational readiness across the main Annex III lifecycle obligations, especially:
- Art. 6 and the Art. 6(3) exception context
- Arts. 9–15 provider controls
- Arts. 16–17 provider governance and QMS framing
- Art. 26 deployer obligations
- Art. 43 conformity assessment pathways
- Art. 49 EU database registration
- Art. 72 post-market monitoring

---

## When to use this skill

Use this skill when the user asks things like:
- “We know the system is high-risk. What do we need to implement now?”
- “Can you assess our readiness for the EU AI Act?”
- “What evidence do we need for Annex III high-risk compliance?”
- “Create a gap analysis and implementation roadmap for our AI system.”
- “What do providers of high-risk AI need beyond classification?”
- “What do deployers need to do under Art. 26?”
- “Do we need a notified body or can we self-assess?”
- “How do we prepare technical documentation and QMS for a high-risk AI system?”

---

## Quick intake questions

Start by collecting concise answers to these questions. If the user does not know, mark assumptions clearly.

### A. Scope and role
1. What does the AI system do in practice?
2. Which Annex III category is believed to apply?
3. Has the system already been classified using a separate high-risk classifier?
4. Is there any argument that the **Art. 6(3) exception** applies, meaning the system may fall within Annex III wording but does **not** materially influence the decision-making in a way that makes it high-risk?
5. Are you acting as **provider**, **deployer**, or both?
6. Is the system already on the market / in service, in pilot phase, or still in development?

### B. Organizational context
7. Which legal entity owns the system and which teams operate it?
8. In which countries will the system be placed on the market or used?
9. Is the use case in a regulated sector such as employment, education, essential services, law enforcement, migration, justice, or biometric identification?
10. Is this a standalone AI system, a component embedded in software, or integrated into a broader product/service?

### C. Technical and control environment
11. What data is used for training, validation, testing, and live operation?
12. What logs are currently generated automatically?
13. What human review or override exists today?
14. What testing exists for accuracy, robustness, bias, and security?
15. Is there already technical documentation, model documentation, validation documentation, or a QMS in place?

### D. Governance and evidence
16. Is there a named owner for compliance readiness?
17. Is there a formal risk management process for the AI system?
18. Are there supplier/vendor dependencies, including GPAI or third-party model providers?
19. Is post-market monitoring already planned?
20. Is management expecting a simple legal memo or an implementation-grade roadmap with evidence requirements?

---

## Decision tree: start here

### Step 1 - Confirm classification posture
- If the system has **not yet been classified**, stop and direct the user to the **EU AI Act System Classifier** first.
- If the system appears to match Annex III but there may be a credible **Art. 6(3) exception** argument, do **not** proceed as if high-risk is settled. Flag the issue and recommend a focused classification memo before readiness work continues.
- If the system is reasonably treated as high-risk, continue.

### Step 2 - Determine actor posture
- If the organization **develops / places on the market / puts into service under its own name**, assess **provider obligations**.
- If the organization **uses** the system in its operations, assess **deployer obligations**.
- If it does both, run both tracks and separate deliverables clearly.

### Step 3 - Determine assessment mode
Choose one of three modes:
- **Rapid triage** - fast RED/AMBER/GREEN scan across all obligation areas
- **Evidence-based readiness assessment** - assess each area against actual documents, processes, owners, and controls
- **Implementation roadmap** - turn identified gaps into a sequenced action plan with owners, dependencies, and deliverables

### Step 4 - Determine conformity assessment path
- For **Annex III point 1**, Annex VI or Annex VII is available only where all relevant harmonised standards or common specifications are applied; otherwise Annex VII applies.
- For **Annex III points 2 to 8**, Article 43(2) requires Annex VI internal control with no notified body.
- For **Annex I Section A** products, follow the sectoral conformity-assessment route under Article 43(3). For **Annex I Section B** products, account for the limited AI Act application stated in Article 2(2).
- If unclear, flag this early because it changes evidence expectations and timelines

---

## Core workflow

### 1. Frame the scope precisely
Produce a short scoping statement covering:
- system name / working label
- practical function
- likely Annex III category
- provider/deployer role split
- lifecycle stage
- jurisdictions
- whether Art. 6(3) remains open or has been ruled out

**Output at this stage:** one-paragraph scope statement + assumption list.

---

### 2. Assess readiness across the 12 obligation areas
For each area below, evaluate:
- **What the AI Act requires**
- **What evidence should exist**
- **Readiness status:** RED / AMBER / GREEN
- **Key gaps**
- **Next actions**
- **Common pitfalls**

#### Area 1 - Risk management system (Art. 9)
Ask:
- Is there a defined AI-specific risk management process across the lifecycle?
- Are known and reasonably foreseeable risks identified and documented?
- Are risk controls tied to testing, design, and residual risk evaluation?
- Are changes, incidents, and monitoring findings fed back into the system?

Evidence examples:
- risk management procedure
- system risk register
- hazard / harm analysis
- control mapping
- residual risk sign-off
- validation and test evidence

Use deep dive: `references/risk-management-system.md`

#### Area 2 - Data governance and data quality (Art. 10)
Ask:
- What datasets were used for training, validation, and testing?
- Are relevance, representativeness, completeness, and error considerations documented?
- Was bias examination performed and recorded?
- Is data provenance and acquisition legality documented?

Evidence examples:
- dataset inventory
- data specification sheets
- bias assessment
- sampling rationale
- data cleaning and labeling procedures
- validation dataset design notes

Use deep dive: `references/data-governance.md`

#### Area 3 - Technical documentation (Art. 11 + Annex IV)
Ask:
- Could the organization produce a defensible Annex IV-style technical file today?
- Is system design, development method, intended purpose, architecture, metrics, risk controls, and change history documented?
- Are monitoring capabilities and limitations explained clearly enough for review?

Evidence examples:
- technical file / Annex IV pack
- architecture diagrams
- model cards / system cards
- development and validation methodology
- version/change log
- limitations and assumptions documentation

Use deep dive: `references/technical-documentation.md`

#### Area 4 - Record-keeping and logging (Art. 12)
Ask:
- What logs are created automatically?
- Do logs support traceability for operation, incidents, human intervention, and review?
- Is retention aligned with legal and operational needs?
- Can logs support investigations and post-market monitoring?

Evidence examples:
- logging specification
- event taxonomy
- retention schedule
- access controls for logs
- sample audit trail outputs

#### Area 5 - Transparency and information to deployers (Art. 13)
Ask:
- Are there instructions for use?
- Are intended purpose, operating conditions, known limitations, expected accuracy, oversight assumptions, and security conditions explained?
- Would a deployer know when the system should not be used?

Evidence examples:
- instructions for use
- deployment manual
- limitation statements
- accuracy/robustness documentation
- user-facing warnings and assumptions

#### Area 6 - Human oversight (Art. 14)
Ask:
- Who is expected to oversee the system?
- Can they understand outputs well enough to intervene meaningfully?
- Is there a stop, override, or escalation mechanism?
- Is oversight designed into the process rather than assumed abstractly?

Evidence examples:
- oversight design specification
- SOPs for reviewers/operators
- override or manual fallback procedures
- training materials
- escalation matrix

#### Area 7 - Accuracy, robustness, and cybersecurity (Art. 15)
Ask:
- What performance thresholds are defined?
- How was robustness tested under foreseeable operating conditions?
- What error handling and fail-safe logic exists?
- What cybersecurity risks, including adversarial manipulation, have been considered?

Evidence examples:
- performance benchmarks
- validation reports
- robustness/stress testing
- security testing results
- vulnerability management records

#### Area 8 - Quality management system (Art. 17)
Ask:
- Is there a documented QMS covering the AI lifecycle?
- Are design, development, testing, change management, supplier control, incident handling, and authority communication governed?
- Are roles and records assigned in a way that can survive audit or conformity review?

Evidence examples:
- QMS manual
- policies and procedures
- role matrix / RACI
- change control procedure
- supplier management records
- CAPA / incident process

Use deep dive: `references/qms-requirements.md`

#### Area 9 - Deployer obligations (Art. 26)
Ask:
- Is the system being used in accordance with the provider’s instructions?
- Are human oversight responsibilities assigned?
- Is input data checked for relevance and suitability?
- Are records maintained during use?
- Are affected persons informed where required?
- Is a **fundamental rights impact assessment** required under Art. 27(1): is the deployer a public-law body or private public-service entity, or is the system an Annex III point 5(b) creditworthiness/credit-scoring or point 5(c) life/health-insurance system (where every deployer owes the FRIA)? Annex III point 2 is excepted.

Evidence examples:
- deployer SOPs
- user governance record
- oversight assignments
- operational monitoring logs
- notice/information materials
- FRIA documentation where relevant

Use deep dive: `references/deployer-obligations.md`

#### Area 10 - Conformity assessment path (Art. 43)
Ask:
- Is the system likely on the Annex VI internal control route?
- Is third-party assessment / notified body involvement required?
- What evidence package would be expected under the chosen route?
- Who owns the conformity assessment timeline?

Evidence examples:
- classification memo
- conformity assessment path memo
- Annex VI checklist
- notified body engagement plan if needed

Use deep dive: `references/conformity-assessment.md`

#### Area 11 - Post-market monitoring (Art. 72)
Ask:
- Is there a documented, proportionate post-market monitoring plan?
- What data will be collected from live operation?
- How are incidents, malfunctions, and performance drift analyzed?
- How do findings feed back into risk management, documentation, and controls?

Evidence examples:
- post-market monitoring plan
- KPI/KRI definitions
- incident intake workflow
- review cadence and reporting structure

#### Area 12 - EU database registration (Art. 49)
Ask:
- Who is responsible for registration before placing on the market or putting into service?
- Is the required registration data known and assembled?
- Is registration integrated into launch governance?

Evidence examples:
- registration readiness checklist
- responsibility assignment
- pre-launch gate / approval workflow

---

### 3. Apply the readiness scoring model
Use this scoring consistently for every area.

#### RED - Not started / materially deficient
Use RED where one or more of the following is true:
- no documented process exists
- no owner is assigned
- evidence is missing or purely informal
- controls exist in practice but are not systematic, documented, or reviewable
- the organization could not defend the area in a conformity assessment or authority inquiry

#### AMBER - Partially addressed / not yet defensible end-to-end
Use AMBER where:
- some controls exist but are fragmented
- evidence exists but is incomplete, inconsistent, outdated, or not AI-specific
- roles are partly assigned but not embedded operationally
- testing or monitoring exists but is not tied back to governance and risk decisions

#### GREEN - Substantially ready
Use GREEN where:
- the process is defined, operational, and documented
- evidence is current and reviewable
- ownership is assigned
- the area is integrated into lifecycle governance
- there are still improvement opportunities, but the organization is broadly defensible

Do **not** mark GREEN purely because “the team is already careful” or “similar controls exist somewhere else.”

---

### 4. Identify critical dependencies and blockers
After scoring, identify blockers such as:
- unresolved Art. 6(3) scope question
- unclear provider vs deployer role split
- lack of named accountable owner
- no technical documentation baseline
- no AI-specific risk register
- insufficient logging or traceability
- no oversight design
- reliance on a third-party model/vendor with weak documentation support
- missing QMS backbone
- unclear conformity assessment path

Group blockers into:
- **Legal/classification blockers**
- **Process/governance blockers**
- **Technical/control blockers**
- **Evidence/documentation blockers**

---

### 5. Build a practical implementation roadmap
Translate gaps into a sequenced roadmap.

Recommended workstreams:
1. **Scope and accountability**
2. **Risk management**
3. **Data governance**
4. **Documentation and logging**
5. **Human oversight and operations**
6. **Testing, robustness, and cybersecurity**
7. **QMS and authority-facing readiness**
8. **Deployer operating model**
9. **Conformity assessment and registration**
10. **Post-market monitoring**

For each workstream define:
- objective
- key deliverables
- owner
- supporting teams
- dependencies
- target timing
- residual decision points

Use templates in `references/templates.md`.

---

### 6. Tailor for DACH implementation reality
Where relevant, add practical DACH-specific points such as:
- likely interaction with German market surveillance or sector regulators
- BNetzA / BSI / sector authority interfaces depending on use case
- procurement and documentation expectations in German enterprises
- works council implications where human oversight affects employees or AI is used in HR contexts
- need for German-language operational materials, training, or works agreements in practice

Use: `references/dach-specific.md`

---

## Practical shortcuts and pitfalls to flag

Always call out shortcuts that look attractive but are weak in a real assessment.

Common examples:
- “We already have ISO processes, so we must be compliant.”
- “We have general model docs, so that counts as Annex IV technical documentation.”
- “Humans review sometimes” without defining who, when, with what authority, and based on what criteria.
- “Security reviewed the app” without AI-specific robustness and adversarial considerations.
- “We keep logs” without confirming traceability, access, retention, and useful event design.
- “The vendor handles compliance” without obtaining evidence and role clarity.
- “We’ll write the documents later” when core controls are not yet actually operating.

---

## Output format

Unless the user asks for something else, structure the final deliverable like this:

### 1. Executive summary
- in-scope system and role
- high-level conclusion on readiness
- top 3–5 critical gaps
- immediate next actions

### 2. Scope and assumptions
- system description
- likely Annex III category
- provider/deployer split
- Art. 6(3) position if relevant
- assumptions / unknowns

### 3. Readiness scorecard
For each of the 12 areas:
- requirement summary
- expected evidence
- status: RED / AMBER / GREEN
- rationale
- immediate next step

### 4. Priority gap analysis
- critical gaps
- why they matter
- dependencies and sequencing

### 5. Implementation roadmap
- 30 / 60 / 90 day view, or phased workstream plan
- owners and dependencies

### 6. DACH-specific notes
- regulator / authority / works council / operational localization issues

### 7. Key caveats
- legal uncertainties
- evidence limitations
- any items needing specialist legal or technical validation

---

## Suggested response patterns

### If the user wants a quick assessment
Provide:
- brief scope statement
- 12-area RED/AMBER/GREEN scorecard
- top 5 actions
- biggest conformity assessment risk

### If the user wants implementation help
Provide:
- scorecard
- gap analysis
- detailed roadmap
- document list to create
- owner suggestions by function

### If the user is a deployer only
Focus more heavily on:
- Art. 26 usage controls
- provider instruction adherence
- oversight assignment
- monitoring and record-keeping in operation
- FRIA / affected-person information where relevant

### If the user is a provider with a mature quality function
Focus more heavily on:
- evidence sufficiency
- AI-specific adaptations to existing QMS
- Annex IV technical documentation completeness
- risk management lifecycle integration
- conformity assessment readiness

---

## Recommended reference map

Use these deep dives selectively rather than overloading the main response:
- `references/risk-management-system.md`
- `references/data-governance.md`
- `references/technical-documentation.md`
- `references/qms-requirements.md`
- `references/conformity-assessment.md`
- `references/deployer-obligations.md`
- `references/dach-specific.md`
- `references/templates.md`

---

## Legacy systems: the grace period moved (Article 111(2))

Regulation (EU) 2026/1744 replaced Article 111(2) on 27 July 2026, and this matters
directly for question 6 of the intake above.

The cut-off is no longer the fixed date of 2 August 2026. It now tracks the date of
application of Chapter III under Article 113, meaning **2 December 2027** for Annex III
systems and **2 August 2028** for Annex I systems. A high-risk system already placed on the
market or put into service before its applicable date falls outside the requirements unless
it is subject to significant changes in its design from that date onward.

Two qualifications that decide most real cases:

- **The grace period is assessed for systems individually placed on the market or put into
  service before the applicable date.** Later units of the same type or model that are first
  supplied after that date are not grandfathered merely because an earlier unit was supplied.
- **Public-authority deployments have their own hard stop.** Providers and deployers of
  high-risk systems intended for use by public authorities must comply by **2 August 2030**
  regardless, and that date did not move.

Practical readiness consequence: record the placement-on-market or putting-into-service
date for each system or unit relied upon, together with its design baseline. For an existing
system, also ask whether a significant design change will occur from the applicable date.

## Disclaimer

This skill provides a practical implementation and readiness framework for the EU AI Act, especially for Annex III high-risk systems. It is not a substitute for formal legal advice, sector-specific regulatory advice, technical assurance, cybersecurity testing, or notified-body input where required.

The AI Act contains cross-references, implementing acts, harmonized standards, and evolving guidance that may change how obligations are interpreted in practice. Where classification is uncertain, where the Art. 6(3) exception may apply, where biometric or sector-specific issues are involved, or where conformity assessment route selection is unclear, the user should validate the position with qualified counsel and relevant technical stakeholders.

---

## What good looks like

A strong outcome from this skill is not just “a compliance memo.” It is:
- a clear scope position
- a defensible readiness score by obligation area
- a concrete evidence list
- a prioritized implementation roadmap
- named ownership
- a practical path toward conformity assessment, deployment readiness, and ongoing monitoring

That is the difference between knowing you are high-risk and being operationally prepared for it.
