# High-Risk AI Classification — Annex I & Annex III

## Two Paths to High-Risk Classification (Art. 6)

### Path A: Product Safety — Art. 6(1) + Annex I

An AI system is high-risk if:
1. It is intended to be used as a **safety component** of a product, OR it is itself a product, covered by the EU harmonization legislation listed in Annex I, AND
2. The product or safety component requires a **third-party conformity assessment** under that legislation

### Path B: Application-Based — Art. 6(2) + Annex III

An AI system is high-risk if it falls within one of the **8 use-case areas** listed in Annex III (subject to Art. 6(3) exception).

---

## Annex I — EU Harmonization Legislation (Product Safety)

### Full List of 18 Product Categories

| Nr. | Product Category (DE) | Product Category (EN) | EU Legislation Reference |
|-----|----------------------|----------------------|--------------------------|
| 1 | Maschinen | Machinery | Regulation (EU) 2023/1230 |
| 2 | Spielzeug | Toys | Directive 2009/48/EC |
| 3 | Sportboote und Wassermotorräder | Recreational craft and personal watercraft | Directive 2013/53/EU |
| 4 | Aufzüge | Lifts | Directive 2014/33/EU |
| 5 | Geräte und Schutzsysteme für explosionsgefährdete Bereiche | Equipment for explosive atmospheres (ATEX) | Directive 2014/34/EU |
| 6 | Funkanlagen | Radio equipment | Directive 2014/53/EU |
| 7 | Druckgeräte | Pressure equipment | Directive 2014/68/EU |
| 8 | Seilbahnen | Cableway installations | Regulation (EU) 2016/424 |
| 9 | Persönliche Schutzausrüstungen | Personal protective equipment (PPE) | Regulation (EU) 2016/425 |
| 10 | Geräte zur Verbrennung gasförmiger Brennstoffe | Appliances burning gaseous fuels | Regulation (EU) 2016/426 |
| 11 | Medizinprodukte | Medical devices | Regulation (EU) 2017/745 |
| 12 | In-vitro-Diagnostika | In vitro diagnostic medical devices | Regulation (EU) 2017/746 |
| 13 | Zivile Luftfahrt | Civil aviation | Regulation (EU) 2018/1139 |
| 14 | Zwei-, drei- und vierrädrige Fahrzeuge | Two- or three-wheel vehicles and quadricycles | Regulation (EU) No 168/2013 |
| 15 | Land- und forstwirtschaftliche Fahrzeuge | Agricultural and forestry vehicles | Regulation (EU) No 167/2013 |
| 16 | Schiffsausrüstung | Marine equipment | Directive 2014/90/EU |
| 17 | Interoperabilität des Eisenbahnsystems | Railway system interoperability | Directive (EU) 2016/797 |
| 18 | Kraftfahrzeuge und Kraftfahrzeuganhänger | Motor vehicles and trailers | Regulation (EU) 2018/858 |

### Annex I Assessment Questions

For each product category, ask:
1. Is the AI system a **safety component** of a product covered by this legislation?
2. Is the AI system **itself a product** covered by this legislation?
3. Does the product require **third-party conformity assessment** under the relevant legislation?

If YES to (1 or 2) AND YES to (3) → **High-risk under Art. 6(1)**

**Examples:**
- AI-based collision avoidance in autonomous vehicle → Annex I Nr. 18 (motor vehicles)
- AI diagnostic algorithm in medical imaging device → Annex I Nr. 11 (medical devices)
- AI controller in industrial robot → Annex I Nr. 1 (machinery)
- AI-powered toy with adaptive behavior → Annex I Nr. 2 (toys)

---

## Annex III — High-Risk AI Application Areas

### Category 1: Biometrics (Biometrie)

**Annex III Nr. 1**

**(a) Remote biometric identification systems (biometrische Fernidentifizierung)**
- One-to-many biometric comparison
- Includes facial recognition, gait recognition, voice identification
- Excludes verification (one-to-one comparison for identity confirmation)
- Note: Real-time RBI in public for law enforcement is prohibited under Art. 5(1)(h)

