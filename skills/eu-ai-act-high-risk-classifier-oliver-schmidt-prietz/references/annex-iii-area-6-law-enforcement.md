# Annex III Area 6 — Law enforcement

**Annex III citation:** Nr. 6
**Effective date:** 2 December 2027 (per AI Omnibus)
**Source:** Commission Guidelines Annex III, Area 6 section. Full text: the Commission Draft Guidelines on Art. 6 classification (2026), Annex III section.

> **Reminder:** Many use cases in this area overlap with Art. 5 prohibitions (notably Art. 5(1)(d) predictive policing based solely on profiling/personality assessment, Art. 5(1)(f) emotion recognition in workplace/education, Art. 5(1)(g) biometric categorisation by sensitive attributes, Art. 5(1)(h) real-time remote biometric identification in publicly accessible spaces). Always check the Art. 5 boundary first. Prohibited systems are NOT high-risk — they are forbidden.

## Scope of the area

Annex III Nr. 6 covers AI systems intended to be used by — or on behalf of — **law enforcement authorities**, or by Union institutions, bodies, offices, or agencies in support of law enforcement authorities. The Commission Guidelines (¶340–¶341) anchor the term to Art. 3(45) AI Act, which mirrors Art. 3(7) of Directive (EU) 2016/680 (the Law Enforcement Directive, "LED"): any public authority — or other entity entrusted by Member State law — competent for the prevention, investigation, detection or prosecution of criminal offences or the execution of criminal penalties, including safeguarding against and preventing threats to public security. A **functional approach** applies: police, public prosecutors, probation and parole services, penitentiary services, and judicial authorities acting in criminal matters all qualify when carrying out law-enforcement (not administrative) tasks. Customs authorities qualify only when preventing/investigating customs-related crimes — administrative customs work falls outside Area 6 (¶343, ¶348–¶349).

The "on behalf of" extension covers contractors and support entities. Union-level coverage explicitly includes **Europol, Eurojust, the EPPO, and Frontex** to the extent their activities constitute law enforcement (¶347). The boundary with **national security/intelligence** is critical: Art. 2(3) AI Act excludes systems used exclusively for military, defence, or national security purposes, regardless of the entity. However, where an intelligence authority performs law enforcement functions, or where a system is intended for joint use by LE and intelligence authorities, it falls within scope and is high-risk if it matches a Nr. 6 use case (¶344–¶345).

The rights at stake are exceptionally heavy: **presumption of innocence, fair trial, freedom from discrimination, data protection, and personal liberty.** Recital 59 emphasises the power imbalance, the risk of surveillance, arrest or deprivation of liberty, and the importance of accuracy, reliability and transparency. Classification as high-risk under Area 6 does not by itself make the use lawful under other Union or national law (¶338).

## Sub-categories

- **Nr. 6(a)** AI systems used to assess the risk of a natural person becoming the **victim** of criminal offences (forward-looking, preventive/protective).
- **Nr. 6(b)** AI systems used as **polygraphs and similar tools** (lie detection via physiological responses, voice stress, eye-tracking/pupillometry, brain-imaging, or behavioural/micro-expression analysis).
- **Nr. 6(c)** AI systems used to **evaluate the reliability of evidence** in the course of investigation or prosecution (authenticity verification, data integrity, source reliability, consistency checks).
- **Nr. 6(d)** AI systems used to assess the risk of a natural person **offending or reoffending**, not solely on the basis of profiling per LED Art. 3(4), or to assess personality traits/characteristics or past criminal behaviour of persons or groups (subject to Art. 5(1)(d) prohibition).
- **Nr. 6(e)** AI systems used for the **profiling of natural persons** (as per LED Art. 3(4)) in the course of the detection, investigation or prosecution of criminal offences.
- **Nr. 6(f)** AI systems used for **crime analytics** — searching complex related/unrelated large datasets to identify unknown patterns or discover hidden relationships in data.

## Practical examples — HIGH-RISK

**Nr. 6(a) — Victim risk assessment**
- **Domestic violence risk assessment** systems analysing victim statements, police reports, prior incidents, restraining-order data, and social services records to score the risk faced by a (potential) victim, informing police protection measures or restraining-order decisions (¶359 examples).
- **Human trafficking vulnerability detection** systems aggregating indicators (age, lack of valid documentation, travel with unrelated adults, signs of control, links to high-risk sectors) to score the likelihood that a person is being or will be trafficked.
- AI-based risk-assessment systems used by **judicial authorities in criminal courts** to estimate the probability of severe or repeated domestic intimate-partner violence when issuing or maintaining restraining orders.

**Nr. 6(b) — Polygraphs and similar**
- AI systems analysing **facial micro-expressions** to assess credibility of answers during an interrogation.
- AI systems measuring **eye-tracking and pupillary responses** while a suspect answers questions.
- AI systems performing **voice stress analysis** or brain-imaging interpretation for deception detection.

