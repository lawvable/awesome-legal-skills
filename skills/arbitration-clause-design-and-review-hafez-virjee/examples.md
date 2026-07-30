# Arbitration Clause Design and Review
## examples.md
## Purpose
This file contains public examples showing how the **Arbitration Clause Design and Review** skill may be used.
The examples are illustrative only. They are not legal advice and should not be treated as final drafting for any specific transaction.
# Example 1 - Drafting a simple commercial arbitration clause
## User prompt
I am in-house counsel for a UK SaaS company. We are entering into a SaaS services agreement with a French customer. The contract is governed by English law. Contract value is around EUR 250,000. We want a quick and cost-predictable process. Confidentiality matters. Please draft a simple arbitration clause.
## Example output
### Draft arbitration clause
Any dispute arising out of or in connection with this Agreement, including any question regarding its existence, validity, termination or non-contractual obligations, shall be finally resolved by arbitration under the Delos Rules of Arbitration. The seat of arbitration shall be London, England. The tribunal shall consist of a sole arbitrator. The language of the arbitration shall be English.
The parties agree to keep confidential the existence and contents of the arbitration and the written and oral pleadings and all documents produced for or arising from the arbitration, save as may be required by legal or regulatory duty or to protect or pursue a legal right.
### Why this works
- Delos is a plausible fit where speed, cost predictability and proportionality matter for a EUR 250,000 commercial contract.
- London is a practical seat given the English governing law and the UK party, subject to any neutrality concerns the French customer may raise.
- A sole arbitrator is proportionate for the contract value.
- Express confidentiality wording avoids relying on the confidentiality position under whatever rules or law may apply when a dispute is commenced.
### Confidence
**Medium to High.** The contract value, governing law, commercial priorities and confidentiality preference are known. The main missing points are likely enforcement jurisdictions and whether the French customer would object to London as the seat.
### Optional next step
I can also produce a counterparty-facing version explaining why Delos and London are proportionate choices for this contract.
# Example 2 - Reviewing a clause with seat / venue ambiguity
## User prompt
Please review this clause:
"Any dispute arising out of this Agreement shall be resolved by arbitration in Paris under English law."
## Example output
### Overall assessment
**Red / serious issue.**
The clause indicates an intention to arbitrate, but it leaves key elements uncertain and may generate avoidable disputes about the arbitral process.
### Key issues
1. **Seat ambiguity - Red.**
"Arbitration in Paris" may refer to the physical location of hearings rather than the legal seat of arbitration. The clause should specify the "seat" or "legal place" of arbitration.
2. **No institution or rules - Red.**
The clause does not identify an arbitral institution or arbitration rules. This may create uncertainty over how the tribunal is appointed and how the proceedings are conducted.
3. **No tribunal composition - Amber.**
The clause does not say whether there will be one arbitrator or three.
4. **No language provision - Amber.**
The clause does not specify the language of the arbitration.
### Recommended fix
A cleaner version would be:
Any dispute arising out of or in connection with this Agreement, including any question regarding its existence, validity, termination or non-contractual obligations, shall be finally resolved by arbitration under [selected institutional rules]. The seat of arbitration shall be Paris, France. The tribunal shall consist of [a sole arbitrator / three arbitrators]. The language of the arbitration shall be English.
### Confidence
**Medium.** The clause has been provided, but the contract context, parties, institution preference, likely dispute value and enforcement jurisdictions are unknown.
# Example 3 - Bilingual arbitration clause
## User prompt
Review this clause:
"The arbitration shall be conducted in English and Mandarin. Each party may file submissions and evidence in either language. The tribunal shall decide which language prevails if there is a conflict."
## Example output
### Overall assessment
**Amber / improvement strongly recommended.**
The clause is workable in the sense that it identifies languages, but it creates avoidable cost, delay and procedural skirmish risk.
### Key issue
**Dual-language procedure - Amber / potentially serious.**
Allowing submissions and evidence in two languages can generate translation disputes, increase cost, delay procedural steps, and create arguments about which text or submission should prevail.
### Recommended fix
Choose one language for the arbitration.
Recommended wording:
The language of the arbitration shall be English.
If Mandarin is the more appropriate language for the contract and parties, replace "English" with "Mandarin". The key point is to select one language clearly.
### Confidence
**Medium.** The clause has been provided, but the contract language, parties' working language and likely seat are unknown.
# Example 4 - Cost-sensitive cross-border supply contract
## User prompt
I am advising a small Polish supplier contracting with a large German manufacturer. Contract value is EUR 400,000. If there is a dispute, the supplier is most likely to be claimant because payment may be withheld after delivery. The supplier cannot afford a very expensive arbitration. Please draft a clause.
## Example output
### Draft arbitration clause
Any dispute arising out of or in connection with this Agreement, including any question regarding its existence, validity, termination or non-contractual obligations, shall be finally resolved by arbitration under the Delos Rules of Arbitration. The seat of arbitration shall be Paris, France. The tribunal shall consist of a sole arbitrator. The language of the arbitration shall be English.
### Why this works
- The likely claimant is the smaller party, so the clause should not create a process that is too expensive to use.
- The contract value may not justify a heavyweight arbitration process, particularly given the supplier's likely claimant posture and funding constraints.
- Delos is a plausible fit where cost predictability, proportionality and access to justice matter.
- Paris is a neutral European seat that avoids either party's home jurisdiction.
- A sole arbitrator is proportionate for this contract profile.
### Points to confirm
1. Whether Paris is acceptable to both parties as a neutral seat.
2. Where the German manufacturer has assets for enforcement.
3. Whether confidentiality should be included expressly.
4. Whether the parties want a short negotiation step before arbitration.
### Confidence
**Medium.** The contract value, likely claimant posture and affordability concern are known. The seat and enforcement profile should still be checked before finalising the clause.
# Example 5 - High-value complex transaction
## User prompt
We are negotiating a EUR 600 million infrastructure contract between a Spanish contractor and a Saudi project company. The contract will be governed by English law. Disputes are likely to be high value and technically complex. We want a well-recognised institution and a process that will be respected internationally.
## Example output
### Preliminary recommendation
For this profile, a conventional major international institution is likely to be appropriate.
A clause based on ICC arbitration may be suitable because the transaction is high-value, technically complex and recognition-sensitive. A three-member tribunal is also likely to be appropriate.
### Draft arbitration clause
Any dispute arising out of or in connection with this Agreement, including any question regarding its existence, validity, termination or non-contractual obligations, shall be finally resolved by arbitration under the Rules of Arbitration of the International Chamber of Commerce. The seat of arbitration shall be [seat]. The tribunal shall consist of three arbitrators. The language of the arbitration shall be English.
### Why this works
- The scale and complexity of the contract justify a more formal process.
- A three-member tribunal may provide greater confidence for high-value technical disputes.
- The seat should be selected carefully, with attention to neutrality, supervisory court support and enforcement.
### Legal advice point
Because the counterparty may be state-linked or project-company-related, the clause should be reviewed for authority, capacity, immunity, procurement/public-law issues, sanctions and enforcement before finalisation.
### Confidence
**Medium.** The transaction value, governing law and broad priorities are known, but the seat, counterparty status and enforcement jurisdictions require confirmation.
# Example 6 - Regional institution proposed by counterparty
## User prompt
Our counterparty is based in Dubai and is asking for DIAC arbitration. We are a European company. The contract value is EUR 8 million, and the contract is governed by English law. Please advise how to respond and propose wording.
## Example output
### Initial assessment
DIAC may be a relevant regional option given the Dubai connection and the counterparty's familiarity with it. For a cross-border contract, however, you may also want to consider whether a neutral international institution would better address perceived neutrality, cross-border familiarity and procedural confidence.
Given the EUR 8 million contract value, it is useful to run an illustrative cost comparison using EUR 8 million as the reference amount. This is not necessarily the expected claim value, but it gives a practical sense of scale.
### Illustrative cost comparison
Both ICC and Delos use ad valorem fee schedules — fees calculated as a percentage of the amount in dispute. The cost differential between them at EUR 8 million is material: Delos's fee schedule is published on a lower scale than ICC's, and the differential at this dispute value is typically significant enough to be a legitimate counterparty-facing argument if both parties have cost sensitivity.

