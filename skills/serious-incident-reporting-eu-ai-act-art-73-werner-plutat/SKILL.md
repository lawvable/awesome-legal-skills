---
name: serious-incident-reporting
description: Serious Incident Reporting (SIR) for high-risk AI systems under Article 73 EU AI Act (Regulation (EU) 2024/1689, KI-Verordnung). Assess, qualify, draft, and submit Article 73 Serious Incident Reporting notifications across the four Art. 3(49) harm categories: death or serious damage to health, critical infrastructure disruption, breach of fundamental rights under Union law, and serious property or environmental damage. Covers Art. 73 deadline buckets (2/10/15 days), market surveillance authority notification, deployer duties under Art. 26(5), cross-regulation mapping with GDPR Art. 33/34 breach notification, NIS2 Art. 23 incident reporting, DORA Art. 19 ICT incident, and MDR vigilance, corrective measures, root-cause analysis, and DACH routing through German market surveillance (BNetzA, BaFin, BSI, BfArM, KBA). Use when asked to evaluate whether an AI incident is reportable, draft a Serious Incident Reporting notification under Art. 73, build an AI incident response playbook, handle an AI failure, AI bias incident, AI discrimination incident or automated decision failure, identify the right market surveillance authority, manage 2/10/15-day Article 73 deadlines, or handle a schwerwiegender Vorfall under the EU AI Act.
---

# Serious Incident Reporting under the EU AI Act (Article 73)

This skill helps assess whether an event involving an AI system triggers serious-incident reporting duties under **Article 73 EU AI Act**, and then turns that legal analysis into a practical response plan, draft notification, and internal action list.

It is designed for providers, deployers, legal/compliance teams, product leads, and incident-response teams that need a usable process rather than abstract commentary.

## When to Use This Skill

Use this skill when the user wants to:

- assess whether an AI-related event qualifies as a **serious incident** under the EU AI Act
- decide whether a system is in scope because it is actually **high-risk**
- determine **when** reporting must happen and under which deadline bucket
- identify the **market surveillance authority** to notify
- prepare a practical **Article 73 report**
- understand **deployer notification duties** under **Article 26(5)**
- coordinate Article 73 with **GDPR**, **NIS2**, **medical device**, **machinery**, or **product safety** reporting
- create an internal **incident playbook**, escalation matrix, or management briefing

## Quick Reality Check Before You Start

This workflow only applies if the system is actually a **high-risk AI system** under the EU AI Act.

That means:

1. it is high-risk under **Article 6(1)** because it is a safety component of an Annex I product or is itself such a product subject to third-party conformity assessment; **or**
2. it falls under **Annex III** and is not carved out by the **Article 6(3)** exception.

If the system is only assumed to be high-risk because it sits near a regulated workflow, stop and confirm classification first. If **Article 6(3)** plausibly applies, incident reporting under Article 73 may not be triggered because the system is not in-scope as high-risk in the first place.

## What This Skill Produces

Depending on the request, produce some or all of the following:

- a **qualification memo**: in scope / out of scope / uncertain
- a **deadline assessment**: 2-day / 10-day / 15-day / follow-up reporting
- a **recipient map** by Member State
- a draft **Article 73 incident report**
- a **cross-regulation notification matrix**
- an **internal action checklist** for legal, product, security, and management
- a short **management briefing** in plain business language

---

## Quick Questions to Ask First

Keep the first intake short and practical. Ask only what is needed to classify and triage.

### Minimum Intake Questions

1. **What AI system is involved?**
   - product name
   - version/build
   - provider legal entity
   - intended purpose

2. **Why do you think it is high-risk?**
   - Annex I safety component/product?
   - Annex III use case?
   - any prior classification memo?
   - any **Article 6(3)** non-high-risk assessment?

3. **What happened?**
   - date/time discovered
   - date/time incident occurred if different
   - what the system did or failed to do
   - causal chain as currently understood

4. **What harm occurred or could have occurred?**
   - death
   - serious harm to health
   - serious property damage
   - serious environmental damage
   - serious and irreversible disruption of critical infrastructure management

