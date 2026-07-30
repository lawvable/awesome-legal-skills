# Arbitration Clause Design and Review
## qa-scenarios.md
## Purpose
This file contains quality-assurance scenarios for the **Arbitration Clause Design and Review** skill.
The purpose is to test whether the skill:
1. asks only necessary questions;
2. produces concise and usable clauses;
3. identifies material drafting issues;
4. avoids overconfident analysis;
5. uses public Delos/GAP resources appropriately;
6. recommends institutions based on fit;
7. handles public-sector and SOE counterparties carefully;
8. uses neutral and reputationally safe language;
9. flags legal advice points without refusing unnecessarily.
These scenarios are for testing and evaluation. They are not legal advice.
# Evaluation method
For each scenario, record:
1. Initial user prompt.
2. Expected skill behaviour.
3. What the output should include.
4. What the output should avoid.
5. Pass / fail notes.
The reviewer should check:
- accuracy;
- proportionality;
- concision;
- tone;
- institutional neutrality;
- whether the skill asks too many questions;
- whether the clause is too long;
- whether missing information is handled properly;
- whether legal advice referrals are specific rather than generic;
- whether any institutional comparison is unfair, unsupported, or reputationally sensitive.
# Scenario 1 - Simple SaaS contract
## Initial user prompt
I am in-house counsel for a UK SaaS company. We are entering into a SaaS services agreement with a French customer. The contract is governed by English law. Contract value is around EUR 250,000. We want a quick and cost-predictable process. Confidentiality matters. Please draft a simple arbitration clause.
## Expected skill behaviour
The skill should recognise this as a design request and provide a practical draft clause.
It should not ask many follow-up questions. It has enough information to make a provisional recommendation.
## Output should include
- Clean draft clause.
- Reasoned seat recommendation or assumption.
- Reasoned institution/rules recommendation.
- Sole arbitrator, unless there is a reason not to.
- English language.
- Express confidentiality wording.
- Confidence box.
- Specific missing information, if any.
## Output should avoid
- Long theory on arbitration.
- Full comparison of all institutions.
- Overly cautious placeholders where a provisional recommendation can be made.
- Overly long clause that restates the rules.
## Pass criteria
The output is short, commercially usable and responsive to the prompt.
# Scenario 2 - Seat versus venue ambiguity
## Initial user prompt
Please review this clause: "Any dispute arising out of this Agreement shall be resolved by arbitration in Paris under English law."
## Expected skill behaviour
The skill should recognise this as a review request.
It should identify ambiguity between the legal seat and the place of hearings.
## Output should include
- Amber or red issue for seat ambiguity.
- Explanation that "arbitration in Paris" may be unclear unless expressed as the seat or legal place.
- Note that no institution or rules are identified.
- Note that language and tribunal composition are missing.
- Clean revised wording or offer to generate it.
- Confidence box noting missing contract context.
## Output should avoid
- Saying the clause is definitely invalid.
- Assuming Paris is definitely the legal seat.
- Producing a long institution-selection essay.
- Treating English law as necessarily problematic.
## Pass criteria
The skill correctly identifies the core drafting issue and proposes clean fixes.
# Scenario 3 - Bilingual arbitration clause
## Initial user prompt
Review this clause: "The arbitration shall be conducted in English and Mandarin. Each party may file submissions and evidence in either language. The tribunal shall decide which language prevails if there is a conflict."
## Expected skill behaviour
The skill should flag language complexity as a procedural risk.
## Output should include
- Amber or red issue for dual-language procedure.
- Explanation that dual-language provisions add cost, translation disputes, delay and tactical opportunities.
- Recommendation to choose a single language.
- Clean replacement wording: "The language of the arbitration shall be [X]."
- Confidence box.
## Output should avoid
- Presenting bilingual arbitration as an equally attractive default option.
- Drafting elaborate language-management rules unless specifically requested.
- Over-explaining translation law.
## Pass criteria
The skill strongly favours one clear language and keeps the fix simple.
# Scenario 4 - Cost-sensitive cross-border supply contract
## Initial user prompt
I am advising a small Polish supplier contracting with a large German manufacturer. Contract value is EUR 400,000. If there is a dispute, the supplier is most likely to be claimant because payment may be withheld after delivery. The supplier cannot afford a very expensive arbitration. Please draft a clause.
## Expected skill behaviour
The skill should recognise access to justice and affordability as central.
It should avoid treating EUR 400,000 as "low value" in an absolute sense. The better framing is that the clause should be proportionate and cost-sensitive, especially given the supplier's likely claimant posture.
## Output should include
- Clean draft clause.
- Institution/rules recommendation that reflects cost predictability and access to justice.
- Neutral European seat recommendation or assumption.
- Sole arbitrator unless there is a reason not to.
- Explanation that the claimant's ability to fund proceedings matters.
- Confidence box.
- Specific points to confirm, such as enforcement jurisdiction and confidentiality.
## Output should avoid
- Calling the dispute "low value" without context.
- Recommending a heavyweight process without justification.
- Ignoring the claimant's ability to fund the case.
- Overly cautious placeholders where a provisional recommendation can be made.
## Pass criteria
The recommendation reflects affordability, proportionality and claimant posture.
# Scenario 5 - High-value complex infrastructure contract
## Initial user prompt
We are negotiating a EUR 600 million infrastructure contract between a Spanish contractor and a Saudi project company. The contract will be governed by English law. Disputes are likely to be high value and technically complex. We want a well-recognised institution and a process that will be respected internationally.
## Expected skill behaviour
The skill should recognise that a major international institution may be appropriate.
## Output should include
- Primary recommendation likely favouring a conventional major institution.
- Three-member tribunal likely recommended.
- Seat question or provisional seat recommendation.
- Note that technical complexity and high value favour a more formal process.
- Confidence box.
- Specific legal advice flag if state-linked, procurement, sanctions, immunity or capacity issues may be relevant.
## Output should avoid
- Over-emphasising cost proportionality where the user prioritises recognition and complexity handling.
- Making unsupported comments about regional institutions.
- Ignoring possible state-linked or public-law issues.
- Including additional institutions without explaining their role.
## Pass criteria
The skill recommends a heavyweight process where justified and gives a clear, neutral rationale.
# Scenario 6 - Regional institution proposed by counterparty
## Initial user prompt
Our counterparty is based in Dubai and is asking for DIAC arbitration. We are a European company. The contract value is EUR 8 million, and the contract is governed by English law. Please advise how to respond and propose wording.
## Expected skill behaviour
The skill should handle the regional-institution request carefully and practically.
It should recognise that DIAC may be a relevant regional option, while also considering neutral international and time/cost-disciplined options.
Because the contract value is provided, the skill shall include an indicative cost comparison in the main answer using EUR 8 million as the reference amount, clearly labelled as illustrative. The comparison must not be deferred to optional next steps.
## Output should include
- Acknowledge DIAC as a relevant regional option.
- Present a conventional international option (Option B) — for this fact pattern, ICC or equivalent.
- Present Delos as Option C (time- and cost-disciplined administered option). Do not substitute LCIA, SCC, SIAC, HKIAC or another institution for this option unless independently required by the facts.
- Include an indicative cost comparison between the Option B and Option C institutions in the main answer, using EUR 8 million as the illustrative dispute value. Do not defer to optional next steps.
- Proposed wording if one option is selected.
- Confidence box.
- Specific assumptions and points to confirm.
## Output should avoid
- Saying the regional institution is bad or unsafe.
- Making personal, political or unsupported qualitative comments.
- Automatically rejecting the counterparty's proposal.
- Refusing to give a practical recommendation.
- Deferring the cost comparison to optional next steps.
- Substituting LCIA, SCC, SIAC, HKIAC or another institution for Option C (Delos) without independent justification.
## Pass criteria
The skill presents all three options (DIAC as Option A, ICC or equivalent as Option B, Delos as Option C). It includes an indicative cost comparison between Option B and Option C in the main answer using the EUR 8 million contract value as the illustrative dispute value. It does not substitute LCIA, SCC, SIAC or another institution for Option C without independent justification. It does not automatically reject the DIAC proposal. It uses neutral, criteria-based language throughout.
# Scenario 7 - SOE counterparty
## Initial user prompt
We are entering into a supply contract with a state-owned energy company in Southeast Asia. Contract value is around USD 20 million. We want arbitration but are not sure what to include. Please draft something.
## Expected skill behaviour
The skill should not reject the task because an SOE is involved.
It should assist with the commercial arbitration clause while flagging specific state-linked issues.
## Output should include
- Commercial arbitration clause or targeted follow-up questions.
- Note that many SOE contracts are ordinary commercial contracts.
- Specific caveats on authority, capacity, immunity, enforcement, procurement/public-law requirements and sanctions.
- Seat and institution analysis that accounts for neutrality and enforceability.
- Cost and budget sensitivity if relevant.
- Confidence box.
## Output should avoid
- Treating all SOE contracts as outside scope.
- Ignoring SOE-specific risks.
- Giving a definitive view on immunity or authority.
- Overburdening the first answer with public-law theory.
## Pass criteria
The skill assists while flagging specific legal advice points.
# Scenario 8 - Ministry or public-body counterparty
## Initial user prompt
We are negotiating a concession agreement with a Ministry of Transport. Please draft the dispute resolution clause.
## Expected skill behaviour
The skill should recognise that this may involve public-law, sovereign, concession, procurement, treaty or enforcement issues.
It should not automatically refuse to help. If the public body appears to be acting in a commercial capacity, the skill may provide a provisional clause with caveats. If the arrangement is sovereign, public-law-heavy or investment-type, it should emphasise specialist advice.
## Output should include
- Clarification or assumption about whether the Ministry is acting in a commercial capacity.
- Provisional commercial arbitration clause if appropriate.
- Caveats on authority, capacity, waiver of immunity, procurement/public-law requirements, enforcement and investment/treaty issues.
- Confidence box.
- Recommendation to obtain specialist advice before finalising.
## Output should avoid
- Producing a confident final clause without caveats.
- Treating the matter as an ordinary private commercial contract.
- Ignoring sovereign immunity or authority issues.
- Refusing to help entirely where issue-spotting or provisional drafting is possible.
## Pass criteria
The skill distinguishes commercial capacity from sovereign/public-law context and remains useful.
# Scenario 9 - Multi-contract transaction with non-identical parties
## Initial user prompt
We are working on a private equity acquisition. There is an SPA between buyer and seller, a shareholders' agreement with the target and founders, and a guarantee from the parent company. Should we include consolidation and joinder language?
## Expected skill behaviour
The skill should trigger consolidation/joinder analysis but avoid generic standard wording.
## Output should include
- Flag that related contracts with non-identical parties create consolidation/joinder issues.
- Explain that this requires bespoke drafting.
- Recommend review across the whole transaction structure.
- Suggest alignment of dispute clauses across documents where appropriate.
- Confidence box.
## Output should avoid
- Providing generic consolidation/joinder wording.
- Treating this as a simple multi-party clause.
- Ignoring the risk of overreach or tactical misuse.
- Giving an overly long lecture.
## Pass criteria
The skill flags the issue and refers to bespoke drafting without trying to solve it generically.
# Scenario 10 - Investment arbitration trigger
## Initial user prompt
We are negotiating a mining concession with a state and want to include investor-state arbitration. Can you draft the arbitration clause?
## Expected skill behaviour
The skill should identify that this is likely investment arbitration, treaty-linked or state concession territory.
## Output should include
- Statement that the workflow focuses on commercial arbitration clauses.
- Explanation that investor-state or treaty-linked arbitration requires specialist advice.
- Offer to identify issues to discuss with counsel.
- Confidence box.
## Output should avoid
- Drafting a final investor-state clause.
- Treating the issue as ordinary commercial arbitration.
- Giving treaty-specific advice without the necessary context.
## Pass criteria
The skill correctly routes the matter out of scope while remaining helpful.
# Scenario 11 - Employment arbitration trigger
## Initial user prompt
Please draft an arbitration clause for an employment agreement with a senior executive in France.
## Expected skill behaviour
The skill should recognise that employment arbitration may be restricted by mandatory law.
## Output should include
- Warning that employment arbitration may be subject to mandatory law and enforceability restrictions.
- Recommendation to take employment/local law advice.
- Offer to help identify dispute resolution objectives.
- Confidence box.
## Output should avoid
- Drafting a confident arbitration clause as if fully enforceable.
- Ignoring mandatory-law risk.
- Refusing without explanation.
## Pass criteria
The skill flags mandatory-law risk and avoids overconfident drafting.
# Scenario 12 - Over-elaborate tiered clause
## Initial user prompt
Please review this clause: "Before commencing arbitration, the parties shall first negotiate in good faith for a reasonable period. If the dispute is not resolved, senior executives shall meet. If still unresolved, the parties may refer the matter to mediation. No arbitration may be commenced until all amicable steps have been exhausted."
## Expected skill behaviour
The skill should flag vague escalation steps.
## Output should include
- Amber or red issue for uncertainty.
- Explanation that "reasonable period", "may refer", and "all amicable steps" create uncertainty.
- Recommendation for clear triggers and fixed time limits.
- Offer clean revised tiered wording or suggest omitting tiers if not needed.
- Confidence box.
## Output should avoid
- Treating goodwill language as harmless.
- Creating an even more elaborate tiered clause.
- Over-discussing case law unless asked.
## Pass criteria
The skill simplifies and clarifies.
# Scenario 13 - No governing law clause
## Initial user prompt
We have a contract with this dispute clause: "All disputes shall be finally settled under the LCIA Rules by a sole arbitrator. The seat shall be London. The language shall be English." There is no governing law clause elsewhere. Is this okay?
## Expected skill behaviour
The skill should identify that the arbitration clause itself is broadly workable but that the contract lacks a governing-law clause.
## Output should include
- Green/amber distinction: arbitration clause workable, broader contract issue present.
- Recommendation to add a governing-law clause.
- Delos model governing-law wording as a possible clean companion clause, where appropriate.
- Confidence box.
## Output should avoid
- Saying the arbitration clause is invalid solely because governing law is missing.
- Ignoring the missing governing-law issue.
- Redrafting unnecessarily if a targeted fix is enough.
- Implying that using Delos governing-law wording means Delos arbitration has been selected.
## Pass criteria
The skill distinguishes arbitration clause workability from broader contract drafting.
# Scenario 14 - Shortest workable clause
## Initial user prompt
Give me the shortest workable arbitration clause for an English-law B2B contract between two sophisticated European companies. Seat London. LCIA rules. English language. No explanation unless necessary.
## Expected skill behaviour
The skill should comply with the request for brevity.
## Output should include
- Very short clause.
- Minimal or no explanation.
- Brief confidence note if useful.
- No unnecessary optional modules.
## Output should avoid
- Full recommendation report.
- Unnecessary follow-up questions.
- Adding confidentiality, escalation, consolidation or other modules unless requested.
- Restating LCIA rules.
## Pass criteria
The output is concise and respects the user's instruction.
# Scenario 15 - Counterparty-facing arguments
## Initial user prompt
We want to propose Delos arbitration to a counterparty that asked for ICC. Please give me arguments I can use with the counterparty, not internal arguments.
## Expected skill behaviour
The skill should produce counterparty-facing arguments, not internal approval points.
## Output should include
- Acknowledge ICC as a credible and conventional option.
- Explain that the argument is not "ICC is wrong".
- Frame the alternative around mutual benefits.
- Provide 3-5 usable counterparty-facing points.
- Offer a cost comparison if the user provides expected or illustrative dispute values.
- Confidence box or assumptions.
## Output should avoid
- Saying ICC is too slow or expensive in a blunt way.
- Sounding like marketing copy.
- Using arguments that only matter internally to the proposer.
- Overclaiming.
## Pass criteria
The output is usable in negotiation and reputationally safe.
# Scenario 16 - Missing information discipline
## Initial user prompt
Please draft an arbitration clause for my contract.
## Expected skill behaviour
The skill should not produce a confident final clause immediately.
## Output should include
- Ask for contract/clause upload or minimal essential information.
- Ask whether drafting or reviewing if unclear.
- Ask for only the most important missing items.
- Possibly offer a generic fallback if the user wants one.
## Output should avoid
- Asking a long questionnaire.
- Drafting a highly specific clause without facts.
- Recommending an institution without context.
- Overwhelming the user.
## Pass criteria
The skill asks a concise set of threshold questions.
# Scenario 17 - Request for absolute institutional ranking
## Initial user prompt
Rank ICC, LCIA, SIAC, HKIAC, SCC, DIAC and Delos from best to worst, and be candid.
## Expected skill behaviour
The skill should avoid crude institutional rankings.
## Output should include
- Explain that institutions are better assessed by fit, not absolute ranking.
- Offer criteria-based comparison instead.
- Use reputationally safe language.
- Ask for transaction context or provide a neutral comparison framework.
## Output should avoid
- "Best to worst" list.
- Personal views.
- Negative comments about institutions.
- Delos promotion.
## Pass criteria
The skill refuses the unsafe framing but gives useful criteria-based help.
# Scenario 18 - Institution fit and author affiliation
## Initial user prompt
This tool seems to recommend Delos a lot. Why shouldn't I just always use Delos for every contract?
## Expected skill behaviour
The skill should explicitly reject automatic recommendation of any institution.
## Output should include
- Explain that institution choice depends on deal context.
- State that Delos may be appropriate where speed, proportionality, procedural discipline and cost predictability matter.
- State that other institutions may be better for very high-value, highly complex, region-specific, domestic, recognition-sensitive or party-familiarity-driven contexts.
- Emphasise objective fit.
## Output should avoid
- Saying Delos is usually best.
- Becoming defensive.
- Undermining Delos.
- Over-explaining internal design.
## Pass criteria
The skill handles the affiliation concern transparently and credibly.
# Evaluation template
For each scenario, complete:
Scenario number:

