# AI System Definition — Art. 3(1) AI Act

## Legal Text

**Article 3(1) — Definition of 'AI system':**

> 'AI system' means a machine-based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments.

*German: 'KI-System' bezeichnet ein maschinengestütztes System, das so konzipiert ist, dass es mit unterschiedlichem Grad an Autonomie arbeiten kann und das nach seiner Einführung eine gewisse Anpassungsfähigkeit aufweisen kann, und das für explizite oder implizite Ziele aus den Eingaben, die es erhält, ableitet, wie es Ergebnisse wie Vorhersagen, Inhalte, Empfehlungen oder Entscheidungen generieren kann, die physische oder virtuelle Umgebungen beeinflussen können.*

**Source:** Regulation (EU) 2024/1689, Art. 3(1)
**Aligned with:** OECD AI definition (OECD/LEGAL/0449), ISO 22989:2022

---

## Commission Guidelines on AI System Definition

**Reference:** Commission Guidelines C(2025) 924 final, 6 February 2025

### Key Interpretive Principles

1. **Technology-neutral definition** — not limited to specific techniques (neural networks, expert systems, statistical methods)
2. **Functional approach** — focuses on what the system does, not how it is built
3. **Broad scope intended** — captures systems using machine learning, logic-based approaches, statistical methods, and hybrid approaches
4. **Excludes traditional software** — simple rule-based systems, conventional databases, and basic automation without inference capability are generally not AI systems

### Boundary Cases (from Commission Guidelines)

**Likely AI systems:**
- Machine learning models (supervised, unsupervised, reinforcement)
- Deep learning / neural networks
- Natural language processing systems
- Computer vision systems
- Recommender systems using collaborative filtering or content-based learning
- Robotic process automation with adaptive/learning components
- Expert systems with learning capability

**Likely NOT AI systems:**
- Simple rule-based automation (if-then-else without learning)
- Conventional databases and search engines (keyword matching)
- Traditional statistical software (descriptive statistics, fixed formulas)
- Basic calculators and spreadsheet formulas
- Static decision trees with no learning component
- Standard business software (ERP, CRM) without AI features

**Gray areas requiring case-by-case analysis:**
- Complex rule-based systems with many interacting rules
- Statistical models with manually tuned parameters
- Heuristic optimization without machine learning
- RPA with limited pattern recognition

---

## Seven-Criteria Analysis Framework

### Criterion 1: Machine-Based Operation (Maschinengestütztes System)

**Definition:** The system is operated by or relies on machine-based (computational) processes.

**Assessment questions:**
- Does the system use hardware and/or software to process information?
- Is it implemented as computer code, firmware, or embedded system?
- Does it run on digital computing infrastructure?

**Threshold:** Very low — virtually all software and digital systems meet this criterion. Only purely mechanical or manual processes are excluded.

**Examples:**
- YES: Any software application, cloud service, embedded controller
- NO: Paper-based checklist, mechanical thermostat, analog gauge

---

### Criterion 2: Degree of Autonomy (Autonomiegrad)

**Definition:** The system is designed to operate with varying levels of autonomy — i.e., some degree of independence from human intervention.

**ISO 22989 Autonomy Scale:**

| Level | Name (DE) | Name (EN) | Description | Example |
|-------|-----------|-----------|-------------|---------|
| 0 | Keine Automatisierung | No automation | Operator controls completely | Manual data entry |
| 1 | Assistenz | Assistance | System suggests, human decides | Spell checker, autocomplete |
| 2 | Teilautomatisierung | Partial automation | Some subfunctions automated, human controls overall | Auto-formatting with approval |
| 3 | Bedingte Automatisierung | Conditional automation | Autonomous in specific contexts, human ready to intervene | Cruise control, chatbot with escalation |
| 4 | Hohe Automatisierung | High automation | Operates parts of mission without intervention | Autopilot with monitoring |
| 5 | Volle Automatisierung | Full automation | Completes entire mission without intervention | Fully autonomous processing pipeline |
| 6 | Autonomie | True autonomy | Adapts goals without oversight | Self-directed AI (theoretical) |

**Assessment questions:**
- Can the system operate without continuous human input?
- At what level does human oversight occur?
- Can the system proceed with a task after initial activation without further instruction?

**Threshold:** Level 1+ satisfies this criterion. The system must exhibit some degree of autonomous operation, but it need not be fully autonomous. Even assistance-level systems (Level 1) can meet this criterion if combined with other AI characteristics.

**Classification criteria for autonomy degree:**
1. External oversight presence/absence (human-in-the-loop, -on-the-loop, -out-of-the-loop)
2. Situational understanding degree
3. Responsiveness to environmental changes
4. Task completion continuity
5. Adaptability degree
6. Performance self-assessment capability
7. Proactive decision/planning capability

---

### Criterion 3: Adaptability After Deployment (Anpassungsfähigkeit)

**Definition:** The system may exhibit adaptiveness after deployment — it can change its behavior based on new data or experience.

**Assessment questions:**
- Does the system learn from new data after initial deployment?
- Can it adjust its parameters, weights, or decision boundaries over time?
- Does user interaction change the system's future behavior?
- Is there continuous learning, online learning, or reinforcement learning after deployment?