5. **Where did the incident occur?**
   - Member State(s)
   - customer/deployer location
   - cross-border impact?

6. **Who identified it first?**
   - provider
   - deployer
   - distributor/importer
   - end user / affected person
   - authority / media / whistleblower

7. **What has already been done?**
   - system suspended?
   - users/deployers informed?
   - rollback / kill switch / access restriction?
   - internal investigation started?

8. **Any overlapping regimes?**
   - personal data breach?
   - NIS2/cyber incident?
   - medical device or in vitro diagnostic?
   - machinery / product safety?
   - labour / workplace impact?

### If Time Is Extremely Short

Ask only these four:

- Is the system definitely **high-risk**?
- Did the event cause or plausibly contribute to **death or serious harm**?
- In which **Member State** did it occur?
- When did the provider or deployer first become **aware**?

---

## Core Workflow

Follow this sequence.

### Step 1 - Confirm Scope: Is the System Actually High-Risk?

Do not jump straight to reporting.

#### 1A. High-risk gateway

Check whether the system is high-risk under **Article 6**:

- **Article 6(1)**: annexed sector product / safety-component route
- **Article 6(2)**: **Annex III** route
- **Article 6(3)**: possible exception for certain Annex III systems that do not pose a significant risk of harm and do not materially influence decision-making, except profiling cases

#### 1B. Decision

- **Yes, clearly high-risk** → continue to Step 2
- **No, clearly not high-risk** → Article 73 does not apply; still assess other regimes
- **Unclear** → state that classification uncertainty itself is material and proceed with a precautionary triage while classification is verified urgently

#### Practical instruction

If the user cannot produce a prior classification memo, ask for:

- intended purpose
- user group
- sector/context
- whether outputs materially influence decisions about persons or safety
- whether the system is a safety component or regulated product

If there is genuine ambiguity and potential severe harm, recommend a conservative incident-response posture while classification is clarified.

For deeper logic, use `references/incident-qualification.md`.

---

### Step 2 - Qualify the Event: Is It a "Serious Incident"?

Under **Article 3(49)**, this is the legal thresholding step.

For practical purposes, treat the event as a serious incident if it directly or indirectly led, might have led, or plausibly contributed to one of the following:

- **death of a person**
- **serious damage to the health of a person**
- **serious and irreversible disruption of the management and operation of critical infrastructure**
- breach of obligations under Union law intended to protect **fundamental rights**, where the breach is serious in effect
- for operational triage, also treat severe damage to **property** or the **environment** as requiring immediate legal review and likely notification planning where the facts align with the statutory serious-harm threshold or adjacent sector rules

#### Decision Tree

1. Did the event involve a high-risk AI system in operation, output, failure, misuse, or foreseeable misuse?
   - if **no** → not Article 73
   - if **yes** → continue

2. Is there actual harm, or a sufficiently evidenced near-term harm scenario, connected to the system?
   - if **no** → record as non-serious incident / post-market issue unless facts change
   - if **yes** → continue

3. Does the harm fall into a severe category?
   - death
   - serious health harm
   - serious fundamental-rights impact
   - critical-infrastructure disruption
   - potentially equivalent severe sectoral harm requiring parallel reporting

4. Is there a causal link or at least a **reasonable likelihood** of one?
   - if **yes** → reportable timeline starts running
   - if **uncertain but plausible** → treat as escalation case; preserve evidence and decide quickly
   - if **clearly no** → document why and monitor

#### Practical rule

Do not wait for perfect forensic proof. **Article 73(2)** is triggered once the provider has established a causal link **or the reasonable likelihood of such a link**.

Use `references/incident-qualification.md` for examples and edge cases.

---

### Step 3 - Put the Incident Into the Correct Deadline Bucket

Once there is a causal link or reasonable likelihood, determine the reporting deadline.

| Scenario | Deadline | Article | Trigger |
|----------|----------|---------|---------|
| Standard serious incident | Immediately, max **15 days** | Art. 73(2) | Causal link or reasonable likelihood established |
| Widespread infringement or Art. 3(49)(b) type | Immediately, max **2 days** | Art. 73(3) | Awareness of incident |
| Death of a person | Immediately, max **10 days** | Art. 73(4) | Causal relationship established or suspected |

