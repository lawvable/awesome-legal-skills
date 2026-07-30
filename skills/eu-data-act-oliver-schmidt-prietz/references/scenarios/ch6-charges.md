# ch6-charges

**Anchor:** Provider × Ch VI × switching-charge reduction and abolition. Art. 29 sets a phased withdrawal of switching charges culminating in abolition on 12 January 2027. The deliverable is the provider's charge framework: which charges count as switching charges (and so fall under Art. 29), which fall outside (and so are not abolished), and how to map the transition between now and 12 January 2027. The mirror question on the customer side (whether a particular charge is a lawful switching charge or not) runs on the same analysis.

**Routes from:**

- "What can we still charge for switching after the Data Act?"
- "What charges have to disappear on 12 January 2027?"
- "Are data egress charges switching charges?"
- "Are standard service fees switching charges?"
- "Can we still impose early-termination penalties on a fixed-term contract?"
- "Our customer is contesting our switching invoice; is it lawful?"

**Adjacent cards (route there instead if the facts indicate):**

- Contract-review focus rather than charge analysis: `ch6-customer-contract-review.md` (customer-side) or `ch6-provider-compliance.md` (provider-side).
- Switching execution mechanics during transition: `ch6-switching-execution.md`.
- Whether the service is carved out of Art. 29 under Art. 31: `ch6-custom-built-carve-out.md`. Art. 29 is one of the obligations that falls away under the Art. 31(1) carve-out.

---

## Canonical fact pattern

The provider has, or is planning, a switching-charge regime: pricing for activities related to data egress, support actions, format conversion, professional-services migration assistance, and similar. The provider also has standard service fees for the underlying service, may have early-termination penalties on fixed-term contracts, and may impose data egress charges for in-parallel use under Art. 34. The provider needs to map each price point to Art. 29 (and adjacent provisions) to know whether the price stays, is reduced to cost, or must be eliminated by 12 January 2027.

The customer-side mirror: a customer has received an invoice or pricing schedule from the provider and needs to assess whether each line is lawful under Art. 29, Recital 88, Recital 89, and Art. 34(2).

---

## Critical disciplines

- **Switching charges, standard service fees, and early-termination penalties are three different things.** Recital 88: switching charges are charges imposed on the customer for the switching process, typically passing on the costs the source provider incurs because of the switching process. Common examples per Recital 88: data egress charges for transit of data to the destination provider or to on-premises infrastructure, and costs of specific support actions during the switching process. Recital 89: standard service fees for the provision of the data processing services themselves are not switching charges; they continue and are not subject to withdrawal. Recital 89 also confirms that fixed-duration contracts may include proportionate early-termination penalties; these are not switching charges either. The Digital Omnibus would put the early-termination clarification into operative form; for now the position rests on Recital 89.
- **The Art. 29 timetable has three phases.** Pre-11 January 2024: any switching charges. From 11 January 2024 to 11 January 2027: reduced switching charges only, capped at the costs incurred by the provider that are directly linked to the switching process concerned (Art. 29(2)-(3)). From 12 January 2027: no switching charges at all (Art. 29(1)). The reduction has been in effect since the regulation entered into force; only the date of abolition is forward-looking.
- **"Directly linked" is a hard cap, not a soft cap.** Art. 29(3): "The reduced switching charges referred to in paragraph 2 shall not exceed the costs incurred by the provider of data processing services that are directly linked to the switching process concerned." No margin, no recovery of indirect costs, no recovery of generic engineering or platform investment. The provider that charges its standard hourly engineering rate for switching-support engineering is over the cap unless it can demonstrate the rate is at cost.
- **In-parallel use under Art. 34 is the one place data egress charges survive past 12 January 2027.** Art. 34(2): where a customer is using one service in parallel with another, the provider may impose data egress charges, but only for the purpose of passing on egress costs incurred and without exceeding such costs. Per FAQ Q54 the Commission view is that in-parallel use implies a constant data egress as opposed to the one-off data egress that can be expected for a switching operation, which is why in-parallel use is treated differently. After 12 January 2027 the question is operationally important: is this a switching event (charges abolished) or in-parallel use (egress charges still possible at cost).
- **The pre-contract disclosure obligation under Art. 29(4) is independent.** Before entering into a contract the provider must give the prospective customer clear information on (a) standard service fees, (b) early-termination penalties that might be imposed, and (c) reduced switching charges that might be imposed during the Art. 29(2) timeframe. The disclosure is procedural and is owed regardless of whether the provider plans to charge anything. Failure to disclose is non-compliance even if the actual charges are lawful.

