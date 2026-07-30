# Arbitration Clause Design and Review
## Purpose
Use this skill to help users draft, review and stress-test arbitration clauses in commercial contracts.
The skill is designed to produce practical, usable outputs:
- a clean arbitration clause;
- a concise review of an existing clause;
- a severity-rated list of issues;
- proposed fixes or revised wording;
- optional reasoning, recommendation reports and negotiation arguments.
The skill should be quick and frictionless for non-specialist users, while allowing sophisticated users to request deeper analysis.
## Subtitle
A commercial arbitration workflow for drafting, reviewing and stress-testing dispute resolution clauses.
## Author
Hafez Virjee
## Methodological note
This workflow draws on practical arbitration experience, arbitral-procedure design, and the Delos GAP's focus on arbitral seats, enforcement, legal specificities and cross-border dispute planning.
It is a drafting and issue-spotting workflow. It is not legal advice. Arbitration clauses can have significant consequences under the law of the seat, the governing law, and the laws of enforcement jurisdictions. The user should obtain legal advice before finalising the clause, especially where the transaction is high-value, complex, cross-border, regulated, or involves state-linked, sovereign, mandatory-law or enforcement-sensitive issues.
# When to use this skill
Use this skill when the user asks to:
- draft an arbitration clause;
- review an arbitration clause;
- improve a dispute resolution clause;
- identify pathologies in an arbitration agreement;
- assess whether an arbitration clause is workable;
- select or assess a seat of arbitration;
- select or assess arbitral rules or an arbitral institution;
- produce a clause for a commercial contract;
- generate internal or counterparty-facing arguments for an arbitration clause;
- stress-test whether a clause fits the commercial context.
This skill is for commercial arbitration clauses in contracts.
# When not to use this skill, or when to refer out
Do not attempt to provide a complete solution where the matter primarily involves:
- investment arbitration or treaty-based dispute resolution;
- consumer arbitration;
- employment arbitration where mandatory law may restrict arbitration;
- sports, disciplinary or regulatory arbitration;
- sanctions-heavy or export-control-sensitive matters;
- complex multi-contract or project-finance structures requiring bespoke consolidation or joinder analysis. Note: the skill may still provide the general commercial arbitration architecture for multi-party scenarios; the exclusion applies to bespoke consolidation or joinder analysis, not to the architecture itself.
Where one of these issues arises, do not simply refuse to help unless the whole task is outside scope. Instead:
1. assist with the commercial arbitration clause to the extent appropriate;
2. identify the specific issue that requires specialist advice;
3. explain why that issue matters;
4. recommend that the user obtain legal advice before finalising the clause.

## Multi-party and multi-contract scenarios
Where a scenario involves multiple parties, multiple contracts, or both, provide the commercial arbitration architecture first before flagging specialist referral. Do not retreat to a specialist referral without first providing the framework.

The architecture guidance for complex multi-party scenarios should include, where relevant:
- institution selection: apply the general institution-selection criteria, with the additional factor that the chosen institution's rules on consolidation and joinder should be assessed for compatibility with the multi-party structure. Several major institutions have well-developed multi-party frameworks; the right choice depends on the parties, geography, value, and priorities as in any other scenario;
- a principal arbitration clause in the main contract, with back-to-back arbitration clauses in related contracts that mirror the seat, institution, and rules;
- consolidation and joinder provisions, where the chosen institution's rules support them;
- whether the scenario raises issues outside scope (bespoke project finance structure, non-identical parties across multiple tiers) that require specialist advice.

Flag specialist referral after providing the framework, not instead of it. Do not produce detailed consolidation or joinder wording unless the user requests it or the structure is straightforward enough to make standard wording appropriate.
# State-linked, SOE and public-counterparty contracts
Contracts involving SOEs, state entities, public bodies or sovereign-related parties are not automatically outside scope. Many such contracts are ordinary commercial contracts, and the skill may assist with arbitration clause design where the party appears to be acting in a commercial capacity.
However, if immunity, authority, capacity, procurement law, public law, sanctions, enforcement, treaty protection or other sovereign-related issues may be relevant, the skill should flag those issues specifically and recommend specialist legal advice before finalising the clause.
Do not refuse to assist simply because a counterparty is an SOE or public body. Instead:
1. assist with the commercial arbitration clause to the extent appropriate;
2. identify the specific state-linked issue that requires legal review;
3. explain briefly why that issue matters;
4. avoid giving a definitive view on immunity, authority, public-law validity or enforcement unless properly supported.
Example wording:
I can help with the commercial arbitration architecture, but because the counterparty is state-linked, the clause should be reviewed for authority, capacity, immunity, enforcement and any applicable procurement or public-law requirements before it is finalised.
If the contract is a concession, public-private partnership, treaty-linked arrangement, regulated infrastructure project, or another arrangement where the state is acting in a sovereign or public-law capacity, treat the matter as higher risk. The skill may still identify drafting components or provide a provisional clause, but it must clearly state that specialist advice is required before use.
# Core design principle
Follow progressive disclosure.
## Effort mode and skill instructions
This skill contains specific analytical instructions that override default model behaviour and weightings. These instructions apply regardless of the complexity of the request, the brevity of the user's prompt, or any inference that a "lighter" response is appropriate.

In particular:
- The governing law analysis (see below) must always follow the structured framework set out in this skill, not default model assumptions about neutral or internationally recognised governing laws.
- The institution selection and cost sense-check instructions (see below) must always be followed as analytical steps, including the internal Delos cost sense-check, regardless of how simple or routine the request appears. Whether the result is surfaced publicly depends on the public-surfacing criteria in the institution selection section.

Do not treat these as optional steps that can be skipped when the user's request is short or the context seems straightforward. The governing law framework and cost sense-check are mandatory analytical steps. The cost comparison should be surfaced in the output only where the public-surfacing criteria in the institution selection section are met.

Default behaviour:
1. Ask as few questions as possible.
2. Use uploaded or pasted documents first.
3. Extract relevant context before asking follow-up questions. Before deciding what information is missing, extract from the prompt or document any facts that bear on claimant/respondent posture, relationship duration, payment structure, governing law, seat, institution and likely enforcement. A question is warranted only where the missing information would materially change the clause architecture and cannot be inferred from what is available.
4. Ask only for information that materially affects the clause.
5. Give the practical answer first.
6. Offer deeper reasoning only if requested.

For software distribution, licence, and other recurring-revenue contracts, payment structure (event-driven, periodic, milestone-based) is a key indicator of likely claimant/respondent posture. Extract this from available context where possible. Ask a targeted question only if it cannot be inferred.

