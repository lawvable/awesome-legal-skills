# EDPB Breach Evidence File — Template [2026] Field Map

> **STATUS — READ FIRST:** This module is based on the EDPB **Template [2026] for personal data breach notification, Version 1.0**, adopted **for public consultation** at the EDPB plenary on 10 June 2026 (document dated 8 June 2026); the consultation runs until **5 August 2026**. Until final adoption it remains a **DRAFT**. National SA notification portals and forms remain authoritative until the template is finally adopted and implemented by the SAs. Source: https://www.edpb.europa.eu/system/files/2026-06/edpb_template_2026_data_breach_notification_v1.0_en.docx — cite the access date whenever the evidence file is generated, and check via web search whether a final version has superseded the draft.

## Purpose

The evidence file turns the assessment into a **single, SA-ready dossier** mirroring the template's numbered structure. Even while the template is in draft, structuring the breach record this way means: (a) every field an SA is likely to ask for is answered or explicitly open; (b) transcribing into any national portal becomes mechanical; (c) the record is defensible — reviewers see legal reasoning, not just a score.

## Fill Rules

1. Emit the evidence file as a **filled document**, never as an empty form. Every field within a presented section gets one of:
   - a substantive answer from the assessment,
   - `[UNKNOWN — investigate]` (plus an entry under "Evidence still needed" in the Evidence Posture), or
   - `[N/A]` with a one-line reason (e.g., integrity fields for a pure confidentiality breach; "reasons for late notification" when filing within 72h).
2. Respect the template's **conditional logic** (noted per field below): where the visibility logic excludes an **entire branch** for this scenario (e.g., the follow-up/withdrawal fields for a new notification; §6.3 for an EEA-established controller), collapse the branch to a single `[N/A — reason]` line instead of listing each excluded field. Rule 1 governs every field inside the branches that ARE presented.
3. Where the template offers an enumerated list, pick from the list verbatim and add free-text detail beneath — that keeps the dossier portal-compatible.
4. The fields marked *(incomplete only)* are options only available when the notification is filed as Incomplete (preliminary, Art. 33(4) phased).
5. Stamp provenance at the end of the document: `Generated with GDPR Breach Response Sentinel v<X.Y> — <date> — based on EDPB Template [2026] v1.0 (DRAFT under public consultation until 2026-08-05)`. Read the live version number from the SKILL.md metadata; never hard-code it.

---

## §1 Information on the Notification

| Field | Options / Content | Conditions |
|-------|-------------------|------------|
| Type of notification | a) New Notification b) Follow-Up Notification | — |
| Sub-type | a) Complete b) Incomplete (preliminary, to be amended) c) Withdraw | "Withdraw" only for follow-ups (e.g., duplicate; no risk after full assessment) |
| Reasons for withdrawing | Free text | Only if Follow-Up + Withdraw |
| ID of previously notified breach | SA-issued ID | Only for follow-ups/withdrawals |
| Controller's internal reference number | Optional | — |

**Skill mapping:** New vs. Follow-Up from case history; Incomplete whenever the "Still Under Investigation" pathway or phased notification (Art. 33(4)) is active; Withdraw when a follow-up assessment concludes no notifiable breach (use the Withdrawal Notice template in [templates.md](templates.md)).

## §2 Controller and Reporting Person

| Field | Options / Content | Conditions |
|-------|-------------------|------------|
| **2.1 Controller:** identifier type + identifier (company ID / org number / VAT) | Optional | — |
| Name of the organisation, contact details | Mandatory | — |
| Sector | Private / Public | — |
| Type of organisation | Freelance/Micro · SME · Large · Other | Private only |
| Classification of economic activity | NACE-style sections A–V | Optional |
| Name + contact details of EEA representative | Mandatory | Only if controller not established in the EEA |
| **2.2 Reporting person:** name, contact details, function | DPO / Legal representative / Authorised representative or other | — |
| **2.3 DPO / contact point:** designated? name, contact details | Mandatory if DPO not the reporting person | — |
| Alternative contact point for more information | DPO / reporting person / other | Only if distinct |
| **2.4 Involvement of other parties** | Yes / No; for each: role (Processor / Joint Controller / Other), name, contact details — multiple allowed | — |

