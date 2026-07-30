---
name: ai-act-knowledge
description: |
  EU AI Act Knowledge Engine — authoritative regulatory Q&A grounded in 70 official EU source documents (including the 2026 Commission draft guidelines on Art. 6 high-risk classification — general principles, Annex I, Annex III). Answers any question about the AI Act with article-level citations from the full regulation text, Commission guidelines, EDPB/EDPS opinions, codes of practice, harmonised standards, FRIA guides, incident templates, and sector-specific guidance. This skill should be used when the user asks about the "EU AI Act", "AI Act regulation", "Regulation 2024/1689", "KI-Verordnung", asks to "explain an AI Act article", "what does Article X say", "AI Act requirements", "AI Act penalties", "AI Act timeline", "GPAI obligations", "high-risk AI", "prohibited AI practices", "AI Act and GDPR", "fundamental rights impact assessment", "AI Act standards", "AI Act national implementation", "AI literacy", "serious incident reporting", "Digital Omnibus", "AI regulatory sandbox", or any question about EU artificial intelligence regulation. Also triggers on German terms: "KI-Gesetz", "KI-Verordnung", "Hochrisiko-KI", "KI-Kompetenz", "Grundrechte-Folgenabschaetzung", "GPAI-Verhaltenskodex". For assessment workflows that produce a classification decision rather than a knowledge answer, offer to run a structured risk-tier classification in-session.
metadata:
  author: Oliver Schmidt-Prietz
  license: AGPL-3.0
  version: 2026.06.21
---

# EU AI Act Knowledge Engine

Authoritative knowledge base for Regulation (EU) 2024/1689 — the EU Artificial Intelligence Act. Grounded in **70 structured reference files** across 15 subdirectories (including the 2026 Commission draft guidelines on Art. 6 classification under `references/commission-guidelines/` — general principles, Annex I, Annex III), sourced exclusively from official EU institutions (European Commission, EDPB, EDPS, ENISA, EBA, Europol, AI Office, EUR-Lex). Every answer must cite specific articles, paragraphs, recitals, or guideline sections.

## Disclaimer (show at session start, do not block)

> **Important:** This skill provides structured AI Act regulatory information based on the EU AI Act (Regulation (EU) 2024/1689) and official EU institutional sources. It is not legal advice. Specific compliance decisions should involve qualified legal counsel with AI Act expertise.

---

## When to Search the Web

The reference files cover official sources through March 2026. Search the web when the user asks about events after that date, enforcement actions, national implementation updates, or non-official analysis (law firm perspectives, think tank papers). For niche topics, useful queries include: `CEN CENELEC JTC 21 harmonised standards [year]`, `EU AI Act Digital Omnibus trilogue [year]`, `[Member State] AI Act supervisory authority [year]`.

---

## Workflow

### Step 1: Classify the Question

| Question Type | Signal Words | Action |
|---------------|-------------|--------|
| **Article lookup** | "What does Art. X say" | Direct file read → cite verbatim |
| **Concept explanation** | "What is...", "explain...", "define..." | Find definition + context + recitals |
| **Obligation mapping** | "What must a [role] do" | Route by role + risk tier |
| **Classification help** | "Is this high-risk?", "Is this an AI system?" | Read `core/decision-trees.md`, walk through relevant tree |
| **Cross-framework** | "AI Act and GDPR", "medical devices + AI" | Multi-file synthesis across domains |
| **Timeline / deadlines** | "When does X apply?" | `governance/implementation-timeline.md` |
| **Penalty / enforcement** | "What are the fines?" | `core/regulation-title-VI-X-governance.md` (Art. 99) |
| **National implementation** | Country-specific | `national/` files + web search for updates |
| **Incident reporting** | "Serious incident", "what to report" | `templates/` files |
| **Sector-specific** | Healthcare, banking, HR, law enforcement | `sector-specific/` or `law-enforcement/` files |

### Step 2: Find and Read Reference Files

Use the **Topic Router** below to find the right files. For most questions, read 2–3 files: the primary source, the regulation article text, and any interpreting guideline or opinion.

Each `references/` subdirectory contains a `README.md` listing its files. For topics not in the Topic Router, use `Glob` to search the `references/` directory by keyword.

Always check recitals (`core/regulation-preamble-recitals.md`) for interpretive context on ambiguous provisions.

### Step 3: Synthesize with Citations

**Citation format:**

| Source Type | Format |
|-------------|--------|
| Regulation text | Art. 6(1)(a) AI Act — "[quoted text]" |
| Recitals | Recital 47 AI Act — "[quoted text]" |
| Commission guidelines | EC Guidelines on [Topic], Section X — "[quoted text]" |
| EDPB/EDPS opinions | EDPB Opinion 28/2024, Point X — "[quoted text]" |
| Codes of practice | GPAI Code of Practice, Measure X.Y — "[quoted text]" |
| Sector guidance | MDCG 2025-6, FAQ X — "[quoted text]" |