#### Standard rule - Article 73(2)

- report **immediately** after establishing causal link or reasonable likelihood
- and **no later than 15 days** after the provider or, where applicable, the deployer became aware of the serious incident

#### Accelerated rule - Article 73(3)

If there is:

- a **widespread infringement**, or
- a serious incident of the type covered by **Article 3(49)(b)**

then report:

- **immediately**, and
- **no later than 2 days** after awareness

#### Death rule - Article 73(4)

If the incident involves **death of a person**:

- report immediately once causal relationship is established or even **suspected**
- and **no later than 10 days** after awareness

#### Incomplete initial report - Article 73(5)

If facts are still developing:

- send an **initial incomplete report** on time
- follow with a more complete report as soon as possible

#### Follow-up investigation - Article 73(6)

After reporting:

- investigate without delay
- conduct risk assessment
- take corrective action
- cooperate with authorities
- avoid altering the system in a way that could compromise causal analysis before informing authorities

Use `references/reporting-requirements.md` for the deadline logic.

---

### Step 4 - Identify the Right Recipient Authority

The baseline rule is simple:

- notify the **market surveillance authority of the Member State where the incident occurred**

But implementation is operationally messy, especially in cross-border or sector-specific cases.

#### 4A. Core recipient logic

- incident in one Member State → notify that State's market surveillance authority
- incident in multiple Member States → prepare a lead-state map and parallel notifications where appropriate
- uncertain location → identify where harm materialised, where the system was deployed, and where the affected persons or infrastructure were located

#### 4B. Germany

For Germany, use **Bundesnetzagentur (BNetzA)** as the primary practical entry point for AI Act market-surveillance routing, while checking whether a **sector-specific competent authority** also needs involvement.

Common examples:

- medical device context → national medical device authority chain
- machinery / product safety context → sector product-safety channel may also matter
- critical infrastructure or cyber context → NIS2 / BSI or sector-specific channels may run in parallel
- employment context → add labour, works council, and data-protection analysis

#### 4C. Article 62 reference

**Article 62** ("Channels for reporting breaches and protection of reporting persons") requires Member States to establish channels for reporting breaches. In practice, these channels also serve as entry points for incident-related questions and operational guidance. The AI Office is expected to provide templates and information tooling. Article 62 is not itself the incident reporting rule, but it matters operationally for identifying the right contact point.

Use `references/dach-specific.md` and `references/reporting-requirements.md`.

---

### Step 5 - Build the Reporting Package

At minimum, assemble the package around the fields authorities will expect, even if the first report is incomplete.

#### Essential content

1. **Provider identification**
   - legal entity
   - address / contact details
   - authorised representative if relevant
   - key incident contact person

2. **AI system identification**
   - name/model/version
   - CE / conformity / registration identifiers where relevant
   - high-risk category and legal basis
   - intended purpose and deployment setting

3. **Incident facts**
   - date/time of incident
   - date/time of awareness
   - location / Member State
   - affected deployer/customer
   - factual narrative of what happened

4. **Impact and affected parties**
   - number and type of persons affected
   - nature and severity of harm
   - whether harm is ongoing
   - critical infrastructure / public service implications
   - whether workers or vulnerable persons were affected

5. **Causation assessment**
   - confirmed causal link / reasonable likelihood / under investigation
   - known failure mode or suspected root cause
   - whether incident involved foreseeable misuse, input data issue, model drift, human oversight failure, or integration failure

6. **Containment and corrective measures**
   - system suspension or rollback
   - warnings to deployers
   - patch / hotfix / model disablement
   - human review measures
   - customer communication

7. **Evidence preservation**
   - logs retained
   - screenshots / prompts / outputs preserved
   - configuration and model version frozen
   - relevant third-party components identified

8. **Parallel notifications**
   - GDPR / NIS2 / MDR / product safety / insurer / contractual notices sent or pending

9. **Planned follow-up**
   - investigation owner
   - next reporting milestone
   - expected timing for supplementary report

Use `references/templates.md` for a practical report template.

