# Annex III Area 7 — Migration, asylum, border control management

**Annex III citation:** Nr. 7
**Effective date:** 2 December 2027 (per AI Omnibus)
**Source:** Commission Guidelines Annex III, Area 7 section. Full text: the Commission Draft Guidelines on Art. 6 classification (2026), Annex III section.

## Scope of the area

Annex III Nr. 7 captures AI systems intended to be used **by or on behalf of competent public authorities** — or by Union institutions, bodies, offices and agencies (notably Frontex, the European Union Agency for Asylum, and eu-LISA) — **in the field of migration, asylum and border-control management**, in so far as such use is permitted under Union or national law. The personal scope is therefore narrow: private actors using AI in adjacent commercial contexts (e.g. airline pre-boarding checks they perform on their own account) do not fall within Area 7 unless they are acting on behalf of a competent authority. The "competent authority" concept extends across border-control authorities (Schengen Borders Code, EBCG Regulation), consular and visa authorities (Visa Code, VIS), asylum determining authorities (Asylum Procedures Directive/Regulation), return and detention authorities (Return Directive), and administrative/judicial appeal bodies reviewing eligibility decisions.

The area is split into four sub-categories: **7(a)** polygraphs and similar tools; **7(b)** risk assessment of persons entering or having entered a Member State (security, irregular-migration, health); **7(c)** assistance to authorities examining asylum, visa and residence applications (and associated complaints regarding eligibility, including reliability-of-evidence checks); and **7(d)** detection, recognition or identification of natural persons in this context — **excluding the verification of travel documents**, which is the only express carve-out within the area itself.

Recital 60 AI Act stresses the heightened vulnerability of the persons concerned: applicants for international protection, third-country nationals at external borders, persons in return or detention procedures. The rights at stake include the right to asylum and the principle of non-refoulement (Art. 18–19 CFR; 1951 Refugee Convention and 1967 Protocol), human dignity (Art. 1 CFR), non-discrimination (Art. 21 CFR), effective remedy (Art. 47 CFR), and the right to good administration. Classification as high-risk under Area 7 does not by itself authorise the use of the system; deployment must additionally comply with the GDPR/EUDPR, the Charter, EU asylum/visa/border-management law, and any large-scale IT system regimes (VIS, SIS, Eurodac, EES, ETIAS, ECRIS-TCN, the Interoperability components) whose purpose limits, access conditions and safeguards must be respected.

## Sub-categories

- **Nr. 7(a)** Polygraphs and similar tools — physiological, behavioural or biometric signal analysis aimed at inferring deception in migration, asylum or border-control settings. Where the same functionality is used by or on behalf of law enforcement authorities, the system is classified under point 6(b) of Annex III instead.
- **Nr. 7(b)** Assessing risks posed by entering/entered natural persons — security risk, irregular-migration risk, or health risk. The decisive element is the intended production of a per-person score, category or flag that can influence entry, stay, detention, return or related measures.
- **Nr. 7(c)** Examining asylum / visa / residence applications, and associated complaints regarding eligibility — including reliability-of-evidence checks (illustrative, not exhaustive). Covers both substantive complaints (facts, evidence, credibility) and complaints about procedural fairness affecting the decision; excludes complaints about mere service quality.
- **Nr. 7(d)** Detecting, recognising or identifying natural persons in migration, asylum or border-control contexts — **except verification of travel documents**. Sensor modality and place of deployment are not decisive; intended purpose is.

## Practical examples — HIGH-RISK

**7(a) — Polygraphs and similar tools**
- AI system deployed in secondary inspection at an external-border airport that analyses a traveller's verbal and non-verbal interview responses and supplies the officer with a supplementary credibility indicator.
- Consular AI that analyses an applicant's voice patterns and verbal responses during a visa interview to provide veracity indicators to the consular officer.

