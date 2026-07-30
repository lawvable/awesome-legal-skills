# Annex III Area 2 — Critical infrastructure

**Annex III citation:** Nr. 2
**Effective date:** 2 December 2027 (per AI Omnibus)
**Source:** Commission Guidelines Annex III, Area 2 section. Full text: the Commission Draft Guidelines on Art. 6 classification (2026), Annex III section.

## Scope of the area

Annex III Nr. 2 covers AI systems intended to be used as **safety components** in the management and operation of six critical-infrastructure sub-sectors: critical digital infrastructure, road traffic, supply of water, supply of gas, supply of heating, and supply of electricity. This is the **only Annex III area** that uses the "safety component" framing — Art. 3(14) AI Act applies here in the same way it does inside the Annex I product-safety branch under Art. 6(1). Recital 55 AI Act explains the rationale: failure or malfunctioning of such a system could endanger life and health at scale and cause appreciable disruption of essential social and economic activities.

Two conditions must both be satisfied for an AI system to fall within Nr. 2. **First**, the system must qualify as a safety component within the meaning of Art. 3(14) AI Act — meaning it must perform a **direct protective function** for the physical integrity of the infrastructure, not merely a supportive, informational, organisational, or optimisation-oriented role. The Commission Guidelines (¶184) enumerate six concrete safety functions (detection, predictive maintenance with direct safety link, prevention, control/limitation, mitigation, supervision of another safety system). **Second**, the system must be intended to be used by an **entity identified as critical under Directive (EU) 2022/2557 (the CER Directive)** — Art. 3(62) AI Act cross-refers to that directive, and Delegated Regulation (EU) 2023/2450 lists the essential services for each sub-sector.

Important horizontal points: (a) cybersecurity-only AI systems are **excluded** from Nr. 2 by Recital 55 — a "cybersecurity component" is not a "safety component" in the Annex III sense (unlike the Annex I context where cybersecurity components have their own carve-out logic); (b) **nuclear-specific safety components are out of scope** (¶205–¶206) — they are governed by Euratom and other nuclear-specific Union law, though electricity-side components of nuclear plants can fall in; (c) NIS2 Directive (Directive (EU) 2022/2555) scope substantially overlaps with the critical digital infrastructure prong here — operators that are NIS2 essential/important entities are frequently also CER-identified critical entities, and deployers should coordinate with a NIS2 scoping assessment where relevant. Purely operational/efficiency/admin AI (load forecasting, ticket triage, predictive maintenance without a direct safety link, network optimisation) falls outside Nr. 2 even when used by a critical entity.

## Sub-categories

- **Nr. 2 — Critical digital infrastructure** — AI safety components used by CER-identified IXP providers, DNS providers, TLD registries, cloud providers, data-centre operators, CDN providers, trust-service providers, electronic-communications providers/networks (Art. 2(8) CER Delegated Regulation).
- **Nr. 2 — Road traffic** — AI safety components used by CER-identified road authorities or Intelligent Transport System (ITS) operators for surface-road network control and management (Art. 2(2)(d) CER Delegated Regulation; waterways excluded).
- **Nr. 2 — Supply of water** — AI safety components used by CER-identified drinking-water suppliers/distributors or by undertakings collecting, treating or disposing of waste water (Art. 2(6)–(7) CER Delegated Regulation).
- **Nr. 2 — Supply of gas** — AI safety components used by CER-identified gas supply, distribution, transmission, storage, LNG, production, purchase, refining and treatment operators (Art. 2(1)(d) CER Delegated Regulation; oil sub-sector excluded).
- **Nr. 2 — Supply of heating** — AI safety components used by CER-identified operators of district heating or district cooling (Art. 2(1)(b) CER Delegated Regulation).
- **Nr. 2 — Supply of electricity** — AI safety components used by CER-identified electricity supply undertakings, DSOs, TSOs, producers, NEMOs, demand-response participants, aggregators, energy-storage market participants (Art. 2(1)(a) CER Delegated Regulation; hydrogen sub-sector excluded; nuclear-specific components excluded).

## Practical examples — HIGH-RISK

