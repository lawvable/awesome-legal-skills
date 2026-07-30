# Gibraltar Legal, Regulatory & Compliance OSINT

**An open-source skills file to ground AI assistants in Gibraltar's legal, regulatory, and compliance landscape.**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Version](https://img.shields.io/badge/version-1.6-blue)]()
[![Jurisdiction](https://img.shields.io/badge/jurisdiction-Gibraltar-red)]()
[![Articles](https://img.shields.io/badge/legal%20articles-7%20published-green)]()

---

## What This Is

Gibraltar is a small jurisdiction with a mature legal and regulatory framework — but one that AI models consistently get wrong. English common law assumptions bleed in where they shouldn't. Procedural rules diverge from UK equivalents in ways that matter in practice. Official sources are fragmented across a dozen different websites with no central index.

This repository contains a structured skills file that corrects that. Upload it to Claude, Gemini, ChatGPT, Harvey, Legora, or any AI assistant to ground it in reliable, jurisdiction-specific knowledge before you start researching.

**It is not a product. It is a reference file released freely under CC BY 4.0.**

---

## Who It's For

- **Gibraltar lawyers** — procedural divergences, case law hierarchy, court structure, employment and public law
- **Compliance & AML/KYC professionals** — FSC, Gambling Division, OFT registers; AML framework; FATF position
- **Legal researchers** — legislation, Hansard, Employment Tribunal decisions, judicial review
- **Journalists and public interest researchers** — court judgments, parliamentary record, press releases
- **Developers building Gibraltar-specific AI tools** — see [API & Integration](#api--integration) below

---

## Contents

```
Gibraltar Legal Regulatory Compliance OSINT skill.md   ← The skills file (v1.3)
README.md                                               ← This file
LICENSE                                                 ← CC BY 4.0
```

The skills file covers:

- **Principles of Gibraltar Law** — source hierarchy, constitutional rights, court structure, civil procedure, employment law, public law & judicial review — each with a link to the full practitioner-depth article on GibCheck
- **Official Data Sources** — verified URLs for the main official Gibraltar datasets, each paired with the relevant GibCheck page
- **Research Profiles** — compliance/AML, legal researcher, parliamentary researcher, journalist, maritime & aviation
- **AI Integration Guidance** — what AI gets wrong about Gibraltar, how to verify outputs
- **Publishers Directory** — key news, government, business and industry sources covering Gibraltar, with links to the GibCheck publishers page

---

## What AI Gets Wrong About Gibraltar (And This File Fixes)

| Common AI error | Correct position |
|-----------------|-----------------|
| Applies English deemed service rules | Gibraltar deemed service by post is **14 days** — *Francis v Clifton-Psaila* |
| Treats English Court of Appeal decisions as binding | English case law is **persuasive only** — not binding in Gibraltar courts |
| Applies post-Jackson costs reforms | Post-Jackson reforms **not adopted** in Gibraltar |
| Treats Gibraltar as EU member post-2020 | EU law has **not applied since 31 December 2020** |
| States collective redundancy threshold as 20 | Gibraltar threshold is **5 employees** (not 20 as in England) |
| Applies English weekly pay cap to redundancy | **No statutory cap** on weekly pay in Gibraltar redundancy calculations |
| Says discrimination awards are capped | Under the Equal Opportunities Act 2006 discrimination awards are **uncapped** |
| Cites wrong regulator for legal practitioners | The **LSRA** has regulated since 30 December 2022 |
| Refers to the "Industrial Tribunal" | Renamed the **Employment Tribunal** since **13 October 2016** |
| States Gibraltar is not a FIFA member | Gibraltar has been a **FIFA member since 13 May 2016** (172–12 Congress vote following CAS award of 2 May 2016) |
| Cites Attorney-General as always the correct Crown defendant | *Marrache v AG* [2013–14 Gib LR 520] — Governor may be correct defendant in constitutional proceedings |

---

## Principles of Gibraltar Law — Published Series

The skills file includes summaries of all six published articles from GibCheck's Principles of Gibraltar Law series.

| Article | URL |
|---------|-----|
| The Legal Development of Gibraltar | https://www.gibcheck.com/legal/principles/legal-development |
| Constitutional Law and Fundamental Rights | https://www.gibcheck.com/legal/principles/constitutional-law |
| Court Structure and Jurisdiction | https://www.gibcheck.com/legal/principles/court-structure |
| Civil Litigation and Procedure | https://www.gibcheck.com/legal/principles/civil-litigation |
| Employment Law in Gibraltar | https://www.gibcheck.com/legal/principles/employment-law |
| Public Law and Judicial Review | https://www.gibcheck.com/legal/principles/public-law |
| **Sports Law in Gibraltar** *(new)* | https://www.gibcheck.com/legal/principles/sports-law |

Coming soon: Family Law; Criminal Law & Procedure; EU Law in Gibraltar; Maritime Law & Admiralty; Probate & Administration of Estates; Companies & Corporate Compliance; International Law; Mutual Legal Assistance.

*Full series: https://www.gibcheck.com/legal/principles*

---

## How to Use

### As a system prompt / context file

Copy the contents of `Gibraltar Legal Regulatory Compliance OSINT skill.md` and paste it as a system prompt or context document in your AI assistant before starting any Gibraltar-related research session.

**Recommended instruction:**

> Use the attached Gibraltar OSINT skills file as your primary reference for Gibraltar law, regulation, and official sources. Clearly distinguish information from this file from other sources. Note any gaps you identify.

### With specific tools

| Tool | Method |
|------|--------|
| **Claude (Projects)** | Add as a Project document — persists across all conversations in that project |
| **ChatGPT Custom GPTs** | Upload as a knowledge base file |
| **Google Gemini** | Paste into system instructions or upload as context |
| **Harvey / Legora** | Upload as a matter context document |

### As an llms.txt reference

Raw file URL:

```
https://raw.githubusercontent.com/Flipsta/Giblegal/main/Gibraltar%20Legal%20Regulatory%20Compliance%20OSINT%20skill.md
```

---

## API & Integration

This skills file is the public-facing layer of a broader Gibraltar public record intelligence project.

**GibCheck** (https://www.gibcheck.com) is the platform being built behind this work, currently in private beta. It provides unified search across Gibraltar's official public datasets, a maritime intelligence page, an aviation intelligence page, a searchable legal practitioners directory, and a practitioner legal reference wired to live records.

If you are building LLM integrations, RAG pipelines, or tooling for Gibraltar legal or compliance workflows, there is more to discuss. The skills file is the opener for that conversation.

**Get in touch:**
- LinkedIn: https://www.linkedin.com/in/philipvasquez
- X / Twitter: @philipvasquez
- API documentation: https://www.gibcheck.com/api-docs

---

## Versioning

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | June 2026 | Initial release |
| 1.2 | June 2026 | Expanded profiles; Gibraltar–EU treaty; OFT URL corrected |
| 1.3 | June 2026 | Added Employment Law and Public Law & JR sections (articles now live on GibCheck); added GibCheck parallel links for each official source; maritime and aviation pages added |
| 1.5 | June 2026 | Added Gibraltar company terms glossary (company.gi, attributed); GCS court structure, jury service, LPA sections; UBO register going free |
| 1.6 | June 2026 | Added Sports Law in Gibraltar article (GFA/FIFA/CAS, GRFU Rugby Europe admission, governance framework); added Gibraltar publishers directory; updated legislation reference table |

To be notified of updates: **Watch** this repository → Custom → Releases.

---

## Contributing

Pull requests and issues are welcome for broken URLs, missing sources, or corrections. Open an issue before a large PR.

---

## Licence & Attribution

Released under **[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)**.

Free to use, share, and adapt for any purpose, including commercial use, with attribution:

> *Gibraltar Legal, Regulatory & Compliance OSINT — Philip Vasquez LLB LLM (2026). CC BY 4.0. https://github.com/Flipsta/Giblegal*

**Author:** Philip Vasquez LLB LLM  
Gibraltar barrister | former Special Projects Lead at a UK fintech specialising in private company information data across the EU | published on litigation funding and wider legal technology policy  
LinkedIn: https://www.linkedin.com/in/philipvasquez

*This file does not constitute legal advice. Always verify against official primary sources.*