**Important:** The regulation says "may exhibit" — adaptability is possible, not required. A system can still be an AI system even if it does not adapt after deployment (e.g., a frozen ML model). This criterion asks whether the system has the capacity to adapt.

**Examples:**
- YES (strong): Recommender system that learns from user clicks; NLP model with RLHF
- YES (moderate): System that is periodically retrained with new data
- YES (weak): System that adjusts thresholds based on feedback
- NO: Frozen model with fixed weights deployed without any update mechanism

---

### Criterion 4: Explicit or Implicit Goals (Ziele)

**Definition:** The system operates toward explicit or implicit objectives.

**Assessment questions:**
- Does the system have a defined purpose or objective function?
- Are goals programmed explicitly (e.g., "classify emails as spam/not spam")?
- Are goals implicit in training data or learned optimization objectives?
- Could the system's purpose be described as achieving a particular outcome?

**Distinction:**
- **Explicit goals:** Programmed objectives, defined KPIs, stated classification targets
- **Implicit goals:** Learned objectives from training data patterns, optimization of loss functions, emergent behavior from training process

**Threshold:** Very broad — almost any purposeful system has goals. The key is that the system is directed toward producing some desired outcome, whether that outcome is explicitly specified or implicitly learned.

---

### Criterion 5: Inference Capability (Ableitungsfähigkeit)

**Definition:** The system infers from input how to generate outputs — it derives outputs through a process beyond simple deterministic rules.

**This is the key distinguishing criterion between AI and traditional software.**

**Assessment questions:**
- Does the system go beyond executing fixed if-then-else rules?
- Does it make predictions, extrapolations, or generalizations?
- Can it process inputs it has not been explicitly programmed to handle?
- Does it use statistical, probabilistic, or learned models to produce outputs?
- Can it handle novel situations not explicitly covered in its programming?

**Inference includes:**
- Statistical inference (regression, classification, clustering)
- Probabilistic reasoning (Bayesian networks, probabilistic programming)
- Neural network forward passes (pattern recognition, feature extraction)
- Logical inference with uncertainty (fuzzy logic, probabilistic logic)
- Learned representations applied to new data

**Inference excludes:**
- Deterministic lookup tables
- Fixed decision trees without learning
- Simple threshold comparisons
- Exact string matching
- Pre-computed response tables

---

### Criterion 6: Output Generation (Ergebniserzeugung)

**Definition:** The system generates outputs such as predictions, content, recommendations, or decisions.

**Output types (non-exhaustive):**

| Output Type | Description | Examples |
|-------------|-------------|---------|
| Predictions | Forecasts or estimates of future states | Credit risk scores, demand forecasts, disease probability |
| Content | Generated text, images, audio, video | ChatGPT responses, DALL-E images, voice synthesis |
| Recommendations | Suggested actions or choices | Product recommendations, treatment suggestions, route planning |
| Decisions | Determinations or classifications | Spam filtering, loan approval, fraud detection |

**Assessment questions:**
- What does the system produce as output?
- Does the output fall into predictions, content, recommendations, or decisions?
- Is the output more than a simple data retrieval or fixed calculation?

---

### Criterion 7: Environmental Influence (Umgebungseinfluss)

**Definition:** The outputs can influence physical or virtual environments.

**Assessment questions:**
- Does the system's output affect the physical world? (e.g., controlling actuators, robots, devices)
- Does it affect virtual environments? (e.g., modifying user interfaces, filtering content, triggering processes)
- Does the output reach end users or other systems that act on it?
- Could the output change someone's experience, choices, or opportunities?

**Physical environment examples:**
- Robot movements, autonomous vehicle control, smart home adjustments, manufacturing control

**Virtual environment examples:**
- Content filtering, search result ranking, personalized interfaces, automated email responses, chatbot interactions, recommendation displays

**Threshold:** Broad — virtually any system whose outputs are consumed by humans or other systems meets this criterion.

---

## Summary Assessment Logic

A system qualifies as an AI system under Art. 3(1) when it cumulatively:
1. Is machine-based (Criterion 1) — almost always met
2. Operates with some autonomy (Criterion 2) — Level 1+ on ISO 22989 scale
3. May adapt after deployment (Criterion 3) — capacity, not requirement
4. Has goals, explicit or implicit (Criterion 4) — almost always met
5. **Performs inference** (Criterion 5) — key distinguishing factor
6. Generates outputs (predictions, content, recommendations, decisions) (Criterion 6)
7. Can influence environments (Criterion 7) — broad threshold

**Critical criterion:** Criterion 5 (inference) is typically the decisive factor. A system that performs genuine inference — going beyond deterministic rules to generalize, predict, or derive outputs from learned patterns — is likely an AI system if it also meets the other criteria.

**Practical test:** If the system uses machine learning, deep learning, or statistical models to produce its outputs, it is very likely an AI system. If it uses only fixed rules without learning or inference, it is very likely not an AI system. Gray areas exist for complex heuristic systems and advanced rule-based expert systems.