**Nr. 6(c) — Evidence reliability evaluation**
- **AI-enabled digital forensics** for image/audio/video analysis to detect alteration or manipulation of evidence (e.g. CCTV authenticity, deepfake detection).
- AI systems detecting **document alterations or forged signatures**.
- AI systems evaluating **authenticity of digital evidence** from mobile devices (analysing metadata, geolocation, file creation/modification histories) and flagging items for closer human examination.
- AI systems assessing the **reliability of human-source evidence** — internal consistency of statements, coherence with verified facts, accuracy of informant/witness reporting across cases.

**Nr. 6(d) — Offending/reoffending risk**
- AI systems used during the **initial processing of detained suspects** (including youth) to calculate a reoffending risk score informing measures, alongside other information and human final decision.
- AI systems used by **probation officers** to support parole or conditional-release decisions, evaluating criminal record, in-custody behaviour, and supervision-related data.
- AI systems used by **penitentiary institutions** to predict re-offending likelihood based on prior record, in-prison violence, or socio-economic data.
- AI-based **recidivism risk-assessment** systems used in criminal courts to estimate the likelihood of recidivism or violent reoffending.

**Nr. 6(e) — Profiling in criminal investigations**
- AI systems assisting in **identifying potential suspects** in a missing-child case by analysing the neighbourhood, persons on the sex-offenders' registry, their movements, and prior victim profiles.
- AI systems generating suspect leads from **witness descriptions and personal data**.
- AI systems performing **targeted online monitoring** classifying users via sentiment analysis, posting patterns, and networks for potential extremist affiliation (not amounting to social scoring under Art. 5(1)(c) where limited to targeted radicalisation monitoring in specific contexts).

## Practical examples — NOT HIGH-RISK

- **Administrative AI systems for LE** — case management, accounting, equipment management, patrol shift scheduling, chatbots on police websites providing general information (¶372). Purely ancillary administrative activities.
- **Automated number-plate readers (ANPR)** identifying concrete vehicles — vehicle-focused, not person-focused; not biometrics under point 1 and no profiling under point 6.
- **Road-safety enforcement AI** — speeding cameras, red-light running, helmet detection, smartphone-while-driving detection.
- **Object detection** — weapons, suspicious parcels, dangerous objects, stolen goods including cultural objects.
- **Behaviour/movement detection** in video feeds (running, raised arms, fighting stance) that does not identify persons.
- **Gunshot detection** systems based on sound analysis, not persons.
- **Customs consignment risk-management** systems checking goods compliance with EU legislation (container number, routing, payment method) — administrative, not law enforcement.
- **Location-focused predictive crime mapping** without individual profiling (e.g. burglary risk in a neighbourhood without linking the prediction to identifiable individuals).
- **Image enhancement, data recovery, crime-scene reconstruction** — assist human experts without evaluating evidence reliability (outside Nr. 6(c)).
- **Pattern-detection systems** flagging similar break-in methods or similar victim profiles across cases without evaluating evidence reliability.
- **CSAM detection/screening** systems that identify, flag, and classify content (new material vs. registered vs. deepfake) without evaluating evidence reliability — though they may still be high-risk under another Annex III area such as Nr. 6(a).
- **Ballistic-matching** systems comparing bullet markings against a reference database — file handling/database search, not reliability evaluation.
- **Police-officer fatigue/stress monitoring** for occupational health and safety (outside Nr. 6(b) and outside Art. 5(1)(f) by virtue of the medical/safety exclusion).
- **Money-laundering/terrorist-financing transaction monitoring** focused purely on structural/quantitative transaction data without enrichment by personal profiles (becomes high-risk if combined with personal data to construct individual profiles).
- **Crime-linkage systems** producing crime-link hypotheses and alerts across incidents using modus operandi data — outputs not tied to a particular individual.

## Boundary with Art. 5 prohibitions

- **Art. 5(1)(d) — Predictive policing solely on profiling/personality**: AI systems assessing or predicting the risk of a natural person committing a criminal offence based **solely** on profiling per LED Art. 3(4) or on the assessment of personality traits/characteristics → **PROHIBITED**. Annex III Nr. 6(d) covers the "not solely based on profiling" variants where the assessment is supported by objective and verifiable facts directly linked to a criminal activity (e.g. reasonable suspicion already exists; the person is already detained, convicted, or under supervision). See ¶367–¶368.
- **Art. 5(1)(f) — Emotion recognition in workplace/education**: prohibited in those settings; the law-enforcement context is generally outside this prohibition. Polygraph-type systems with emotion-recognition functionality (e.g. fear as a proxy for lie detection) may also fall under Annex III point 1(c) (biometrics) in addition to Nr. 6(b).
- **Art. 5(1)(g) — Biometric categorisation by sensitive attributes** (race, religion, political opinion, sexual orientation, etc.) → **PROHIBITED**.
- **Art. 5(1)(h) — Real-time remote biometric identification in publicly accessible spaces for LE** → **PROHIBITED** unless one of the narrow exceptions applies (targeted search for victims of specific offences, prevention of specific substantial threats, location/identification of suspects of certain serious offences). Where an exception applies, or where the RBI is **post-event**, Annex III Nr. 1(a) (biometrics) governs and the system is high-risk; Art. 26(10) AI Act sets the authorisation regime for post-event RBI use by LE.

