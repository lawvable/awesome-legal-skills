# Prohibited AI Practices — Art. 5 AI Act

## Overview

Article 5 AI Act prohibits 8 categories of AI practices. These prohibitions apply since **2 February 2025** (Art. 113(a)). Violation carries the highest penalty: up to **EUR 35,000,000 or 7% of total worldwide annual turnover** (Art. 99(3)).

**Commission Guidelines Reference:** Guidelines on Prohibited AI Practices (Art. 5), published 4 February 2025.

---

## Category 1: Subliminal, Manipulative, or Deceptive Techniques — Art. 5(1)(a)

**Prohibition:** Placing on the market, putting into service, or using an AI system that deploys subliminal techniques beyond a person's consciousness, or purposefully manipulative or deceptive techniques, with the objective or effect of materially distorting a person's behavior, causing or being reasonably likely to cause significant harm.

**Recitals:** 28, 29

### Key Legal Test

Three cumulative conditions: (1) the AI system deploys subliminal, manipulative, or deceptive techniques; AND (2) these techniques materially distort a person's or group's behavior (causing decisions they would not otherwise have made); AND (3) this causes or is reasonably likely to cause significant harm (physical, psychological, financial, or societal).

### Key Elements

- **Subliminal techniques:** Operating below conscious awareness threshold (e.g., subliminal messaging, hidden audio frequencies, imperceptible visual stimuli)
- **Manipulative techniques:** Exploiting cognitive biases, dark patterns with AI amplification, emotional manipulation through personalized content
- **Deceptive techniques:** Misrepresenting AI system nature, creating false impressions of human interaction, concealing AI involvement in decision-making
- **Material distortion of behavior:** Person makes a decision they would not otherwise have made
- **Significant harm:** Physical, psychological, financial, or societal harm

### Boundary Analysis

| PROHIBITED | NOT PROHIBITED | Distinguishing Factor |
|-----------|---------------|----------------------|
| AI using imperceptible audio frequencies to influence purchasing decisions | AI-powered recommendation engine with visible "recommended for you" label | Conscious awareness: subliminal vs. transparent operation |
| Hyper-personalized persuasion system exploiting individual psychological vulnerabilities to change voting behavior | A/B testing of marketing messages with AI optimization | Harm threshold + intent: significant harm to democratic processes vs. optimizing engagement |
| AI chatbot impersonating a deceased family member to extract financial commitments | AI customer service chatbot clearly disclosed as AI (Art. 50(1)) | Deception: concealing AI nature to exploit emotional state vs. transparent interaction |
| AI system creating fake social consensus to pressure individuals into decisions | AI-powered social proof display ("1,000 people bought this") based on real data | Deception: fabricated information vs. factual display |

### Gray Zone Scenarios

1. **Persuasive health app:** An AI system nudges users toward healthier behavior using personalized psychological insights. The techniques could be considered "manipulative" (exploiting cognitive biases), but the purpose is beneficial. **Key question:** Does the beneficial purpose negate "significant harm"? The Commission Guidelines suggest that the harm requirement is objective — even well-intentioned manipulation that materially distorts behavior could be prohibited if it causes significant autonomy harm.

2. **AI-powered pricing:** Dynamic pricing system that adjusts prices based on predicted willingness to pay, using behavioral analysis. **Key question:** Is personalized pricing "manipulative"? If it exploits individual psychological profiles to extract maximum price, it may cross the line. If it simply reflects supply/demand, likely not prohibited. The distinction depends on whether the system targets individual vulnerabilities.

3. **Gamification AI:** Workplace gamification system using AI to maximize engagement through variable reward schedules (similar to slot machines). **Key question:** Do variable reward mechanisms constitute "subliminal" or "manipulative" techniques? If designed to exploit addictive tendencies, possibly yes — especially if employees cannot opt out.

### Interaction with Other Categories

- **+ Category 2:** If manipulative techniques specifically target vulnerable groups (children, elderly), both Art. 5(1)(a) and Art. 5(1)(b) may be triggered. Apply both analyses.
- **+ Art. 50:** Systems that are deceptive because they fail to disclose AI involvement may trigger both the prohibition (if harm results) and Art. 50 transparency obligations.

### Assessment Methodology

1. **Identify the technique:** Is the AI system using subliminal, manipulative, or deceptive techniques? (Technical analysis of system operation)
2. **Assess awareness:** Is the affected person aware of the technique's influence? (User testing, design review)
3. **Evaluate behavior distortion:** Would the person have made the same decision without the AI system's influence? (Counterfactual analysis)
4. **Assess harm:** Is significant harm caused or reasonably likely? (Impact assessment — physical, psychological, financial, societal)
5. **Check intent or effect:** Art. 5(1)(a) covers both intentional manipulation AND systems with the *effect* of manipulation — purpose alone does not exempt.

