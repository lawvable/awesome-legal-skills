# Sector-Specific Classification Guidance

Sector-specific guidance for applying the AI Act classification framework. Cross-references Annex III categories, relevant EU legislation, and common sector applications.

---

## 1. Healthcare (Gesundheitswesen)

### Annex III Triggers

| Annex III Category | Sub-Category | Typical Healthcare Applications |
|---|---|---|
| Nr. 5(b) | Risk assessment — life and health insurance | AI underwriting, health risk scoring |
| Nr. 1(a) | Remote biometric identification | Patient identification via biometrics |

**Annex I triggers (Art. 6(1)):**
- Annex I Nr. 11: Medical devices (Regulation (EU) 2017/745 — MDR)
- Annex I Nr. 12: In vitro diagnostic medical devices (Regulation (EU) 2017/746 — IVDR)

**Critical:** Most AI in clinical diagnosis, treatment planning, or patient monitoring is a **medical device** under MDR/IVDR and therefore high-risk via Art. 6(1) + Annex I, not via Annex III.

### Sector-Specific EU Legislation Interaction

| Legislation | Relevance |
|---|---|
| MDR (EU) 2017/745 | AI as medical device or safety component — double conformity assessment (AI Act + MDR) |
| IVDR (EU) 2017/746 | AI in vitro diagnostics — same double conformity requirement |
| GDPR Art. 9 | Health data as special category — heightened data protection requirements |
| Clinical Trials Regulation (EU) 536/2014 | AI in clinical trial design or patient selection |
| eHealth Regulation (proposed) | European Health Data Space — secondary use of health data |

### Practical Compliance Considerations

1. **Double conformity assessment:** AI qualifying as a medical device must pass BOTH MDR/IVDR conformity assessment AND AI Act requirements. Notified bodies must assess both.
2. **CE marking:** AI medical devices already carry CE marking under MDR — AI Act adds additional layer, not replacement.
3. **GDPR Art. 9 health data:** Processing health data for AI training requires explicit consent or specific legal basis. Art. 10(5) AI Act allows processing of special category data for bias detection under strict conditions.
4. **Software as Medical Device (SaMD):** The MDR's broad SaMD definition captures many clinical AI tools. Check MDCG guidance on qualification of software.
5. **R&D exclusion:** AI in pre-clinical research phase may qualify for Art. 2(6) or Art. 2(8) exclusion, but only until placed on market.

### Common AI Applications

| Application | Annex Trigger | Likely Risk Level |
|---|---|---|
| Clinical decision support (diagnosis) | Annex I Nr. 11 (MDR) | High-risk (Art. 6(1)) |
| Medical imaging analysis (radiology AI) | Annex I Nr. 11 (MDR) | High-risk (Art. 6(1)) |
| Drug interaction checker | Annex I Nr. 11 (MDR) | High-risk (Art. 6(1)) |
| Health insurance risk scoring | Annex III Nr. 5(b) | High-risk (Art. 6(2)) |
| Hospital scheduling optimization | None | Minimal risk |
| Patient chatbot (symptom checker) | Art. 50(1) + possibly MDR | Limited risk or high-risk (MDR) |
| Administrative billing AI | None | Minimal risk |
| Clinical trial patient matching | Art. 2(6) possible | Context-dependent |

---

## 2. Finance and Insurance (Finanz- und Versicherungswesen)

### Annex III Triggers

| Annex III Category | Sub-Category | Typical Finance Applications |
|---|---|---|
| Nr. 5(a) | Creditworthiness assessment (Kreditwuerdigkeitspruefung) | Credit scoring, loan approval AI |
| Nr. 5(b) | Risk assessment — life and health insurance | Insurance premium AI, underwriting |

**Note on fraud detection:** AI systems used for fraud detection in financial services typically do NOT fall under Annex III Nr. 5, as fraud detection evaluates transaction patterns, not individual creditworthiness or insurance risk. However, if a fraud detection score affects a person's access to financial services, an Annex III Nr. 5(a) argument could arise.

### Sector-Specific EU Legislation Interaction