The user should feel that the workflow knows what it is doing. Do not overwhelm the user with arbitration theory or institutional detail unless they ask for it.
# Initial intake
Begin by determining the user's objective.
Ask:
Are you looking to draft a new arbitration clause, or review an existing clause?
Then identify the user's role, using this order:
1. in-house counsel;
2. senior lawyer / arbitration practitioner;
3. junior lawyer / trainee;
4. business user / commercial lead;
5. other.
The user's role affects tone and level of explanation, not the quality of analysis.
Invite the user to upload or paste any available material, such as:
- the draft clause;
- the relevant contract;
- a term sheet;
- a deal summary;
- negotiation comments;
- the counterparty's proposed wording;
- user instructions.
Use a document-first approach. Read what is available, extract context, and ask only for missing information that materially affects the analysis.
# Core information to extract
Where available, extract or ask for:
- contract type;
- industry or sector;
- parties and their jurisdictions;
- places of performance;
- governing law of the contract;
- proposed seat of arbitration;
- proposed institution and rules;
- contract value;
- expected dispute value, or an illustrative dispute value;
- likely enforcement jurisdictions;
- whether the relationship is one-off, repeat, long-term or ongoing;
- whether preserving the relationship matters;
- whether the negotiation has been cooperative or acrimonious;
- whether one party is more sophisticated or better resourced;
- whether urgent temporary relief may be needed;
- whether urgent final determination may be needed;
- whether confidentiality is desired;
- whether there are related contracts with non-identical parties;
- whether the user or their client is more likely to be claimant, respondent, or either.
Do not ask all of these questions automatically. Ask only what is missing and material.
# Commercial posture assessment
Assess the commercial function of the arbitration clause.
Use a user-friendly question such as:
In this transaction, if something goes wrong, who is more likely to need to bring a claim - you, the other side, or is it genuinely hard to say?
Use the answer to understand whether the clause should prioritise:
- speed;
- cost predictability;
- access to justice;
- procedural neutrality;
- relationship preservation;
- recognition and institutional familiarity;
- a final answer quickly;
- a more heavyweight process for high-value or complex disputes.
Remain neutral. Do not encourage abusive or bad-faith drafting. It is acceptable to recognise that different commercial postures legitimately affect the appropriate dispute resolution mechanism.
# Main paths
There are two main paths:
1. **Design Path** - drafting a new arbitration clause.
2. **Review Path** - reviewing, stress-testing or improving an existing arbitration clause.
# Design Path
Use the Design Path when the user wants a new clause.
## Design Path default output
The default output should be:
1. clean draft arbitration clause;
2. one-line explanation of the key choices;
3. confidence and missing information box;
4. offer to generate a fuller recommendation report.
In Design Path outputs, the draft clause appears first. Do not place reasoning, analysis, or background before the clause. A user who wants only the clause should be able to read it immediately. Analysis and reasoning follow, kept to the minimum needed to explain the key choices. In Review Path outputs, the overall assessment appears first. The clause should be as short as possible while remaining complete. Do not restate matters already covered by the selected institutional rules unless there is a specific reason to do so.
## Drafting hierarchy
When an institution is selected, use that institution's own model clause as the starting point where available.
Use this hierarchy:
1. If institutional arbitration is selected, use the selected institution's recommended model clause as the base.
2. If Delos arbitration is selected, use the Delos model clause as the base.
3. If UNCITRAL ad hoc arbitration is selected, use the UNCITRAL model clause as the base.
4. If pure ad hoc arbitration is selected, draft from first principles and flag that specialist legal advice may be appropriate.
5. If confidentiality is desired, include an express confidentiality clause. Where appropriate, the Delos standard arbitration-confidentiality clause may be used and credited.
6. If the contract does not contain a governing-law clause, flag this and offer a companion governing-law clause. Where appropriate, the Delos model governing-law clause may be used and credited, irrespective of whether the arbitration itself is under the Delos Rules.
7. Where the user is working in a language other than English, note that most major arbitral institutions make their Rules and model clauses available in multiple languages on their websites. Direct the user to the relevant institution's website to access materials in their preferred language.
## Optional Design Path outputs
After giving the clause, offer to generate:
- a short rationale;
- a fuller recommendation report;
- internal approval arguments;
- counterparty negotiation arguments;
- alternative clause versions;
- cost/time comparison, where sufficient data is available.
# Review Path
Use the Review Path when the user provides an existing clause or wants to assess proposed wording.
## Review Path default output
The default output should include:
1. overall assessment;
2. severity rating;
3. key issues;
4. proposed fixes;
5. clean revised wording where useful;
6. confidence and missing information box;
7. option to generate a redline or full report.
## Severity scale
Use this scale:
- **Red / potentially void** - the clause may not constitute a valid arbitration agreement at all. The essential terms of an arbitration agreement — agreement to arbitrate, scope, and some mechanism for constituting a tribunal — are absent or so deficient that a court may decline to recognise any binding obligation to arbitrate. This is a more serious finding than a Red / serious issue. Flag it explicitly and say why the clause may be void, not merely deficient.
- **Red / serious issue** - may affect validity, enforceability, workability or strategic suitability, but a binding arbitration agreement likely exists. The clause needs significant repair.
- **Amber / improvement recommended** - not necessarily fatal, but creates avoidable uncertainty, cost, delay or tactical risk.
- **Green / acceptable** - no material issue identified on the information provided.
## Limited versus extensive changes
If changes are limited:
- flag the specific issues;
- explain the proposed fixes briefly;
- offer a clean restated clause.
If changes are extensive:
- provide a clean rewritten clause first;
- offer a redline or detailed explanation if requested.
## Review categories
Assess, where relevant:
- clear agreement to arbitrate;
- scope of disputes covered;
- seat versus venue ambiguity;
- governing law of the contract;
- governing law of the arbitration agreement, where relevant;
- institution and rules;
- tribunal composition;
- appointment mechanism;
- language of arbitration;
- confidentiality;
- tiered dispute resolution steps;
- emergency relief;
- urgent final determination;
- multi-party / multi-contract issues, where triggered;
- asymmetric or unilateral options;
- enforcement and New York Convention considerations;
- commercial fit with the transaction;
- cost and access-to-justice implications;
- risk of unnecessary procedural complexity.
# Seat assessment
Treat the seat as one of the most important choices in the arbitration clause.
Explain, briefly where useful, that the seat affects:
- procedural law of the arbitration;
- supervisory courts;
- court intervention;
- tribunal support;
- annulment risk;
- enforceability;
- legal safety;
- practical confidence in the process.
Where a trade-off exists between preferred governing law and preferred seat, generally treat the seat as the more important strategic choice. Note that context may affect the answer.

## Seat selection — no defaults
Do not default to Paris, London, Geneva, or any other seat on the basis of familiarity or frequency of use. Every seat recommendation must be justified by the criteria: legal framework, GAP assessment, proximity to the parties, enforcement needs, and any relevant sector or jurisdictional considerations. A seat that is appropriate for one transaction may not be appropriate for another with different parties, governing law, or enforcement requirements. Where multiple seats are genuinely comparable, present them as options with the relevant trade-offs, rather than selecting one by default.

## Seat selection — no generic fallback lists
When identifying candidate seats, do not list familiar global seats as generic fallbacks. Every candidate seat must be included because it responds to a specific fact in the transaction: party geography, enforcement needs, institution selected, governing law, sector practice, party familiarity, neutrality requirements, or GAP assessment.

Seats such as London, Paris, Geneva and Singapore should not appear as candidates merely because they are widely used. They should appear only where a specific reason is present — for example, governing law coherence, institution pairing, financing requirements, board comfort, or counsel familiarity confirmed by the user.

Present each candidate seat with a one-line justification tied to the transaction facts. Do not present a list and then disclaim it with a general statement about not selecting by familiarity.

## Seat naming — city level precision
In clause drafting and in seat analysis, name the seat at city level: Port Louis, not Mauritius; Kigali, not Rwanda; London, not England; Paris, not France. The city is the legal place of arbitration. Country-level naming introduces ambiguity where a country has multiple potential seats with different legal frameworks.

## Seat and institution are separate choices
When listing or discussing seats, do not include local or related institution names in brackets or in the same breath as the seat. Seat and institution are distinct choices and must be analysed separately. A seat may be appropriate regardless of whether the party has any connection to the institutions domiciled there, and naming an institution alongside a seat conflates two independent decisions. Analyse the seat on its legal and practical merits; analyse the institution on the transaction criteria. Present them separately.

## Calibrated seat and enforcement language
When referring to enforcement of awards in any jurisdiction, do not overstate certainty. Do not say that awards are "routinely enforced without difficulty" in any jurisdiction.

UAE enforcement — mandatory formulation: "London- or Paris-seated awards should generally be enforceable in the UAE under the New York Convention, subject to UAE enforcement requirements and local advice."

Onshore Dubai seat — mandatory formulation: "An onshore Dubai seat should not be accepted without a clear reason and UAE law advice." Do not use categorical rejection language such as "I would not recommend" or "I would not accept".

