# Art. 6(1) + Annex I — Practitioner Digest

**Source:** Commission Draft Guidelines on the classification of high-risk AI systems under Article 6 AI Act (2026 draft for stakeholder consultation), Section III. Full text: the Commission Draft Guidelines on Art. 6 classification (2026), Annex I section.

## 1. The cumulative-conditions framing (¶27)

Article 6(1) lays down **two cumulative conditions** that must both be satisfied for an AI system to be high-risk under this branch:

1. The AI system is intended to be used as a **safety component** of a product, OR the AI system **itself is a product**, covered by the Union harmonisation legislation listed in Annex I.
2. The product whose safety component is the AI system, or the AI system itself, is required to undergo a **third-party conformity assessment**.

Both conditions must hold. Failure of either drops the system out of Art. 6(1) (it may still qualify under Art. 6(2)/Annex III).

Coverage by Annex I legislation alone is a necessary but **not sufficient** condition. This is the most common misconception in practice — see ¶21 and the smart-thermostat example in ¶48–49.

## 2. AI system as product itself vs safety component

### 2.1 AI system as the product itself (¶30)

An AI system is the regulated product itself where it:
- Is independently placed on the market,
- Has its own intended purpose, and
- Is directly regulated by Annex I legislation.

Example: under Regulation (EU) 2023/1230 (Machinery Regulation), the definition of machinery-related products explicitly includes certain software — which may therefore itself be a regulated product and high-risk under Art. 6(1) if third-party conformity assessment is required.

### 2.2 AI system as safety component (¶31)

An AI system is a safety component where it is, or is intended to be, part of a regulated product — even if placed on the market independently of that product. The AI system must be evaluated as part of the product's overall safety assessment under the relevant Annex I legislation.

## 3. The Art. 3(14) two-prong test (¶¶32–49)

Art. 3(14) defines safety component as *"a component of a product or of an AI system which fulfils a safety function for that product or AI system, or the failure or malfunctioning of which endangers the health and safety of persons or property"*.

This is an **autonomous AI Act definition** (¶33). It is independent of sector-specific definitions of "safety component" in Annex I legislation.

The definition lays down **two alternative scenarios** (¶34). Either is sufficient.

### Scenario (i) — Safety function (intent-based, ¶¶35–37)

The system constitutes a safety component if the provider's intended purpose is to **prevent or mitigate risks to health and safety of persons or property**. Use the ¶37 box checklist — see [safety-function-checklist.md](safety-function-checklist.md) for the full taxonomy.

Key tells:
- Preventive functions: monitoring/detection of harm-leading situations, prevention of physical harm, supervision of another safety system.
- Mitigation functions: control or limitation of physical harm, mitigation of consequences (e.g., safe-stop), control of another safety system.
- NOT safety functions: performance optimisation, service efficiency, automation of user decisions, comfort/convenience.

### Scenario (ii) — Failure or malfunctioning (consequences-based, ¶¶38–43)

The system constitutes a safety component if its failure or malfunctioning **could endanger** the health and safety of persons or property.

Failure modes (¶39): incorrect outputs (false positives/negatives), loss of function/availability, performance instability/drift, timing/latency errors, misclassification leading to hazardous control decisions.

The likelihood must be more than theoretical (¶39). Failures can stem from internal faults (e.g., programming error) or external influences (e.g., unforeseen input data format).

Endangerment (¶40) means an increase in hazard. It does **not** include reputational harm, purely financial loss, minor service degradation, or inconvenience without safety hazard.

Critical point: a system with **only efficiency / comfort intent** may still qualify as a safety component under prong (ii) if its failure could endanger health, safety, or property (¶42; gas appliance carbon-monoxide example in ¶43).

## 4. Third-party conformity assessment requirement (¶¶50–59)

The product (or the AI system if it is the product) must be required to undergo a third-party conformity assessment under the Annex I legal act.

### Module-by-module reference (Decision 768/2008/EC; ¶¶53–55)

| Module | Notified body involvement | Counts as third-party? |
|--------|---------------------------|------------------------|
| **A** (pure internal control) | None | NO — unless conditioned on mandatory harmonised standards |
| **A1, A2** | Production phase only (notified body or in-house body) | YES (in production phase) |
| **B** (design phase) | Required in design phase | YES — always combined with C1/C2/D/E/F |
| **C** | Not required alone | Always combined with notified-body modules |
| **C1, C2** | Required (specific aspects) | YES |
| **D, D1, E, E1, F, F1** | Required | YES |
| **G** | Required | YES |
| **H, H1** | Required (design + production) | YES |

