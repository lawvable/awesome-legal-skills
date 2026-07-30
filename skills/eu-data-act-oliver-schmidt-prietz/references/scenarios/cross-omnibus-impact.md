# cross-omnibus-impact

**Anchor:** Any × cross-chapter × Digital Omnibus impact. The card operationalises the current-law-vs-proposal discipline (`references/gotchas.md` entries 19 and 20) across the build. It walks the Commission's Digital Omnibus proposal (COM(2025) 833 final, 19 November 2025) provision-by-provision against the current Data Act, identifies which scenarios are materially affected, and structures the "watch-list" framing the skill applies to every deliverable touching an affected provision. Reads from `sources/digital-omnibus-amendments-tracker.md`.

**Routes from:**

- "How would the Digital Omnibus change [the analysis we just did]?"
- "Should we draft against the proposal or the current law?"
- "What's the status of the Digital Omnibus and when do we need to act?"
- "Does the proposal change our Art. [4(8) / 5(11) / 15 / 25 / 31] posture?"
- "Will the absorption of DGA, ODD, FFD, P2B into the Data Act affect us?"
- "How does the Omnibus interact with [our current GDPR / ePrivacy / NIS2 work]?"

**Adjacent cards (route there instead if the facts indicate):**

- The question is purely a current-law analysis with no proposal dimension: route to the chapter-specific scenario card.
- The question is about a different Commission instrument (the parallel Digital Omnibus on AI; the Cyber Resilience Act; the AI Act; the European Health Data Space): out of scope of this card. Run sectoral specialist counsel.
- The proposal has been adopted between the skill's source date and the matter date: the card is out of date. Run `sources/digital-omnibus-amendments-tracker.md` to confirm status; trigger the maintenance protocol in that file.

---

## Canonical fact pattern

A Data Act deliverable touches one or more provisions affected by the Commission's Digital Omnibus proposal. The provisions principally affected are: Arts. 4(8) and 5(11) (trade-secret refusal); Arts. 14 to 22 (Ch V public-sector exceptional need); Art. 25 (cloud-switching transitional period and early-termination penalties); Art. 31 (custom-built carve-out and SME / small-mid-cap exemptions); Art. 36 (smart-contract essential requirements). The proposal would also absorb the Data Governance Act, the Open Data Directive, the Free Flow of Non-Personal Data Regulation, and the Platform-to-Business Regulation into the Data Act's chapter structure.

The matter date is between November 2025 (proposal tabling) and the proposal's adoption (estimated mid-to-late 2026 at earliest). The current law (Regulation (EU) 2023/2854 as published on 22 December 2023) is in force unamended. The proposal is in co-legislator negotiation and may be amended substantially before adoption.

---

## Critical disciplines

Three points trip up the proposal-vs-current-law discipline.

- **Never draft against a proposal as if it were law.** Recital 7 of `references/gotchas.md` entry 20 captures the operative rule: the current law as published in the OJ governs today; the proposal informs forward-looking awareness. Client deliverables that treat proposed amendments as operative create immediate legal risk if the proposal is amended or withdrawn. The exception is purely forward-looking strategic documents (multi-year compliance roadmaps; M&A diligence for closings post-adoption window), where the proposal is the relevant horizon.
- **Never omit the proposal where it materially affects the analysis.** The same gotcha entry covers the opposite failure. A deliverable that produces a current-law answer without flagging an adopted-by-mid-2026 amendment that would change the answer is leaving the user to make a decision on incomplete information. The flag is forward-looking, not load-bearing; the current-law answer governs today.
- **Re-check status before any major deliverable.** The proposal's status changes. The skill source date is fixed; the matter date moves. Before producing a deliverable touching an affected provision, re-check `sources/digital-omnibus-amendments-tracker.md` and, where the matter is high-stakes, check EUR-Lex (legislative procedure 2025/0379(COD), Council and Parliament committee pages, and the Commission's "Have your say" portal). If status has changed materially since the skill's source date, the proposal entry in the tracker is updated.

---

## The seven-step walk

The walk runs once for the proposal-vs-current-law overlay. The output of each step feeds the watch-list flag that goes into the underlying deliverable.

