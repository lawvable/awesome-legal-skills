---
name: regulatory-deal-card-generator-patrick-munro
description: Generates standalone interactive HTML "deal cards" that translate complex regulations into negotiation-ready reference tools, systematically distinguishing mandatory obligations from negotiable implementation choices. Use when the user needs an interactive regulatory guide for (1) contract negotiation support, (2) client education or internal training, (3) regulatory briefings for commercial stakeholders, or (4) structured comparison between required and flexible compliance paths. Primary focus on EU digital regulation (Data Act, AI Act, CRA, DORA, NIS2, GDPR) but the structural pattern transfers to any regulation where separating hard obligations from implementation choice is the point. Supports bilingual output where the jurisdiction calls for it.
metadata:
  author: "Patrick Munro"
  license: "agpl-3.0"
  version: "2026-04-25"
---

# Regulatory Deal Card Generator

## Purpose

Produces a single self-contained HTML file that presents a regulation as an interactive "deal card" for use in negotiation, advisory, or training settings. The output clearly separates what the law compels from what it leaves open to the parties. This matters because most regulatory guides collapse the two together, which wastes negotiation capital on obligations that are not negotiable and leaves genuine flexibility on the table.

## When to use

- Preparing for a contract negotiation where a specific regulation drives material clauses
- Briefing a commercial counterparty or client on what a regulation actually requires of them
- Building internal training material that needs to outlast a single briefing session
- Producing a client-facing deliverable that survives being emailed around without losing its structure
- Any situation where the question "must we, or may we?" needs to be answered clause-by-clause

## Output format

A single HTML file, inline CSS and JS, no external dependencies beyond optional web fonts. Offline-capable. Print-friendly. Designed to be opened in a browser and used as a working tool, not a static reference.

Core visible components:

- Sticky navigation across regulation sections
- Per-requirement rows showing: the requirement with its article reference, the required response, the negotiable aspects, and a worked example
- Collapsible detail blocks for secondary material
- Hover tooltips for defined terms
- Risk badges (high / medium / low) per requirement
- Optional bilingual toggle where applicable

## Core structural rule

Every row in the deal card answers three questions, in this order:

1. **What does the regulation mandate?** (with article citation)
2. **What is fixed about how it must be done?** (the non-negotiable floor)
3. **What is open to negotiation?** (implementation mechanism, timing, allocation between parties, documentation format, etc.)

A row that cannot distinguish (2) from (3) is a row that has not been thought through. Force the distinction even when it is uncomfortable, and flag genuine ambiguity explicitly rather than hiding it in neutral prose.

## Workflow

1. **Identify the regulation.** Confirm official citation, current consolidated version, and date of last amendment.
2. **Verify the text.** Cross-check against the primary source (EUR-Lex for EU instruments, official gazette or equivalent for national law). Do not rely on secondary summaries. If the regulation is recent or amended, check for corrigenda.
3. **Structure by business logic, not article order.** Users read deal cards by topic (data access, incident reporting, third-party risk) rather than by article number. Group accordingly and cite articles within each topic.
4. **Classify each requirement.** For each provision, write down the mandatory minimum, then separately write down what the parties can decide for themselves. Resist the temptation to collapse them.
5. **Add a worked example per requirement.** A concrete scenario showing what compliance looks like in practice, and where relevant a counter-example showing what non-compliance looks like.
6. **Build the HTML.** Use the pattern in `references/html-template.md`. Keep the file self-contained.
7. **Test interactivity.** Every collapsible, tooltip, and filter should work in a cold browser with no dev tools open.
8. **Add version metadata.** Regulation citation, date verified, and a visible note that the user should re-verify before relying on the output for any binding decision.

## Design principles

### Negotiation-focused framing

Translate legal language into three registers:

- Legal: "The data holder shall make data available to the user without undue delay."
- Business: "You must provide user access promptly; what counts as promptly, and in what format, is yours to negotiate."
- Risk: "Failure to provide access exposes you to administrative fines and a private right of action by users."

### Article-level precision

Always cite specific articles. Be precise about whether a provision sits in the main text, an annex, or an implementing act. Where the provision depends on a delegated act that has not yet been adopted, say so.

### Example-rich rows

Aim for at least one example per major requirement. Where a regulation has been the subject of enforcement action or published guidance, incorporate it. Where the regulation is so new that no enforcement exists, say that too, rather than padding with hypotheticals presented as settled practice.

## Severity framework

Every row carries a visible risk level:

| Severity | Meaning |
|---|---|
| HIGH | Material administrative fines, criminal penalties, or private rights of action on the table |
| MEDIUM | Administrative sanctions possible, supervisory action likely |
| LOW | Best practice; non-compliance unlikely to be directly sanctioned but may affect later enforcement posture |

Risk level is about the consequence of non-compliance, not about how easy compliance is.

## HTML template

See `references/html-template.md` for the full template, including:

- Base CSS with design tokens
- Navigation and panel structure
- Problem row layout with required / negotiable split
- Collapsible sections and tooltip pattern
- Risk badge styling
- Print and mobile stylesheets
- Bilingual toggle pattern

The template is a starting point. Adapt the copy and structure to the specific regulation. Keep the visual consistency.

## Bilingual output

For jurisdictions where bilingual material is standard (German and English for DACH commercial work, French and English for dual-filing contexts, etc.), the template supports a language toggle. Two patterns:

- **Parallel columns**: suited to terminology mapping and defined-term glossaries
- **Language toggle**: suited to full parallel text where both versions are authoritative

Do not machine-translate legal text. If you cannot produce accurate parallel legal text in both languages, produce one language and note the translation gap.

## Quality checklist

Before finalizing:

- [ ] All article references verified against the primary source
- [ ] Mandatory vs. negotiable distinction made explicit for every row
- [ ] At least one worked example per major requirement
- [ ] Every defined term in the deal card has a tooltip definition
- [ ] Navigation works across all panels
- [ ] Search and filter (if included) work across all content
- [ ] Print stylesheet produces a usable printed document
- [ ] Mobile layout is legible without horizontal scroll
- [ ] Regulation version and verification date are visibly displayed
- [ ] Limitations and open questions in the regulation are flagged honestly

## Limitations and disclaimers

The deal card is a negotiation and training aid. It is not legal advice and does not substitute for qualified counsel on specific matters. Include a visible disclaimer in the output along these lines:

> "This deal card reflects the regulation as of [date]. Regulations evolve; guidance and enforcement practice evolve faster. Verify current text before relying on this document for any binding decision. Specific matters require qualified legal counsel in the applicable jurisdiction."

## Output location

Save generated files with a clear naming convention:

```
[regulation-short-name]-deal-card-[YYYY-MM-DD].html
```

Example: `data-act-deal-card-2026-04-23.html`
