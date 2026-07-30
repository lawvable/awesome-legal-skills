# Classification Case Studies

Five worked examples applying the Art. 3(1) AI system test and risk classification framework. Each case study references the classification methodology in the parent SKILL.md and supporting reference files.

---

## Case Study 1: Smart Home Thermostat (Minimal Risk)

### Scenario
A smart thermostat learns household heating patterns and automatically adjusts temperature. It uses sensor data (temperature, humidity, occupancy) and learns user preferences over time. Sold directly to consumers under the manufacturer's brand.

### Art. 3(1) AI System Test

| # | Criterion | Met? | Reasoning |
|---|-----------|------|-----------|
| 1 | Machine-based operation | Yes | Software running on embedded hardware |
| 2 | Degree of autonomy | Level 3 | Operates autonomously in heating context, user can override |
| 3 | Adaptability after deployment | Yes | Learns user patterns through reinforcement from usage data |
| 4 | Explicit or implicit goals | Yes | Implicitly learned goal: maintain comfort while minimizing energy |
| 5 | Inference capability | Yes | Predicts optimal temperature schedules based on learned patterns |
| 6 | Output generation | Yes | Generates heating control decisions (predictions + decisions) |
| 7 | Environmental influence | Yes | Directly controls physical environment (temperature) |

**Determination:** IS an AI system under Art. 3(1).

### Risk Classification

| Step | Analysis | Result |
|---|---|---|
| Art. 5 Prohibited Practices | No prohibited practice applicable — no manipulation, no biometric processing, no social scoring | Clear |
| Annex I Product Safety | Not a product covered by Annex I harmonization legislation (not a machinery, medical device, etc.) | Not applicable |
| Annex III Application-Based | Not used for biometrics, critical infrastructure management, employment, essential services, law enforcement, migration, justice, or education | Not applicable |
| GPAI Model | Not based on a GPAI model — purpose-built narrow ML system | Not applicable |
| Art. 50 Transparency | Does not interact with persons conversationally, does not generate synthetic content | Not applicable |

**Classification: Minimal risk** — Only Art. 4 AI competence obligation applies to the provider.

### Key Takeaway
Not every AI system is high-risk. A smart thermostat, despite being a genuine AI system with learning capabilities, does not trigger any Annex I or Annex III category and has no Art. 50 transparency trigger. It falls in the minimal risk category.

---

## Case Study 2: HR Screening Tool (High-Risk)

### Scenario
A SaaS provider offers an AI-powered CV screening tool that ranks job applicants based on qualification matching, experience scoring, and cultural fit prediction. The tool processes applicant CVs, generates a ranking score (1-100), and flags top candidates. Used by corporate HR departments across the EU.

### Art. 3(1) AI System Test

| # | Criterion | Met? | Reasoning |
|---|-----------|------|-----------|
| 1 | Machine-based operation | Yes | Cloud-based software processing |
| 2 | Degree of autonomy | Level 2-3 | Automated scoring with human review of results |
| 3 | Adaptability after deployment | Yes | Learns from hiring outcomes to refine scoring |
| 4 | Explicit or implicit goals | Yes | Explicit goal: rank candidates by suitability |
| 5 | Inference capability | Yes | Infers candidate quality beyond simple keyword matching |
| 6 | Output generation | Yes | Generates ranking scores and recommendations |
| 7 | Environmental influence | Yes | Influences hiring decisions (virtual environment) |

**Determination:** IS an AI system under Art. 3(1).

### Risk Classification

