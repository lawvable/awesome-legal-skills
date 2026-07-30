---
name: "legal-analysis-forge-oliver-schmidt-prietz"
description: "EU Digital Regulation Legal Analysis Forge — generates a tailored expert prompt for structured legal analysis of an EU digital-regulation document, optionally executes it in-session, and always produces a plain-English explainer alongside the formal output. Handles Regulations, Directives, Commission Guidelines, EDPB Opinions, CJEU and AG judgments, national DPA decisions, codes of conduct, and draft consultations across the EU digital stack."
metadata:
  author: "Oliver Schmidt-Prietz"
  license: "agpl-3.0"
  version: "2026-06-09"
---

# Legal Analysis Forge

A prompt generator for structured legal analysis of EU digital regulation documents. The skill characterises a document, elicits the desired outcome and audience, and produces a tailored expert prompt. It optionally runs the prompt in-session and supports refinement.

## When to invoke

Invoke when the user:

- Provides a legal document (PDF, URL, pasted text) from the EU digital regulation stack and asks for analysis, feedback, a memo, a consultation response, a post, a briefing, or similar
- References a recent EU instrument, judgment, or guidance document and signals they want structured analysis rather than a quick answer
- Asks for an "effective prompt" for legal analysis of a specific document
- Is preparing a stakeholder consultation response, a board paper, a client memo, or a horizon-scan entry on a regulatory development

Do not invoke when:

- The user wants a quick factual answer about a regulation. Answer directly.
- The work is operational compliance (running an LIA, drafting a DPA, mapping AI Act obligations, building a RoPA). Route to the relevant compliance skill instead.
- The document is outside the EU digital regulation scope. Decline and explain scope.

## Scope

EU digital regulation only. Covers: GDPR, AI Act, Data Act, DGA, DSA, DMA, NIS2 (and Member State implementations including BSIG-neu), ePrivacy, CRA, DORA, eIDAS 2.0, PLD (Dir. 2024/2853), AI Liability Directive (when adopted), and adjacent secondary instruments (delegated acts, implementing acts, harmonised standards under Art. 40 AI Act and equivalents, codes of conduct under Art. 40 GDPR / Art. 56 AI Act / Art. 45 DSA). Out of scope: competition, IP, tax, employment, sectoral law not touching the digital stack.

## Workflow

Six steps. Steps 5 (Execute) and 6 (Refine) are optional and skipped where not needed. Skip elicitation where the answer is clear from the conversation; the goal is the minimum number of questions consistent with a precise prompt.

### Step 1 — Ingest

Read the document. Sources:

- **Uploaded PDF**: use the `pdf-processing-anthropic` skill if the file is not already in context
- **Pasted text**: read in chat
- **URL**: fetch via `WebFetch`; if the URL is an EUR-Lex page, prefer the CELEX-linked HTML
- **Reference by name**: confirm the precise document with the user (title, date, CELEX or ECLI) before proceeding

If the document is long, read at minimum: title, recitals, all substantive articles, annexes referenced in the substantive provisions, final provisions (entry into force, transitional, review), and any disclaimers limiting scope.

**Freshness check (automatic for drafts and consultation documents)**: where the document is a draft, a public consultation version, a Commission proposal, or any text labelled as preliminary, run a freshness check against authoritative sources (see Live research protocol below) before proceeding. The user may have provided a superseded version. If a finalised or later version exists, surface it and ask: *"Proceed with the version you provided, the later version, or both?"* Do not silently substitute documents.

### Step 2 — Characterise

Produce a structured one-screen characterisation. Load `references/document_taxonomy.md` for the catalog and characterisation signals. Required fields:

- **Instrument type** (Regulation, Directive, Commission Guidelines, EDPB Guidelines, CJEU judgment, AG Opinion, etc.)
- **Binding force** (binding / non-binding / quasi-binding via enforcement reliance)
- **Issuer and legal basis** (e.g. Commission under Art. 6(5) AI Act, EDPB under Art. 70 GDPR, Council and Parliament under Art. 16 TFEU)
- **Status** (in force / draft / under consultation / under appeal / pending entry into application / repealed)
- **Subject matter** and primary affected provisions (which Articles and Recitals of which instruments)
- **Sectoral interfaces** (where this touches adjacent EU digital instruments and sectoral law)
- **Contestable interpretive moves** (3–5 spotted on first read, with paragraph references)
- **Temporal application** (entry into force, date of application, transitional rules, sunset)
- **Plain-language summary** (2–3 sentences, no legal jargon beyond what is unavoidable, what this document is and why a regulated entity should care)

Present the characterisation to the user and ask: *"Is this characterisation correct? Anything missing or misclassified?"* Adjust before proceeding.

### Step 3 — Elicit

Ask at most three questions. Skip any answered in prior context. The single mandatory question is outcome type.