**Rules:**
- Lead with the direct answer, then the legal basis
- Quote operative text, don't just paraphrase
- When guidance is "in preparation" (see Watch List), say so explicitly
- When the regulation is ambiguous, cite the relevant recital and note uncertainty
- For German-speaking users, include the German article title on first reference: "Art. 9 (Risikomanagementsystem)"
- Regulation text > delegated acts > guidelines > codes of practice > opinions. When sources conflict, higher authority prevails
- Commission guidelines are non-binding soft law — note this when citing them

---

## Topic Router

For topics not listed here, use `Glob` to search `references/` by keyword, or check the `README.md` in each subdirectory.

| User Asks About | Read These Files |
|-----------------|-----------------|
| **Definitions** (Art. 3) | `core/regulation-title-I-general.md` → `guidelines/ai-system-definition.md` |
| **"Is this an AI system?"** | `core/decision-trees.md` (Tree A) → `guidelines/ai-system-definition.md` |
| **Prohibited practices** (Art. 5) | `guidelines/prohibited-practices-full.md` → `core/regulation-title-II-prohibited.md` |
| **High-risk classification** (Art. 6) | `core/decision-trees.md` (Tree B) → `core/annex-iii-high-risk.md` |
| **High-risk requirements** (Art. 8–15) | `core/regulation-title-III-high-risk.md` → `core/regulation-preamble-recitals.md` |
| **Risk management** (Art. 9) | `core/regulation-title-III-high-risk.md` → `standards/standardisation-overview.md` |
| **Data governance** (Art. 10) | `core/regulation-title-III-high-risk.md` → `opinions/edpb-opinion-28-2024.md` |
| **Transparency** (Art. 50) | `core/regulation-title-IV-transparency.md` → `codes-of-practice/transparency-code-draft-2.md` |
| **GPAI obligations** (Art. 51–56) | `core/regulation-title-V-gpai.md` → `codes-of-practice/gpai-code-final.md` |
| **GPAI systemic risk** | `core/regulation-title-V-gpai.md` (Art. 51) → `codes-of-practice/gpai-code-detailed.md` |
| **Provider obligations** | `core/regulation-title-III-high-risk.md` (Art. 16–25) |
| **Deployer obligations** | `core/regulation-title-III-high-risk.md` (Art. 26) |
| **Provider vs. deployer** | `core/decision-trees.md` (Tree C) → `compliance-guides/modifying-ai-classification.md` |
| **FRIA** (Art. 27) | `fria/article-27-fria.md` → `fria/ecnl-fria-guide.md` |
| **Conformity assessment** (Art. 43) | `core/regulation-title-III-high-risk.md` (Art. 43) → `standards/standardisation-overview.md` |
| **Penalties / fines** (Art. 99) | `core/regulation-title-VI-X-governance.md` (Art. 99) |
| **Timeline / deadlines** | `governance/implementation-timeline.md` |
| **FAQ** | `governance/ai-office-faq.md` → `governance/ec-qa-navigating-ai-act.md` |
| **AI Act + GDPR** | `opinions/edpb-opinion-28-2024.md` → `opinions/edpb-edps-joint-opinion-2026.md` |
| **Medical devices** | `sector-specific/medical-devices-ai.md` |
| **Banking / financial** | `sector-specific/banking-ai-implications.md` → `core/annex-iii-high-risk.md` (Area 8) |
| **Employment / HR** | `sector-specific/staffing-businesses-ai.md` → `core/annex-iii-high-risk.md` (Area 4) |
| **Law enforcement** | `law-enforcement/europol-ai-policing.md` → `core/regulation-title-II-prohibited.md` (Art. 5 RBI) |
| **Digital Omnibus** | `guidelines/digital-omnibus.md` → `opinions/edpb-edps-joint-opinion-2026.md` |
| **Standards / harmonised** | `standards/harmonised-standards-map.md` → `standards/standardisation-overview.md` |
| **Cybersecurity** | `cybersecurity/enisa-ai-cybersecurity.md` → `cybersecurity/enisa-cybersecurity-standardisation.md` |
| **Serious incidents** (Art. 73) | `templates/draft-guidance-art73-high-risk.md` → `templates/serious-incident-template-gpai.md` |
| **Germany** | `national/german-ai-bill.md` → `national/national-implementation-plans.md` |
| **National implementation** | `national/national-implementation-plans.md` → web search for latest |
| **Modifying AI systems** | `compliance-guides/modifying-ai-classification.md` |
| **SME / startups** | `compliance-guides/small-businesses-guide.md` |
| **Whistleblowing** | `compliance-guides/whistleblowing-ai-act.md` → `governance/whistleblower-tool.md` |
| **Copyright / TDM** | `compliance-guides/copyright-tdm-consultation.md` → `core/regulation-title-V-gpai.md` |
| **AI literacy** (Art. 4) | `compliance-guides/ai-literacy-repository.md` → `core/regulation-title-I-general.md` |
| **Regulatory sandboxes** | `national/regulatory-sandboxes.md` |
| **Open source** (Art. 2(12)) | `core/regulation-title-I-general.md` → `core/regulation-title-V-gpai.md` (Art. 53(2)) |
| **Recital interpretation** | `core/regulation-preamble-recitals.md` |

