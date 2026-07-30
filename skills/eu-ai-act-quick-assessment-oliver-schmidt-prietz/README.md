# EU AI Act Quick Assessment — Deployment Guide

> 📄 **[View the interactive skill page →](https://oliverschmidtprietz.github.io/EU-AI-Act-Suite/ai-act-quick/)**

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Overview

EU AI Act Quick Assessment — fast 15–25 minute triage for preliminary classification:

- **Adaptive 2-batch intake** — minimal questions, system-description-informed
- **6-step gate sequence** — scope, AI-system test, prohibited, Annex I, Annex III, GPAI
- **Preliminary classification output** with confidence level
- **Compliance deadlines** for the identified tier
- **Jurisdiction flags** highlighting Member-State-specific considerations
- **Template offer** — option to escalate to a full assessment (classification, role determination, obligation mapping, formal report)
- **Clear scope boundary** — designed for triage, not final determination

## File Structure

```
ai-act-quick/
├── SKILL.md                              # Main skill instructions (deploy this)
├── CHANGELOG.md                          # Version history
├── evals/
│   └── evals.json                        # Test cases
└── references/
    ├── quick-decision-tree.md            # 6-step gate sequence
    ├── compliance-deadlines.md           # Tier-by-tier deadline lookup
    └── jurisdiction-flags.md             # Member State-specific flags
```

## Deployment

### Claude.ai (User Skills)

1. Go to **Settings → Profile → Custom Skills** (or equivalent)
2. Upload the entire `ai-act-quick/` folder structure
3. The skill will auto-trigger on "quick AI Act check", "preliminary assessment", "Schnellprüfung", or "Ersteinschätzung"

### Claude Code / Custom MCP Setup

1. Copy the `ai-act-quick/` folder to your skills directory:
   ```bash
   cp -r ai-act-quick/ /path/to/your/skills/user/ai-act-quick/
   ```
2. Ensure the skill is registered in your configuration

## Usage

### Quick Start

Dump what you know about the system:

> "Quick AI Act check please — we're a SaaS in Berlin selling a meeting-summary
> tool that transcribes calls and produces action items using GPT-4. Customers
> are EU businesses. Does the AI Act apply, and what tier?"

The skill will run a 15–25 minute triage and return a preliminary verdict with confidence.

### Trigger Phrases

- "Quick AI Act assessment" / "Preliminary check" / "Does the AI Act apply?"
- "Schnellprüfung" / "Ersteinschätzung" / "AI Act triage"
- "Run a quick classification"

### Workflow

| Phase | Description |
|-------|-------------|
| **Phase 1: Quick Context** | Adaptive 2-batch intake (system description + role/jurisdiction) |
| **Phase 2: Rapid Classification** | 6-step gate sequence — scope, AI-system, prohibited, Annex I, Annex III, GPAI |
| **Phase 3: Preliminary Output** | Tier verdict + confidence + jurisdiction flags + deadlines |
| **Phase 4: Template Offer** | Optional escalation to a full assessment (classification, role determination, obligation mapping, formal report) |

## Capabilities Summary

| Feature | Description |
|---------|-------------|
| Adaptive Intake | Description-informed minimal-question flow (2 batches) |
| 6-Step Gate | Scope → AI-system → prohibited → Annex I → Annex III → GPAI |
| Confidence Tagging | Each verdict carries a HIGH / MEDIUM / LOW confidence indicator |
| Deadline Lookup | Tier-specific compliance dates |
| Jurisdiction Flags | Member-State-specific signals (BSI / CNIL / Garante / etc.) |
| Escalation | Smooth escalation to a full assessment (classification, role determination, obligation mapping, report) |
| Scope Discipline | Outputs explicitly marked PRELIMINARY — not a substitute for full assessment |

## Regulatory Basis

| Document | Reference |
|----------|-----------|
| EU AI Act | Regulation (EU) 2024/1689 |
| Art. 5 / Annex I / Annex III | Risk-tier classification anchors |
| Art. 51 / 53 / 55 | GPAI thresholds and obligations |
| Compliance deadlines | Title XIII + Commission implementation timeline |

## License & Disclaimer

This is a preliminary AI Act assessment based on Regulation (EU) 2024/1689, designed for rapid triage. It is not legal advice and does not replace a full assessment — validate results with a full risk-tier classification, role determination, obligation mapping, formal report, and qualified legal counsel.

Licensed under AGPL-3.0.

> **Quality assurance:** this skill ships with evaluation tests in the `evals/` folder, which I run to check its outputs against expected results.

---

*Created by Oliver Schmidt-Prietz — [OneZero Legal](https://onezero.legal)*
