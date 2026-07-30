# Breach Documentation Templates

---

## 1. Art. 33 Notification to Supervisory Authority

```
PERSONAL DATA BREACH NOTIFICATION
Pursuant to Article 33 GDPR

1. CONTROLLER INFORMATION
   Organization: [Name]
   Address: [Address]
   Contact: [DPO Name, Email, Phone]

2. BREACH DETAILS
   Date/Time of Breach: [If known, or "Under investigation"]
   Date/Time of Awareness (T0): [Timestamp]
   Nature of Breach: [Confidentiality/Integrity/Availability - explain]

3. DATA AFFECTED
   Categories of Data: [Specific list]
   Approximate Number of Records: [Number or estimate with basis]
   Approximate Number of Individuals: [Number or estimate with basis]

4. LIKELY CONSEQUENCES
   [Description of potential impacts on data subjects]
   [Based on severity assessment: specific risks identified]

5. MEASURES TAKEN/PROPOSED
   Containment: [Actions taken to stop breach]
   Mitigation: [Steps to reduce impact on subjects]
   Prevention: [Future safeguards planned]

6. NOTIFICATION TO DATA SUBJECTS
   [Will communicate / Have communicated on [date] /
    Not required because: (detailed justification)]

7. CROSS-BORDER ELEMENTS (if applicable)
   Member States affected: [List]
   Establishments involved: [List]

8. ADDITIONAL INFORMATION
   [If phased notification: Information to follow includes...]
   [If delayed beyond 72h: REASONS FOR DELAY - detailed explanation]

---
Assessment generated with GDPR Breach Response Sentinel
Guidance version: EDPB Guidelines 9/2022 v2.0, ENISA Methodology v1.0
This output does not constitute legal advice.
```

---

## 2. Art. 34 Communication to Data Subjects

```
IMPORTANT: Security Incident Affecting Your Personal Data

Dear [Name/Customer],

WHAT HAPPENED
On [date], we discovered [brief, clear description of the incident -
one or two sentences maximum].

WHAT DATA WAS INVOLVED
The affected information includes:
• [Specific item 1]
• [Specific item 2]
• [Specific item 3]

[If applicable: The following was NOT affected:
(e.g., passwords, payment card numbers)]

WHAT WE ARE DOING
We immediately [containment actions - specific, not vague].

We have also:
• [Mitigation step 1]
• [Mitigation step 2]

We have notified the [relevant supervisory authority] as required by law.

WHAT YOU SHOULD DO
We recommend you take these steps to protect yourself:

1. [Specific action - e.g., "Change your password for this account
   and any other accounts where you used the same password"]
2. [Specific action - e.g., "Monitor your bank statements for
   any unauthorized transactions"]
3. [Specific action - e.g., "Be alert for suspicious emails or calls
   claiming to be from us"]

FOR MORE INFORMATION
If you have questions or concerns, please contact our Data Protection Officer:
Name: [DPO Name]
Email: [DPO Email]
Phone: [DPO Phone]

We sincerely apologize for this incident and any concern it may cause.

[Signature Block]
[Date]
```

---

## 3. Processor Client Notification (Track B)

```
NOTICE OF SECURITY INCIDENT
[Processor Name] → [Controller Name]
Issued pursuant to GDPR Article 33(2) and [DPA Reference]

Date of Notice: [Date]
Incident Reference: [Internal ID]

SUMMARY
We are writing to inform you of a security incident that may have
affected personal data we process on your behalf.

TIMELINE
• [Date/Time]: [Event - first indication]
• [Date/Time]: [Event - confirmation]
• [Date/Time]: [Event - containment]
• [Date/Time]: This notification

INCIDENT DESCRIPTION
[Factual description of what occurred - no speculation]

DATA POTENTIALLY AFFECTED
Based on our investigation, the following categories of data
may have been affected:
• [Category 1]
• [Category 2]

Estimated volume: [Number] records relating to [Number] individuals

ACTIONS TAKEN
We have implemented the following measures:
• [Action 1]
• [Action 2]
• [Action 3]

ASSISTANCE OFFERED
We are prepared to assist your assessment by providing:
• Technical logs and forensic data
• Detailed incident timeline
• Support for your regulatory notification

IMPORTANT DISCLAIMER
As Processor, we provide this information to assist your assessment
under GDPR Article 33. Final risk determination and notification
decisions rest with you as Controller. Any severity indication we
attach (see Handoff Package) is a provisional, informational view
prepared as controller support — it is not binding and does not
constitute our assessment of your notification obligations.

NOTE ON YOUR 72-HOUR CLOCK
Per EDPB Guidelines 9/2022, you as Controller should be considered
"aware" of this breach upon receipt of this notice. Your Art. 33(1)
72-hour period therefore starts now.

CONTACT
[Processor DPO/Security Contact]
[Email]
[Phone]

Available for calls: [Hours/Timezone]
```

