# Breach Sentinel — Deployment Guide

> 📄 **[View the interactive skill page →](https://oliverschmidtprietz.github.io/GDPR-Breach-Sentinel/)**

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Overview

GDPR Breach Response Sentinel — an advanced incident response skill for Claude that provides:

- **Breach qualification triage** — "is this even a personal data breach?" gate before the workflow
- **ENISA severity assessment** with borderline score analysis, bridged to the Art. 33/34 statutory legal tests
- **EDPB-template-aligned breach evidence file** mirroring the EDPB Template [2026] for breach notification (draft, public consultation)
- **EDPB case matching** against 18 documented breach scenarios (as analogies, with limits stated)
- **Dedicated Art. 34 decision module** — high-risk test, all three Art. 34(3) exceptions, communication strategy
- **Strategic case advisory** — senior counsel-level analysis and recommendations
- **Dynamic web research** for enforcement precedents and SA-specific guidance, with source discipline
- **Flexible mitigation playbooks** tailored to the specific incident
- **SA contact directory** with jurisdiction-specific portal lookup
- **AI Act Art. 73 intersection** for breaches involving high-risk AI systems
- **Sectoral parallel-regime screen** (NIS2, DORA, eIDAS, ePrivacy, insurance, works council)
- **Audit-ready .docx document generation** (evidence file, Art. 33, Art. 34, compliance logs, follow-up/withdrawal, etc.)
- **Post-notification case tracking**
- **Processor track done right** — notify controller without undue delay (Art. 33(2)), contractual DPA windows, handoff package; no phantom 72h processor deadline

## File Structure

```
breach-sentinel/
├── SKILL.md                              # Main skill instructions (deploy this)
├── evals/
│   └── evals.json                        # 13 test cases, 132 assertions
└── references/
    ├── enisa-methodology.md              # ENISA scoring tables, legal bridge, worked examples
    ├── edpb-template-evidence-file.md    # EDPB Template [2026] field map + evidence file builder
    ├── art34-communication.md            # Art. 34 decision framework incl. all 34(3) exceptions
    ├── parallel-regimes.md               # AI Act Art. 73 depth + NIS2/DORA/eIDAS/etc. screen
    ├── edpb-cases.md                     # 18 EDPB breach case scenarios + analogy rules
    ├── templates.md                      # 17 document templates (Art. 33/34, handoff, follow-up …)
    ├── strategic-advisory.md             # Advisory framework, principles, tone examples
    ├── mitigation-playbook.md            # Design principles, output format, action categories
    ├── post-notification-tracking.md     # Tracking dashboard template
    └── web-research.md                   # Search query templates, source discipline, DE routing
```

## Deployment

### Claude.ai (User Skills)

1. Go to **Settings → Profile → Custom Skills** (or equivalent)
2. Upload the entire `breach-sentinel/` folder structure
3. The skill will auto-trigger when you mention data breaches, Art. 33/34, "Datenpanne", or related topics

### Claude Code / Custom MCP Setup

1. Copy the `breach-sentinel/` folder to your skills directory:
   ```bash
   cp -r breach-sentinel/ /path/to/your/skills/user/breach-sentinel/
   ```
2. Ensure the skill is registered in your configuration

## Usage

### Quick Start

Just tell Claude about a breach:

> "We just discovered that an external attacker exfiltrated our customer database. 
> About 2,000 records with names, emails, and payment data. We're based in Munich. 
> This happened yesterday at 3pm."

The skill will activate and walk you through the assessment.

### Trigger Phrases

- "We had a data breach" / "Datenpanne" / "Datenschutzverletzung"
- "Do we need to notify the SA?" / "72 hours" / "Art. 33"
- "Help me assess this breach" / "ENISA assessment"
- "Generate breach notification documents"

### Modes

| Mode | When to Use |
|------|-------------|
| **Guided** | You're unsure about details; skill asks questions one by one |
| **Fast Path** | You have all the facts; dump them and get an instant assessment |
| **Emergency** | <12 hours remaining on notification clock |

## Capabilities Summary

| Feature | Description |
|---------|-------------|
| Breach Qualification Triage | Gate before the workflow: security incident vs. personal data breach (Art. 4(12)) |
| ENISA Severity Calculation | Full SE = (DPC × EI) + CB with contextual adjustments — as decision support |
| Art. 33/34 Legal Bridge | Written bridge from score → facts → safeguards → statutory conclusions in every assessment |
| EDPB Evidence File | Filled dossier mirroring the EDPB Template [2026] (draft) — all 7 sections, portal-ready |
| Art. 34 Decision Module | High-risk test, exceptions 34(3)(a)/(b)/(c), communication strategy, decision memo |
| Evidence Posture | Facts / assumptions / unknowns discipline with confidence level in every assessment |
| Borderline Score Analysis | Extra scrutiny for scores near 2.0/3.0/4.0 thresholds |
| EDPB Case Matching | Maps to 18 documented scenarios from Guidelines 01/2021 — as analogies with stated limits |
| Strategic Advisory | Senior counsel-level analysis: hidden risks, SA strategy, leverage points |
| Dynamic Web Research | Current enforcement precedents and SA guidance, with source discipline rules |
| SA Contact Lookup | Finds notification portal URLs and jurisdiction-specific requirements |
| Germany SA Routing | Correctly routes to BfDI vs. LfDI/LDA based on entity type |
| Mitigation Playbook | Case-specific, flexibly structured action plan with owners and deadlines |
| AI Act Integration | Art. 73 serious incident screening (definition, deadlines, applicability) for AI breaches |
| Parallel-Regime Screen | NIS2, DORA, eIDAS, ePrivacy, criminal, insurance, contractual, works council |
| Processor Track | Art. 33(2) without-undue-delay duty, contractual DPA windows, handoff package |
| Document Generation | Audit-ready .docx files — 17 templates incl. follow-up, withdrawal, late-notification |
| Post-Notification Tracking | Ongoing case management dashboard incl. follow-up and withdrawal milestones |

## Regulatory Basis

| Document | Reference |
|----------|-----------|
| GDPR Articles 33 & 34 | Breach notification obligations |
| EDPB Guidelines 9/2022 v2.0 | Personal data breach notification |
| EDPB Guidelines 01/2021 v2.0 | Examples regarding breach notification |
| EDPB Template [2026] v1.0 | Personal data breach notification template — DRAFT, public consultation until 5 Aug 2026 |
| ENISA Severity Methodology | Risk assessment formula and scoring |
| EU AI Act (Reg. 2024/1689) | Art. 73 serious incident reporting (applies from 2 Aug 2026) |

## License & Disclaimer

This skill provides guidance based on publicly available GDPR regulatory materials. It does not constitute legal advice. All notification decisions should involve qualified legal counsel and your organization's DPO.

---

*Created by Oliver Schmidt-Prietz — OneZero Legal
