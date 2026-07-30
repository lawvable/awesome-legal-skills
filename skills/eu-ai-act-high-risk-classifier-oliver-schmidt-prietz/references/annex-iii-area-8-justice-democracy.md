# Annex III Area 8 — Administration of justice and democratic processes

**Annex III citation:** Nr. 8
**Effective date:** 2 December 2027 (per AI Omnibus)
**Source:** Commission Guidelines Annex III, Area 8 section. Full text: the Commission Draft Guidelines on Art. 6 classification (2026), Annex III section.

## Scope of the area

Annex III Nr. 8 covers two materially different sub-areas held together by the common goal of protecting fundamental rights central to a democratic Union. Recital 61 AI Act justifies high-risk classification on the basis of potentially significant impact on democracy, the rule of law and fundamental rights, including the right to an effective remedy and to a fair trial (¶404). Recital 62 adds, for the electoral sub-area, that the high-risk regime addresses risks of undue external interference with the right to vote enshrined in Article 39 of the Charter, and adverse effects on democracy and the rule of law (¶435). The two sub-categories — judicial assistance (8(a)) and democratic processes (8(b)) — are otherwise analysed independently.

Two explicit carve-outs frame the boundary of Area 8. **For 8(a)**, Recital 61 excludes AI systems intended for purely ancillary administrative activities that do not affect the actual administration of justice in individual cases — examples include anonymisation/pseudonymisation of judicial decisions, internal communication, scheduling, fee verification, and document dispatch (¶419, ¶423). The judicial-authority limb also requires that the system either (i) assist in researching and interpreting facts and the law, or (ii) assist in applying the law to a concrete set of facts; mere information retrieval (Boolean/keyword search) is not within scope (¶421). The same logic extends to alternative dispute resolution (ADR) bodies whose decisions **produce legal effects for the parties** — arbitration awards typically do, mediation outcomes typically do not (¶430–¶432). **For 8(b)**, the second sentence of Nr. 8(b) excludes AI systems whose outputs natural persons are not directly exposed to — i.e. back-office campaign-logistics tools (¶445). General-purpose chatbots that refuse voting advice and neutral election-information systems also fall outside (¶437).

The rights at stake are the right to a fair trial and to an effective remedy (Art. 47 Charter, Art. 19 TEU), judicial independence (Recital 61), and the right to vote (Art. 39 Charter). The boundary with the Article 5 prohibitions is important: legitimate political-influence AI sits **inside** Annex III Nr. 8(b) as high-risk, whereas subliminal, purposefully manipulative or deceptive techniques materially distorting behaviour fall under Art. 5(1)(a) and are **prohibited** (¶446–¶447). The AI Act takes a product-safety approach for legitimate uses; foreign information manipulation and interference (FIMI) is regulated through the Political Advertising Regulation, the Digital Services Act and the European Democracy Shield rather than through the high-risk regime.

## Sub-categories
- **Nr. 8(a) — Judicial assistance** — AI systems intended to be used by a judicial authority or on its behalf to assist that authority in researching and interpreting facts and the law and in applying the law to a concrete set of facts; and AI systems used in **alternative dispute resolution** in similar ways where the outcome of the ADR proceedings produces legal effects for the parties. EXCLUDING purely ancillary administrative tasks (anonymisation, case management, scheduling, fee verification, document dispatch, internal communications) that do not affect the actual administration of justice in individual cases.
- **Nr. 8(b) — Democratic processes** — AI systems intended to be used to influence the outcome of an election or referendum, or to influence the voting behaviour of natural persons in the exercise of their vote in elections or referenda. EXCLUDING AI systems whose outputs natural persons are not directly exposed to — i.e. tools used to organise, optimise or structure political campaigns from an administrative or logistical viewpoint.

## Practical examples — HIGH-RISK

