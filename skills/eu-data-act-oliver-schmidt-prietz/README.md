# EU Data Act Practitioner Skill — Deployment Guide

> 📄 **[View the interactive skill page →](https://oliverschmidtprietz.github.io/EU-Data-Act/)**

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Overview

Practitioner-grade analysis and drafting on **Regulation (EU) 2023/2854** (the Data Act). Calibrated for senior legal counsel, compliance officers, and product counsel working with the Data Act in client-facing or in-house contexts.

The skill's architectural anchor is **role × chapter × stage**. Every matter is positioned by identifying:

- which Data Act roles the parties play (user, data holder, data recipient, third party, customer, provider, public sector body, plus any concurrent GDPR roles);
- which chapter(s) of the regulation govern (II–VIII);
- which stage of that chapter's process the matter is at.

The anchor determines which references load and which scenario card the skill applies.

## Coverage

| Chapter | Articles | Operative depth |
|---------|----------|-----------------|
| Ch II | 3–7 | Full — IoT product and related service data; B2C and B2B sharing |
| Ch III | 8–12 | Full — mandatory B2B sharing under other Union law (FRAND, compensation) |
| Ch IV | 13 | Full — unfair contract terms unilaterally imposed in B2B data contracts |
| Ch V | 14–22 | Full — public sector exceptional-need access |
| Ch VI | 23–31 | Full — switching between data processing services |
| Ch VII | 32 | Full — third-country governmental access |
| Ch VIII | 33–36 | Gate-only, except Arts. 34–35 where they serve Ch VI |

### Cross-regime gates

| Gate | Reference file | Posture |
|------|----------------|---------|
| GDPR + ePrivacy | `references/gates/gdpr-overlay.md` | Operative when personal data or terminal-equipment access is in scope |
| Trade Secrets Directive (EU) 2016/943 | `references/gates/trade-secrets-directive.md` | Operative when trade-secret protection is claimed or asserted |
| DMA gatekeeper exclusion | `references/gates/dma-gatekeeper.md` | Operative on Art. 5 third-party requests and Art. 6(2)(d) onward sharing |
| Sectoral lex specialis | `references/gates/sectoral-lex-specialis.md` | Warn-only (vehicles, medical devices, DORA, NIS2, CRA, AI Act, eIDAS, energy, agriculture, telecoms) |
| Member State implementing law | `references/gates/member-state.md` | Warn-only (competent authorities, dispute settlement, penalties) |

## File structure

```
eu-data-act/
├── SKILL.md                              # Entry point and router
├── CHANGELOG.md                          # Version history
├── references/
│   ├── method/
│   │   ├── analysis-method.md            # The seven-step cognitive flow
│   │   └── house-style.md                # Voice, length, citation, structure
│   ├── gates/
│   │   ├── gdpr-overlay.md               # Art. 1(5) bridge, Case A/B, ePrivacy
│   │   ├── trade-secrets-directive.md    # TSD ladder, serious-AND-irreparable
│   │   ├── dma-gatekeeper.md             # Art. 5(3) exclusion, Art. 6(2)(d)
│   │   ├── sectoral-lex-specialis.md     # Warn-only sectoral catalogue
│   │   └── member-state.md               # Warn-only MS implementing law
│   ├── gotchas.md                        # 20 numbered failure-mode entries
│   └── scenarios/                        # Pre-walked role × chapter × stage cards
├── sources/
│   ├── regulation-2023-2854.md           # Verbatim Data Act (119 recitals + 50 articles)
│   ├── faq-v1-4.md                       # Commission FAQ v1.4 (22 Jan 2026, CC BY 4.0)
│   ├── digital-omnibus-amendments-tracker.md
│   ├── mcts-sccs-recommendation-pointer.md
│   ├── vehicle-data-guidance-pointer.md
│   ├── _versions.json                    # Source provenance
│   └── _manifest.sha256                  # Source checksums
├── scripts/
│   └── validate_sources.py               # Source layer validator (20/20 checks)
├── templates/                            # Drafting templates
└── evals/                                # Eval fixtures + grading
```

## Deployment

### Claude Code (recommended)

Symlink the skill folder into `~/.claude/skills/`:

```bash
ln -s ~/CLAUDE_PROJECTS/SKILLS/claude-skills/skills/eu-data-act ~/.claude/skills/eu-data-act
```

### Claude.ai (User Skills)

Upload the entire `eu-data-act/` folder structure under Settings → Profile → Custom Skills.

## Trigger phrases

- "Data Act" / "Datengesetz" / "Regulation (EU) 2023/2854"
- "Art. 4(1) request" / "Art. 5(1) third-party request" / "trade-secret handbrake"
- "cloud switching obligations" / "Chapter VI" / "Art. 25 mandatory terms"
- "Chapter V exceptional need" / "Art. 17 public-sector request"
- "Art. 13 unfair contract terms" / "Art. 32 third-country access"
- References to specific Data Act articles or recitals.

## Source layer validator

Run before any release or downstream symlink:

```bash
python3 scripts/validate_sources.py --verbose
```

Checks heading taxonomy (every expected recital, article, and FAQ question), pointer-file presence, manifest checksums, and `_versions.json` structure. Exit 0 means all checks pass. Current state: 20/20.

## Regulatory basis

| Document | Reference |
|----------|-----------|
| EU Data Act | Regulation (EU) 2023/2854 |
| Commission FAQ on the Data Act | v1.4 (22 January 2026), CC BY 4.0 |
| Digital Omnibus proposal | COM(2025) 833 final, 19 November 2025 (co-legislator negotiation, not adopted) |
| Trade Secrets Directive | Directive (EU) 2016/943 |
| GDPR | Regulation (EU) 2016/679 |
| ePrivacy Directive | Directive 2002/58/EC |
| Digital Markets Act | Regulation (EU) 2022/1925 |

## License and disclaimer

Licensed under **AGPL-3.0**.

This skill provides structured guidance based on the EU Data Act, the Commission's FAQ, and adjacent EU law. It does not constitute legal advice. Substantive deliverables produced with the skill should be reviewed by qualified legal counsel with Data Act expertise.

> **Quality assurance:** this skill ships with evaluation tests in the `evals/` folder, which I run to check its outputs against expected results.

---

*Created by Oliver Schmidt-Prietz — [OneZero Legal](https://onezero.legal)*