| Step | Analysis | Result |
|---|---|---|
| Art. 5 Prohibited Practices | No subliminal manipulation, no exploitation of vulnerabilities. Cultural fit prediction may raise Art. 5(1)(a) concerns if it manipulates — but typically not prohibited if transparent | Clear (monitor) |
| Annex I Product Safety | Not a product under Annex I harmonization legislation | Not applicable |
| Annex III Nr. 4(a) | **YES** — AI system intended to be used for recruitment, specifically for screening or filtering applications and evaluating candidates | **Triggered** |
| Art. 6(3) Exception check | System ranks and scores candidates → not a narrow procedural task (a), not improving completed human activity (b), not just pattern detection (c), not merely preparatory (d) — it effectively pre-selects candidates | Exception does NOT apply |
| Art. 6(3) Profiling check | System evaluates personal aspects (performance, qualifications) of individual persons → profiling present → exception blocked regardless | Profiling confirmed |

**Classification: High-risk (Art. 6(2), Annex III Nr. 4(a))** — Full Chapter III, Section 2 obligations apply.

### Key Takeaway
HR screening tools that rank, score, or filter candidates are textbook Annex III Nr. 4(a) high-risk systems. The Art. 6(3) exception is doubly blocked: (1) the task is substantive, not narrow/procedural, and (2) profiling is present, which independently blocks the exception.

---

## Case Study 3: Customer Service Chatbot (Limited Risk)

### Scenario
An e-commerce company deploys a GPT-4-based customer service chatbot on its website. The chatbot answers product questions, processes return requests, and provides order status updates. It does not make decisions about credit, employment, or access to services — it provides information and routes complex queries to human agents.

### Art. 3(1) AI System Test

| # | Criterion | Met? | Reasoning |
|---|-----------|------|-----------|
| 1 | Machine-based operation | Yes | Cloud-based LLM processing |
| 2 | Degree of autonomy | Level 3 | Autonomously handles conversations, escalates edge cases |
| 3 | Adaptability after deployment | Limited | Fine-tuned on company data, but does not continuously learn in production (frozen weights) |
| 4 | Explicit or implicit goals | Yes | Goal: answer customer queries accurately |
| 5 | Inference capability | Yes | Generates contextual responses through language model inference |
| 6 | Output generation | Yes | Generates text content (recommendations, answers) |
| 7 | Environmental influence | Yes | Influences customer decisions, modifies digital interface |

**Determination:** IS an AI system under Art. 3(1).

### Risk Classification

| Step | Analysis | Result |
|---|---|---|
| Art. 5 Prohibited Practices | No manipulation, no vulnerability exploitation, no social scoring | Clear |
| Annex I Product Safety | Not a product under Annex I | Not applicable |
| Annex III Application-Based | Customer service does not fall under any Annex III category — not biometrics, critical infrastructure, education, employment, essential services, law enforcement, migration, or justice | Not applicable |
| GPAI Model | Based on GPT-4 (GPAI model) — but GPAI obligations fall on the model provider (OpenAI), not on the deployer. The deployer's system classification is assessed independently | Not triggered for deployer |
| Art. 50(1) Transparency | **YES** — System interacts directly with natural persons (chatbot) | **Triggered** |

**Classification: Limited risk (Art. 50(1))** — Must disclose AI interaction to users.

### Key Takeaway
A chatbot built on a GPAI model (like GPT-4) is not automatically high-risk. The risk classification depends on the *system's* intended purpose and deployment, not on the underlying model. GPAI obligations attach to the model provider through the value chain, while the system deployer's obligations depend on its own classification. Art. 50(1) requires clear disclosure: "You are interacting with an AI system."

---

## Case Study 4: Medical Imaging AI (High-Risk via Annex I)

### Scenario
A startup develops an AI system that analyzes chest X-rays to detect potential pneumonia and lung nodules. The system highlights regions of interest and provides a confidence score. It is CE-marked as a Class IIa medical device under MDR (EU) 2017/745. Radiologists use it as a diagnostic support tool.

### Art. 3(1) AI System Test

| # | Criterion | Met? | Reasoning |
|---|-----------|------|-----------|
| 1 | Machine-based operation | Yes | Deep learning model on dedicated hardware |
| 2 | Degree of autonomy | Level 2 | Provides analysis, radiologist makes final diagnosis |
| 3 | Adaptability after deployment | No | Frozen model weights — updates only via new version releases |
| 4 | Explicit or implicit goals | Yes | Explicit: detect and highlight potential pathologies |
| 5 | Inference capability | Yes | Infers presence of pathologies from image patterns |
| 6 | Output generation | Yes | Generates predictions (highlighted regions, confidence scores) |
| 7 | Environmental influence | Yes | Influences diagnostic process |