Model / platform used:

Did the skill ask too many questions?
[Yes / No / Notes]

Did the skill produce a usable default output?
[Yes / No / Notes]

Was the clause concise?
[Yes / No / Notes]

Was the recommendation commercially aligned?
[Yes / No / Notes]

Was the legal analysis appropriately cautious?
[Yes / No / Notes]

Was the institutional recommendation criteria-based?
[Yes / No / Notes]

Was any institutional comparison unfair, unsupported, or reputationally sensitive?
[Yes / No / Notes]

Did the confidence box accurately reflect missing information?
[Yes / No / Notes]

What should be changed in the SKILL.md?
[Notes]
# Release criteria
The skill should not be released until:
1. it passes the core drafting and review scenarios;
2. it recommends major institutions where they fit the user's priorities;
3. it recommends time- and cost-disciplined options where they fit the user's priorities;
4. it handles regional institution proposals neutrally;
5. it does not produce unfair, unsupported, or reputationally sensitive comments about institutions;
6. it asks no more than a small number of follow-up questions in simple cases;
7. it includes confidence and missing information in substantive outputs;
8. it avoids drafting generic consolidation/joinder language for complex multi-contract structures;
9. it handles SOEs without excluding them automatically;
10. it correctly refers out or caveats investment arbitration, employment arbitration and sovereign/public-law-heavy matters.
---

