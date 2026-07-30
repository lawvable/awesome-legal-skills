---
name: gdpr-breach-sentinel-oliver-schmidt-prietz
description: |
  Elite incident response and legal compliance guidance for data breaches under GDPR Articles 33 & 34. Use when: (1) User reports a data breach or security incident — including "is this even a personal data breach?" triage, (2) User asks about breach notification obligations or deadlines, (3) User mentions "72 hours", Art. 33, Art. 34, or notification requirements, (4) Discussion involves security incidents affecting personal data, (5) User needs breach risk assessment using ENISA methodology, (6) User mentions "Data Breach" or "Incident" or "Data Leakage" or "Ransomware" or "Exfiltration", (7) User needs to determine Controller vs Processor obligations, (8) Cross-border breach scenarios requiring Lead SA determination, (9) User needs a mitigation playbook or immediate response recommendations, (10) User needs audit-ready breach documentation (.docx) or an EDPB-template-aligned breach notification / evidence file — including follow-up and withdrawal notifications, (11) Breach involves an AI system requiring AI Act Art. 73 serious incident screening.
metadata:
  author: Oliver Schmidt-Prietz
  license: AGPL-3.0
  version: 2026.06.11
---

# GDPR Breach Response Sentinel

Guide users through post-breach compliance with **GDPR Articles 33 & 34**, **EDPB Guidelines 9/2022 & 01/2021**, and **ENISA Severity Methodology**. Build an EDPB-template-aligned breach evidence file, generate audit-ready documentation, and provide actionable mitigation guidance.

---

## Session Initialization

### 1. Display Disclaimer (show at session start, do not block)

> **Important:** This skill provides structured GDPR breach-notification guidance based on Art. 33–34 GDPR, EDPB Guidelines, and ENISA methodology. It is not legal advice. Final notification decisions should involve your organisation's DPO and qualified legal counsel.

### 2. Confidentiality & Input Hygiene (show with disclaimer, do not block)

> **Handle with care:** This may be a live incident.
> - Do not paste real personal data unless necessary — anonymised or pseudonymised samples ("Employee A", "Patient 1") are sufficient for the assessment.
> - Do not upload forensic artefacts, logs, or personal data to public tools unless cleared by your security and legal teams; for an actual breach, work in an environment your organisation has approved for confidential incident data.
> - Preserve legal privilege: keep communications prepared with or for legal counsel separate from operational facts, and mark them as privileged.
> - Keep facts, assumptions, and legal conclusions clearly separated in everything you record (see Evidence Posture below).

### 3. Check Emergency Status

> "Are you in a time-critical situation with less than 12 hours remaining on your notification clock?"

- **Yes** → Activate EMERGENCY MODE (see below)
- **No** → Proceed — offer STANDARD MODE or FAST PATH

### 4. Breach Qualification Gate (run BEFORE intake)

Not every security incident is a personal data breach. Establish two things first:

1. **Security breach?** "Has there been a breach of security affecting your systems, premises, processes, or people?"
2. **Personal data affected?** "Did it lead — actually or possibly — to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data transmitted, stored or otherwise processed?" (Art. 4(12))

Classify into exactly one verdict:

| Triage Verdict | Meaning | Next Step |
|----------------|---------|-----------|
| **SECURITY INCIDENT ONLY** | No personal data affected (e.g., DDoS against a static site, malware on a system holding no personal data) | Art. 33/34 not triggered. Document why no personal data was involved (offer a short internal security-incident record, .docx), advise preserving that documentation, screen parallel regimes (NIS2 etc.), and stop the GDPR workflow — no dashboard, no ENISA run |
| **BREACH CONFIRMED** | Personal data demonstrably affected | Proceed to intake — the 72h clock analysis applies |
| **BREACH LIKELY — UNDER INVESTIGATION** | Personal data probably affected but not yet confirmed | Proceed to intake; treat T0 conservatively and use the "Still Under Investigation" pathway |
| **INSUFFICIENT FACTS** | Cannot yet say whether personal data is affected | Preserve evidence (logs, system images, access records), define fact-finding actions with owners and deadlines, re-triage as soon as facts emerge |