**Always accompany this notice with the Processor → Controller Handoff Package (template 13).**

---

## 4. Internal Compliance Log (Art. 33(5))

```
INTERNAL BREACH RECORD
Required under GDPR Article 33(5)

═══════════════════════════════════════════════════════════════
INCIDENT IDENTIFICATION
═══════════════════════════════════════════════════════════════
Incident ID: [Unique identifier]
Date of Record: [Today's date]
Prepared by: [Name, Role]
Approved by: [DPO/Responsible person]

═══════════════════════════════════════════════════════════════
SECTION 1: FACTS OF THE BREACH
═══════════════════════════════════════════════════════════════
Discovery Date/Time: [When first suspected]
Awareness Date/Time (T0): [When reasonable certainty achieved]
T0 Triggering Event: [Specific event that established certainty]
Gap Justification: [If gap > 24h, detailed explanation]

Breach Type(s): [Confidentiality / Integrity / Availability]
Description: [Detailed factual description of what occurred]

═══════════════════════════════════════════════════════════════
SECTION 2: DATA AFFECTED
═══════════════════════════════════════════════════════════════
Categories of Personal Data:
• [Category 1]
• [Category 2]

Volume:
• Approximate Records: [Number]
• Approximate Individuals: [Number]
• Estimation Methodology: [How these numbers were determined]

Special Categories (Art. 9): [Yes/No - if yes, specify]
Vulnerable Subjects: [Yes/No - if yes, specify]

═══════════════════════════════════════════════════════════════
SECTION 3: RISK ASSESSMENT (ENISA METHODOLOGY)
═══════════════════════════════════════════════════════════════
DPC (Data Processing Context):
• Base Category: [Simple/Behavioral/Financial/Sensitive]
• Base Score: [1-4]
• Adjustments Applied: [List with reasoning]
• Final DPC: [Score]

EI (Ease of Identification):
• Identifier Types Present: [List]
• Assessment: [Negligible/Limited/Significant/Maximum]
• Final EI: [0.25/0.50/0.75/1.00]

CB (Circumstances of Breach):
• Confidentiality: [0/+0.25/+0.50] - [Reasoning]
• Integrity: [0/+0.25/+0.50] - [Reasoning]
• Availability: [0/+0.25/+0.50] - [Reasoning]
• Malicious Intent: [0/+0.50] - [Reasoning]
• Total CB: [Sum]

SEVERITY CALCULATION:
SE = (DPC × EI) + CB
SE = ([DPC] × [EI]) + [CB]
SE = [Final Score]

Severity Level: [LOW / MEDIUM / HIGH / VERY HIGH]

LEGAL TEST BRIDGE (Art. 33/34):
• Key facts: [what happened, to whose data, at what scale]
• Safeguards: [in place before / applied after]
• Likely impact on individuals: [likelihood & severity reasoning]
• Art. 33(1) conclusion: [NOTIFY SA / NO — unlikely to result in a
  risk, because ...]
• Art. 34(1) conclusion: [NOTIFY SUBJECTS / NO — no high risk,
  because ... / NO — exception Art. 34(3)(a)/(b)/(c), because ...]
• Divergence from ENISA presumption: [NONE / explained]

EDPB Case Comparison:
• Most Similar Case: [Case XX - Description]
• EDPB Recommendation: [SA: Y/N, Subjects: Y/N]
• Differences from Our Situation: [List]
• Impact on Assessment: [Supports/Requires reconsideration]

═══════════════════════════════════════════════════════════════
SECTION 4: OVERRIDE DOCUMENTATION (IF APPLICABLE)
═══════════════════════════════════════════════════════════════
System-Calculated Verdict: [LEVEL] (SE = [score])
Final Classification Selected: [LEVEL]
Override Applied: [YES/NO]

[If YES:]
• Reason for Override: [Detailed justification]
• Authorized By: [Name, Role]
• Legal Counsel Consulted: [Yes/No - if yes, name]
• Override Timestamp: [Date/Time]

═══════════════════════════════════════════════════════════════
SECTION 5: EFFECTS OF THE BREACH
═══════════════════════════════════════════════════════════════
Actual Impact (Known):
[What has demonstrably occurred]

Potential Impact (Assessed):
[What could reasonably occur based on data exposed]

═══════════════════════════════════════════════════════════════
SECTION 6: REMEDIAL ACTION
═══════════════════════════════════════════════════════════════
Containment Measures:
• [Action 1 - Date/Time]
• [Action 2 - Date/Time]

Mitigation Measures:
• [Action 1 - Date/Time]
• [Action 2 - Date/Time]

Preventive Measures (Future):
• [Planned improvement 1 - Target Date]
• [Planned improvement 2 - Target Date]

═══════════════════════════════════════════════════════════════
SECTION 7: NOTIFICATION DECISIONS
═══════════════════════════════════════════════════════════════
SA Notification:
• Decision: [YES - notified / YES - pending / NO - not required]
• SA(s): [Name(s)]
• Deadline: [Timestamp]
• Submitted: [Date/Time or "Pending"]
• Reference Number: [If received]

Subject Notification:
• Decision: [YES - required / NO - not required]
• Method: [Direct communication / Public announcement / N/A]
• Timing: [Date or "Planned for X"]

═══════════════════════════════════════════════════════════════
SECTION 8: JUSTIFICATION FOR DECISIONS
═══════════════════════════════════════════════════════════════
[If SA notification NOT made:]
This breach is unlikely to result in a risk to the rights and
freedoms of natural persons because:
[Detailed reasoning - multiple paragraphs if needed]

[If Subject notification NOT made:]
This breach is unlikely to result in a HIGH risk to the rights
and freedoms of natural persons because:
[Detailed reasoning]

Encryption Exemption Claimed: [Yes/No]
[If Yes: Algorithm, key status, backup status, confidence level]

═══════════════════════════════════════════════════════════════
SECTION 9: RECORD AUTHENTICATION
═══════════════════════════════════════════════════════════════
Prepared by: [Name] | Role: [Title] | Date: [Date]
Reviewed by: [Name] | Role: [Title] | Date: [Date]
Approved by: [Name] | Role: [Title] | Date: [Date]

Assessment Tool: GDPR Breach Response Sentinel
Guidance Version: EDPB Guidelines 9/2022 v2.0
Methodology: ENISA Severity Assessment v1.0

DISCLAIMER: This assessment was generated with AI assistance and
does not constitute legal advice. Final decisions were made by
the individuals named above.
═══════════════════════════════════════════════════════════════
```