1. **Outcome type.** What is the deliverable? Options in `references/outcome_templates.md`: stakeholder consultation response, internal compliance memo, external client memo, public commentary (LinkedIn / blog / newsletter), conference talk preparation, internal risk assessment, litigation brief input, comparative analysis, horizon-scan entry, skill input.
2. **Audience.** Regulator, client, internal management, legal peers, public, or mixed.
3. **Stance.** Neutral analysis, defending position X, challenging position X, or open horizon-scan.

Optional follow-ups, asked only when unclear:

- Output language: EN / DE / both
- Length target
- Specific issues to scrutinise beyond those flagged in Step 2
- Comparative dimension on or off (compare with prior law or sister instrument)
- Register override (default is the dry practitioner register defined in `references/analytical_canon.md`)

### Step 4 — Generate prompt

Load `references/outcome_templates.md` and `references/analytical_canon.md`. Assemble the prompt with the following blocks in order:

1. **Role.** Expertise markers tailored to outcome type (from `outcome_templates.md`)
2. **Context.** Document title, type, issuer, legal basis, status, date, link or attachment reference
3. **Task.** Specific outcome with audience and length target
4. **Analytical framework.** General legal interpretation rules from `analytical_canon.md` plus document-specific scrutiny points from Step 2
5. **Specific provisions warranting scrutiny.** The interpretive moves spotted in Step 2, with paragraph references and the question to address for each
6. **Citation conventions.** From `analytical_canon.md`
7. **Register constraints.** From `analytical_canon.md`
8. **Output structure.** Tailored to outcome type (from `outcome_templates.md`)
9. **Self-check protocol.** From `analytical_canon.md`

Save the prompt to `./[doc_slug]_prompt_[outcome_slug].md` in the user's current working directory (or to a target directory the user has specified). Present the file. Also output the prompt inline in chat so the user can copy it directly.

`doc_slug` is a stable, descriptive slug derived from the document title (e.g. `ai_act_art6_high_risk_guidelines_draft_2026`). `outcome_slug` is short (e.g. `consultation`, `memo`, `linkedin_de`, `briefing`).

### Step 5 — Execute (optional)

If the user signals they want the analysis run in-session, use the generated prompt to produce the analysis directly. Save to `./[doc_slug]_analysis_[outcome_slug].md` in the user's current working directory and present.

Alongside the formal analysis, always produce a **plain-English explainer** for the user of the skill:

- **150–300 words. This is a hard upper bound, not a soft target.** If you find yourself exceeding 300 words, cut — do not negotiate with yourself that "this analysis was complex enough to justify more". A 300-word ceiling forces the explainer to do the one job it is for: tell the practitioner, in one screenful of plain language, what the document is and what the analysis found. Anything longer is the formal analysis duplicating itself. Count words before saving; if over 300, revise down.
- Plain language; no legal jargon beyond what is unavoidable
- Explains what the document is, what the analysis found, what remains uncertain
- Saved as `./[doc_slug]_plain_english_[outcome_slug].md` in the user's current working directory
- Audience is the practitioner using the skill, not the deliverable's downstream audience

After producing both, offer integration into the formal deliverable in any of the following forms (the user decides):