## Common Art. 6(3) exception scenarios

Art. 6(3) exceptions are **almost universally unavailable** in Area 6 because of the profiling re-exception in Art. 6(3) last paragraph (any system performing profiling of natural persons is always high-risk):

- **Nr. 6(a), 6(d), 6(e)** — by definition involve risk assessment or profiling of natural persons; the profiling re-exception always bites.
- **Nr. 6(b)** — polygraphs/similar play a decision-making role on truthfulness with profiling characteristics; ¶362 confirms the exemptions in Art. 6(3) do not apply.
- **Nr. 6(c)** — narrow exceptions can apply where an AI system performs **purely procedural or preparatory tasks** in the evidence-evaluation workflow that do not themselves impact the assessment of reliability. Guidelines examples (¶365 c) include: systems that classify documents, pictures, videos selected for authenticity analysis into categories without affecting reliability assessment (Art. 6(3)(a) — narrow procedural task); and systems indexing/tagging financial documents collected for evidence-reliability evaluation (Art. 6(3)(a) and (d) — narrow procedural / preparatory task).
- **Nr. 6(d)** — preparatory-task exemptions can apply for systems that check completeness of risk-assessment forms, flag entry-data inconsistencies (Art. 6(3)(a) and/or (d)), or collect and pre-sort prior convictions, probation reports, and other records to prepare a case file for human officers (Art. 6(3)(d) — preparatory task).
- **Nr. 6(f)** — crime analytics that surface patterns/relationships without profiling individuals may avoid the profiling re-exception; whether any Art. 6(3) limb applies depends on the specific narrow-procedural / preparatory / detection-of-deviation analysis.

## Common profiling considerations

**Profiling per LED Art. 3(4)** = any form of automated processing of personal data consisting of the use of personal data to evaluate certain personal aspects relating to a natural person, in particular to analyse or predict aspects concerning that person's performance, economic situation, health, personal preferences, interests, reliability, behaviour, location or movements.

- Most LE use cases in Area 6 involve profiling — it is essentially the definitional purpose of sub-categories 6(a), 6(d) and 6(e).
- **Group-level analysis without personal data is not profiling** (¶354). A system analysing aggregate statistics or geographic/density data without applying its conclusions to individuals does not profile. But the moment the profile is applied to an individual, profiling occurs.
- **Location/area predictions are not profiling** when they do not single out identifiable persons (¶355). Predicting risk areas during mass events from geographic/density data alone is outside Area 6. But adding emotion-recognition capabilities (anger, aggressiveness) would bring the system under Annex III point 1(c).
- Where profiling is performed by the AI system, the **profiling re-exception in Art. 6(3) last paragraph** applies and blocks any Art. 6(3) exemption — the system is high-risk by virtue of profiling alone.

## Cross-references

- [art-6-3-exception-decision-tree.md](art-6-3-exception-decision-tree.md) — the four Art. 6(3) limbs and the profiling re-exception.
- [annex-iii-area-1-biometrics.md](annex-iii-area-1-biometrics.md) — overlap with biometrics use cases (point 1) where polygraph/emotion-recognition functions are present or post-event RBI is used.
- Related follow-on activities: **role determination**, **obligation mapping**, and **article-level Q&A** over the AI Act and Commission guidelines.
- AI Act **Art. 5(1)(d)** — predictive policing prohibition (sole-basis profiling / personality assessment).
- AI Act **Art. 5(1)(f)** — emotion recognition in workplace/education prohibition.
- AI Act **Art. 5(1)(g)** — biometric categorisation by sensitive attributes prohibition.
- AI Act **Art. 5(1)(h)** — real-time RBI in publicly accessible spaces for LE prohibition (with narrow exceptions).
- AI Act **Art. 2(3)** — national security exclusion.
- AI Act **Art. 3(45)** — definition of "law enforcement authority".
- AI Act **Art. 26(10)** — authorisation regime for post-event RBI use by LE.
- AI Act **Recital 59** — rationale for high-risk classification of LE use cases.
- **Directive (EU) 2016/680** (Law Enforcement Directive, "LED") — Art. 3(4) profiling definition; Art. 3(7) competent-authority definition (mirrored in AI Act Art. 3(45)).
- **Directive 2012/29/EU** (Victims' Rights Directive) — Art. 2(1)(a) victim definition (retrospective; AI Act point 6(a) is forward-looking).
- **Directive (EU) 2024/1385** — combating violence against women and domestic violence (victim definition for gender-based violence).