---

## The seven-step walk

### Step 1: Scope check

Verify the Data Act applies. Confirm the service is a "data processing service" within Art. 2(8); per FAQ Q58a the Commission considers IaaS, PaaS, and SaaS all in scope. Confirm Ch VI applies (post-12-September-2025, or in scope of forward-looking obligations even on legacy contracts). Confirm the service is not within an Art. 31 carve-out: Art. 31(1) makes Art. 29 inapplicable to custom-built services that meet the cumulative qualifying limbs and the negative limb (route to `ch6-custom-built-carve-out.md` if arguable).

### Step 2: Chapter identification

Chapter VI. Art. 29 (charges, with three operative timeline anchors), Art. 25(2)(i) (the contractual reference to Art. 29 charges), Art. 26(a) (general information obligation), Art. 34 (in-parallel use egress charges), Recitals 88 and 89 (operative definitions).

### Step 3: Role mapping

| Entity | Data Act role | GDPR role (if personal data in scope) | Other |
|--------|---------------|----------------------------------------|-------|
| Provider | Provider of data processing services |  | Source provider in switching scenarios; party imposing the charges |
| Customer | Customer (Art. 2(30)) | Controller, typically | Counterparty to the charges |
| Outsourced switching support (e.g. a third party engaged by the provider) |  |  | Per Recital 89 outsourcing costs cannot be passed to the customer unless they cover work performed at the customer's request beyond statutory obligations |

Recital 89 makes the outsourcing point explicit: a source provider can outsource switching tasks, but the customer should not bear the cost of that outsourcing.

### Step 4: Fact-category sorting

Card-specific dimensions to sort each price point against.

- **Charge type.** Data egress; format conversion; export tooling; professional-services migration assistance; engineering support; account-management support; project-management surcharges; bandwidth surcharges; certificate / key reissuance; security review costs; legal review costs; documentation production; testing / verification of the export.
- **Phase to which the charge attaches.** Notice period vs transitional period vs retrieval period vs in-parallel use. Notice and transitional fall under Art. 29; in-parallel use under Art. 34(2). Retrieval-period support sits in the transitional / post-transitional band.
- **Cost basis.** At cost (only directly-linked costs); at cost-plus-margin; at standard service rate; bundled into a standard service fee. Only at-cost is permitted from 11 January 2024 to 11 January 2027; from 12 January 2027 zero, except Art. 34(2) in-parallel use.
- **Triggered by customer request beyond statutory obligations?** Per Recital 89 a customer can ask for additional services that go beyond the provider's switching obligations under the Data Act, and the provider may charge for those services where the customer agrees to the price in advance. This is a narrow carve-out: only when the customer asks, only when the customer pre-agrees, only for work beyond the statutory minimum.
- **Contract type for early-termination penalties.** Fixed-term contracts only, per Recital 89, and the penalty must be proportionate. Indefinite-duration contracts cannot bear an "early-termination penalty" as such because there is no fixed term to be terminated early.

### Step 5: Limb-by-limb application of Art. 29 and adjacent provisions

The analysis walks each price point against the operative limbs.

**Art. 29(1). The 12 January 2027 abolition.** "From 12 January 2027, providers of data processing services shall not impose any switching charges on the customer for the switching process." Absolute. No carve-outs except Art. 34(2) for in-parallel use (which is structurally not a switching event). Art. 31 carve-out for custom-built services is the other route out of Art. 29 entirely.

**Art. 29(2). The interim period.** "From 11 January 2024 to 12 January 2027, providers of data processing services may impose reduced switching charges on the customer for the switching process." Permission, not obligation: the provider may reduce to zero unilaterally if it chooses. Most providers will run charges through the interim window. The reduction is mandatory; the imposition is optional.

**Art. 29(3). The at-cost cap.** "The reduced switching charges referred to in paragraph 2 shall not exceed the costs incurred by the provider of data processing services that are directly linked to the switching process concerned." Three limbs to test on each line item: (a) the cost was actually incurred by the provider (not a hypothetical), (b) it is directly linked to the switching process (not generic engineering, not platform investment, not pre-existing infrastructure depreciation), and (c) it does not exceed the actual cost (no markup, no margin).

**Art. 29(4). Pre-contract disclosure.** "Before entering into a contract with a customer, providers of data processing services shall provide the prospective customer with clear information on the standard service fees and early termination penalties that might be imposed, as well as on the reduced switching charges that might be imposed during the timeframe referred to in paragraph 2." Three components: standard service fees, early-termination penalties, reduced switching charges during interim. The disclosure is a clear-information standard, not a hidden-in-the-fine-print standard.