**Skill mapping:** Role determination (Track A/B/Hybrid) feeds §2.4 — a processor-origin breach (Track B upstream) is recorded here by the *controller* with the processor named as involved party.

## §3 Initial Information on the Breach

### 3.1 Timeline

| Field | Options / Content | Conditions |
|-------|-------------------|------------|
| When did the breach occur? | a) specific day b) date range c) ongoing since date d) cannot be determined e) to be determined *(incomplete only)* | — |
| Only estimated dates | Checkbox — explain estimation method in the timeline comments | — |
| Beginning / ending date & time | Timestamps | Per occurrence type |
| **Date & time of controller awareness** | = T0 from the assessment | Mandatory |
| **Reasons for late notification** | Free text | Visible when awareness + 72h has passed at filing — feed the Late Notification Explanation template |
| How was the breach discovered? | a) controller detection b) processor detection & communication c) data subject d) external party e) press f) other | — |
| Further description of discovery | e.g., IDS/EDR alert, coordinated vulnerability disclosure | — |
| Date of notification by other party | Approximate if unknown | Only if discovered via b)–f) — for processor discovery this is T0-P communication date |
| Further timeline comments | Duration of C/I/A impacts, **processor awareness date (T0-P)**, estimation methods | — |

**Skill mapping:** T0 validation and Two-Stage T0 analysis populate this section directly. Always record T0-P here in processor-origin cases.

### 3.2 Nature, Circumstances, Summary

| Field | Options / Content |
|-------|-------------------|
| Nature of the breach | Confidentiality / Integrity / Availability (multi-select) |
| Type of confidentiality breach | a) exfiltrated/disclosed b) likely exfiltrated/disclosed (no evidence) c) NOT exfiltrated/disclosed (reasonable evidence) d) not possible to assess e) to be determined *(incomplete only)* |
| Data unintelligible / individuals not identifiable? | a) yes, protection intact (e.g., secure encryption) b) protective measures likely subvertible (e.g., key exposure, technical weakness) c) no d) not possible to assess e) to be determined *(incomplete only)* — **this is the Art. 34(3)(a) screen; feed the encryption logic tree from [enisa-methodology.md](enisa-methodology.md) §5** |
| Type of integrity breach | a) altered, no evidence of wrong use b) altered + wrong use, recoverable c) altered + wrong use, NOT recoverable |
| Type of availability breach | a) temporary b) permanent c) not determined — assess from the data subject's perspective |
| **Nature of the incident** (taxonomy, pick all that fit) | a) abuse of access privileges by employee · b) encrypted device / ransomware · c) hacking / malware · d) phishing / social engineering · e) security vulnerability exploited (CVE / zero day) · f) unauthorised access in IT systems · g) data exfiltration · h) wrong data subject's data shown (record mix-up) · i) device lost or stolen · j) e-waste (data on obsolete device) · k) incorrect paper disposal · l) mail lost or opened / misdelivery (post/email) · m) misconfiguration · n) incorrect access permissions (cloud storage, shared folder) · o) paper lost/stolen/insecure · p) data deleted/destroyed · q) data displayed to wrong recipient · r) data sent by mistake (post/email) · s) email to multiple recipients without BCC / open distribution list · t) technical malfunction · u) unauthorised data modification · v) unintended publication (public link / website / shared drive) · w) verbal unauthorised disclosure · x) to be determined · y) other |
| Cause of the breach | a) internal non-malicious b) internal malicious c) external non-malicious d) external malicious e) to be determined *(incomplete only)* f) unknown — **maps to the CB malicious-intent factor** |
| Further description of the nature | Detection, awareness, cause, root cause if known, and the facts grounding each conclusion |
| Systems / software / services / infrastructure involved | Group semantically (production DBs, test infrastructure, software, services) with location |

**Skill mapping:** the EDPB case-matching category and the ENISA CB factors translate directly into the taxonomy + cause fields.

### 3.3 Data Subjects Concerned