| Legislation | Relevance |
|---|---|
| PSD2 / PSD3 (Payment Services Directive) | AI in payment authentication, fraud detection |
| CRD VI / CRR III (Capital Requirements) | AI in risk models — supervisory expectations |
| Solvency II (Insurance) | AI in actuarial models, risk assessment |
| MiCA (Markets in Crypto-Assets) | AI in crypto trading, market surveillance |
| DORA (Digital Operational Resilience Act) | ICT risk management for AI in financial services |
| Consumer Credit Directive (EU) 2023/2225 | Right to explanation for credit decisions — reinforces AI Act |
| GDPR Art. 22 | Automated individual decision-making — applies to AI credit/insurance decisions |

### Practical Compliance Considerations

1. **FRIA mandatory (Art. 27):** Deployers of high-risk AI in credit scoring and insurance MUST conduct a Fundamental Rights Impact Assessment before deployment.
2. **GDPR Art. 22 overlap:** Fully automated credit/insurance decisions require human intervention rights under GDPR — AI Act's human oversight (Art. 14) complements this.
3. **Profiling re-exception trap:** Credit scoring and insurance risk assessment almost always involve profiling (Art. 4(4) GDPR), so the Art. 6(3) exception is effectively unavailable for these use cases.
4. **Existing regulatory frameworks:** Financial supervisors (BaFin, ECB SSM) already require model validation, explainability, and governance. Map existing frameworks to AI Act obligations.
5. **DORA interaction:** DORA's ICT risk management requirements (effective Jan 2025) overlap with AI Act technical measures — coordinate compliance.

### Common AI Applications

| Application | Annex Trigger | Likely Risk Level |
|---|---|---|
| Credit scoring / loan approval | Annex III Nr. 5(a) | High-risk (Art. 6(2)) |
| Life/health insurance underwriting | Annex III Nr. 5(b) | High-risk (Art. 6(2)) |
| Fraud detection (transaction-level) | None (typically) | Minimal risk |
| Anti-money laundering (AML) screening | None (typically) | Minimal risk |
| Algorithmic trading | None | Minimal risk (but MiFID II regulated) |
| Robo-advisory | Art. 50(1) | Limited risk (+ MiFID suitability) |
| Customer service chatbot | Art. 50(1) | Limited risk |
| Claims processing automation | Art. 6(3)(a) possible | Context-dependent |

---

## 3. HR and Employment (Personalwesen und Beschaeftigung)

### Annex III Triggers

| Annex III Category | Sub-Category | Typical HR Applications |
|---|---|---|
| Nr. 4(a) | Recruitment and selection (Einstellung) | CV screening, candidate ranking, interview analysis |
| Nr. 4(b) | Decisions affecting terms of work (Arbeitsbedingungen) | Performance evaluation, promotion, termination, task allocation |

**Critical:** Annex III Nr. 4 has the broadest scope in employment — it covers the entire employment lifecycle from recruitment through termination.

### Sector-Specific EU Legislation Interaction

| Legislation | Relevance |
|---|---|
| GDPR Art. 22 | Automated employment decisions — human intervention rights |
| GDPR Art. 9 | Processing of health/biometric/union membership data |
| BetrVG (Germany) | Works council co-determination (Mitbestimmungsrecht) for AI introduction — § 87(1) Nr. 6 |
| Platform Work Directive (EU) 2024/2831 | Algorithmic management obligations for platform workers |
| Employment Equality Directives 2000/43/EC, 2000/78/EC | Non-discrimination — AI must not discriminate on protected grounds |
| Art. 5(1)(f) AI Act | Emotion recognition in workplace is PROHIBITED |

### Practical Compliance Considerations

1. **Emotion recognition ban:** Art. 5(1)(f) prohibits emotion recognition in the workplace (except medical/safety). This bans AI-based mood analysis, engagement scoring from facial expressions, or stress detection in employees.
2. **Works council involvement (Germany):** Art. 26(7) AI Act requires informing employee representatives. In Germany, § 87(1) Nr. 6 BetrVG gives works councils co-determination rights for AI monitoring systems — this goes beyond the AI Act's information obligation.
3. **Profiling re-exception:** HR AI systems almost always involve profiling of individuals (evaluating performance, predicting suitability), so the Art. 6(3) exception is effectively blocked. Assume high-risk for most employment AI.
4. **Platform Work Directive:** For platform workers, the Directive adds algorithmic transparency, human review of automated decisions, and right to explanation — overlapping with AI Act.
5. **FRIA for certain deployers:** Art. 27 FRIA is required for specific private deployers using high-risk HR AI systems.
6. **Bias testing critical:** Employment AI carries high discrimination risk. Art. 10 data governance and Art. 9 risk management must specifically address bias across protected characteristics.