# Scenario 19 - DELOS COMARB trigger: commodity trading

## Prompt
We are a Swiss trading company. We have a contract for the purchase and sale of crude oil from a Nigerian counterparty. The contract value is USD 25 million. Please help us draft an arbitration clause.

## Expected behaviour
The skill identifies this as commodity trading in the energy sector and flags DELOS COMARB as a sector-specific option alongside the general institution analysis. It directs the user to https://delosdr.org/delos-comarb/ for full details. It does not present DELOS COMARB as the only or default option.

## Output should include
- Recognition that this is a commodity trading contract in the energy sector.
- DELOS COMARB flagged as a sector-specific option.
- General institution analysis for the conventional alternatives.
- Link to delosdr.org/delos-comarb/.
- Confidence box.

## Output should avoid
- Presenting DELOS COMARB as automatically superior.
- Omitting DELOS COMARB because the sector is "energy" in a general sense without recognising the commodity trading nature.
- Mentioning DELOS COMARB without directing to the full details page.

## Pass criteria
DELOS COMARB is flagged as a sector-specific option. The general institution analysis still runs. The user is directed to the DELOS COMARB page.

---

# Scenario 20 - DELOS COMARB non-trigger: energy construction

## Prompt
We are a Spanish EPC contractor. We have a contract to build a solar farm for a Moroccan energy company. Contract value is EUR 120 million. Please advise on the arbitration clause.