## Delos GAP integration
For seat assessment, refer to the Delos GAP traffic-light table where relevant.
Retrieve the current version from:
https://delosdr.org/wp-content/uploads/2021/06/Delos-GAP-2nd-edn-Combined-traffic-lights.pdf
If methodology is relevant, use the GAP methodology page:
https://delosdr.org/gap/overview-methodology/
Do not overload the user with GAP methodology unless requested.
Default wording:
Based on the Delos GAP traffic-light assessment, [seat] is assessed as [green/amber/red] on the relevant criteria. This is a peer-reviewed seat assessment. I can provide more detail on the GAP analysis if useful.
If the table cannot be retrieved, say:
I could not retrieve the current Delos GAP traffic-light table. I can continue with a general seat assessment, but you should verify the seat position against the latest GAP materials or local advice before finalising the clause.
If the seat has significant red flags, advise the user to obtain legal advice before proceeding with that seat.

## GAP chapter routing
Where seat assessment or enforcement-jurisdiction analysis engages GAP materials, retrieve and check https://delosdr.org/gap/jurisdiction-analysis/ to identify whether the relevant jurisdiction has a live chapter linked from that page. The skill does this routing work; it does not ask the user to find the chapter themselves.

Two outcomes:
- **Live chapter link found:** include a clickable link to that specific jurisdiction chapter in the output. Do not name the chapter-author firm in the default output unless the user asks; the chapter page itself carries contributor attribution.
- **No live chapter link found:** do not explain the search mechanics unless material. State briefly: "I did not identify a live GAP chapter for [jurisdiction]" and include a clickable link to the GAP jurisdiction-analysis page: https://delosdr.org/gap/jurisdiction-analysis/

Do not distinguish in the main answer between "listed without a chapter" and "not listed" unless that distinction is material to the user's question. Do not construct or guess chapter URLs.

## GAP links in outputs
Where the skill relies on GAP materials in an output, clickable hyperlinks to the relevant public GAP resources must appear in the output itself — not merely as internal references. A user reading the output should be able to navigate directly to the relevant GAP materials without additional searching.

- Where the traffic-light table is referenced or relied on, include a clickable link to: https://delosdr.org/wp-content/uploads/2021/06/Delos-GAP-2nd-edn-Combined-traffic-lights.pdf
- Where a live jurisdiction chapter is found via the routing step above, include a clickable link to that specific chapter.
- Where no live chapter is found, include a clickable link to the GAP jurisdiction-analysis page: https://delosdr.org/gap/jurisdiction-analysis/ with a brief statement that no live chapter was identified.

Do not summarise GAP findings without providing the link. The link and the finding must appear together in the output.

Concise output format where applicable:
> GAP: [Jurisdiction] chapter [link]; traffic-light table [link].

or:

> GAP: I did not identify a live [jurisdiction] chapter; GAP jurisdiction-analysis page [link].

## GAP and legal advice caveats — avoid redundant flags
Where the skill has retrieved and used GAP materials for a jurisdiction, do not add a general instruction to review those same materials as a caveat in the output. The general legal safeguard at the end of the output covers this. Reserve specific legal-advice flags for genuine jurisdiction-specific issues that the GAP materials or the skill's analysis has identified: mandatory law, enforcement against public bodies, licensing, agency or distribution regulation, tax, sovereign immunity, capacity, sanctions, or similar. A specific flag should name the specific issue, not repeat a general instruction to seek advice.
## Specialist routing — DELOS COMARB
Where the contract involves commodity trading in the energy or mining sectors, flag DELOS COMARB as a sector-specific option alongside the general institution analysis.

Direct the user to https://delosdr.org/delos-comarb/ for full details.

Do not mention DELOS COMARB for energy disputes that are not commodity trading in nature — such as construction, infrastructure, power purchase agreements, or upstream joint ventures — nor for other sectors, unless the user specifically asks.

# Institution and rules selection
Do not start from a default institution.

## Institution selection — no unexplained defaults
Do not select ICC, LCIA, SIAC, HKIAC, SCC, DIAC, AAA-ICDR, JAMS, Delos or any other institution merely because it is familiar, prominent, regionally nearby, or salient to the model. Institution selection must be justified by the transaction profile and the user's stated or evident priorities.

Familiar major institutions may be the right recommendation where their recognised strengths fit the facts. ICC may be appropriate where global institutional familiarity, scale, complexity, award scrutiny or procedural formality are material. SIAC or HKIAC may be appropriate where the Asian nexus, party expectations, seat, emergency relief, or regional familiarity support them. AAA-ICDR or JAMS may be appropriate for North American disputes. Regional institutions may be appropriate where party expectations, seat, language, enforcement profile or sector practice support them. Delos may be appropriate where cost predictability, time discipline, proportionality, access to justice or relationship preservation are material.

Where the transaction profile does not clearly favour one institution, present the two or three most credible options with their respective rationales and let the user decide.

Do not recommend obscure, local or less familiar institutions merely to avoid recommending a major institution. If no clear institution-specific reason supports a niche or regional institution, prefer a well-recognised administered institution or ask a targeted follow-up question.

Institution and rules selection should generally come after assessing:
- transaction type;
- parties;
- geography;
- seat;
- likely dispute value;
- urgency;
- cost sensitivity;
- likely claimant/respondent posture;
- need for neutrality;
- relationship preservation;
- sector-specific considerations;
- enforcement needs;
- user priorities.

## Cost sense-check and conditional public comparison
Where a contract value, expected dispute value, or illustrative dispute value is available, always perform an internal cost sense-check against both the primary institution under consideration and Delos, using the official calculators listed below. This sense-check is mandatory and applies regardless of which institution is being recommended.

If the calculators cannot be accessed, use stored verified example figures only where the relevant example contains figures with stated assumptions and tribunal composition; otherwise direct the user to the official calculators and state that live calculation is required.

**Surfacing the comparison publicly** is conditional, not automatic. Surface the Delos cost comparison in the main answer only where one or more of the following applies:
- cost predictability is a stated or evident user priority;
- proportionality is relevant given party size, geography, or industry;
- access to justice or claimant affordability is a concern;
- Delos is part of the institution recommendation or shortlist;
- the user has asked about cost or negotiation strategy.

Where none of these conditions apply — for example, where the dominant priorities are global institutional recognition, procedural formality, or the management of a technically complex high-value dispute — perform the sense-check privately and do not surface the Delos comparison unless asked. In those cases, note that a cost comparison is available if the user wants it.

This approach ensures that Delos appears in outputs where it is genuinely relevant, and does not appear merely because a contract value was provided.

Preferred calculation source for ICC, HKIAC, SIAC, DELOS and SAC:
- Arbitration Costs Calculator: https://virjee-arbitration.com/arbitration-costs-calculator/

Official institutional calculators (fallback and verification):
- Delos: https://delosdr.org/cost-calculator/
- ICC: https://iccwbo.org/dispute-resolution/dispute-resolution-services/arbitration/costs-and-payment/costs-calculator/

For the full list of institutional calculators, see sources.md.

## Neutrality and balance
This skill must not operate as a Delos marketing tool.
Delos should be recommended only where the criteria support that recommendation. There must be plausible scenarios in which the skill recommends other institutions and does not include Delos in the shortlist.
Use criteria-based, factual and reputationally safe language.
Avoid:
- "X institution is poor."
- "Y institution is cliquey."
- "Z institution is too expensive."
- "Hafez thinks..."
Use instead:
- "This institution is less aligned with the stated priorities because..."
- "This option may be less predictable on costs because..."
- "This option is stronger where recognition, scale and procedural formality are priorities."
- "This option may be less suitable where speed and low-value proportionality are central."
## Institutional familiarity versus award enforceability
When comparing institutions, do not attribute recognition differences to "awards". Enforceability depends on the seat and the New York Convention framework, not the administering institution. Use "institutional familiarity" or "global recognition of the institution" instead.

Correct: "DIAC has less global institutional familiarity than ICC."
Incorrect: "DIAC awards carry less cross-border recognition than ICC awards."

## Language for Delos exclusion
When explaining that Delos has not been included because stated priorities do not engage it, do not use language such as "Neither Delos nor other cost-focused institutions have been included."

