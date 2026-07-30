---
name: "swiss-legal-source-authority-triage-enrique-g-zbinden"
description: >-
  Swiss legal source and authority triage. Use when a user asks a Swiss legal, regulatory, compliance, contract, employment, corporate, litigation, IP, tax, privacy, public-law, fintech, register, or cantonal-law question; when Swiss law may apply; or when an AI legal answer needs source routing across federal, cantonal, communal, regulator, register, contractual, professional, soft-law, multilingual, or open-data layers.
  
metadata:
  author: "Enrique G. Zbinden"
  license: "mit"
  version: "2026-05-16"
---

# Swiss Legal Source & Authority Triage

## Purpose

Use this skill to map the Swiss legal authority structure before producing a legal answer.

This skill does **not** provide Swiss legal advice. It helps an AI assistant identify the correct source layer, authority hierarchy, language/version checks, uncertainty flags, and human-review boundaries for Swiss legal research and legal-operations workflows.

Core thesis: **for Swiss legal AI, route authority before generating an answer.**

## When to use this skill

Use this skill whenever:

- The user asks a question involving Swiss law, Switzerland, a Swiss party, Swiss assets, Swiss employment, Swiss contracts, Swiss courts, Swiss regulators, Swiss companies, Swiss data protection, Swiss financial regulation, Swiss IP, Swiss tax, Swiss criminal/public law, or Swiss cantonal/municipal law.
- The user asks whether a legal issue is federal, cantonal, communal, regulatory, contractual, professional, or mixed.
- The user asks for Swiss legal research sources, legal-source validation, or a legal source map.
- A contract, policy, memo, or compliance workflow claims to be governed by Swiss law.
- The answer could be affected by official-language versions, cantonal variation, regulator practice, pending reform, or register/legal-state evidence.

## Safety and role limits

Do not present the output as legal advice. Use language such as:

> This is a Swiss legal source and authority triage, not legal advice. It identifies likely source layers and review points. A qualified Swiss lawyer should review any concrete legal position, filing, advice to a client, or operational decision.

Escalate clearly when the issue involves:

- Litigation strategy, limitation periods, procedural deadlines, criminal exposure, regulatory authorisation, sanctions, employment termination, immigration, tax, financial-market authorisation, medical/health regulation, or court filings.
- Client-specific facts that materially affect the legal outcome.
- Cantonal or municipal law where the relevant canton/commune is unknown.
- Professional secrecy, attorney-client privilege, legal-profession regulation, or data that may be confidential.
- Non-public sources, paywalled doctrine, unpublished practice, or recent legal reform.

## Core principles

1. **Authority before answer**: first identify which Swiss source layer controls.
2. **Official before aggregator**: use official sources as authority; use aggregators only for discovery unless their legal status is independently confirmed.
3. **Current law before commentary**: verify the law in force, effective dates, amendments, and transitional rules before summarising doctrine or practice.
4. **Canton before generalisation**: do not assume Swiss law is uniform where cantonal or communal competence may matter.
5. **Language before confidence**: German, French, and Italian official versions may matter. English translations are usually informational unless an official status is established.
6. **Regulator practice is not always binding law**: classify guidance, circulars, enforcement reports, FAQs, and self-regulation separately from statutes and ordinances.
7. **Doctrine is persuasive, not binding**: use doctrinal sources (commentaries, treatises, textbooks, expert opinions) only after official law, case law and regulatory practice have been checked. Treat doctrine as persuasive authority. Prefer works over names, check editions and languages, and note doctrinal disagreements.
8. **Review boundary before conclusion**: state where human legal judgment enters.

## Triage workflow

### Step 1: Classify the issue

Classify the user's request as one or more of:

- Private law / contract / tort / property
- Corporate / commercial register / authority to sign
- Employment / social security / immigration-adjacent
- Data protection / privacy / information security
- Financial-market / AML / fintech / insurance
- Competition / consumer / unfair competition
- IP / technology / licensing
- Tax / customs / trade / sanctions
- Public law / administrative law / public procurement
- Criminal / regulatory enforcement
- Civil, criminal, administrative, or arbitration procedure
- Cantonal / communal / professional-regulatory matter
- Mixed or uncertain

