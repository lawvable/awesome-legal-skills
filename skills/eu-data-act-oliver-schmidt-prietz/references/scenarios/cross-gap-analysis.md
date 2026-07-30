# cross-gap-analysis

**Anchor:** Any × cross-chapter × gap analysis. The card structures a multi-chapter compliance review of an organisation's Data Act posture. It walks the seven-step method for each engaged chapter and produces a structured gap-analysis table per chapter, following `references/method/house-style.md` "Gap analysis or compliance check" deliverable conventions.

**Routes from:**

- "We need a Data Act readiness assessment for [product / business line]."
- "Where are our compliance gaps across Chapters II, IV, and VI?"
- "Run a Data Act gap analysis for our SaaS connected-product offering."
- "We're preparing for 12 September 2025 application; what do we need to fix?"
- "Compare our current state to the Data Act requirements across the stack."

**Adjacent cards (route there instead if the facts indicate):**

- Single-chapter scoping question: route to the chapter-specific card (e.g. `ch2-trade-secret-stages-1-2.md` for a trade-secret-only question; `ch7-third-country-request.md` for an Art. 32 request).
- The question is "does the Data Act apply to us?", not a gap analysis: route to a scoping-only response. The seven-step method's Step 1 is the answer; a full gap analysis is over-build.
- The boundary with GDPR is the principal concern: route to `cross-gdpr-boundary.md`.
- The question is about how the Digital Omnibus would change a gap analysis: route to `cross-omnibus-impact.md`.

---

## Canonical fact pattern

An organisation is in scope of the Data Act under Art. 1(3). It is one or more of: a manufacturer of connected products placed on the Union market; a provider of related services; a data holder; a data recipient; a provider of data processing services; a participant in data spaces or vendor of smart contracts. It has not previously completed a Data Act compliance posture review, or its prior review is out of date.

The deliverable is a gap analysis: the difference between the organisation's current compliance state and the Data Act's required state, with concrete actions and owners. The deliverable is internal to the organisation and is typically the input to a remediation plan.

The scope of the gap analysis covers the chapters engaged by the organisation's activities. A connected-product manufacturer with a SaaS related service typically engages Ch II (user access), Ch IV (unfair B2B terms in the data-sharing contract), Ch VI (switching for the SaaS), and Ch VII (third-country governmental access for the SaaS hosting). It may also touch Ch III (mandatory B2B sharing under other Union law) and Ch V (public-sector exceptional need) on a watch-list basis.

---

## Critical disciplines

These three points distinguish a useful Data Act gap analysis from a checkbox exercise.

- **One chapter per pass.** Each engaged chapter gets its own seven-step walk, its own role map, and its own gap table. Blending chapters into a single matrix produces analytical errors because the operative rules differ. A finding under Ch II ("the user has not been told about data access rights") and a finding under Ch VI ("the customer cannot retrieve exportable data on termination") are different obligations on different actors and need separate remediation tracks.
- **Role per phase, not role overall.** An organisation typically plays multiple Data Act roles across product lines, customer relationships, and lifecycle phases. The role map captures the role for the specific obligation under review, not a single overall role label. The same organisation is data holder for its connected product, provider for its SaaS layer, customer for its cloud infrastructure, and possibly user for the connected products it consumes from suppliers. See `references/gotchas.md` entry 2 (manufacturer is not always the data holder) and the role-bifurcation discipline in `references/method/analysis-method.md`.
- **Current law before proposal.** The gap analysis assesses the organisation against the current Data Act as published. The Digital Omnibus proposal (COM(2025) 833 final, 19 November 2025) is awareness only and goes in a separate "watch-list" column or footer. Building the gap analysis against proposed amendments produces an analysis that may become wrong if the proposal is amended or withdrawn. See `references/gotchas.md` entry 20 and `cross-omnibus-impact.md`.

---

## The seven-step walk (run per engaged chapter)

The method runs once per chapter. The output presents the seven-step results for each chapter and consolidates into the gap table.

### Step 1: Scope check