---

### Step 6 - Handle Deployer Duties Under Article 26(5)

If the user is a **deployer**, or if the provider learned of the issue through a deployer, apply **Article 26(5)** explicitly.

Under Article 26(5), deployers of high-risk AI systems must:

- monitor operation based on instructions for use
- where they believe use may result in a risk, inform the provider/distributor and relevant market-surveillance authority without undue delay and suspend use
- where they identify a **serious incident**, **immediately inform first the provider, and then the importer or distributor and the relevant market surveillance authorities**
- if unable to reach the provider, Article 73 applies **mutatis mutandis**

#### Practical meaning

If the user is a deployer:

- do not wait for the provider to "take over" before preserving evidence and preparing authority notification
- suspend use where risk is live
- document attempts to contact provider
- preserve logs for at least the applicable retention period, noting **Article 26(6)** requires at least six months where logs are under the deployer's control

If the user is a provider:

- ask when and how the deployer first noticed the event
- ask whether the deployer already informed authorities
- align messaging fast to avoid contradictory reports

Use `references/corrective-measures.md`.

---

### Step 7 - Map Overlapping Legal Regimes

Article 73 rarely sits alone. Run a parallel obligations check.

#### 7A. GDPR

Ask:

- did the incident involve personal data?
- was there unauthorised access, loss, corruption, exposure, or unfair/automated decision impact?
- does the event trigger **Article 33 GDPR** breach notification to the supervisory authority?
- are **Article 34 GDPR** notifications to data subjects required?
- does the incident expose a flawed or outdated **DPIA**?

#### 7B. NIS2 / cyber security

Ask:

- is the entity an essential or important entity?
- did the incident impair availability, authenticity, integrity, or confidentiality of network/information systems?
- are early warning / incident notification duties triggered under the applicable national NIS2 implementation?

#### 7C. Medical devices / IVD / machinery / product safety

For AI systems embedded in regulated products:

- check whether the incident must also be reported under MDR/IVDR vigilance rules
- check whether machinery or general product safety incident channels apply
- note **Article 73(9) and (10)**: where equivalent Union reporting regimes exist, AI Act incident notification may be limited to certain types of incidents, especially those affecting fundamental rights under Article 3(49)(c), and medical-device route incidents go to the designated national competent authority

#### 7D. Employment and German works council issues

If the incident occurred in employment or workplace monitoring context:

- assess whether workers' representatives / works council need to be informed
- in Germany, remember **BetrVG** co-determination and information implications may be live, especially where the system monitors behaviour or performance or affects personnel decisions

Use `references/cross-regulation-mapping.md` and `references/dach-specific.md`.

---

### Step 8 - Drive Corrective Measures and Investigation Discipline

The report is not the end. The operational response matters just as much.

#### Provider checklist under Article 73(6)

- start investigation **without delay**
- perform risk assessment of incident and system
- identify corrective action
- cooperate with authorities and notified body where relevant
- preserve evidence and avoid uncontrolled changes to the system before authority coordination

#### Good practice actions

- freeze model/version identifiers
- snapshot configurations, prompts, training/fine-tune references, and deployment environment
- document whether human oversight failed because of design, workload, UI, instructions, or user workarounds
- assess whether incident suggests a broader field-corrective action across customers
- review whether the post-market monitoring system and complaint-handling process worked as designed

#### Outputs for the user

- immediate containment actions
- stakeholder communication map
- field correction / patch / rollback plan
- legal reporting matrix
- board or management briefing

Use `references/corrective-measures.md` and `references/templates.md`.

---

## Decision Logic Summary

### Fast Triage Tree

**Q1. Is the system actually high-risk?**
- No → Article 73 out, check other regimes
- Yes / likely yes → Q2

**Q2. Does the event fit a serious-incident harm category?**
- No → record and monitor
- Yes / maybe → Q3

**Q3. Is there a causal link or reasonable likelihood?**
- No → document and reassess as facts develop
- Yes / plausible → Q4

**Q4. Which deadline bucket applies?**
- death → immediate / max 10 days
- widespread / Article 3(49)(b) type → immediate / max 2 days
- otherwise → immediate / max 15 days