### Enforcement Context

**Expected AI Office focus:** Systems operating at scale with potential for mass behavioral manipulation — particularly in advertising, political communication, and consumer finance. The Commission Guidelines emphasize that the prohibition is technology-neutral and applies regardless of the sophistication of the technique.

---

## Category 2: Exploitation of Vulnerabilities — Art. 5(1)(b)

**Prohibition:** AI systems that exploit vulnerabilities of a person or group due to age, disability, or a specific social or economic situation, with the objective or effect of materially distorting behavior and causing or being likely to cause significant harm.

**Recitals:** 28, 29

### Key Legal Test

Three cumulative conditions: (1) the system targets or exploits a vulnerability related to age, disability, or social/economic situation; AND (2) materially distorts the behavior of the person or group; AND (3) causes or is likely to cause significant harm to that person or another.

### Key Elements

- **Protected groups:** Children, elderly, persons with disabilities, persons in precarious economic situations
- **Exploitation:** Taking advantage of reduced capacity to resist influence
- **Material distortion:** Causing different behavior than would occur without exploitation
- **Significant harm requirement:** Must cause or be likely to cause significant harm

### Boundary Analysis

| PROHIBITED | NOT PROHIBITED | Distinguishing Factor |
|-----------|---------------|----------------------|
| AI targeting elderly with dementia for high-interest financial products based on detected cognitive decline | AI-powered accessibility tool adapting interface for elderly users | Exploitation vs. assistance: targeting vulnerability for profit vs. serving the vulnerable person's interest |
| AI toy that manipulates children's trust to encourage purchases or dangerous actions | AI educational tool adapted to child's learning level | Direction of benefit: exploiting reduced resistance vs. age-appropriate education |
| Predatory lending AI detecting financial distress signals and offering high-cost loans | AI financial planning tool detecting financial distress and offering budgeting help | Same detection, opposite response: exploitation vs. protection |
| AI system using simplified language to bypass informed consent of persons with intellectual disabilities | AI system using simplified language to genuinely help persons with intellectual disabilities understand their options | Intent and effect: undermining autonomy vs. supporting autonomy |

### Gray Zone Scenarios

1. **Age-targeted marketing to teenagers:** AI advertising system on social media targeting 13-17-year-olds with beauty products using influencer-style AI-generated content. Teenagers are more susceptible to social comparison and body image influence. **Key question:** Does general age-targeted marketing to minors constitute "exploitation of vulnerability due to age"? The answer likely depends on whether the system specifically leverages adolescent psychological vulnerabilities (body image, peer pressure) versus age-appropriate advertising.

2. **Addiction-aware recommendation:** A streaming platform's AI recommendation system detects patterns indicating addictive usage but continues optimizing for engagement. **Key question:** Does knowing about a vulnerability (addictive tendency) and continuing to exploit it constitute "exploitation" under Art. 5(1)(b)? The "specific social or economic situation" clause may extend to addiction-related vulnerabilities.

3. **Crisis-priced essential services:** AI pricing system for essential goods (e.g., medications, heating) that increases prices when detecting individual economic distress signals. **Key question:** Economic vulnerability exploitation — does price discrimination based on detected financial distress cross the line from market dynamics to prohibited exploitation?

### Interaction with Other Categories

- **+ Category 1:** Manipulative techniques targeting vulnerable groups trigger both provisions. The vulnerability exploitation (Cat. 2) acts as an aggravating factor.
- **+ Category 3:** Social scoring of vulnerable groups could trigger both Cat. 2 (exploitation of vulnerability) and Cat. 3 (social scoring leading to detrimental treatment).

### Assessment Methodology

1. **Identify target group:** Does the system's user base or affected population include persons in protected vulnerability categories?
2. **Assess whether vulnerability is leveraged:** Does the system's design or operation specifically target, use, or benefit from the vulnerability?
3. **Evaluate behavior distortion:** Would the affected persons have acted differently if not for the exploitation of their vulnerability?
4. **Assess harm:** Is significant harm caused or reasonably likely to the vulnerable person or another?
5. **Distinguish exploitation from assistance:** Is the system designed to help or to take advantage of the vulnerability?

### Enforcement Context

**Expected enforcement priority:** Systems targeting children online, predatory financial products using AI to detect and exploit economic vulnerability, and AI systems in care settings (elderly care, disability services) that may exploit reduced autonomy.

---

## Category 3: Social Scoring — Art. 5(1)(c)

**Prohibition:** AI systems for evaluation or classification of natural persons or groups based on social behavior or personal characteristics, where the resulting social score leads to detrimental or unfavorable treatment that is:
- (i) unjustified or disproportionate to the social behavior or its gravity, or
- (ii) in social contexts unrelated to those in which the data was originally generated

