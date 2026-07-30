# TSA Cybersecurity Incident Reporting — Procedures and Requirements

Source: TSA Security Directives; CISA guidance; Federal Register notices

---

## 24-Hour Reporting Obligation

All covered entities under any TSA cybersecurity Security Directive are required to report cybersecurity incidents to **CISA within 24 hours** of identifying an incident. This is a **hard deadline** — the clock starts when the entity identifies the incident, not when the investigation is complete.

**Key principle**: Report early with limited information. TSA and CISA do not expect a complete investigation before the initial report. Updates are provided as the investigation progresses.

---

## What Qualifies as a Reportable Incident

A cybersecurity incident is reportable if it results in — or is reasonably likely to result in — operational disruption, safety impact, or unauthorised access involving a Critical Cyber System (CCS).

**Definite reportable incidents:**
- Ransomware infection confirmed on IT or OT systems
- Unauthorised access confirmed to any CCS
- Malware detected on CCS (even if contained)
- Denial of service that impacts operational capability
- Confirmed phishing attack with resultant system access
- Insider threat with confirmed access to CCS
- Physical security breach resulting in suspected cyber access
- Loss or suspected loss of operational control of OT systems
- Detection of reconnaissance activity specifically targeting CCS

**Potentially reportable (apply judgement; when in doubt, report):**
- Phishing with credential theft (no confirmed CCS access yet)
- Suspicious login attempts with partial success indicators
- Discovery of unknown devices on OT network segments
- Evidence of lateral movement in IT with potential path to OT
- Vendor notification of a breach affecting systems they manage for you

**Not reportable (generally):**
- Spam email with no credential compromise
- Blocked phishing attempt (no access)
- Routine vulnerability scan activity from authorised ASV/pen test firm
- Failed brute-force with no account compromise

---

## How to Report to CISA

### CISA Reporting Channels (24/7)

| Channel | Contact |
|---------|---------|
| **Phone** | 1-888-282-0870 (CISA 24/7 Operations Center) |
| **Email** | CISAgov@mail.dhs.gov |
| **Online** | https://myservices.cisa.gov/report (CISA Reporting Portal) |

### TSA Notification
In addition to CISA, notify TSA via the TSA Operations Center:
- **TSA Operations Center**: 1-866-289-9673

### Internal Notification Sequence
Before or concurrent with CISA reporting:
1. Cybersecurity Coordinator notified immediately upon incident identification
2. Cybersecurity Coordinator notifies Accountable Executive
3. Legal counsel notified (regulatory reporting obligations)
4. OT operations team notified if OT systems involved
5. CISA report made within 24 hours
6. TSA notification made per directive requirements

---

## Initial Report — Minimum Required Information

The initial 24-hour report should include as much of the following as available. Missing information can be provided in follow-up reports.

**Required fields for initial report:**
- Organisation name and sector (pipeline, freight rail, transit, etc.)
- Contact name and phone number (Cybersecurity Coordinator)
- Date and approximate time incident was identified
- Brief description of what was observed
- Systems affected (IT, OT, or both — be as specific as safe to share)
- Operational impact (disruption to operations? estimated scope)
- Containment actions taken so far
- Whether law enforcement has been notified (FBI, etc.)

**Sample initial report language:**
> "[Organisation Name], a [natural gas pipeline / freight railroad / transit agency] operator, is reporting a cybersecurity incident identified on [date/time]. We detected [ransomware/unauthorised access/malware] on [IT systems / OT control systems / both]. At this time, [describe operational impact]. We have taken [initial containment actions]. Our Cybersecurity Coordinator is [Name] and can be reached at [phone]. We will provide updates as our investigation progresses."

---

## Follow-Up Reporting

After the initial 24-hour report, maintain regular communication with CISA and TSA as the investigation develops:

**Follow-up report triggers:**
- Identification of root cause
- Significant change in scope (more systems affected than initially reported)
- Significant operational impact change
- Recovery milestones reached
- Incident closure