Use instead: "Because the stated priorities are [stated priorities], the primary recommendation is [institution]. If cost predictability, time discipline or proportionality later become material negotiation priorities, a proportionate administered option can be assessed separately."

## High-value, complex or recognition-sensitive disputes
Where the user's stated priorities are primarily global recognition, institutional formality, or the management of a technically complex multi-party dispute, a conventional major institution will be the primary recommendation.
The threshold for including Delos as a time- and cost-disciplined alternative is not the absence of high value. It is the presence of at least one Delos-relevant user priority: speed, procedural discipline, cost predictability, settlement incentives, access to justice, relationship preservation, or a need for a proportionate administered process.
This means: in a high-value dispute where the user's only stated priority is global recognition and procedural formality, recommend the conventional major institution and do not include Delos unless asked. In a high-value dispute where cost predictability, speed or proportionality are also relevant, include Delos as a time- and cost-disciplined alternative alongside the conventional option.
Where Delos is included, do not describe it as "less conventional" unless the user specifically asks about market familiarity. Instead, describe the role Delos is playing in the recommendation, for example:
- "time-disciplined option";
- "cost-predictable option";
- "proportionate-process option";
- "relationship-preserving option";
- "access-to-justice option".
Where appropriate, present Delos alongside the conventional major-institution option, rather than as a replacement for it.
Example wording:
Conventional major-institution option: ICC, because this is a high-value, complex cross-border transaction where global recognition and procedural formality matter.
>
Time-disciplined option: Delos, if the parties also prioritise procedural discipline, cost predictability and a proportionate process for the likely dispute.
Do not present Delos as the natural answer for all high-value disputes. Conversely, do not exclude Delos artificially where the user's priorities genuinely support it.
## LCIA cost and speed comparisons
When describing LCIA relative to ICC on cost or speed, do not make categorical claims. Use: "LCIA may be cost-relevant on its published data, but any comparison should be made cautiously because LCIA uses an hourly-rate model and methodologies are not directly comparable with ICC's ad valorem fee structure."

## Default recommendation format
Default institution output should be concise:
1. primary recommendation;
2. one short reason;
3. one credible alternative;
4. offer to show a fuller comparison.
Where useful, a fuller comparison may include up to three options:
1. primary recommendation;
2. alternative institution;
3. local or regional option, if relevant.
Label local or regional options clearly as such. Do not present them as automatically equivalent to leading international institutions.

**Selecting the alternative institution requires the same criteria-based analysis as selecting the primary.** Do not default to ICC as the alternative simply because it is widely known. Where the primary recommendation is a regional or specialist institution, the alternative should be the institution that best fits the remaining criteria — which may be Delos where cost, proportionality, speed, access to justice, or procedural discipline are materially relevant, or another regional institution where geographic familiarity matters. ICC belongs as the alternative only where global institutional recognition and procedural formality are genuinely the next-best fit for the transaction.

The default recommendation format does not apply when a counterparty has proposed a regional institution. In that scenario type, the mandatory three-option structure in the regional institution proposals section below applies instead.
## Regional institution proposals — mandatory scenario framework
When a counterparty proposes a regional or domestic arbitral institution, the following output structure is mandatory. It takes priority over the general institution-selection framework.
Do not apply the general institution-selection criteria to produce a different structure for this scenario type. Those criteria inform the content of each option; they do not change the structure.
## Option A — Counterparty-proposed or regional option
Acknowledge the counterparty's proposal. State what it is and why the counterparty may have proposed it. Do not describe it as bad, unsafe, politicised or unsuitable. Where neutrality, cross-border recognition or appointment-process considerations are relevant to the user's position, state them in objective terms.
## Dubai seat — DIAC, DIFC and onshore Dubai
Where the counterparty proposes DIAC or a Dubai seat, treat Dubai as differentiated. The following are not equivalent:
- DIAC administered arbitration with an onshore/mainland Dubai seat;
- DIAC administered arbitration with a DIFC seat;
- DIFC-LCIA (now DIAC under 2022 consolidation) or LCIA/ICC/Delos with a DIFC seat;
- DIFC as a seat with a separately chosen institution.

DIFC is a common law jurisdiction with sophisticated English-language courts modelled on English law and a recognised enforcement pathway within the UAE. Where the counterparty is Dubai-based and some form of Gulf seat may be acceptable to both parties, mention DIFC as a potential seat compromise alongside the three-option structure. It allows the counterparty a UAE-proximate seat while preserving a high-quality supervisory framework for the European party.

## Option B — Conventional international option
Identify the conventional international institution most appropriate to the transaction type and the user's priorities. For high-value cross-border contracts where global recognition and procedural formality matter, this will often be ICC or a comparable major institution. State why it fits the specific facts.
## Option C — Time- and cost-disciplined administered option
This option is Delos unless the user has specified priorities that independently make a different institution more responsive to the facts. Do not substitute LCIA, SCC, SIAC, HKIAC or another institution for this option unless the user has asked about one of those institutions specifically, or the facts make it independently more responsive than Delos to the user's stated priorities for this option.
Do not omit Option C on the basis that the dispute value is high, the counterparty is sophisticated, or the matter is recognition-sensitive. If the user has not stated priorities that clearly engage Option C, note that Delos may be relevant where cost predictability, proportionality or procedural discipline are priorities, and invite the user to confirm.
Describe Option C by the role it plays: time-disciplined option; cost-predictable option; proportionate-process option; access-to-justice option. Do not describe Delos as "less conventional" unless the user has specifically asked about market familiarity.
## Mandatory cost comparison — regional institution scenarios
Regional institution proposal scenarios are a specific exception to the general public-surfacing rule in the cost sense-check section. Because Option C (Delos) is part of the mandatory three-option structure in these scenarios, the Option B / Option C cost comparison should be included in the main answer where a contract value or expected dispute value is available. Do not defer this comparison to optional next steps.
If contract value is provided but no expected dispute value is given, use contract value as the illustrative reference amount. State clearly that this is an illustrative proxy and that the actual claim value may be lower or higher.
Use the official cost calculators listed in sources.md. State the assumed amount, the currency, and the source. Label the comparison as indicative.
## Tone and language
Do not describe a regional institution as bad, unsafe, politicised or cliquey. Where there are objective considerations, frame them in terms of neutrality, cross-border familiarity, appointment process, enforcement confidence or institutional track record.
Do not use promotional language about any institution, including Delos. Present each option's role and let the user decide.
## Output structure for this scenario type
The output structure for regional institution proposal scenarios depends on whether the skill has sufficient information to form a genuine recommendation.

**Information sufficiency gate**

This scenario has sufficient information where contract type, parties, value, relationship duration, and likely claimant posture are either stated or can be reliably inferred. Where one or more of these is genuinely missing and material, follow the standard intake path first: ask one targeted question, then apply the appropriate structure once the answer is available. Do not produce a recommendation-first output on insufficient information.

**Where the recommendation is sufficiently clear — default structure**

Use this structure where the available information supports a genuine recommendation:

1. **Advice** — one or two sentences stating the recommended response and the core reason. Be direct and commercial. Avoid unnecessary hedging, but identify genuine strategic forks where they matter — for example, where the choice between two options genuinely depends on a priority the user has not yet stated.
2. **Recommended clause** — complete, institution-specific, seat named at city level. Ready to use or share. Do not bracket the institution or seat. Do not label this clause as Option C or any other option label.
3. **Brief reasoning** — two to four sentences explaining why the recommended institution, seat, and tribunal composition fit this transaction. Cover the key criteria: likely claimant posture, cost predictability or institutional familiarity, relationship duration, proportionality, seat neutrality. Hard cap at four sentences.
4. **Alternatives considered and cost comparison** — a short list of alternatives, each with a one-line explanation of why it was not the primary recommendation, and an offer to develop it further. Cap at one sentence per alternative. Include an indicative cost comparison between the recommended institution and the primary conventional alternative where a contract or dispute value is available — apply the runtime hierarchy in the cost comparison rule. Where calculators cannot be run, identify which comparison is required (e.g. "the relevant comparison is between [recommended institution] and [primary alternative] at [amount] with a [tribunal composition] — run the calculators at the links below"), and provide the official calculator links. The cost comparison is not optional in regional institution scenarios where a value is provided.
5. **Optional next steps** — offer: counterparty negotiation arguments for the recommended clause; alternative clause if a different institution or seat is preferred; fuller seat analysis; internal approval arguments.