**Recitals:** 31

### Key Legal Test

Three elements: (1) the AI system evaluates or classifies persons based on social behavior or personal characteristics; AND (2) this produces a "social score" (general-purpose trustworthiness or behavior rating); AND (3) the score leads to detrimental treatment that is either unjustified/disproportionate OR applied in unrelated contexts. Note: unlike earlier drafts, this prohibition applies to **both public and private actors**.

### Key Elements

- **Social scoring:** Systematic evaluation of trustworthiness, social behavior, or personal traits
- **By public authorities OR on their behalf:** Includes government contractors and delegated entities
- **OR by private actors:** Also covers private-sector social scoring
- **Detrimental treatment:** Adverse consequences based on score
- **Unjustified/disproportionate:** Treatment exceeds what the behavior warrants
- **Context crossing:** Using data from one context (e.g., social media) to make decisions in another (e.g., creditworthiness)

### Boundary Analysis

| PROHIBITED | NOT PROHIBITED | Distinguishing Factor |
|-----------|---------------|----------------------|
| Government trustworthiness scoring affecting access to public services based on social media behavior | Government fraud detection system using specific risk indicators relevant to the service | General social scoring vs. context-specific, proportionate risk assessment |
| Employer scoring employees across all life domains (social media, spending habits, associations) to determine promotions | Employer performance review based on work-related KPIs measured by AI | Context crossing: unrelated social data vs. job-relevant performance data |
| Insurance company combining social behavior, political activity, and shopping patterns to create "lifestyle score" for premium calculation | Insurance company using driving behavior data to adjust car insurance premiums | Scope: general social behavior score vs. risk-relevant, context-specific data |
| Platform combining behavioral data across unrelated contexts (shopping, social media, dating) to create universal user rating | Platform-specific reputation score based on transaction behavior on that platform (e.g., seller rating) | Context: cross-context aggregation vs. single-context, relevant scoring |

### Gray Zone Scenarios

1. **Tenant screening aggregation:** AI system that aggregates a prospective tenant's credit score, social media behavior, previous landlord reviews, and neighborhood data into a "reliability score" for landlords. **Key question:** Is this a prohibited "social score" or a legitimate multi-factor risk assessment? The context crossing (social media → housing decisions) may trigger Art. 5(1)(c)(ii), even if individual factors are lawful to consider.

2. **Employee engagement scoring:** AI system scoring employees on "engagement" using email response times, meeting participation, after-hours work, social interactions, and wellness app data. **Key question:** If the score influences promotions or termination decisions, does combining work-adjacent behavioral data into a single score constitute social scoring? The aggregation of diverse behavioral indicators into a single score is the critical factor.

3. **Municipal benefit optimization:** City government AI system that scores residents' "community contribution" (volunteering, environmental behavior, civic participation) to prioritize access to municipal services (parking, swimming pool bookings). **Key question:** Even with beneficial intent, does scoring citizens on civic behavior and allocating public services accordingly constitute social scoring? The detrimental treatment condition (limited service access) combined with government actor status strongly suggests prohibition.

### Interaction with Other Categories

- **+ Category 2:** Social scoring of economically vulnerable persons leading to loss of essential services combines both provisions.
- **+ Category 4:** If a social score is used to predict criminal behavior, both Cat. 3 (social scoring) and Cat. 4 (criminal risk prediction from profiling) may be triggered.

### Assessment Methodology

1. **Identify scoring:** Does the system produce a score, rating, or classification based on social behavior or personal characteristics?
2. **Assess generality:** Is the score a general-purpose behavioral/trustworthiness rating, or a specific, context-limited assessment?
3. **Check for context crossing:** Is data from one social context used to make decisions in unrelated contexts?
4. **Evaluate detrimental treatment:** Does the score lead to unfavorable treatment for the scored individuals?
5. **Assess proportionality:** Is the treatment justified by and proportionate to the underlying behavior?

### Enforcement Context

**Expected focus:** Government systems first (highest political sensitivity), followed by large-scale private platforms aggregating behavioral data across contexts. The Commission Guidelines clarify that lawful, context-specific assessments (credit scoring based on financial data, fraud detection) are not social scoring.

---

## Category 4: Individual Criminal Risk Prediction — Art. 5(1)(d)

**Prohibition:** AI systems for making risk assessments of natural persons to assess or predict the risk of a natural person committing a criminal offense, based solely on profiling or personality traits.

**Recitals:** 32

### Key Legal Test

Three cumulative conditions: (1) the system assesses or predicts the risk of a natural person committing a criminal offense; AND (2) at the individual level (specific persons); AND (3) based *solely* on profiling of the person or on their personality traits or characteristics.

### Key Elements

