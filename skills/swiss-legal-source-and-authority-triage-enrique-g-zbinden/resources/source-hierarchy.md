# Swiss Legal Source Hierarchy

This file classifies source types for Swiss legal AI workflows. The purpose is not to rank every individual source absolutely, but to prevent an AI assistant from confusing official authority, discovery infrastructure, open data, commercial research products, and secondary commentary.

## Tier 1 — Official primary law

Use first for legal text, effective dates, amendments, and treaty status.

- Fedlex: https://www.fedlex.admin.ch/en/home
- Official Compilation / Amtliche Sammlung / Recueil officiel / Raccolta ufficiale
- Classified or Systematic Compilation / Systematische Rechtssammlung / Recueil systématique / Raccolta sistematica
- Federal treaties published through Fedlex
- Official cantonal law portals
- Official communal/local legal portals where relevant

Treatment: controlling primary source, subject to language/version/date checks.

## Tier 2 — Official case law

Use for judicial interpretation, leading decisions, procedural practice, and court-specific doctrine.

- Federal Supreme Court: https://www.bger.ch/
- Federal Administrative Court: https://www.bvger.ch/
- Federal Criminal Court: https://www.bstger.ch/
- Federal Patent Court: https://www.bundespatentgericht.ch/
- Cantonal court portals

Treatment: official case-law source. Check whether the decision is a leading decision, published decision, unpublished/anonymised decision, or lower-court decision.

## Tier 3 — Official legislative materials

Use for legislative intent, reform tracking, consultation history, and parliamentary status.

- Federal Gazette / Bundesblatt / Feuille fédérale / Foglio federale: via Fedlex
- Curia Vista: https://www.parlament.ch/en/ratsbetrieb/curia-vista
- Official Bulletin: https://www.parlament.ch/en/ratsbetrieb/amtliches-bulletin
- Consultation procedure materials: via Fedlex and admin.ch

Treatment: not the operative legal rule unless enacted, but important for interpretation and reform tracking.

## Tier 4 — Official regulator and supervisory authority material

Use for sector interpretation, supervisory expectations, enforcement posture, guidance, circulars, and authorisation context.

- FINMA: https://www.finma.ch/
- FDPIC / EDÖB: https://www.edoeb.admin.ch/en
- COMCO / WEKO: https://www.weko.admin.ch/
- SECO: https://www.seco.admin.ch/
- Swissmedic: https://www.swissmedic.ch/
- Federal Tax Administration / ESTV: https://www.estv.admin.ch/
- Federal Office of Communications / BAKOM-OFCOM: https://www.bakom.admin.ch/
- fedpol / MROS: https://www.fedpol.admin.ch/

Treatment: classify carefully as binding ordinance, circular, guidance, enforcement report, recommendation, FAQ, or soft-law/self-regulatory material.

## Tier 5 — Registers and legal-state sources

Use for legal-state facts: existence, registration, publications, ownership/status notices, insolvency/publication events, IP registrations.

- Zefix: https://www.zefix.ch/
- Swiss Official Gazette of Commerce / SHAB / SOGC: https://www.shab.ch/
- Cantonal commercial registers
- Swissreg / IPI: https://www.swissreg.ch/
- Debt enforcement and bankruptcy publication sources
- Land register sources where access is available

Treatment: evidence of register/legal-state facts, not a substitute for legal analysis.

## Tier 6 — Open discovery and AI-ready layers

Use for search, metadata, citation graphs, APIs, bulk data, and cross-source discovery.

- OpenCaseLaw: https://opencaselaw.ch/
- LexFind: https://www.lexfind.ch/
- Entscheidsuche: https://entscheidsuche.ch/
- opendata.swiss: https://opendata.swiss/en
- Fedlex-JOLux: https://swiss.github.io/fedlex-jolux/

Treatment: useful for discovery and machine workflows. Verify controlling propositions against official sources where possible.

## Tier 7 — Doctrine and expert authority

Use for doctrinal commentary, treatises, textbooks, expert opinions, and academic works after official law, case law and regulator practice have been checked. Doctrine helps structure interpretation and identify controversies but is **persuasive, not binding**. Prefer named works (e.g., commentaries, treatises, academic articles) over bare names. Check the edition date, language and publication context. Doctrine may diverge between German-, French- and Italian-language scholarship and between cantons.

Examples:

- Commentaries (e.g., **Basler Kommentar**, **Berner Kommentar**, **Commentaire romand**)
- Treatises, handbooks and textbooks in specific fields (e.g., Criminal law, Constitutional law, Tax law, Company law, Data protection)
- Published expert opinions and legal reports

Treatment: persuasive authority. Use doctrine to understand the structure of the law, standard interpretations and doctrinal controversies. Do not cite doctrine as controlling law without confirming with official sources. See `resources/doctrine-and-expert-authority-map.md` for a field-based guide.

## Tier 8 — Secondary orientation

Use for orientation, teaching, context, and research expansion. These sources provide general overviews, research guidance and legal-cultural context but are not primary or doctrinal authority.

- GlobaLex Switzerland research guide
- Library of Congress Guide to Law Online: Switzerland
- UZH / Center for Legal Data Science legal-data resources
- **sui generis** open-access journal
- University legal research guides
- Open academic introductions to Swiss law
- Law-firm notes, newsletters, blog posts and practitioner commentary

Treatment: secondary. These resources are helpful for broad orientation and to discover further sources but are not authoritative. Verify any legal claim against official sources and doctrine.

## Tier 9 — Commercial or login-based legal research products

Use where the user has access and where professional research completeness requires it.

- Swisslex
- Lawsearch / Weblaw
- Legalis
- Private legal AI and research platforms
- Firm knowledge bases

Treatment: powerful research tools, but classify separately from free/open public infrastructure and avoid implying public accessibility.

## Source-status labels

Use these labels in outputs. Choose the label that best reflects the legal status of each cited source. Expand or refine as needed for doctrinal nuance.

- `official-primary-law`
- `official-case-law`
- `official-legislative-material`
- `official-regulator-material`
- `official-register-legal-state`
- `official-cantonal-or-communal`
- `open-data-or-machine-readable`
- `free-discovery-layer`
- `doctrine-or-expert-authority`
- `secondary-orientation`
- `commercial-or-login-based`
- `soft-law-or-self-regulation`
- `unknown-or-unverified-status`