Run the Art. 1(2), 1(3), and 1(6) scope tests for each chapter independently. A chapter may apply (the organisation is in scope) or not (the organisation falls within an Art. 1(6) carve-out, or the chapter's personal-scope conditions are unmet, or the organisation has no in-scope data).

For Ch II, additionally run the Art. 2(5) connected-product test, the Art. 2(6) related-service test, and the Art. 2(22) "placed on the Union market" test. Connected products manufactured in the EU for export are out of scope; mobile products merely circulating in the EU are not placed (FAQ Q9). For Ch VI, run the Art. 2(8) data-processing-service test. For Ch VII, run Art. 2(8) plus the "non-personal data held in the Union" location test.

### Step 2: Chapter identification

Confirm the chapter and list the operative articles engaged. A connected-product gap analysis under Ch II will principally engage Arts. 3, 4 and 5, with the Art. 4(2) safety-security handbrake and the Art. 4(6) to (8) and Art. 5(9) to (11) trade-secret ladders as conditional sub-modules. A Ch VI analysis will engage Arts. 23 to 31 with the Art. 30 functional-equivalence asymmetry (IaaS vs PaaS / SaaS) and the Art. 31 custom-built carve-out as conditional sub-modules. A Ch IV analysis will engage Arts. 13, 14 (unilateral termination right where Art. 13 is breached), 12 (purpose and modalities), and the Commission's Art. 41 non-binding model contractual terms.

### Step 3: Role mapping

Map the organisation against each engaged chapter, entity-by-entity, phase-by-phase. Show as a table. Where the organisation is the manufacturer, the controller, the data holder, and the trade-secret holder for the same dataset, the gap analysis confirms all four roles in the table; it does not collapse them.

| Entity | Phase / activity | Data Act role | GDPR role (if personal data) | Other |
|--------|-------------------|---------------|------------------------------|-------|
| [Organisation, business unit 1] | [e.g. design and manufacture of connected product] | Manufacturer (Art. 1(3)(a)); data holder (Art. 2(13)) | Controller for personal data generated by the product | Trade-secret holder under Directive (EU) 2016/943 |
| [Organisation, business unit 2] | [e.g. SaaS related-service operation] | Provider of related service; data holder for related-service data | Controller (or processor, depending on whether the organisation determines purposes and means) |  |
| [Organisation, business unit 3] | [e.g. consumption of IaaS for hosting] | Customer of data processing service (Art. 2(30)) | Controller / processor depending on the data |  |
| [Customer enterprise 1] | [e.g. fleet operator using the connected product] | User (Art. 2(12)) | Controller (per Recital 34 if not the data subject) |  |
| [End user, natural person] | [e.g. driver of the connected vehicle] |  | Data subject |  |

Recital 34 places the non-data-subject user in the controller role. Where the organisation supplies connected products to enterprise customers, the gap analysis flags the customer's parallel GDPR controller obligations and confirms that the organisation's Art. 4(12) and 5(7) legal-basis controls account for that role split. See `references/gotchas.md` entry 3.

### Step 4: Fact-category sorting

Classify the data in scope across the standard dimensions: personal vs non-personal; raw or pre-processed vs derived (Recital 15); product data vs related-service data; readily available vs not (Art. 2(17)); content vs non-content (Recital 16); trade-secret vs not. The classification table is part of the gap-analysis deliverable; the operative rules under Steps 5 and 6 depend on it.

For a multi-chapter gap analysis, the data-category table typically appears once at the start of the deliverable and is referenced from each chapter section. Where chapters apply to different data subsets (Ch II to product/related-service data only; Ch VI to data processed by data processing services; Ch VII to non-personal data held in the Union), the per-chapter sections clarify which subset is engaged.

### Step 5: Limb-by-limb application of the operative articles

Run the limb-by-limb tests for each operative article. The depth of the test depends on the article's structure:

- **Multi-limb cumulative tests** (e.g. Art. 2(5) connected product; Art. 4(8) refusal; Art. 15(1)(b) exceptional need; Art. 31(1) custom-built carve-out): each limb assessed independently. Findings name the failing limb.
- **Closed-list prohibitions** (Art. 5(3) gatekeeper exclusion; Art. 6(2) third-party prohibitions): each item assessed. Closed-list framing means unlisted behaviours are not prohibited under that provision (other Union law may still apply). See `references/gotchas.md` entry 12.
- **Illustrative lists** (Recital 31 objective elements; FAQ Q22a technical and practical access requirements): each item considered as an example; the operative test is the principle the list illustrates. See `references/gotchas.md` entry 8.

The gap-analysis deliverable does not enumerate every limb in the body of the document. The body identifies the relevant articles and the findings; the per-limb analysis sits in working papers, referenced from the deliverable where the analytical detail matters.

### Step 6: Cross-regime gate check

Run the gates for each chapter:

- **GDPR overlay** (`references/gates/gdpr-overlay.md`): always engaged where personal data is in scope. The gate adds findings to the gap table, typically under a "GDPR overlay" heading.
- **Trade Secrets Directive overlay** (`references/gates/trade-secrets-directive.md`): engaged if any data is trade-secret-protected. Gap-table findings on stage-1 safeguards, identification of trade secrets in metadata, technical and organisational measures, and refusal-letter readiness.
- **DMA gatekeeper exclusion** (`references/gates/dma-gatekeeper.md`): engaged if the organisation receives Art. 5 third-party requests or onward-shares data under Art. 6(2)(d). Gap-table findings on recipient screening and contract clauses.
- **Sectoral lex specialis** (`references/gates/sectoral-lex-specialis.md`): engaged if the organisation's products fall in a regulated sector (vehicles, medical devices, energy, financial services, AI systems, eIDAS, NIS2, CRA). Gap-table findings flag the sectoral regime and the interaction with the Data Act.
- **Member State implementing law** (`references/gates/member-state.md`): engaged for the Member State(s) of establishment and the Member State(s) where the customers are located. Gap-table findings on competent-authority designation, dispute-settlement bodies, and any national derogations.

### Step 7: Synthesis with current-law-vs-proposal

For each chapter, the gap analysis states the current law as the operative requirement. The Digital Omnibus proposal (COM(2025) 833 final, 19 November 2025) is flagged in a "watch-list" column on the gap table where the proposal materially affects the chapter (Arts. 4(8) and 5(11) refusal grounds; Art. 15 Ch V circumstances; Art. 25 early-termination penalties; Art. 31 custom-built carve-out; Art. 36 smart contracts; consolidation absorbing DGA, ODD, FFD, P2B). The watch-list entries inform risk and timing decisions; they do not change current-state compliance.

---

## Decision point

After Steps 5 and 6 per chapter, the gap analysis yields a structured table per chapter and a consolidated remediation backlog. The deliverable's output structure:

1. **Per-chapter gap tables.** One table per engaged chapter, following the house-style "Gap analysis or compliance check" format.
2. **Consolidated remediation backlog.** Cross-chapter prioritisation (criticality, regulatory exposure, dependency on other actions).
3. **Watch-list section.** Digital Omnibus and other forthcoming changes (e.g. EDIB-advised guidelines on Art. 9(5) compensation, on Art. 32(3) conditions; Commission delegated acts under Art. 33; harmonised standards under Art. 35).
4. **Assumptions section.** Any unverified facts the analysis proceeded on (per `references/method/house-style.md`).

---

## Output skeleton: gap analysis deliverable

Markdown deliverable. Length depends on chapters engaged; a four-chapter gap analysis runs 8 to 15 pages typically. The deliverable is internal-facing and assumes the reader has a working Data Act vocabulary.

```
# Data Act gap analysis: [Organisation / scope] as of [Date]

## Executive findings
[Lead paragraph: the three to five most consequential gaps. No
restatement of the prompt. The reader is the project sponsor or
general counsel; assume working knowledge of the Data Act.]

## Scope of the analysis
- Organisation: [legal entity, business units in scope]
- Chapters engaged: [list]
- Chapters out of scope: [list, with reason; typically Art. 1(6)
  carve-out or no in-scope activity]
- Reference date: [as of date]
- Data Act version: Regulation (EU) 2023/2854 as published in the OJ
  on 22 December 2023, no amending act adopted as of the reference
  date.

## Assumptions
- [Assumption 1]. If [contrary fact], [how findings shift].
- [Assumption 2]. If [contrary fact], [how findings shift].

## Role mapping
[Table of entities × phases × roles, per Step 3 above.]

## Data classification
[Table of data categories × dimensions, per Step 4 above.]

## Chapter [N]: [Chapter title]

### Operative articles engaged
[Short list: Arts. X, Y, Z. Recitals A, B.]

### Gate results
- GDPR overlay: [engaged / not engaged]. [If engaged, principal
  findings.]
- Trade Secrets Directive overlay: [engaged / not engaged].
- DMA gatekeeper: [engaged / not engaged].
- Sectoral lex specialis: [engaged / not engaged; sector].
- Member State implementing law: [list of relevant MS and findings].

### Gap table

| Issue | Current state | Required state | Action | Owner | Deadline |
|-------|---------------|----------------|--------|-------|----------|
| [Specific issue, with article citation] | [What the organisation does today] | [What the Data Act requires] | [Concrete action] | [Role / function in the organisation] | [Date or trigger] |

[Repeat one row per gap, sorted by criticality.]

### Watch-list (Digital Omnibus and forthcoming changes)
- [Watch-list item 1: which provision, what the proposal would do,
  current status, expected impact.]

[Repeat Chapter section for each engaged chapter.]

## Consolidated remediation backlog
[Cross-chapter prioritisation. Recommend a sequence and owner.]

## Recommendations
[Concrete and specific. Not "consider", not "explore". "Notify the
competent authority of [Member State]", "Update the [contract /
process / control] by [date]".]
```

---

## Gap-table examples (illustrative content for the per-chapter tables)

Examples below show the granularity the gap table targets. They are not a closed list; the gap table includes all findings the seven-step walk produces for the chapter.

### Ch II example rows

| Issue | Current state | Required state | Action | Owner | Deadline |
|-------|---------------|----------------|--------|-------|----------|
| Art. 3(2) pre-purchase information | Product pages do not list data categories generated, frequency, technical means, or retention | Information provided to user prior to contract conclusion | Update product pages and pre-purchase flows | Product marketing + DPO | [Date] |
| Art. 4(1) user access infrastructure | No user-facing portal; ad-hoc support response on request | Continuous, real-time, machine-readable access where technically feasible | Build user data-access portal with structured-format export | Engineering + product | [Date] |
| Art. 4(6) trade-secret identification | Trade-secret-protected data not separately tagged in product schema; safeguards not in template terms | Trade secrets identified including in metadata; proportionate technical and organisational safeguards proposed in writing | Tag trade-secret-protected fields; draft Art. 4(6) safeguards clause for user terms | Engineering + legal | [Date] |
| Art. 4(12) GDPR legal basis for B2B user disclosure | No documented legal basis for enterprise-user disclosure of driver personal data | Valid Art. 6 GDPR legal basis; Art. 9 condition where applicable; Art. 5(3) ePrivacy if terminal-equipment access | LIA or alternative; consider anonymisation route | DPO + legal | [Date] |

### Ch VI example rows

| Issue | Current state | Required state | Action | Owner | Deadline |
|-------|---------------|----------------|--------|-------|----------|
| Art. 25(2)(a) maximum transitional period | Standard customer contract specifies 6-month transition | 30 days, extendable to 7 months on demonstrated technical unfeasibility | Rewrite Art. 25(2) clauses; update standard terms | Legal + commercial | [Date] |
| Art. 25(2)(d) maximum notice period | Notice period 6 months | 2 months maximum | Update notice period in standard terms | Legal | [Date] |
| Art. 25(2)(g) retrieval period | Data retention post-termination unspecified | 30-day minimum retrieval | Specify 30-day retrieval in standard terms; update operations to support | Legal + operations | [Date] |
| Art. 30 functional equivalence (IaaS lines only) | Functional-equivalence support not implemented | IaaS lines: functional equivalence on switch; PaaS / SaaS lines: open interfaces and exportable data export under Art. 30(5) | Scope IaaS vs non-IaaS lines; build the asymmetric obligations into the technical roadmap | Engineering | [Date] |

### Ch VII example row

| Issue | Current state | Required state | Action | Owner | Deadline |
|-------|---------------|----------------|--------|-------|----------|
| Art. 32 third-country governmental access framework | No documented framework; ad-hoc legal review on receipt of order | Documented framework covering Art. 32(1) preventive measures; Art. 32(2) and (3) decision tree; Art. 32(3) consultation channel (Bundesjustizamt in Germany; Bureau de l'entraide pénale internationale in France); Art. 32(4) minimisation; Art. 32(5) customer notification | Build framework; identify national-body counterparts; integrate into incident-response runbook | Legal + security + DPO | [Date] |

---

## Citations to load

The deliverable cites the regulation throughout. When this card fires, quote selectively from:

- `sources/regulation-2023-2854.md` for every article and recital the gap analysis applies. Per-chapter sections in the deliverable cite the operative articles directly.
- `sources/faq-v1-4.md` Q3 (Ch III scope), Q4 / Q34a (Ch II temporal scope), Q8 / Q9 (placed on the Union market), Q10 (related-service test), Q18 (data portability complementarity), Q21 (manufacturer not always the data holder), Q25 / Q25a (Art. 4(2) handbrake, Case B legal basis), Q33 (no Data Act right to erasure of non-personal data), Q36 (DMA gatekeeper exclusion), Q60 / Q61 / Q62 / Q63 (Ch VII / Art. 32), Q72 (Art. 9(5) compensation guidelines forthcoming). Frame each as Commission interpretation.
- `references/gates/*.md` for the gate analyses. The gap-analysis deliverable summarises gate findings; the gates carry the detail.
- `sources/digital-omnibus-amendments-tracker.md` for the watch-list column.

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/method/analysis-method.md` (the seven-step flow, run per chapter).
- `references/method/house-style.md` (output discipline; in particular the "Gap analysis or compliance check" deliverable conventions and the table format).
- `references/gates/gdpr-overlay.md`, `trade-secrets-directive.md`, `dma-gatekeeper.md`, `sectoral-lex-specialis.md`, `member-state.md` (load conditionally per chapter).
- `references/gotchas.md` (the cross-cutting failure-mode catalogue; check every entry against every chapter's gap-table findings).
- `cross-gdpr-boundary.md` (for the GDPR-Data Act boundary findings in the gap table).
- `cross-omnibus-impact.md` (for the watch-list framing and the proposal-status discipline).
- Per-chapter scenario cards as they are drafted (e.g. `ch2-trade-secret-stage-3-refusal.md`, `ch2-trade-secret-stages-1-2.md`, `ch7-third-country-request.md`); the gap analysis cites the cards for specific findings.

---

## Drafter notes

- **One chapter per pass; consolidate at the end.** Resist the temptation to merge findings into a cross-chapter matrix during the analysis. The merge happens in the consolidated remediation backlog, after each chapter's gap table is complete. Merging earlier produces analytical errors because chapters' operative rules differ.
- **Owners are roles, not individuals.** The "Owner" column in the gap table names the function (DPO, Legal, Engineering, Product, Commercial, Operations, Security). Naming individuals dates the deliverable and creates HR-management noise. The remediation plan can map functions to individuals separately.
- **Deadlines reference the Data Act schedule.** Art. 50 deadlines (12 September 2025 general application; 12 September 2026 design obligation under Art. 3(1); 12 September 2027 unfair-terms application to legacy contracts) are absolute and known. Internal deadlines should anchor to these, not to abstract "Q3 2026" labels that drift.
- **The watch-list is not a remediation backlog.** The Digital Omnibus proposal items belong in a separate column or section. They inform risk and roadmap decisions but do not produce current-state remediation actions, because the current law has not changed. See `references/gotchas.md` entry 20.

---

## Note on structural invention

The prototype card (`ch2-trade-secret-stage-3-refusal.md`) is single-chapter, single-scenario. The gap-analysis card is structurally different: it runs the seven-step method multiple times (once per engaged chapter) and produces a structured tabular deliverable rather than a refusal letter or memorandum. The card preserves the prototype's ten-section structure (anchor; routes from; adjacent cards; canonical fact pattern; critical disciplines; the seven-step walk; decision point; output skeleton; citations to load; cross-references; drafter notes), with the seven-step walk written generically (per-chapter) and the output skeleton extended into a multi-chapter deliverable with the per-chapter table format mandated by `references/method/house-style.md`. The "Gap-table examples" section is added because the table format is the operative output, and worked rows let the drafter calibrate granularity without re-inventing the format on each use.