---

## Key Timelines

| Date | What Applies | Article |
|------|-------------|---------|
| **2 Feb 2025** | Prohibited practices (Art. 5) + AI literacy (Art. 4) | Art. 113(a) |
| **2 Aug 2025** | GPAI obligations (Art. 51–56) + governance + penalties | Art. 113(b) |
| **2 Aug 2026** | General application — Art. 50 transparency (50(1)/(3)/(4) + 50(2) for new systems) + most remaining provisions | Art. 113 *(50(2) legacy marking: 2 Dec 2026)* |
| **2 Dec 2027** | High-risk AI (Annex III) | Art. 6(2) *(Omnibus-postponed from 2 Aug 2026)* |
| **2 Aug 2028** | High-risk AI in Annex I products (medical devices, machinery, etc.) | Art. 6(1) *(Omnibus-postponed from 2 Aug 2027)* |

> **AI Omnibus 2026** postponed the high-risk effective dates. See [Commission guidelines references/commission-guidelines/](references/commission-guidelines/) for the 2026 draft Art. 6 classification guidelines, and `../ai-act-high-risk/references/ai-omnibus-timeline-postponements.md` for the citation chain.

---

## Watch List — Upcoming Official Sources

These are in preparation. When users ask about these topics, note that official guidance is expected and offer to search the web:

- Guidelines on high-risk classification (practical) — 2026
- Guidelines on transparency requirements (Art. 50) — 2026
- Guidelines on provider/deployer obligations — 2026
- **Official FRIA Template** (Art. 27) — 2026
- Guidelines on substantial modification — 2026
- **Joint EC/EDPB Guidelines on AI Act + GDPR interplay** — 2026

Source: `guidelines/guidelines-roadmap.md`

---

## Suite Integration

This skill is the deep reference layer for the 5 workflow skills. When a user's question suggests they need a structured assessment rather than a knowledge answer, recommend the right skill:

| User Need | Hand Off To |
|-----------|-------------|
| Structured classification assessment | `/ai-act-classifier` |
| Role determination (provider/deployer) | `/ai-act-roles` |
| Compliance checklist with RACI matrix | `/ai-act-obligations` |
| Formatted compliance documentation | `/ai-act-report` |
| Quick 15-minute triage | `/ai-act-quick` |

If the user provides an **Assessment Context** block from another skill, use it to tailor answers (focus on their risk tier, role, sector, jurisdiction).

---

## Cross-Framework Reference

The knowledge base covers the AI Act side of these overlaps. For the other framework (GDPR, MDR, etc.), rely on training knowledge or web search — the reference files do not contain non-AI Act regulation text.

| Overlap | AI Act Side | Reference File |
|---------|------------|----------------|
| **GDPR** — training data, DPIA | Art. 10, Art. 26(9) | `opinions/edpb-opinion-28-2024.md` |
| **Medical Devices** — MDR/IVDR | Art. 6(1), Annex I | `sector-specific/medical-devices-ai.md` |
| **Banking** — CRD, MiFID II | Annex III Area 5, 8 | `sector-specific/banking-ai-implications.md` |
| **Employment** — national labour law | Annex III Area 4 | `sector-specific/staffing-businesses-ai.md` |
| **Law enforcement** — LED | Annex III Area 6, Art. 5(1)(h) | `law-enforcement/europol-ai-policing.md` |
| **Copyright** — DSM Directive | Art. 53(1)(c)-(d) | `compliance-guides/copyright-tdm-consultation.md` |
| **Cybersecurity** — CRA | Art. 15 | `cybersecurity/enisa-ai-cybersecurity.md` |
| **Whistleblowing** — Directive 2019/1937 | Art. 87 | `compliance-guides/whistleblowing-ai-act.md` |

---

## Critical Reminders

1. **No hallucinated citations.** Never invent article numbers, recital numbers, or guideline sections. If you cannot find a provision in the reference files, say so.

2. **Source hierarchy.** Regulation text > delegated acts > Commission guidelines > codes of practice > EDPB opinions > sector guidance. Higher authority prevails on conflict.

3. **Evolving landscape.** Major Commission guidelines are still in preparation (see Watch List). Flag this uncertainty when answering in those areas.

4. **German-language support.** Every reference file includes a German title. For DE-speaking users: "Art. 9 (Risikomanagementsystem)", "Art. 5 (Verbotene Praktiken)".

5. **ISO/IEC gap.** ISO 42001 and ISO 23894 are relevant but paywalled — not in the knowledge base. Mention their existence when discussing standards alignment.

6. **Digital Omnibus.** The proposal would amend the AI Act significantly. When discussing affected provisions, flag both current law and proposed changes. See `guidelines/digital-omnibus.md`.

7. **Penalty tiers.** Art. 5 violations: EUR 35M / 7% turnover. High-risk requirements: EUR 15M / 3%. Incorrect info to authorities: EUR 7.5M / 1%. SME caps apply (Art. 99(5)–(6)).