- **(Critical digital infrastructure)** AI fire-alarm control system in cloud computing centres — direct safety function protecting both physical infrastructure and natural persons (¶191).
- **(Road traffic)** AI real-time translation tool for transport-service employees overcoming language barriers between control centre and drivers / passengers and drivers, contributing to public-transport safety (¶196(a)).
- **(Road traffic)** AI monitoring road traffic and adjusting traffic lights accordingly — directly controls/limits physical harm to road users and surroundings (¶196(a)).
- **(Road traffic)** AI recognising heavy objects on vulnerable bridges and quaysides to prevent collapse — direct protection of physical integrity, comparable to an emergency button (¶196(a)).
- **(Road traffic)** AI linking real-time water-level data to lock management for road traffic in flood-risk scenarios (¶196(a)).
- **(Road traffic)** Intelligent Traffic Control System (iTCS) communicating with road users via telecommunications networks to prioritise users, prevent head-on collisions and chain-reaction accidents (¶196(a)).
- **(Water)** AI pressure sensor inside water-pressure monitoring systems used in distribution of drinking water (¶198(a)).
- **(Water)** AI predicting sewage-system overflow that impacts drinking water (¶198(a)).
- **(Electricity)** AI surveillance and perimeter protection (cameras, radar, drone-control) directly protecting physical integrity of the infrastructure (¶206(a)).
- **(Electricity)** AI anomaly-detection on grid data supporting decision-making for **critical functions** such as power-load distribution, grid stability, or shutdown procedures (¶206(a)).

## Practical examples — NOT HIGH-RISK

- **(Critical digital infrastructure)** AI for trouble-ticket management, customer-tailored network optimisation, AI-assisted technical user-guide interactions, or network-load prediction — service-quality / operational, no direct safety function (¶194(b)).
- **(Road traffic)** AI traffic-flow optimisation platform that analyses real-time data but does not directly trigger safety-relevant traffic-management changes — provides insights only (¶196(b), ¶183).
- **(Road traffic)** AI predictive-maintenance system that is one precautionary measure among several and not essential to safe operation (¶196(b)).
- **(Gas)** AI predictive-maintenance tool for gas-pipeline monitoring — does not directly control safety functions; independent safety systems remain operational (¶200(a)).
- **(Heating)** AI in autonomously moving robots performing predefined patrols and checkpoints in heating plants — detection-only, no preventive/interventive capacity, no safety function (¶202(a)).
- **(Electricity)** AI grid-optimisation by energy-demand forecasting — core safety functions handled separately (¶206(b)).
- **(Electricity)** AI cybersecurity monitoring for energy-grid networks — cybersecurity-only, excluded by Recital 55 (¶206(b)).
- **(Electricity)** AI quality-assurance of meter installation from images — recommendations to human worker only (¶206(b)).
- **(Electricity)** AI incident detection for precautionary outage prevention — precautionary, advisory, no direct safety function; even an erroneous warning does not by itself create an outage (¶206(b)).
- **(Electricity)** AI forecasting grid imbalances at 15-minute intervals to support operational planning — no direct link between system output and potential physical harm (¶206(b)).
- **(Critical digital infrastructure)** AI "mere conduit" passively conveying traffic or data without control or decision-making over content/destination (¶182).
- **(Cross-cutting cybersecurity examples — out of scope)** AI honeypot systems, AI engagement with attackers to learn attack patterns, AI detecting unauthorised password access, AI detecting suspicious email addresses / stolen data — solely cybersecurity, excluded by Recital 55 (¶187).

## Safety-component framing

Annex III Nr. 2 applies the same Art. 3(14) two-prong test that governs Annex I AI systems under Art. 6(1):

- **Scenario (i) — Safety function** (intent-based). The AI system must be **intended** to perform a direct protective function for the physical integrity of the critical infrastructure. The Commission Guidelines ¶184 list six qualifying safety functions: (a) monitoring/detection of situations that may directly lead to physical harm; (b) monitoring/detection of maintenance needs whose neglect would directly threaten physical integrity; (c) prevention (e.g., blocking start-up if abnormal behaviour detected); (d) control/limitation (adjusting infrastructure function in response to risk); (e) mitigation (e.g., triggering a safe stop); (f) supervision of another safety system. See [safety-function-checklist.md](safety-function-checklist.md) for the operational test.
- **Scenario (ii) — Failure or malfunctioning** (consequences-based). Even where the system is not labelled as a safety component, malfunction-driven failure that directly endangers life, health, or physical integrity at scale can bring the system within scope (Recital 55).

