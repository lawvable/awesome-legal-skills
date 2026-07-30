# DPA Art. 28 GDPR — Deployment Guide

> 📄 **[View the interactive skill page →](https://oliverschmidtprietz.github.io/GDPR-Data-Processing-Agreement/)**

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Overview

DPA Art. 28 GDPR — review, drafting, and redlining of Data Processing Agreements (AVV / Auftragsverarbeitungsvertrag) and Art. 26 Joint Controller Arrangements:

- **5 operating modes** routed automatically — REVIEW_QUICK, REVIEW_NEG (negotiation-grade), DRAFT, REDLINE, JOINT_CONTROLLER
- **Bilingual output** — DE and EN, parallel quality
- **Two perspectives** — controller-side and processor-side reviews
- **Two review depths** — quick (Art. 28(3)(a)–(h) coverage check) and negotiation-grade (clause-by-clause risk scoring)
- **Commission SCC anchor** — built on Commission Implementing Decision (EU) 2021/915
- **Template library** — commercial, hybrid, and strict DPA templates (DE + EN); JCA templates (DE + EN)
- **Common-defects catalog** for fast spotting in vendor-provided drafts
- **Negotiation fallback positions** — pre-drafted alternative language for contentious clauses
- **SCC module guide** — when and how to bolt Modules 1–4 onto a DPA for international transfers
- **Tier selection helper** — match commercial / hybrid / strict template to deal context
- **Strict quality gates** — verified Art. 28(3) coverage before delivery

## File Structure

```
dpa-art28/
├── SKILL.md                                       # Main skill instructions (deploy this)
├── CHANGELOG.md                                   # Version history
├── references/
│   ├── 2021-915-commission-text-en.md             # Commission Implementing Decision (EU) 2021/915 — EN
│   ├── 2021-915-commission-text-de.md             # Commission Implementing Decision (EU) 2021/915 — DE
│   ├── art28-3-checklist.md                       # Art. 28(3)(a)–(h) coverage checklist
│   ├── art26-joint-controller.md                  # Art. 26 JCA framework
│   ├── common-defects.md                          # Vendor-DPA defect catalog
│   ├── negotiation-fallbacks.md                   # Fallback positions for contentious clauses
│   ├── sccs-module-guide.md                       # International-transfer SCC integration
│   └── tier-selection.md                          # Commercial / hybrid / strict tier helper
├── templates/
│   ├── dpa-commercial-de.md                       # Commercial DPA — DE
│   ├── dpa-commercial-en.md                       # Commercial DPA — EN
│   ├── dpa-hybrid-de.md                           # Hybrid DPA — DE
│   ├── dpa-hybrid-en.md                           # Hybrid DPA — EN
│   ├── dpa-strict-de.md                           # Strict DPA — DE
│   ├── dpa-strict-en.md                           # Strict DPA — EN
│   ├── jca-de.md                                  # JCA template — DE
│   └── jca-en.md                                  # JCA template — EN
└── workflows/
    ├── review-quick.md                            # REVIEW_QUICK procedure
    ├── review-negotiation.md                      # REVIEW_NEG procedure
    ├── draft.md                                   # DRAFT procedure
    ├── redline.md                                 # REDLINE procedure
    └── joint-controller.md                        # JOINT_CONTROLLER procedure
```

## Deployment

### Claude.ai (User Skills)

1. Go to **Settings → Profile → Custom Skills** (or equivalent)
2. Upload the entire `dpa-art28/` folder structure
3. The skill will auto-trigger on "DPA", "AVV", "Auftragsverarbeitung", "Art. 28 contract", "redline this DPA", "JCA", or "joint controller agreement"

### Claude Code / Custom MCP Setup

1. Copy the `dpa-art28/` folder to your skills directory:
   ```bash
   cp -r dpa-art28/ /path/to/your/skills/user/dpa-art28/
   ```
2. Ensure the skill is registered in your configuration

## Usage

### Quick Start

Paste a DPA or ask for one:

> "Review this DPA from a vendor — we're the controller. Quick check first,
> then tell me what's missing under Art. 28(3) and what I should push back on."

Or:

> "Draft a strict-tier DPA in German for an EU-based processor handling
> employee data, including SCCs Module 2 for our US subsidiary."

### Trigger Phrases

- "DPA" / "AVV" / "Auftragsverarbeitung" / "Auftragsverarbeitungsvertrag"
- "Art. 28 contract" / "Data processing agreement" / "Processor agreement"
- "Review this DPA" / "Draft a DPA" / "Redline this DPA"
- "Art. 26 arrangement" / "JCA" / "Joint controller agreement"

### Mode Router

| Mode | When |
|------|------|
| **REVIEW_QUICK** | Fast Art. 28(3)(a)–(h) coverage check |
| **REVIEW_NEG** | Negotiation-grade clause-by-clause risk scoring |
| **DRAFT** | Produce a new DPA from a chosen template tier |
| **REDLINE** | Mark up an existing draft with proposed changes |
| **JOINT_CONTROLLER** | Art. 26 Joint Controller Arrangement workflow |

## Capabilities Summary

| Feature | Description |
|---------|-------------|
| Bilingual (DE/EN) | Parallel quality across both languages |
| Dual Perspective | Controller-side and processor-side review |
| Commission SCC | Built on Implementing Decision (EU) 2021/915 |
| Template Library | 3 DPA tiers × 2 languages + JCA × 2 languages |
| Defect Catalog | Common vendor-DPA defects with diagnostic signals |
| Negotiation Fallbacks | Pre-drafted alternative language for contested clauses |
| SCC Integration | International-transfer module guidance (Modules 1–4) |
| Tier Selection | Commercial / hybrid / strict matched to deal context |
| Quality Gates | Verified Art. 28(3) coverage before delivery |

## Regulatory Basis

| Document | Reference |
|----------|-----------|
| GDPR Art. 28 | Controller-processor relationship |
| GDPR Art. 28(3)(a)–(h) | Mandatory DPA content |
| GDPR Art. 26 | Joint controller arrangements |
| Commission Implementing Decision (EU) 2021/915 | EU-wide DPA standard contractual clauses |
| Commission Implementing Decision (EU) 2021/914 | International transfer SCCs (Modules 1–4) |

## License & Disclaimer

This skill provides structured GDPR Art. 28 / Art. 26 contracting guidance. It is not legal advice. Negotiated DPAs and JCAs should be reviewed by qualified data protection counsel before signing.

Licensed under AGPL-3.0.

> **Quality assurance:** this skill ships with evaluation tests in the `evals/` folder, which I run to check its outputs against expected results.

---

*Created by Oliver Schmidt-Prietz — [OneZero Legal](https://onezero.legal)*