**7(b) — Person-level risk assessment**
- Risk-scoring system that analyses a traveller's personal history, travel patterns and watch-list matches to produce a per-person risk score used by border guards to refer the person to second-line checks.
- Automated security/irregular-migration/health risk-flagging used during travel authorisation or visa processing on a per-person basis.
- Visa overstay-risk ranking using nationality and similar proxies that channels applicants from specific groups into intensified tracks.
- System inferring a named traveller's likelihood of irregular migration from recent online search behaviour and emitting a per-person risk flag for entry control (must not cross the Art. 5(1)(c) social-scoring or Art. 5(1)(d) crime-prediction prohibitions).
- Health-risk flagging system that assesses whether an individual presents an infectious-disease risk based on biometric readings and recent travel history and flags them for additional medical checks.
- Group-level indicators (e.g. overstay rates by route and season) **applied to named travellers** by a rules engine to generate per-person irregular-migration flags — even if the AI module on its own only outputs aggregates, the combined configuration is high-risk.

**7(c) — Application/complaint examination**
- AI system that assesses the authenticity and consistency of documents or the plausibility of personal narratives and provides credibility signals the examiner relies on for the eligibility decision (asylum, visa, residence).
- System that analyses phone data lawfully obtained from a device to validate routes, timelines or contacts and produces signals used in eligibility appraisal.
- Document-morphing / non-conforming-ink / copied-signature / chip-PKI-validity detection when performed **as a step in the eligibility examination** (this is examination assistance, distinct from the 7(d) travel-document-verification carve-out).
- AI system that identifies substantive or credibility-relevant discrepancies against prior submissions to assist subsequent examination of an asylum, visa or residence application or its associated complaint.
- AI system that analyses recorded speech to indicate a likely country or region of origin used in the authority's eligibility reasoning and selection of country-of-origin information.

**7(d) — Detection, recognition, identification**
- Live facial recognition at border-crossing points comparing live camera feeds to biometric templates in connected systems and returning identity hits for operator action (also high-risk under Annex III(1)).
- Satellite imagery, surveillance towers or unmanned platforms that flag human presence at land borders and cue patrol dispatch, apprehension or secondary checks.
- Maritime-surveillance AI that detects and tracks persons for migration management or border-control operations, including cueing interception or boarding — irrespective of whether deployed in territorial waters, contiguous zone or high seas.
- Sensor-data analysis detecting persons (including hidden persons) inside vehicles and generating alerts that prompt second-line checks.
- AI monitoring reception or detention areas that detects or tracks identified persons and alerts staff for intervention.
- Presentation-attack / on-person liveness detection used within person detection or recognition flows (as opposed to bare travel-document verification).

## Practical examples — NOT HIGH-RISK

- **Travel-document verification** (the express 7(d) carve-out) — AI that checks morphing, unusual inks, copied signatures, chip validity or PKI validity on a travel or identity document. Presentation-attack detection used **solely as an anti-spoofing safeguard within a one-to-one verification flow** at seamless borders remains part of verification and is not, on its own, classified under Area 7.
- Applicant-service tools — chatbots that answer FAQs, route users to forms, schedule appointments, or deliver application-status notifications. The intended purpose is service delivery to the applicant, not assistance to the authority in examining eligibility.
- Aggregate or cohort-level migration analytics that detect trends, anticipate flows, or identify possible irregular-migration networks where no natural person is identified or identifiable from the outputs.
- Aggregate health-flagging that triggers uniform public-health measures (e.g. testing every passenger on a flight) without selecting specific individuals for differential treatment.
- Vehicle-focused screening — licence-plate / travel-time analytics that route a vehicle to a general secondary lane for technical inspection without creating a personal risk indicator about driver or passengers; stolen-vehicle flagging at border crossings.
- Search-and-rescue / safety-of-navigation systems whose outputs go exclusively to SAR coordination or collision avoidance and are not used to cue border-control actions on the detected persons.
- Crowd-size or gate-occupancy estimation used to balance lanes and reduce queues, provided the system does not detect, recognise or identify persons or emit person-level alerts.
- Post-decision data cleaning — harmonising terminology and detecting duplicates in completed risk-assessment or eligibility records after the human assessment has been concluded.