### Common AI Applications

| Application | Annex Trigger | Likely Risk Level |
|---|---|---|
| CV screening / ranking | Annex III Nr. 4(a) | High-risk (Art. 6(2)) |
| Automated interview scoring | Annex III Nr. 4(a) | High-risk (Art. 6(2)) |
| Performance evaluation AI | Annex III Nr. 4(b) | High-risk (Art. 6(2)) |
| Workforce planning/scheduling | Art. 6(3)(a) possible | Context-dependent |
| Employee monitoring (productivity) | Annex III Nr. 4(b) | High-risk (Art. 6(2)) |
| Emotion/mood detection (employees) | Art. 5(1)(f) | PROHIBITED |
| Chatbot for HR queries | Art. 50(1) | Limited risk |
| Payroll automation | None | Minimal risk |

---

## 4. Law Enforcement (Strafverfolgung)

### Annex III Triggers

| Annex III Category | Sub-Category | Typical Law Enforcement Applications |
|---|---|---|
| Nr. 1(a) | Remote biometric identification (Fernidentifizierung) | Facial recognition in public spaces |
| Nr. 6(a) | Individual risk assessment (Risikobewertung) | Re-offending risk, victimization risk |
| Nr. 6(b) | Polygraph and similar tools | Emotion detection, lie detection |
| Nr. 6(c) | Evidence reliability assessment | Evaluating evidence credibility |
| Nr. 6(d) | Crime risk — profiling | Predictive policing for individuals |
| Nr. 6(e) | Crime analytics | Pattern analysis, organized crime mapping |

**Art. 5 prohibitions particularly relevant:**
- Art. 5(1)(d): Individual criminal risk prediction without factual basis — PROHIBITED
- Art. 5(1)(e): Untargeted facial recognition database scraping — PROHIBITED
- Art. 5(1)(h): Real-time remote biometric identification in public — PROHIBITED (with narrow exceptions)

### Sector-Specific EU Legislation Interaction

| Legislation | Relevance |
|---|---|
| LED (EU) 2016/680 (Law Enforcement Directive) | Data protection for law enforcement processing — replaces GDPR |
| Directive (EU) 2016/681 (PNR) | Passenger Name Record processing — interacts with migration AI |
| Prüm II (proposed) | Cross-border police data exchange — biometric data sharing |
| Schengen Information System (SIS) Regulation | Border alerts — AI matching against databases |

### Practical Compliance Considerations

1. **Art. 5(1)(h) real-time biometric ID:** Prohibited in principle. Three narrow exceptions: (i) targeted search for specific crime victims/missing persons, (ii) preventing specific imminent terrorist threat, (iii) identifying suspect of specific listed criminal offenses. All require prior judicial or independent administrative authorization.
2. **Art. 5(1)(d) profiling prohibition:** Assessing individual criminal risk solely based on profiling or personality traits is prohibited. Risk assessment must be based on objective, verifiable facts linked to criminal activity.
3. **LED replaces GDPR:** Law enforcement processing falls under LED 2016/680, not GDPR. Data protection requirements differ (no consent basis, different lawfulness grounds). However, DPIA equivalent exists under Art. 27 LED.
4. **Post-remote biometric identification (Art. 26(10)):** Deployers of high-risk post-identification systems in law enforcement must obtain prior authorization from judicial authority or independent administrative authority.
5. **National security exclusion:** Art. 2(3) — AI systems used exclusively for military or national defense purposes are excluded entirely. But dual-use systems (police + military) remain in scope.

### Common AI Applications

| Application | Annex Trigger | Likely Risk Level |
|---|---|---|
| Facial recognition (real-time, public) | Art. 5(1)(h) | PROHIBITED (narrow exceptions) |
| Facial recognition (post-identification) | Annex III Nr. 1(a) | High-risk (Art. 6(2)) |
| Individual re-offending risk score | Annex III Nr. 6(a) / Art. 5(1)(d) | High-risk or PROHIBITED |
| Predictive policing (individual) | Art. 5(1)(d) | PROHIBITED |
| Crime hotspot analysis (area-based) | Annex III Nr. 6(e) | High-risk (Art. 6(2)) |
| Lie/emotion detection (interrogation) | Annex III Nr. 6(b) | High-risk (Art. 6(2)) |
| Automated license plate recognition | Annex III Nr. 1(a) possible | Context-dependent |
| Evidence analysis (forensics) | Annex III Nr. 6(c) | High-risk (Art. 6(2)) |