**(b) Biometric categorization (biometrische Kategorisierung)**
- AI systems categorizing persons based on biometric data
- Assigning to specific categories (age, gender, ethnicity, etc.)
- Note: Categorization for sensitive characteristics (race, religion, etc.) is prohibited under Art. 5(1)(g)

**(c) Emotion recognition (Emotionserkennung)**
- AI systems inferring emotions from biometric data
- Note: In workplace and education contexts, this is prohibited under Art. 5(1)(f)
- High-risk when used in other contexts (e.g., border control, law enforcement)

**Recitals:** 53-55

#### Edge Cases & Boundaries

| IN (high-risk) | OUT (not high-risk) | Reasoning |
|----------------|---------------------|-----------|
| Post-event facial recognition from CCTV for suspect identification | Facial detection without identification (counting faces in a crowd) | Identification (matching to database) vs. detection (no matching) |
| Biometric age estimation to restrict access (e.g., online age verification) | Simple age-gate checkbox with no biometric processing | Biometric data processing vs. self-declaration |
| Voice identification matching caller to speaker database | Voice-controlled home assistant recognizing registered user profiles (verification, not identification) | One-to-many identification vs. one-to-one verification |
| Emotion recognition at border control | Sentiment analysis of text reviews (no biometric data) | Biometric data vs. text data — Art. 3(40) defines biometric data as physical/physiological/behavioral characteristics |

#### Cross-Jurisdiction Notes

- **DE:** Any biometric system in the workplace may additionally trigger BetrVG §87(1) Nr. 6 (works council co-determination for monitoring devices), even if the biometric use is not the primary purpose
- **FR:** CNIL position (2022) on facial recognition: strict proportionality test applies beyond AI Act requirements; CNIL pre-consultation recommended for biometric systems
- **IT:** Garante has issued specific enforcement decisions against biometric systems (Clearview AI, facial recognition in retail) — Italian enforcement tends to be early and aggressive
- **NL:** AP (Autoriteit Persoonsgegevens) SyRI ruling established precedent on governmental algorithmic profiling — biometric systems in government services face heightened scrutiny

#### Art. 6(3) Exception Applicability

**Rarely applicable.** Remote biometric identification, categorization, and emotion recognition are by nature substantive assessment tools — they typically *replace or influence* human assessment of identity or emotional state. The Art. 6(3) exception (narrow procedural task, complementary to human activity) almost never applies to biometric AI.

**Exception scenario:** A biometric system that merely sorts photos by objective physical attributes (height range, hair color) to narrow a search for human review — without identifying, categorizing by sensitive traits, or inferring emotions — might qualify under Art. 6(3)(a) as a "narrow procedural task."

---

### Category 2: Critical Infrastructure (Kritische Infrastrukturen)

**Annex III Nr. 2**

AI systems intended to be used as safety components in the management and operation of:
- **Critical digital infrastructure** (telecommunications, cloud, data centers)
- **Road traffic** (traffic management, autonomous driving support)
- **Water supply** (treatment and distribution)
- **Gas supply** (distribution networks)
- **Heating supply** (district heating)
- **Electricity supply** (grid management, smart grid)

**Key test:** The AI system must be a **safety component** — i.e., its failure or malfunction could endanger health, safety, or cause significant disruption.

**Recitals:** 55-56

#### Edge Cases & Boundaries

| IN (high-risk) | OUT (not high-risk) | Reasoning |
|----------------|---------------------|-----------|
| AI load balancing in electricity grid to prevent blackouts | AI optimizing energy billing for individual customers | Safety component (grid stability) vs. commercial function (billing) |
| AI traffic signal optimization affecting vehicle flow and pedestrian safety | AI route planning app suggesting fastest route to individual user | Infrastructure management (safety) vs. consumer advisory (convenience) |
| AI monitoring water treatment plant for contamination detection | AI chatbot answering customer questions about water quality | Safety component (contamination detection) vs. information service (Q&A) |
| AI managing telecommunications network failover during emergencies | AI-powered spell-check in telecom company's customer email system | Critical function (network continuity) vs. non-critical function (text editing) |