---

## 5. Non-Notification Justification Document

```
BREACH NON-NOTIFICATION JUSTIFICATION
Article 33(1) Assessment Documentation

Date: [Date]
Incident Reference: [ID]
Prepared by: [Name, Role]

═══════════════════════════════════════════════════════════════
DECISION SUMMARY
═══════════════════════════════════════════════════════════════
Decision: NO NOTIFICATION to Supervisory Authority required
Basis: Breach is "unlikely to result in a risk to the rights
and freedoms of natural persons" per Article 33(1)

═══════════════════════════════════════════════════════════════
BREACH SUMMARY
═══════════════════════════════════════════════════════════════
Nature: [Brief description]
Data Categories: [List]
Individuals Affected: [Number]
Breach Type: [C/I/A]

═══════════════════════════════════════════════════════════════
RISK ASSESSMENT
═══════════════════════════════════════════════════════════════
ENISA Severity Score: [Score] (LOW - below threshold of 2)
(The score is decision support; the decision rests on the
Art. 33(1) legal test below.)

DPC: [Score] - [Reasoning]
EI: [Score] - [Reasoning]
CB: [Score] - [Reasoning]

LEGAL TEST BRIDGE (Art. 33(1)):
• Key facts: [summary]
• Safeguards: [in place / applied after]
• Likely impact on individuals: [reasoning]
• Conclusion: the breach is UNLIKELY to result in a risk to the
  rights and freedoms of natural persons, because: [reasoning]

═══════════════════════════════════════════════════════════════
JUSTIFICATION FOR NON-NOTIFICATION
═══════════════════════════════════════════════════════════════
This breach does not require notification because:

1. [Primary reason - e.g., data was encrypted with state-of-the-art
   measures and key was not compromised]

2. [Secondary reason - e.g., data exposed was limited in sensitivity
   and could not be used to identify individuals]

3. [Supporting factor - e.g., no evidence of actual access or
   exfiltration; data was only potentially exposed]

EDPB Case Comparison:
This situation is analogous to EDPB Case [XX], where the
Guidelines concluded notification was not required because [reason].

═══════════════════════════════════════════════════════════════
ATTESTATION
═══════════════════════════════════════════════════════════════
This decision has been reviewed and approved. The internal breach
record required by Article 33(5) has been completed and retained.

Approved by: [DPO Name]
Date: [Date]

This document retained for regulatory audit purposes.
═══════════════════════════════════════════════════════════════
```