**Incident closure report should include:**
- Timeline from detection to containment to eradication to recovery
- Root cause analysis
- Systems affected (final scope)
- Data involved (any cardholder data, PII, operational data)
- Actions taken (containment, eradication, recovery)
- Lessons learned
- Corrective actions planned or implemented to prevent recurrence

---

## CIRB (Cyber Incident Response Board) and External Assistance

If the incident is significant, CISA may:
- Dispatch a CISA Rapid Response Team (CISA has dedicated ICS/OT responders)
- Coordinate with FBI Cyber Division if criminal activity suspected
- Share sanitised threat intelligence with other critical infrastructure operators via ISACs

**Free CISA services available to covered entities:**
- Incident response support (CIRP assistance, forensics support)
- Cybersecurity advisory services
- Vulnerability scanning (CISA CSET — Cybersecurity Evaluation Tool)
- Exercises (tabletop exercise facilitation)
- Threat intelligence (CISA advisories, ICS-CERT alerts)

---

## Sector-Specific ISACs

Information Sharing and Analysis Centers (ISACs) provide sector-specific threat intelligence and incident coordination:

| Sector | ISAC | Website |
|--------|------|---------|
| Pipeline / Energy | E-ISAC (Energy ISAC) | https://www.eisac.com |
| Oil and Natural Gas | ONG-ISAC | https://www.ongisac.org |
| Rail / Surface Transportation | Surface Transportation ISAC (ST-ISAC) | https://www.surfacetransportationisac.org |
| Public Transit | PT-ISAC | https://www.pt-isac.org |
| Multi-sector | MS-ISAC (focused on SLTT) | https://www.cisecurity.org/ms-isac |

ISAC membership is strongly encouraged by TSA and CISA. Incidents can be reported to ISACs for anonymised sharing with sector peers.

---

## Post-Incident IRP Testing Requirement

Following a significant cybersecurity incident, covered entities should:
1. Conduct an after-action review (AAR) within 30 days of incident closure
2. Document lessons learned
3. Update the IRP to reflect lessons learned
4. Update the CIP if architectural or procedural changes are required
5. Consider whether the incident warrants unscheduled IRP testing (e.g., drill on the specific scenario that occurred)
6. Track corrective actions to closure

The annual IRP testing requirement (test two objectives) does not reset due to a real incident — a real incident response may count as a test if properly documented.

---

## Cyber Incident Notification Log

Maintain a log of all regulatory notifications made for each incident. Recommended fields:

| Field | Example |
|-------|---------|
| Incident ID | INC-2026-001 |
| Date/time identified | 2026-03-10 14:32 UTC |
| Date/time CISA notified | 2026-03-11 09:15 UTC (within 24h ✅) |
| CISA ticket/case number | CISA-2026-XXXXX |
| Date/time TSA notified | 2026-03-11 09:30 UTC |
| TSA case reference | TSA-XXXX |
| Date/time law enforcement notified | N/A or 2026-03-11 |
| Internal legal counsel notified | 2026-03-10 15:00 UTC |
| Accountable Executive notified | 2026-03-10 14:45 UTC |
| Follow-up reports submitted | 2026-03-15, 2026-03-22 |
| Incident closure date | 2026-03-25 |
| Closure report submitted to CISA | 2026-03-30 |

---

## CIRPA — Cyber Incident Reporting for Critical Infrastructure Act

In addition to TSA-specific reporting, large-scale incidents may also trigger reporting obligations under **CIRCIA (Cyber Incident Reporting for Critical Infrastructure Act of 2022)**:

- CIRCIA requires covered entities to report significant cyber incidents to CISA within **72 hours** (broader trigger than TSA's 24-hour requirement)
- Ransom payments must be reported within **24 hours** under CIRCIA
- TSA's 24-hour requirement is more stringent — complying with TSA also satisfies CIRCIA timelines
- CIRCIA final rules were under development as of 2025/2026; interim guidance from CISA applies

**Practical guidance**: When in doubt, report to CISA as early as possible. TSA's 24-hour requirement is the most demanding — use it as your reporting trigger.