| Field | Options / Content |
|-------|-------------------|
| Categories of data subjects | a) customers (incl. prospects) b) employees (former/current/candidates) c) military or law-enforcement staff d) minors e) patients f) students g) subscribers h) users i) vulnerable individuals (specify why) j) additional (describe) k) not yet known *(incomplete only)* — **categories d/e/i trigger the VULNERABLE flag** |
| Number of data subjects | exact / approximate / cannot be determined / to be determined *(incomplete only)* + the number |

### 3.4 Data Records Concerned

| Field | Options / Content |
|-------|-------------------|
| Type of breached data | a) basic data b) contact details c) biometric d) criminal convictions/offences e) political opinions f) racial or ethnic origin g) religious/philosophical beliefs h) sex life/sexual orientation i) trade-union membership j) genetic k) health l) economic & financial m) employment-related health n) identification data (national ID) o) location p) official documents (scans) q) payment methods r) profile data s) user credentials t) not yet known *(incomplete only)* u) additional — **DPC mapping: c–k and m → 4 (Art. 9/10); l, q → 3; o, r (and similar behavioural data, e.g. purchase/order histories) → typically 2; a, b → 1, subject to contextual adjustments** |
| Number of records | exact / approximate / cannot be determined / to be determined *(incomplete only)* + number. **Distinguish records from persons** — "5 data types about 100 people" ≠ "100 data types about 5 people"; state both dimensions |

### 3.5 Measures in Place When the Breach Occurred

Multi-select + description: a) pseudonymisation · b) backup/recovery plan · c) data encryption · d) DP & infosec policies · e) DP & security training · f) incident log · g) levels of access to data · h) logical access control (e.g., MFA) · i) periodic audits · j) physical access control · k) up-to-date IT systems · l) other. If §3.2 flagged measures as likely subvertible, detail that here.

**Skill mapping:** this is the "Safeguards (in place before)" line of the Legal Bridge.

## §4 Further Information

| Field | Options / Content |
|-------|-------------------|
| **4.1 Likely consequences** per breach type | Confidentiality: disclosed beyond policy scope / linkable to other data / usable for other or unlawful purposes / other / under assessment *(incomplete only)*. Integrity: invalid data used / validly-modified data misused / other. Availability: inability to access services / service disruption / other |
| Nature of potential impact on data subjects | a) loss of control b) limitation of rights c) discrimination d) identity theft/usurpation e) fraud f) financial loss g) unauthorised reversal of pseudonymisation h) reputational damage i) loss of confidentiality of data under professional secrecy j) disclosure to unauthorised third parties k) significant economic or social disadvantage l) physical or mental harm m) damage to property n) other o) to be determined |
| Severity of potential impacts | Minor / Moderate / Severe / To be determined — select the highest plausible |
| **4.2 Outcome of the risk assessment** | a) **likely to result in a high risk** b) likely to result in a (not high) risk c) **unlikely to result in a risk** d) additional information needed *(incomplete only)* — **this is the Art. 33(1)/34(1) conclusion of the Legal Bridge** |
| Description of the risk assessment | "Please describe the methodology used and the relevant factors" → state: **ENISA Severity Methodology (SE = (DPC × EI) + CB) as decision support, bridged to the Art. 33(1)/34(1) legal tests** — paste the Legal Bridge block here |
| **4.3 Measures taken** to address/mitigate | From the Mitigation Playbook — state to what extent each measure resolves the issue |
| **4.4 Measures to prevent recurrence** | a) anonymisation b) backup/recovery c) change of processes d) encryption e) policies f) training g) erasure h) incident log i) access levels j) logical access control k) audits l) physical access control m) pseudonymisation n) up-to-date systems o) other + description |

## §5 Communication to Data Subjects

| Field | Options / Content |
|-------|-------------------|
| Communicated? | a) yes b) no, will be on [date] / date TBD c) no, investigation ongoing *(incomplete only)* d) no — not high risk (Art. 34(1) not met) e) no — an **Art. 34(3) condition** is met |
| Date informed / planned date | Per answer above |
| Which Art. 34(3) condition | (a) protection measures applied (e.g., encryption rendering data unintelligible) · (b) subsequent measures ensure high risk no longer likely · (c) disproportionate effort → public communication or equally effective measure instead — + description of why and the measures taken (see [art34-communication.md](art34-communication.md)) |
| All or subset informed | all / not all + reasons per subgroup (unreachable, other laws, phased) |
| Means of communication | individual (letter/email/personal) / public announcement (website/press/social) / other |
| Content of the information sent | Paste the actual text, or provide means for the SA to consult it |

