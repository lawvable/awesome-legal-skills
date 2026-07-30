# Parallel Reporting Regimes — Screening Reference

A personal data breach frequently triggers reporting or involvement duties **outside** the GDPR. This reference supports the Sectoral Parallel-Regime Screen in SKILL.md: identify candidate regimes, state them in the output, and analyse in depth **only on request**. Standard output line:

> **Potential parallel regimes identified:** [list] — not assessed in detail unless requested.

---

## 1. EU AI Act — Art. 73 Serious Incident Reporting (in depth)

**Who:** Providers of **high-risk AI systems** (Annex III stand-alone systems; Annex I product-embedded systems). Deployers have a duty to inform the provider (and, where the provider cannot be reached, take over reporting duties per Art. 73(4)).

**Trigger — "serious incident", Art. 3(49):** an incident or malfunctioning of an AI system that directly or indirectly leads to:
- (a) the **death of a person, or serious harm to a person's health**;
- (b) a **serious and irreversible disruption of the management or operation of critical infrastructure**;
- (c) the **infringement of obligations under Union law intended to protect fundamental rights**;
- (d) **serious harm to property or the environment**.

Note (c): a significant GDPR breach caused by a high-risk AI system can itself constitute a serious incident — assess this limb whenever the AI SYSTEM flag is set.

**To whom:** the **market surveillance authority of the Member State(s) where the incident occurred** — not the data protection SA (unless the Member State designated the same body).

**Deadlines (Art. 73(2)–(5)):**

| Situation | Deadline |
|-----------|----------|
| General rule | Immediately after establishing a **causal link** between the AI system and the incident (or the reasonable likelihood of one); at the latest **15 days** after the provider/deployer becomes aware |
| **Widespread infringement**, or serious incident under Art. 3(49)(b) (critical infrastructure) | Immediately; at the latest **2 days** after awareness |
| **Death** of a person | Immediately after the causal link is established/suspected; at the latest **10 days** after awareness |
| Incomplete information | An **initial incomplete report followed by a complete report** is permitted where necessary to ensure timely reporting |

After reporting: the provider performs the necessary investigations (incl. risk assessment of the incident and corrective action) and must not alter the system or evidence in a way that affects the evaluation before informing the authority.

**Applicability:** Art. 73 obligations apply from **2 August 2026**. High-risk systems that are products (or safety components) under the Annex I sectoral legislation follow the **2 August 2027** application date, and Art. 73(9)–(10) defer to equivalent sectoral incident-reporting regimes (e.g., MDR/IVDR for medical devices) for some categories — for those, only limb (c) fundamental-rights incidents are reported under the AI Act. **Before the applicable date, present the duty as "applies from", never as live.**

**Relationship to GDPR:** fully parallel — separate trigger, recipient, deadline, and content. A breach can require GDPR Art. 33 notification (72h, data protection SA) AND Art. 73 reporting (15/10/2 days, market surveillance authority) simultaneously.

---

## 2. Screening Table — Other Regimes

| Regime | Who / Trigger | Screen Questions | Note |
|--------|---------------|------------------|------|
| **NIS2** (Directive 2022/2555 + national implementation) | Essential/important entities (energy, transport, health, digital infrastructure, ICT services, etc.) with a **significant incident** | Is the organisation in scope of NIS2 / its national implementation? Does the incident significantly affect service provision? | Separate track with its own early-warning (24h) / incident-notification (72h) / final-report cadence to the CSIRT or national cyber authority — **if the `nis2-navigator` skill is available, use it for this track**; the GDPR and NIS2 reports are parallel, not substitutes |
| **DORA** (Regulation 2022/2554) | Financial entities (banks, insurers, investment firms, crypto, ICT third-party providers) with **major ICT-related incidents** | Is the entity financial-sector regulated? Does the incident meet DORA's classification criteria? | Reporting to the financial supervisor on its own timeline; client notification duties may also arise |
| **eIDAS** (Regulation 910/2014, as amended) | Trust service providers | Is the organisation a (qualified) trust service provider? Does the incident significantly impact the trust service or its data? | Notify the supervisory body (and affected parties where relevant) without undue delay, in any event within 24h of awareness |
| **ePrivacy / telecoms** | Providers of publicly available electronic communications services | Is the breached service a public ECS? | Sector-specific breach notification (in DE via TDDDG/TKG; BfDI competence) runs alongside GDPR |
| **Criminal law** | Any victim of a criminal act (hacking, extortion, theft) | Malicious external/internal actor? Ransom demand? | Police/judicial report is voluntary but is an explicit EDPB template field (§6.1); coordinate timing with counsel; preserves evidence chain |
| **Insurance** | Cyber / D&O policies | Does a policy cover the incident? | Notification clauses often have **short windows and forfeiture risk**; check immediately, even before coverage analysis |
| **Contracts** | Customer / partner agreements beyond DPAs | Do MSAs, SLAs, or security addenda require incident notice? | Contractual notice duties are independent of GDPR thresholds — a non-notifiable breach can still be contractually notifiable |
| **Employment / works council** | Employee data affected (esp. Germany) | Is employee personal data involved? Is there a works council? | Co-determination and information rights (e.g., BetrVG) may attach to the incident response and monitoring measures; involve HR/labour counsel |

---

## 3. Output Discipline

1. Screen all rows above in every assessment; list only the plausible hits.
2. Add the result to the Assessment Dashboard ("Parallel Regimes" row) and to **§6.1 of the EDPB evidence file** (other authorities notified — name the authority and its case ID once notified).
3. Do **not** assess any parallel regime in depth unless the user asks — state that explicitly.
4. Deadlines under parallel regimes can be **shorter** than the GDPR's 72h (NIS2 early warning 24h, eIDAS 24h, insurance windows) — when a hit is plausible, say so prominently.
