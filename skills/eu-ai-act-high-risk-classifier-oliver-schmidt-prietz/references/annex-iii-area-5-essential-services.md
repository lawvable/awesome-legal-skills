# Annex III Area 5 — Essential private and public services and benefits

**Annex III citation:** Nr. 5
**Effective date:** 2 December 2027 (per AI Omnibus)
**Source:** Commission Guidelines Annex III, Area 5 section. Full text: the Commission Draft Guidelines on Art. 6 classification (2026), Annex III section.

## Scope of the area

Point 5 of Annex III bundles four distinct service domains in which AI use can profoundly affect a natural person's ability to participate in society or maintain their standard of living: (a) public assistance benefits and services administered by — or on behalf of — public authorities, including healthcare; (b) creditworthiness evaluation and credit scoring for natural persons; (c) risk assessment and pricing for life and health insurance; and (d) emergency call evaluation, dispatch of emergency first response services, and emergency healthcare patient triage (Commission Guidelines ¶279–¶280). All four sub-categories concern natural persons only — purely B2B and corporate-applicant use cases are out of scope (e.g. ¶288, ¶305 carve-out for legal persons).

The legislator's rationale (Recital 58 AI Act) is that biased, inaccurate or discriminatory AI in these areas can deny people access to essential services, financial inclusion or life-saving emergency response. The rights at stake include the right to social security and social assistance, the right to healthcare, the right to non-discrimination, and the right to an effective remedy (¶279, ¶282, ¶294, ¶310, ¶329). "Essential services" is interpreted by reference to Recital 58: services and benefits "necessary for people to fully participate in society or to improve their standard of living" (¶281, ¶301).

Two structural limits keep the area focused. First, **5(a) is restricted to public authorities or those acting "on their behalf"** (¶285–¶287) — purely private charitable aid is outside. Second, **5(b) excludes AI used for the purpose of detecting financial fraud** (¶306–¶309); but the carve-out applies only where fraud detection is the *main* intended use, and AML/CFT systems are not covered by the fraud carve-out (¶309). **5(c) is restricted to life and health insurance** (and credit life insurance, private long-term care insurance, personal pension products in so far as they materially impact old-age livelihood) — motor, property, liability and investment-product insurance are out (¶314, ¶316–¶318). **5(d) applies to emergency response and emergency triage**, not routine clinical decision-support or appointment scheduling (¶329–¶335).

## Sub-categories

- **Nr. 5(a) Public benefits eligibility** — AI systems intended to be used by public authorities (or on their behalf) to evaluate the eligibility of natural persons for essential public assistance benefits and services (including healthcare), and to grant, reduce, revoke or reclaim such benefits (¶282–¶293).
- **Nr. 5(b) Creditworthiness / credit scoring** — AI systems intended to be used to evaluate the creditworthiness of natural persons or establish their credit score; exception for AI used for the purpose of detecting financial fraud (¶294–¶309).
- **Nr. 5(c) Insurance risk assessment and pricing** — AI systems intended to be used for risk assessment and pricing in relation to natural persons in the case of life and health insurance only (¶310–¶321).
- **Nr. 5(d) Emergency call evaluation/dispatch and emergency healthcare triage** — AI systems evaluating/classifying emergency calls, dispatching or prioritising emergency first response services (police, firefighters, medical aid), and emergency healthcare patient triage systems (¶329–¶336).

## Practical examples — HIGH-RISK

**5(a) Public benefits eligibility**
- Unemployment-benefit eligibility recommender analysing whether an applicant qualifies, for what period and what amount, and making a recommendation to a case handler (¶a-examples after ¶293).
- Social-benefits eligibility system that processes application data and cross-references external databases and then generates an eligibility decision (¶a-examples).
- Social-housing prioritisation system evaluating profiles for eligibility, urgency and prioritisation based on income, household size, age, employment status, location (¶a-examples).
- Home-care prioritisation system distributing limited in-home care hours among eligible elderly or dependent persons (¶a-examples).
- Application-flagging system that detects irregularities or fraud indicators in sickness-benefit applications and flags them for further investigation, materially influencing access to benefits (¶a-examples).
- Chatbot personalised to a specific eligibility assessment that answers a case handler's legal questions about whether to grant or refuse care benefits (¶a-examples — contrast with the factual-information chatbot under Art. 6(3)).
- Healthcare preventive-screening invitation system that also performs an eligibility evaluation for the screening (mammogram invitations based on segmentation + eligibility) (¶a-examples).