---

## 6. Emergency Follow-Up Checklist

```
⚡ EMERGENCY ASSESSMENT - FOLLOW-UP REQUIRED

The following must be completed within 48 hours:

□ Complete full ENISA calculation with proper adjustments
□ Validate T0 establishment with documentation
□ Review Art. 34 subject notification requirement
□ Complete Internal Compliance Log
□ Submit phased notification to SA if new information material
□ Engage legal counsel for review
□ Document any changes to preliminary assessment

Emergency assessment timestamp: [Time]
Follow-up deadline: [Time + 48h]
```

---

## 7. Mitigation Playbook

```
BREACH MITIGATION PLAYBOOK
Incident Reference: [ID]
Generated: [Date/Time]
Breach Summary: [Brief description tailored to this case]

═══════════════════════════════════════════════════════════════
PRIORITIZED ACTION PLAN
═══════════════════════════════════════════════════════════════

Structure this section based on what best fits the incident.
Options: by workstream, by timeline, by system, by stakeholder,
or any combination. Choose the structure that makes the playbook
most actionable for the specific situation.

| # | Action | Rationale | Priority | Owner | Deadline | Dependencies | Status |
|---|--------|-----------|----------|-------|----------|--------------|--------|
| 1 | [Specific action] | [Why this matters for this case] | Critical | [Role] | T0+[X] | [None / Action #X] | ☐ |
| 2 | [Specific action] | [Why this matters for this case] | Critical | [Role] | T0+[X] | [None / Action #X] | ☐ |
| ... | ... | ... | ... | ... | ... | ... | ☐ |

═══════════════════════════════════════════════════════════════
LESSONS LEARNED (TO BE COMPLETED POST-INCIDENT)
═══════════════════════════════════════════════════════════════

What went well:
[To be completed]

What could be improved:
[To be completed]

Systemic changes implemented:
[To be completed]

Sign-off:
Prepared by: [Name] | Date: [Date]
Reviewed by: [Name] | Date: [Date]

---
Assessment generated with GDPR Breach Response Sentinel
This output does not constitute legal advice.
```

---

## 8. Post-Notification Tracker

