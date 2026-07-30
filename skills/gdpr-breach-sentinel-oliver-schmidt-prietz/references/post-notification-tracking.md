# Post-Notification Tracking

After the initial assessment and notification, the skill supports ongoing case management.

## Tracking Dashboard

```
╔══════════════════════════════════════════════════════════════╗
║              POST-NOTIFICATION TRACKER                        ║
╠══════════════════════════════════════════════════════════════╣
║ Incident Reference: [ID]                                     ║
║ Date of Initial Assessment: [Date]                           ║
╠══════════════════════════════════════════════════════════════╣
║ SA NOTIFICATION                                              ║
║ ☐ Initial notification submitted    Due: [Date] Status: [ ]  ║
║   Type: [New — Complete / New — Incomplete (phased)]         ║
║ ☐ SA acknowledgment received        Status: [ ]              ║
║ ☐ Follow-up notification sent       Due: [Date] Status: [ ]  ║
║   (completing/amending — reference prior notification ID)    ║
║ ☐ Withdrawal filed (if applicable)  Date: [ ] Reason: [ ]    ║
║ ☐ SA inquiry response (if any)      Due: [Date] Status: [ ]  ║
╠══════════════════════════════════════════════════════════════╣
║ DATA SUBJECT NOTIFICATION                                    ║
║ ☐ Communication drafted             Status: [ ]              ║
║ ☐ Communication sent                Date: [ ]                ║
║ ☐ Subject inquiries tracked         Count: [ ]               ║
╠══════════════════════════════════════════════════════════════╣
║ MITIGATION EXECUTION                                         ║
║ ☐ Phase 1 (Immediate) complete      Due: T0+4h   Status: [ ]║
║ ☐ Phase 2 (Technical) complete      Due: T0+72h  Status: [ ]║
║ ☐ Phase 3 (Organizational) complete Due: T0+30d  Status: [ ]║
╠══════════════════════════════════════════════════════════════╣
║ DOCUMENTATION                                                ║
║ ☐ Internal Compliance Log finalized Status: [ ]              ║
║ ☐ Root cause analysis completed     Status: [ ]              ║
║ ☐ Lessons learned documented        Status: [ ]              ║
║ ☐ DPIA update (if required)         Status: [ ]              ║
║ ☐ Art. 30 records updated           Status: [ ]              ║
╚══════════════════════════════════════════════════════════════╝
```

## Follow-Up Prompts

At the end of each session, remind the user:
- "Would you like me to generate any documentation as .docx files?"
- "Do you need me to research your specific SA's notification portal and requirements?"
- "Would you like to update the post-notification tracker?"