**Art. 29(5). Provider information on complex switching.** "Where relevant, providers of data processing services shall provide information to a customer on data processing services that involve highly complex or costly switching or for which it is impossible to switch without significant interference in the data, digital assets or service architecture." This is a separate transparency duty, not a justification for higher charges. Complexity is disclosed; charges remain at the Art. 29(3) cap.

**Art. 29(6). Publicity.** Information referred to in paragraphs (4) and (5) shall be made publicly available, where applicable, via a dedicated section of the provider's website or in any other easily accessible way.

**Art. 34(2). In-parallel use egress charges.** "Where a data processing service is being used in parallel with another data processing service, the providers of data processing services may impose data egress charges, but only for the purpose of passing on egress costs incurred, without exceeding such costs." Two cumulative limbs: (a) the use must be in parallel, not a switching event; (b) the egress charge must be at cost, no margin. The Art. 34(2) charge survives the 12 January 2027 abolition because in-parallel use is structurally different from switching (FAQ Q54).

**Recital 88. Definition of switching charges.** "Switching charges are charges imposed by providers of data processing services on the customers for the switching process. Typically, those charges are intended to pass on costs which the source provider of data processing services may incur because of the switching process to the customer who wishes to switch. Common examples of switching charges are costs related to the transit of data from one provider of data processing services to another or to an on-premises ICT infrastructure (data egress charges) or the costs incurred for specific support actions during the switching process." This is operative for classification: data egress and switching support are inside Art. 29's scope.

**Recital 89. Carve-outs from "switching charges".** Standard service fees for the data processing service itself: not switching charges, not subject to withdrawal, continue until the contract ends. Early-termination penalties on fixed-duration contracts: permitted, must be proportionate to cover early termination of the contract, in accordance with Union or national law, not switching charges. Outsourced support: costs of outsourcing by the provider cannot be passed to the customer, except where the work covers customer-requested additional services that go beyond the statutory obligations and the customer has agreed in advance. The Digital Omnibus would codify the early-termination point; the Recital 89 position is the current law.

### Step 6: Cross-regime gate check

- **GDPR overlay (loaded if personal data flows).** Load `references/gates/gdpr-overlay.md` only where the charge is for export of personal data and the question of "ordinary processing fees" versus "switching fees" intersects with GDPR Art. 12(5)'s ban on disproportionate fees for data-subject rights. The Ch VI customer is not a data subject and Art. 12(5) does not apply directly, but the GDPR fee analysis is a useful cross-check for the customer's own downstream costs.
- **Trade Secrets Directive overlay (rarely loaded).** The trade-secret carve-out under Art. 25(2)(f) and Art. 30(6) limits the scope of exportable data, which limits what the provider could lawfully be charging to export. The overlap with charges is narrow; load only where the provider's exemption is in dispute.
- **Sectoral lex specialis (warn-only).** DORA (Regulation (EU) 2022/2554) ICT third-party arrangements may have parallel charge-related disclosure requirements; NIS2 (Directive (EU) 2022/2555) supply-chain risk obligations may require disclosure of switching cost exposure. Load `references/gates/sectoral-lex-specialis.md`.
- **Member State implementing law (warn-only).** Where the customer is contesting an invoice via Art. 38 complaint or Art. 10 dispute settlement, the competent authority and certified dispute body identifications are Member State specific. Load `references/gates/member-state.md`.

### Step 7: Synthesis with current-law-vs-proposal

- **Current law.** Art. 29(1)-(7) of Regulation (EU) 2023/2854 (Data Act) is operative: reduction at cost from 11 January 2024 and abolition from 12 January 2027. Art. 34(2) preserves egress charges at cost for in-parallel use. Recitals 88 and 89 set the operative definitions: switching charges include data egress and specific switching support; standard service fees are not switching charges; early-termination penalties on fixed-term contracts are permitted and proportionate; outsourcing costs are not passed to the customer except for customer-requested additional services beyond the statutory minimum.
- **Proposed amendment under the Digital Omnibus.** COM(2025) 833 final (19 November 2025) proposes operative clarification that providers may include early-termination penalties in fixed-term contracts. This codifies the existing Recital 89 position; the practical effect today is small (the position is already taken in the recital). The Omnibus also proposes expansion of the Art. 31 custom-built carve-out (which would remove some services from Art. 29 entirely) and SME / small-mid-cap exemption from non-IaaS obligations for pre-12-September-2025 contracts. Status: co-legislator negotiation, not adopted. See `sources/digital-omnibus-amendments-tracker.md`.