- **Individual level:** Must target specific natural persons (not statistical area-based analysis)
- **Criminal offense prediction:** Assessing likelihood of committing future crimes
- **Based solely on profiling:** Using personal characteristics without factual basis in prior behavior
- **Personality traits:** Including but not limited to nationality, place of residence, physical features, ethnicity

**Important exception:** This does NOT prohibit AI systems that support human assessment based on objective, verifiable facts directly linked to criminal activity. Systems supplementing (not replacing) human assessment of specific, factual criminal intelligence are not prohibited.

### Boundary Analysis

| PROHIBITED | NOT PROHIBITED | Distinguishing Factor |
|-----------|---------------|----------------------|
| Predictive policing flagging individuals as "pre-criminals" based on demographics and neighborhood | Crime hot-spot mapping analyzing geographic crime patterns (area-level, not individual) | Individual vs. area level: targeting specific persons vs. statistical analysis of locations |
| AI scoring individuals' likelihood to offend based on social media personality analysis | Recidivism risk assessment based on criminal history, used to supplement judicial decision | Data basis: personality profiling vs. factual criminal history |
| Criminal risk prediction based on facial features or physiognomy | Forensic face matching against existing database of suspects (identification, not prediction) | Purpose: predicting future crime from traits vs. identifying known suspects |
| AI system creating individual "threat scores" from social media sentiment analysis | AI system analyzing seized electronic evidence in ongoing criminal investigation | Basis: profiling for prediction vs. analyzing factual evidence |

### Gray Zone Scenarios

1. **Enhanced recidivism assessment:** AI recidivism tool that uses criminal history (not prohibited alone) but also incorporates socioeconomic factors, family situation, and neighborhood characteristics. **Key question:** When does a factual-basis assessment cross into prohibited profiling? The "solely on profiling" requirement is key — if the system uses factual criminal history plus personality traits, the mixed basis creates a gray zone. The Commission Guidelines suggest that systems must have a meaningful factual basis in *criminal* activity, not just correlated demographic factors.

2. **Radicalization detection:** AI system monitoring online behavior to detect "radicalization patterns" and flag individuals as potential threats. **Key question:** If based on behavioral patterns (website visits, communication patterns) rather than personality traits, is this profiling or behavioral analysis? The boundary between behavioral analysis (observing what someone does) and personality profiling (inferring who someone is) is critical.

3. **Insurance fraud prediction:** AI predicting insurance fraud risk per individual based on behavioral and demographic profiling. **Key question:** Insurance fraud is a criminal offense — does predicting fraud risk based on profiling fall under this prohibition? The private sector context and the specific, factual indicators typically used in fraud detection likely keep most fraud detection systems outside the prohibition, but systems relying heavily on demographic profiling could cross the line.

### Interaction with Other Categories

- **+ Category 3:** A social scoring system that produces a score used for criminal risk prediction combines both prohibitions.
- **+ Category 7 (Biometric Categorization):** Using biometric data to infer criminal propensity combines Cat. 4 and Cat. 7.
- **vs. Annex III Nr. 6(d):** Criminal offense risk assessment that is NOT based solely on profiling (i.e., uses factual criminal history) is not prohibited but is classified as **high-risk** under Annex III Nr. 6(d).

### Assessment Methodology

1. **Identify purpose:** Does the system assess or predict individual criminal risk?
2. **Check individual targeting:** Does the system generate risk assessments for specific natural persons (not area-level statistics)?
3. **Analyze data basis:** Is the assessment based solely on profiling/personality traits, or does it incorporate objective facts directly linked to criminal activity?
4. **Evaluate "solely" criterion:** If mixed data, what is the weight of profiling vs. factual basis? A predominantly profiling-based system with token factual elements may still be prohibited.
5. **Check human oversight:** Is the system supplementing human judgment (which suggests non-prohibition) or replacing it (which suggests prohibition)?

### Enforcement Context

**Expected focus:** Law enforcement predictive policing tools, border security individual risk scoring, and corporate background check systems that predict criminal propensity. The dividing line between prohibited Cat. 4 and high-risk Annex III Nr. 6(d) will be a major focus of enforcement guidance.

---

## Category 5: Untargeted Facial Recognition Database Scraping — Art. 5(1)(e)

**Prohibition:** AI systems that create or expand facial recognition databases through untargeted scraping of facial images from the internet or CCTV footage.

**Recitals:** 34

### Key Legal Test

Two elements: (1) the AI system creates or expands a facial recognition database; AND (2) it does so through *untargeted* scraping of facial images from the internet or CCTV.

### Key Elements

- **Untargeted scraping:** Mass collection without specific lawful purpose or individual consent
- **Facial images:** Biometric data capable of identifying individuals
- **From internet or CCTV:** Including social media, websites, video surveillance
- **Creating or expanding databases:** Building reference databases for facial recognition

