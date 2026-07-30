# Privacy Notice EU — Deployment Guide

> 📄 **[View the interactive skill page →](https://oliverschmidtprietz.github.io/GDPR-Privacy-Notice-EU/)**

## Overview

Pan-EU GDPR Privacy Notice Generator — a comprehensive drafting skill for Claude that produces jurisdiction-aware, GDPR-compliant privacy notices as professional .docx documents:

- **Five notice types**: Website/App, Applicant, Employee, Business Partner (B2B), B2C Customer
- **Multi-jurisdiction coverage**: DE (DSGVO+BDSG+TDDDG), FR (RGPD+LIL+LCEN), AT, IT, ES, NL, BE, IE, UK GDPR
- **Multi-language support**: German, French, English — with bilingual and pan-EU options
- **AI Act transparency integration**: Art. 50 AI Act disclosure requirements
- **Type-driven intake**: data categories, legal bases, and retention defaults tailored to each notice type
- **Art. 13/14 compliance verification**: structured checklist before delivery
- **Cookie & tracking section**: with CMP integration guidance
- **Art. 21 objection box**: visually prominent, separate presentation per GDPR requirement
- **DPIA indicator screening**: flags when Art. 35 assessment may be needed
- **Audit-ready .docx output** with professional formatting

## File Structure

```
privacy-notice-eu/
├── SKILL.md                              # Main skill instructions (deploy this)
└── references/
    ├── templates.md                      # Document template: structure, formatting, translations
    ├── EU_COMMON.md                      # Pan-EU GDPR requirements (Art. 13/14 checklist, legal bases)
    ├── DE.md                             # Germany-specific requirements (BDSG, TDDDG, DSK guidance)
    ├── FR.md                             # France-specific requirements (CNIL recommendations, LIL, LCEN)
    ├── OTHER_EU.md                       # AT, IT, ES, NL, BE, IE, UK GDPR specifics
    └── NOTICE_TYPES.md                   # Type profiles: section maps, data categories, intake questions
```

## Deployment

### Claude.ai (User Skills)

1. Go to **Settings → Profile → Custom Skills** (or equivalent)
2. Upload the entire `privacy-notice-eu/` folder structure
3. The skill will auto-trigger when you mention privacy notices, Datenschutzerklaerung, politique de confidentialite, Art. 13/14, or related topics

### Claude Code / Custom MCP Setup

1. Copy the `privacy-notice-eu/` folder to your skills directory:
   ```bash
   cp -r privacy-notice-eu/ /path/to/your/skills/user/privacy-notice-eu/
   ```
2. Ensure the skill is registered in your configuration

## Usage

### Quick Start

Just tell Claude what you need:

> "I need a privacy notice for our SaaS platform. We're a German GmbH based in Berlin,
> targeting customers in Germany and France. We use Google Analytics, Stripe for payments,
> and OpenAI for an AI chatbot feature."

The skill will activate and walk you through the intake process.

### Trigger Phrases

- "Create a privacy notice" / "Datenschutzerklaerung erstellen" / "politique de confidentialite"
- "Privacy policy for our website" / "Art. 13 GDPR"
- "Bewerber-Datenschutz" / "applicant privacy notice"
- "Employee data protection notice" / "Beschaeftigten-Datenschutz"

### Workflow

| Step | Description |
|------|-------------|
| **1. Scope** | Notice type, jurisdiction(s), language, template choice |
| **2. Intake** | Type-driven collection: controller info, data inventory, legal bases, processors, cookies, AI |
| **3. Draft** | Generate notice from template + type profile + collected information |
| **4. Verify** | Art. 13/14 compliance check + type-specific checks + AI Act check |
| **5. Deliver** | Professional .docx output with post-generation checklist |

### Notice Types

| Type | Typical Use Case |
|------|------------------|
| **Website / App** | Visitors, users, subscribers — includes sub-types (brochure, e-commerce, SaaS, mobile, marketplace, AI platform) |
| **Applicant** | Job applicants and candidates |
| **Employee** | Employees, contractors, interns |
| **B2B Partner** | Contact persons at vendors, suppliers, clients |
| **B2C Customer** | End consumers in purchase/service relationships |
| **Combined** | Multiple audiences in one or linked notices |

## Regulatory Basis

| Document | Reference |
|----------|-----------|
| GDPR Articles 13 & 14 | Information duties to data subjects |
| GDPR Article 21(4) | Prominent presentation of right to object |
| GDPR Article 22 | Automated decision-making transparency |
| EU AI Act Article 50 | AI transparency obligations |
| BDSG (Germany) | Sec. 26 employee data, DPO thresholds |
| CNIL Recommendations (France) | 2020 privacy notice guidance |
| TDDDG (Germany) | Telemedien/cookie requirements |

## Version History

See [CHANGELOG.md](CHANGELOG.md).

## License & Disclaimer

This skill provides drafting guidance based on publicly available GDPR regulatory materials. It does not constitute legal advice. All privacy notices should be reviewed by qualified data protection counsel and your organization's DPO before publication.

> **Quality assurance:** this skill ships with evaluation tests in the `evals/` folder, which I run to check its outputs against expected results.

---

*Created by Oliver Schmidt-Prietz — [OneZero Legal](https://onezero.legal)*