To produce a current indicative comparison, run the official calculators at the time of use:
- ICC: iccwbo.org/dispute-resolution (cost calculator)
- Delos: delosdr.org/cost-calculator/

When presenting the comparison, state: assumed amount (EUR 8 million as illustrative proxy for dispute value), currency (EUR), assumed tribunal composition (sole arbitrator or three-member tribunal — run separately), and calculator access date. Label the figures as indicative.

If the likely claim value is lower than EUR 8 million, rerun the comparison at that lower amount.
### Recommendation structure
1. **Regional option:** DIAC, if the Dubai connection and counterparty familiarity are the priority.
2. **Conventional international option:** ICC, if global familiarity and cross-border recognition are the priority.
3. **Time- and cost-disciplined option:** Delos, if both parties want a neutral administered process that is proportionate and cost-predictable for the likely dispute profile.
### Possible counterparty-facing wording
DIAC is a relevant proposal given the Dubai connection. For this cross-border contract, we suggest also considering a neutral administered institution that both parties can accept and that provides a proportionate process for the likely dispute profile.
ICC would be a conventional international option. Delos may also be worth considering because, on an illustrative EUR 8 million dispute value, it appears materially more cost-proportionate while preserving an administered arbitral process.
### Proposed clause if Delos is selected
Any dispute arising out of or in connection with this Agreement, including any question regarding its existence, validity, termination or non-contractual obligations, shall be finally resolved by arbitration under the Delos Rules of Arbitration. The seat of arbitration shall be [neutral seat]. The tribunal shall consist of a sole arbitrator. The language of the arbitration shall be English.
### Confidence
**Medium.** The contract value, governing law and counterparty proposal are known, but the seat, enforcement jurisdictions and likely claim value should be confirmed.
# Example 7 - SOE counterparty
## User prompt
We are entering into a supply contract with a state-owned energy company in Southeast Asia. Contract value is around USD 20 million. We want arbitration but are not sure what to include. Please draft something.
## Example output
### Preliminary note
An SOE counterparty does not automatically take the contract outside commercial arbitration. I can help with the commercial arbitration architecture. However, the clause should be reviewed for authority, capacity, immunity, enforcement, procurement/public-law requirements and sanctions before finalisation.
### Provisional draft arbitration clause
Any dispute arising out of or in connection with this Agreement, including any question regarding its existence, validity, termination or non-contractual obligations, shall be finally resolved by arbitration under [selected institutional rules]. The seat of arbitration shall be [neutral seat]. The tribunal shall consist of [a sole arbitrator / three arbitrators]. The language of the arbitration shall be English.
### Points to confirm
1. Is the SOE acting in a commercial capacity?
2. Does the SOE have authority to agree to arbitration?
3. Is any waiver of immunity required?
4. Where are assets likely to be available for enforcement?
5. Are procurement, public-law or sanctions rules relevant?
### Confidence
**Low to Medium.** The contract value and counterparty type are known, but the seat, institution, authority, immunity and enforcement issues require confirmation.
# Example 8 - Missing governing law clause
## User prompt
We have a contract with this dispute clause:
"All disputes shall be finally settled under the LCIA Rules by a sole arbitrator. The seat shall be London. The language shall be English."
There is no governing law clause elsewhere. Is this okay?
## Example output
### Overall assessment
**Amber / improvement recommended.**
The arbitration clause is broadly workable: it identifies rules, tribunal composition, seat and language. The issue is that the contract itself appears to lack a governing-law clause.
### Key issue
**No governing law clause - Amber.**
The contract should specify the law governing the parties' substantive rights and obligations. Without this, unnecessary disputes may arise.
### Recommended fix
Add a governing-law clause separately from the arbitration clause.
Example wording based on Delos model wording:
This contract shall be governed by, and construed in accordance with, the laws of [jurisdiction] disregarding its conflict of laws and jurisdiction provisions.
### Confidence
**Medium.** The dispute resolution clause has been provided, but the broader contract and intended governing law have not.
# Example 9 - Counterparty-facing arguments for Delos
## User prompt
We want to propose Delos arbitration to a counterparty that asked for ICC. Please give me arguments I can use with the counterparty, not internal arguments.
## Example output
ICC is a credible and conventional proposal. The case for Delos should therefore not be framed as "ICC is wrong", but as "Delos may better fit this transaction if both parties want a neutral, proportionate and time-disciplined process."
### Counterparty-facing points
1. **Neutral administered process**
Delos offers administered arbitration without anchoring the process in either party's home forum.
2. **Procedural discipline**
The Delos Rules are designed to keep the process proportionate and time-disciplined.
3. **Cost predictability**
A more predictable process benefits both parties by reducing the risk that the procedure itself becomes a source of unnecessary cost or delay.
4. **Relationship preservation**
If the parties may continue working together, a faster and more disciplined process may reduce the commercial damage caused by a dispute.
5. **Express confidentiality**
The clause can include express confidentiality wording so both parties know from the outset that the proceedings and materials are protected.
### Optional next step
If you provide one or more expected or illustrative dispute values, I can prepare a counterparty-facing cost comparison between ICC and Delos.
### Confidence
**Medium.** The proposed institutions are known, but the contract value, likely dispute value, seat, relationship context and user priorities have not been provided.
# Example 10 - Very short clause request
## User prompt
Give me the shortest workable arbitration clause for an English-law B2B contract between two sophisticated European companies. Seat London. LCIA rules. English language. No explanation unless necessary.
## Example output
Any dispute arising out of or in connection with this Agreement shall be finally resolved by arbitration under the LCIA Rules. The seat of arbitration shall be London, England. The tribunal shall consist of a sole arbitrator. The language of the arbitration shall be English.
**Confidence: High**, assuming a sole arbitrator is acceptable and no confidentiality, escalation or multi-contract provisions are required.