### Boundary Analysis

| PROHIBITED | NOT PROHIBITED | Distinguishing Factor |
|-----------|---------------|----------------------|
| Scraping social media photos to build a general-purpose facial recognition database | Building a facial recognition database from photos voluntarily submitted with informed consent | Consent and targeting: untargeted scraping vs. consent-based enrollment |
| Collecting CCTV footage to create biometric identification databases | Using authorized CCTV with facial recognition in real-time without retaining biometric templates | Database creation: building a persistent database vs. real-time processing without storage |
| Web crawling for profile pictures to train facial recognition models | Training facial recognition models on licensed, consented datasets | Data acquisition: untargeted scraping vs. lawful acquisition |

### Gray Zone Scenarios

1. **Research dataset creation:** Academic researchers scraping publicly available photos to create a facial recognition research dataset. **Key question:** Does the scientific research exclusion (Art. 2(6)) protect this, or does the absolute nature of Art. 5 prohibitions override? If the dataset is intended only for research and never deployed, Art. 2(6) may apply. But if the dataset could later be commercialized, the prohibition applies.

2. **Targeted law enforcement scraping:** Police using AI to scrape a specific suspect's photos from social media to build a reference template. **Key question:** Is this "untargeted" scraping? The key word is "untargeted" — scraping photos of a specific, identified suspect for a specific investigation may not be "untargeted." However, building a broader database while searching for one person likely crosses the line.

### Interaction with Other Categories

- **+ Category 7:** If the scraped facial images are used to categorize persons by sensitive characteristics (race, religion), both Cat. 5 and Cat. 7 are triggered.
- **+ Category 8:** If untargeted scraping feeds a real-time biometric identification system in public, both Cat. 5 (database creation) and Cat. 8 (real-time RBI) are triggered.

### Assessment Methodology

1. **Identify data source:** Where are the facial images obtained from?
2. **Assess targeting:** Is the collection targeted (specific persons, with legal basis) or untargeted (mass scraping)?
3. **Check consent:** Did the individuals consent to their images being used for facial recognition?
4. **Evaluate purpose:** Is the purpose to create or expand a facial recognition database?
5. **Check research exception:** If research-only, does Art. 2(6) apply?

### Enforcement Context

**Established precedent:** Multiple DPA enforcement actions against Clearview AI across the EU (CNIL: EUR 20M fine; Garante: EUR 20M fine; ICO: GBP 7.5M fine; HDPA: EUR 20M fine). These GDPR-based decisions will inform AI Act enforcement under the broader Art. 5(1)(e) prohibition. The AI Office is expected to prioritize this category given existing enforcement momentum.

---

## Category 6: Emotion Recognition in Workplace and Education — Art. 5(1)(f)

**Prohibition:** AI systems to infer emotions of a natural person in the areas of workplace and education institutions, except where the AI system is intended to be placed on the market or put into service for medical or safety reasons.

**Recitals:** 33

### Key Legal Test

Three elements: (1) the AI system infers emotions of natural persons; AND (2) in the workplace or educational institution context; AND (3) it is not intended for medical or safety purposes (exceptions).

### Key Elements

- **Emotion recognition (Emotionserkennung):** Inferring emotional states from biometric data (facial expressions, voice tone, body language, physiological signals)
- **Workplace:** Any employment context, including remote work monitoring
- **Educational institutions:** Schools, universities, training centers
- **Medical exception:** Systems for therapeutic purposes (e.g., pain assessment for non-verbal patients)
- **Safety exception:** Systems for safety-critical applications (e.g., detecting driver fatigue)

### Boundary Analysis

| PROHIBITED | NOT PROHIBITED | Distinguishing Factor |
|-----------|---------------|----------------------|
| Camera reading employee facial expressions during meetings to assess "engagement" | Camera monitoring workplace for physical safety (slip and fall detection) without emotion inference | Emotion inference: detecting emotions vs. detecting physical events |
| AI monitoring student engagement via emotion detection in online classes | Exam proctoring system detecting eye movement patterns for cheating (without inferring emotions) | What is detected: emotional state vs. behavioral compliance |
| Voice analysis detecting employee stress levels during calls | Voice recognition authenticating employee identity | Analysis target: emotional state vs. identity verification |
| Wearable monitoring employee emotional states during work | Wearable detecting driver fatigue in commercial vehicle (safety exception) | Context: general workplace vs. safety-critical application |
| AI detecting student frustration in e-learning to recommend content differently | AI detecting seizure onset in a student with epilepsy in classroom (medical exception) | Purpose: engagement optimization vs. medical safety |

### Gray Zone Scenarios

