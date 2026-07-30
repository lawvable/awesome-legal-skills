# NIS2 Compliance Navigator — Deployment Guide

> 📄 **[View the interactive skill page →](https://oliverschmidtprietz.github.io/NIS2-Navigator/)**

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Overview

NIS2 Compliance Navigator — scope classification, Art. 21 gap analysis, and compliance roadmap under EU Directive 2022/2555:

- **Scope & classification** — Annex I / Annex II + essential vs. important entity determination
- **Art. 21 gap analysis** with 0–4 maturity scoring across the 10 risk-management measures
- **ISO 27001 cross-references** for each measure to leverage existing certification work
- **Compliance roadmap** with prioritisation framework (legal exposure, dependency, quick wins)
- **Deep German BSIG-neu coverage** — § 30 BSIG registration, NIS2UmsuCG specifics
- **Profiles for IT, FR, NL, AT, ES** — country-specific entity-type taxonomies and supervisory authorities
- **Management briefing template** (Art. 20 / § 38 BSIG) for board-level liability
- **Incident reporting framework** with timelines and escalation paths
- **Supply chain security** considerations integrated throughout
- **Final assessment report** consolidating scope, gaps, and roadmap

## File Structure

```
nis2-navigator/
├── SKILL.md                              # Main skill instructions (deploy this)
├── CHANGELOG.md                          # Version history
└── references/
    ├── sector-classification.md          # Annex I / II sector taxonomy + entity-size rules
    ├── art21-measures.md                 # The 10 risk-management measures (Art. 21(2)(a)-(j))
    ├── germany-nis2umsucg.md             # § 30 BSIG, NIS2UmsuCG, BSI registration
    ├── eu-jurisdiction-profiles.md       # IT, FR, NL, AT, ES — entity taxonomy + SA contacts
    ├── regulatory-sources.md             # Official EU + Member State source catalog
    └── templates.md                      # Output templates (gap analysis, roadmap, briefing)
```

## Deployment

### Claude.ai (User Skills)

1. Go to **Settings → Profile → Custom Skills** (or equivalent)
2. Upload the entire `nis2-navigator/` folder structure
3. The skill will auto-trigger on "NIS2", "BSIG", "BSIG-neu", "NIS2UmsuCG", "Annex I/II", "essential entity", or "Art. 21 gap analysis"

### Claude Code / Custom MCP Setup

1. Copy the `nis2-navigator/` folder to your skills directory:
   ```bash
   cp -r nis2-navigator/ /path/to/your/skills/user/nis2-navigator/
   ```
2. Ensure the skill is registered in your configuration

## Usage

### Quick Start

Describe your organisation:

> "We're a German cloud-services provider with 80 employees and €15M turnover.
> Do we fall under NIS2? If yes, give me a gap analysis against Art. 21 and a
> 12-month roadmap."

The skill will classify scope, run the gap analysis, and produce a phased roadmap.

### Trigger Phrases

- "NIS2" / "NIS-2" / "BSIG" / "BSIG-neu" / "NIS2UmsuCG"
- "Essential entity" / "Important entity" / "Annex I/II"
- "Art. 21 gap analysis" / "NIS2 readiness" / "Cybersecurity compliance assessment"
- "BSI registration" / "§ 30 BSIG"
- "Cyberbeveiligingswet" / "Loi Résilience" / "decreto legislativo 138"

### Workflow

| Phase | Description |
|-------|-------------|
| **Session Init** | Disclaimer, web search for recent developments, jurisdiction focus selection |
| **Phase 1: Scope & Classification** | Annex I/II routing, essential vs. important, jurisdiction-specific overlays (~5 min) |
| **Phase 2: Art. 21 Gap Analysis** | 0–4 maturity scoring across the 10 measures with ISO 27001 anchors (~15 min) |
| **Phase 3: Compliance Roadmap** | Prioritisation framework + Germany-specific items + Art. 20 / § 38 BSIG management briefing |
| **Output** | Final Assessment Report consolidating scope, gaps, and roadmap |

## Capabilities Summary

| Feature | Description |
|---------|-------------|
| Scope Classification | Annex I/II + essential/important + jurisdiction-specific overlays |
| Art. 21 Gap Analysis | 0–4 maturity scoring across all 10 measures |
| ISO 27001 Crossref | Each measure mapped to ISO 27001 controls |
| Roadmap Prioritisation | Legal-exposure-aware sequencing with quick-win identification |
| Germany Deep Coverage | § 30 BSIG, NIS2UmsuCG, BSI registration workflow |
| EU Profiles | IT, FR, NL, AT, ES — entity taxonomy + SA contacts |
| Management Briefing | Art. 20 / § 38 BSIG board-level liability briefing template |
| Final Report | Audit-ready assessment report consolidating all phases |

## Regulatory Basis

| Document | Reference |
|----------|-----------|
| NIS2 Directive | EU Directive 2022/2555 |
| Art. 21 | 10 risk-management measures |
| Art. 23 | Incident reporting obligations |
| Art. 20 | Management body responsibilities |
| Annex I / II | Sector and entity-type taxonomy |
| BSIG-neu (DE) | German NIS2UmsuCG transposition, § 30, § 38 |
| ISO 27001 | Risk-management measure crossref |

## License & Disclaimer

This skill provides structured NIS2 compliance guidance based on EU Directive 2022/2555 and national transposition laws. It is not legal advice. Final compliance decisions should involve your organisation's CISO / Information Security Officer and qualified legal counsel experienced in cybersecurity regulation.

Licensed under AGPL-3.0.

> **Quality assurance:** this skill ships with evaluation tests in the `evals/` folder, which I run to check its outputs against expected results.

---

*Created by Oliver Schmidt-Prietz — [OneZero Legal](https://onezero.legal)*