```
POST-NOTIFICATION CASE TRACKER
Incident Reference: [ID]
Initial Assessment Date: [Date]
Last Updated: [Date]

═══════════════════════════════════════════════════════════════
SA NOTIFICATION STATUS
═══════════════════════════════════════════════════════════════

SA Name: [Name]
Portal Used: [URL]
Reference Number: [If received]

| Milestone | Due Date | Completed | Notes |
|-----------|----------|-----------|-------|
| Initial notification submitted | [Date] | ☐ | |
| SA acknowledgment received | — | ☐ | |
| Supplementary info (if phased) | [Date] | ☐ | |
| SA follow-up inquiry response | [Date] | ☐ | |
| Case closed by SA | — | ☐ | |

═══════════════════════════════════════════════════════════════
DATA SUBJECT NOTIFICATION STATUS
═══════════════════════════════════════════════════════════════

| Milestone | Due Date | Completed | Notes |
|-----------|----------|-----------|-------|
| Communication drafted | [Date] | ☐ | |
| DPO/Legal review | [Date] | ☐ | |
| Communication sent | [Date] | ☐ | |
| Method: [Direct/Public/Both] | — | — | |
| Total subjects notified | — | — | Count: [X] |
| Subject inquiries received | — | — | Count: [X] |
| All inquiries resolved | — | ☐ | |

═══════════════════════════════════════════════════════════════
MITIGATION EXECUTION STATUS
═══════════════════════════════════════════════════════════════

| Phase | Deadline | Status | Completion Date |
|-------|----------|--------|-----------------|
| Phase 1: Immediate Actions | T0 + 4h | ☐ | |
| Phase 2: Technical Measures | T0 + 72h | ☐ | |
| Phase 3: Organizational Measures | T0 + 30d | ☐ | |

═══════════════════════════════════════════════════════════════
DOCUMENTATION COMPLETENESS
═══════════════════════════════════════════════════════════════

| Document | Required | Completed | Location |
|----------|----------|-----------|----------|
| Internal Compliance Log (Art. 33(5)) | YES | ☐ | |
| Art. 33 SA Notification | [YES/NO] | ☐ | |
| Art. 34 Subject Communication | [YES/NO] | ☐ | |
| Non-Notification Justification | [YES/NO] | ☐ | |
| Root Cause Analysis | YES | ☐ | |
| Lessons Learned | YES | ☐ | |
| DPIA Update | [YES/NO] | ☐ | |
| Art. 30 Records Update | [YES/NO] | ☐ | |

═══════════════════════════════════════════════════════════════
CASE STATUS
═══════════════════════════════════════════════════════════════
Overall Status: [ACTIVE / PENDING SA RESPONSE / CLOSED]
Next Action Required: [Description]
Next Deadline: [Date]

Last updated by: [Name] | Date: [Date]

---
Assessment generated with GDPR Breach Response Sentinel
This output does not constitute legal advice.
```

---

## 9. Hybrid Scenario Dashboard (Track A + B)

For **processor-only** (pure Track B) cases, use the Track B block below on its own — the controller-shaped main Assessment Dashboard fields ("Notify SA", 72h clock) are then marked as downstream controller duties, never as the processor's.

```
╔═══════════════════════════════════════════════════════════════╗
║                    TRACK A: INTERNAL DATA                      ║
╠═══════════════════════════════════════════════════════════════╣
║ DPC: [score] - [category + adjustments]                        ║
║ EI:  [score] - [level]                                         ║
║ CB:  [score] - [breakdown]                                     ║
║ SE:  [calculation] = [final]                                   ║
║ Verdict: [LEVEL]                                               ║
║ Override: [None / Original: X, Selected: Y, Reason: Z]         ║
║ SA Deadline: [timestamp]                                       ║
║ Subject Notification: [Required/Not Required]                  ║
╚═══════════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════════╗
║                    TRACK B: CLIENT DATA                        ║
╠═══════════════════════════════════════════════════════════════╣
║ Processor Awareness (T0-P): [timestamp]                        ║
║ Statutory Duty: Notify controller WITHOUT UNDUE DELAY          ║
║   (Art. 33(2)) — no statutory 72h applies to the processor     ║
║ Contractual Deadline: [per client DPA + time remaining]        ║
║ Clients Affected: [list/count]                                 ║
║ Notification Status: [Pending/Sent per client]                 ║
║ Handoff Package: [Complete / items outstanding]                ║
║ Risk Assessment: Informational ENISA view provided as          ║
║   controller support — final Art. 33/34 determination          ║
║   rests with the controller                                    ║
║ Controller 72h Clock: starts when each controller is informed  ║
║   (downstream controller duty, not the processor's)            ║
╚═══════════════════════════════════════════════════════════════╝
```

**Never conflate Track A and Track B documentation.**

---

## 10. Follow-Up Notification (Supplementing or Completing)