1. **Sentiment analysis of text communication:** AI system analyzing employee emails and chat messages for "sentiment" or "tone" to assess team morale. **Key question:** Is text-based sentiment analysis "emotion recognition" under Art. 5(1)(f)? The prohibition refers to inferring "emotions" — if the system infers emotional states (frustrated, happy, anxious) from text, it likely falls within the prohibition. If it merely classifies tone (formal, informal, urgent) without inferring emotional states, it may not.

2. **Safety-adjacent emotion detection:** Factory worker fatigue detection system using facial analysis to prevent accidents. The system detects drowsiness (physical state) but the underlying model also captures emotional states. **Key question:** Does the safety exception apply when the primary purpose is safety but emotion data is incidentally captured? The exception requires the system to be "intended" for safety reasons — if designed for safety, incidental emotion data capture may be acceptable, but the system should not use or store the emotion data.

3. **Remote proctoring with engagement metrics:** Online exam proctoring AI that flags "suspicious behavior" using facial analysis — it detects gaze direction, head movement, but also "confusion" and "stress" levels. **Key question:** Can an educational testing system detect behavioral anomalies without inferring emotions? If the system's model inherently infers emotional states as part of its behavioral analysis, the prohibition applies even if emotional data is not the primary output.

### Interaction with Other Categories

- **+ Category 1:** Emotion recognition combined with manipulative techniques (detecting employee emotions to manipulate them into compliance) triggers both Cat. 1 and Cat. 6.
- **+ Annex III Nr. 1(c):** Emotion recognition *outside* workplace/education is not prohibited but is high-risk under Annex III Nr. 1(c). The boundary between "workplace" and "non-workplace" contexts matters.
- **+ Annex III Nr. 4:** Workplace AI that monitors employees without emotion recognition is high-risk under Annex III Nr. 4(b); with emotion recognition, it's prohibited under Cat. 6.

### Assessment Methodology

1. **Identify emotional inference:** Does the system infer, detect, or classify emotional states?
2. **Identify context:** Is the system used in a workplace or educational institution?
3. **Define "workplace" broadly:** Includes remote work, home office, field work, platform work — any professional employment context
4. **Check medical exception:** Is the system specifically intended for medical purposes (diagnosis, treatment, patient monitoring)?
5. **Check safety exception:** Is the system specifically intended for safety-critical applications where emotional state directly affects safety?
6. **Verify exception specificity:** The exception must be the system's *intended purpose*, not an incidental benefit

### Enforcement Context

**Expected priority:** Workplace monitoring vendors marketing "engagement analytics" or "sentiment monitoring" products for employee evaluation. Educational technology companies offering "attention tracking" or "engagement monitoring" with emotion inference components. National labor authorities (in addition to AI authorities) may enforce through existing employment law channels.

---

## Category 7: Biometric Categorization for Sensitive Characteristics — Art. 5(1)(g)

**Prohibition:** AI systems that categorize natural persons individually based on their biometric data to deduce or infer their race, political opinions, trade union membership, religious or philosophical beliefs, sex life, or sexual orientation.

**Recitals:** 30

### Key Legal Test

Three elements: (1) the system uses biometric data; AND (2) categorizes individual natural persons; AND (3) the purpose or effect is to deduce or infer sensitive characteristics (race, political opinions, trade union membership, religion, sex life, sexual orientation).

### Key Elements

- **Biometric categorization:** Using biometric data (facial features, voice, gait, etc.) to sort individuals
- **Sensitive categories:** Race/ethnicity, political opinion, trade union membership, religion, sex life, sexual orientation
- **Individual level:** Categorizing specific persons (not aggregate statistical analysis)

**Exception:** Labeling or filtering of lawfully acquired biometric datasets (e.g., for law enforcement to filter photos by hair color to narrow search — but not to infer sensitive characteristics).

### Boundary Analysis

| PROHIBITED | NOT PROHIBITED | Distinguishing Factor |
|-----------|---------------|----------------------|
| AI categorizing job applicants by perceived ethnicity from photos | AI filtering photos by objective physical descriptors (hair color, height range) without inferring sensitive categories | Target: sensitive characteristics vs. objective physical descriptors |
| System inferring religious belief from facial features or clothing analysis | Age estimation system using facial analysis (age is not in the sensitive characteristic list) | Category: sensitive (religion) vs. non-sensitive (age) |
| AI detecting sexual orientation from biometric behavioral patterns | AI analyzing gait patterns for medical diagnosis (movement disorder detection) | Purpose: inferring sensitive trait vs. medical analysis |
| AI system inferring political affiliation from voice patterns or facial micro-expressions | AI system using voice biometrics for speaker identification (who, not what they believe) | What is inferred: beliefs/orientation vs. identity |

### Gray Zone Scenarios