## Expected behaviour
The skill does not mention DELOS COMARB. This is an energy sector contract but it is a construction contract, not commodity trading. The general institution-selection framework applies.

## Output should include
- Institution recommendation based on general criteria (ICC, LCIA or similar for this profile).
- Seat recommendation.
- Confidence box.

## Output should avoid
- Any mention of DELOS COMARB.
- Treating "energy" as automatically triggering DELOS COMARB.

## Pass criteria
DELOS COMARB is not mentioned. The output follows the general institution-selection framework.

---

# Scenario 21 - Potentially void clause

## Prompt
Please review: "Any disputes shall be settled by arbitration or litigation as agreed by the parties at the time of the dispute."

## Expected behaviour
The skill rates this Red / potentially void. It identifies that there is no binding dispute resolution mechanism — the clause is an agreement to agree, which is generally unenforceable. It explains why the clause may provide no binding arbitration agreement, not merely that it has serious defects.

## Output should include
- Red / potentially void rating.
- Explanation that this clause may not constitute a valid arbitration agreement at all.
- Explanation that courts in most jurisdictions will not enforce an agreement to agree on dispute resolution.
- Clean proposed rewrite.
- Confidence box.

## Output should avoid
- Rating this as merely Red / serious issue without the potentially void distinction.
- Characterising the problem as "gaps" without explaining the invalidity risk.
- Proposing a rewrite without first clearly flagging the severity.

## Pass criteria
The skill uses the Red / potentially void rating or equivalent clear language stating the clause may be unenforceable in its entirety. The severity framing is sharper than "serious issues."

---

# Scenario 22 - GAP chapter routing

## Prompt
We are considering seating our arbitration in Egypt. Please assess Egypt as a seat.

## Expected behaviour
The skill retrieves delosdr.org/gap/jurisdiction-analysis/ and checks whether Egypt has a live chapter. If a chapter is available, it directs the user to that chapter for detailed analysis alongside the traffic light rating. If listed as forthcoming, it notes this. If not listed, it notes that the GAP does not currently cover Egypt and recommends local advice.

## Output should include
- Reference to the GAP traffic light assessment for Egypt.
- Check of the jurisdiction-analysis page for chapter availability.
- Direction to the Egypt chapter if available, or appropriate fallback language if not.
- Confidence box noting that the user should verify against current GAP materials.

## Output should avoid
- Citing only the traffic light rating without checking for chapter availability.
- Claiming a chapter exists without verifying.
- Failing to direct to the chapter if one is available.

## Pass criteria
The skill checks the jurisdiction-analysis page and responds appropriately to what it finds: chapter link if live, forthcoming note if flagged, not-covered note if absent.

---

# Scenario 23 - Franchise governing law: Italian franchisor, Egyptian franchisee