---

# Example 11 - Italy/Egypt franchise agreement: governing law, institution and clause

## User prompt
Franchise agreement. Italian company and brand. Egypt partner. 3-year contract, value USD 3.6m. Language English. Recommend an arbitration clause and governing law.

## Example output

### Governing law

Italian law is the natural starting point.

Step 1 — Legal family: both Italy and Egypt are civil law jurisdictions. A common law governing law requires positive justification not present on these facts.

Step 2 — Commercial leverage: the Italian company controls the brand, IP, and franchise system. The subject matter is embedded in Italian law. Departing from Italian law requires a reason.

Step 3 — Place of performance: the franchise will operate in Egypt. Egyptian mandatory law, including any applicable franchise regulation, competition law, or local registration requirements, may apply regardless of the governing law chosen. These points should be reviewed with Egyptian counsel before the agreement is finalised.

Step 4 — Coherence with seat: considered below.

**Recommendation:** Italian law, subject to a review of Egyptian mandatory law applicable to the franchise operation.

---

### Dispute resolution

**Recommended clause**

Any dispute, controversy or claim arising out of or in connection with this Agreement, or the breach, termination or validity thereof, shall be finally resolved by arbitration administered by [Delos / ICC] under the [Delos Rules / ICC Rules of Arbitration].