- Executive summary at the top of the deliverable
- Sidebar or call-out box
- Annex
- Client-facing cover note
- Not integrated (kept separate for the user's own orientation)

If running the analysis, apply the self-check protocol from `analytical_canon.md` before delivery. Do not skip this step.

### Step 6 — Refine

Handle refinement requests without restarting the workflow. Common requests:

- **"Rewrite for a different audience"** — adjust register and structure, keep substance. Update `outcome_slug` accordingly.
- **"Rewrite as a different outcome type"** — switch the template; re-run Step 4 with new outcome type only.
- **"Translate to German"** — use the German legal terminology guidance in `analytical_canon.md`; preserve all citations in original form.
- **"Tighten"** — reduce length while keeping all substantive findings; do not drop citations.
- **"Expand on point X"** — deepen specific analysis; do not pad other sections.
- **"Add comparative dimension"** — introduce comparison with named prior law or sister instrument.
- **"Different stance"** — re-run Step 4 with revised stance parameter.

Save refinements with `_v2`, `_v3` suffixes. Keep prior versions; do not overwrite.

## Live research protocol

The skill offers live research on authoritative sources whenever the AI's training data is at risk of being stale, incomplete, or unverifiable. The goal is to prevent reliance on potentially outdated training data in legal output.

### When live research is offered

- The user provides a draft document that may have been superseded by a final version (automatic in Step 1)
- The analysis turns on a citation the AI cannot verify from the prompt context
- The user signals the analysis must be submission-ready (consultation response, litigation input, board paper, client memo)
- The user requests it explicitly
- The AI is uncertain whether a transposition deadline, application date, or amendment has come into effect
- The AI is uncertain whether a CJEU case it would otherwise cite is the most recent on the point

Live research is opt-in. Where the skill offers it and the user declines, the skill flags the gap explicitly in the output rather than guessing.

### Authoritative sources

**Primary EU sources (cite directly)**:

- `eur-lex.europa.eu` — Official Journal, EU instruments, consolidated texts, CELEX records
- `curia.europa.eu` — CJEU and General Court judgments, AG Opinions, Orders
- `edpb.europa.eu` — EDPB guidelines, opinions, binding decisions
- `ec.europa.eu` and its sub-domains — Commission communications, guidelines, draft acts
- `digital-strategy.ec.europa.eu` — AI Office outputs, AI Act resources
- `enisa.europa.eu` — ENISA guidance (NIS2, CRA)
- `berec.europa.eu` — BEREC outputs
- `consilium.europa.eu` and `europarl.europa.eu` — Council and Parliament documents during legislative procedure

**Primary national sources (cite directly)**:

- National DPA websites (e.g. bfdi.bund.de, datenschutzkonferenz-online.de, cnil.fr, garanteprivacy.it, autoriteitpersoonsgegevens.nl, aepd.es)
- National official gazettes for transposition law (e.g. bundesgesetzblatt.de, legifrance.gouv.fr, gazzettaufficiale.it)
- National courts where ECLI-enabled
- National competent authorities designated under NIS2, CRA, AI Act, DSA, DMA

**Permitted for context only (do not cite in place of primary)**:

- Commercial trackers (artificialintelligenceact.eu, gdprhub.eu)
- Law firm client alerts
- Peer-reviewed academic journals
- IAPP and similar professional bodies

**Excluded**:

- Wikipedia
- LinkedIn and other social media
- News articles (except solely to confirm a publication date)
- Aggregator blogs and unsourced commentary

### Procedure

1. Identify the specific question requiring research
2. Search the authoritative source most likely to have the answer
3. Fetch the relevant page or document
4. Cite the source with date of access and direct URL where the page is non-paginated; with paragraph, article, or section reference where the source provides one
5. In the output, mark live-verified citations as such, e.g. *"[live-verified, accessed YYYY-MM-DD]"*

### Freshness check (automatic for drafts)

For draft consultation documents, Commission proposals, and any text labelled as preliminary, the freshness check in Step 1 runs without user prompting:

1. Identify the document title and date
2. Search the issuer's authoritative source for a finalised or later version
3. If a later version exists, present both versions to the user and ask which to use
4. Proceed only after the user has chosen

### Failure mode

If live research returns inconclusive results (no clear authoritative answer, conflicting sources, source unreachable), report the inconclusiveness and fall back to flagging the gap. Never extrapolate from inconclusive research to a definitive citation.

## Integration with other skills

If the characterisation surfaces a downstream operational task, suggest the relevant existing skill rather than absorbing the task into this one:

- GDPR Art. 6(1)(f) balancing → suggest the LIA skill
- International transfer assessment → suggest the TIA skill
- Art. 28 processing arrangement drafting or review → suggest the DPA skill
- RoPA update → suggest the ROPA skill
- AI Act classification or obligations mapping → suggest the AI Act skill suite
- NIS2 scope or gap analysis → suggest the NIS2 Navigator skill
- Breach scenario → suggest the Breach Sentinel skill
- Data Act compliance → suggest the Data Act skill

The suggestion is offered after the analysis is delivered, not before — the analysis comes first.

## File output conventions

All outputs are written to the user's current working directory unless the user specifies a target directory. Naming:

- `[doc_slug]_prompt_[outcome_slug].md` — generated prompt
- `[doc_slug]_analysis_[outcome_slug].md` — executed analysis
- `[doc_slug]_characterisation.md` — optional, the Step 2 output saved as a standalone artifact when the user wants it

Use `_v2`, `_v3` for refinements. Stable slugs across versions allow tracking a single document through multiple analyses.

## Default behaviours

- **Register**: dry practitioner — Oliver's house style codified in `references/analytical_canon.md`; overridable on request.
- **Language**: match the document language for the prompt; output language per user choice in Step 3.
- **Live research**: offered whenever needed; opt-in by the user; authoritative sources only. Automatic freshness check for drafts and consultation documents in Step 1.
- **Plain-English explainer**: produced alongside every executed analysis; integration into the deliverable is the user's choice.
- **Length targets**: the numbers in `references/outcome_templates.md` are defaults, not constraints. Adjust to the length of the source document and the depth of the task.
- **Citation depth, quotation, uncertainty, hallucination control**: see `references/analytical_canon.md`. The skill enforces those rules in every executed analysis.

## Reference files

- `references/document_taxonomy.md` — instrument types, binding force, characterisation signals, what to look for per type
- `references/outcome_templates.md` — prompt skeletons per outcome type with roles, structures, and registers
- `references/analytical_canon.md` — general legal interpretation rules, register constraints, citation conventions, self-check protocol, bilingual handling

## More EU regulation skills

This skill works standalone. Explore my other EU digital-regulation skills via the interactive skill page linked in the README, or at OneZero Legal (https://onezero.legal).