**Q5. Who reports?**
- provider by default under Article 73
- deployer also has duties under Article 26(5)

**Q6. Where?**
- market surveillance authority of Member State where incident occurred
- Germany: start with BNetzA routing plus sector overlays

---

## Practical Drafting Guidance

When preparing an answer, avoid vague legalese. Structure the response like this:

1. **Bottom line** - report now / likely report / monitor only
2. **Why** - high-risk basis + serious-incident basis + causation status
3. **Deadline** - 2 / 10 / 15 days and when the clock started
4. **Who to notify** - authority map + provider/deployer split
5. **What to send now** - minimum report contents
6. **What to do today** - suspend, preserve logs, inform deployers, assign owner
7. **What else may be triggered** - GDPR, NIS2, MDR, etc.

---

## DACH-Specific Notes

### Germany

- Treat **BNetzA** as the primary practical AI Act market-surveillance entry point for routing/reporting questions in Germany.
- Check whether a sector authority also needs notification.
- If employees are affected, consider **BetrVG**, internal investigation protocols, and communication with workers' representatives.
- If personal data is involved, identify the competent German supervisory authority under GDPR in parallel.

### Austria

- Verify the competent national authority for the specific AI Act and sector context.
- Where facts are time-critical, prepare a report package first and finalise recipient confirmation in parallel.

### Switzerland

- Switzerland is not an EU Member State, so Article 73 itself is not an EU Member State reporting route there.
- But Swiss incidents may still matter contractually, for product safety, data protection, and for EU reporting if the same AI system caused or contributed to incidents within the EU or affected EU deployments.

Use `references/dach-specific.md`.

---

## Omnibus / Timing Caveat

The Digital Omnibus simplification package (Commission proposal December 2025) progressed to a Council/Parliament provisional political agreement on 7 May 2026. That agreement would shift the application date for Annex III high-risk obligations to **2 December 2027** and Annex I high-risk obligations to **2 August 2028** if formally adopted. It is **not yet adopted law** — pending formal adoption and Official Journal publication. For now, do **not** rewrite the legal substance based on the provisional agreement alone.

Practical rule:

- note the provisional agreement as context where timing matters
- apply the **current law as enacted** unless and until amendments are adopted and in force

---

## Output Format

When using this skill, tailor the response into these deliverables.

### Deliverable 1 - Qualification Snapshot

- system classification: high-risk / not high-risk / uncertain
- Article 6 basis
- Article 6(3) exception assessment if relevant
- serious incident: yes / no / uncertain
- causal link: established / reasonably likely / not established

### Deliverable 2 - Reporting Recommendation

- report required: yes / likely yes / not yet
- deadline bucket: 2 / 10 / 15 days
- awareness date
- clock-start rationale
- initial incomplete report needed: yes / no

### Deliverable 3 - Recipient Map

- Member State(s)
- primary market surveillance authority
- sector-specific authority overlap
- provider vs deployer notification split

### Deliverable 4 - Action Plan

- next 4 hours
- next 24 hours
- next 7 days

### Deliverable 5 - Drafts

If requested, provide:

- draft Article 73 notification
- deployer notice to provider
- management briefing
- cross-regulation notification matrix

---

## Reference Files

Use these for deeper analysis and practical drafting:

- `references/incident-qualification.md`
- `references/reporting-requirements.md`
- `references/corrective-measures.md`
- `references/cross-regulation-mapping.md`
- `references/dach-specific.md`
- `references/templates.md`

---

## Disclaimer

This skill provides a structured legal-operations workflow for EU AI Act serious-incident handling. It is not a substitute for case-specific legal advice, sector-specific regulatory advice, or forensic fact-finding.

Important limits:

- Article 73 only applies to **high-risk AI systems** that are actually in scope.
- Serious-incident analysis is **fact-sensitive** and may change quickly as evidence develops.
- Sector-specific product, cyber, labour, and data-protection rules may impose **parallel or stricter** duties.
- Where death, critical infrastructure, medical-device safety, or multi-state harm is involved, escalate to specialist counsel immediately.