### Nr. 8(a) — Judicial assistance
- **Judicial decision/judgment drafting systems** that analyse case facts, submissions, applicable law and case law and then generate drafts of judicial decisions or judgments (including the reasoning and decision parts) (¶423 list). Both limbs of 8(a) are satisfied; no Art. 6(3) exception applies due to proximity to decision-making.
- **Small-claims or order-for-payment generators** that produce draft decisions in low-value or undisputed civil proceedings relying on structured case data and legal templates. The proximity to the final decision blocks any Art. 6(3) filter.
- **Repetitive-case support systems** that extract relevant facts, cluster cases by recurring factual patterns, search prior decisions for analogous cases and reasoning, and assemble suggested text modules for the final decision. Assessed in combined configuration (not module-by-module), the joint outputs materially influence individual outcomes.
- **Precedent and applicable-law selection systems** that analyse the facts of a concrete case and suggest applicable laws, precedents, and how they apply — directly assists in the core judicial task and cannot benefit from Art. 6(3) exceptions.
- **ADR adjudication-assistance systems** used by arbitral tribunals (or other ADR bodies whose outcomes produce legal effects, e.g. equality bodies, labour conciliation bodies issuing binding decisions, professional disciplinary bodies) in researching/interpreting facts and law and applying law to concrete facts. Examples mirror the judicial-authority examples above (¶441).

### Nr. 8(b) — Democratic processes
- **AI-enabled political ad targeting** systems (including specialised recommender systems) that optimise targeting and ad delivery of political advertising within the limits of Regulation (EU) 2024/900. These typically involve profiling, which triggers the re-exception and prevents Art. 6(3) filtering.
- **AI-enabled political-dialogue chatbots / virtual spokespersons** developed for use by political actors to interact with natural persons in a conversational manner to persuade them to support a candidate or policy (also subject to Art. 50 transparency obligations).
- **AI-enabled voter advice applications (VAAs)** that ask voters about preferences, values, or issues and recommend the "closest match" party or candidate — generates personalised recommendations that steer perceived political proximity. Note: a static rule-based VAA may not qualify as an AI system at all; only adaptive/inferential VAAs are in scope.
- **AI-enabled constituency-boundary or redistricting systems** intended to influence the outcome of an election by shaping electoral geography (¶439, "influencing the outcome … can go beyond voting and relate to other stages of the electoral process, such as redrawing the boundaries of constituencies").

## Practical examples — NOT HIGH-RISK

### Nr. 8(a) carve-outs (purely ancillary or administrative)
- **Court case management and case-assignment systems** that assign cases to judges based on specialisation, workload, or holiday schedule — administrative, no effect on adjudication in individual cases (Recital 61; ¶423 list). Different conclusion if the system also performs procedural judicial assessments (jurisdiction, single-judge vs. panel, public-session need).
- **Court speech-to-text transcription systems** with speaker separation, punctuation insertion, and legal-terminology correction. Even when transcripts later form part of the evidentiary record, the system performs a clerical technical task and does not analyse, evaluate, or draw conclusions. Conclusion changes if the transcript is further processed by an AI system to summarise, evaluate, or recommend.
- **Court website chatbots / virtual assistants** providing the public with information about procedural steps, required documents, deadlines, and available remedies — no assistance in researching/interpreting facts and the law.
- **Press-release and legal-summary drafting systems** that translate technical judgment language into accessible public summaries — ancillary administrative activity that does not affect administration of justice in individual cases.
- **Evidence management and search systems** that build chronologies and provide references within evidentiary material without analysing, evaluating, or drawing conclusions — organisation and access, not legal reasoning.
- **Other ancillary administrative tools**: anonymisation/pseudonymisation of judicial decisions, internal personnel communication, delivery-address search and document dispatch, court-fee payment verification, electronic-signature processing, power-of-attorney verification (¶423 list).
- **AI systems used by parties or their legal representatives** (e.g. attorney tools to facilitate submissions to a court) — parties are not acting "on behalf of" a judicial authority, so outside 8(a) entirely.
- **ADR systems where outcomes have no legal effect** — typical mediation or conciliation producing a voluntary, non-binding agreement falls outside 8(a) (¶430).

