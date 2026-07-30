# Prohibited Practices — Article 5 Complete Checklist

## Table of Contents

1. [Manipulation and Deception](#1-manipulation-and-deception-causing-significant-harm)
2. [Exploitation of Vulnerabilities](#2-exploitation-of-vulnerabilities)
3. [Social Scoring](#3-social-scoring)
4. [Individual Predictive Policing](#4-individual-predictive-policing)
5. [Untargeted Facial Image Scraping](#5-untargeted-facial-image-scraping)
6. [Emotion Recognition in Workplace/Education](#6-emotion-recognition-in-workplace-and-education)
7. [Biometric Categorisation of Sensitive Characteristics](#7-biometric-categorisation-inferring-sensitive-characteristics)
8. [Real-Time Remote Biometric Identification](#8-real-time-remote-biometric-identification-for-law-enforcement)
9. [Assessment Methodology](#9-assessment-methodology)

---

## 1. Manipulation and Deception Causing Significant Harm

**Article reference:** Article 5(1)(a)

**Prohibited:** Placing on the market, putting into service, or using an AI system that deploys subliminal techniques beyond a person's consciousness, or purposefully manipulative or deceptive techniques, that materially distort behaviour and cause or are reasonably likely to cause significant harm.

**Examples:**
- Voice agent impersonating a family member to extract money
- System exploiting cognitive biases to push vulnerable consumers into unaffordable subscriptions
- Chatbot using dark patterns that go beyond persuasion into deception, causing financial harm
- AI-generated fake emergency alerts designed to trigger panic buying

**Edge cases and boundaries:**
- **Persuasive UX vs. manipulation:** Standard recommendation engines and A/B testing are not prohibited unless they cross into intentional deception with significant harm. The threshold is *purposeful* manipulation + *significant* harm.
- **Harm types:** Economic, physical, or psychological — must be significant and causally linked to the AI's manipulative technique.
- **Advertising:** Targeted advertising is generally not prohibited, but may cross the line if it uses subliminal techniques on identified vulnerable groups.

**Key test:** (1) Is the technique subliminal or deliberately deceptive? (2) Does it materially distort behaviour? (3) Is significant harm caused or likely?

---

## 2. Exploitation of Vulnerabilities

**Article reference:** Article 5(1)(b)

**Prohibited:** AI systems that exploit vulnerabilities due to age, disability, or social or economic situation, materially distorting behaviour and causing or likely causing significant harm.

**Examples:**
- Targeted in-app purchase pressure on children using manipulative game mechanics
- Debt collection AI targeting low-income individuals with deceptive legal threats
- AI companion apps exploiting elderly users' loneliness to drive excessive purchases
- Predatory lending algorithms specifically designed to target financially distressed individuals

**Edge cases and boundaries:**
- **Accessibility features** designed to help vulnerable groups are not exploitation
- **Age-appropriate content filtering** is protective, not exploitative
- **Marketing segmentation by demographics** is not per se prohibited — crosses the line when it becomes targeted exploitation with significant harm
- **Educational apps for children** need careful assessment if they use engagement mechanics tied to purchases

**Key test:** (1) Is a specific vulnerability being exploited (not just addressed)? (2) Does it materially distort behaviour? (3) Is significant harm caused or likely?

---

## 3. Social Scoring

**Article reference:** Article 5(1)(c)

**Prohibited:** AI systems evaluating or classifying persons based on social behaviour or personal/personality characteristics, where the resulting social score leads to detrimental or unfavourable treatment that is:
- unjustified or disproportionate to the social behaviour, OR
- in social contexts unrelated to where the data was originally collected

**Examples:**
- Composite "trust score" from social media behaviour used to deny housing
- Score based on lawful political activity used to restrict access to public services
- Loyalty programme data used to create behavioural ratings affecting unrelated services
- Employee "reliability score" derived from off-duty social media activity

**Edge cases and boundaries:**
- **Credit scoring** is not automatically social scoring, but could become prohibited if it expands into broad social evaluation across unrelated contexts
- **Fraud detection scores** limited to the specific transactional context are generally acceptable
- **Customer loyalty tiers** within a single service relationship are not social scoring
- **HR performance ratings** based on work-related metrics within the employment context are distinct from social scoring, but watch for scope creep

**Key test:** (1) Is behaviour from one context used to score treatment in an unrelated context? (2) Is the adverse treatment disproportionate?

---

## 4. Individual Predictive Policing

**Article reference:** Article 5(1)(d)

**Prohibited:** AI systems making risk assessments of natural persons to predict the risk of committing a criminal offence, based solely or primarily on profiling or personality/characteristics assessment. Does not affect human-initiated analysis supported by AI based on objective, verifiable facts directly linked to criminal activity.

**Examples:**
- "Likely offender" lists generated from demographic proxies and neighbourhood data
- Recidivism prediction based primarily on socioeconomic background without offence-specific facts
- Gang membership prediction based on social network analysis and postcode

**Edge cases and boundaries:**
- **Crime hotspot mapping** (location-based, not individual-based) may be permissible but is high-risk at minimum
- **Investigation support** using objective case facts is explicitly carved out
- **Border between predictive policing and investigation support:** If the system predicts individual risk primarily from profiling → prohibited. If it supports an active investigation with objective facts → potentially permissible but likely high-risk under Annex III category 6

**Key test:** Is the risk prediction about an *individual* based *solely or primarily* on profiling rather than objective, verifiable facts linked to criminal activity?

---

## 5. Untargeted Facial Image Scraping

**Article reference:** Article 5(1)(e)

**Prohibited:** AI systems that enable untargeted scraping of facial images from the internet or CCTV footage to create or expand facial recognition databases.

**Examples:**
- Vendor scraping social networks and public webcams to build a face database for identity services (Clearview AI-type systems)
- Building training datasets by mass-downloading profile photos without consent
- CCTV footage systematically processed to build searchable facial databases

**Edge cases and boundaries:**
- **Targeted collection with consent** for a specific authentication service is different but still triggers biometric/GDPR obligations
- **Research datasets** with proper legal basis and ethics approval may be distinct, but the untargeted scraping prohibition is broadly drawn
- **Existing databases:** The prohibition targets the *creation or expansion* through untargeted scraping — using a lawfully compiled database is a separate question

**Key test:** Is the system enabling *untargeted* scraping of facial images to *create or expand* a recognition database?

---

## 6. Emotion Recognition in Workplace and Education

**Article reference:** Article 5(1)(f)

**Prohibited:** Using emotion recognition AI in the workplace or educational institutions, except where the system is intended to be put into place or on the market for medical or safety reasons.

**Examples:**
- "Engagement detector" evaluating employees during meetings or training
- Proctoring tool inferring stress, attention, or deception in students during exams
- Call centre emotion monitoring scoring agent performance
- Classroom attention tracking via facial expression analysis

**Edge cases and boundaries:**
- **Medical exception:** Driver drowsiness detection for safety is a potential exception, but the burden of justification is high. Must be genuinely medical or safety-related, not repackaged performance monitoring.
- **Safety exception:** Operator fatigue detection in safety-critical environments (e.g., air traffic control) may qualify, but document the safety justification thoroughly.
- **Customer-facing emotion recognition** (outside workplace/education context) is not prohibited under this category but triggers Article 50 transparency duties and may be high-risk.
- **Even if excepted:** Such systems often trigger Article 50 disclosure obligations and may be high-risk under Annex III category 4 (employment) or category 3 (education).

**Key test:** (1) Is it emotion recognition? (2) Is it in a workplace or educational setting? (3) Does a genuine medical/safety exception apply?

---

## 7. Biometric Categorisation Inferring Sensitive Characteristics

**Article reference:** Article 5(1)(g)

**Prohibited:** Biometric categorisation systems that categorise individuals based on their biometric data to infer race, political opinions, trade union membership, religious or philosophical beliefs, sex life, or sexual orientation. Exception for labelling or filtering of lawfully acquired biometric datasets or law enforcement categorisation of biometric data.

**Examples:**
- Classifying ethnicity or sexual orientation from facial features
- Inferring religious beliefs from biometric gait analysis
- System predicting political orientation from facial structure

**Edge cases and boundaries:**
- **Categorisation for non-sensitive attributes** (e.g., age estimation for access control) is not prohibited under this category but may be high-risk or trigger Article 50 duties
- **Medical biometric analysis** (e.g., detecting health conditions from gait) requires careful distinction from inferring sensitive characteristics
- **Law enforcement exception** is narrow — categorisation for criminal investigation has specific carve-outs but is tightly regulated

**Key test:** Does the system use biometric data to *infer* any of the listed sensitive characteristics?

---

## 8. Real-Time Remote Biometric Identification for Law Enforcement

**Article reference:** Article 5(1)(h), with specific exceptions in Article 5(2)–(3)

**Prohibited in principle:** Real-time remote biometric identification systems in publicly accessible spaces for law enforcement purposes.

**Narrow exceptions (all require prior authorisation):**
- Targeted search for specific victims (abduction, trafficking, sexual exploitation)
- Prevention of specific, substantial, imminent threat to life or terrorist attack
- Identification of suspects for specific serious criminal offences (as listed)

**Requirements for exceptions:**
- Judicial or independent administrative authorisation (prior, or within 48 hours in urgent cases)
- Necessity and proportionality assessment
- Temporal, geographic, and personal scope limitations
- Notification to the relevant market surveillance authority
- Member State must have explicitly authorised the use in national law

**Examples:**
- Live face identification in a city centre for general policing → **prohibited**
- Targeted real-time identification to find a kidnapping victim with prior judicial authorisation → **potential exception**

**Edge cases and boundaries:**
- Distinguish **real-time** from **post** (ex-post remote biometric identification has different rules — may be high-risk under Annex III rather than prohibited)
- Distinguish **remote** from **local** (border control 1:1 verification at a checkpoint is different)
- Distinguish **identification** (1:N search) from **verification** (1:1 match)
- Distinguish **publicly accessible spaces** from private/restricted areas

---

## 9. Assessment Methodology

When evaluating Article 5, apply this structured approach:

1. **Map the system's function** to each of the eight categories above
2. **For each potential match**, apply the specific key test
3. **Document edge cases** — if a system is close to a prohibition boundary, document why it falls on the permissible side with specific factual reasoning
4. **Check for exceptions** — narrow law enforcement/medical/safety carve-outs exist for some categories
5. **If prohibited**, the system must be taken off the market or out of service. No grace period — the prohibition has applied since 2 February 2025.
6. **If borderline**, escalate to legal counsel with a documented analysis. Err on the side of caution — prohibited practice fines reach €35M or 7% of global turnover.

**Prohibition applies since:** 2 February 2025 — no transition period remains.
