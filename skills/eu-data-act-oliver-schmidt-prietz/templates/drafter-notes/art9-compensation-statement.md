# Drafter notes: art9-compensation-statement

The Art. 9 compensation statement is the data holder's primary written articulation of its commercial position in a mandatory B2B data-sharing relationship. The most common drafting failures are mis-identifying the recipient's status (and therefore the Art. 9(4) cap), failing to itemise costs sufficiently, and treating margin as freely chosen rather than reasoned.

## Substantive risks of using the template

- **The Art. 9(4) cap is the load-bearing distinction.** For SMEs (within Recommendation 2003/361/EC) and not-for-profit research organisations that do not have partner or linked enterprises that fail the SME test, compensation is capped at the Art. 9(2)(a) costs. No Art. 9(2)(b) investments and no margin are chargeable. Section 3 of the template forces the status identification; section 4 branches on it. Drafters who misclassify an SME recipient as "other" expose the data holder to challenge under Art. 9(4) and possible enforcement by the competent authority. Where the recipient self-identifies as SME, the data holder should not unilaterally redesignate; verification is appropriate, but the verification must respect the Art. 8(5) limit on demanding more information than necessary.
- **"Non-discriminatory" is the Art. 8(3) limb, not the Art. 9 limb.** The compensation must be non-discriminatory across comparable categories of recipients. The data holder cannot quote one price to recipient A and a different price to a comparable recipient B without an objective justification. Section 9 of the template addresses this explicitly. Where the recipient asks under Art. 8(3) second sentence, the data holder must provide information demonstrating no discrimination, without undue delay. The drafter should anticipate this request and have the supporting comparable-contract evidence ready.
- **"Reasonable" under Art. 9(1) is not a free hand.** Margin should be reasoned, not asserted. Section 8 of the template requires reasoning tied to comparables, sector practice, and recipient category. A margin of, say, 50% of cost might be reasonable in some data markets and clearly excessive in others. Drafters should not invent a margin without a defensible reference point.
- **Itemisation matters.** Art. 9(7) gives the recipient the right to information sufficient to assess compliance with Art. 9(1)-(4). A statement that says "total compensation: X" without breakdown is non-compliant with Art. 9(7) and exposes the data holder to challenge. Sections 5, 6, and 7 of the template force itemisation.
- **Cost recovery vs. cost reallocation.** Art. 9(2)(a) costs are the costs incurred in making the data available. Drafters sometimes inflate these by attributing infrastructure that would have existed anyway (the connected product itself, the data collection infrastructure that the data holder needs for its own product). Art. 9(2)(a) is narrower: it is the incremental costs of making the data available to the recipient, plus the allocable share of relevant shared infrastructure. The drafter should be able to defend each item as causally linked to the data-sharing arrangement.
- **Recital 7-style mixed datasets are the typical scenario.** Where the data is mixed personal/non-personal, the cost of anonymisation or pseudonymisation may be chargeable under Art. 9(2)(a) where it is necessary to make the data available. Where it serves the data holder's broader GDPR compliance posture rather than the specific making-available activity, the allocation is harder. Drafters should articulate the basis for any anonymisation cost.
- **The Commission guidelines (Art. 9(5)).** At the time of the source's freshness date (15 May 2026), the Commission has not yet adopted formal guidelines. Section 11 of the template omits the guidelines language unless adopted guidelines exist at the time of drafting. Drafters should check the Commission's public register before drafting.
- **The compensation statement is not a contract.** It is the data holder's explanation of the basis for the compensation it seeks. The actual compensation is agreed in the data-sharing contract. The drafter should not allow the statement to drift into contractual binding language; it is a Art. 9(7) information deliverable.

## Pointers to gates and scenarios

- Scenario cards: `references/scenarios/ch3-frand-terms.md` (FRAND framework); `references/scenarios/ch3-compensation-challenge.md` (recipient-side challenge perspective).
- Sectoral gate: `references/gates/sectoral-lex-specialis.md` (relevant where sectoral law (e.g. PSD, FIDA, sectoral data spaces) sets specific compensation rules; Art. 9(6) preserves Union law and national law that excludes compensation or provides for lower compensation).
- Member State gate: `references/gates/member-state.md` (Member State law may exclude compensation in specific contexts, e.g. official statistics under Art. 9(6) read together with Art. 15(3) and Art. 20(4)).

## Common drafting mistakes the drafter should check for

- Asserting "the compensation is reasonable" without supporting analysis. Reasonable is a standard the data holder must defend; the statement should show the work.
- Treating an SME recipient as a non-SME because the SME has partner or linked enterprises that are themselves SMEs. The cap applies as long as none of the partner or linked enterprises fail the SME test. The drafter should verify the corporate structure rather than assuming.
- Charging Art. 9(2)(b) investments to an Art. 9(4) recipient. The cap is explicit; investments and margin are not chargeable.
- Asserting margin without reasoning. Section 8 requires the calibration basis.
- Failing to provide the calculation worksheets. Section 10 surfaces this; Art. 9(7) requires sufficient detail for assessment.
- Inflating Art. 9(2)(a) costs by attributing infrastructure that would have existed anyway. Causal attribution is the discipline.
- Treating R&D investment in the connected product as fully chargeable. R&D in the product itself is largely not attributable to making the data available; the attributable share is typically a small fraction.
- Failing to address the Art. 8(3) non-discrimination position. Drafters who have not compared the calculation to comparable recipient arrangements are exposed.
- Discrimination against the recipient through indirect terms. The compensation statement is one of multiple terms; if other terms (delivery timing, format, exclusivity, audit rights) are imposed differently on this recipient vs comparables, the package as a whole may be discriminatory even if the headline compensation is identical.
- Missing the Digital Omnibus check. COM(2025) 833 final affects some Ch III provisions; the drafter should check `sources/digital-omnibus-amendments-tracker.md` to confirm whether Art. 9 has any forward-looking flag relevant to the statement.

## Length and tone

Practitioner-direct, evidence-based. The data holder is justifying its commercial position with reference to the regulatory standard. The tone is neutral; the substance is the calculation. Drafters should resist the temptation to argue for higher compensation through tone; the calculation either supports the figure or it does not.