---

## 5. Education (Bildungswesen)

### Annex III Triggers

| Annex III Category | Sub-Category | Typical Education Applications |
|---|---|---|
| Nr. 3(a) | Access determination (Zugang) | AI determining admissions or access to education |
| Nr. 3(b) | Assessment of learning outcomes (Bewertung) | Automated grading, examination scoring |
| Nr. 3(c) | Monitoring and proctoring (Ueberwachung) | AI proctoring, behavior monitoring, cheating detection |

### Sector-Specific EU Legislation Interaction

| Legislation | Relevance |
|---|---|
| GDPR Art. 8 | Child consent — parental consent required for under-16 (varies by Member State, 13-16) |
| GDPR Art. 9 | Special category data — health data of students, biometric data |
| Art. 5(1)(f) AI Act | Emotion recognition in education is PROHIBITED |
| Art. 5(1)(b) AI Act | Exploitation of vulnerabilities (age) — minors are a protected group |
| UN Convention on the Rights of the Child | Best interests of the child — interpretive lens for AI Act |

### Practical Compliance Considerations

1. **Emotion recognition ban:** Art. 5(1)(f) prohibits emotion recognition in educational institutions. This bans AI-based attention monitoring, engagement scoring from facial expressions, or emotional state analysis in classrooms.
2. **Vulnerable groups:** Students — especially minors — are considered vulnerable groups. Art. 5(1)(b) provides heightened protection against exploitative AI practices targeting age-related vulnerabilities.
3. **GDPR child consent:** Processing children's personal data for AI systems in education requires careful legal basis analysis. GDPR Art. 8 sets consent threshold. Many Member States set lower ages (e.g., Germany: 16, Spain: 14, Denmark: 13).
4. **Art. 6(3) exception limited:** Automated grading and admissions decisions typically involve individual assessment and may constitute profiling, making the Art. 6(3) exception unavailable for most Annex III Nr. 3 use cases.
5. **Proctoring AI:** AI-based exam proctoring (behavior analysis, eye tracking, browser monitoring) falls under Nr. 3(c) and is high-risk. If it includes emotion recognition, it is PROHIBITED under Art. 5(1)(f).
6. **Adaptive learning systems:** Personalized learning AI that adapts content based on student performance may trigger Nr. 3(a) or (b) if it determines access to educational levels or assesses learning outcomes with real consequences.

### Common AI Applications

| Application | Annex Trigger | Likely Risk Level |
|---|---|---|
| Automated admissions scoring | Annex III Nr. 3(a) | High-risk (Art. 6(2)) |
| Automated essay grading | Annex III Nr. 3(b) | High-risk (Art. 6(2)) |
| AI exam proctoring | Annex III Nr. 3(c) | High-risk (Art. 6(2)) |
| Emotion/attention monitoring | Art. 5(1)(f) | PROHIBITED |
| Adaptive learning platform | Nr. 3(a)/(b) possible | Context-dependent |
| Plagiarism detection | Art. 6(3)(a) possible | Likely not high-risk |
| Administrative scheduling | None | Minimal risk |
| Student chatbot (FAQ) | Art. 50(1) | Limited risk |

---

## Cross-Sector Notes

1. **Profiling trap:** In Healthcare (insurance), Finance, HR, and Law Enforcement, most AI involves profiling of natural persons. The Art. 6(3) exception is effectively unavailable for these sectors' core AI applications.

2. **GPAI in all sectors:** When a sector-specific AI system is built on a GPAI model (e.g., LLM-based clinical assistant, GPT-powered CV screener), BOTH the sector-specific obligations AND the GPAI obligations apply through the value chain.

3. **Multiple Annex triggers:** A single system may trigger multiple Annex III categories (e.g., AI that evaluates employee health data triggers both Nr. 4(b) employment and potentially Nr. 5(b) health insurance). Classify under the highest applicable category.

4. **National implementation:** Member States may adopt national rules that go beyond the AI Act minimum. Always check national AI strategies and implementing legislation for the relevant jurisdiction.