**Determination:** IS an AI system under Art. 3(1).

### Risk Classification

| Step | Analysis | Result |
|---|---|---|
| Art. 5 Prohibited Practices | No prohibited practice applicable | Clear |
| Annex I Nr. 11 Product Safety | **YES** — System is a medical device under MDR (EU) 2017/745 (Annex I, Section A, Nr. 11). AI is a safety component of the medical device | **Triggered** |
| Art. 6(1) | AI system falls under Annex I → high-risk under Art. 6(1). Third-party conformity assessment required if medical device is Class IIa or higher | High-risk |

**Classification: High-risk (Art. 6(1), Annex I Nr. 11)** — Double conformity: both MDR and AI Act requirements apply.

### Key Takeaway
Medical AI classified as a medical device under MDR is high-risk through the Annex I pathway (Art. 6(1)), not through Annex III. This triggers full Chapter III, Section 2 obligations AND MDR obligations. The Art. 6(3) exception is not relevant here — it only applies to Annex III systems. For Annex I systems, high-risk status is automatic upon triggering. Also see [sector-guidance.md](sector-guidance.md) Healthcare section.

---

## Case Study 5: Predictive Maintenance (Minimal/Context-Dependent)

### Scenario
A manufacturing company deploys an AI system that monitors machine vibration data, temperature, and power consumption to predict equipment failures before they occur. The system generates maintenance alerts (e.g., "Motor bearing likely to fail within 14 days — schedule maintenance"). It does not affect workers or public safety — it monitors industrial equipment only.

### Art. 3(1) AI System Test

| # | Criterion | Met? | Reasoning |
|---|-----------|------|-----------|
| 1 | Machine-based operation | Yes | Edge computing + cloud analytics |
| 2 | Degree of autonomy | Level 2 | Generates alerts, maintenance team decides action |
| 3 | Adaptability after deployment | Yes | Continuously learns from new sensor data and failure outcomes |
| 4 | Explicit or implicit goals | Yes | Explicit: predict equipment failures |
| 5 | Inference capability | Yes | Infers failure probability from sensor patterns |
| 6 | Output generation | Yes | Generates predictions (failure forecasts, maintenance recommendations) |
| 7 | Environmental influence | Yes | Triggers maintenance workflows |

**Determination:** IS an AI system under Art. 3(1).

### Risk Classification

| Step | Analysis | Result |
|---|---|---|
| Art. 5 Prohibited Practices | No prohibited practice — monitors machines, not people | Clear |
| Annex I Product Safety | Check: Is the equipment monitored covered by Annex I? If the AI is a safety component of machinery under Machinery Regulation (EU) 2023/1230 → may trigger. If standalone monitoring → likely not | Context-dependent |
| Annex III Nr. 2 Critical Infrastructure | Check: Is the monitored equipment part of critical digital or physical infrastructure (energy, water, transport)? If yes → Annex III Nr. 2 may apply | Context-dependent |
| GPAI / Art. 50 | Not GPAI-based, does not interact with natural persons | Not applicable |

**Classification (standard factory):** Minimal risk — no Annex I or III trigger if monitoring standard manufacturing equipment.

**Classification (critical infrastructure):** Potentially high-risk if monitoring energy grid components, water treatment systems, or transport infrastructure (Annex III Nr. 2).

### Key Takeaway
Predictive maintenance is a clear example of context-dependent classification. The same technology monitoring a factory conveyor belt is minimal risk, but monitoring a power grid transformer is potentially high-risk under Annex III Nr. 2. Always assess the deployment context, not just the technology. If the AI is a safety component of machinery, also check Annex I.
