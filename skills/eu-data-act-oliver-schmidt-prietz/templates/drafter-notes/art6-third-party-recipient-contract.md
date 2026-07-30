# Drafter notes: art6-third-party-recipient-contract

The Art. 6 contract is the operational backbone of the user-third-party flow. The most common drafting failure is treating Art. 6(2) as a list of suggestions rather than a closed list of prohibitions, and producing a contract that contradicts or weakens the eight points.

## Substantive risks of using the template

- **The Art. 6(2) list is closed and cumulative.** Eight items, each independent. The contract should reproduce each of them; the template's section 4 does so verbatim. Drafters who paraphrase Art. 6(2) often inadvertently weaken or alter the prohibitions. The verbatim reproduction makes the contractual obligation coextensive with the regulatory obligation, which is the cleanest enforcement posture.
- **Art. 6(2)(d) gatekeeper prohibition has downstream reach.** The Third Party cannot share with a DMA-designated gatekeeper. This includes onward sharing to a subcontractor or affiliate that is a gatekeeper. The drafter should ensure the Third Party's operational reality (cloud providers, analytics partners, AI training infrastructure) does not include sharing the data with a gatekeeper. See `references/gates/dma-gatekeeper.md`.
- **Art. 6(2)(e) competing-product restriction is asymmetric.** The Third Party cannot use the data to develop a connected product that competes with the connected product from which the data originates. Related services are not prohibited (Recital 32). The drafter should ensure section 3 (purposes) describes a service or use that does not stray into competing connected products. Where the Third Party's roadmap could plausibly produce a competing connected product within the term, the contract should include a specific carve-out and a notification mechanism.
- **Art. 6(2)(b) profiling restriction.** Profiling is permitted only where necessary to provide the service requested by the User. Drafters should ensure section 3's purpose statement is precise enough that profiling necessity is determinable. Where the Third Party's business model is profiling-adjacent (advertising, scoring, behavioural analysis), additional safeguards under GDPR Art. 22 may also be needed.
- **Art. 6(2)(c) onward sharing requires a contract with the User AND the trade-secret safeguards.** A common drafting mistake is allowing the Third Party to subcontract or onward-share under its own discretion. Art. 6(2)(c) requires (i) a contract with the User permitting the onward sharing and (ii) the onward recipient takes all necessary measures agreed between the data holder and the Third Party to preserve trade-secret confidentiality. The drafter should consider whether onward sharing is anticipated and structure section 4(c) accordingly.
- **Art. 6(2)(h) consumer protection.** The provision applies where the User is a consumer. The Third Party cannot prevent the consumer-User from making the data available to other parties. This is sometimes inadvertently broken by exclusivity clauses or tie-in arrangements. The drafter should ensure no clause in the contract conflicts with Art. 6(2)(h) where the User is a consumer.
- **The trade-secret safeguards under Art. 5(9) are a separate document.** The data holder negotiates the safeguards with the Third Party directly under Art. 5(9). This contract (User-Third Party) cross-references those safeguards but does not replace them. Section 5 makes this clear. Drafters should not try to consolidate the two documents because the User is not party to the Art. 5(9) safeguards.
- **GDPR roles need clear allocation.** The Third Party can be a processor for the User (where the User is controller), a joint controller with the User (where they jointly determine purposes and means), or an independent controller (where the Third Party uses the data for its own purposes within the agreed purposes). The drafter should not paper over this with vague language. The role allocation drives Art. 28 / 26 / 24 GDPR documentation and operational obligations.
- **Art. 13 unfairness exposure.** Where this contract is unilaterally imposed by the Third Party on the User (e.g. take-it-or-leave-it terms for a consumer service or an SME-User), Art. 13 unfairness analysis applies. Terms that fail the Art. 13(3) general test or fall within Art. 13(4) or 13(5) lists are unenforceable. Drafters should ensure the agreement does not embed terms vulnerable to unfairness challenge, particularly liability limitations and exclusivity arrangements.

## Pointers to gates and scenarios

- Scenario card: `references/scenarios/ch2-third-party-permitted-use.md` (closed list of prohibitions, operational mechanics).
- DMA gate: `references/gates/dma-gatekeeper.md` (always relevant; Art. 6(2)(d) and downstream considerations).
- GDPR gate: `references/gates/gdpr-overlay.md` (always relevant where personal data is in scope; section 7 of the template).
- Trade-secret gate: `references/gates/trade-secrets-directive.md` (relevant where trade-secret data is in scope; the Third Party's compliance with Art. 5(9) safeguards is a precondition for Art. 6(2)(g) compliance).
- Sectoral gate: `references/gates/sectoral-lex-specialis.md` (relevant in regulated sectors where the Third Party's processing is also constrained by sectoral law).

## Common drafting mistakes the drafter should check for

- Paraphrasing Art. 6(2). The list is closed; verbatim reproduction in section 4 is the safest drafting.
- Allowing "for purposes related to the User's service" rather than naming the purposes. Art. 6(1) requires purpose specification, and generic language opens the door to scope creep.
- Drafting an exclusivity clause that breaches Art. 6(2)(h). Consumer-users cannot be prevented from making the data available to other parties.
- Including a "Third Party may use the data for its product development" clause. This routinely breaches Art. 6(2)(e) because product development that ends with a competing connected product is prohibited.
- Treating the Third Party as a processor by default. Many Art. 5(1) flows place the Third Party in an independent-controller role (e.g. where the Third Party provides a service that requires processing for its own purposes). The default-processor assumption is wrong in those cases.
- Forgetting the Recital 39 limit on profiling. Profiling for purposes other than service necessity is prohibited; the drafter should ensure no clause in the contract authorises profiling beyond that limit.
- Drafting indemnity asymmetrically against the User. Art. 13 unfairness analysis bites; section 4 limit on intentional acts and gross negligence is the minimum.
- Failing to address gatekeeper status going forward. The Third Party may not be a gatekeeper today but could be designated during the term. The template includes a continuing notification obligation.
- Failing to coordinate with the trade-secret safeguards. Where the Third Party has agreed safeguards with the data holder under Art. 5(9), this contract (User-Third Party) should cross-reference them. Independent contracts can drift; coordination is the drafter's responsibility.
- Failing to consider sectoral overlay. In regulated sectors (vehicles, medical devices, finance), the Third Party's processing may also be constrained by sectoral law. Run the sectoral gate.

## Length and tone

Contract style: clear, neutral, complete. The contract reproduces regulatory obligations and operationalises them. Drafters should resist the temptation to add favourable terms beyond what the User actually requires or what the Third Party can credibly accept; over-drafting invites unfairness challenge and complicates enforcement.