**Skill mapping:** the Art. 34 Decision Memo populates this section 1:1.

## §6 Other Issues

| Field | Options / Content |
|-------|-------------------|
| **6.1** Reported to police/judicial authorities as criminal offence? | yes / no / unknown |
| Notified to other authorities or bodies under other legislation (e.g., national cyber security centre)? | yes / no / unknown — + which authority and its case ID. **Feed from the Sectoral Parallel-Regime Screen** (NIS2/CSIRT, DORA, eIDAS, AI Act Art. 73, ePrivacy, insurance) |
| **6.2 Cross-border (EEA-established controller):** cross-border processing? | yes / no / unknown — only if controller established in the EEA |
| Lead SA · EEA countries with establishments · EEA countries with affected subjects · **approximate number of data subjects per country** · SAs notified/to be notified | The template carries the full EEA SA list incl. all German federal/Land authorities — use the SA routing from the Cross-Border Rules |
| **6.3 Non-EEA-established controller** (GDPR via Art. 3(2)) | EEA countries with affected subjects · per-country subject counts · **every SA notified or to be notified** (no one-stop-shop — Guidelines 9/2022 v2.0 para 73) |

## §7 Attachments

Inventory — dated copies of: a) communication to data subjects · b) risk assessment · c) research/forensic report (cyber incidents) · d) ransomware note · e) phishing message · f) internal breach-notification procedure · g) internal deletion/destruction policy for outdated data · h) communication to wrong recipients · i) external notification/message of the breach · j) other.

**Phishing note (from the template):** split the affected communications into three categories — the mailbox owner/data subject, data subjects who received a phishing mail, and data subjects whose data was in the compromised mailbox.

**Skill mapping:** generate the Attachment Inventory template ([templates.md](templates.md)) and reconcile it against this list — every claimed attachment must exist and be dated.

---

## Assessment → Template Mapping (quick table)

| Skill artefact | Template destination |
|----------------|----------------------|
| Triage verdict + breach type | §3.2 nature fields |
| T0 / T0-P / clock status | §3.1 timeline (awareness, processor communication date, late-notification reason) |
| ENISA components (DPC/EI/CB/SE) | §4.2 methodology description |
| **Legal Bridge conclusions** | §4.2 outcome (a/b/c) + description |
| Encryption logic tree | §3.2 "unintelligible" field + §5 Art. 34(3)(a) |
| Flags: VULNERABLE | §3.3 subject categories d/e/i |
| Flags: SCALE | §3.3/3.4 numbers |
| Mitigation Playbook | §4.3 / §4.4 |
| Art. 34 Decision Memo | §5 |
| Parallel-Regime Screen | §6.1 |
| Cross-Border analysis / Lead SA | §6.2 / §6.3 incl. per-country counts |
| Evidence Posture "unknowns" | every `[UNKNOWN — investigate]` entry; choose sub-type **"Incomplete"** when material unknowns affect mandatory template fields or the Art. 33(3) content (and commit to a supplementation timeframe) — minor residual unknowns alone do not force an Incomplete filing |

## Output Rules

1. Offer the evidence file proactively whenever the Legal Bridge concludes SA notification is (or may be) required; on request in all other cases.
2. Emit as Markdown; offer **.docx rendering** via the document generation process in SKILL.md (A4, Arial 11pt, ISO 8601 dates).
3. Repeat the draft-status banner at the top of every emitted evidence file, with access date.
4. If the notification will be filed as **Incomplete**, list the open fields and the committed supplementation timeframe (Art. 33(4)) at the top of the document.
5. For **follow-up** or **withdrawal** filings, reference the prior notification ID and use the corresponding templates in [templates.md](templates.md).