Only the last three verdicts proceed to intake (and appear in the Assessment Dashboard's Triage row); a SECURITY INCIDENT ONLY verdict ends with a short triage record instead of the full dashboard. If facts later change (e.g., the incident turns out to have touched personal data), re-run the gate.

### 5. Intake Mode Selection

Offer the user a choice:

> **How would you like to proceed?**
> - **Guided Mode** — I'll walk you through questions one at a time (recommended if unsure)
> - **Fast Path** — Provide a structured summary of the incident and I'll assess immediately

If user selects **Fast Path**, accept a free-form or structured description and extract **all 11 data points** matching the guided mode questions: (1) Role, (2) Timeline/T0, (3) Breach Type, (4) Data Categories, (5) Subject Count, (6) Identifiers, (7) Encryption, (8) Malicious Intent, (9) Cross-Border, (10) DPA Deadlines, (11) AI System Involvement. If any data points are missing from the user's description, prompt for the missing items before proceeding. Confirm all extracted values before proceeding. Skip to Risk Assessment once confirmed.

If the user selects **Guided Mode** but has already supplied some or all data points, do not re-ask them one by one — confirm the supplied values in a single table (as in Fast Path) and ask only for what is missing.

### Quick Decision Trees

For rapid preliminary orientation on common scenarios (lost encrypted device, misdirected email, ransomware, phishing), use the decision trees in [references/enisa-methodology.md](references/enisa-methodology.md) §0. Trees are orientation only — always complete the full assessment for the definitive classification.

---

## Standard Mode: Question Sequence (Guided Mode)

Ask questions **ONE AT A TIME** in this order:

| Order | Category | Key Question |
|-------|----------|--------------|
| 1 | **Role** | "Does the affected data belong to your organization, your clients, or BOTH?" |
| 2 | **Timeline** | "When did you achieve reasonable certainty a breach occurred?" (This is T0) |
| 3 | **Breach Type** | "Which types of breach apply? Select ALL that apply: Confidentiality (data disclosed), Integrity (data altered), Availability (data lost/inaccessible), or **Still Under Investigation**. Many incidents involve multiple types — e.g., ransomware typically involves both Availability and potentially Confidentiality." |
| 4 | **Data Categories** | "What categories of personal data were involved?" |
| 5 | **Subject Count** | "Approximately how many individuals are affected?" |
| 6 | **Identifiers** | "What identifiers are present? (names, emails, IDs, etc.)" |
| 7 | **Encryption** | "Was the data encrypted? Is the key secure? Stored separately?" |
| 8 | **Malicious Intent** | "Was this accidental or intentional (theft, hacking)?" |
| 9 | **Cross-Border** | "Are affected individuals in multiple EU Member States? Where is your main establishment?" |
| 10 | **DPA Deadlines** | "Does your Data Processing Agreement specify a notification window? (Common: 24h or 48h)" |
| 11 | **AI System** | "Does this breach involve an AI system? (e.g., model leak, adversarial attack, AI-generated output exposure)" |

### Role Determination (Track Selection)

| Scenario | Track | Action |
|----------|-------|--------|
| **Controller Only** | A | Full risk assessment, SA notification decision |
| **Processor Only** | B | Notify controller without undue delay; prepare provisional factual/risk support package; final Art. 33/34 decision remains with the controller |
| **Hybrid (Both)** | A+B | Run parallel tracks, never conflate |

### Breach Type: "Still Under Investigation"

If the user selects "Still Under Investigation" for breach type:

1. **Start the clock anyway** — T0 is based on reasonable certainty that a breach *occurred*, not on full scope determination. If personal data was involved, the 72h clock is likely already running.
2. **Preserve evidence** — Advise the user to preserve logs, system images, and access records before any remediation.
3. **Assume worst-case for initial assessment** — Score CB based on the worst plausible scenario given the known facts. This can be revised downward in a supplementary notification.
4. **Use phased notification** — Art. 33(4) explicitly allows phased notification. Advise the user to file an initial notification with known facts and commit to supplementary information within a defined timeframe.
5. **Document the investigation** — Record what is known, what is unknown, and what steps are being taken to determine the full scope. This demonstrates accountability to the SA.
6. **Reassess when scope is clearer** — Once the investigation reveals the actual breach type(s), re-run the ENISA calculation and update the assessment.

### T0 Validation Rules

Challenge T0 claims when:
- Gap between suspicion and certainty > 24 hours → Ask for investigation details
- Gap > 48 hours → Flag as "may be scrutinized by SA"
- T0 set at convenient boundary (midnight, 9 AM) → Ask for specific triggering event

**Two-Stage T0 Analysis (Processor Scenarios):**

For processors, T0 operates in two stages with distinct legal consequences:

| Stage | T0 Event | Obligation Triggered | Deadline |
|-------|----------|---------------------|----------|
| **Stage 1: Processor T0 (T0-P)** | Processor becomes aware of the breach | Notify the controller "without undue delay" (Art. 33(2)) | Statutory: without undue delay; contractual: per DPA (often 24-48h) |
| **Stage 2: Controller T0** | Controller is informed by the processor (per EDPB Guidelines 9/2022, the controller should be considered "aware" once the processor has informed it) | Controller's 72h clock starts for SA notification | 72h from controller's T0 |

Always determine both T0 timestamps for processor scenarios and display both in the assessment. The processor's own awareness does *not* start the controller's 72h clock — the controller's clock starts when the controller is informed (or otherwise becomes aware itself).

### Processor Deadlines (Track B)

The processor's **statutory** duty is to notify the controller **without undue delay** after becoming aware (Art. 33(2)). There is **no statutory 72-hour deadline for the processor**, and the processor does not notify the SA — unless it is simultaneously a controller for some of the affected processing, in which case run Track A in parallel for that data.

On top of the statutory duty, most DPAs add a **contractual** notification window:
- **24 hours** (common in financial services, healthcare)
- **48 hours** (common in enterprise agreements)
- **"Without undue delay"** (mirrors GDPR language)

If the user is a processor:
1. Establish the processor awareness time (T0-P).
2. Ask for the DPA window and compute the contractual deadline from T0-P.
3. Treat the contractual deadline as the operational target. Where the DPA is silent, "without undue delay" still means hours, not days.
4. Explain the downstream consequence: the controller's 72h clock starts when the processor informs it — prompt processor notification directly protects the controller's compliance.

**Track B output must show:** processor awareness time (T0-P) · contractual deadline and time remaining · "without undue delay" status · controller handoff package completeness (see [references/templates.md](references/templates.md)) · the controller's 72h clock as a **downstream controller duty**, never as the processor's own statutory clock.

### Supply Chain / Sub-Processor Chain Breaches

When a breach originates at a sub-processor, notification follows the contractual chain: `Sub-Processor → Processor → Controller → SA`. Each link owes the next link notice "without undue delay" (plus any DPA window). The controller's 72h clock starts only when the controller is informed or otherwise becomes aware. Don't wait for complete upstream details — each link notifies with available information and supplements later. Document when each link was notified and what was provided; SAs scrutinise chain delays. If an entity in the chain is also controller for some affected data, run Tracks A and B in parallel.

---

## Risk Assessment (ENISA Methodology)

**Formula:** `SE = (DPC × EI) + CB`

For detailed scoring tables, read [references/enisa-methodology.md](references/enisa-methodology.md).

### Quick Reference

**DPC (Data Processing Context): 1-4 (hard bounds after adjustments)**
| Category | Score |
|----------|-------|
| Simple (name, contact) | 1 |
| Behavioral (location, browsing) | 2 |
| Financial (bank, salary) | 3 |
| Sensitive Art. 9 (health, biometric) | 4 |

**DPC Cap Rule:** After applying contextual adjustments (see [enisa-methodology.md](references/enisa-methodology.md)), the final DPC is **capped at 4.0** and **floored at 1.0**. Where adjustments would exceed the cap (e.g., Art. 9 base 4 + vulnerable subjects +3 = theoretical 7), note the excess factors as qualitative aggravating circumstances in the Strategic Advisory — they reinforce severity but do not change the numeric score.

**EI (Ease of Identification): 0.25-1.00**
| Level | Score |
|-------|-------|
| Negligible | 0.25 |
| Limited | 0.50 |
| Significant | 0.75 |
| Maximum | 1.00 |

**CB (Circumstances): 0-2 (additive)**
- Confidentiality loss: 0 / +0.25 / +0.50
- Integrity loss: 0 / +0.25 / +0.50
- Availability loss: 0 / +0.25 / +0.50
- Malicious intent: +0.50

### Severity Verdicts (Presumptive)

| SE Score | Level | Presumptive action (subject to Art. 33/34 legal test) |
|----------|-------|-------------------------------------------------------|
| < 2 | LOW | Presumption: internal log only (Art. 33(5)) |
| 2 – < 3 | MEDIUM | Presumption: SA notification (Art. 33) |
| 3 – < 4 | HIGH | Presumption: SA + Data Subjects (Art. 33 & 34) |
| ≥ 4 | VERY HIGH | Presumption: SA + Subjects + consider public communication |

### The Legal Test — Art. 33/34 Bridge (MANDATORY)

The ENISA score **informs** the legal assessment; it does not mechanically determine notification duties. The statutory triggers are normative legal tests:

- **Art. 33(1):** notify the SA unless the breach is "**unlikely to result in a risk** to the rights and freedoms of natural persons". If you cannot positively conclude "unlikely", the presumption is to notify.
- **Art. 34(1):** communicate to data subjects when the breach is "**likely to result in a high risk**" to rights and freedoms — unless an Art. 34(3) exception applies (see Art. 34 Decision Module below).

Every assessment MUST contain a written bridge from score to conclusion:

```
LEGAL BRIDGE
ENISA score:      [SE value + level]
Key facts:        [what happened, to whose data, at what scale]
Safeguards:       [in place before the breach / applied after]
Likely impact:    [likelihood & severity of consequences for individuals]
→ Art. 33(1):     [NOTIFY SA / NO — unlikely to result in a risk, because …]
→ Art. 34(1):     [NOTIFY SUBJECTS / NO — no high risk, because … /
                   NO — exception Art. 34(3)(a)/(b)/(c) applies, because …]
```

If the legal conclusion diverges from the score's presumption — in either direction — state why in writing. The score creates a presumption; the bridge is the decision. A worked example is in [references/enisa-methodology.md](references/enisa-methodology.md) §4a.

### Borderline Score Guidance

When a score is within 0.25 of a threshold (2.0 / 3.0 / 4.0), explicitly note this in the assessment, apply the borderline guidance table in [references/enisa-methodology.md](references/enisa-methodology.md) §4b, lean conservative, and recommend the user discuss the borderline classification with their DPO or legal counsel.

### Flags to Apply

| Flag | Condition | Effect |
|------|-----------|--------|
| 🚩 SCALE | >100 individuals | Increased SA scrutiny |
| 🔒 ENCRYPTED | Data encrypted, key secure | May support Art. 34(3)(a) exception |
| 👶 VULNERABLE | Minors, patients | Consider upgrading notification |
| ⚠️ CROSS-BORDER | Cross-border processing | One-stop-shop analysis (see Cross-Border Rules) |
| 🇬🇧 UK SUBJECTS | UK residents affected | Separate ICO notification required (see UK note below) |
| 🤖 AI SYSTEM | AI system involved | Check AI Act Art. 73 obligations |

**UK GDPR Note:** For UK-resident data subjects, ICO guidance may differ from EDPB recommendations. The UK is not bound by EDPB guidelines — it follows ICO guidance under the UK GDPR and Data Protection Act 2018. The ENISA methodology provides a useful analytical framework, but ICO's own risk assessment approach should also be consulted. Always use the [ICO's self-assessment tool](https://ico.org.uk/for-organisations/report-a-breach/) when available, and note that the ICO has its own notification portal and forms separate from any EU SA.

---

## Evidence Posture (include in EVERY assessment)

Defensible breach decisions separate what is known from what is assumed. Every assessment output must contain:

```
EVIDENCE POSTURE
Established facts:       [verified, with source — logs, forensics, admissions]
Working assumptions:     [explicitly labelled, with their basis]
Material unknowns:       [what is not yet known that could change the verdict]
Evidence still needed:   [next fact-finding actions — owner, deadline]
Confidence level:        [HIGH / MEDIUM / LOW]
Impact on notification:  [how the unknowns affect the Art. 33/34 conclusions]
```

Never present an assumption as a fact. Phased notification (Art. 33(4)) exists precisely so that incomplete facts do not delay the initial notification.

---

## AI Act Intersection (Art. 73 Check)

If the user confirms the breach involves an AI system, perform an additional assessment:

1. **Classification:** Is this a **high-risk AI system** (AI Act Annex III, or a product-embedded system under Annex I)? Is it deployed in a regulated sector (healthcare, law enforcement, critical infrastructure)?
2. **Serious incident test (Art. 3(49)):** Does the incident directly or indirectly lead to (a) the death of a person or serious harm to a person's health; (b) a serious and irreversible disruption of the management or operation of critical infrastructure; (c) an infringement of obligations under Union law intended to protect fundamental rights; or (d) serious harm to property or the environment?
3. **If yes → Art. 73 reporting:** The **provider** (or, where applicable, the deployer) reports to the **market surveillance authority** of the Member State(s) where the incident occurred — immediately after establishing a causal link between the AI system and the incident (or its reasonable likelihood), and at the latest **15 days** after awareness. Shortened deadlines: **2 days** for widespread infringement or a critical-infrastructure incident under Art. 3(49)(b); **10 days** in the event of death. An initial incomplete report followed by a complete report is permitted.
4. **Applicability:** Art. 73 applies from **2 August 2026** (high-risk systems embedded in Annex I regulated products: 2 August 2027; sectoral reporting equivalences under Art. 73(9)-(10)). Before the applicable date, state that the duty "will apply from" that date — it is not yet a live obligation.
5. **Parallel obligations:** Art. 73 runs **in parallel** to GDPR notification — separate obligations, separate recipients, separate deadlines.

Full detail (definitions, deadlines, deferrals): read [references/parallel-regimes.md](references/parallel-regimes.md).

### Output
When the AI SYSTEM flag is set, insert this block into the Assessment Dashboard as its own **AI ACT STATUS** section (placed before LEGAL VERDICT), in addition to the one-line `AI Act Art. 73` row:
```
AI ACT STATUS: [Applicable / Not Applicable / Not Yet Applicable / Requires Further Assessment]
Art. 73 Reporting: [Required / Not Required / Not Yet Applicable / Under Assessment]
AI System Classification: [High-Risk Annex III / High-Risk Annex I product-embedded / Limited Risk / Minimal Risk / Not Classified]
```
Do not take the user's Annex III classification at face value: a CE-marked medical device or other Annex I regulated product is **product-embedded** high-risk (application 2 Aug 2027; Art. 73(9)-(10) defer largely to sectoral vigilance regimes such as MDR/IVDR, which may impose **live** reporting duties today). Recommend verifying with the user's regulatory team.

---

## Sectoral Parallel-Regime Screen

A personal data breach often triggers duties outside the GDPR. Run a lightweight screen after the GDPR assessment — or directly at triage exit for SECURITY INCIDENT ONLY verdicts — identify, do not analyse in depth unless the user asks:

| Regime | Trigger Hint |
|--------|--------------|
| NIS2 / national implementation | Essential/important entity with a significant ICT incident — if the `nis2-navigator` skill is available, use it for that track |
| DORA | Financial entity with an ICT-related incident |
| eIDAS | Trust service provider |
| AI Act Art. 73 | High-risk AI system serious incident (see above) |
| ePrivacy / telecoms | Provider of publicly available electronic communications services |
| Criminal law | Report to police/judicial authorities (also an EDPB template field) |
| Insurance | Cyber policy notification clauses — often short windows |
| Contracts | Customer/partner notification clauses beyond DPAs |
| Employment | Works council / employee representative involvement where employee data is affected (especially in Germany) |

Output line for the dashboard: "**Potential parallel regimes identified:** [list] — not assessed in detail unless requested." Details and screening questions: [references/parallel-regimes.md](references/parallel-regimes.md).

---

## EDPB Case Matching

After risk assessment, match to EDPB Guidelines 01/2021 cases. See [references/edpb-cases.md](references/edpb-cases.md).

**Categories:**
- Ransomware: Cases 01-04
- Data Exfiltration: Cases 05-07
- Internal Human Risk: Cases 08-09
- Lost/Stolen Devices: Cases 10-12
- Mispostal: Cases 13-16
- Social Engineering: Cases 17-18

**Analogy warning:** EDPB cases are illustrative analogies, **not binding decisions**. Factual differences matter, and an analogy never replaces the Art. 33/34 legal test on the actual facts. State the closest case, the limits of the analogy, and where your facts differ (see the analogy rules in the reference).

Output format:
> "This scenario resembles **EDPB Case [XX]**: [Description]. EDPB recommendation: SA [YES/NO], Subjects [YES/NO]. Your situation differs in: [differences]. Limits of the analogy: [limits]. This [supports/suggests reconsidering] your calculated verdict."

---

## Dynamic Web Research Module

After completing the ENISA calculation and EDPB case matching, **automatically** perform targeted web research to enrich the assessment. Read [references/web-research.md](references/web-research.md) for specific query templates (enforcement precedents, SA-specific guidance, sector trends, EDPB updates, AI Act, damages precedent) and how to incorporate findings. Apply the **source discipline** rules in that reference: official sources (SA / EDPB / Commission) first, no SEO or marketing pages as the basis for legal conclusions, cite access dates, and never invent portal links or SA contact details. Add a "Regulatory Intelligence" section to the Assessment Dashboard.

---

## Cross-Border Rules

### First: Is It Actually Cross-Border Processing?

One-stop-shop requires genuine **cross-border processing** (Art. 4(23)) — processing in the context of establishments in more than one Member State, or processing that substantially affects individuals in more than one Member State. **Do not assume cross-border processing merely because affected individuals live in several Member States** — the test is the processing, not subject residence. Analyse before applying the one-stop-shop.

### Controllers WITH EU Establishment

- Notify **Lead SA only** (one-stop-shop), where a main establishment and lead SA can be determined
- Lead SA = location of main establishment
- Indicate affected Member States in the notification (the EDPB template asks for per-country subject counts)

### Controllers WITHOUT EU Establishment

- One-stop-shop does NOT apply — the mere presence of an EU representative does not trigger it (EDPB Guidelines 9/2022 v2.0, para 73)
- Notify **EACH SA** where affected subjects reside in their Member State
- Track submissions individually; national portals may require local formats and fields

### Lead SA Determination Questions

1. "Where are decisions about this data processing made?"
2. "Where is your central administration?"
3. "Which establishment has authority over this processing?"

### SA Contact Directory

For the identified Lead SA or relevant SA(s), use web_search to find:
- Official SA notification portal URL
- SA contact email and phone for breach notifications
- Any SA-specific notification forms or requirements (some SAs have their own mandatory forms, e.g., BfDI in Germany, CNIL in France)
- Operating hours and emergency contact procedures

For **Germany**, route between BfDI (federal bodies, telecoms/post) and the LfDI/LDA of the relevant Bundesland (private sector) — see the Germany routing rules in [references/web-research.md](references/web-research.md).

Output the SA contact details in the Assessment Dashboard. In **processor-only (Track B)** runs, frame SA details as courtesy material for the controller handoff package — never as a portal the processor should use itself — and mark the dashboard's "Notify SA" / SA-deadline rows as downstream controller duties (N/A for the processor).

---

## Mitigation Playbook

After the risk assessment, generate a **tailored mitigation playbook** specific to the incident — not a generic checklist but case-driven actions that actually matter for THIS breach.

Read [references/mitigation-playbook.md](references/mitigation-playbook.md) for the full playbook design principles, output format (prioritized action plan with owner/deadline/dependencies), and common action categories to draw from.

---

## User Override Protocol

If user disagrees with calculated severity:

1. Document original: "My assessment indicates **[LEVEL]** (SE = [score]). You wish to classify as **[USER LEVEL]**."
2. Require justification
3. If DOWNGRADE, display warning:

> ⚠️ **REGULATORY RISK WARNING**
> You are selecting lower severity than ENISA indicates. If the SA later determines higher severity was warranted, this may increase regulatory scrutiny and result in separate sanctions. Recommend documenting with legal counsel involvement.

4. Document override in Internal Compliance Log

---

## Output: Assessment Dashboard

```
╔══════════════════════════════════════════════════════════════╗
║                 BREACH ASSESSMENT SUMMARY                     ║
╠══════════════════════════════════════════════════════════════╣
║ Triage:         [BREACH CONFIRMED / LIKELY — UNDER            ║
║                  INVESTIGATION / INSUFFICIENT FACTS]          ║
║ Role:           [Controller / Processor / Hybrid]             ║
║ Breach Type:    [Confidentiality / Integrity / Availability]  ║
║                 (multiple types may apply)                    ║
║ T0 (Awareness): [Timestamp]                                   ║
║ Clock Status:   [X hours elapsed / Y hours remaining]         ║
║ DPA Deadline:   [If applicable: X hours / N/A]                ║
╠══════════════════════════════════════════════════════════════╣
║                 SEVERITY CALCULATION                          ║
╠══════════════════════════════════════════════════════════════╣
║ DPC: [Score] - [Category + Adjustments]                       ║
║ EI:  [Score] - [Level]                                        ║
║ CB:  [Score] - [Breakdown]                                    ║
║ SE = (DPC × EI) + CB = [Final Score]                          ║
║ Severity Level: [LOW / MEDIUM / HIGH / VERY HIGH]             ║
║ Borderline:     [YES - near X threshold / NO]                 ║
║ EDPB Case Match: Case [XX] - [Supports/Reconsider]            ║
╠══════════════════════════════════════════════════════════════╣
║                 EVIDENCE POSTURE                              ║
╠══════════════════════════════════════════════════════════════╣
║ Confidence: [HIGH/MED/LOW] | Material unknowns: [count/list]  ║
╠══════════════════════════════════════════════════════════════╣
║                 FLAGS                                         ║
╠══════════════════════════════════════════════════════════════╣
║ 🚩 Scale: [YES/NO] | 🔒 Encrypted: [YES/NO]                   ║
║ 👶 Vulnerable: [YES/NO] | ⚠️ Cross-Border: [YES/NO]           ║
║ 🤖 AI System: [YES/NO]                                        ║
╠══════════════════════════════════════════════════════════════╣
║                 LEGAL VERDICT                                 ║
╠══════════════════════════════════════════════════════════════╣
║ Legal Bridge:    Art. 33(1) [notify / no risk]                ║
║                  Art. 34(1) [high risk / not high risk /      ║
║                  exception 34(3)(a)/(b)/(c)]                  ║
║ Notify SA:       [YES/NO] - Deadline: [TIME]                  ║
║ Notify Subjects: [YES / NO / Exception 34(3)(a)/(b)/(c)]      ║
║ Internal Log:    [MANDATORY]                                  ║
║ AI Act Art. 73:  [Required/Not Required/Not Yet Applicable/   ║
║                  N/A]                                         ║
║ Parallel Regimes: [list or "none identified"]                 ║
╠══════════════════════════════════════════════════════════════╣
║                 SA CONTACT DETAILS                            ║
╠══════════════════════════════════════════════════════════════╣
║ Lead SA:         [Name]                                       ║
║ Portal:          [URL]                                        ║
║ Contact:         [Email / Phone]                              ║
║ Additional SAs:  [If cross-border without one-stop-shop]      ║
╠══════════════════════════════════════════════════════════════╣
║                 REGULATORY INTELLIGENCE                       ║
╠══════════════════════════════════════════════════════════════╣
║ [Summary of relevant enforcement precedents and guidance]     ║
╚══════════════════════════════════════════════════════════════╝
```

---

## Art. 34 Decision Module

Whenever the facts or the score suggest possible high risk, run a dedicated Art. 34 analysis — never reduce it to a yes/no line:

- **Trigger:** "likely to result in a high risk" (Art. 34(1)); timing "without undue delay".
- **Exceptions (Art. 34(3)):** (a) appropriate technical/organisational protection measures were applied to the affected data — in particular measures rendering it unintelligible, such as state-of-the-art encryption with a secure key; (b) **subsequent measures** ensure the high risk is no longer likely to materialise; (c) communication would involve **disproportionate effort** → a public communication or equally effective measure must be made instead.
- **Content (Art. 34(2)):** plain-language description of the breach, DPO/contact point, likely consequences, measures taken or proposed, and concrete self-protection steps.
- **Strategy:** direct vs. public communication, phased communication, vulnerable subjects first, languages per affected Member State, support channel, fraud/phishing warning wording.
- **Backstop:** the SA can order communication or confirm an exception (Art. 34(4)).

Read [references/art34-communication.md](references/art34-communication.md) for the full decision framework, and record the outcome in an **Art. 34 Decision Memo** (see [references/templates.md](references/templates.md)).

---

## Strategic Case Advisory

After presenting the Assessment Dashboard, deliver a strategic advisory as a senior data protection lawyer briefing the client's crisis team. This goes beyond the ENISA score — it's what separates competent compliance from excellent incident response.

Read [references/strategic-advisory.md](references/strategic-advisory.md) for the full advisory framework, principles, section structure, and tone examples. Cover: Case Assessment & Risk Landscape, SA Interaction Strategy, Notification Drafting Guidance, Hidden Risks & Second-Order Effects, Defensive Documentation, and Competitive Advantage in Crisis.

---

## Document Generation

After completing the assessment, offer to generate **audit-ready .docx documents**.

### Available Documents
1. **EDPB Breach Evidence File** — full notification dossier mirroring the EDPB Template [2026] structure (see below)
2. **Art. 33 SA Notification** — Formal notification to Supervisory Authority
3. **Art. 34 Subject Communication** — Plain-language notification to data subjects
4. **Art. 34 Decision Memo** — Documented high-risk analysis and exception reasoning
5. **Processor Client Notification + Handoff Package** — Notice and support package to controller clients (Track B)
6. **Internal Compliance Log** — Art. 33(5) mandatory documentation
7. **Non-Notification Justification** — When deciding NOT to notify
8. **Follow-Up / Withdrawal Notification** — Supplementing, completing, or withdrawing a prior notification
9. **Mitigation Playbook** — Prioritized checklist with owners and deadlines
10. **Complete Breach Response Package** — All applicable documents bundled

### EDPB Breach Evidence File

On request — and proactively whenever SA notification is required — build the **EDPB-template-aligned breach evidence file**: one document mirroring the numbered structure of the EDPB *Template [2026] for personal data breach notification* (§1 notification info through §7 attachments). Fill every field from the assessment; mark gaps `[UNKNOWN — investigate]` and inapplicable fields `[N/A]`. Always flag the template's **draft / public-consultation status** and that national SA portals remain authoritative until adoption. Read [references/edpb-template-evidence-file.md](references/edpb-template-evidence-file.md) for the field map, fill rules, and document skeleton.

### Document Generation Process

Read [references/templates.md](references/templates.md) for document templates and formatting standards (A4, Arial 11pt, headers/footers, ISO 8601 dates). Check for a docx generation skill (`docx-processing-anthropic` in Claude Code, or `/mnt/skills/public/docx/SKILL.md` in Claude.ai Projects). Fall back to Markdown if unavailable. Pre-fill values from the assessment; mark gaps with `[TO BE COMPLETED]`.

---

## Post-Notification Tracking

After the initial assessment, offer ongoing case management. Read [references/post-notification-tracking.md](references/post-notification-tracking.md) for the tracking dashboard template covering SA notification status (including follow-up and withdrawal), subject communication, mitigation execution phases, and documentation completion.

At the end of each session, remind the user:
- "Would you like me to generate any documentation as .docx files — including the EDPB evidence file?"
- "Do you need me to research your specific SA's notification portal and requirements?"
- "Would you like to update the post-notification tracker?"

---

## Emergency Mode

### Activation Triggers
- < 12 hours remaining on clock
- User explicitly requests
- Immediate risk to data subject safety
- T0 was > 60 hours ago

### Emergency Protocol

Display:
> ⚡ **EMERGENCY MODE ACTIVATED**
> Generating minimum viable assessment.

**Abbreviated Intake (8 questions):**
0. Does the incident involve personal data at all? (If clearly not → SECURITY INCIDENT ONLY — document why and stop the GDPR workflow)
1. Role: Controller, Processor, or Both?
2. What type of data? (Simple/Behavioral/Financial/Sensitive)
3. How many people affected?
4. Was data encrypted with key secure?
5. Malicious or accidental?
6. Which countries are affected individuals in?
7. If Processor: Does your DPA specify a notification window? (e.g., 24h, 48h)

**Rapid Calculation:**
- DPC: Use stated category, no adjustments
- EI: Default to 0.75 (Significant)
- CB: Score based on malicious/accidental + assume confidentiality loss

**Emergency Output:**
1. Preliminary verdict with caveats — including a compressed Legal Bridge (Art. 33/34 conclusions in one line each)
2. Minimum viable Art. 33 notification (generated as .docx if possible)
3. Critical immediate mitigation actions (top 5 only)
4. SA contact details (via web search)
5. Follow-up checklist (REQUIRED WITHIN 48 HOURS)

---

## Critical Reminders

1. **Document EVERYTHING** — Even non-notifiable breaches (Art. 33(5))
2. **Processors notify Controllers without undue delay (Art. 33(2))** — No statutory 72h applies to the processor; the controller's clock starts when you inform it; DPA windows are contractual, on top
3. **72 hours is maximum, not target** — "Without undue delay"
4. **Phased notification acceptable** — Don't delay for complete info
5. **The ENISA score is a presumption** — The Art. 33/34 Legal Bridge is the decision; document it in writing
6. **Not every incident is a breach** — Run the Breach Qualification Gate before the workflow
7. **SA can order subject notification** — Even if controller declined
8. **Failure to notify is separately sanctionable** — Up to €10M or 2% turnover
9. **Non-EU controllers: no one-stop-shop** — Notify each relevant SA
10. **Encryption doesn't erase breach** — Still document internally
11. **UK is separate** — Requires ICO notification post-Brexit; ICO guidance may differ from EDPB; use ICO's own self-assessment tool and notification portal
12. **AI systems have parallel obligations** — AI Act Art. 73 runs alongside GDPR (applies from 2 Aug 2026)
13. **EDPB Template [2026] is a DRAFT** — Under public consultation until 5 Aug 2026; national SA portals remain authoritative
14. **Always offer document generation** — Audit-ready .docx files, not just chat output
15. **Research the specific SA** — Portal URLs and requirements vary significantly

---

## Version & Regulatory Basis

| Document | Version | Last Verified |
|----------|---------|---------------|
| EDPB Guidelines 9/2022 (Notification) | v2.0 | Check for updates via web search |
| EDPB Guidelines 01/2021 (Examples) | v2.0 | Check for updates via web search |
| ENISA Severity Methodology | v1.0 | Check for updates via web search |
| EU AI Act (Regulation 2024/1689) | In force; Art. 73 applies from 2 Aug 2026 | Art. 73 serious incident reporting |
| EDPB Template [2026] for personal data breach notification | v1.0 DRAFT — public consultation until 5 Aug 2026 | Evidence-file structure; check consultation outcome via web search |

**Important:** Regulatory guidance evolves. The Dynamic Web Research Module should be used in every assessment to check for updates to these foundational documents.

## Related GDPR skills

This skill works standalone, but pairs well with my other EU data-protection skills — install any on its own or combine them:

- **DPIA Sentinel** — Art. 35 Data Protection Impact Assessments
- **Privacy Notice Generator** — Art. 13/14 privacy notices
- **Transfer Impact Assessment (TIA)** — Chapter V transfer assessments
- **DPA Art. 28** — controller–processor agreements (AVV)
- **Legitimate Interest** — Art. 6(1)(f) LIA / balancing test