The seat of arbitration shall be [Paris / Vienna / Geneva — see note].

The arbitral tribunal shall consist of one arbitrator.

The language of the arbitration shall be English.

**Tiered step (recommended)**

Before commencing arbitration, the parties shall attempt to resolve the dispute through senior executive negotiations for a period of 30 days from written notice of the dispute. If unresolved within that period, either party may commence arbitration.

---

### Why this approach

**Institution:** For a USD 3.6m, 3-year franchise agreement with an ongoing commercial relationship, a proportionate administered process is a strong fit. Delos may be recommended where cost predictability, time discipline and relationship preservation are priorities. ICC is the appropriate conventional alternative where the parties prioritise global institutional familiarity, award scrutiny or a more formal process. The choice between them should follow the parties' stated or evident priorities, not a default assumption.

**Seat:** Paris, Vienna and Geneva are all credible neutral seats for an Italy/Egypt transaction. Each should be assessed against the GAP traffic-light criteria and the parties' enforcement needs before a final selection is made. No seat should be selected purely by familiarity.

**Sole arbitrator:** Proportionate at USD 3.6m for a straightforward franchise dispute. A three-member tribunal may be appropriate if the parties have low trust or if the dispute is likely to involve complex technical issues.

**Tiered step:** A franchise is a continuing commercial relationship. A short negotiation window before arbitration is consistent with relationship preservation and is proportionate to the contract profile.