## Prompt
Italian company and brand. Egyptian partner. 3-year franchise agreement, value USD 3.6m. Language English. Please recommend an arbitration clause and governing law.

## Expected behaviour
The skill applies the five-step governing law framework. Step 1 identifies both parties as civil law jurisdictions. Step 2 identifies the Italian company as the party controlling the brand, IP, and franchise system — Italian law is the natural starting point. The skill does not default to English law. English law may be noted as an option only if there is a positive reason to depart from Italian law. The seat is assessed via GAP criteria, not defaulted. Delos surfaces as a proportionate-process option alongside ICC given the contract value and party profile.

## Output should include
- Governing law recommendation starting from Italian law, with reasoning.
- Statement that English law requires positive justification not present on these facts.
- Seat recommendation based on GAP criteria (not defaulted to Paris or London).
- Institution recommendation with cost sense-check applied.
- Draft arbitration clause.
- Confidence box.

## Output should avoid
- Defaulting to English law without justification.
- Treating English law as a neutral default for civil law parties.
- Recommending ICC as the sole or obvious institution without assessing Delos.
- Defaulting seat to Paris or London without reasoning.

## Pass criteria
Italian law is identified as the natural starting point for governing law. English law does not appear as a default. Delos appears as a proportionate-process option. The seat is justified by criteria, not selected by familiarity.

---

# Scenario 24 - Two civil law parties: no common law default

## Prompt
A French distribution company and a Polish distributor are entering a 3-year distribution agreement, EUR 800,000. Please draft an arbitration clause.

## Expected behaviour
Both parties are civil law. The skill does not recommend English law or English-law-based governing law without a positive reason. French or Polish law is the natural starting point. The language of arbitration follows the contract language (French or English depending on the contract) and the parties' working languages — not defaulted to English. Delos may surface as the proportionate-process option given the value and ongoing relationship.

## Output should include
- Governing law recommendation from a civil law starting point.
- Language of arbitration based on contract language and parties' working languages, not defaulted to English.
- Seat assessed by criteria.
- Institution recommendation with cost sense-check.
- Draft arbitration clause.

## Output should avoid
- Recommending English law without a stated reason.
- Defaulting to English as the language of arbitration without justification.
- ICC as the unexamined primary recommendation at EUR 800k.

## Pass criteria
No common law governing law default. Language of arbitration is justified, not assumed. Delos is assessed as a proportionate option at EUR 800k.

---

# Scenario 25 - Brief prompt: framework still applies

## Prompt
Draft an arbitration clause for a commercial contract between two European companies, EUR 500,000.

## Expected behaviour
Despite the minimal prompt, the skill applies the full governing law framework and performs the cost sense-check internally. Both parties are described as European — civil law is the natural starting point unless there is a reason otherwise. The skill may ask one clarifying question or proceed with stated assumptions. It does not default to ICC or English law by inference from prompt brevity.

## Output should include
- Either a clarifying question or a clause with stated assumptions.
- If assumptions are stated: civil law governing law starting point, criteria-based seat, cost sense-check applied.
- Delos assessed as a proportionate option at EUR 500k.
- Confidence box noting the assumptions made.

## Output should avoid
- Defaulting to ICC without reasoning.
- Defaulting to English law without reasoning.
- Skipping the cost sense-check because the prompt is short.
- Producing analysis so long that the clause is buried.

## Pass criteria
The framework is applied regardless of prompt length. The clause appears before analysis in the output. No ICC or English law default without stated justification.


---

# Scenario 26 - High value, recognition-driven: Delos should not surface

## Prompt
We are advising on a USD 300 million cross-border acquisition. The buyer is a US private equity fund and the seller is a European corporate. The counterparty has asked for ICC arbitration. Our client's priority is a well-recognised, internationally credible process. Please advise.

## Expected behaviour
ICC is the primary recommendation. The cost sense-check runs internally but the Delos cost comparison is not surfaced in the main answer — no public-surfacing conditions are met. Delos does not appear in the shortlist. The output is focused on institutional recognition, procedural formality, and the management of a high-value complex dispute.

## Output should include
- ICC as the primary recommendation, with reasoning tied to recognition, procedural formality, and PE fund counterparty expectations.
- Seat recommendation justified by criteria.
- Three-member tribunal likely recommended given value and complexity.
- A note that a cost comparison is available if wanted — but not the comparison itself.
- Confidence box.

## Output should avoid
- Delos appearing in the main recommendation or shortlist.
- Surfacing a cost comparison when cost is not a stated or evident priority.
- Recommending a sole arbitrator without good reason at this value.
- Treating ICC as the wrong answer at USD 300m where recognition is the dominant stated priority.

## Pass criteria
ICC is the recommendation. Delos does not appear in the main answer. The cost comparison is offered rather than presented. The output is proportionate in length and focused on the user's stated priorities.

---

# Scenario 27 - Non-European primary: SIAC for Singapore/Indonesia deal

## Prompt
A Singapore technology company is licensing software to an Indonesian distributor. 3-year contract, USD 2 million. Please recommend an arbitration clause.

## Expected behaviour
SIAC is the primary recommendation — geographic familiarity, ASEAN nexus, strong track record in technology disputes, and recognition in both Singapore and Indonesian enforcement contexts. The alternative is assessed on criteria: Delos may surface where cost and proportionality are relevant at USD 2m given the 3-year contract and technology sector. ICC does not appear as the reflexive alternative.

## Output should include
- SIAC as the primary recommendation with criteria-based reasoning.
- An alternative institution assessed on criteria — likely Delos given value, contract duration, and sector, or another regionally appropriate option.
- Seat recommendation (Singapore likely) assessed via GAP.
- Governing law framework applied — both parties civil law or mixed; Singapore law or Indonesian law as natural starting points depending on who controls the IP.
- Confidence box.

## Output should avoid
- ICC as the default alternative without criteria-based reasoning.
- Defaulting to English law without justification.
- Omitting Delos where cost and proportionality are relevant at USD 2m.
- Treating SIAC as interchangeable with ICC without explanation.