```
FOLLOW-UP PERSONAL DATA BREACH NOTIFICATION
Pursuant to Article 33(4) GDPR

Type: FOLLOW-UP — [COMPLETE (closing an incomplete notification) /
                   INCOMPLETE (further supplement to follow)]
ID of previously notified breach: [SA-issued reference]
Controller internal reference: [ID]
Date of this follow-up: [Date]

1. WHAT CHANGED SINCE THE PREVIOUS NOTIFICATION
   [New facts, revised scope, completed forensics — itemised]

2. UPDATED FIELDS
   | Field | Previously reported | Now | Basis for revision |
   |-------|--------------------|----|--------------------|
   | [e.g., subjects affected] | [old] | [new] | [evidence] |

3. UPDATED RISK ASSESSMENT (if changed)
   [Revised ENISA score + revised Art. 33/34 Legal Bridge]

4. UPDATED MEASURES
   [Containment/mitigation/prevention progress since last filing]

5. OUTSTANDING ITEMS (if still incomplete)
   [Open fields + committed timeframe for the next supplement]
```

---

## 11. Withdrawal of a Notification

```
WITHDRAWAL OF PERSONAL DATA BREACH NOTIFICATION

Type: FOLLOW-UP — WITHDRAW
ID of previously notified breach: [SA-issued reference]
Controller internal reference: [ID]
Date: [Date]

REASON FOR WITHDRAWAL
[e.g., duplicate notification; full assessment established that no
personal data breach occurred; completed risk assessment concluded
the breach is unlikely to result in a risk — with reasoning]

SUPPORTING ANALYSIS
• Established facts that changed the assessment: [list with sources]
• Art. 33(1) legal test conclusion: [reasoning]
• Internal record: the Art. 33(5) internal documentation of the
  incident and of this withdrawal decision is retained.

[Note: withdrawal cancels the notification, not the documentation
duty. The internal breach record remains mandatory.]
```

---

## 12. Late Notification Explanation (>72h)

```
REASONS FOR NOTIFICATION AFTER 72 HOURS
Annex to breach notification [reference]

Controller awareness (T0): [timestamp]
Notification filed: [timestamp] ([X] hours after T0)

CHRONOLOGY OF THE DELAY
| From | To | What happened | Why notification was not yet possible |
|------|----|---------------|----------------------------------------|
| [t]  | [t]| [event]       | [reason]                               |

REASONS
[e.g., scope determination required forensic analysis; competing
emergency containment; coordination with law enforcement — be
specific and honest; generic workload arguments will not persuade]

MEASURES TAKEN DURING THE DELAY PERIOD
[Containment and mitigation actions that protected data subjects
while notification was pending]

PROCESS IMPROVEMENT
[What changes prevent recurrence of the delay]
```

---

## 13. Processor → Controller Handoff Package

```
PROCESSOR HANDOFF PACKAGE
[Processor Name] → [Controller Name]
Accompanies the Art. 33(2) notice dated [date] | Reference: [ID]

═══════════════════════════════════════════════════════════════
1. INCIDENT FACTS (established only — assumptions labelled)
═══════════════════════════════════════════════════════════════
• Processor awareness (T0-P): [timestamp + triggering event]
• Nature of the incident: [EDPB taxonomy term + description]
• Cause: [internal/external, malicious/non-malicious, root cause
  if known]
• Systems/services involved: [scoped list with locations]

═══════════════════════════════════════════════════════════════
2. DATA SCOPE (for the controller's risk assessment)
═══════════════════════════════════════════════════════════════
• Data categories affected: [list]
• Data subject categories: [list]
• Records / individuals (estimate + methodology): [numbers]
• Safeguards applied to the data: [encryption status, key status,
  pseudonymisation, access controls]

═══════════════════════════════════════════════════════════════
3. PROVISIONAL INFORMATIONAL RISK VIEW (NON-BINDING)
═══════════════════════════════════════════════════════════════
Provided solely as controller support. The Art. 33/34 assessment
and all notification decisions are the controller's.
• Informational ENISA view: DPC [x] · EI [x] · CB [x] · SE [x]
• Factors the controller will likely weigh: [list]

═══════════════════════════════════════════════════════════════
4. EVIDENCE INVENTORY
═══════════════════════════════════════════════════════════════
• Preserved: [logs, images, access records — with hashes/dates]
• Available on request: [forensic report, timeline exports]
• Not yet available: [items + expected date]

═══════════════════════════════════════════════════════════════
5. WHAT THE CONTROLLER STILL NEEDS TO DO / DECIDE
═══════════════════════════════════════════════════════════════
□ Confirm receipt (starts your Art. 33(1) 72h clock — EDPB
  Guidelines 9/2022)
□ Perform the Art. 33/34 risk assessment (we will support)
□ Decide SA notification + subject communication
□ Tell us which additional artefacts you need, and by when

CONTACTS & AVAILABILITY
[Processor incident lead + DPO, response-time commitment]
```