### Nr. 8(b) carve-outs (admin/logistical or neutral)
- **Campaign staff and volunteer management systems**; rally scheduling and assignment tools; topic-selection tools used in back-office campaign work — excluded by the second sentence of Nr. 8(b).
- **Donor-database analytics** predicting contribution likelihood for current or future campaigns — back-office, not exposed to natural-person targets.
- **Generative AI for drafting campaign slogans and communications** that humans review before dissemination — assists preparation of materials, not the influence itself (note: still subject to Art. 50 transparency where applicable).
- **Neutral election-information chatbots** operated on behalf of election authorities providing politically neutral information (when, where, and how to vote) (still subject to Art. 50 transparency).
- **General-purpose chatbots with adequate guardrails** that refuse to give voting advice or provide only neutral factual information about parties/candidates/voting procedures.
- **Legislative-monitoring, sociological-research, and academic-modelling AI** — monitoring elected officials' legislative activity for informational purposes, sociological agencies analysing election data objectively, academic institutions modelling electoral behaviour for research (the latter also likely covered by the Art. 2(6) research carve-out).
- **Vote-counting / OCR ballot-scanning systems** functioning as technical aids for mechanical recognition and tallying — intended purpose is not "influence", but technical accuracy.

## Boundary with Art. 5 prohibitions

- **Art. 5(1)(a)** prohibits AI systems deploying subliminal techniques beyond a person's consciousness or purposefully manipulative or deceptive techniques with the objective or effect of materially distorting behaviour in a way that causes (or is reasonably likely to cause) significant harm. Annex III Nr. 8(b) addresses the **legitimate** (non-prohibited) variants of political influence (e.g. compliant ad targeting, transparent chatbots, voter advice applications). If a deployment crosses into subliminal/manipulative/deceptive territory, it is prohibited under Art. 5(1)(a) and does not need an Annex III analysis at all.
- **Art. 5(1)(f)** (emotion-inference) is not specific to Area 8 but may intersect with campaign chatbots; verify the system is not deployed in a workplace/education context where emotion inference is prohibited.
- **FIMI (foreign information manipulation and interference)** is not regulated through the AI Act's high-risk regime — it is illegitimate activity governed by Regulation (EU) 2024/900 (Political Advertising Regulation), Regulation (EU) 2022/2065 (Digital Services Act), and the European Democracy Shield (JOIN(2025) 791). The AI Act adopts a complementary product-safety approach (¶446–¶447).

## Common Art. 6(3) exception scenarios

The Commission supplies worked examples of when the filter mechanism applies. Always apply the **profiling re-exception** first: if the system performs profiling, the filter is blocked regardless of which limb of Art. 6(3) the provider invokes.

### Nr. 8(a) judicial assistance — exception scenarios

- **(a) Narrow procedural task**
  - **Pre-classification of incoming applications/claims** by case type (contract, inheritance, etc.) — narrow procedural classification, qualifying under Art. 6(3)(a). Falls out of the exception if it also recommends admissibility (substantive assessment).
  - **Metadata extraction** from case files (procedural roles: parties, representatives, witnesses, experts) to support clerical work such as summons.
  - **Advanced search engines** in public case-law databases (Boolean/keyword + NLP search, summaries of published decisions) — narrow procedural assistance even if technically "interpreting the law".

- **(b) Improvement of a completed human activity**
  - **Language editing / proofreading** of judicial decisions or judgments already drafted by the judge — style improvements without content change.
  - **Factual-completeness check** comparing a judge-drafted decision against the case file to flag aspects not addressed — compliance check on completed human work; does not assess credibility, determine facts, or suggest answers.

- **(d) Preparatory task**
  - **Case-law summarisation for a human judge** who performs the actual legal analysis — preparatory, qualifying under Art. 6(3)(d), provided proximity to the final decision remains low.
  - **Document handling, indexing, translation** of case materials to support a judge's later analysis — preparatory.

- **(c) Detection of decision-making patterns or deviations** is rarely invoked in 8(a); the Commission focuses on (a), (b), and (d).

### Nr. 8(b) democratic processes — exception scenarios

- Most Nr. 8(b) systems involve **profiling of voters** (political ad targeting, voter advice applications, persuasion chatbots), so the re-exception applies and the filter is blocked.
- **(b) Improvement of a completed human activity** — the Commission's single worked example: an AI system that **checks the tone of campaign texts already written by humans**, highlighting unclear or counterproductive wording or conflicts with prior party materials. Even though it could be argued to influence electoral outcomes, the system merely improves a previously completed human activity (Art. 6(3)(b)).

## Common profiling considerations