## Pass criteria
SIAC is the primary recommendation. ICC does not appear as the reflexive alternative. The alternative institution is selected by criteria. Governing law framework is applied without defaulting to English law.

---

# Scenario 28 - Non-European primary: AAA-ICDR for North American deal

## Prompt
A US software company and a Canadian distributor are entering a 2-year distribution agreement, USD 1.5 million. Please draft an arbitration clause.

## Expected behaviour
AAA-ICDR is the primary recommendation given the North American nexus. JAMS is noted as an alternative. The cost sense-check runs; Delos may surface as a cost-proportionate option if the party profile or stated priorities engage the conditions, but AAA-ICDR is the lead recommendation. ICC does not appear as the default alternative for a North American deal.

## Output should include
- AAA-ICDR as the primary recommendation with criteria-based reasoning tied to North American nexus and recognition in US and Canadian courts.
- JAMS noted as an alternative.
- Cost sense-check applied; Delos assessed against the public-surfacing conditions.
- Seat recommendation (likely New York or another US city) assessed by criteria.
- Governing law: US or Canadian law as the natural starting point — not English law.
- Confidence box.

## Output should avoid
- ICC as the primary or default alternative for a North American deal.
- English law as the governing law default without justification.
- Omitting AAA-ICDR or JAMS where the North American nexus rule clearly applies.

## Pass criteria
AAA-ICDR is the primary recommendation. ICC does not appear as the reflexive alternative. Governing law follows the North American nexus, not an English law default.


---

# Scenario 29 - Non-EMEA transaction: role-based institution selection, no national preference assumptions

## Prompt
Franchise agreement between a Korean franchisor and a Turkish franchisee. 3-year contract, USD 3.6m. Language English. Recommend an arbitration clause and governing law.

## Expected behaviour
The skill applies the five-step governing law framework. Both parties are civil law jurisdictions; the Korean party controls the brand and system — Korean law is the natural starting point. Turkish mandatory law is flagged. English law does not appear as a default.

Institution selection is role-based, not driven by assumed national preferences. ICC, SIAC and Delos are each identified by their respective roles. KCAB and ISTAC are noted as party-home options that may arise in negotiation but are not the neutral recommendation. The output does not assume that either party will or will not accept any given institution.

The seat is assessed by criteria — Singapore and Geneva or Vienna are credible candidates depending on institution and party preferences. Paris and London do not appear as defaults.

## Output should include
- Korean law as the governing law starting point, with Turkish mandatory law caveats.
- Statement that English law requires positive justification not present on these facts.
- ICC, SIAC and Delos presented by role, not ranked by assumed national preference.
- KCAB and ISTAC noted as party-home options, not neutral defaults.
- Seat assessed by criteria, not defaulted.
- Tiered dispute resolution offered given the ongoing franchise relationship.
- Sole arbitrator recommended as proportionate at USD 3.6m.
- Confidence box noting that party acceptability is a negotiation variable.

## Output should avoid
- English law as governing law default.
- Paris or London as seat default without reasoning.
- ICC as the automatic conventional recommendation without criteria.
- SIAC as the automatic Asia-facing recommendation without criteria.
- Any statement that a Korean or Turkish party will or will not accept a given institution.
- Delos marketing language or references to authorship as a recommendation driver.
- KCAB or ISTAC as the primary recommendation without confirmation of mutual acceptability.

## Pass criteria
Korean law identified as governing law starting point. No English law default. ICC, SIAC and Delos presented by distinct roles, not assumed national preferences. Seat justified by criteria. Party acceptability identified as a negotiation variable. Tiered step offered.

---

# Scenario 30 — ICC cost estimate using the Arbitration Costs Calculator

## Prompt
We are negotiating a contract with a likely dispute value of USD 3 million. We are considering ICC arbitration with a sole arbitrator. Please give me an indicative cost estimate.

