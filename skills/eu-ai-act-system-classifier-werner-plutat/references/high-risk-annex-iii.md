# High-Risk AI Systems — Annex III Categories

## Table of Contents

1. [Biometrics](#1-biometric-identification-and-categorisation)
2. [Critical Infrastructure](#2-critical-infrastructure)
3. [Education](#3-education-and-vocational-training)
4. [Employment](#4-employment-workers-management-and-access-to-self-employment)
5. [Essential Services](#5-essential-private-and-public-services)
6. [Law Enforcement](#6-law-enforcement)
7. [Migration & Border Control](#7-migration-asylum-and-border-control)
8. [Justice & Democracy](#8-administration-of-justice-and-democratic-processes)
9. [Annex I — Regulated Products](#9-annex-i--regulated-products-and-safety-components)
10. [Article 6(3) Exception](#10-article-63-exception--when-annex-iii-systems-are-not-high-risk)
11. [Classification Methodology](#11-classification-methodology)

---

## 1. Biometric Identification and Categorisation

**Annex III, point 1**

High-risk AI systems under point 1 (in so far as their use is permitted under relevant Union or national law):
- **(a) Remote biometric identification systems.** The point expressly states this "shall not include AI systems intended to be used for biometric verification the sole purpose of which is to confirm that a specific natural person is the person he or she claims to be." One-to-one verification is therefore NOT Annex III high-risk.
- **(b) Biometric categorisation** according to sensitive or protected attributes or characteristics based on the inference of those attributes
- **(c) Emotion recognition** systems

**Examples:**
- Post-event identification of suspects from CCTV recordings for criminal investigation (remote identification)
- Identifying an unknown person in a crowd against a watchlist
- Categorising people by inferred ethnicity or political views from biometric data
- Emotion recognition outside the prohibited workplace and education contexts

**Edge cases:**
- **Airport e-gate facial verification (1:1 match against passport)** → biometric verification of a claimed identity, expressly excluded from point 1(a). Check the Annex I path instead if it sits in a regulated product, and Art. 50 transparency.
- **Biometric access control** (device unlock, secure-facility entry) → 1:1 verification, excluded from point 1(a)
- Voice biometrics confirming a caller is who they claim to be → verification, excluded; identifying an unknown speaker against many profiles → remote identification, in scope
- Age estimation without identifying anyone → not point 1(a); assess under point 1(b) only if it infers protected attributes

**Boundary with Article 5:** Real-time remote biometric identification in publicly accessible spaces for law enforcement is *prohibited* (Article 5), not merely high-risk. Post (ex-post) processing and non-law-enforcement uses fall here.

---

## 2. Critical Infrastructure

**Annex III, point 2**

High-risk AI systems intended to be used as safety components in the management and operation of the domains point 2 exhaustively lists:
- **critical digital infrastructure**
- **road traffic**
- **the supply of water, gas, heating or electricity**

Telecommunications generally, transport modes other than road traffic, and "other critical infrastructure" are NOT in the list. Point 2 is exhaustive; do not extend it by analogy or by a service-continuity argument.

**Examples:**
- AI controlling electricity grid load balancing and fault response
- Water treatment plant process optimisation with safety implications
- Traffic signal optimisation systems affecting pedestrian and vehicle safety
- Safety components in the operation of critical digital infrastructure (for example data-centre or core-network safety systems qualifying as critical digital infrastructure)

**Edge cases:**
- **Business analytics** on infrastructure data (demand forecasting for planning) → not high-risk unless it drives operational safety decisions
- **Customer-facing energy apps** (usage monitoring, billing) → generally not high-risk
- **Predictive maintenance** → high-risk if failure to predict correctly creates safety risk; lower risk if it merely optimises scheduling
- **Smart building systems** → depends on whether the AI is a safety component (fire systems, HVAC in hospitals) vs. convenience feature

**Key question:** Is the AI system a safety component in the management and operation of one of the exhaustively listed domains: critical digital infrastructure, road traffic, or the supply of water, gas, heating or electricity?

---

## 3. Education and Vocational Training

**Annex III, point 3**

High-risk AI systems intended for:
- Determining access to or admission to educational institutions
- Evaluating learning outcomes, including to steer the learning process
- Assessing the appropriate level of education for an individual
- Monitoring and detecting prohibited behaviour of students during tests

**Examples:**
- University admissions scoring/ranking algorithms
- Automated essay grading used for official marks
- AI determining whether a student should be placed in advanced or remedial tracks
- Proctoring software detecting cheating (beyond emotion recognition, which may be prohibited)

**Edge cases:**
- **Adaptive learning platforms** that adjust difficulty → high-risk if outcomes determine educational progression; lower if purely supplementary
- **Language learning apps** (Duolingo-style) → generally not high-risk if they don't determine access to formal education
- **Plagiarism detection** → high-risk if results directly lead to disciplinary decisions; lower if merely flagging for human review
- **Internal practice quizzes** with no impact on grades → not high-risk

**Key question:** Does the AI materially determine or influence access to education, grades, or progression?

---

## 4. Employment, Workers Management, and Access to Self-Employment

**Annex III, point 4**

High-risk AI systems intended for:
- Recruitment and selection (CV screening, candidate ranking, interview assessment)
- Decisions on promotion, termination, task allocation, monitoring, or evaluation of contractual relationships
- Performance evaluation
- Decisions on access to self-employment opportunities

**Examples:**
- CV screening and candidate shortlisting tools
- AI-assisted interview scoring (video analysis, response evaluation)
- Algorithmic task allocation in gig economy platforms
- Workforce analytics determining promotion eligibility
- Automated performance ratings based on productivity metrics

**Edge cases:**
- **Job board matching** (suggesting relevant postings) → generally not high-risk if it doesn't determine access
- **Meeting scheduling assistants** → not high-risk
- **Workforce planning models** (aggregate headcount forecasting) → not high-risk unless they drive individual decisions
- **Time tracking tools** with simple clock-in/out → not high-risk; becomes high-risk if tracking feeds into automated performance evaluation

**DACH note:** In Germany, virtually all systems in this category trigger works council co-determination under BetrVG §87(1) no. 6 and potentially §95. See [dach-specific.md](dach-specific.md).

**Key question:** Does the AI influence decisions about individual workers' hiring, evaluation, progression, or working conditions?

---

## 5. Essential Private and Public Services

**Annex III, point 5**

High-risk AI systems under point 5:
- **(a)** used by or on behalf of **public authorities** to evaluate eligibility for essential public assistance benefits and services, including healthcare, and to grant, reduce, revoke or reclaim them
- **(b)** to evaluate the **creditworthiness** of natural persons or establish their credit score, "with the exception of AI systems used for the purpose of detecting financial fraud"
- **(c)** for **risk assessment and pricing** in relation to natural persons in the case of **life and health insurance**
- **(d)** to evaluate and classify **emergency calls** or to dispatch, or establish priority in dispatching, emergency first response services and emergency healthcare patient triage

Housing is NOT an Annex III point 5 category. The list is exhaustive.

**Examples:**
- Bank credit scoring algorithms determining loan approval
- Insurance risk models pricing life or health coverage
- Welfare benefits eligibility assessment systems used by or on behalf of public authorities
- Emergency call centre AI triaging calls by severity

**Edge cases:**
- **Fraud detection in financial services** → expressly excluded from point 5(b). A system whose purpose is detecting financial fraud is not high-risk under this point, whatever its side effects on the customer
- **Housing or rental allocation** → not listed in point 5. If a public authority allocates social housing as an essential public assistance benefit, assess under point 5(a) on that statutory basis, not under a general housing category
- **Marketing offers** (pre-approved credit card offers) → generally not high-risk if no actual creditworthiness decision
- **Insurance pricing for non-life/non-health** (for example travel or motor insurance) → not listed in point 5(c). The annex is exhaustive; do not extend it by analogy
- **Customer service chatbots** for banks/insurers → not high-risk unless they make or materially influence eligibility decisions

**DACH note:** Credit scoring in Germany has additional SCHUFA/creditworthiness regulatory overlay. BaFin expects model risk management documentation for AI in financial services. See [dach-specific.md](dach-specific.md).

**Key question:** Does the AI fall within one of the four listed point 5 activities: public-benefit eligibility decisions, creditworthiness (outside fraud detection), life and health insurance pricing, or emergency call handling and triage?

---

## 6. Law Enforcement

**Annex III, point 6**

High-risk AI systems intended for use by law enforcement authorities for:
- Individual risk assessments (assessing risk of offending or re-offending)
- Polygraphs and similar tools
- Evaluation of reliability of evidence
- Predicting occurrence or reoccurrence of criminal offences based on profiling (non-prohibited forms)
- Profiling in the course of detection, investigation, or prosecution

**Examples:**
- Recidivism risk scoring tools used in sentencing or parole decisions
- AI-assisted evidence analysis and pattern recognition in investigations
- Deception detection systems (voice stress analysis, micro-expression analysis)
- Crime pattern analysis that profiles individuals (non-prohibited forms)

**Edge cases:**
- **Prohibited vs. high-risk boundary:** Individual predictive policing based *solely* on profiling is prohibited (Article 5). Investigation support using objective case facts may be high-risk but not prohibited.
- **Forensic tools** (DNA matching, fingerprint analysis) → high-risk if AI-driven with material influence on outcomes
- **Body camera footage analysis** → depends on whether it identifies individuals or merely catalogues events

**Key question:** Is the AI system used by law enforcement in a way that affects individual rights, liberty, or criminal justice outcomes?

---

## 7. Migration, Asylum, and Border Control

**Annex III, point 7**

High-risk AI systems under point 7 (in so far as their use is permitted under relevant Union or national law), intended for use by or on behalf of competent public authorities or Union institutions, bodies, offices or agencies:
- **(a)** as polygraphs or similar tools
- **(b)** to assess a risk, including a security risk, a risk of irregular migration, or a health risk, posed by a person intending to enter or having entered a Member State
- **(c)** to assist in the examination of applications for asylum, visa or residence permits and associated complaints, including related assessments of the reliability of evidence
- **(d)** for detecting, recognising or identifying natural persons in the context of migration, asylum or border control management, "with the exception of the verification of travel documents"

**Examples:**
- Border risk profiling systems flagging travellers for secondary inspection
- AI assessing credibility of asylum seekers' narratives and evidence in an application procedure
- AI identifying undocumented persons from biometric or other data in a border context

**Edge cases on document checks:**
- **Verification of travel documents** (checking a passport is authentic and belongs to the holder) → expressly excluded from point 7(d)
- **Automated document verification for visa processing** → the point 7(d) exclusion covers travel-document verification; a system that goes further and assesses the applicant's eligibility or the reliability of supporting evidence belongs under point 7(c)

**Edge cases:**
- **Automated passport gates** (document + face match confirming the holder is who they claim to be) → travel-document verification excluded from point 7(d), and 1:1 biometric verification excluded from point 1(a); not Annex III high-risk on either limb
- **Queue management systems** at borders → not high-risk if purely logistical
- **Translation tools** for asylum interviews → not high-risk if they don't influence the decision

**Key question:** Does the AI affect decisions about an individual's entry, asylum status, or migration-related rights?

---

## 8. Administration of Justice and Democratic Processes

**Annex III, point 8**

High-risk AI systems intended for:
- Assisting judicial authorities in researching and interpreting facts and law
- Assisting judicial authorities in applying the law to facts
- Assisting in alternative dispute resolution
- Influencing the outcome of elections or referendums (not tools for organisational/logistics)

**Examples:**
- AI legal research tools recommending case outcomes to judges
- Sentencing recommendation algorithms
- AI-mediated online dispute resolution platforms
- Voter targeting systems that go beyond standard political advertising
- AI generating personalised political messaging at scale

**Edge cases:**
- **Legal research tools** (case law search, citation analysis) → high-risk if they recommend outcomes; lower if they merely retrieve and organise information
- **Court scheduling systems** → not high-risk (organisational)
- **Election logistics** (polling station management, vote counting verification) → not high-risk as organisational tools
- **Social media recommendation algorithms** during elections → assess whether they cross into actively influencing electoral outcomes vs. neutral content delivery

**Key question:** Does the AI materially influence judicial decisions, dispute outcomes, or democratic processes?

---

## 9. Annex I — Regulated Products and Safety Components

Separate from Annex III. A system is high-risk under Annex I if:
1. It is a product OR a safety component of a product
2. The product is covered by EU harmonisation legislation listed in Annex I
3. The product is subject to third-party conformity assessment under that legislation

**Which Section the legislation sits in decides which regime applies.** Section A carries the
full Chapter III high-risk regime. For Section B products, the amended Article 2(2) limits the
AI Act to Article 6(1), the new Article 60a and Articles 102 to 112, with Articles 57 to 59
applying only in so far as the high-risk requirements have been integrated into that sectoral
legislation. Check the Section before drawing any obligation from an Annex I match.

**Section A (New Legislative Framework, full Chapter III regime):**
- Medical Devices Regulation (MDR), Regulation (EU) 2017/745
- In Vitro Diagnostic Medical Devices Regulation (IVDR), Regulation (EU) 2017/746
- Toy Safety Directive 2009/48/EC
- Lifts Directive 2014/33/EU, ATEX Directive 2014/34/EU, Pressure Equipment Directive 2014/68/EU
- Radio Equipment Directive 2014/53/EU
- Recreational craft, cableways, PPE, gas appliances

**Section B (sectoral route, limited Article 2(2) application):**
- Machinery Regulation (EU) 2023/1230. **Moved here with effect from 27 July 2026** by
  Regulation (EU) 2026/1744, which deleted the old machinery entry from Section A. AI-enabled
  machinery therefore no longer follows the full Chapter III route.
- Civil aviation, Regulation (EU) 2018/1139, and civil aviation security, Regulation (EC) No 300/2008
- Motor vehicles, Regulation (EU) 2018/858, and general vehicle safety, Regulation (EU) 2019/2144
- Two- and three-wheel vehicles, agricultural and forestry vehicles, marine equipment,
  rail interoperability

**Examples, with the Section that governs them:**
- AI-powered diagnostic tool in a Class IIa+ medical device, MDR conformity assessment.
  **Section A**, full regime.
- Machine vision system in industrial machinery with a safety function. **Section B since
  27 July 2026**, so the sectoral route under Article 2(2), not the full Chapter III set.
- AI-based flight management component in aviation. **Section B.**
- Autonomous driving features in motor vehicles. **Section B.**

**Practical questions:**
- Which product regulatory regime applies, and is it Annex I Section A or Section B?
- Is the AI a safety component within the amended Article 3(14), meaning its **intended purpose**
  is to prevent or mitigate risks to health and safety of persons or property? Integration into a
  regulated product is not enough on its own.
- Does Article 6(1a) exclude it, because it is used solely for non-safety related user assistance,
  performance optimisation, service efficiency, automation, convenience or quality control? Does
  Article 6(1b) pull it back in, because failure or malfunctioning would endanger health and safety?
- Is the third-party conformity assessment required **solely** for risks other than health and
  safety, for example radio spectrum or electromagnetic interference? Article 6(1c) then means
  Article 6(1)(b) is not satisfied. This matters in particular for the Radio Equipment Directive.
- Which conformity assessment route applies, and is it third-party?

---

## 10. Article 6(3) Exception — When Annex III Systems Are NOT High-Risk

Even if an Annex III use case matches, the system is **not** high-risk if it:

1. Performs a **narrow procedural task**, OR
2. **Improves the result** of a previously completed human activity, OR
3. Detects **decision-making patterns or deviations from prior decision-making patterns** and is not meant to replace or influence the previously completed human assessment **without proper human review**, OR
4. Performs a **preparatory task** for an assessment listed in Annex III

**AND** the AI system does not pose a significant risk of harm to health, safety, or fundamental rights, including by not materially influencing the outcome of decision making.

**Profiling override, check this FIRST:** Art. 6(3), third subparagraph: "Notwithstanding the first subparagraph, an AI system referred to in Annex III shall always be considered to be high-risk where the AI system performs profiling of natural persons." A profiling system never gets the exception, whichever condition it would otherwise meet.

**Examples where the exception might apply:**
- Spell-checking and formatting tool for judicial documents (narrow procedural task)
- AI suggesting synonyms in a CV (improving prior human work)
- Dashboard visualising hiring trends without recommending candidates (detecting patterns)
- Document pre-sorting before human credit assessment (preparatory task)

**Caution:** This exception must be documented thoroughly. If the system is close to the boundary, the safer classification is high-risk. The provider must document the reasons why the exception applies (Article 6(4)).

---

## 11. Classification Methodology

For each system under assessment:

1. **Map the intended purpose** precisely — classification turns on intended use, not general technical capability
2. **Check all eight Annex III categories** — a system may fall under multiple categories
3. **For each potential match**, assess whether the AI makes or *materially influences* decisions in that domain
4. **Apply the Article 6(3) exception** only if clearly justified — document reasoning
5. **Check Annex I** separately for product/safety component status
6. **If high-risk under multiple categories**, comply with the union of all applicable obligations (the requirements are the same but documentation should address each use case)
7. **If borderline**, classify as high-risk — the cost of compliance is lower than the cost of getting it wrong (€15M or 3%)