If the relevant canton, commune, regulator, sector, contract type, or factual setting is missing, proceed with explicit assumptions and flag the gap. Ask a clarifying question only when the missing fact makes source routing impossible.

### Step 2: Map the authority layer

Identify every layer that may control the answer:

| Layer | What to check |
|---|---|
| Federal law | Federal Constitution, federal acts, ordinances, treaties, federal official publications |
| Cantonal law | Cantonal constitution, acts, ordinances, court organisation, administrative practice |
| Communal/local law | Municipal rules, permits, zoning, police regulations, local public-law instruments |
| Official case law | Federal Supreme Court, Federal Administrative Court, Federal Criminal Court, Federal Patent Court, cantonal courts |
| Regulator practice | FINMA, FDPIC/EDÖB, COMCO/WEKO, SECO, Swissmedic, FTA/ESTV, BAKOM/OFCOM, fedpol/MROS, sector bodies |
| Registers/legal state | Zefix, cantonal commercial registers, SHAB/SOGC, Swissreg, land register where accessible, debt enforcement/bankruptcy publications |
| Contractual source | Governing law, jurisdiction/arbitration clause, order of precedence, policies, schedules, standards incorporated by reference |
| Professional/self-regulation | Bar/professional rules, SRO rules, industry codes, exchange rules, association standards |
| Doctrine/expert authority | Commentaries, treatises, textbooks, expert opinions, academic articles. Use only after official sources and regulator practice. Check edition, language and doctrinal posture. |
| Soft law / secondary | Guidance, commentary, law-firm notes, academic writing, open-access journals, research guides |

### Step 3: Apply the Swiss source hierarchy

Use this hierarchy when deciding what source to rely on:

1. **Official primary law**: Fedlex; Official Compilation; Classified/Systematic Compilation; treaties; official cantonal and communal law portals.
2. **Official case law**: Federal Supreme Court; Federal Administrative Court; Federal Criminal Court; Federal Patent Court; cantonal court portals.
3. **Official legislative materials**: Federal Gazette; Curia Vista; Official Bulletin; consultation materials; dispatches/messages.
4. **Official regulator practice**: FINMA, FDPIC/EDÖB, COMCO/WEKO, Swissmedic, SECO, FTA/ESTV, BAKOM/OFCOM, fedpol/MROS, and other competent authorities.
5. **Registers and legal-state sources**: Zefix, cantonal commercial registers, SHAB/SOGC, Swissreg, public insolvency and publication sources.
6. **Open discovery / AI-ready layers**: OpenCaseLaw, LexFind, Entscheidsuche, opendata.swiss datasets, Fedlex-JOLux, open APIs and bulk datasets.
7. **Doctrine and expert authority**: Commentaries, treatises, textbooks, expert opinions and academic works. Doctrine is persuasive only. Use after official sources. See `resources/doctrine-and-expert-authority-map.md`.
8. **Secondary orientation**: GlobaLex, Library of Congress, UZH/CLDS resources, open-access journals, university guides, law-firm notes and practitioner commentary. Useful for broad context and discovery but not authoritative.
9. **Commercial or login-based sources**: Swisslex, Lawsearch/Weblaw, Legalis, private legal AI platforms, firm knowledge bases. Treat as useful but not public authority.

Do not treat a discovery layer as controlling authority merely because it is searchable or AI-accessible.

### Step 4: Verify language, version, and temporal status

For each material source, record:

- Official language version checked: DE / FR / IT / RM / EN.
- Whether the English version is official, informational, or uncertain.
- Law-in-force date, effective date, amendment date, and transitional period if relevant.
- Whether the material is current law, draft law, consultation material, legislative history, regulator guidance, case law, doctrine, or open-data metadata.
- Whether the source is official, open-data, aggregator/discovery, commercial, academic, or secondary.

Flag multilingual divergence risk where wording could affect interpretation.