1. **Gender estimation from biometrics:** AI system estimating gender from facial features for marketing purposes. **Key question:** "Sex life" and "sexual orientation" are prohibited categories, but binary gender estimation is not explicitly listed. However, if the system effectively categorizes by perceived sex, and this information could be used to infer sexual orientation (e.g., by combining with other data), the prohibition may apply indirectly. Gender estimation alone is likely not prohibited but falls in a gray zone.

2. **Diversity analytics:** HR department using biometric analysis of group photos to assess workforce diversity (ethnic composition). **Key question:** Even if the purpose is positive (promoting diversity), using biometric categorization to infer race/ethnicity of individuals is prohibited under Art. 5(1)(g). The prohibition does not include a "beneficial purpose" exception.

3. **Cultural bias in facial analysis:** AI system that, as an unintended side effect of its primary function (e.g., face-based age estimation), generates intermediate features that encode race or ethnicity. **Key question:** If the system does not output sensitive categorizations but its internal representations encode them, is the prohibition triggered? The key word is "deduce or infer" — if the system's purpose does not include categorization by sensitive traits and such categorization is not an output, the prohibition likely does not apply, but the system should be designed to minimize encoded sensitive information.

### Interaction with Other Categories

- **+ Category 5:** If biometric categorization is based on untargeted scraped facial images, both Cat. 5 and Cat. 7 are triggered.
- **+ Category 6:** Emotion recognition that incidentally categorizes by ethnicity (due to biased training data) could trigger both Cat. 6 and Cat. 7.
- **+ Annex III Nr. 1(b):** Biometric categorization that does NOT target sensitive characteristics (e.g., categorizing by age group, height) is not prohibited but may be high-risk under Annex III Nr. 1(b).

### Assessment Methodology

1. **Identify biometric processing:** Does the system process biometric data (facial images, voice, gait, physiological signals)?
2. **Assess categorization output:** Does the system categorize, label, or sort individuals?
3. **Check target categories:** Are the categories sensitive characteristics (race, political opinion, trade union, religion, sex life, sexual orientation)?
4. **Evaluate individual level:** Is categorization at the individual level, or aggregate/statistical only?
5. **Check for indirect inference:** Even if not the primary purpose, does the system enable inference of sensitive characteristics from its outputs?

### Enforcement Context

**Expected focus:** Facial analysis vendors, biometric access control systems with demographic classification features, and HR technology using biometric assessment. The GDPR Art. 9 (special categories) enforcement experience will inform AI Act enforcement.

---

## Category 8: Real-Time Remote Biometric Identification in Public — Art. 5(1)(h)

**Prohibition:** Use of real-time remote biometric identification (RBI) systems in publicly accessible spaces for law enforcement purposes.

**Recitals:** 34, 35, 36

### Key Legal Test

Four cumulative conditions: (1) biometric identification (one-to-many comparison against a reference database); AND (2) real-time (simultaneous or minimal delay); AND (3) remote (without physical proximity or cooperation); AND (4) in publicly accessible spaces for law enforcement purposes.

### Key Elements

- **Real-time:** Processing occurs simultaneously or with minimal delay
- **Remote:** Without physical proximity or cooperation of the identified person
- **Biometric identification:** One-to-many comparison against a reference database
- **Publicly accessible spaces:** Streets, parks, transport hubs, shopping areas
- **Law enforcement purpose:** For the purpose of criminal law enforcement

### Three Narrow Exceptions (Art. 5(2))

Each requires prior judicial or independent administrative authorization (except verified urgency):

1. **Targeted victim search:** Search for specific potential victims of abduction, trafficking, or sexual exploitation
2. **Imminent threat prevention:** Prevention of a specific, substantial, and imminent threat to life or a foreseeable terrorist attack
3. **Serious crime investigation:** Identification of suspects of specific serious criminal offenses (listed in Annex IIa, punishable by at least 4 years)

**Conditions for exceptions:**
- Strictly necessary and proportionate
- Prior authorization by judicial authority or independent administrative authority
- Time and geographic limitations
- Fundamental rights impact assessment required
- Registration in EU database required

### Boundary Analysis

| PROHIBITED | NOT PROHIBITED | Distinguishing Factor |
|-----------|---------------|----------------------|
| Real-time facial recognition scanning crowds in a city square for law enforcement | One-to-one biometric verification at an access control point (airport gate, building entry) | One-to-many vs. one-to-one: identification vs. verification |
| Live facial recognition at a protest to identify participants | Post-event forensic analysis of recorded CCTV footage to identify a specific suspect | Timing: real-time vs. post-event (retrospective analysis is not "real-time") |
| Continuous biometric scanning in a shopping mall for shoplifting prevention | Biometric access control within a private, non-publicly-accessible building (e.g., server room) | Space: publicly accessible vs. restricted access |
| Real-time gait recognition scanning train station passengers for law enforcement | Real-time facial recognition in a private corporate office for employee time-tracking (not publicly accessible, not law enforcement) | Purpose + space: law enforcement in public vs. private use in private space |

