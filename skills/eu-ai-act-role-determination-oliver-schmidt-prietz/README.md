# EU AI Act Role Determination — Deployment Guide

> 📄 **[View the interactive skill page →](https://oliverschmidtprietz.github.io/EU-AI-Act-Suite/ai-act-roles/)**

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Overview

EU AI Act Role Determination — determines the organisation's role in the AI value chain and assesses quasi-provider risk:

- **Primary role determination** — provider, deployer, importer, distributor
- **Quasi-provider risk assessment (Art. 25)** — substantial modification, rebranding, intended-purpose change, high-risk repurposing
- **Visual decision trees** for primary role and quasi-provider triggers
- **Fine-tuning assessment** — when does fine-tuning a GPAI model trigger quasi-provider obligations?
- **Substantial modification analysis** per Art. 3(23) and Commission guidance
- **Value chain obligation mapping** — which obligations attach to which role
- **Employment-law overlay** for HR/workforce AI deployments
- **Sector guidance cross-reference** for sector-specific role nuances
- **Role Determination Dashboard** output with legal basis and follow-up actions

## File Structure

```
ai-act-roles/
├── SKILL.md                              # Main skill instructions (deploy this)
├── CHANGELOG.md                          # Version history
├── evals/
│   └── evals.json                        # Test cases
└── references/
    ├── role-definitions.md               # Provider, deployer, importer, distributor — Art. 3 definitions
    ├── substantial-modification.md       # Art. 3(23) substantial-modification analysis
    ├── quasi-provider-scenarios.md       # Art. 25 trigger scenarios
    ├── finetuning-assessment.md          # When fine-tuning becomes substantial modification
    ├── value-chain-obligations.md        # Obligation map per role
    ├── compliance-deadlines.md           # Deadline anchors per role
    ├── employment-law-overlay.md         # HR/workforce-specific overlay
    ├── sector-guidance-crossref.md       # Sector-specific role considerations
    └── case-studies.md                   # Worked role-determination examples
```

## Deployment

### Claude.ai (User Skills)

1. Go to **Settings → Profile → Custom Skills** (or equivalent)
2. Upload the entire `ai-act-roles/` folder structure
3. The skill will auto-trigger on "AI Act role", "provider vs deployer", "quasi-provider", "Art. 25", "substantial modification", or "Anbieter / Betreiber"

### Claude Code / Custom MCP Setup

1. Copy the `ai-act-roles/` folder to your skills directory:
   ```bash
   cp -r ai-act-roles/ /path/to/your/skills/user/ai-act-roles/
   ```
2. Ensure the skill is registered in your configuration

## Usage

### Quick Start

Describe what your organisation does with the AI:

> "We're a German bank. We licensed an off-the-shelf credit-scoring model from
> a US vendor, fine-tuned it on our own data, and rebranded the output for our
> customers. Are we the provider, deployer, or quasi-provider?"

The skill will walk through primary-role and quasi-provider trees.

### Trigger Phrases

- "Determine AI Act role" / "Provider or deployer?" / "Are we the deployer?"
- "Quasi-provider" / "Art. 25" / "Substantial modification" / "Wesentliche Veränderung"
- "Value chain responsibilities" / "Anbieter" / "Betreiber"
- "Does fine-tuning make us the provider?"

### Workflow

| Phase | Description |
|-------|-------------|
| **Phase 1: Context Gathering** | Adaptive intake — what the organisation does with the AI, source/origin of the system |
| **Phase 2: Primary Role Determination** | Visual decision tree — provider / deployer / importer / distributor |
| **Phase 3: Quasi-Provider Risk Assessment (Art. 25)** | Trigger assessment tree — substantial modification, rebranding, purpose change, high-risk repurposing |
| **Phase 4: Role Determination Dashboard** | Output: primary role + quasi-provider verdict + legal basis + obligations preview |

## Capabilities Summary

| Feature | Description |
|---------|-------------|
| Primary Role Determination | Provider, deployer, importer, distributor — visual decision tree |
| Quasi-Provider Assessment | Art. 25 trigger tree (substantial modification, rebranding, purpose change, high-risk repurposing) |
| Fine-Tuning Analysis | When fine-tuning a GPAI model becomes substantial modification |
| Substantial Modification | Art. 3(23) analysis with Commission guidance |
| Value Chain Mapping | Obligations per role, feeding into obligation mapping |
| Employment-Law Overlay | HR/workforce-specific role considerations |
| Sector Cross-References | Sector-specific role nuances |
| Role Dashboard | Single-page output with verdict + legal basis + next steps |

## Regulatory Basis

| Document | Reference |
|----------|-----------|
| EU AI Act | Regulation (EU) 2024/1689 |
| Art. 3 | Definitions — provider, deployer, importer, distributor |
| Art. 3(23) | Substantial modification definition |
| Art. 25 | Responsibilities along the AI value chain (quasi-provider) |
| Commission Value Chain Guidance | Quasi-provider trigger interpretation |
| Art. 16, 26 | Obligations per primary role |

## License & Disclaimer

This skill provides structured AI Act role-determination guidance based on Regulation (EU) 2024/1689 and Commission value chain guidance. It is not legal advice. Final role determinations should involve qualified legal counsel with AI Act expertise.

Licensed under AGPL-3.0.

> **Quality assurance:** this skill ships with evaluation tests in the `evals/` folder, which I run to check its outputs against expected results.

---

*Created by Oliver Schmidt-Prietz — [OneZero Legal](https://onezero.legal)*