The output cites current law as operative. For early-termination penalties the Recital 89 position governs today; the Omnibus codification is forward-looking. Per gotchas 13 and 20 the Art. 31 expansion is not law.

---

## Decision point

After Steps 5 and 6 the charge analysis yields one of four paths.

1. **All charges lawful.** Each line item is either a standard service fee (outside Art. 29), a proportionate early-termination penalty on a fixed-term contract (Recital 89), an at-cost reduced switching charge through 11 January 2027 (Art. 29(2)-(3)), an at-cost in-parallel-use egress charge (Art. 34(2)), or a customer-requested additional service beyond the statutory minimum (Recital 89). Output Path 1 below.
2. **Some charges unlawful.** One or more charges exceed Art. 29(3) cap, are mislabelled (switching charge dressed as standard service fee or vice versa), or fail the Art. 29(4) pre-contract disclosure. Output Path 2 below: line-by-line classification and corrective action.
3. **Charges lawful today, abolition pending.** Charges are within the Art. 29(2)-(3) interim regime but the provider has not planned for the 12 January 2027 abolition. Output Path 3 below: transition plan from at-cost to zero.
4. **Custom-built carve-out may apply.** Route to `ch6-custom-built-carve-out.md` before completing this analysis.

---

## Output skeleton: Path 1 (all charges lawful, brief confirmation)

Memo, Markdown. Length: one to two pages.

```
Subject: Charge analysis under Article 29 and Article 34, [provider]

Conclusion. The charges listed are lawful as of [date]. The
breakdown by category is below. The 12 January 2027 abolition under
Article 29(1) will eliminate the switching charges category; the
other categories continue.

Charge classification.
| Charge | Category | Operative provision | Status |
|--------|----------|---------------------|--------|
| [Standard service fee] | Standard service fee | Recital 89 | Outside Art. 29; continues to contract end |
| [Switching support] | Reduced switching charge | Art. 29(2)-(3) | At cost; abolished 12 Jan 2027 |
| [Data egress, switching] | Reduced switching charge | Art. 29(2)-(3); Recital 88 | At cost; abolished 12 Jan 2027 |
| [Data egress, in-parallel use] | Egress charge for in-parallel use | Art. 34(2) | At cost; continues past 12 Jan 2027 |
| [Early-termination penalty] | Proportionate penalty | Recital 89 | Permitted on fixed-term contract |

Art. 29(4) pre-contract disclosure is present in the contract at
clause [X], covering standard service fees, early-termination
penalties, and reduced switching charges.
```

---

## Output skeleton: Path 2 (unlawful charges, line-by-line)

Memo, Markdown. Length: two to four pages.

```
Subject: Charge analysis under Article 29 and Article 34, [provider
         / contesting customer]

Conclusion. [N] charges are unlawful or sub-compliant under Articles
29 and 34. Corrective action is needed by [date]. The line-by-line
analysis is below.

Charge analysis.
| Charge | Provider classification | Correct classification | Issue | Action |
|--------|-------------------------|------------------------|-------|--------|
| [Charge A] | Standard service fee | Switching charge (Recital 88) | Mislabelled; not eligible to continue past 12 Jan 2027 | Reclassify; reduce to cost now; plan abolition. |
| [Charge B] | Switching support at hourly rate | Reduced switching charge with margin | Exceeds Art. 29(3) cap | Re-calculate at cost; refund overcharges where invoiced. |
| [Charge C] | Egress charge | Switching egress | Treated as continuing past 12 Jan 2027 | Plan abolition; do not invoice post-12-Jan-2027. |
| [Charge D] | Early-termination penalty | Standard penalty | Indefinite-duration contract | Cannot be an "early-termination penalty"; remove or reframe. |

Pre-contract disclosure.
[Whether the Art. 29(4) disclosure is present, and whether it
covers standard service fees, early-termination penalties, and
reduced switching charges with clear information.]

Corrective actions.
1. [Action] by [date].
2. [...]
```

---

## Output skeleton: Path 3 (transition plan to 12 January 2027)

Roadmap. Markdown. Length: two to three pages.

