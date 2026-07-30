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

High-risk AI systems intended for:
- **Remote biometric identification** (not real-time in public spaces for law enforcement — that is prohibited under Article 5)
- **Post (ex-post) remote biometric identification** for law enforcement
- **Biometric verification** for access to services, premises, or devices
- **Biometric categorisation** based on sensitive or protected attributes

**Examples:**
- Airport e-gate facial verification (1:1 match against passport)
- Post-event identification of suspects from CCTV recordings for criminal investigation
- Biometric access control for secure facilities
- Age estimation systems for age-restricted services

**Edge cases:**
- Simple photo matching for account recovery → likely not high-risk if narrow scope
- Liveness detection without identification → assess based on biometric data processing
- Voice biometrics for speaker verification in call centres → high-risk if used for identification decisions

**Boundary with Article 5:** Real-time remote biometric identification in publicly accessible spaces for law enforcement is *prohibited* (Article 5), not merely high-risk. Post (ex-post) processing and non-law-enforcement uses fall here.

---

## 2. Critical Infrastructure

**Annex III, point 2**

High-risk AI systems intended as safety components in the management and operation of:
- Road traffic and supply of water, gas, heating, and electricity
- Digital infrastructure and telecommunications
- Other critical infrastructure where AI failure could endanger safety

**Examples:**
- AI controlling electricity grid load balancing and fault response
- Water treatment plant process optimisation with safety implications
- Traffic signal optimisation systems affecting pedestrian and vehicle safety
- AI-driven network routing in telecommunications with safety-critical dependencies

**Edge cases:**
- **Business analytics** on infrastructure data (demand forecasting for planning) → not high-risk unless it drives operational safety decisions
- **Customer-facing energy apps** (usage monitoring, billing) → generally not high-risk
- **Predictive maintenance** → high-risk if failure to predict correctly creates safety risk; lower risk if it merely optimises scheduling
- **Smart building systems** → depends on whether the AI is a safety component (fire systems, HVAC in hospitals) vs. convenience feature

**Key question:** Is the AI system a safety component, or does its failure risk endangering life, health, or critical service continuity?

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

High-risk AI systems intended for:
- Creditworthiness assessment and credit scoring
- Risk assessment and pricing in life and health insurance
- Evaluation of eligibility for essential public benefits and services
- Deciding on the provision, reduction, revocation, or reclamation of such benefits
- Housing allocation and rental eligibility assessment
- Emergency services dispatch prioritisation (triage)

**Examples:**
- Bank credit scoring algorithms determining loan approval
- Insurance risk models pricing life or health coverage
- Welfare benefits eligibility assessment systems
- Social housing allocation algorithms
- Emergency call centre AI triaging calls by severity

**Edge cases:**
- **Fraud detection** in banking → may be high-risk if it leads to account restrictions or service denial for individuals
- **Marketing offers** (pre-approved credit card offers) → generally not high-risk if no actual creditworthiness decision
- **Insurance pricing for non-life/non-health** (e.g., travel insurance) → not explicitly listed but assess by analogy
- **Customer service chatbots** for banks/insurers → not high-risk unless they make or materially influence eligibility decisions

**DACH note:** Credit scoring in Germany has additional SCHUFA/creditworthiness regulatory overlay. BaFin expects model risk management documentation for AI in financial services. See [dach-specific.md](dach-specific.md).

**Key question:** Does the AI determine or materially influence an individual's access to credit, insurance, benefits, housing, or emergency services?

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

High-risk AI systems intended for use by competent authorities for:
- Risk assessment at borders (security, health, irregular migration)
- Assisting in examination of asylum applications (credibility assessment, status determination)
- Verification of travel documents and supporting documentation
- Detection of irregular migration

**Examples:**
- Border risk profiling systems flagging travellers for secondary inspection
- AI assessing credibility of asylum seekers' narratives
- Automated document verification for visa processing
- AI-driven detection of forged identity documents

**Edge cases:**
- **Automated passport gates** (simple document + face match) → high-risk if they determine entry decisions
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

**Key EU legislation in Annex I (non-exhaustive):**
- Medical Devices Regulation (MDR) — Regulation (EU) 2017/745
- In Vitro Diagnostic Medical Devices Regulation (IVDR) — Regulation (EU) 2017/746
- Machinery Regulation — Regulation (EU) 2023/1230
- Toy Safety Directive — Directive 2009/48/EC
- Radio Equipment Directive — Directive 2014/53/EU
- Civil aviation safety regulations
- Motor vehicle type-approval regulations
- Railway interoperability directives

**Examples:**
- AI-powered diagnostic tool in a Class IIa+ medical device (MDR conformity assessment)
- Machine vision system in industrial machinery with safety function
- AI-based flight management component in aviation
- Autonomous driving features in motor vehicles

**Practical questions:**
- Which product regulatory regime applies?
- Is the AI a safety component or does it drive safety-relevant decisions?
- Which conformity assessment route applies, and is it third-party?

---

## 10. Article 6(3) Exception — When Annex III Systems Are NOT High-Risk

Even if an Annex III use case matches, the system is **not** high-risk if it:

1. Performs a **narrow procedural task**, OR
2. **Improves the result** of a previously completed human activity, OR
3. Detects **decision patterns** without replacing or influencing human assessment, OR
4. Performs a **preparatory task** for an assessment listed in Annex III

**AND** the AI system does not pose a significant risk of harm to health, safety, or fundamental rights.

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