### Step 1: Scope check

Confirm which provisions of the current Data Act the underlying matter engages. The proposal-impact analysis runs only on provisions the matter actually engages. A Ch IV unfair-terms review does not pull in the Art. 31 custom-built carve-out proposal; a Ch VI switching review does not pull in the Art. 4(8) trade-secret-refusal proposal.

Cross-check the matter against the proposal's affected-provision list:

- Ch II: Arts. 4(8), 5(11)
- Ch V: Arts. 14 to 22 (principally Art. 15 circumstances)
- Ch VI: Arts. 25, 31
- Ch VIII: Art. 36
- Consolidation: DGA (Regulation (EU) 2022/868), ODD (Directive (EU) 2019/1024), FFD (Regulation (EU) 2018/1807), P2B (Regulation (EU) 2019/1150)

Where the matter does not engage any affected provision, the impact analysis records "no Digital Omnibus impact" and the deliverable proceeds on current law only.

### Step 2: Chapter identification

Identify the chapter(s) engaged by the matter and cross-reference against the proposal's chapter-level changes. Some changes are within-chapter amendments (e.g. new refusal ground added to Art. 4(8)); others are cross-chapter restructurings (e.g. consolidation absorbing DGA into a new Chapter VIIa). The structural changes do not affect current law but may affect strategic timing decisions (e.g. whether to start a DGA-led data-intermediation initiative now or wait for the Omnibus).

### Step 3: Role mapping

The proposal does not amend the Data Act's role definitions (Arts. 2(8), 2(12), 2(13), 2(14), 2(30) and related). Role mapping for the proposal-impact analysis is the role mapping for the underlying matter. The card does not re-derive roles.

The exception: where the proposal absorbs an instrument with a different role taxonomy (DGA's "data intermediation service provider"; ODD's "public sector body"; P2B's "online intermediation service provider"), the role mapping post-adoption will need to be re-run against the consolidated chapter structure. For now, the current taxonomy governs.

### Step 4: Fact-category sorting

The proposal does not amend the Data Act's data-category framework (Arts. 2(15) product data, 2(16) related-service data, 2(17) readily available, Recital 15 raw / pre-processed / derived, Recital 16 content). The data-category sort for the proposal-impact analysis is the sort for the underlying matter.

The exception: the proposal's new Art. 4(8) and 5(11) refusal ground for substantial risk of unlawful trade-secret acquisition, use, or disclosure to third-country entities operating under weaker-protection legal regimes is structurally adjacent to Art. 32 Ch VII. The new ground does not change the data categories but does introduce a new factual consideration (the recipient's third-country exposure profile) that the trade-secret analysis would need to incorporate post-adoption.

### Step 5: Limb-by-limb application

Run the proposal-vs-current-law analysis for each affected provision the matter engages. The structure for each provision:

- **Current law (operative).** What the regulation says today, quoted from `sources/regulation-2023-2854.md`. The provision text governs the matter.
- **Proposed amendment (forward-looking).** What the Commission proposes to change. The proposal text is in COM(2025) 833 final; the tracker file (`sources/digital-omnibus-amendments-tracker.md`) summarises the principal proposed changes by provision.
- **Status as of matter date.** Co-legislator negotiation; not adopted; expected adoption window (the tracker file gives mid-to-late 2026 at earliest as of the skill source date).
- **Material impact on the matter.** Whether the proposal, if adopted in current form, would change the answer; if so, how.
- **Recommendation.** Whether to act now on current law only; or to act now on current law with a documented hedge for the proposal scenario; or to defer action pending adoption.

#### Art. 4(8) / Art. 5(11) trade-secret refusal

**Current law (operative).** Art. 4(8) and Art. 5(11) require, in exceptional circumstances, a case-by-case refusal substantiated on objective elements demonstrating highly likely serious AND irreparable economic damage (Recital 31). The Recital 31 objective elements are illustrative (`references/gotchas.md` entry 8): enforceability of trade-secret protection in third countries; nature and level of confidentiality of the data; uniqueness and novelty of the connected product.