**Nr. 8(a) — judicial assistance.** Whether profiling is present depends heavily on what the system processes. Purely legal-research and case-law-analysis systems that operate on legal sources (not on personal data of parties) are typically **not profiling**. Systems that evaluate aspects of the parties (e.g. assessing credibility, predicting recidivism in a way that crosses into Annex III Nr. 6 / Nr. 8 overlap, or generating personalised recommendations about a party) may perform profiling and lose access to the Art. 6(3) filter. Note also the overlap with Annex III Nr. 6 (law enforcement) for judicial authorities acting in criminal matters — they are simultaneously "judicial authorities" under Nr. 8 and "law enforcement authorities" under Nr. 6 (¶408).

**Nr. 8(b) — democratic processes.** Voter profiling is paradigmatic. Political ad targeting, voter advice applications, and persuasion chatbots typically build or rely on profiles of natural persons to evaluate political preferences, values, propensity to vote, or persuadability. The Commission confirms in the targeting example that profiling typically blocks the Art. 6(3) filter (¶preceding the Nr. 8(b) example list). In practice, assume profiling applies to any Nr. 8(b) system that personalises output to individual natural persons; document carefully if claiming otherwise.

## Interplay with other EU acts

- **Regulation (EU) 2024/900 (Political Advertising Regulation, "PAR")** — AI-enabled political ad targeting is subject to PAR transparency, targeting-data and labelling rules in parallel with the AI Act high-risk regime.
- **Regulation (EU) 2022/2065 (Digital Services Act, "DSA")** — Very Large Online Platforms (VLOPs) and search engines hosting political content are subject to systemic-risk management, transparency, and risk-mitigation obligations that complement the AI Act.
- **European Democracy Shield (JOIN(2025) 791)** — the EU's strategic framework for resilient democracies; the AI Act high-risk regime for Nr. 8(b) is one product-safety pillar within this broader policy.
- **Directive 2013/11/EU (Consumer ADR Directive)** as amended by Directive 2025/2647 — provides the reference framework for "ADR body" in Nr. 8(a) and now contains additional safeguards on automated decision-making in ADR (parties must be informed and may request human review), applying in parallel with the AI Act.
- **Directive 2008/52/EC (EU Mediation Directive)** — relevant for determining whether mediation outcomes "produce legal effects" (typically only when parties stipulate enforceability under national law).
- **Article 19 TEU and Article 47 Charter** — judicial independence and right to effective remedy / fair trial underpin the Nr. 8(a) regime.
- **Article 39 Charter** — right to vote underpins the Nr. 8(b) regime.
- **Art. 50 AI Act transparency obligations** — political-dialogue chatbots, neutral election-information chatbots, AI-generated political content, and judicial-authority chatbots interacting with the public are subject to Art. 50 transparency independently of high-risk classification.

## Cross-references
- [art-6-3-exception-decision-tree.md](art-6-3-exception-decision-tree.md) — apply for every Art. 6(3) claim, including the mandatory profiling check (especially load-bearing for Nr. 8(b)).
- [art-6-2-annex-iii-guidelines.md](art-6-2-annex-iii-guidelines.md) — general guidance on Annex III classification.
- [ai-omnibus-timeline-postponements.md](ai-omnibus-timeline-postponements.md) — confirms 2 December 2027 effective date for Annex III high-risk obligations.
- Related follow-on activities: **role determination** (provider vs. deployer — note that public prosecutors may be "judicial authorities" under 8(a) **and** "law enforcement authorities" under Nr. 6 depending on institutional independence and intended use); **obligation mapping** (high-risk provider/deployer duties triggered once Area 8 classification stands).
- **AI Act Art. 5(1)(a)** — prohibited subliminal/manipulative/deceptive techniques; verify a candidate Nr. 8(b) system is not in fact prohibited.
- **AI Act Art. 50** — transparency obligations for chatbots and AI-generated content (chatbot disclosure, deepfake/AI-content labelling).
- **Regulation (EU) 2024/900** — Political Advertising Regulation (transparency and targeting limits for AI-enabled political advertising).
- **Regulation (EU) 2022/2065** — Digital Services Act (VLOP risk management and transparency).
- **European Democracy Shield (JOIN(2025) 791)** — broader EU policy framework against FIMI.