**5(b) Creditworthiness / credit scoring**
- Numerical credit-scoring system based on payment behaviour and income used to support a consumer-credit or mortgage decision (¶a-examples after ¶309).
- Credit-bureau scoring system whose scores are shared with third parties for downstream decisions on loans, mortgages, housing, healthcare or telecommunication services — deployer need not equal the decision-maker (¶a-examples).
- Public financial-service creditworthiness systems for subsidised loans, first-time-buyer support, student support, social microcredit (¶303 — these public financial services are "essential private services" within 5(b)).
- Integrated creditworthiness-plus-pricing system that combines the two functionalities in one integrated process (¶300).

**5(c) Insurance risk assessment and pricing**
- Life-insurance application reviewer processing age, health status, family history, lifestyle and occupation against mortality tables to decide whether to accept and on what terms (¶a-examples after ¶321).
- Health-insurance premium calculator predicting expected annual medical cost for a risk group and adding administration and profit margin (¶a-examples).
- Credit-life-insurance risk system (payment-protection insurance tied to mortgages or large credit lines) — still high-risk under 5(c), even if the underlying assessment looks like a credit-score (¶318).
- Private long-term-care insurance risk-assessment system (¶317).
- Health-insurance pricing system run by a public-law insurer — public-law status of the insurer does not exempt the system (¶319).

**5(d) Emergency calls and triage**
- 112 emergency-call NLP classifier that assigns urgency and routes responders (¶a-examples after ¶336).
- Police emergency-call urgency/seriousness analyser extracting keywords to prioritise interventions (¶a-examples).
- Real-time decision-support assistant for emergency call-takers, listening for life-threatening signals and comparing to historical call data (¶a-examples).
- Queue-triage AI that identifies waiting emergency calls as life-threatening and alerts the human call-taker to prioritise (¶a-examples).
- Emergency-department patient-prioritisation AI (without performing clinical/diagnostic acts) (¶a-examples).
- Hospital chatbot triggering emergency medical services (no clinical/diagnostic function) (¶a-examples).
- Wildfire resource-allocation AI that triggers dispatching of emergency first response services and pre-positions assets (¶a-examples).
- Mental-health crisis triage chatbot using NLP to assess severity/urgency of chat-based emergency contact (¶a-examples).

## Practical examples — NOT HIGH-RISK

