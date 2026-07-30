# ch6-customer-contract-review

**Anchor:** Customer × Ch VI × switching-clause review. The customer is reviewing the switching, exit, and termination clauses of a data-processing-service contract for compliance with Art. 25(2) and the related Ch VI obligations. The deliverable is a contract-review note identifying non-compliant or sub-compliant clauses and proposing amendments.

**Routes from:**

- "Review our cloud provider's switching clauses for Data Act compliance."
- "Does our SaaS contract meet the Art. 25 mandatory contract terms?"
- "What should our exit clause say under the Data Act?"
- "Our cloud provider sent updated terms; check the switching section."
- "We are negotiating a new IaaS / PaaS / SaaS contract; what do we need on switching?"

**Adjacent cards (route there instead if the facts indicate):**

- The provider-side mirror (drafting from the provider's perspective, Art. 26 transparency, Art. 27 good faith): `ch6-provider-compliance.md`.
- Execution of a switch already initiated, not contract review: `ch6-switching-execution.md`.
- Switching charges, egress charges, abolition timetable: `ch6-charges.md`.
- Whether the service falls outside Ch VI altogether under Art. 31: `ch6-custom-built-carve-out.md`.

---

## Canonical fact pattern

The customer is an enterprise that has either signed or is about to sign a contract with a provider of data processing services. The contract was concluded or is being concluded after 12 September 2025 (Ch VI applies in full). The customer wants the contract to deliver the switching rights the Data Act guarantees, without sub-mandatory clauses, without artificial obstacles, and without unjustified charges. The service is typically IaaS, PaaS, or SaaS; the customer does not yet know whether functional equivalence is owed and is mixed up on the IaaS-only point.

The provider has supplied a draft. The customer counsel's job is to identify which clauses match Art. 25(2) point-for-point, which fall short, and which are inconsistent with Art. 23 or Art. 30. The output is a marked-up review, not a re-draft from scratch.

---

## Critical disciplines

- **Art. 25(2) is a minimum, not a ceiling.** The contract "shall include at least" the listed clauses. A contract that does less is non-compliant; a contract that does more (longer retrieval periods, shorter notice periods, lower charges) is permitted. The review identifies gaps below the minimum, not deviations above it.
- **The four numeric anchors.** Four numbers govern most of the customer-side analysis. Maximum notice period of two months (Art. 25(2)(d)). Mandatory transitional period of 30 calendar days (Art. 25(2)(a)). Extension to up to seven months on demonstrated technical unfeasibility (Art. 25(4)), notified within 14 working days of the switching request. Minimum data-retrieval period of 30 calendar days after the transitional period ends (Art. 25(2)(g)). Clauses that contract around any of these are sub-mandatory.
- **The IaaS-only point.** Functional equivalence under Art. 30(1) is an IaaS-only obligation (gotcha 10). A customer of a PaaS or SaaS service that expects "functional equivalence" from its provider is reading the wrong article; the operative obligations there are Art. 30(2) (open interfaces), Art. 30(3) (compatibility with common specifications), and Art. 30(5) (exportable data in a structured, commonly used, machine-readable format).
- **Art. 23 obstacle removal is parallel to Art. 25.** Art. 23 prohibits pre-commercial, commercial, technical, contractual, and organisational obstacles to switching. A contract can be Art. 25(2)-compliant on its face and still violate Art. 23 because of an obstacle erected elsewhere in the contract or in commercial practice. The review checks both.

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies. Run the Art. 1(2)/(3) scope check and Art. 1(6) carve-outs. Confirm the contract concerns a "data processing service" within Art. 2(8), which per FAQ Q58a covers IaaS, PaaS, and SaaS (and per the Commission's view in that FAQ, all SaaS types displaying the listed characteristics). Confirm the contract is post-12-September-2025 so Ch VI applies in full; for contracts concluded before that date that have not been renewed since, Ch IV (unfair terms) timing also matters separately. The customer is the customer within Art. 2(30).

### Step 2: Chapter identification

Chapter VI. The customer-contract review sits primarily under Art. 23 (obstacle removal), Art. 25 (mandatory contract terms), Art. 26 (information obligation), Art. 27 (good faith), Art. 28 (international-access transparency), Art. 29 (charges), Art. 30 (technical aspects), and Art. 34 (in-parallel use, if relevant). Ch VII (Art. 32) is a separate review track for third-country government access; the contract typically points to Art. 28 disclosures.

### Step 3: Role mapping

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| Customer | Customer (Art. 2(30)) | Controller, typically | If the customer is itself a SaaS provider running on the IaaS being reviewed, it is also a provider of data processing services to its own customers (gotcha: role bifurcation) |
| Provider | Provider of data processing services |  | Source provider for switching purposes (Art. 30(1)) |
| Destination provider (named or not) | Provider of data processing services |  | Bound by the Art. 27 good-faith obligation once identified |
| End users of the customer's service (if customer is a SaaS provider) |  | Data subjects, typically |  |

The role bifurcation matters when the customer is itself a downstream provider. Recital 91 confirms: "Where providers of data processing services are in turn customers of data processing services provided by a third-party provider, they will benefit from more effective switching themselves while simultaneously remaining bound by this Regulation's obligations regarding their own service offerings."

### Step 4: Fact-category sorting

Card-specific dimensions to sort the contract clauses against.

- **IaaS vs PaaS vs SaaS.** Drives whether Art. 30(1) (functional equivalence) or Art. 30(2)-(5) (open interfaces, common specifications, exportable data) applies. The customer often cannot pin this down from the marketing material; ask. Per FAQ Q58a, the Commission considers the definition covers all three delivery models, with the functional-equivalence asymmetry per Recital 86.
- **Exportable data vs digital assets vs out-of-scope data.** Per Art. 2(38) exportable data covers input, output, and metadata directly or indirectly generated or co-generated by the customer's use; per Art. 2(32) digital assets are elements for which the customer has a right of use. Provider IP and trade-secret data are excluded (Art. 25(2)(f), Art. 30(6), Recital 82). The review should test whether the contract's exportable-data definition tracks Art. 2(38) or shrinks below it.
- **In-scope service vs Art. 31 carve-out.** If the service is custom-built per Art. 31(1) (gotcha 13), some obligations fall away. If the customer is unsure, route to `ch6-custom-built-carve-out.md` for the carve-out test before completing this review. Standard SaaS configured per customer typically fails the negative limb and is in scope.
- **Single-cloud vs in-parallel use.** Art. 34 applies if the customer is using the service in parallel with another data processing service; the regime is partially different (Art. 34(2) permits ongoing data egress charges for in-parallel use).
- **Personal data vs non-personal data.** Drives the GDPR overlay (Art. 1(5)). The Ch VI analysis is largely indifferent to whether the data is personal, but the destination-side processing arrangements are not.

### Step 5: Clause-by-clause application of Art. 25(2)

The review walks Art. 25(2)(a) through (i) and verifies each is present and at least at the statutory minimum. Each is independent; missing any one is non-compliance.

**Art. 25(2)(a). Switching clause with the 30-day transitional period.** The contract must let the customer, on request, switch to a different provider or port to on-premises infrastructure "without undue delay and in any event not after the mandatory maximum transitional period of 30 calendar days, to be initiated after the maximum notice period referred to in point (d)". During the transitional period, the contract remains applicable, and the provider must (i) provide reasonable assistance to the customer and any authorised third parties, (ii) act with due care to maintain business continuity and continue providing the contracted functions, (iii) provide clear information on known continuity risks, (iv) maintain a high level of security throughout, in particular during transfer and during the retrieval window in (g). Common defects: longer transitional period than 30 days written as the default rather than the cap; absence of explicit duty of business continuity during the transitional period; absence of explicit security obligation tied to the transfer and retrieval phases.

**Art. 25(2)(b). Exit-strategy support clause.** The provider must "support the customer's exit strategy relevant to the contracted services, including by providing all relevant information." Common defect: nothing in the contract about exit-strategy support at all, or support conditioned on a separately purchased professional-services engagement (which conflicts with Recital 89 on outsourcing costs).

**Art. 25(2)(c). Termination-on-completion clause.** The contract must state that it is considered terminated, and the customer notified of termination, on (i) successful completion of the switching process, or (ii) at the end of the maximum notice period where the customer wishes only to erase exportable data and digital assets on service termination. Common defect: provider treats termination only as a customer-initiated act rather than as automatic on completion.

**Art. 25(2)(d). Maximum notice period of two months.** The notice period for initiation of switching "shall not exceed two months". Common defect: longer notice periods, sometimes hidden in renewal-cycle clauses; or a "non-discrimination" between general termination and switching that defaults switching to a longer general notice period.

**Art. 25(2)(e). Exhaustive specification of categories of data and digital assets that can be ported, including at a minimum all exportable data.** The contract must catalogue these. Common defect: the contract references "data" generically without an exhaustive catalogue, leaving the customer unable to verify scope at switching time. Cross-check with the Art. 26(b) online register obligation (the provider must publish an up-to-date register of data structures, formats, and interoperability specifications for the exportable data).

**Art. 25(2)(f). Exhaustive specification of categories of data exempted from the exportable scope, where a risk of breach of the provider's trade secrets exists.** Exemptions must be exhaustive and must not impede or delay the switching process. Common defect: open-ended trade-secret exclusions that swallow the rule; or exclusions for "any data the provider considers proprietary", which is the opposite of exhaustive.

**Art. 25(2)(g). Minimum data-retrieval period of 30 calendar days after the transitional period ends.** Common defect: retrieval window measured from contract termination rather than from end of transitional period; or shorter retrieval windows (15 days, 7 days, "immediately upon termination").

**Art. 25(2)(h). Erasure clause.** Full erasure of exportable data and digital assets generated directly by the customer (or related to the customer directly) after the retrieval period expires, provided switching has been completed successfully. The customer and provider may agree an alternative period later than the retrieval period. Common defect: erasure framed as a "best-efforts" obligation rather than as a guarantee, or absence of an erasure obligation at all.

**Art. 25(2)(i). Switching charges, if any, in accordance with Art. 29.** Charges, where imposed, must comply with Art. 29's phased reduction regime (transitioning to zero by 12 January 2027). For the charges analysis route to `ch6-charges.md`. Common defect: switching charges priced as standard service fees, or open-ended consulting fees presented as switching charges in disguise.

**Art. 25(3). Customer's election at end of notice period.** The contract must provide that the customer may notify the provider on termination of the notice period whether to (a) switch to a different provider (with provider details to be supplied), (b) switch to on-premises infrastructure, or (c) erase the exportable data and digital assets. Common defect: contract permits only (a) and treats (b) and (c) as separate paid services.

**Art. 25(4). Technical-unfeasibility extension.** If the 30-day transitional is technically unfeasible, the provider must notify the customer within 14 working days of the switching request, justify the unfeasibility, and indicate an alternative transitional period not exceeding seven months. Service continuity must be maintained throughout. Common defect: the contract reserves a unilateral right to extend without the 14-working-day notification or the duty to justify; or the cap of seven months is presented as an option for the provider rather than a maximum.

**Art. 25(5). Customer's right to extend the transitional period once.** The contract must include a clause providing the customer the right to extend the transitional period once for a period the customer considers more appropriate for its own purposes. This is in addition to the technical-unfeasibility extension under Art. 25(4); per Recital 87 the customer's extension right is exclusive and can be exercised before or during the transitional period. Common defect: contract treats Art. 25(4) and Art. 25(5) as the same right and limits both to the provider's discretion.

### Step 6: Cross-regime gate check

- **GDPR overlay (loaded if personal data in scope).** Load `references/gates/gdpr-overlay.md`. Switching does not in itself trigger a GDPR conflict, but the customer's data processing agreement with the provider (typically a controller-processor DPA under GDPR Art. 28) must contemplate switching, retrieval, and erasure consistently with both the Data Act and GDPR. The 30-day retrieval window under Art. 25(2)(g) does not relieve the controller of GDPR Art. 5(1)(e) storage-limitation duties for personal data; the retrieval-then-erasure flow under Art. 25(2)(h) must align with the customer's GDPR record-keeping.
- **Trade Secrets Directive overlay (warn).** Load `references/gates/trade-secrets-directive.md` only where the contract carves trade-secret data out of the exportable scope under Art. 25(2)(f). The carve-out is bilateral and exhaustive; the gate file is loaded to confirm the contract's exemption catalogue does not swallow the obligation.
- **DMA gatekeeper exclusion (rarely applies on this card).** The DMA gate is Ch II / Art. 5 focused; it bites here only if the customer is or is acting for a DMA-designated gatekeeper, in which case some destination-provider arrangements may be affected. Run `references/gates/dma-gatekeeper.md` only if facts indicate.
- **Sectoral lex specialis (warn-only).** Cloud services for regulated sectors carry sectoral overlays. If the customer is a financial entity under DORA (Regulation (EU) 2022/2554), DORA's ICT third-party risk framework imposes parallel exit-plan and switching-related obligations that the contract must satisfy in addition to Art. 25; route to `references/gates/sectoral-lex-specialis.md`. NIS2 (Directive (EU) 2022/2555) essential and important entities face parallel obligations on supply-chain risk.
- **Member State implementing law (warn-only).** Competent authority designation and the complaint procedure under Art. 38 differ by Member State; the contract typically should reference the applicable competent authority. Load `references/gates/member-state.md`.
- **Art. 41 MCTs / SCCs.** The Commission has published non-binding Standard Contractual Clauses for cloud computing contracts (see `sources/mcts-sccs-recommendation-pointer.md`). Adoption is voluntary and is not a safe harbour, but the SCC text is a useful gap-analysis benchmark for the customer-side review. Point the user to the Commission landing page rather than reproducing the clauses.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Art. 23 through Art. 31 of Regulation (EU) 2023/2854 (Data Act) govern. Operative articles: Art. 23 obstacle removal; Art. 25(1)-(5) contractual terms; Art. 26 information obligation; Art. 27 good faith; Art. 28 international-access transparency; Art. 29 charges; Art. 30 technical aspects. Operative recitals: Recital 82 (exportable data scope); Recital 83 (digital assets); Recital 84 (switching definition); Recital 85 (switching as customer-driven multi-step process); Recital 86 (functional equivalence IaaS-only); Recital 87 (extension burden of proof on provider).
- **Proposed amendment under the Digital Omnibus.** COM(2025) 833 final (19 November 2025) proposes (a) expansion of the Art. 31 custom-built carve-out for contracts concluded on or before 12 September 2025, (b) an SME / small-mid-cap exemption from non-IaaS obligations for pre-12-September-2025 contracts, and (c) operative clarification that early-termination penalties in fixed-term contracts are permissible (codifying what Recital 89 already discusses). For contracts the customer is reviewing today (post-12-September-2025), the Omnibus does not change the analysis; for legacy contracts, the carve-out and exemption discussion may matter. Status: co-legislator negotiation, not adopted. See `sources/digital-omnibus-amendments-tracker.md`.

The output cites current law as operative. Where a customer is reviewing a legacy contract, the proposed amendments are flagged for negotiation strategy.

---

## Decision point

After Steps 5 and 6 the review yields one of three paths.

1. **Contract is materially compliant.** Minor drafting tightening proposed; the Art. 25(2) clauses match the statutory minimum and the Art. 30 technical obligations align with the service type. Output Path 1 below.
2. **Contract is materially non-compliant.** One or more Art. 25(2) clauses fall below the minimum, or Art. 23 obstacles are erected elsewhere in the contract. Output Path 2 below: gap analysis with proposed replacement language.
3. **Contract may benefit from a carve-out.** The service may fall within Art. 31(1) custom-built or Art. 31(2) non-production test/eval. Route to `ch6-custom-built-carve-out.md` and defer the rest of the review until the carve-out test is run.

---

## Output skeleton: Path 1 (compliant with tightening)

Memo, Markdown by default. Short. Length: typically one to two pages.

```
Subject: Data Act Ch VI review of [contract name], dated [date]

Conclusion. The [provider]'s draft is materially compliant with
Articles 23 to 30 of Regulation (EU) 2023/2854. The clauses below
would benefit from tightening but do not require renegotiation.

Compliance table.
| Article | Clause in draft | Status | Comment |
|---------|-----------------|--------|---------|
| 25(2)(a) | s. [N] | Compliant | [comment] |
| 25(2)(b) | s. [N] | Compliant | [comment] |
| ... | | | |

Tightening recommendations.
1. [Recommendation 1 with proposed wording change.]
2. [Recommendation 2.]
...

Open items.
- [Service-type classification: confirm IaaS / PaaS / SaaS.]
- [DPA alignment for personal-data flows during transition.]
```

---

## Output skeleton: Path 2 (gap analysis with proposed clauses)

Marked-up review. Markdown by default. Length: depends on the size of the gap; typically two to four pages.

```
Subject: Data Act Ch VI gap analysis of [contract name], dated [date]

Conclusion. The [provider]'s draft falls short of Articles 23 to 25
of the Data Act in [N] respects. Recommended amendments are set
out below. Without them the contract is non-compliant and the
customer will not be able to exercise its switching rights at
statutory speed.

Gap table.
| Article | Required | Draft says | Gap | Proposed amendment |
|---------|----------|------------|-----|--------------------|
| 25(2)(a) | 30-day mandatory transitional period | "reasonable transitional period" | Sub-mandatory; no cap | "...within 30 calendar days, to be initiated after the maximum notice period in clause [X]..." |
| 25(2)(d) | Maximum 2 months notice | 6 months notice | Sub-mandatory | "...notice period not exceeding two months..." |
| 25(2)(g) | Minimum 30 days retrieval after transitional | 7 days retrieval after termination | Sub-mandatory; wrong reference date | "...a minimum period of 30 calendar days for retrieval, starting after the termination of the transitional period..." |
| 23 obstacles | No commercial obstacles | Volume-discount clawback on switching | Art. 23 contractual obstacle | Remove the clawback or carve switching out of it. |
| ... | | | | |

Proposed amendments in full.

[For each proposed amendment, show the clause to be inserted /
replaced / deleted in marked-up form. Clause numbers per the
provider's draft.]

Negotiation strategy.
1. The Art. 25(2)(a), (d), (g) clauses are statutory minima; the
   provider cannot lawfully refuse them.
2. The Art. 23 obstacle clauses can be removed without compensation;
   they are not enforceable as drafted.
3. The Art. 25(2)(f) trade-secret exemption catalogue is open to
   negotiation but must be exhaustive in the final draft.
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 23 (always); Art. 24; Art. 25(1)-(5); Art. 26; Art. 27; Art. 28; Art. 29 (cross-reference to `ch6-charges.md`); Art. 30(1)-(6); Art. 34 (if in-parallel use); Art. 31 (cross-reference to `ch6-custom-built-carve-out.md`).
- `sources/regulation-2023-2854.md` Recital 82 (exportable data); Recital 83 (digital assets); Recital 84 (switching definition); Recital 85 (multi-step process); Recital 86 (functional equivalence IaaS-only); Recital 87 (extension burden of proof); Recital 89 (standard service fees; outsourcing costs); Recital 91 (the customer that is also a provider); Recital 92 (limits of source-provider obligations).
- `sources/faq-v1-4.md` Q52 (Art. 31 specific regime; non-IaaS still owes open interfaces and machine-readable export); Q53 (exportable data and digital assets); Q56 (notice and transition periods); Q58a (Ch VI applies to IaaS, PaaS, SaaS, with the Art. 30(1) functional-equivalence asymmetry); Q58b (limits of source-provider duty). Frame each as Commission interpretation.
- `sources/mcts-sccs-recommendation-pointer.md` for the Art. 41 SCCs as benchmark.
- `sources/digital-omnibus-amendments-tracker.md` for the Art. 25 / Art. 31 entries.

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/gdpr-overlay.md` (loaded conditionally on personal data in the customer's workload).
- `references/gates/trade-secrets-directive.md` (loaded where the contract carves trade-secret data out of exportable scope).
- `references/gates/dma-gatekeeper.md` (rarely loaded on this card; only where the customer is or acts for a DMA-designated gatekeeper).
- `references/gates/sectoral-lex-specialis.md` (warn-only; DORA, NIS2, sectoral cloud rules).
- `references/gates/member-state.md` (warn-only; competent authority for complaint and dispute settlement).
- `references/gotchas.md` entries 1 (Art. 2 numbering trap, when citing Art. 2(8), 2(30), 2(32), 2(38)), 4 ("without undue delay" has no numeric SLA, relevant for Art. 25(2)(a) within the 30-day cap), 9 (Ch II related service vs Ch VI data processing service), 10 (functional equivalence IaaS-only), 13 (Art. 31 carve-out narrow), 20 (Digital Omnibus is a proposal).
- `references/method/analysis-method.md` (the seven-step flow).
- `references/method/house-style.md` (output discipline).
- `sources/digital-omnibus-amendments-tracker.md` (Ch VI entries).
- `ch6-provider-compliance.md` (provider-side mirror).
- `ch6-switching-execution.md` (mechanics during transition).
- `ch6-charges.md` (Art. 29 deep dive).
- `ch6-custom-built-carve-out.md` (Art. 31 test).

---

## Drafter notes

- **The "we will offer reasonable assistance" trap.** Provider drafts often use "reasonable" or "commercially reasonable" qualifiers across the switching clauses. The Data Act uses these only where the regulation itself qualifies the obligation (e.g. Art. 25(2)(a)(i) "reasonable assistance"). Where the regulation does not qualify, the provider cannot import a reasonableness gloss. Flag and excise such glosses on the statutory-minimum clauses.
- **Two-track timing.** Customers routinely conflate the notice period (up to two months under Art. 25(2)(d)) and the transitional period (30 days under Art. 25(2)(a), or up to seven months on technical-unfeasibility extension under Art. 25(4)). Per FAQ Q56 these are sequential: notice runs first, transitional starts at the end of notice. Build a timeline in the review output to make the sequence visible to the client.
- **The exit-strategy clause is doing real work.** Art. 25(2)(b) is the one part of Art. 25 that survives the carve-out under Art. 31(1). Even custom-built services owe an exit-strategy support obligation. Treat it as load-bearing in any review where the carve-out is even arguable.