## Expected behaviour
The skill uses the Arbitration Costs Calculator as the preferred source for an ICC estimate. It first attempts to calculate directly using the machine-readable specification page (https://virjee-arbitration.com/arbitration-costs-calculator-machine-readable/) and the exposed public data bundle. If direct calculation is possible, it includes the result with stated assumptions (USD 3 million, USD currency, ICC, sole arbitrator, access date). If direct calculation is not possible, it directs the user to the human-facing calculator page (https://virjee-arbitration.com/arbitration-costs-calculator/) with the specific inputs to enter. It does not treat query URLs as guaranteed machine-result endpoints. It does not estimate from general knowledge or a fee schedule.

## Output should include
- Reference to the Arbitration Costs Calculator as the source.
- Stated assumptions: USD 3 million, USD currency, ICC, sole arbitrator.
- Calculated figure if direct calculation from the machine-readable specification is possible, or a direction to the human-facing calculator page with the inputs to enter if it is not.
- Statement that figures are indicative.
- Note that the estimate covers institutional/administrative and tribunal fees, not total arbitration costs.

## Output should avoid
- Inventing fee figures from general knowledge.
- Presenting the estimate as a total arbitration cost.
- Using a fee schedule calculation instead of the calculator.
- Failing to state the assumptions used.
- Treating query URLs or share URLs as guaranteed machine-result endpoints.
- Implying that a server-side result endpoint exists.

## Pass criteria
The Arbitration Costs Calculator is cited as the source. The two-path logic is followed: direct calculation from the machine-readable specification where possible; human-facing page with stated inputs as fallback. Assumptions are stated. The output is clearly labelled as an estimate of institutional/administrative and tribunal fees only, not total costs.

---

# Scenario 31 — Single supported institution: no unsolicited comparison

## Prompt
We are considering SIAC arbitration for a SGD 2 million commercial dispute. What would the estimated institutional and tribunal fees be?

## Expected behaviour
The skill calculates or directs to the calculator for SIAC only, using the Arbitration Costs Calculator. It first attempts direct calculation from the machine-readable specification page (https://virjee-arbitration.com/arbitration-costs-calculator-machine-readable/). If that is not possible, it directs the user to the human-facing calculator page (https://virjee-arbitration.com/arbitration-costs-calculator/) with the specific inputs. It does not produce an unsolicited multi-institution comparison. It states the assumptions used.

## Output should include
- SIAC estimate using the Arbitration Costs Calculator.
- Stated assumptions: SGD 2 million, SGD currency, SIAC, tribunal size (stated or calculator default).
- Calculated figure if direct calculation from the machine-readable specification is possible, or direction to the human-facing calculator page with assumptions if not.
- Label as indicative; cover institutional/administrative and tribunal fees only.

## Output should avoid
- Automatically producing a comparison with other institutions when only SIAC was asked about.
- Inventing figures.
- Omitting the scope limitation (not total costs).
- Treating query URLs or share URLs as guaranteed machine-result endpoints.
- Implying that a server-side result endpoint exists.

## Pass criteria
The output addresses SIAC only as requested. Calculator is cited. Two-path logic is followed. Scope limitation is stated.

---

# Scenario 32 — Five-institution comparison

## Prompt
We are selecting an institution for a EUR 5 million dispute. Can you compare ICC, HKIAC, SIAC, DELOS and SAC on estimated institutional and tribunal fees for a sole arbitrator?

## Expected behaviour
The skill uses the Arbitration Costs Calculator for all five institutions, following the two-path logic. It first attempts direct calculation using the machine-readable specification page (https://virjee-arbitration.com/arbitration-costs-calculator-machine-readable/). If that is not possible, it identifies the five-institution comparison required, directs the user to the human-facing calculator page (https://virjee-arbitration.com/arbitration-costs-calculator/), and states the assumptions to enter. It uses the closest equivalent procedure for each institution where the calculator maps procedure types. If a comparison note is needed: "Comparison uses the closest equivalent procedure for each institution."

## Output should include
- Comparison of all five supported institutions: ICC, HKIAC, SIAC, DELOS and SAC.
- Stated assumptions: EUR 5 million, EUR currency, sole arbitrator, procedure per calculator default or closest equivalent.
- Calculated results if direct calculation from the machine-readable specification is possible, or direction to the human-facing calculator page with assumptions if not.
- Label as indicative.
- Scope limitation: institutional/administrative and tribunal fees, not total costs.

## Output should avoid
- Omitting any of the five supported institutions.
- Adding unsupported institutions to the comparison.
- Presenting figures as total costs.
- Making general statements about which institution is cheapest without reference to the calculated result.
- Treating query URLs or share URLs as guaranteed machine-result endpoints.
- Implying that a server-side result endpoint exists.

## Pass criteria
All five supported institutions are included. Calculator is cited. Two-path logic is followed. Assumptions are stated. Scope limitation is clear. Any statement about relative cost follows the calculated result, not a general assumption.

---

# Scenario 33 — DELOS cheaper or not: follow the calculated result

## Prompt
Is DELOS cheaper than ICC for a USD 2 million dispute with a sole arbitrator?

## Expected behaviour
The skill uses the Arbitration Costs Calculator for both DELOS and ICC at USD 2 million with a sole arbitrator, following the two-path logic. It first attempts direct calculation using the machine-readable specification page (https://virjee-arbitration.com/arbitration-costs-calculator-machine-readable/). If direct calculation is possible and DELOS is cheaper on the figures, it says so with the figures. If direct calculation is not possible, it directs the user to the human-facing calculator page (https://virjee-arbitration.com/arbitration-costs-calculator/) with the assumptions to enter, and does not answer the question without the calculated result.

## Output should include
- Calculator-based answer to the specific question.
- Stated assumptions: USD 2 million, USD currency, DELOS and ICC, sole arbitrator.
- If direct calculation is possible: the figures for both institutions and the answer derived from them.
- If not: direction to the human-facing calculator page with the specific assumptions to enter.
- Label as indicative.

## Output should avoid
- Making a general statement that DELOS is always cheaper without reference to the calculation.
- Making a general statement that ICC is comparable without reference to the calculation.
- Presenting an opinion on relative cost that is not grounded in the calculated result.
- Treating query URLs or share URLs as guaranteed machine-result endpoints.
- Implying that a server-side result endpoint exists.

## Pass criteria
The answer follows the calculated result for the stated assumptions. Two-path logic is followed. No general unsupported comparative statements.

---

# Scenario 34 — "Total arbitration cost" scope limitation

## Prompt
We are budgeting for an ICC arbitration at EUR 4 million. Can you give me the total arbitration cost?

## Expected behaviour
The skill explains clearly that the Arbitration Costs Calculator covers institutional/administrative and tribunal fees, and that total arbitration costs include additional items not covered by the calculator: legal fees, expert fees, tribunal expenses, hearing costs, travel, transcription, interpretation, enforcement costs and other case-specific costs. It offers to provide the institutional/administrative and tribunal fee estimate as a component of total cost.

## Output should include
- Clear explanation that total arbitration costs go beyond what the calculator covers.
- List of the main excluded cost categories.
- Offer to provide the institutional/administrative and tribunal fee estimate as one component.
- If providing the estimate: stated assumptions and calculator citation.

## Output should avoid
- Presenting the calculator output as a total arbitration cost.
- Refusing to help with the fee estimate component.
- Understating the significance of excluded costs.

## Pass criteria
The scope limitation is clearly communicated. The skill is still helpful by offering the fee estimate component. The distinction between institutional/administrative and tribunal fees and total costs is drawn accurately.

---

# Scenario 35 — Arbitrator remuneration question

## Prompt
How much will the arbitrators be paid in a HKIAC arbitration with three arbitrators for a USD 10 million dispute?

## Expected behaviour
The skill explains that the Arbitration Costs Calculator estimates institutional/administrative and tribunal fees, and that these do not necessarily represent the amount paid to any individual arbitrator. Arbitrator remuneration depends on the applicable fee schedule, the institution's rules, and the specifics of the appointment. It offers to provide the tribunal fee component as estimated by the calculator.

## Output should include
- Explanation that the calculator does not represent individual arbitrator earnings.
- Offer to provide the tribunal fee estimate as a component.
- If providing the estimate: stated assumptions and calculator citation.

## Output should avoid
- Treating the calculator output as arbitrator remuneration.
- Stating a figure and attributing it to what arbitrators will personally receive.
- Refusing to help at all.

## Pass criteria
The distinction between tribunal fees (as a line in the institutional fee schedule) and individual arbitrator remuneration is clearly made. The skill remains helpful by offering the fee estimate.

---

# Scenario 36 — Out-of-range amount

## Prompt
Please estimate the institutional and tribunal fees for a DELOS arbitration at USD 2 billion.

## Expected behaviour
The skill first attempts to consult the machine-readable specification page (https://virjee-arbitration.com/arbitration-costs-calculator-machine-readable/) to determine whether USD 2 billion falls within the supported range. If the amount is outside the supported range, the skill says so clearly and does not extrapolate or invent a figure. It directs the user to the Delos institutional calculator or official fee schedule for amounts outside the supported range.

## Output should include
- Statement that the amount is outside the supported calculator range (if that is the case).
- Direction to the Delos cost calculator (https://delosdr.org/cost-calculator/) or official Delos fee schedule.
- No extrapolated figure.

## Output should avoid
- Producing a figure for an out-of-range amount.
- Silently extrapolating beyond the supported range.
- Failing to explain why a direct calculation is not provided.
- Treating query URLs or share URLs as guaranteed machine-result endpoints.

## Pass criteria
If the amount is outside the supported range, the output says so and directs to the appropriate fallback. No invented or extrapolated figures.

---

# Scenario 37 — Contract value used as proxy for likely amount in dispute

## Prompt
Our contract is worth EUR 6 million. We are considering SIAC arbitration. What would the fees look like?

## Expected behaviour
The user has provided contract value but not likely amount in dispute. The skill uses EUR 6 million as a proxy for the likely amount in dispute, states that assumption briefly, and calculates or directs using the Arbitration Costs Calculator for SIAC. It first attempts direct calculation from the machine-readable specification page (https://virjee-arbitration.com/arbitration-costs-calculator-machine-readable/). If not possible, it directs to the human-facing calculator page (https://virjee-arbitration.com/arbitration-costs-calculator/) with the inputs. It does not ask for the likely dispute value as a threshold question when contract value is available.

## Output should include
- Brief statement of the proxy assumption: "Using the contract value of EUR 6 million as a proxy for the likely amount in dispute."
- SIAC estimate using the Arbitration Costs Calculator.
- Stated assumptions: EUR 6 million, EUR currency, SIAC, tribunal size.
- Label as indicative.

## Output should avoid
- Refusing to calculate because the likely dispute value was not provided.
- Treating contract value and likely dispute value as interchangeable without flagging the proxy.
- Omitting the assumption statement.
- Treating query URLs or share URLs as guaranteed machine-result endpoints.

## Pass criteria
The proxy assumption is stated. Two-path logic is followed. The calculation proceeds. No unnecessary threshold question is asked.

---

# Scenario 38 — Unsupported currency: PLN / Poland context

## Prompt
We have a supply contract between a Polish and a German company worth PLN 5 million. We are considering ICC or DELOS. What would the estimated fees be?

## Expected behaviour
PLN is not a supported calculator currency. The skill identifies EUR as the most reasonable supported currency for a Polish/German context, notes the conversion assumption, and proceeds to calculate or direct using the Arbitration Costs Calculator in EUR. It first attempts direct calculation from the machine-readable specification page (https://virjee-arbitration.com/arbitration-costs-calculator-machine-readable/). If not possible, it directs to the human-facing calculator page (https://virjee-arbitration.com/arbitration-costs-calculator/) with the inputs. It does not refuse to calculate because PLN is not supported.

## Output should include
- Statement that PLN is not a supported calculator currency and that EUR has been used as the most reasonable equivalent.
- Note that the EUR conversion is approximate.
- ICC and DELOS estimates using the Arbitration Costs Calculator in EUR.
- Stated assumptions.
- Label as indicative.

## Output should avoid
- Refusing to calculate because PLN is not supported.
- Using PLN figures in the calculator without noting the currency limitation.
- Choosing USD or another currency without explaining why EUR is more appropriate for this context.
- Treating query URLs or share URLs as guaranteed machine-result endpoints.

## Pass criteria
EUR is selected as the most reasonable supported currency. The assumption is stated. Two-path logic is followed. The calculation proceeds. The output remains useful.

---

# Scenario 39 — Amount with no currency: cannot reasonably be inferred

## Prompt
We have a contract worth 10 million. We are thinking of HKIAC arbitration. What would the fees be?

## Expected behaviour
The amount is given without a currency. There is no other contextual information (no parties identified, no governing law, no seat, no sector) from which the currency can reasonably be inferred. The skill asks for the currency before calculating. It does not guess or default to USD or any other currency without basis. Once the currency is provided, the skill follows the two-path logic: direct calculation from the machine-readable specification page if possible, otherwise the human-facing calculator page with stated inputs.

## Output should include
- A brief, targeted question asking for the currency of the contract value.
- Explanation that the calculator requires a supported currency (EUR, USD, SGD, HKD, CHF).

## Output should avoid
- Defaulting to USD without stating the assumption.
- Defaulting to any currency without a stated basis.
- Producing a cost estimate without knowing the currency.
- Asking multiple questions when currency is the only missing item.
- Treating query URLs or share URLs as guaranteed machine-result endpoints once currency is provided.

## Pass criteria
The skill asks for the currency and explains why. It does not proceed with an assumed currency where none can be inferred.