## Boundary with Art. 5 prohibitions

- **Art. 5(1)(b) — exploitation of vulnerabilities.** Behaviour-analysis tools at borders (voice-stress, micro-expressions, gaze patterns) are not prohibited merely because they may misinterpret stress or cultural expressions; they become prohibited only where the design or use is to materially distort the behaviour of vulnerable persons in a significantly harmful way. Otherwise they remain in scope of 7(a) as high-risk.
- **Art. 5(1)(c) — social scoring.** Systems that, over time, evaluate or rank migrants based on physiological reactions, behaviour (including online activity) or other personal data to derive a generalised trustworthiness or risk score — especially when used across contexts or producing detrimental treatment — may amount to prohibited social scoring. Below that threshold the same tool is high-risk under 7(b).
- **Art. 5(1)(d) — individual crime-risk prediction.** Tools predicting future criminal behaviour at borders from gaze or speech patterns may be prohibited where Art. 5(1)(d) conditions are met; otherwise they fall under 7(b) when the intended purpose is to assess migration/security risk.
- **Art. 5(1)(f) — emotion recognition.** The Art. 5(1)(f) prohibition targets workplace and educational settings; it does not extend with the same force to migration/border-control contexts. Deception or credibility-analysis tools at borders are not therefore prohibited under Art. 5(1)(f) and are typically high-risk under 7(a). **Art. 5(1)(g) — biometric categorisation by sensitive attributes** still applies fully.
- **Art. 5(1)(h) — real-time RBI in publicly accessible spaces for LE.** Per the Commission Guidelines on prohibited practices, a border-crossing point is **not** a publicly accessible space, so the prohibition does not apply there; deployment in such areas is instead captured as high-risk under Annex III(1) or Annex III(7). The street leading to a border-crossing point or a forest nearby normally **is** a publicly accessible space, so the prohibition (subject to the Art. 5(1)(h)(i)-(iii) exceptions and Art. 5(2)-(5) safeguards) does apply there. Migration is administrative, not law enforcement; the real-time RBI prohibition is structured for the LE setting.

## Common Art. 6(3) exception scenarios

The filter mechanism is generally **unavailable** across Area 7:

- **7(a)** — Polygraph-type systems produce evaluative outputs that directly influence the substance of an individual examination and are not narrow procedural, preparatory or post-decision tasks. The exception does not apply.
- **7(b)** — Systems within 7(b) typically amount to **profiling** (automated processing of personal data to evaluate or predict a natural person's behaviour or movements). Per Art. 6(3) last sub-paragraph, AI systems performing profiling cannot benefit from the exception. Only narrow procedural or purely preparatory functions that do **not** themselves amount to profiling and do **not** materially influence the substance or outcome of an individual risk assessment can escape — and combined configurations are assessed as a whole, not module by module.
- **7(c)** — Where outputs materially influence eligibility (validating or challenging evidence, prioritising issues, pre-classifying status elements), the system stays high-risk. **Narrow procedural / preparatory carve-outs the Commission does accept:** fixed-label case-file organisation; completeness/format checking of visa/ETIAS applications without risk scoring; verbatim-difference highlighting **without** credibility assessment; neutral interview transcription, translation or summarisation **without** legal/credibility inferences; ex-post pattern detection on completed files for quality assurance. Embedding low-risk modules inside a single integrated assistant that steers eligibility analysis **does not** bring the whole system under the filter.
- **7(d)** — Only functions that neither detect, recognise nor identify persons and that do not influence operational decision-making qualify. Example: stabilising, denoising or enhancing video feeds without performing any detection/recognition/identification and without producing cues for operational response (Art. 6(3)(d) preparatory task).

## Common profiling considerations

- Asylum, visa and residence eligibility decisions and migration/security/health risk assessments are paradigm cases of **profiling** within Art. 4(4) GDPR / Art. 3(52) AI Act: automated processing of personal data to evaluate personal aspects of a natural person (background, credibility, risk, eligibility). This triggers the profiling re-exception in Art. 6(3) AI Act, which removes the filter mechanism.
- Aggregate-only outputs that are never applied to identified or identifiable persons fall outside profiling. However, **low-level aggregation or linkability with other datasets can still make aggregate data personal data**, and the moment an aggregate indicator is applied to a named traveller, profiling re-enters.
- A "combined configuration" (e.g. AI aggregator + non-AI rules engine that applies the aggregate to named persons) is assessed as a whole: profiling at the system level disqualifies all components from the filter.

## Vulnerability and fairness considerations

- Persons in scope of Area 7 are often in a **particularly vulnerable position** (asylum seekers, applicants for international protection, irregular migrants, persons in detention or return procedures). Recital 60 AI Act flags this explicitly; the AI Act's high-risk requirements on accuracy, robustness, transparency and human oversight take on heightened importance here.
- **Data-quality and representativeness** under Art. 10 are critical: training, validation and testing data must be examined for biases that disfavour specific nationalities, ethnicities, languages or routes; documented risks of inaccuracy and bias in deception-detection and risk-scoring tools mean these obligations are not formalities.
- **Overreliance and automation bias** (¶389) are explicit concerns even where a human takes the final decision. Art. 14 human-oversight requirements should be configured to ensure outputs are treated as supplementary, not determinative.
- **Non-refoulement and effective remedy** must be preserved by design: the deployer (typically a public body, hence subject to the FRIA under Art. 27) cannot let AI outputs effectively close off access to the asylum procedure or to effective judicial review.
- **Sectoral data-protection regimes** (Eurodac, VIS, SIS, EES, ETIAS, ECRIS-TCN, Interoperability components) impose additional purpose limits and access conditions that must be respected on top of the AI Act.

## Cross-references

- [art-6-3-exception-decision-tree.md](art-6-3-exception-decision-tree.md) — Art. 6(3) filter mechanism, including the profiling re-exception that disqualifies most of Area 7.
- [annex-iii-area-1-biometrics.md](annex-iii-area-1-biometrics.md) — Most 7(d) identification systems and 7(a) modalities involving biometrics are **also** high-risk under Area 1 and therefore subject to third-party conformity assessment under Art. 43.
- Related follow-on activities: **role determination** (provider vs. deployer; public-authority deployers); **obligation mapping** (Art. 26 deployer duties incl. Art. 27 fundamental-rights impact assessment for public-authority deployers; Art. 49 EU database registration for Annex III systems used by public authorities).
- **AI Act Art. 5** — Art. 5(1)(b), (c), (d), (g) and (h) prohibitions interact with Area 7 (see boundary section above).
- **AI Act Art. 2(3)** — National-security exclusion does **not** cover all migration/border management; only AI systems placed on the market or put into service exclusively for national-security purposes are excluded. Ordinary border control, asylum and visa processing remain in scope.
- **EU sectoral regimes** — Schengen Borders Code (Reg. (EU) 2016/399); European Border and Coast Guard Regulation (Reg. (EU) 2019/1896); Visa Code (Reg. (EC) No 810/2009) and VIS Regulation (Reg. (EU) 2021/1134); Common European Asylum System incl. Asylum Procedures Directive 2013/32/EU (replaced 12 June 2026 by the Asylum Procedures Regulation (EU) 2024/1348); Return Directive 2008/115/EC; Screening Regulation (EU) 2024/1356; Return Border Procedure Regulation (EU) 2024/1349; Asylum and Migration Management Regulation (EU) 2024/1351; Eurodac Regulation (EU) 2024/1358 (from 12 June 2026).
- **AI Act Recital 60** — Vulnerability and fundamental-rights framing for Area 7.