Operational, efficiency, optimisation, advisory, informational, organisational, or "mere conduit" AI that does **not** perform such a direct protective function falls outside Nr. 2 — even when used by a CER-identified critical entity. Conversely, **cybersecurity-only** AI is excluded by Recital 55 even where a malfunction could in theory affect operations; the carve-out for cybersecurity components only exists in the Annex I context (Art. 6(1)), not inside Annex III.

The availability of a **redundant or backup safety system** that itself directly protects physical integrity is a factor when judging whether the AI system in question genuinely performs a safety function (¶186). If the protective function depends on the AI, that strengthens the safety-component classification; if the AI is one precautionary measure among many independently operational safety safeguards, that points away from high-risk.

## Common Art. 6(3) exception scenarios

The Art. 6(3) exceptions are **typically unavailable** for genuine Nr. 2 safety components, for a structural reason: where an AI system has been correctly characterised as a safety component performing a direct protective function for critical infrastructure, it inherently poses a significant risk to health, safety, or fundamental rights, and it is by definition material to the operator's decision-making about how to protect that infrastructure. The Commission Guidelines explicitly flag this in the cloud-centre fire-alarm example (¶191): "None of the exceptions listed in Article 6(3) AI Act apply to such a system due to its role in preventing direct damage to the physical infrastructure of the centre, as well as harm to natural persons." See [art-6-3-exception-decision-tree.md](art-6-3-exception-decision-tree.md) for the full test.

The correct gating question for Nr. 2 is therefore usually upstream: **is the system actually a safety component used by a CER-identified critical entity?** If yes, expect high-risk classification. If no, the system is outside Nr. 2 entirely — there is no need to invoke Art. 6(3).

## Common profiling considerations

Profiling-of-natural-persons exposure is **generally low** in this area. Most Nr. 2 systems operate on infrastructure-level telemetry — sensor data, network traffic flows, grid load curves, pressure readings, traffic-control parameters — rather than on personal data of identified or identifiable individuals. The Art. 6(3) profiling re-exception (which automatically reinstates high-risk status whenever the AI profiles natural persons) is therefore rarely engaged in practice for this area, both because Art. 6(3) is rarely available here in the first place (see above) and because the underlying data is largely non-personal.

The principal exception is **end-user-facing infrastructure data**, for example smart-meter data tied to individual household consumption patterns, ITS systems that ingest individual driver/vehicle data, or electronic-communications metadata flows that can identify subscribers. Where such an AI system is genuinely a safety component (rare for these data flows, but possible — e.g., an ITS that monitors individual vehicle behaviour to trigger collision-avoidance), the profiling carve-out could bite. Deployer-side controllers should in any case run the GDPR Art. 22 analysis independently.

## Cross-references

- [safety-function-checklist.md](safety-function-checklist.md) — operational test for the Art. 3(14) two-prong safety-component definition.
- [art-6-3-exception-decision-tree.md](art-6-3-exception-decision-tree.md) — when (and rarely, in this area) Art. 6(3) exceptions apply.
- [art-6-2-annex-iii-guidelines.md](art-6-2-annex-iii-guidelines.md) — horizontal Commission Guidelines for the Annex III branch.
- Related follow-on activities: **role determination** (provider vs deployer obligations for safety components); **obligation mapping** (Chapter III, Section 2 requirements once classified high-risk); a **NIS2 scoping assessment** (substantial overlap with NIS2 essential/important entity scope in the critical digital infrastructure prong).
- Recital 55 AI Act — distinguishes "safety component" from "cybersecurity component"; cybersecurity-only carve-out exists in the Annex I context, **not** within Annex III Nr. 2.
- Directive (EU) 2022/2557 (CER Directive) and Delegated Regulation (EU) 2023/2450 — defines who counts as a critical entity in each sub-sector; Art. 3(62) AI Act anchors Annex III Nr. 2 to these instruments.