#### Cross-Jurisdiction Notes

- **DE:** KRITIS-Verordnung (BSI-KritisV) defines critical infrastructure operators with specific thresholds (e.g., 500,000+ supplied persons for energy). AI safety components in KRITIS-designated entities face both AI Act and BSI requirements. See [references/jurisdiction-requirements.md] Section 6
- **FR:** ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information) oversees critical infrastructure cybersecurity; AI systems in OIV (Opérateurs d'Importance Vitale) face additional ANSSI requirements
- **NL:** Vital infrastructure designation under Wet beveiliging netwerk- en informatiesystemen — AI safety components in designated entities face dual requirements
- **All:** NIS2 transposition creates additional cybersecurity obligations for AI in critical infrastructure across all EU Member States

#### Art. 6(3) Exception Applicability

**Rarely applicable for true safety components.** If the AI system's failure could endanger health or safety, it is by definition performing a substantive safety function, not a "narrow procedural task." The exception might apply to non-safety AI within critical infrastructure (e.g., AI scheduling maintenance teams — procedural, not safety-critical).

#### Sector-Specific Considerations

- **Energy sector:** ENTSO-E network codes may impose additional grid stability requirements on AI-managed systems
- **Transport:** AI in connected/automated vehicles faces Annex I Nr. 18 (product safety) AND potentially Annex III Nr. 2 (infrastructure safety component) dual classification
- **Telecom:** EECC (European Electronic Communications Code) may impose additional requirements on AI in network management

---

### Category 3: Education and Vocational Training (Bildung und Berufsausbildung)

**Annex III Nr. 3**

**(a) Access and admission determination:**
- AI systems determining access to or admission into educational institutions
- Distributing or allocating persons to educational institutions or programs

**(b) Student assessment:**
- AI systems evaluating learning outcomes
- Including systems that steer the learning process
- Determining level of education a person will receive

**(c) Monitoring and proctoring:**
- AI systems monitoring prohibited behavior during tests/examinations

**Recitals:** 56-57

#### Edge Cases & Boundaries

| IN (high-risk) | OUT (not high-risk) | Reasoning |
|----------------|---------------------|-----------|
| AI scoring university admissions applications | AI spell-checking a student's essay (without grading) | Decision on access vs. writing tool assistance |
| Adaptive learning platform determining which curriculum track a student follows | AI flashcard app adapting review frequency (spaced repetition) | Determines level of education received vs. optimizes study technique |
| AI exam proctoring monitoring for cheating during high-stakes test | AI organizing a student's study calendar | Monitoring prohibited behavior vs. organizational tool |
| AI evaluating learning outcomes for grade assignment | AI recommending supplementary reading materials | Assessment (grade) vs. recommendation (no decision weight) |
| AI system placing students into ability-grouped classes | AI-powered campus navigation app | Allocation of persons to programs vs. utility function |

#### Cross-Jurisdiction Notes

- **DE:** State education laws (Landesschulgesetze) vary across 16 Bundesländer — some states restrict automated grading beyond AI Act requirements. Data protection: school data processing subject to state data protection acts
- **FR:** Code de l'éducation provisions on equal access and non-discrimination — AI in education must be assessed against French educational equality principles (Baccalauréat reform context)
- **NL:** Dutch education inspection (Inspectie van het Onderwijs) may assess AI educational tools independently of AI Act market surveillance
- **IT:** Ministerial guidelines on digital technology in schools may impose additional transparency requirements for AI educational tools
- **ES:** Organic law on education (LOMLOE) provisions on equity and inclusion — AI systems affecting educational access must be assessed for compliance with Spanish inclusion requirements

#### Art. 6(3) Exception Applicability

**Sometimes applicable, but narrow:**

- Art. 6(3)(a) "narrow procedural task": AI system that formats exam questions or manages test logistics (seating, timing) without affecting assessment → likely qualifies
- Art. 6(3)(b) "improves result of previously completed human activity": AI system that checks a teacher's hand-graded exams for arithmetic errors → likely qualifies
- Art. 6(3)(c) "detects decision-making patterns without replacing/influencing": AI system analyzing grade distributions for bias detection (meta-analysis, not individual grading) → likely qualifies
- **Does NOT qualify:** Any AI system that directly determines grades, admissions, or track placement — these replace or materially influence human assessment

**Profiling re-exception:** If the educational AI performs profiling of students (e.g., learning profiles, aptitude assessment), Art. 6(3) exception does NOT apply regardless of other conditions.

---

### Category 4: Employment, Workers Management, Self-Employment Access (Beschäftigung, Arbeitnehmersteuerung, Zugang zur Selbstständigkeit)

**Annex III Nr. 4**

**(a) Recruitment and selection:**
- AI systems for placing targeted job advertisements
- Analyzing and filtering job applications
- Evaluating candidates in interviews or tests

**(b) Decisions on terms and conditions:**
- AI systems making or materially influencing decisions on:
  - Promotion
  - Termination of contractual relationship
  - Task allocation based on behavior/personal traits
  - Monitoring and evaluation of performance and behavior

**Recitals:** 57-58

#### Edge Cases & Boundaries

| IN (high-risk) | OUT (not high-risk) | Reasoning |
|----------------|---------------------|-----------|
| AI resume screening/CV scoring tool ranking applicants | AI-powered job board matching candidates with listings (no filtering, pure matching) | Filtering/evaluating candidates vs. displaying opportunities |
| AI video interview analysis scoring body language | AI scheduling interviews (choosing time slots) | Evaluation of candidate vs. administrative scheduling |
| AI performance monitoring scoring employees | AI helpdesk ticket routing assigning support requests | Evaluating behavior/performance vs. workload distribution (unless based on personal traits) |
| AI determining gig worker task allocation based on behavioral score | AI distributing tasks based on skill certification and availability (objective criteria) | Personal traits/behavior vs. objective qualifications |
| AI recommending which employees to promote | AI organizing training session registrations | Influencing promotion decisions vs. administrative function |
| AI-powered personality test for hiring | AI managing onboarding document checklist | Evaluating candidate traits vs. administrative process |

**Critical boundary — "materially influencing":** An AI system that provides a recommendation that a human decision-maker routinely follows is "materially influencing" even if a human formally makes the decision. Token human oversight does not remove high-risk classification.

#### Cross-Jurisdiction Notes

- **DE:** Works council co-determination (BetrVG §87(1) Nr. 6, §94, §95) applies to virtually all employment AI in companies with a works council — Betriebsvereinbarung required. See [references/jurisdiction-requirements.md] Section 3.1
- **AT:** ArbVG §96(1) Nr. 3 consent requirement for dignity-affecting systems — broader trigger than German law. See [references/jurisdiction-requirements.md] Section 3.2
- **FR:** CSE consultation required (L. 2312-38 Code du Travail) before introducing employment AI. Platform worker algorithmic transparency requirements (Loi du 21 juin 2023). See [references/jurisdiction-requirements.md] Section 3.4
- **NL:** Works council consent (Art. 27(1)(l) WOR) for monitoring systems. AP algorithmic accountability framework applies. See [references/jurisdiction-requirements.md] Section 3.5
- **IT:** Art. 4 Statuto dei Lavoratori requires trade union agreement or labor inspectorate authorization before deploying monitoring AI. D.Lgs. 104/2022 (Decreto Trasparenza) requires employee disclosure. See [references/jurisdiction-requirements.md] Section 3.6
- **ES:** RD-ley 9/2021 ("Ley Rider") requires algorithmic transparency for platform workers. ET Art. 64(4)(d) requires algorithm information to works council. See [references/jurisdiction-requirements.md] Section 3.7
- **CH:** OR Art. 328b limits employee data processing to employment suitability. nDSG Art. 21 provides automated decision-making protections. See [references/jurisdiction-requirements.md] Section 3.3

#### Art. 6(3) Exception Applicability

**Limited applicability:**

- Art. 6(3)(a) "narrow procedural task": AI formatting job postings or scheduling interviews → likely qualifies
- Art. 6(3)(b) "improves previously completed human activity": AI spell-checking a manager's performance review → likely qualifies
- Art. 6(3)(d) "preparatory task": AI system pre-sorting incoming applications by objective criteria (complete/incomplete documents) without evaluating content → may qualify
- **Does NOT qualify:** Any AI system that screens, scores, ranks, or evaluates candidates or employees — these influence assessment
- **Profiling re-exception:** Employment AI that profiles workers (behavioral patterns, personality analysis, performance prediction) cannot use Art. 6(3) regardless

**This is the most frequently triggered Annex III category in practice.** Most AI in HR/workforce management will be high-risk.

---

### Category 5: Access to Essential Private and Public Services (Zugang zu wesentlichen Dienstleistungen)

**Annex III Nr. 5**

**(a) Creditworthiness assessment (Kreditwürdigkeit):**
- AI systems evaluating creditworthiness of natural persons
- Excludes: detection of financial fraud
- Reference: Recitals 58-59

**(b) Insurance risk assessment:**
- AI systems for risk assessment and pricing in life and health insurance

**(c) Social benefits and services:**
- AI systems evaluating eligibility for public assistance benefits or services
- Including granting, reducing, revoking, or reclaiming such benefits

**(d) Emergency services dispatch:**
- AI systems dispatching or establishing priority in emergency first response services
  - Fire departments
  - Medical aid
  - Police/law enforcement

**Recitals:** 58-60

#### Edge Cases & Boundaries

| IN (high-risk) | OUT (not high-risk) | Reasoning |
|----------------|---------------------|-----------|
| AI credit scoring for bank lending decisions | AI fraud detection flagging suspicious transactions | Creditworthiness assessment vs. fraud detection (explicitly excluded) |
| AI determining life insurance premium based on risk assessment | AI calculating car insurance premium based on vehicle and driving data | Life/health insurance vs. non-life insurance (only life and health specifically covered) |
| AI evaluating social welfare benefit eligibility | AI chatbot answering FAQ about social benefit programs | Eligibility determination vs. information provision |
| AI triage system prioritizing 112/emergency calls | AI system managing non-emergency municipal service requests | Emergency dispatch (life-threatening) vs. routine service management |
| AI-based credit limit recommendation to bank officer | AI-based spending pattern analysis for customer financial wellness dashboard | Creditworthiness (lending decision input) vs. financial information service (no lending decision) |

**Important nuance — fraud detection carve-out:** Art. 5(a) explicitly excludes fraud detection from the creditworthiness category. However, if a fraud detection system's output materially influences creditworthiness decisions (e.g., fraud score used to deny credit), the boundary becomes gray.

#### Cross-Jurisdiction Notes

- **DE:** BaFin MaRisk requirements on AI model governance in credit decisions — dual compliance with AI Act and BaFin model risk management. See [references/jurisdiction-requirements.md] Section 4.1
- **AT:** FMA analogous expectations for Austrian banks and insurers
- **CH:** FINMA model governance requirements apply to Swiss financial institutions using AI; AI Act applies if outputs reach EU market. See [references/jurisdiction-requirements.md] Section 4.3
- **FR:** ACPR/AMF expectations on AI in French banking and insurance; Banque de France has published specific positions on AI credit scoring
- **NL:** DNB/AFM algorithmic accountability expectations — Netherlands has the most developed regulatory position on AI fairness in financial services among covered jurisdictions. See [references/jurisdiction-requirements.md] Section 4.5
- **IT:** Banca d'Italia Circular 285 on model risk; IVASS insurance governance requirements
- **ES:** BdE/CNMV positions on AI in financial services; AESIA coordination with financial regulators

#### Art. 6(3) Exception Applicability

**Narrow applicability:**

- Art. 6(3)(a) "narrow procedural task": AI system that merely calculates a debt-to-income ratio from provided figures (pure calculation, no assessment) → may qualify
- Art. 6(3)(d) "preparatory task": AI system checking completeness of loan application documents (no creditworthiness assessment) → may qualify
- **Does NOT qualify:** Any AI system that evaluates, scores, or assesses creditworthiness, insurance risk, or benefit eligibility — these are the exact decisions the category covers
- **Profiling re-exception:** Credit scoring and insurance risk assessment inherently involve profiling of natural persons → Art. 6(3) exception almost always excluded by the profiling re-exception

**Profiling note:** Customer profiling characteristics that may trigger this category:
- Fraud probability assessment (Betrugswahrscheinlichkeit)
- Behavior prediction (Verhaltensvorhersage)
- Credit worthiness scoring (Kreditwürdigkeit)
- Social rating (Soziale Einstufung)
- Emotion recognition (Emotionserkennung)
- Psychological or economic profiling

---

### Category 6: Law Enforcement (Strafverfolgung)

**Annex III Nr. 6**

**(a) Individual risk assessment:**
- AI systems assessing risk of a person becoming a victim of criminal offenses

**(b) Polygraph and similar tools:**
- AI systems used as polygraphs or similar tools to detect deception

**(c) Evidence reliability:**
- AI systems evaluating reliability of evidence in criminal investigations

**(d) Criminal offense risk assessment:**
- Assessing risk of offending or reoffending (not solely based on profiling — that's prohibited under Art. 5(1)(d))

**(e) Profiling in criminal investigation:**
- AI systems profiling persons during detection, investigation, or prosecution

**Recitals:** 60-61

#### Edge Cases & Boundaries

| IN (high-risk) | OUT (not high-risk) | Reasoning |
|----------------|---------------------|-----------|
| AI recidivism risk tool using criminal history + contextual factors | AI predicting crime based solely on profiling/personality (prohibited under Art. 5(1)(d)) | High-risk (factual basis) vs. prohibited (solely profiling) — critical boundary |
| AI analyzing digital forensic evidence for reliability assessment | AI managing case file documents (indexing, tagging without assessment) | Assessing evidence reliability vs. administrative document management |
| AI assisting with criminal profiling during active investigation | AI analyzing general crime statistics for policy planning (no individual profiling) | Individual profiling vs. aggregate analysis |
| AI polygraph analyzing physiological responses during interview | Standard digital recording equipment without analytical AI | AI deception detection vs. recording equipment |

#### Cross-Jurisdiction Notes

- **DE:** Police use of AI varies by state (Polizeigesetze der Länder); some states have specific provisions on predictive policing. Federal: BKA-Gesetz provisions on data analytics
- **FR:** CNIL has taken strong positions on police use of AI; French administrative courts have restricted some algorithmic policing tools
- **NL:** SyRI ruling (Rechtbank Den Haag, 2020) established precedent restricting governmental algorithmic profiling — landmark case with EU-wide influence
- **ES:** Organic law on citizen security (Ley Orgánica 4/2015) provisions interact with AI Act for law enforcement AI

#### Art. 6(3) Exception Applicability

**Very limited.** Law enforcement AI is generally used for substantive assessment (risk evaluation, evidence analysis, profiling) rather than narrow procedural tasks. The exception might apply to:
- AI system managing case numbering or filing (purely administrative)
- AI system transcribing interview recordings (preparatory, without assessment)

**Does NOT qualify:** Any AI system that assesses risk, evaluates evidence, detects deception, or profiles individuals.

---

### Category 7: Migration, Asylum, and Border Control (Migration, Asyl und Grenzkontrolle)

**Annex III Nr. 7**

**(a) Polygraph and similar tools:**
- AI systems as polygraphs for migration/asylum purposes

**(b) Risk assessment:**
- AI systems assessing risk (security, health, irregular migration) posed by persons seeking entry

**(c) Application examination:**
- AI systems assisting examination of applications for asylum, visa, or residence permits
- Including related complaints regarding eligibility

**(d) Detection:**
- AI systems for detecting, recognizing, or identifying persons in migration context
- Excluding verification of travel documents

**Recitals:** 61-62

#### Edge Cases & Boundaries

| IN (high-risk) | OUT (not high-risk) | Reasoning |
|----------------|---------------------|-----------|
| AI assessing asylum application credibility | AI translating asylum interview for interpreter (translation only) | Application assessment vs. language processing tool |
| AI detecting persons at border using biometric analysis | AI scanning passport MRZ zone for data entry (document verification) | Person detection/identification vs. document machine reading (explicitly excluded) |
| AI assessing health risk of arriving travelers (beyond basic screening) | Thermal camera detecting elevated body temperature without AI analysis | AI health risk assessment vs. simple sensor measurement |
| AI profiling travelers at airport for risk-based screening | AI managing queue flow at passport control (no person assessment) | Risk assessment of persons vs. operational logistics |

#### Cross-Jurisdiction Notes

- **DE:** BAMF (Bundesamt für Migration und Flüchtlinge) has already deployed AI tools for dialect recognition and document verification — these require AI Act assessment
- **FR:** OFPRA (Office Français de Protection des Réfugiés) use of AI in asylum procedures subject to French administrative law protections
- **IT:** High migration processing volume makes AI in migration context particularly prevalent; Garante has taken positions on biometric processing of migrants
- **ES:** Ministry of Interior AI use in border control (Southern border context) — significant volume
- **NL:** IND (Immigratie- en Naturalisatiedienst) use of AI in residence permit decisions — SyRI ruling principles apply

#### Art. 6(3) Exception Applicability

**Very limited.** Migration and border control AI typically makes or influences substantive assessments about persons.

- Possible exception: AI that verifies document format/completeness (purely procedural) without assessing content
- **Does NOT qualify:** Risk assessment, application examination, person detection — all substantive

---

### Category 8: Administration of Justice and Democratic Processes (Rechtspflege und demokratische Prozesse)

**Annex III Nr. 8**

**(a) Judicial assistance:**
- AI systems assisting judicial authorities in researching and interpreting facts and law
- AI systems applying law to concrete facts
- AI systems used in alternative dispute resolution

**(b) Electoral influence:**
- AI systems intended to influence outcome of elections or referendums
- AI systems intended to influence voting behavior
- Excludes: organizational/logistical election support (e.g., vote counting machines with basic software)

**Recitals:** 62

#### Edge Cases & Boundaries

| IN (high-risk) | OUT (not high-risk) | Reasoning |
|----------------|---------------------|-----------|
| AI legal research tool applying law to specific facts and recommending outcomes | General-purpose legal database search engine (keyword search, no analysis) | Applying law to facts (legal reasoning) vs. information retrieval |
| AI-assisted sentencing recommendation system | AI managing court docket scheduling | Legal assessment vs. administrative scheduling |
| AI-powered online dispute resolution platform making binding decisions | AI chatbot explaining general legal procedures to citizens | Dispute resolution (binding) vs. general information |
| AI-generated political campaign targeting voters based on predicted susceptibilities | AI managing voter registration data integrity (administrative) | Influencing voting behavior vs. administrative data management |
| AI system generating personalized political messaging to change voter preferences | AI summarizing candidate positions factually and neutrally | Influencing behavior vs. neutral information provision |

#### Cross-Jurisdiction Notes

- **DE:** Judicial independence (Art. 97 GG) creates unique constraints on AI in courts — AI must not compromise judicial independence; Länder court administrations have varying positions
- **FR:** Loi pour une République numérique (2016) already requires open data for judicial decisions but restricts profiling of judges — AI analyzing judicial decision patterns to predict outcomes of specific judges is restricted
- **IT:** Italian courts have specific positions on AI in judicial proceedings (Consiglio Superiore della Magistratura)
- **NL:** Dutch judiciary has engaged with AI cautiously; Rechtspraak (council for the judiciary) has published principles on AI use
- **ES:** CGPJ (Consejo General del Poder Judicial) has published ethics guidelines on AI in judiciary

#### Art. 6(3) Exception Applicability

**Narrow cases only:**

- Art. 6(3)(a) "narrow procedural task": AI managing court filing, docket scheduling, document formatting → qualifies
- Art. 6(3)(d) "preparatory task": AI organizing case documents, creating timeline of events (factual, no legal analysis) → may qualify
- **Does NOT qualify:** Any AI that researches law, applies law to facts, recommends outcomes, or assists in dispute resolution — these are substantive judicial functions
- **Electoral:** Art. 6(3) rarely applies — systems designed to influence elections or voting behavior are substantive by nature

---

## Annex III Assessment Checklist

```
ANNEX III HIGH-RISK SCREENING

| # | Category | Applicable? | Specific Sub-Category | Reasoning |
|---|----------|-------------|----------------------|-----------|
| 1 | Biometrics | [Yes/No] | [1a/1b/1c] | |
| 2 | Critical infrastructure | [Yes/No] | | |
| 3 | Education & vocational training | [Yes/No] | [3a/3b/3c] | |
| 4 | Employment & workers management | [Yes/No] | [4a/4b] | |
| 5 | Essential services access | [Yes/No] | [5a/5b/5c/5d] | |
| 6 | Law enforcement | [Yes/No] | [6a/6b/6c/6d/6e] | |
| 7 | Migration, asylum, border | [Yes/No] | [7a/7b/7c/7d] | |
| 8 | Justice & democratic processes | [Yes/No] | [8a/8b] | |

Annex III category triggered: [YES — Category X / NO]
→ If YES, proceed to Art. 6(3) exception analysis
```

---

## Art. 6(3) Exception Quick Reference

| Category | Exception Likelihood | Key Factor |
|----------|---------------------|------------|
| 1 — Biometrics | **Very Low** | Biometric systems inherently perform substantive assessment |
| 2 — Critical Infrastructure | **Very Low** | Safety components inherently perform substantive safety functions |
| 3 — Education | **Low-Medium** | Possible for administrative/formatting tools; not for assessment |
| 4 — Employment | **Low** | Most HR AI influences decisions; profiling re-exception often applies |
| 5 — Essential Services | **Very Low** | Profiling re-exception almost always applies for credit/insurance |
| 6 — Law Enforcement | **Very Low** | Assessment, profiling, and evidence analysis are substantive |
| 7 — Migration | **Very Low** | Person assessment and examination are substantive |
| 8 — Justice & Democracy | **Low** | Legal reasoning is substantive; admin tasks may qualify |

**Remember:** The Art. 6(3) exception does NOT apply if the system performs profiling of natural persons (Art. 4(4) GDPR definition), regardless of which condition (a)-(d) is otherwise met.

---

## Important Notes

1. **Delegated acts:** The Commission may adopt delegated acts to amend Annex III (Art. 7), adding or modifying high-risk categories. Always search for latest updates.
2. **Combination effects:** A system may trigger multiple Annex III categories simultaneously.
3. **Indirect triggering:** Even if the AI system is not directly used for a listed purpose, if its output materially contributes to a listed decision, it may be high-risk.
4. **GPAI integration:** A GPAI model integrated into a high-risk system makes the entire system high-risk; the GPAI model provider has obligations under Art. 53.
5. **National law expansion:** National employment, financial, and sector-specific laws may create additional requirements beyond the AI Act's high-risk obligations — always check jurisdiction-specific requirements via [references/jurisdiction-requirements.md].