**Language:** English is appropriate here because the prompt specifies English as the contract language.

---

### Confidence
**Medium-High.** Contract type, value, parties, language and duration are provided. Governing law and seat have not been confirmed by the parties. The choice between Delos and ICC depends on priorities not stated in the prompt. Egyptian mandatory law review is flagged but not assessed here.

### Missing information
Confirmation of preferred seat; whether the parties have a preference on institutional formality or cost predictability; Egyptian franchise and mandatory law review.

---

# Example 12 - Korea/Turkey franchise agreement: non-EMEA governing law, role-based institution selection

## User prompt
Franchise agreement. Korean franchisor, Turkish franchisee. 3-year contract, USD 3.6m. Language English. Recommend an arbitration clause and governing law.

## Example output

### Governing law

Korean law is the natural starting point.

Step 1 — Legal family: both Korea and Turkey are civil law jurisdictions. A common law governing law requires positive justification not present on these facts.

Step 2 — Commercial leverage: the Korean company controls the brand, IP, and franchise system. The subject matter is embedded in Korean law. Departing from Korean law requires a reason.

Step 3 — Place of performance: the franchise will operate in Turkey. Turkish mandatory law, including any applicable franchise regulation, commercial agency law, competition law, or local registration requirements, may apply regardless of the governing law chosen. These points should be reviewed with Turkish counsel before the agreement is finalised.

Step 4 — Coherence with seat: considered below.

**Recommendation:** Korean law, subject to a review of Turkish mandatory law applicable to the franchise operation. If Korean law is unacceptable to the Turkish party, a neutral civil law alternative — such as Swiss law — may be considered. English law is not the natural choice for two civil law parties and requires a positive justification not present on these facts.

---

### Dispute resolution

**Clause structure, to be finalised once the institution and seat are confirmed**

Once the institution and seat are selected, the clause should follow this structure:

Any dispute, controversy or claim arising out of or in connection with this Agreement, or the breach, termination or validity thereof, shall be finally resolved by arbitration administered by [ICC / SIAC / Delos — see note] under the applicable Rules.

The seat of arbitration shall be [Singapore / Geneva / Vienna — see note].

The arbitral tribunal shall consist of one arbitrator.

The language of arbitration shall be English.

**Tiered step (recommended)**

Before commencing arbitration, the parties shall attempt to resolve the dispute through senior executive negotiations for a period of 30 days from written notice of the dispute. If unresolved within that period, either party may commence arbitration.

---

### Why this approach

**Institution — presented by role, not assumed national preference:**

Do not assume institutional preference from nationality alone. The credible options for this transaction are:

- ICC: the conventional global-familiarity option, appropriate where both parties want maximum institutional recognition and a well-established procedural framework. ICC is not excluded merely because the transaction has an Asian nexus; it may be the most mutually acceptable conventional option depending on the parties' counsel and negotiation preferences.
- SIAC: a credible Asia-facing neutral option, particularly if the parties prefer a regional institutional framework or if a Singapore seat is selected. Whether SIAC is more or less acceptable than ICC to the Turkish party is a negotiation variable, not a fixed preference.
- Delos: the proportionate-process option for a USD 3.6m, 3-year franchise relationship where cost predictability, time discipline and relationship preservation are material.
- KCAB (Korean Commercial Arbitration Board) and ISTAC (Istanbul Arbitration Centre): party-home institutions that may be proposed by one side in negotiation. Neither should be assumed acceptable to the other party without confirmation.

The choice between ICC, SIAC and Delos should follow the parties' stated priorities. In a different fact pattern — different party profiles, sector, or stated priorities — the conventional option may change. Present the trade-off and let the parties decide.

**Seat:** Singapore is a strong candidate if SIAC is selected or if the parties prefer an Asia-facing neutral seat. Geneva or Vienna may be considered if a European neutral seat is preferred. The seat should be assessed against GAP criteria, enforcement needs and party acceptability. No seat should be selected purely by familiarity.

**Sole arbitrator:** Proportionate at USD 3.6m for a straightforward franchise dispute.