- **5(a) — Proactive identification without eligibility check**: AI identifying persons in need of preventive care, where outputs are not used to prioritise, exclude or otherwise influence access (¶b-examples after ¶293).
- **5(a) — Anonymised matching to support services**: AI matching natural persons to public support services based on needs, using anonymised data, pre-filling applications, without evaluating eligibility (¶b-examples).
- **5(a) — Case-handler allocation**: AI merely informing which body or person should further assess an application — no eligibility evaluation (¶b-examples).
- **5(a) — Corporate applicants**: AI assessing reimbursement claims from companies, not from natural persons (¶b-examples; cf. ¶288).
- **5(b) — Fraud detection**: AI for detecting misused, forged or altered identification or financial documents (ID cards, driver's licences, income statements, bank statements) where fraud detection is the main intended use (¶306–¶308).
- **5(b) — Customer classification, marketing, segmentation, pricing simulations** that do not feed creditworthiness assessment (¶b-examples after ¶309).
- **5(b) — Customer-support and complaint-handling AI** before or after a credit decision, where it does not itself assess creditworthiness or build a credit score (¶b-examples).
- **5(b) — Credit-exposure monitoring** for internal prudential purposes after credit is granted (¶b-examples).
- **5(b) — Collateral evaluation** AI focused solely on the asset's features, risk factors and sale feasibility (¶b-examples).
- **5(b) — Margin credit for leveraged trading** — non-essential private service (¶b-examples; cf. ¶304 on leisure/travel/premium credit-card loans, stocks/securities, complex instruments).
- **5(c) — Non-life/non-health insurance**: motor, home, liability, travel pricing systems are outside 5(c) (¶314). Insurance-based investment products (PRIIPs Regulation Art. 4(2)) are also outside (¶314).
- **5(c) — Claims management** for health-insurance products that verify policy validity or determine pay-out, distinct from risk assessment or pricing (¶b-examples after ¶321).
- **5(c) — Product design for life insurance** analysing aggregate demographic and behavioural data to design new products, where no individual risk-profile evaluation occurs (¶b-examples).
- **5(d) — Pure transcription** of poor-quality emergency calls without classifying or evaluating them (¶b-examples after ¶336).
- **5(d) — General disaster forecasting** (flood-zone identification, wildfire spread modelling, weather/seismic monitoring) where the system is not intended to decide when/where to dispatch emergency services (¶336, ¶b-examples).
- **5(d) — Training-simulator AI** providing realistic scenarios and debriefings for first responders — not used on real-time calls (¶b-examples).
- **5(d) — Biometric patient identification** for medical procedures — not within any 5(d) purpose (¶b-examples).
- **5(d) — Network/connectivity AI** for emergency-call traffic routing — not responsible for the substantive outcome (¶b-examples).
- **5(d) — Healing-time estimation** and **routine medical-appointment scheduling** — no link to life-threatening emergencies (¶b-examples).

## Boundary clarifications

- **5(a) — Public-authority limitation and "on behalf of"**: AI used by private actors administering means-tested benefits *on behalf of* the state IS in scope (¶285–¶287, drawing on CJEU Fish Legal C-279/12 ¶51–¶52: entities vested with special powers beyond normal private-law rules count). Purely private charitable aid programmes — without public-law authority or special powers — are NOT.
- **5(a) — Tax remission is excluded** as a "financial support" but not a "service or benefit as such" (¶289).
- **5(a) — Evaluation without grant decision still counts**: AI used solely to evaluate eligibility is high-risk even if it does not itself grant/deny benefits; conversely, AI used solely to grant, deny, reduce, revoke or reclaim (without prior eligibility evaluation) also falls within 5(a) (¶292).
- **5(a) — Healthcare creditworthiness routes to 5(a), not 5(b)**: If a creditworthiness assessment is used to evaluate eligibility for public assistance benefits/services, it is classified under 5(a), not 5(b) (¶296).
- **5(b) — Fraud carve-out is purpose-based**: AI for transaction-level fraud detection (forged documents, anomalous application patterns) is NOT high-risk under 5(b), but only where fraud detection is the *main* intended use, preceding other purposes (¶306–¶307). If the fraud-detection output also feeds creditworthiness, the system still falls outside 5(b) (¶308). AML/CFT systems are NOT covered by the fraud carve-out and become high-risk if functionally linked to creditworthiness assessment (¶309).
- **5(b) — Pricing alone is outside 5(b)**: A standalone pricing AI relying on data from a separate creditworthiness assessment is NOT within 5(b) — but an integrated system combining assessment and pricing IS (¶300).
- **5(b) — Essential vs non-essential private services**: Essential includes bank-account provision, payment services with ancillary credit, loans, credit cards, credit-line extensions, mortgages, public financial services (¶302–¶303). Non-essential includes stocks/securities, margin trading, complex financial instruments, premium credit cards, leisure/travel loans (¶304). If a system is intended for both essential and non-essential services, it is classified as high-risk (¶305).
- **5(c) — Life and health only**: Motor, property, liability insurance pricing is NOT covered by 5(c) (¶314). However, health-class risks under Solvency II Annex I Section A points 1 and 2 (accident/industrial injury, sickness) ARE covered (¶316). Credit life insurance, private long-term care insurance and personal pension products with material livelihood impact ARE covered (¶317–¶318).
- **5(c) — No fraud carve-out**: Unlike 5(b), there is NO fraud-detection exception in 5(c). A risk-assessment/pricing system that also has fraud-detection functionality is still high-risk under 5(c); only a genuinely distinct stand-alone fraud system escapes (¶321).
- **5(c) — Claims management ≠ risk assessment/pricing**: Claims-validation and pay-out-amount AI is outside 5(c) (¶b-examples).
- **5(c) — Public-law insurers are in scope**: An AI used by a public-law health insurer for risk assessment/pricing is high-risk under 5(c) (¶319); private health insurance is essential even where the Member State has universal public healthcare (¶320).
- **5(d) — Emergency vs non-emergency healthcare**: Emergency call evaluation, dispatch, prioritisation and emergency triage are high-risk. Non-emergency healthcare triage tools (appointment scheduling, room/bed management, estimated healing time, patient identification) are NOT in 5(d) (¶b-examples).
- **5(d) — Forecasting must be specifically linked to dispatch**: General disaster/wildfire/flood forecasting is outside 5(d); forecasting specifically intended to decide when/where to dispatch emergency services IS within 5(d) (¶336).
- **5(d) — Medical-device overlap**: Emergency healthcare patient triage systems that qualify as medical devices under MDR Art. 2(1) and satisfy Art. 6(1) AI Act fall under Annex I AI Act (Art. 6(1) route); only if Art. 6(1) is not triggered do they fall under 5(d) (¶331, ¶334–¶335).

## Common Art. 6(3) exception scenarios

The Art. 6(3) "filter" allows certain Annex III systems to escape high-risk classification when they perform only narrow procedural, completion-improvement, pattern-detection, or preparatory tasks — provided they do not perform profiling of natural persons (Art. 6(3) penultimate sub-paragraph).

- **(a) Narrow procedural task** — Rare in 5(a)–(c) because most evaluations have direct outcome consequences. Possible examples from the guidelines: factual-information chatbots that only retrieve and structure existing information for case handlers without evaluating eligibility (¶c-examples after ¶293); speech-to-text systems with on-site case-handler review (¶c-examples).
- **(b) Improvement of completed activity** — Tools that polish or format the output of a case-worker who has already made the eligibility decision (e.g. cleaning up decision notes).
- **(c) Detection of decision-making patterns** — AI auditing benefit-decision consistency across cases, flagging deviations for human re-review without itself deciding eligibility.
- **(d) Preparatory task** — Translating foreign-language benefit applications where translation is an unavoidable but non-decisive step (¶c-examples). Summarising medical reports for a case handler who will review the full report before deciding (¶c-examples). Speech-to-text capture of case-handler/applicant conversations where the case handler is present and can verify the summary (¶c-examples). In 5(d): interpreting weather risk data in advance of a probable emergency to feed prioritisation that is then evaluated by human analysts/commander (¶c-examples). Situational-awareness gathering for on-site commanders that structures sensor data without evaluating triage (¶c-examples).

**IMPORTANT — profiling re-exception**: The Art. 6(3) filter explicitly does NOT apply where the AI system performs profiling of natural persons (Art. 6(3) penultimate sub-paragraph; see also `art-6-3-exception-decision-tree.md`). Credit scoring (5(b)) and insurance risk assessment (5(c)) are paradigm cases of profiling under Art. 4(4) GDPR — they evaluate personal aspects (financial situation, health, behaviour) of natural persons. Most 5(a) benefits-eligibility evaluations also involve profiling. In these sub-categories, Art. 6(3) will almost always be unavailable, regardless of how "narrow" or "preparatory" the task may appear.

## Common profiling considerations

- **5(b) Creditworthiness and credit scoring** are textbook profiling: the system evaluates personal aspects (financial situation, payment behaviour, demographic data) of natural persons to predict their willingness/ability to repay (Art. 4(4) GDPR; ¶295–¶296).
- **5(c) Insurance risk assessment** evaluates personal aspects (health status, family history, lifestyle, occupation, mortality predictors) and is profiling.
- **5(a) Benefits eligibility** typically involves profiling — household composition, income, employment status, behaviour are personal aspects evaluated to predict eligibility or fraud risk.
- **5(d) Emergency triage** is generally NOT profiling when based on severity criteria (presenting symptoms, call content, urgency indicators); it MAY become profiling where prioritisation criteria are tied to identity-based attributes (e.g. predicted patient demographics or behavioural history).
- For all four sub-categories, GDPR Art. 22 (right not to be subject to solely automated decisions producing legal/significant effects) frequently overlaps. Where profiling is present, the AI Act's Art. 6(3) filter is unavailable.

## Cross-references

- [art-6-3-exception-decision-tree.md](art-6-3-exception-decision-tree.md) — Art. 6(3) filter and profiling re-exception logic.
- [art-6-2-annex-iii-guidelines.md](art-6-2-annex-iii-guidelines.md) — general Annex III classification framework.
- [art-6-general-principles.md](art-6-general-principles.md) — intended-purpose test, value-chain attribution.
- Related follow-on activities: **role determination** (provider vs deployer role allocation for 5(a) public-authority deployers and 5(b)/5(c) financial-sector deployers); **obligation mapping** (Chapter III Section 2 high-risk obligations triggered by Art. 6(2) classification).
- **GDPR Art. 22** — automated decisions producing legal/significant effects; frequent overlap with 5(a)–(c).
- **GDPR Art. 9** — special categories (health data in 5(a) healthcare benefits and 5(c) health insurance).
- **Regulation (EC) 883/2004** — coordination of social security systems (terminology for 5(a) social-security benefits).
- **Capital Requirements Regulation (EU) 575/2013, Art. 144** and **Solvency II Directive 2009/138/EC, Art. 120** — prudential-purpose IRB/internal-model AI carve-out and its limits (¶322–¶328); a system used for both creditworthiness/credit-scoring and IRB capital calculation is still high-risk under 5(b).
- **2002/65/EC Distance Marketing of Financial Services Directive Art. 2(b)** — financial-services definitions referenced at ¶302.
- **Directive (EU) 2018/1972 European Electronic Communications Code Art. 2(31), (36), (38), (39)** — definitions of emergency communication, PSAP, emergency services referenced for 5(d) (¶332–¶333).
- **TFEU Art. 196** — emergency response as Member State competence (¶333).
- **Medical Devices Regulation (EU) 2017/745** — emergency triage systems that qualify as medical devices route through Annex I AI Act / Art. 6(1) before falling back to 5(d) (¶331, ¶334–¶335).