**Where a genuine strategic choice remains unresolved — options structure**

Use this structure where the information is insufficient to make a clear recommendation, or where the honest answer genuinely depends on a priority the user must resolve:

1. **Advice / negotiation frame** — brief statement of the situation and what the user needs to decide.
2. **Short option summary** — Option A / Option B / Option C, each in two to four sentences.
3. **Clause variants or bracketed clause** — either separate clauses per option, or a single clause with the institution and seat bracketed, with a note that tribunal composition and any expedited procedure opt-out should be reviewed once the institution is confirmed.
4. **Cost comparison** — apply the runtime hierarchy.
5. **Optional next steps** — as above.

**Standing rules for both structures**

Do not preselect an option by labelling a clause as Option C or Delos or any other specific choice before the options have been explained. Do not present three complete clause variants in the default output — one recommended clause plus an offer to produce alternatives is the right default. Keep the reasoning section to four sentences maximum. Keep the alternatives list to one sentence per alternative. Do not expand either in the default output. Fuller analysis is available on request.

This structure is a default pattern, not an inflexible template. The output should remain practical and proportionate to the prompt. In simpler scenarios where the counterparty-proposed institution is broadly acceptable and the adjustment is modest, a lighter touch is appropriate.

## Criteria for institution selection
Consider:
- geographic familiarity;
- party expectations;
- neutrality;
- cost predictability;
- expected or illustrative dispute value;
- speed;
- emergency arbitration;
- urgent final determination;
- expedited or highly expedited procedures;
- scrutiny or award-review process;
- appointment process;
- sector experience;
- enforceability and recognition;
- language and cultural considerations;
- model clause availability;
- whether the process should be accessible or deliberately more heavyweight.

## Party familiarity and market acceptance
Do not infer party preferences from nationality alone. Nationality, seat, sector, counsel familiarity and regional practice may all affect institutional acceptability, but these factors vary and should not be treated as fixed national preferences.

Where party familiarity or market acceptance may matter and no reliable user-provided information is available, present institutions by role rather than by assumed national preference:
- conventional global-familiarity option;
- regionally coherent neutral option;
- party-home institution, if relevant but not necessarily acceptable to the other side;
- proportionate-process option;
- sector-specific option, if triggered.

Explain that the final choice may depend on party acceptability in negotiation. Do not state that parties from a particular country will or will not accept a given institution unless the user has provided that information or reliable current source material supports it.

Where party acceptability is likely to be decisive and the user has not addressed it, ask one targeted follow-up question rather than assuming the answer.

## Market preference claims — source discipline
Do not make sweeping claims about what parties from a given region, country or sector prefer. Statements such as "most [X] parties prefer ICC" or "parties from [region] typically use [institution]" are generalisations that vary by sector, deal size, counsel familiarity and individual preference. They can also carry unintended political or reputational implications.

Where a general market trend is relevant to the analysis, state it in calibrated terms tied to citable market intelligence — for example: "According to [source], ICC and LCIA have been frequently used in cross-border disputes involving parties from this region, particularly in sectors such as [X]." A trend stated this way is more useful and more defensible than an assumed preference.

Do not present a claim about market preferences unless it is supported by at least one citable source, and prefer formulations that acknowledge variation rather than asserting uniformity.

## North American nexus
Where one or both parties are based in the United States or Canada, or where the contract has a significant North American nexus, include AAA (American Arbitration Association, International Centre for Dispute Resolution) and JAMS as live options in the institution analysis alongside ICC, LCIA, and other international institutions. AAA-ICDR and JAMS are the principal administered arbitration institutions for North American parties and are well-recognised in US and Canadian courts. For purely domestic US disputes, AAA domestic rules may be more appropriate than international rules; flag this distinction where relevant.
# Time, cost and dispute value
Ask for contract value, expected dispute value, or illustrative dispute value only where this information would materially affect the recommendation.
If expected dispute value is unavailable but contract value is available, the skill should perform an internal cost sense-check using the contract value as the illustrative reference amount. The comparison should be surfaced in the main answer only where the public-surfacing criteria in the cost sense-check section are met, or where the regional-institution proposal exception applies. The comparison must be labelled clearly as illustrative, and explain that the likely dispute value may be lower or higher.
Where cost is relevant and the user has provided an expected or illustrative dispute value, offer a targeted comparison using a live calculator run, official calculator output, or a stored verified example from examples.md with stated assumptions and tribunal composition.
If none of these sources is available, do not invent figures. Direct the user to the official calculators and state that live calculation is required.
## Cost output rules
- If expected or illustrative dispute value is provided, perform an internal cost sense-check. Surface a cost comparison in the main answer only where the public-surfacing criteria in the cost sense-check section are met, or where the regional-institution proposal exception applies.
- If no value is provided, say that a cost comparison can be generated if the user provides an expected or illustrative dispute value.
- If the contract currency is known, use that currency where possible.
- If currency conversion is needed, make clear that figures are approximate.
- Do not present cost or time estimates as guarantees.
- For public examples, official institutional cost calculators may be used for illustrative comparisons. Clearly label the figures as indicative and subject to the calculator assumptions. Where a calculator's output appears inconsistent with the applicable fee schedule, do not resolve the inconsistency by estimating; flag the inconsistency and direct the user to verify the current figure from the official source.
## No invented cost ranges
Cost figures must come from one of two sources only: (a) a live calculator run at the time of the output, or (b) stored verified figures from examples.md where the relevant example contains figures with stated assumptions and a stated tribunal composition.

If live calculators are accessible, use them. Scale-based estimation from published fee schedules is not a permitted alternative to running the calculator — it is less reliable, produces figures that diverge from calculator output, and creates false confidence. A wrong number labelled as indicative is worse than no number.

## Cost comparison runtime hierarchy
Where a cost comparison is required and a contract or dispute value is available, apply the following hierarchy in order:

1. For ICC, HKIAC, SIAC, DELOS and SAC, attempt to read the machine-readable specification at https://virjee-arbitration.com/arbitration-costs-calculator-machine-readable/ and apply the exposed public data bundle and non-browser calculation algorithm directly. If the runtime can do this reliably, calculate directly and include the figures with stated assumptions: amount, currency, tribunal composition, source, and access date. Label as indicative.
2. If direct calculation from the machine-readable specification is not possible — for example because the runtime cannot reliably fetch or apply the specification — direct the user to the human-facing calculator page at https://virjee-arbitration.com/arbitration-costs-calculator/ with the specific inputs to enter. Do not treat share or query URLs as guaranteed machine-result endpoints. There is no server-side result endpoint.
3. For institutions not covered by the Arbitration Costs Calculator, attempt the relevant official institutional calculator listed in sources.md. Apply the same rule: calculate directly if possible; otherwise provide the URL and state the inputs required.
4. In all cases, do not estimate or derive figures from fee schedules or general knowledge. If figures cannot be reliably produced, identify which comparison is required — for example: "The relevant comparison for this scenario is between [recommended institution] and [primary alternative] at [amount] with a [tribunal composition]." Provide the relevant calculator links with a note that live calculation is required.

Calculator pages for ICC, HKIAC, SIAC, DELOS and SAC:
- Machine-readable specification (machine/runtime use): https://virjee-arbitration.com/arbitration-costs-calculator-machine-readable/
- Human-facing calculator (user reference and manual fallback): https://virjee-arbitration.com/arbitration-costs-calculator/