**Proposed amendment.** The proposal would add a refusal ground where there is a substantial risk that the trade-secret data could be unlawfully acquired, used, or disclosed to entities in third countries operating under legal regimes offering weaker protection than the EU. Case-by-case and objective-elements requirements would be retained.

**Material impact.** Data holders facing requests from users or third parties with third-country exposure (foreign-parent enterprises; vendors that route data through third-country processors; recipients in jurisdictions without trade-secret protection comparable to Directive (EU) 2016/943) could rely on the new ground. The current Art. 4(8) and 5(11) analysis already permits the Recital 31 "enforceability in third countries" element; the proposal would elevate that element to an independent refusal ground.

**Recommendation.** Current-law refusal letters under Art. 4(8) and 5(11) use the Recital 31 element where the facts support it. Refusal letters drafted on the proposed new ground alone are not yet lawful; the new ground is not in force. See `ch2-trade-secret-stage-3-refusal.md` for the current Art. 4(8) workflow.

#### Art. 15 Ch V circumstances

**Current law (operative).** Art. 15(1)(a) covers public emergency response where alternative means are infeasible; Art. 15(1)(b) covers non-emergency, non-personal-data-only, specific legal task, alternatives exhausted including market purchase. Art. 15(2) excludes Art. 15(1)(b) requests against microenterprises and small enterprises.

**Proposed amendment.** The proposal would narrow the conditions under which public authorities can demand data from businesses in non-emergency situations. The proposed narrowing affects Art. 15(1)(b) principally; the operational text is in COM(2025) 833 final.

**Material impact.** Public-sector bodies issuing Art. 15(1)(b) requests under the current text may find the scope reduced post-adoption. Data holders facing such requests today respond under current law; data holders building Art. 15 response capabilities should design for both current and proposed scope to avoid rebuild post-adoption.

**Recommendation.** Current-law analysis applies to current Art. 15 requests. Capability-build can hedge for the proposed narrowing.

#### Art. 25 cloud-switching transitional period

**Current law (operative).** Art. 25(2) imposes a maximum 30-day transitional period (extendable to up to 7 months on demonstrated technical unfeasibility per Art. 25(4)); a maximum 2-month notice period (Art. 25(2)(d)); a minimum 30-day retrieval period (Art. 25(2)(g)). Recital 89 confirms that standard service fees and early-termination penalties in fixed-term contracts are not "switching charges" under Art. 29.

**Proposed amendment.** The proposal would clarify in operative form that providers may include early-termination penalties in fixed-term contracts. This codifies what Recital 89 already implies; the proposal does not introduce new restrictions.

**Material impact.** Modest. The current Recital 89 framing already permits early-termination penalties; the proposal moves the framing into operative text, reducing the risk that a customer or competent authority argues that Recital 89 is non-binding.

**Recommendation.** Current Art. 25 contractual posture stands. The proposed clarification supports the existing practice rather than disrupting it.

#### Art. 31 custom-built carve-out

**Current law (operative).** Art. 31(1) applies only to data processing services "of which the majority of main features has been custom-built to accommodate the specific needs of an individual customer or where all components have been developed for the purposes of an individual customer, and where those data processing services are not offered at broad commercial scale via the service catalogue of the provider of data processing services." Two qualifying alternatives in the first limb AND the negative limb (not offered at broad commercial scale). Standard SaaS offerings configured per customer typically fail the negative limb (`references/gotchas.md` entry 13).

**Proposed amendment.** The proposal would expand Art. 31(1) exemptions for custom-made services but limit the expansion to contracts concluded before or on 12 September 2025. Separate proposed exemptions for SMEs and small mid-caps providing non-IaaS services under pre-12-September-2025 contracts.

**Material impact.** Significant for SaaS / PaaS providers with legacy customer contracts. Providers with pre-12-September-2025 custom-build contracts could rely on a broader carve-out post-adoption; providers signing new custom-build contracts after that date remain under the current narrow text. SME / small-mid-cap providers with legacy contracts gain a separate exemption.

**Recommendation.** Current Art. 31 analysis applies. Providers with pre-12-September-2025 contracts that may fall within the proposed broadened carve-out can document the qualifying facts now (contract date, custom-build features, customer-specificity) so that the proposed expansion is operationally available immediately on adoption.