---

## 14. Art. 34 Decision Memo

```
ARTICLE 34 DECISION MEMO
Communication to data subjects — documented decision
Incident Reference: [ID] | Date: [Date] | Prepared by: [Name, Role]

1. HIGH-RISK ANALYSIS (Art. 34(1))
   [Legal Bridge: facts → safeguards → likely impact →
   "likely to result in a high risk": YES / NO, because ...]

2. EXCEPTIONS CONSIDERED (Art. 34(3)) — all three, in order
   (a) Protection measures applied (e.g., encryption, key secure):
       [AVAILABLE / NOT AVAILABLE — reasoning incl. key status]
   (b) Subsequent measures ensure high risk no longer likely:
       [AVAILABLE / NOT AVAILABLE — measure, evidence it worked]
   (c) Disproportionate effort → public communication instead:
       [APPLICABLE / NOT APPLICABLE — effort comparison; if
       applicable: the equally effective public measure chosen]

3. DECISION
   [COMMUNICATE (direct) / COMMUNICATE (public, under (c)) /
   NO COMMUNICATION — exception (a)/(b) applies]
   Timing: [without undue delay — planned date(s), phasing]

4. STRATEGY (if communicating)
   Channels: [direct/public/both] | Languages: [list]
   Vulnerable subjects prioritised: [how]
   Support channel: [line/mailbox/FAQ + staffing]
   Fraud/phishing warning included: [YES — wording reference]

5. APPROVAL
   DPO: [name/date] | Legal counsel: [name/date or N/A]
   SA backstop noted: the SA may require communication (Art. 34(4)).
```

---

## 15. Attachment Inventory (EDPB Evidence File §7)

```
ATTACHMENT INVENTORY
Incident Reference: [ID] | Compiled: [Date]

| # | Attachment (dated copy of …) | Exists | Date | Location/owner |
|---|------------------------------|--------|------|----------------|
| a | Communication to data subjects | ☐ | | |
| b | Risk assessment | ☐ | | |
| c | Forensic / research report (cyber incidents) | ☐ | | |
| d | Ransomware note | ☐ | | |
| e | Phishing message | ☐ | | |
| f | Internal breach-notification procedure | ☐ | | |
| g | Internal deletion/destruction policy | ☐ | | |
| h | Communication to wrong recipient(s) | ☐ | | |
| i | External notification/message of the breach | ☐ | | |
| j | Other: [specify] | ☐ | | |

Phishing cases — categorise affected communications three ways:
mailbox owner · recipients of the phishing mail · subjects whose
data was inside the compromised mailbox.
```

---

## 16. Country-by-Country Affected Subjects Table

```
AFFECTED DATA SUBJECTS BY COUNTRY
Incident Reference: [ID] | As of: [Date] | Basis: [exact/estimate
+ methodology]

| Country (EEA) | Affected subjects | SA concerned | Notified? |
|---------------|-------------------|--------------|-----------|
| [DE]          | [n]               | [SA name]    | [via lead SA /
|               |                   |              |  direct / date] |
| [FR]          | [n]               | [SA name]    | [...]     |
| TOTAL         | [n]               |              |           |

One-stop-shop: [YES — lead SA [name]; concerned SAs informed via
cooperation / NO — non-EU controller: each SA notified directly]
```

---

## 17. Other-Authority Notification Log

```
OTHER AUTHORITIES & BODIES — NOTIFICATION LOG
Incident Reference: [ID]

| Authority/Body | Regime | Required/Voluntary | Deadline | Notified
  (date) | Their case ID |
|----------------|--------|--------------------|----------|---------|---|
| [Police/prosecutor] | Criminal | Voluntary | — | | |
| [National cyber security centre / CSIRT] | NIS2 | [Required?] |
  [24h/72h] | | |
| [Financial supervisor] | DORA | [Required?] | [...] | | |
| [Market surveillance authority] | AI Act Art. 73 | [Required?
  from 2026-08-02] | [15d/10d/2d] | | |
| [Insurer] | Policy | Contractual | [window] | | |

Feed completed rows into §6.1 of the EDPB evidence file.
```