```
Subject: Transition plan to 12 January 2027 charge abolition

Conclusion. The current charges are lawful under Article 29(2)-(3).
Abolition under Article 29(1) requires the actions below. The
charges that survive the abolition (in-parallel use egress, standard
service fees, early-termination penalties on fixed-term contracts)
are listed separately.

Phase-out timeline.
| Phase | Date | Action |
|-------|------|--------|
| Now | T0 | Maintain at-cost cap; tighten cost-allocation methodology |
| Pre-12-Jan-2027 | T0 to T0+18 months | Customer comms; contract updates; price-list updates |
| 12 January 2027 | T+18 months | Zero switching charges |
| Post-12-Jan-2027 | Ongoing | Art. 34(2) egress charges at cost for in-parallel use only |

Charges that survive.
| Charge | Operative provision |
|--------|---------------------|
| Standard service fees | Recital 89 |
| Early-termination penalties on fixed-term contracts | Recital 89 |
| Art. 34(2) in-parallel use egress at cost | Art. 34(2) |
| Customer-requested additional services beyond statutory minimum | Recital 89 |

Operational changes.
1. Cost allocation methodology revised to confirm Art. 29(3)
   "directly linked" cap is met today.
2. Pre-12-Jan-2027 customer notifications under Art. 29(4) refreshed.
3. Distinction between switching events and in-parallel use codified
   in the operational playbook (FAQ Q54).
```

---

## Citations to load

When this card fires, quote from:

- `sources/regulation-2023-2854.md` Art. 25(2)(i) (contractual reference); Art. 29(1)-(7) (operative); Art. 34(2) (in-parallel use); Art. 26(a) (general information obligation); Art. 31 (carve-out, cross-reference); Art. 50 (temporal).
- `sources/regulation-2023-2854.md` Recital 88 (switching charges definition); Recital 89 (standard service fees not switching charges; outsourcing; early-termination penalties on fixed-term; customer-requested additional services beyond statutory minimum).
- `sources/faq-v1-4.md` Q54 (Commission interpretation: switching is one-off egress, in-parallel use is constant egress; Art. 34(2) survives abolition); Q58a (Ch VI applies to IaaS, PaaS, SaaS); Q72 (compensation guidelines are forthcoming, not yet published; flag where compensation appears in cross-regime analysis). Frame as Commission interpretation.
- `sources/digital-omnibus-amendments-tracker.md` for the early-termination penalty operative clarification, the Art. 31 expansion, and the SME / small-mid-cap exemption (all proposals).

Never paraphrase the regulation from training data. Quote from the source files.

---

## Cross-references

- `references/gates/gdpr-overlay.md` (rarely loaded; only where the GDPR Art. 12(5) fee analysis is a useful cross-check).
- `references/gates/trade-secrets-directive.md` (rarely loaded; only where the Art. 25(2)(f) / Art. 30(6) trade-secret carve-out is in dispute and overlaps with what is being charged for).
- `references/gates/sectoral-lex-specialis.md` (warn-only; DORA, NIS2 parallel disclosure or risk obligations).
- `references/gates/member-state.md` (warn-only; competent authority for Art. 38 complaint and Art. 10 dispute settlement).
- `references/gotchas.md` entries 13 (Art. 31 carve-out narrow), 16 (Commission compensation guidelines forthcoming, not adopted), 20 (Digital Omnibus is a proposal).
- `references/method/analysis-method.md` (the seven-step flow).
- `references/method/house-style.md` (output discipline).
- `sources/digital-omnibus-amendments-tracker.md` (Ch VI entries).
- `ch6-customer-contract-review.md` (customer-side context).
- `ch6-provider-compliance.md` (provider-side context).
- `ch6-switching-execution.md` (live-switch context).
- `ch6-custom-built-carve-out.md` (Art. 31 test, which removes a service from Art. 29 scope).

---

## Drafter notes

- **The cost methodology is the substance.** Art. 29(3)'s "directly linked" cap will not hold up under audit if the provider has not documented its cost allocation. Standard hourly engineering rates do not pass; documented per-switch incremental costs do. Recommend the provider develop a cost methodology now, with audit-trail documentation, even where current charges look unobjectionable.
- **The in-parallel-use distinction is operational, not just legal.** FAQ Q54 frames it as one-off egress (switching, abolished) versus constant egress (in-parallel use, Art. 34(2) survives). Providers should be able to tell the difference per customer and per workload; customers should be able to challenge a mis-classification at invoice time. The distinction will get sharper after 12 January 2027 as the abolition forces the line to be drawn.
- **Customer-requested additional services beyond the statutory minimum.** Recital 89 carves these out. The carve-out is narrower than providers often assume: the customer must request, the customer must pre-agree the price, and the service must go beyond the statutory Ch VI obligations. A provider that bundles "standard switching support" into a paid-tier and treats it as a customer-requested service is misusing the carve-out.