### Gray Zone Scenarios

1. **"Near-real-time" processing:** System that processes biometric data with a 30-minute delay rather than instantaneously. **Key question:** What delay crosses the boundary from "real-time" to "post-event"? The Commission Guidelines indicate that the concept of "real-time" should be interpreted broadly — any processing with the *purpose* of immediate identification, even with technical delays, may be captured.

2. **Semi-public spaces:** Biometric identification in a hospital waiting room, train station commercial area, or university campus. **Key question:** Are these "publicly accessible spaces"? The concept should be interpreted broadly — any space where the general public has access, even if technically private property, is likely covered.

3. **Non-law-enforcement purpose in public:** Municipality using real-time biometric identification for urban planning (counting and tracking pedestrian flows) rather than law enforcement. **Key question:** The prohibition is specifically for "law enforcement purposes." If the purpose is genuinely not law enforcement, the prohibition may not apply — but the system would still be high-risk under Annex III Nr. 1(a), and any function creep toward law enforcement use would trigger the prohibition.

### Interaction with Other Categories

- **+ Category 5:** Real-time RBI that builds a persistent database from the biometric scans also triggers Cat. 5 (untargeted facial recognition database scraping).
- **+ Category 7:** If the RBI system also categorizes individuals by sensitive characteristics during identification, Cat. 7 is additionally triggered.
- **+ Annex III Nr. 1(a):** Non-real-time (post-event/retrospective) biometric identification in public spaces is not prohibited but is high-risk under Annex III Nr. 1(a). Real-time RBI in non-publicly-accessible spaces for non-law-enforcement purposes is also high-risk.

### Assessment Methodology

1. **Identify biometric processing:** Is the system performing biometric identification (one-to-many matching)?
2. **Assess timing:** Is the processing real-time or with minimal delay?
3. **Check remoteness:** Does the system operate without subject cooperation or physical proximity?
4. **Identify space:** Is the space publicly accessible?
5. **Check purpose:** Is the purpose law enforcement? Be strict — any law enforcement use in public spaces triggers the prohibition.
6. **If exceptions claimed:** Verify all conditions (judicial authorization, time/geographic limits, necessity, proportionality, FRIA, EU database registration).

### Enforcement Context

**Expected strict enforcement:** This is the most politically visible prohibition. Member States must ensure no unauthorized deployment. The exceptions are narrow and require prior judicial authorization — law enforcement agencies must establish robust approval procedures. AI Office expected to monitor closely through national authority coordination.

---

## Multi-Category Interaction Assessment

When screening a system, assess whether it could trigger **multiple** prohibited categories simultaneously:

```
MULTI-CATEGORY INTERACTION MAP

Category 1 (Manipulation) ←──→ Category 2 (Vulnerability)
  Manipulative techniques targeting vulnerable groups

Category 3 (Social Scoring) ←──→ Category 4 (Criminal Prediction)
  Social score used for criminal risk prediction

Category 5 (Facial Scraping) ←──→ Category 7 (Biometric Categorization)
  Scraped facial data used to categorize sensitive traits

Category 5 (Facial Scraping) ←──→ Category 8 (Real-time RBI)
  Scraped database feeds real-time identification system

Category 6 (Emotion: Workplace) ←──→ Category 7 (Biometric: Sensitive)
  Biased emotion recognition incidentally categorizes ethnicity

When multiple categories are triggered, each must be documented
separately — there is no "merger" of prohibitions.
```

---

## Screening Methodology

When screening a system against Art. 5, check each category systematically:

```
PROHIBITED PRACTICE SCREENING (Art. 5)

| # | Category | Applicable? | Reasoning |
|---|----------|-------------|-----------|
| 1 | Subliminal/manipulative/deceptive techniques | [Yes/No/Possibly] | |
| 2 | Exploitation of vulnerabilities | [Yes/No/Possibly] | |
| 3 | Social scoring | [Yes/No/Possibly] | |
| 4 | Criminal risk prediction (profiling-only) | [Yes/No/Possibly] | |
| 5 | Untargeted facial recognition scraping | [Yes/No/Possibly] | |
| 6 | Emotion recognition (workplace/education) | [Yes/No/Possibly] | |
| 7 | Biometric categorization (sensitive traits) | [Yes/No/Possibly] | |
| 8 | Real-time remote biometric ID (public/LE) | [Yes/No/Possibly] | |

Prohibited practice identified: [YES — Category X / NO]
Multi-category interaction: [YES — Categories X+Y / NO]
```

If "Possibly" for any category → flag for detailed legal analysis and recommend counsel involvement.
