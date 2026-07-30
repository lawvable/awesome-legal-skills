# EU AI Act Obligations Mapper — Deployment Guide

> 📄 **[View the interactive skill page →](https://oliverschmidtprietz.github.io/EU-AI-Act-Suite/ai-act-obligations/)**

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Overview

EU AI Act Obligations Mapper — produces an actionable compliance matrix for a given role + risk tier:

- **Role × tier obligation matrix** — provider, deployer, importer, distributor across prohibited, high-risk, GPAI, Art. 50, minimal
- **RACI assignments** for each obligation (Responsible / Accountable / Consulted / Informed)
- **Implementation priorities** sequenced against compliance deadlines
- **Technical measures** — risk management, data governance, logging, transparency, human oversight, accuracy/robustness, cybersecurity
- **Organisational measures** — quality management, post-market monitoring, incident reporting, conformity assessment
- **Management systems** — what is required (e.g., Art. 17 QMS) vs. recommended
- **Impact assessments** required (DPIA, FRIA, conformity assessment) with cross-references
- **GDPR crosswalk** — overlap and interplay between AI Act and GDPR obligations
- **Regulatory overlays** — sector-specific layers (banking, medical devices, employment)
- **Art. 6(4) documentation** support for Art. 6(3)-exception users
- **EU database registration** workflow for Annex III high-risk systems
- **Compliance roadmap** with priority decision tree

## File Structure

```
ai-act-obligations/
├── SKILL.md                                  # Main skill instructions (deploy this)
├── CHANGELOG.md                              # Version history
├── evals/
│   └── evals.json                            # Test cases
└── references/
    ├── high-risk-provider-obligations.md     # Art. 16, 9, 10, 11, 12, 13, 14, 15
    ├── high-risk-deployer-obligations.md     # Art. 26, 27 (FRIA)
    ├── gpai-obligations.md                   # Art. 53, 55, Code of Practice
    ├── low-risk-obligations.md               # Art. 50 transparency + voluntary measures
    ├── technical-measures.md                 # Risk mgmt, data governance, logging, etc.
    ├── organizational-measures.md            # QMS, post-market monitoring, incident reporting
    ├── management-systems.md                 # Art. 17 QMS specifics
    ├── conformity-assessment.md              # Annex VI/VII procedures
    ├── post-market-monitoring.md             # Art. 72 post-market system
    ├── eu-database-registration.md           # Art. 71 EU database workflow
    ├── art6-4-documentation.md               # Art. 6(4) exception documentation
    ├── fria-template.md                      # Fundamental Rights Impact Assessment scaffold
    ├── gdpr-crosswalk.md                     # AI Act ↔ GDPR mapping
    ├── regulatory-overlays.md                # Sector-specific compliance layers
    ├── compliance-roadmap.md                 # Priority decision tree + sequencing
    └── case-studies.md                       # Worked obligation-mapping examples
```

## Deployment

### Claude.ai (User Skills)

1. Go to **Settings → Profile → Custom Skills** (or equivalent)
2. Upload the entire `ai-act-obligations/` folder structure
3. The skill will auto-trigger when you ask to map obligations, build a compliance checklist, or assess provider/deployer duties under the AI Act

### Claude Code / Custom MCP Setup

1. Copy the `ai-act-obligations/` folder to your skills directory:
   ```bash
   cp -r ai-act-obligations/ /path/to/your/skills/user/ai-act-obligations/
   ```
2. Ensure the skill is registered in your configuration

## Usage

### Quick Start

Tell the skill your role and risk tier (or just describe the system):

> "We're the deployer of a high-risk AI system used for credit scoring in
> Germany. What obligations do we have, and what should we prioritise in
> the first 6 months?"

The skill will produce a tailored obligation matrix with RACI and priorities.

### Trigger Phrases

- "Map AI Act obligations" / "Check what we need to do" / "Compliance checklist"
- "Deployer obligations" / "Provider duties" / "Art. 26" / "Art. 16-17"
- "AI literacy Art. 4" / "DPIA" / "FRIA" / "fundamental rights assessment"
- "Pflichtenkatalog"

### Workflow

| Phase | Description |
|-------|-------------|
| **Phase 1: Input Context** | Context-aware adaptive intake — role, risk tier, sector, jurisdiction; consumes prior skill output if provided |
| **Phase 2: Obligation Mapping** | Tier-specific obligation list with priority decision tree |
| **Phase 3: Implementation Roadmap** | Sequenced plan against deadlines with quick-win identification |
| **Phase 4: Obligations Matrix Output** | RACI-tagged matrix: technical measures, organisational measures, management systems, impact assessments, GDPR cross-refs |

## Capabilities Summary

| Feature | Description |
|---------|-------------|
| Role × Tier Matrix | All combinations (provider/deployer/importer/distributor × prohibited/high-risk/GPAI/Art. 50/minimal) |
| RACI Assignments | Per-obligation R/A/C/I tagging |
| Technical Measures | Art. 9, 10, 11, 12, 13, 14, 15 implementation guidance |
| Organisational Measures | Art. 17 QMS, post-market monitoring, incident reporting |
| Conformity Assessment | Annex VI / VII procedure routing |
| EU Database Registration | Art. 71 high-risk system registration |
| FRIA Support | Art. 27 fundamental rights impact assessment scaffold |
| GDPR Crosswalk | Mapping to GDPR obligations (DPIA, controller/processor) |
| Sector Overlays | Banking, medical devices, employment, biometrics |
| Compliance Roadmap | Priority decision tree + deadline-aware sequencing |

## Regulatory Basis

| Document | Reference |
|----------|-----------|
| EU AI Act | Regulation (EU) 2024/1689 — Titles III, IV, V |
| Art. 9–15 | Technical requirements for high-risk systems |
| Art. 16–17 | Provider obligations + QMS |
| Art. 26–27 | Deployer obligations + FRIA |
| Art. 50 | Transparency obligations |
| Art. 53, 55 | GPAI obligations (standard + systemic risk) |
| Art. 71 | EU database registration |
| Art. 72 | Post-market monitoring |
| GPAI Code of Practice | Art. 53 implementation framework |
| GDPR | Crosswalk for DPIA + controller/processor obligations |

## License & Disclaimer

This skill provides structured AI Act obligations guidance based on Regulation (EU) 2024/1689. It is not legal advice. Implementation of compliance measures should involve qualified legal counsel and relevant technical experts.

Licensed under AGPL-3.0.

> **Quality assurance:** this skill ships with evaluation tests in the `evals/` folder, which I run to check its outputs against expected results.

---

*Created by Oliver Schmidt-Prietz — [OneZero Legal](https://onezero.legal)*
