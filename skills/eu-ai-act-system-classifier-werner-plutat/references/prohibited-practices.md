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

**Prohibited:** AI systems making risk assessments of natural persons in order to assess or predict the risk of committing a criminal offence, based **solely** on the profiling of a natural person or on assessing their personality traits and characteristics. Does not affect human-initiated analysis supported by AI based on objective, verifiable facts directly linked to criminal activity.

**Examples:**
- "Likely offender" lists generated from demographic proxies and neighbourhood data
- Recidivism prediction based primarily on socioeconomic background without offence-specific facts
- Gang membership prediction based on social network analysis and postcode

**Edge cases and boundaries:**
- **Crime hotspot mapping** based only on aggregate location data may fall outside Annex III point 6 where it does not assess or predict the risk of a natural person or perform profiling. Assess the actual intended purpose and outputs
- **Investigation support** using objective case facts is explicitly carved out
- **Border between predictive policing and investigation support:** If the system predicts individual risk based solely on profiling or personality assessment → prohibited. If objective, verifiable facts directly linked to criminal activity enter the assessment, the prohibition does not bite, but the system is then typically high-risk under Annex III point 6(d), which covers exactly this non-prohibited risk assessment

**Key test:** Is the risk prediction about an *individual* based *solely* on profiling or personality traits, with no objective, verifiable facts directly linked to criminal activity in the assessment?

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

**Narrow exceptions normally require prior authorisation.** In a duly justified situation of urgency, use may begin while authorisation is requested without undue delay and no later than 24 hours, subject to immediate cessation and deletion if refused:
- Targeted search for specific victims (abduction, trafficking, sexual exploitation)
- Prevention of specific, substantial, imminent threat to life or terrorist attack
- Identification of suspects for specific serious criminal offences (as listed)

**Requirements for exceptions:**
- Prior judicial or independent administrative authorisation. In a duly justified situation of urgency, use may commence without authorisation provided it is requested without undue delay, at the latest within 24 hours; if rejected, use stops immediately and all data, results and outputs are discarded (Art. 5(3))
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


### Art. 5(1)(ba) - Non-consensual intimate material (added by Regulation (EU) 2026/1744)

Placing on the market, putting into service or using an AI system that generates or
manipulates realistic images, video, audio or similar material of an identifiable natural
person's intimate parts, or of an identifiable natural person engaged in sexually explicit
activities, without that person's freely given, specific, informed, unambiguous and
explicit consent.

**Applies from 2 December 2026** (Art. 113(3)(a) as amended).

Scope limits in Art. 5(1a) and (1b):
- For providers, placing on the market or putting into service is prohibited only where
  such generation is the system's intended purpose, or where the design, training,
  architecture, capabilities or user-facing functionality make it a reasonably foreseeable
  and reproducible outcome without significant technical modification AND the system lacks
  reasonable and adequate safeguards to prevent it and correct observed misuse.
- For deployers, use is prohibited only where the deployer uses the system for that purpose.
- Manipulation that neither increases the exposure of depicted intimate parts nor alters the
  nature of depicted sexually explicit activity does not count as manipulation.

Not caught: material that does not depict identifiable natural persons; realistic partially
nude depictions where intimate parts are not revealed **and** no sexually explicit activity is
depicted; works that are not realistic, including artistic works only in so far as they do not
realistically depict an identifiable person; and generation with the person's explicit consent.
Note that "artistic" alone exempts nothing: realism is the operative element of Art. 5(1)(ba),
so a realistic depiction of an identifiable person is caught however it is framed.

**Try-on and medical applications are not categorically exempt.** They fall outside the
prohibition only where intimate parts are not exposed or the specified explicit consent exists.
Recital 12 of Regulation (EU) 2026/1744 additionally recognises exceptional generation for
diagnosis or treatment by medical professionals where the person is incapable of giving
consent, subject to fundamental-rights, data-protection and medical law. A virtual try-on
feature that exposes intimate parts of an identifiable person without consent is inside the
prohibition, whatever it is called.

### Art. 5(1)(bb) - Child sexual abuse material (added by Regulation (EU) 2026/1744)

Placing on the market, putting into service or using an AI system that generates or
manipulates material or a performance within the meaning of Art. 2, points (c) and (e), of
Directive 2011/93/EU, except where a "without right" defence applies under national law
(for example law-enforcement use, or red-teaming and evaluation to test compliance).

**Applies from 2 December 2026.** The Art. 5(1a) provider and deployer limits apply here too. Art. 5(1b) does **not**: by its own terms it governs point (ba) only, so there is no equivalent manipulation carve-out for CSAM.


## 9. Assessment Methodology

When evaluating Article 5, apply this structured approach:

1. **Map the system's function** to each of the ten categories above (eight original, plus Art. 5(1)(ba) and (bb) added on 27 July 2026)
2. **For each potential match**, apply the specific key test
3. **Document edge cases** — if a system is close to a prohibition boundary, document why it falls on the permissible side with specific factual reasoning
4. **Check for exceptions** — narrow law enforcement/medical/safety carve-outs exist for some categories
5. **If prohibited**, the system must be taken off the market or out of service. For the original eight categories there is no grace period: the prohibition has applied since 2 February 2025. The two categories added by Regulation (EU) 2026/1744, Art. 5(1)(ba) and (bb), apply from 2 December 2026.
6. **If borderline**, escalate to legal counsel with a documented analysis. Err on the side of caution — prohibited practice fines reach €35M or 7% of global turnover.

**Prohibition applies since:** 2 February 2025 for the original eight categories, with no transition period remaining. Art. 5(1)(ba) and (bb) apply from 2 December 2026.