### Module A with mandatory harmonised standards (¶¶56–57)

In some Annex I legislation (Toys Safety Regulation, Machinery Regulation, Radio Equipment Regulation), the use of Module A is conditioned on the manufacturer applying harmonised standards published in the Official Journal that cover all relevant health and safety requirements.

In these cases, **the procedural flexibility to choose Module A does NOT affect high-risk classification** (¶57). The system is still high-risk under Art. 6(1). This is the explicit clarification in Toys Safety Reg. Recital 15 (cited in ¶59) and applied analogously to Machinery Reg. Art. 25(2)/(3).

### Decisive factor (¶58)

The decisive factor is whether the product is subject to enhanced regulatory scrutiny before lawful placing on market, due to potential impact on public interests (health, safety, environment) — whether through third-party CA or through internal control subject to **mandatory harmonised standards**.

## 5. Section A vs Section B distinction (¶60)

Once high-risk under Art. 6(1) is established, the applicable AI Act regime depends on which **section** of Annex I the legal act is in:

- **Section A — NLF-based legislation** → **full Chapter III** applies (Art. 8–17 quality/risk/data/transparency/oversight/accuracy etc., conformity assessment integration via Art. 8(2), 102–109).
- **Section B — other Union harmonisation legislation** (aviation, automotive, rail, agricultural vehicles, etc.) → only **Art. 6(1), 102–109, 112** apply per Art. 2(2) AI Act.

See [annex-i-section-a-vs-b.md](annex-i-section-a-vs-b.md) for the full mapping.

## 6. Worked examples consolidated

### Safety-function path (¶45) — high-risk under prong (i)

- Machinery: AI vision detecting human presence in robot cell, triggering safe stop.
- ATEX equipment: AI monitoring gas concentrations, commanding shutdown.
- Pressure equipment: AI predicting runaway pressure, actuating shutdown.
- Rail: AI monitoring speed/preventing collisions and derailments.

### Failure-based path (¶46) — high-risk under prong (ii)

- Lifts: AI for door closing/obstacle detection (efficiency intent; malfunction injures).
- Vehicles: lane-assist AI (UX intent; malfunction causes collision).
- Agriculture: chemical-spray targeting AI (optimisation intent; failure endangers nearby persons).

### NOT safety components (¶47)

- Toys: AI recommending music in a connected toy.
- Agriculture: AI in drone for yield forecasting or irrigation optimisation (where failure does not endanger).

### Borderline / vulnerable-user cases (¶48 footnote 5)

Default rule for consumer smart appliances (thermostats, washing machines, air purifiers, refrigerators, TVs) is **NOT** a safety component. Exception: smart door locks, child-lock functions, devices used by/around children or vulnerable users may qualify under the failure-based prong.

### Smart thermostat (¶49)

Default: NOT a safety component (comfort/efficiency intent; failure produces inconvenience or higher bills, not endangerment).
Exception: if the thermostat performs a safety function (e.g., child-lock) or where failure could endanger health/safety, it does qualify.

## 7. Compliance-burden minimisation (¶¶60–62)

The AI Act provides mechanisms to integrate AI-specific risks into existing sectoral compliance frameworks:

- **Art. 8(2)** — interplay with sectoral legislation: AI Act requirements can be integrated into existing sectoral conformity-assessment processes.
- **Art. 9(10)** — risk management: AI-specific risks may be added into existing risk management systems.
- **Art. 17(3)** — quality management: AI-specific quality requirements may be integrated into existing QMS.
- **Art. 40** — harmonised standards: AI Act harmonised standards must be consistent with standards developed under Annex I legislation.

For Section A AI systems, single-framework compliance is therefore the design intent (avoiding duplication of effort between AI Act and sectoral requirements).

---

## Sources

- Commission Guidelines Annex I (full text): the Commission Draft Guidelines on Art. 6 classification (2026), Annex I section
- Art. 6(1), Art. 3(14) (safety component), Art. 2(2) (Section B scope), Art. 8(2), Art. 9(10), Art. 17(3), Art. 40 AI Act
- Decision 768/2008/EC — conformity assessment modules
- Blue Guide 2022 (2022/C 247/01) — NLF guidance