#### Art. 36 smart-contract essential requirements

**Current law (operative).** Art. 36 imposes essential requirements on smart-contract vendors: robustness; safe termination; data archiving; access control; consistency. EU declaration of conformity is required.

**Proposed amendment.** The proposal would remove the Art. 36 essential-requirements compliance regime and instead link compliance to harmonised standards via Commission standard-setting powers.

**Material impact.** Smart-contract vendors currently building toward Art. 36 essential-requirements compliance face a regime shift if the proposal is adopted. The shift is from self-declaration against essential requirements to compliance with harmonised standards; the latter is typically more determinate but is gated on the standards being adopted.

**Recommendation.** Smart-contract vendors maintain current essential-requirements work; harmonised-standards compliance work begins when CEN-CENELEC mandates are issued. Adoption-date readiness is a design decision.

#### Consolidation: DGA, ODD, FFD, P2B absorption

**Current law (operative).** The four instruments apply as standalone regimes. Regulation (EU) 2022/868 (DGA) governs data intermediation services and data altruism. Directive (EU) 2019/1024 (ODD) governs public-sector re-use. Regulation (EU) 2018/1807 (FFD) governs free flow of non-personal data. Regulation (EU) 2019/1150 (P2B) governs platform-to-business relations.

**Proposed amendment.** The proposal would repeal and absorb DGA, ODD, FFD into the Data Act as new Chapters VIIa, VIIb, VIIc (per Commission proposal structure). P2B would be repealed with substance covered by the DMA / DSA per the Commission's assessment.

**Material impact.** Strategic, not operational, in the short term. Organisations operating under DGA, ODD, FFD continue to apply those instruments as published. Compliance documentation references will need to update post-adoption to point to the consolidated Data Act chapters. Organisations planning new initiatives in the affected areas may prefer to design the initiative to be portable across the pre-adoption and post-adoption regulatory architectures.

**Recommendation.** Current standalone compliance applies. Strategic plans factor in the consolidation as a known forward event.

### Step 6: Cross-regime gate check

The proposal also amends GDPR and ePrivacy. The Data Act-side amendments are the principal focus of this card. Where the matter touches GDPR or ePrivacy, the GDPR-side and ePrivacy-side proposed amendments are noted in parallel:

- **GDPR-side proposed amendments.** Legitimate-interest framing for AI training; clarifications on consent withdrawal; modernisations to international transfer regime. These do not affect Data Act mechanics directly but may shift the Case B legal-basis calibration (`cross-gdpr-boundary.md`).
- **ePrivacy-side proposed amendments.** Modernisations to Art. 5(3) (cookie consent) and related provisions. These do not affect Data Act mechanics directly but may shift the connected-product terminal-equipment access analysis (`references/gates/gdpr-overlay.md` ePrivacy section).
- **NIS2 / CRA / AI Act-side amendments.** The Digital Omnibus is broader than just the Data Act. Where the matter touches a sectoral instrument, run `references/gates/sectoral-lex-specialis.md` and check the proposal's effect on that instrument separately. The sectoral effect is out of scope of this card.

The card's gate-check output: a list of which other regimes the matter also touches, and a flag of whether the Omnibus also amends them. Detail goes in the relevant gate or scenario card.

### Step 7: Synthesis with current-law-vs-proposal

The synthesis step here is the entire card. The output is structured so the deliverable presents current law as operative and the proposal as awareness. Format:

> **Current law.** [Statement of what the regulation says today, with citation to `sources/regulation-2023-2854.md`. This is the operative answer to the matter.]
>
> **Proposed amendment under Digital Omnibus.** [Statement of what the proposal would change, with the proposal's status: in co-legislator negotiation as of [date]; not adopted. Expected adoption window: mid-to-late 2026 at earliest. The proposal does not change the current-law answer.]
>
> **Action implication.** [Whether and how the proposal affects the recommendation. Common patterns: "no change to current-law action; the proposal would [outcome]"; "current-law action proceeds; design the [contract / control / process] to accommodate the proposed change to avoid rebuild post-adoption"; "current-law action proceeds; the proposal would [block / permit] this action post-adoption, which is a strategic-timing input for the next cycle".]

Every deliverable touching an affected provision includes this synthesis block. The block is not optional. The block is also not a substitute for the current-law analysis; it sits after the current-law answer, not in place of it.

---

## Decision point

After Steps 5 and 6, the proposal-impact analysis yields one of three outcomes for any specific matter.

1. **No material impact.** The proposal does not affect the matter's analysis even if adopted. The deliverable includes the synthesis block stating "no material impact" and proceeds on current law without further reference.
2. **Material impact; current law governs.** The proposal would change the answer but is not in force. The deliverable proceeds on current law, includes the synthesis block flagging the proposed change and its status, and the recommendation may include a hedge (design for adoption window; document qualifying facts) without acting on the proposal.
3. **Material impact; current law unworkable; the user requests a forward-looking analysis.** The deliverable presents the current-law answer first (which may be a "current Art. X bars this action" finding) and then a proposal-conditional alternative ("if and when the proposal is adopted in current form, the action would be permitted"). The deliverable is explicit that the second analysis is conditional and may need re-running if the proposal is amended.

The card never produces an output that treats the proposal as adopted.

---

## Output skeleton: Digital Omnibus impact section

This card does not produce a standalone deliverable. It produces a section that is incorporated into the underlying deliverable (memorandum, gap analysis, refusal letter, contractual review). The section format:

```
## Digital Omnibus impact (forward-looking)

### Affected provisions touched by this matter
- Art. [X(N)]: [one-line summary of the provision and the matter's
  engagement with it]
- [Repeat per affected provision]

### Proposal-vs-current-law analysis

[Per affected provision, the synthesis block from Step 7 above.]

### Action implications
- [Concrete action implication for the matter: act now on current
  law; act now with hedge; defer pending adoption; strategic-timing
  consideration only.]

### Status as of [matter date]
- Commission proposal: COM(2025) 833 final, presented 19 November
  2025.
- Legislative procedure: 2025/0379(COD).
- Co-legislator status: [Council general approach status; EP
  rapporteur status; trilogue status].
- Expected adoption window: [per the tracker; mid-to-late 2026 at
  earliest as of skill source date].
- Substantive amendment during co-legislator negotiation is likely;
  the proposal as tabled may not be the proposal as adopted.

### Tracker reference
- `sources/digital-omnibus-amendments-tracker.md` for the
  consolidated affected-provision list.
- The tracker is the navigation aid; the operative proposal text
  is in COM(2025) 833 final on EUR-Lex.
```

The section runs in every deliverable touching an affected provision. The section length scales with the number of provisions engaged. For a single-provision matter, the section is short (one synthesis block plus the status snapshot). For a multi-chapter gap analysis, the section is longer (one synthesis block per chapter).

---

## When the proposal is adopted

When the Digital Omnibus is adopted and published in the OJ, the skill maintenance protocol runs (see `sources/digital-omnibus-amendments-tracker.md` "Skill maintenance trigger" section):

1. Replace the tracker with a definitive crosswalk old-text vs new-text.
2. Update `sources/_versions.json` to reflect the amending regulation's CELEX.
3. Fetch the Commission's consolidated version of Regulation (EU) 2023/2854 from EUR-Lex and replace `regulation-2023-2854.md`.
4. Archive the pre-Omnibus snapshot under `sources/_archive/{YYYY-MM-DD-pre-omnibus}/`.
5. Update affected scenario cards (including this one).
6. Update affected templates (notably the Art. 4(8) refusal letter and any Ch V templates).
7. Bump major version.

Until adoption, the card produces a watch-list framing, not a transition plan.

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` for each affected provision the matter engages. The current law is the operative answer.
- `sources/digital-omnibus-amendments-tracker.md` for the consolidated affected-provision list and the legislative-status snapshot.
- COM(2025) 833 final for the operative proposed text (the proposal document on EUR-Lex; the tracker does not reproduce the proposed text verbatim). Where the deliverable cites the proposed text, it cites COM(2025) 833 final, recital or article number.
- Council and European Parliament procedural pages for current legislative status (procedure 2025/0379(COD)). The tracker file's status snapshot dates as of the skill source date; the deliverable's status snapshot should be re-confirmed for high-stakes matters.

Never paraphrase the proposed text from training data; quote from COM(2025) 833 final. Never present the proposal as if it were law.

---

## Cross-references

- `sources/digital-omnibus-amendments-tracker.md` (the central source for affected-provision tracking and maintenance triggers).
- `references/gotchas.md` entry 20 (Digital Omnibus is a proposal; mandatory check on every relevant deliverable). Entry 13 is also relevant (Art. 31 custom-built carve-out, currently narrow; proposed broader). Entry 19 (FAQ framing) is parallel discipline.
- `references/method/analysis-method.md` Step 7 (synthesis with current-law-vs-proposal; this card operationalises Step 7).
- `references/method/house-style.md` "Current-law-vs-proposal tagging" subsection (the format the synthesis block follows).
- `ch2-trade-secret-stage-3-refusal.md` (touches the Art. 4(8) proposal; the prototype card already includes the synthesis block for Art. 4(8)).
- `ch7-third-country-request.md` (Art. 32 not principally affected by the proposal; the card flags this in its synthesis).
- `cross-gap-analysis.md` (the gap-analysis card uses the synthesis block in its "watch-list" column).
- `cross-gdpr-boundary.md` (the GDPR-Data Act boundary card flags GDPR-side and ePrivacy-side proposal items in parallel).

---

## Drafter notes

Operational observations for using this card.

- **The watch-list is not a remediation backlog.** The proposal-impact section informs forward-looking decisions. It does not produce current-state remediation actions because the current law has not changed. Deliverables that mix proposal-impact items into the current-law action list create confusion and risk of acting on a non-binding proposal. Keep the two separate.
- **Re-check status for high-stakes deliverables.** The skill source date is fixed; the matter date moves. For high-stakes deliverables (M&A diligence; regulatory filings; significant capability investments), re-check `sources/digital-omnibus-amendments-tracker.md` for status updates and check EUR-Lex procedure 2025/0379(COD) for the latest co-legislator position. The tracker file's "Legislative status snapshot" is dated; if the matter date is significantly after that date, status may have advanced.
- **Substantial amendment during negotiation is likely.** The Commission's proposal is not the Council's general approach is not the Parliament's position is not the trilogue outcome. The proposal items the card lists are the Commission's proposal as tabled; the co-legislators may amend each of them. Deliverables hedging on the proposed text should hedge on a range of plausible outcomes, not just on the proposal as tabled.
- **Adoption is one event; entry into force / application is another.** EU regulations typically have a defined entry-into-force date (publication + 20 days, or otherwise specified) and a separate application date (often 12 to 24 months later). The Digital Omnibus, if adopted as a regulation, will follow this pattern. The deliverable's timing analysis should distinguish: adoption date; entry-into-force date; application date for each affected provision (which may differ across provisions, mirroring Art. 50 of the current Data Act).
- **The proposal interacts with the EDIB guidelines work.** Several provisions affected by the proposal are also subject to forthcoming guidelines from the European Data Innovation Board (Art. 9(5) compensation per FAQ Q72; Art. 32(3) third-country conditions). Where both the proposal and EDIB guidelines are pending on the same provision, the deliverable's watch-list flags both.

---

## Note on structural invention

The prototype card (`ch2-trade-secret-stage-3-refusal.md`) is single-scenario and single-chapter. This card is structurally different: it is a discipline card rather than a scenario card. The card preserves the prototype's ten-section structure (anchor; routes from; adjacent cards; canonical fact pattern; critical disciplines; the seven-step walk; decision point; output skeleton; citations to load; cross-references; drafter notes), but two adaptations were necessary. First, the "limb-by-limb application" in Step 5 walks each affected provision (5 provisions plus the consolidation) rather than each limb of a single article. Second, the "output skeleton" is a section that incorporates into other deliverables, not a standalone refusal letter or memorandum. A "When the proposal is adopted" section was added to operationalise the maintenance protocol cross-reference; this is not in the prototype but the maintenance trigger is unique to this card.