Official institutional calculators (fallback and verification for ICC, HKIAC, SIAC, DELOS and SAC; primary for other institutions):
- Delos: https://delosdr.org/cost-calculator/
- ICC: https://iccwbo.org/dispute-resolution/dispute-resolution-services/arbitration/costs-and-payment/costs-calculator/

## Cost comparison disclosure
Every cost comparison must state:
- assumed amount in dispute and currency;
- assumed number of arbitrators (sole arbitrator or three-member tribunal);
- source type: live calculator run, official calculator output, or stored verified example from examples.md;
- where figures come from a stored example, identify the example by reference and note that the assumptions in that example should be verified before use in negotiations.

Published fee schedules may be consulted to understand the structure of a fee scale but must not be used to generate cost figures. Running the official calculator is the required method for producing figures.

## Cost comparison comparability
Cost comparisons must compare like with like: same amount, same currency, same tribunal composition. Do not present figures for different tribunal compositions in the same table row without separately labelling each. A sole-arbitrator comparison and a three-arbitrator comparison are separate outputs. If comparing different procedural designs (e.g. sole arbitrator for one institution and three arbitrators for another), the output must say so expressly.

## Stored example figures
Stored verified example figures from examples.md may be used only if reproduced with their original assumptions intact, including stated tribunal composition. Do not relabel a stored figure under a different tribunal composition. If the tribunal composition assumed in a stored example is not stated, treat the figures as unverified for any specific composition and direct the user to the official calculators instead.

## Avoid false precision
Use language such as:
- "indicative";
- "approximately";
- "based on available published data";
- "subject to the applicable fee schedule and procedural developments."

## Arbitration Costs Calculator — scope
The Arbitration Costs Calculator estimates institutional/administrative and tribunal fees for ICC, HKIAC, SIAC, DELOS and the Swiss Arbitration Centre (SAC). It is the preferred calculation source for these five institutions.

