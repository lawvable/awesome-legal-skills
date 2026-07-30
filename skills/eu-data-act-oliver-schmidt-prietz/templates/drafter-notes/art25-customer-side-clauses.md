# Drafter notes: art25-customer-side-clauses

The Art. 25 review is a procedurally rich, substantively detailed exercise. The most common drafting failures on the customer side are accepting under-specified exportable-data clauses, failing to challenge broad internal-functioning trade-secret carve-outs, and missing the 12 January 2027 switching-charges abolition deadline.

## Substantive risks of using the template

- **Art. 25 is a list of minimum mandatory terms.** Art. 25(2) says the contract "shall include at least" the listed items. The provider can offer more customer-favourable terms; it cannot offer less. Drafters should treat each Art. 25(2) point as a presence/absence check first, then a substantive-compliance check.
- **The 12 January 2027 switching-charges abolition.** Art. 29(1) abolishes switching charges from 12 January 2027 (with limited exceptions, primarily Art. 34 in-parallel use egress at cost). Contracts signed before this date often carry switching-charge clauses that will become unenforceable on that date. The customer should not pay these charges after the abolition date. Section 11 of the template addresses this. Drafters should also check the Digital Omnibus tracker; COM(2025) 833 final may affect aspects of the Ch VI charges regime.
- **The 30-day transitional period in Art. 25(2)(a).** The mandatory maximum transitional period is 30 calendar days, with technical-unfeasibility exception allowing up to seven months under Art. 25(4). Contracts that provide longer transitional periods by default (without the Art. 25(4) technical-unfeasibility predicate) are non-compliant. Customers should not accept "60 days" or "90 days" as the default; the default is 30 days.
- **Art. 25(2)(d) two-month maximum notice period.** A clause that requires longer notice is unenforceable to the extent of the excess. Customers should treat the contract's notice period as capped at two months by direct effect of Art. 25(2)(d).
- **Art. 25(2)(e) exhaustive specification of exportable data.** Vague exportable-data clauses ("data the customer has uploaded") leave the customer exposed at switching time, when the provider may interpret the clause narrowly. The customer should require an exhaustive specification that includes customer data (uploaded), customer-generated data (created within the service), customer-configured digital assets (workflows, configurations, integrations, custom code), and metadata necessary to interpret and use the data.
- **Art. 25(2)(f) internal-functioning carve-out is narrow.** The provider may exempt categories of data specific to its internal functioning from the exportable data set, but only where a risk of breach of trade secrets genuinely exists and only where the exemption does not impede or delay switching. Providers often draft broad carve-outs that capture customer-relevant data. The customer should challenge any carve-out that prevents reasonable use of the data in the destination service.
- **Art. 25(2)(g) 30-day retrieval period is a minimum.** The customer can negotiate longer. Particularly for complex switches, a 30-day retrieval window may be inadequate; the customer should consider negotiating a longer retrieval period commensurate with the switching complexity.
- **Functional equivalence under Art. 30(1) applies to IaaS only.** For PaaS and SaaS, the provider's obligation is to provide open interfaces and standardised export formats (Art. 30(2)-(5)). The customer should not expect functional equivalence outside IaaS; the customer's transition planning must account for this.
- **Art. 13 unfairness overlay.** Where Art. 25 terms are unilaterally imposed (which is typical in B2B cloud contracts where the customer signs standard terms), Art. 13 unfairness analysis is available. The combination of Art. 25 minimum-terms enforcement and Art. 13 unfairness analysis is the customer's strongest posture.
- **The Art. 26 pre-contractual transparency obligation.** Providers must provide specified pre-contractual information about switching. A provider that failed to do so at contract conclusion may face a separate non-compliance claim, and the customer should preserve evidence.

## Pointers to gates and scenarios

- Scenario card: `references/scenarios/ch6-customer-contract-review.md` (Art. 25 mandatory terms walkthrough from the customer side).
- Custom-built carve-out: `art31-custom-built-assessment.md` template (where the provider invokes Art. 31).
- Sectoral gate: `references/gates/sectoral-lex-specialis.md` (relevant where the cloud service is sector-specific and sectoral law layers on top; DORA for financial services; sectoral cloud frameworks for healthcare; EUCS for public-sector clouds).
- Member State gate: `references/gates/member-state.md` (relevant for the competent authority under Art. 37(4)(b)).

## Common drafting mistakes the drafter should check for

- Accepting "switching is supported" generic clauses that do not enumerate the Art. 25(2) items. Each item must be presence-checked.
- Accepting the provider's switching charges as compliant with Art. 29 without scrutinising the cost basis. The provider bears the burden of justifying cost basis under Art. 29; the customer should demand it.
- Treating the 12 January 2027 abolition date as effective immediately. Switching charges are permitted before the abolition date (with the Art. 29 cost-basis discipline); they are abolished after. Drafters who confuse the regime get the timing wrong.
- Failing to challenge broad internal-functioning carve-outs under Art. 25(2)(f). Providers often over-claim trade-secret protection over customer-relevant configuration and metadata.
- Not addressing related-service interdependencies. A customer's actual switch often requires moving multiple interconnected services; the contract may treat each service in isolation. Coordinated switching is a customer requirement and may need to be raised separately.
- Forgetting the alternative-transitional-period notification under Art. 25(4). The provider must notify within 14 working days of the switching request and duly justify technical unfeasibility. The customer should pre-plan how to respond if this notification comes.
- Failing to integrate Art. 13 unfairness analysis. Where Art. 25 minimum-terms enforcement gets the customer to a baseline, Art. 13 may get the customer further. The two regimes interlock.
- Missing the Digital Omnibus check. `sources/digital-omnibus-amendments-tracker.md` lists Ch VI provisions affected; check current legislative status before final drafting.

## Length and tone

Structured, clause-by-clause, evidence-based. The review is internal customer work product; the tone should be precise rather than persuasive. Where the review is being shared with the provider as part of renegotiation, edit for diplomatic tone but retain the substantive findings.