### Step 5: Identify Swiss-specific uncertainty flags

Always consider these flags:

- **Cantonal competence**: answer may vary by canton.
- **Communal/local competence**: permits, zoning, public order, local regulations, or procurement may depend on commune.
- **Sector regulator**: FINMA, FDPIC/EDÖB, COMCO/WEKO, Swissmedic, SECO, FTA/ESTV, BAKOM/OFCOM, fedpol/MROS, or other authority may control.
- **Public vs private employer/entity**: employment, procurement, transparency, and public-law remedies may change.
- **Professional secrecy or privilege**: especially lawyers, healthcare, finance, auditors, fiduciaries, and regulated professionals.
- **Self-regulation**: SRO, exchange, professional association, or industry code may be relevant but not equivalent to statute.
- **Pending reform**: draft law, consultation, Federal Council dispatch, parliamentary business, or transition period may affect advice.
- **Source currency**: outdated law, old practice, superseded guidance, or pre-reform case law.
- **Register fact vs legal conclusion**: company/register data shows legal state but may not resolve authority, enforceability, or liability.
- **Human judgment required**: interpretation, risk appetite, legal strategy, and client-specific facts cannot be reduced to source lookup.

### Step 6: Produce the answer in a safe frame

Use the following output structure unless the user asks for a different format.

```markdown
# Swiss Legal Source Map

## 1. Issue classification
[Classify the issue and state key assumptions.]

## 2. Likely authority layers
| Layer | Relevance | Source path to check | Status |
|---|---|---|---|
| Federal law | ... | ... | Official / primary |
| Cantonal law | ... | ... | Requires canton |
| Regulator | ... | ... | Guidance / circular / enforcement / binding rule |

## 3. Primary sources to check first
[List official statutes, ordinances, treaties, court databases, regulator materials, registers, or cantonal portals.]

## 4. Discovery and secondary sources
[List OpenCaseLaw, LexFind, Entscheidsuche, opendata.swiss, academic guides, commentary, etc., with a warning not to treat them as authority unless appropriate.]

## 5. Language, version, and date checks
[DE/FR/IT/RM/EN; in-force date; amendment/reform risk; translation caution.]

## 6. Preliminary legal-information frame
[Give only source-grounded legal information. Do not provide a definitive client-specific legal conclusion unless the sources and facts support it.]

## 7. Swiss-specific uncertainty flags
[Cantonal, regulator, professional secrecy, pending reform, source currency, factual gaps.]

## 8. Human review boundary
[Information only / lawyer review recommended / lawyer review required / authority confirmation required / regulator-specific advice required.]

## 9. Review receipt
- Sources checked:
- Sources not checked:
- Assumptions:
- Remaining gaps:
- Date of triage:
```

## Compact mode

When the user needs a brief response, provide:

```markdown
**Swiss source route:** [federal/cantonal/regulator/register/contractual/mixed]
**Official sources first:** [sources]
**Discovery aids:** [sources]
**Key Swiss flags:** [cantonal/language/regulator/reform/facts]
**Review boundary:** [what needs Swiss lawyer or authority review]
```

## Prohibited shortcuts

Do not:

- Start with a confident legal conclusion before mapping authority.
- Treat Switzerland as legally uniform where cantonal or communal law may matter.
- Treat English translations as controlling without checking status.
- Treat regulator guidance, FAQs, or law-firm commentary as binding law without qualification.
- Treat OpenCaseLaw, LexFind, Entscheidsuche, or another aggregator as a substitute for official sources.
- Ignore source date, in-force date, transitional provisions, or pending reform.
- Draft filings, regulatory submissions, or advice-to-client conclusions without clear human-review warnings.

## Navigation

Use the reference files in `resources/`:

- `swiss-legal-source-map.md` — curated Swiss source list by source type.
- `source-hierarchy.md` — authority hierarchy and source-status taxonomy.
- `doctrine-and-expert-authority-map.md` — doctrine and expert-authority guidance.
- `output-template.md` — reusable Swiss source-map template.
- `examples.md` — sample outputs for common Swiss legal questions.