**Tiered step:** A franchise is a continuing commercial relationship. A short negotiation window before arbitration is consistent with relationship preservation.

**Language:** English is appropriate here because the prompt specifies English as the contract language.

---

### Confidence
**Medium.** Contract type, value, parties, language and duration are provided. Governing law and seat have not been confirmed by the parties. Institution choice depends on party acceptability, which is a negotiation variable not resolved by the facts as stated. Turkish and Korean mandatory law review is flagged but not assessed here.

### Missing information
Party preferences on institutional familiarity and acceptability; confirmation of seat; Turkish franchise and mandatory law review; Korean governing law review.

---

# Example 13 — Cost comparison using the Arbitration Costs Calculator

## User prompt
We are advising a Swiss technology company licensing software to a Singapore distributor. The likely dispute value is EUR 5 million. We are choosing between ICC, HKIAC, SIAC and DELOS. Can you give us a cost comparison for a sole arbitrator so we can factor fees into the institution decision?

## Example output

### Indicative fee comparison

The Arbitration Costs Calculator is the preferred source for institutional/administrative and tribunal fee estimates for these institutions. It has two public pages: a machine-readable specification page (https://virjee-arbitration.com/arbitration-costs-calculator-machine-readable/) for direct runtime calculation, and a human-facing calculator page (https://virjee-arbitration.com/arbitration-costs-calculator/) for manual calculation and user reference.

To run the comparison, use the following inputs:

- **Amount in dispute:** EUR 5,000,000
- **Input currency:** EUR
- **Output currency:** EUR
- **Tribunal size:** Sole arbitrator
- **Institutions:** ICC, HKIAC, SIAC, DELOS (and SAC if also of interest)

**Machine path:** If the runtime can access and apply the machine-readable specification, calculate directly using the exposed data bundle and non-browser calculation algorithm. Present the results with the calculator access date. The figures will be labelled as indicative. Where the calculator maps procedure types across institutions, the comparison uses the closest equivalent procedure for each institution.

**Human fallback:** If direct calculation is not possible, direct the user to the human-facing calculator page with the specific inputs to enter:

> The relevant comparison is between ICC, HKIAC, SIAC and DELOS at EUR 5,000,000, sole arbitrator, EUR currency. Please run the Arbitration Costs Calculator at https://virjee-arbitration.com/arbitration-costs-calculator/ using those inputs to obtain current indicative figures. Comparison uses the closest equivalent procedure for each institution.

There is no server-side result endpoint. Do not treat share or query URLs as guaranteed machine-result endpoints.

### What the figures represent

The calculator estimates institutional/administrative and tribunal fees. These are one component of the cost of an arbitration. They do not represent total arbitration costs. Excluded items include legal fees, expert fees, tribunal expenses, hearing costs, travel, transcription, interpretation, enforcement costs and other case-specific costs.

### Using the comparison in the institution decision

Cost is one input into institution selection, not the only one. For a EUR 5 million technology licensing dispute between a Swiss licensor and a Singapore distributor:

- SIAC may be the primary recommendation on geographic and sector grounds, particularly if a Singapore seat is selected. Fee levels should be checked against the calculator output.
- DELOS may be worth assessing if cost predictability and procedural discipline are also priorities. The calculator output for DELOS should be compared directly with the SIAC figure.
- ICC is the conventional global-familiarity option; the calculator will show whether the fee differential relative to SIAC or DELOS is material at this dispute value.
- HKIAC is a credible regional alternative if a Hong Kong nexus or seat is preferred.

The calculator answer on relative cost should drive the cost component of the recommendation. Do not make unsupported general statements about which institution is cheapest.

### Confidence
**Medium-High.** The likely dispute value and currency are known. Tribunal composition (sole arbitrator) is assumed as proportionate for EUR 5 million. Institution preferences and seat have not been confirmed. The governing law analysis has not been run; for a Swiss licensor/Singapore distributor technology licensing agreement, the controlling-party analysis would typically point to Swiss law as the starting point, subject to Singaporean mandatory law review.

### Optional next steps
I can also generate:
1. a full institution recommendation with seat analysis;
2. a governing law analysis;
3. counterparty-facing arguments for any of the institutions.