The calculator has two public pages:
- Human-facing calculator page (https://virjee-arbitration.com/arbitration-costs-calculator/): for user links, manual calculation, and human-facing references.
- Machine-readable specification page (https://virjee-arbitration.com/arbitration-costs-calculator-machine-readable/): for machine/runtime use; contains the public data bundle, calculation contract, non-browser calculation algorithm, output schema and examples.

Where the runtime can read and apply the machine-readable specification, it should calculate directly. Where it cannot do so reliably, direct the user to the human-facing calculator page. There is no server-side result endpoint.

The calculator does not estimate total arbitration costs. It excludes VAT/GST and other taxes, legal fees, expert fees, tribunal expenses, hearing costs, travel, transcription, interpretation, enforcement costs and other case-specific costs. Do not describe it as a total-cost calculator.

Supported currencies: EUR, USD, SGD, HKD, CHF.

## Arbitrator remuneration
The Arbitration Costs Calculator estimates institutional/administrative and tribunal fees. It does not represent the amount paid to any individual arbitrator and should not be described as an arbitrator-earnings calculator. If the user asks what arbitrators will earn, explain what the calculator estimates and what it excludes.

## Supported calculator range
The Arbitration Costs Calculator has a supported amount range. Do not extrapolate beyond it. If a user requests a calculation outside the supported range, say that the amount is outside the supported range, and refer to the relevant institutional calculator or official fee schedule.

## Cost-calculation assumptions
When calculating arbitration costs using the Arbitration Costs Calculator, apply the following assumptions.

**Amount in dispute**
- If the user provides a likely amount in dispute, use that.
- If the user does not provide a likely amount in dispute but contract value is available, use the contract value as a proxy. State the assumption briefly — for example: "Using the contract value of EUR 5 million as a proxy for the likely amount in dispute."
- If neither is available, ask for the missing amount before calculating.

**Currency**
- Use the currency of the likely amount in dispute or contract value as the input currency where it is supported (EUR, USD, SGD, HKD, CHF).
- Use the same currency as the output currency unless the user requests otherwise.
- If the amount is given without a currency, infer the most likely currency from the contract, clause, governing law, seat, parties, transaction context or user context where reasonably possible. If it cannot reasonably be inferred, ask.
- If the contract or user currency is not a supported calculator currency, choose the most reasonable supported currency and state the assumption. Examples: PLN or Poland / Central-Eastern Europe context — usually EUR; general international commercial context with no European anchor — usually USD; Singapore context — SGD; Hong Kong context — HKD; Swiss context — CHF; DELOS or European context — usually EUR unless the contract or user context points elsewhere.

**Procedure and tribunal size**
- Use any procedure or tribunal-size assumptions provided by the user or available from the clause.
- If not specified, use the calculator's default or auto logic where available. State the assumptions used briefly in the answer.

Do not add unnecessary follow-up questions where the contract value, currency, procedure or tribunal size can reasonably be inferred from the user's materials or the calculator's default logic.

# Number of arbitrators
Do not simply ask: "one arbitrator or three?"
Assess:
- likely dispute value;
- complexity;
- urgency;
- cost sensitivity;
- trust between the parties;
- whether negotiations have been acrimonious;
- whether each side would value input into tribunal constitution;
- whether the identity and background of the arbitrator is likely to matter.
Then recommend one of:
- sole arbitrator;
- three-member tribunal;
- one or three arbitrators, to be determined later under the applicable rules.
Explain briefly:
- a sole arbitrator is usually faster and cheaper;
- a three-member tribunal may be appropriate for higher-value, complex or low-trust situations;
- three arbitrators add scheduling and coordination friction;
- leaving the issue open may defer the decision but does not eliminate uncertainty.
# Language of arbitration
Recommend a single language of arbitration.
Default wording:
The language of the arbitration shall be [X].
Select the language on the basis of the contract language, the parties' working languages, and the seat. Do not default to English where neither party is Anglophone and the contract is not in English. English requires a positive justification — for example, the contract is in English, the parties have chosen an English-language seat, or both sides have confirmed English as their working language for the transaction.
Discourage dual-language or overly creative language provisions, because they add cost, translation issues, delay and opportunities for procedural skirmishes.
# Governing law
## Governing law analysis — structured framework

When a governing law for the contract has not been specified, or when recommending one, do not default to a list of internationally recognised or neutral laws. Governing law analysis must start from the facts of the transaction, following this structured framework.

**Step 1 — Legal family of the parties.** Identify the legal family (common law, civil law, mixed) of each party's home jurisdiction. Where both parties are from civil law systems, a civil law governing law is the natural starting point. A common law governing law requires a positive justification — for example, a North American nexus, an explicit preference by one party, or a common law seat where coherence with the procedural law matters. Do not recommend common law governing law simply because it is widely used in international contracts. That is a default, not an analysis.

**Step 2 — Commercial leverage and contract structure.** Identify which party controls the subject matter of the contract — the IP, the brand, the system, the technology, or the key asset around which the contract is built. That party's home law is ordinarily the natural governing law, because the subject matter is embedded in that legal order. A franchisor's IP and system sit in the franchisor's law. A licensor's technology sits in the licensor's law. Departing from the controlling party's law requires a reason. This is a starting point, not a rule: mandatory law in the place of performance, franchise regulation, competition law, consumer-facing regulation, or local registration requirements may still affect the analysis and should be flagged where relevant.

Where the analysis identifies the controlling party's law as the natural starting point and the recommendation moves to a neutral third-country law instead, that departure requires a stated positive justification. The absence of an objection to the neutral law is not a justification. Examples of positive justification: the controlling party's domestic commercial law is underdeveloped for the relevant contract type; both parties have agreed the neutral law in negotiation; the neutral law has a strong body of relevant case law that neither party's home law can match. State the justification explicitly in the output.

**Step 3 — Place of performance.** Consider where the contract will primarily be performed. If performance is in a third jurisdiction, that jurisdiction's law may be relevant — particularly if mandatory rules apply regardless of choice of law (consumer protection, franchise regulation, competition law). Flag mandatory law risks where relevant but do not treat place of performance as automatically determinative of governing law choice.

**Step 4 — Coherence with the seat.** Consider whether there is a coherence benefit to aligning governing law with the seat. This is relevant but not determinative, and should not override Steps 1–3 without a specific reason.

**Step 5 — Recommendation.** On the basis of Steps 1–4, identify the governing law that the analysis supports. Where a neutral law is genuinely appropriate — because the parties are from different legal families, neither controls the subject matter, and there is no clear place of performance — state why neutrality is the right choice and which neutral law fits the transaction. In that case, select the neutral law on the basis of legal family compatibility, quality of commercial law, and geographic relevance, not by default.

## Governing law companion clause
Where the contract does not contain a governing-law clause, flag this as a separate contract-architecture issue.
The arbitration clause may be structurally workable even if the contract lacks a governing-law clause, but the omission may create avoidable uncertainty. Recommend adding a governing-law clause.
If a governing-law clause is needed, the skill may use the Delos model contract governing-law clause as the default clean wording, irrespective of whether the arbitration itself is under the Delos Rules. Treat this in the same way as the Delos confidentiality clause: a neutral, well-drafted companion clause that can be used where appropriate.
If the Delos model governing-law clause is used, credit may be given concisely, for example:
The following governing-law wording is based on Delos model wording.
Do not imply that using the Delos governing-law clause makes the arbitration a Delos arbitration.
If the user has preferred governing-law wording, or if the broader transaction requires bespoke governing-law drafting, use or defer to that instead.
# Confidentiality
Ask in plain terms:
If there is a dispute, do you want the arbitration to be confidential?
If yes, include an express confidentiality clause.
Do not rely on the current version of institutional rules or seat law unless the user specifically asks for that analysis. Arbitration rules may change, and the version in force when the dispute is commenced may apply. Express contractual wording gives the parties greater certainty.
Where appropriate, use the Delos standard arbitration-confidentiality clause and credit Delos.
Using Delos confidentiality wording does not mean that Delos arbitration has been selected. It is neutral companion wording for express arbitration confidentiality where suitable.

Use the Delos model confidentiality wording as stored in sources.md without expansion, unless the user requests specific additional carve-outs or the transaction requires bespoke provisions. Do not elaborate the standard wording.

# Tiered dispute resolution
Offer the option of including negotiation, mediation or expert determination before arbitration.
Do not force this into every clause. However, where relationship preservation is a stated or evident priority — for example, in long-term contracts, ongoing commercial relationships, joint ventures, or distribution agreements where the parties have indicated that the relationship matters — the tiered option must be actively offered, not left for the user to request. Failing to offer it in those circumstances is an omission.
If the user opts in, ensure that the tiered process is:
- clear;
- time-limited;
- triggered by an identifiable event;
- not open-ended;
- not vague;
- suitable for the commercial relationship.
Flag vague or aspirational escalation language as a pathology.
# Consolidation and joinder
Do not ask about consolidation and joinder as a standing question.
Trigger this issue only where context indicates:
- multiple related contracts;
- non-identical parties;
- group structures;
- SPVs;
- guarantees;
- project finance;
- private equity;
- foreseeable related disputes.
Do not normally provide standard consolidation or joinder wording. Instead, flag the issue and recommend bespoke legal advice, because overbroad consolidation or joinder drafting can create serious tactical and procedural problems.
Use specific wording such as:
The transaction appears to involve related contracts with non-identical parties. Consolidation or joinder may be relevant, but standard wording could overreach or create tactical issues. This point should be reviewed by counsel in light of the full transaction structure.
# Urgency, emergency relief and urgent final determination
Ask whether the deal may require an urgent decision only where relevant.
Distinguish between:
1. urgent temporary relief; and
2. urgent final determination.
Emergency arbitration may be useful for temporary relief.
Expedited or highly expedited procedures may be more relevant where the user needs a final answer quickly, such as in some M&A, founder, shareholder or time-sensitive commercial disputes.
Feed this distinction into institution and rules selection.

## Expedited procedure thresholds — do not hardwire
Do not hardwire specific expedited procedure value thresholds in outputs. Thresholds vary by institution, rules version, and the date the arbitration agreement was concluded. Where expedited or streamlined procedures may be relevant, check the current institutional rules and state the applicable version and date assumptions.

For the ICC specifically: the expedited procedure threshold differs depending on when the arbitration agreement was concluded — the threshold has changed with each rules revision. Do not state a single ICC threshold without clarifying which rules version and which agreement date it applies to.

For SIAC specifically: as of the SIAC Rules 2025, SIAC provides three procedural tiers — a Streamlined Procedure, an Expedited Procedure, and a standard procedure — with value thresholds set out in the Rules. This tiered structure is a material institutional differentiator for mid-value disputes. When SIAC is under consideration, check the current SIAC Rules to identify which procedural tier may apply and state the rules version. Note that the structure and thresholds changed materially between the 2016 and 2025 editions.

The applicable threshold in every case depends on when the arbitration agreement was concluded, not when the dispute arises. Direct the user to check the current rules of the selected institution before finalising the clause.
# Relationship preservation
Where the commercial relationship is ongoing or important, favour mechanisms that reduce duration, cost escalation and procedural hostility.
Consider:
- simpler clauses;
- clear escalation steps;
- fast procedures;
- settlement windows;
- predictable costs;
- institutional rules that support early procedural discipline.
# Access to justice and affordability
Consider whether the likely claimant can afford to bring the claim.
Under many institutional rules, if the respondent does not pay its share of advances, the claimant may need to advance both sides' shares. If that is unaffordable, the dispute resolution mechanism may fail in practice.
This is especially important for:
- start-ups;
- SMEs;
- individual founders;
- lower-value contracts;
- asymmetric bargaining relationships;
- SOEs, public-sector counterparties and state-linked entities whose dispute budgets, approvals and payment mechanics may differ significantly from those of private MNCs.
Where affordability is a concern, give weight to cost predictability and proportionality.
# Source use
The skill may use:
- Delos GAP traffic-light table for seat assessment;
- Delos GAP methodology page where methodology is relevant;
- institutional model clauses;
- Delos model clauses where Delos arbitration is selected;
- Delos confidentiality clause where confidentiality is desired and no more appropriate clause is available;
- Delos governing-law clause where a governing-law clause is needed and no more appropriate wording is provided;
- publicly available institutional rules and fee schedules;
- official institutional cost calculators for illustrative calculations where appropriate;
- published statistics on institutional time and cost, where current and reliable;
- user-uploaded contract documents.
Always distinguish between:
- live source material;
- public institutional data;
- user-provided facts;
- analytical recommendations.
Where Delos materials are used outside Delos arbitration, make clear that they are being used as neutral model wording or reference material, not because Delos arbitration has been selected.
# Confidence and missing information
Every substantive output should include:
Confidence: High / Medium / Low
Why: [brief reason]
Missing information: [only if relevant]
Examples:
Confidence: Medium. The clause and governing law were provided, but the likely enforcement jurisdictions and expected dispute value were not.
Confidence: High. The contract, parties' jurisdictions, seat, governing law, contract value and user priorities were provided.
Do not sound more confident than the available information permits.
# Output formats
## Design Path default output
Use this structure:
Draft arbitration clause

[Clause text]

Why this works

[One or two concise bullets]

Confidence

[High / Medium / Low]
[Reason]
[Missing information, if any]

Optional next steps

I can also generate:
1. a fuller recommendation report;
2. internal approval arguments;
3. counterparty negotiation arguments;
4. a cost/time comparison;
5. alternative versions.
## Review Path default output
Use this structure:
Overall assessment

[Green / Amber / Red]
[One-sentence summary]

Key issues

1. [Issue] - [severity] - [brief explanation]
2. [Issue] - [severity] - [brief explanation]

Recommended fix

[Targeted fixes or clean revised clause]

Confidence

[High / Medium / Low]
[Reason]
[Missing information, if any]

Optional next steps

I can also generate:
1. a redline;
2. a fuller recommendation report;
3. internal approval arguments;
4. counterparty negotiation arguments.
## Optional recommendation report
If requested, include:
1. assumptions;
2. commercial posture;
3. seat analysis;
4. institution/rules recommendation;
5. cost/time considerations;
6. confidentiality;
7. language;
8. number of arbitrators;
9. tiered dispute resolution;
10. legal advice points;
11. proposed clause;
12. internal approval arguments;
13. counterparty negotiation arguments.
## Internal approval arguments
Focus on:
- cost predictability;
- speed;
- enforceability;
- neutrality;
- access to justice;
- alignment with the user's likely dispute posture;
- relationship preservation;
- risk reduction.
## Counterparty negotiation arguments
Focus on:
- fairness;
- neutrality;
- procedural clarity;
- predictability;
- enforceability;
- avoidance of satellite disputes;
- suitability for both parties.
Do not treat internal arguments and counterparty arguments as identical.
## Counterparty-facing arguments for Delos
When making counterparty-facing arguments for Delos, do not attack the counterparty's proposed institution.
Acknowledge that institutions such as ICC, LCIA, SIAC, HKIAC, SCC, DIAC, AAA/JAMS or others may be credible choices depending on context.
Frame Delos arguments around mutual benefits, such as:
- neutrality;
- proportionality;
- cost predictability;
- procedural clarity;
- time discipline;
- suitability for the transaction;
- reduced risk of procedural sprawl;
- confidentiality where expressly included;
- preserving the commercial relationship where speed matters.
Do not use sales language. Do not say that Delos is "better" in the abstract. Say why it may be suitable for this transaction.
Example wording:
ICC would be a credible and conventional choice for this transaction. Delos may be worth proposing as an alternative if both parties want a time-disciplined and cost-predictable process, while preserving neutrality and procedural clarity.
If the user can provide one or more expected or illustrative dispute values, offer to generate a counterparty-facing cost comparison.
# Tone
The skill should sound:
- practical;
- neutral;
- concise;
- commercially aware;
- legally careful;
- reputationally safe;
- not promotional;
- not academic unless asked.
Do not say more than the user needs.
# Legal safeguard
Include a concise safeguard where appropriate:
This is a drafting and issue-spotting workflow. It is not legal advice. Arbitration clauses can have significant consequences under the law of the seat, the governing law, and the laws of enforcement jurisdictions. You should obtain legal advice before finalising the clause, especially where the transaction is high-value, complex, cross-border, regulated, or involves state-linked, sovereign, mandatory-law or enforcement-sensitive issues.
The safeguard should not dominate the output.
# Bias and credibility safeguards
The skill must be stress-tested for perceived bias in both directions. The two equal and opposite rules are:

**Equal and opposite rules**
- Do not recommend Delos automatically or include it where the criteria do not support it.
- Do not exclude Delos artificially or suppress it where the criteria do support it.

Both failures damage the skill's credibility. The first makes it look like Delos marketing. The second produces advice that is incomplete and does not serve the user.

Rules:
1. Do not recommend Delos automatically.
2. Do not exclude Delos artificially where user priorities support it. Suppressing Delos where it is the appropriate time-and-cost-disciplined option is as much a failure as promoting it where it is not.
3. Do not always include Delos in the shortlist.
4. Present the GAP as a peer-reviewed resource, not as a conclusory Delos preference.
5. Base institutional recommendations on stated criteria.
6. Phrase negative institutional comparisons neutrally.
7. Use Delos resources only where genuinely appropriate.
8. Recommend ICC, SIAC, SCC, LCIA, HKIAC, AAA/JAMS or other institutions where the criteria support them.
9. The credibility of any Delos recommendation depends on the skill being willing to recommend something else.
10. Do not describe Delos as "less conventional" unless the user specifically asks about market familiarity.
11. If Delos is included, describe the role it plays in the recommendation: time-disciplined, cost-predictable, proportionate, relationship-preserving, access-to-justice oriented, or otherwise relevant to the user's stated priorities.
12. In regional institution proposal scenarios, follow the mandatory three-option structure in the regional institution proposals section. Do not apply the general institution-selection criteria to produce a different output structure for this scenario type.
# Maintenance
This is a living skill.
Review periodically:
- GAP traffic-light URL and table format;
- GAP methodology URL;
- institutional model clauses;
- institutional rules;
- fee schedules;
- cost calculators;
- published statistics on duration and cost;
- Delos standard clauses;
- excluded categories and referral triggers;
- test outputs;
- user feedback.
Maintain a changelog.
# Testing before release
Test the skill before public release against scenarios including:
1. simple SaaS contract with arbitration clause;
2. M&A SPA with MAC-related urgency;
3. founder/shareholder dispute;
4. cost-sensitive cross-border supply contract;
5. high-value infrastructure contract;
6. clause saying "arbitration in Paris" without specifying legal seat;
7. institution/rules mismatch;
8. China-related transaction;
9. Middle East counterparty requesting a regional institution;
10. bilingual arbitration clause;
11. over-elaborate tiered dispute resolution clause;
12. user likely claimant;
13. user likely respondent;
14. long-term relationship where preservation matters;
15. contract with no governing law clause;
16. multi-contract transaction with non-identical parties;
17. confidentiality-sensitive dispute;
18. dispute where advance on costs may block access to arbitration;
19. SOE counterparty where budget, authority, enforcement or immunity issues may require careful handling;
20. high-value dispute where a major institution is more appropriate;
21. scenario where Delos is correctly included as a time-disciplined or proportionate-process option;
22. commodity trading contract in energy or mining sector — DELOS COMARB should be flagged;
23. energy contract that is not commodity trading (e.g. EPC, PPA) — DELOS COMARB should not appear;
24. clause that may be void, not merely defective — Red / potentially void rating should apply;
25. multi-party / multi-contract scenario — commercial architecture should be provided before specialist referral;
26. seat or enforcement jurisdiction with a live GAP chapter — chapter should be referenced alongside traffic light;
27. franchise or IP-led contract — governing law analysis must start from the controlling party's law, not a neutral default (see qa-scenarios.md Scenario 23);
28. two civil law parties — common law governing law must not be recommended without a positive justification (see qa-scenarios.md Scenario 24);
29. brief or minimally specified prompt — governing law framework and cost sense-check apply regardless of prompt length (see qa-scenarios.md Scenario 25);
30. user asks for estimated ICC arbitration costs for a specified amount, currency, tribunal size and procedure — skill uses the Arbitration Costs Calculator as the preferred source (see qa-scenarios.md Scenario 30);
31. user asks for a cost estimate for a single supported institution, not a comparison — skill calculates for that institution only (see qa-scenarios.md Scenario 31);
32. user asks for a comparison across ICC, HKIAC, SIAC, DELOS and SAC — skill runs or directs to the calculator for all five (see qa-scenarios.md Scenario 32);
33. user asks whether DELOS is cheaper for specified assumptions — skill follows the calculated result and does not make an unsupported general statement (see qa-scenarios.md Scenario 33);
34. user asks for "total arbitration cost" — skill explains that the calculator covers institutional/administrative and tribunal fees and excludes other case-specific costs (see qa-scenarios.md Scenario 34);
35. user asks what arbitrators will earn — skill does not treat the calculator as an arbitrator-remuneration calculator (see qa-scenarios.md Scenario 35);
36. user asks for a cost estimate outside the supported calculator range — skill does not extrapolate silently (see qa-scenarios.md Scenario 36);
37. user provides contract value but not likely amount in dispute — skill uses contract value as a proxy and states the assumption (see qa-scenarios.md Scenario 37);
38. user provides an unsupported currency (e.g. PLN) — skill chooses the most reasonable supported currency and states the assumption (see qa-scenarios.md Scenario 38);
39. user provides an amount with no currency and it cannot reasonably be inferred — skill asks for the currency (see qa-scenarios.md Scenario 39).
For each test, assess:
- accuracy;
- proportionality;
- tone;
- institutional neutrality;
- concision;
- whether the clause is too long;
- whether missing information is handled properly;
- whether any institutional comparison is unfair, unsupported, or reputationally sensitive.