---
name: "eu-ai-act-high-risk-classifier-oliver-schmidt-prietz"
description: "Depth assessment of whether an AI system is high-risk under Art. 6 of the EU AI Act, grounded in the Commission's draft Art. 6(5) classification guidelines (general principles + Annex I + Annex III). Covers the Annex I product-safety route, all eight Annex III areas with worked examples, the Art. 6(3) exception and its profiling re-exception, and the Art. 25 quasi-provider trap. Outputs a structured decision block, a practitioner memo, and a JSON interchange artefact."
metadata:
  author: "Oliver Schmidt-Prietz"
  license: "agpl-3.0"
  version: "2026-06-09"
---

# EU AI Act High-Risk Classification

Depth assessment of whether an AI system is **high-risk** under **Art. 6 AI Act** (Regulation (EU) 2024/1689), grounded in the European Commission's draft Art. 6(5) classification guidelines (general principles, Annex I, Annex III) published for stakeholder consultation in 2026.

## Disclaimer (show at session start, do not block)

> **Important:** This skill provides structured high-risk classification guidance based on the EU AI Act (Regulation (EU) 2024/1689) and the Commission's draft Art. 6(5) classification guidelines (general principles, Annex I, Annex III) issued for stakeholder consultation. The Commission guidelines are non-binding; authoritative interpretation rests with the Court of Justice of the EU. This is not legal advice. Final classification decisions should involve qualified legal counsel with AI Act expertise.

---

## When to use this skill

- The user has already concluded (via broad risk-tier triage or otherwise) that high-risk is the likely tier and needs the **depth assessment**.
- A high-risk verdict is consequential (FRIA may apply, Chapter III conformity assessment regime, post-market monitoring, registration in EU database).
- The user explicitly asks for Annex I or Annex III analysis.
- The user is uncertain whether a borderline AI system is high-risk and needs the Commission-guideline-grounded reasoning.

If the AI system has not yet been triaged across all five risk tiers (prohibited / high-risk / GPAI / limited / minimal), do that breadth-first triage before the Annex I / Annex III depth analysis below. For a pure article-lookup question without a classification verdict, answer it directly with the cited regulation text rather than running the full depth assessment.

---

## Effective dates (per AI Omnibus 2026)

| Provision | Original date (Art. 113) | **Postponed date (AI Omnibus)** |
|-----------|--------------------------|----------------------------------|
| Art. 6(2) + Annex III obligations | 2 August 2026 | **2 December 2027** |
| Art. 6(1) + Annex I obligations   | 2 August 2027 | **2 August 2028**   |
| Art. 111(2) legacy cut-off        | 2 August 2026 | **2 December 2027** |

See [references/ai-omnibus-timeline-postponements.md](references/ai-omnibus-timeline-postponements.md) for citation chain.

---

## Required inputs

Before beginning, gather from the user:

1. **System description** — what does it do, who built it, who uses it, what is the intended purpose stated by the provider.
2. **Intended-purpose evidence** — instructions for use, technical documentation, promotional materials, terms of service, sales materials. The provider's framing matters per ¶¶10–13 of the general-principles guidelines.
3. **Deployment context** — sector (machinery, medical, employment, education, law enforcement, etc.), is the user the provider, deployer, importer, or distributor.
4. **Modification status** — is the user the original provider or did they fine-tune / rebrand / substantially modify a third-party system (Art. 25 trap).

If any of these is missing, ask before proceeding. Classifications based on incomplete information must be flagged as preliminary.

---

## Decision tree

Run the five steps in order. Each step either terminates with a verdict or feeds the next.

### Step 1 — AI system gating (Art. 3(1))

Confirm the technology meets the Art. 3(1) AI system definition. If it does not (e.g., pure rule-based software with no inference, no learning, no autonomy), the AI Act does not apply → terminate as **not in AI Act scope**. Reference: see Commission Guidelines on the definition of an artificial intelligence system, C(2025) 5053 (separate from these high-risk guidelines).

### Step 2 — Intended-purpose framing (Art. 3(12); general principles ¶¶10–13)

Document the provider's stated intended purpose. Apply the **GPAI / multi-purpose trap** test:

- If the provider's materials present the system as broadly applicable across many contexts and do not consistently exclude high-risk uses → the intended purpose is **deemed** to encompass high-risk uses (¶12).
- Merely asserting in terms-of-service that high-risk use is excluded is **insufficient** if other materials (promotional, examples, product positioning) suggest such uses are feasible and reasonably foreseeable (¶12).
- Capture but exclude from this assessment: Art. 3(13) "reasonably foreseeable misuse" — by definition outside intended purpose.

Output of Step 2: a clean, documented intended-purpose statement to use in Steps 3 and 4.

### Step 3 — Art. 6(1) / Annex I branch

Apply this branch in full **before** Step 4. The two branches are not mutually exclusive: a system can be high-risk under both Art. 6(1) and Art. 6(2) (in which case the Art. 6(1) conformity-assessment integration applies — see Art. 8(2) and Art. 102–109).

#### 3a. Is the AI system a product / safety component under Annex I?

Screen against the Union harmonisation legislation listed in Annex I AI Act (machinery, toys, lifts, ATEX, radio equipment, pressure equipment, recreational craft, cableways, gas appliances, MDR, IVDR, automotive, aviation, etc.). Distinguish:

- **AI system is itself a regulated product** (¶30): independently placed on market, has own intended purpose, directly regulated. Example: machinery-related software under Reg. (EU) 2023/1230.
- **AI system is a safety component of a regulated product** (¶31).

If neither applies → skip to Step 4.

#### 3b. Safety-component two-prong test (Art. 3(14); ¶¶32–49)

Apply BOTH alternative scenarios — either is sufficient:

**Scenario (i) — Safety function (intent-based, ¶¶35–37)**
The system constitutes a safety component if the provider's intended purpose is to prevent or mitigate risks to health, safety, or property. Use this checklist (from ¶37 box):

- **Preventive functions** (any one): monitoring/detection of harm-leading situations; maintenance/inspection detection; harm prevention; supervision of another safety system.
- **Mitigation functions** (any one): control or limitation of physical harm; mitigation of consequences (e.g., safe-stop); control of another safety system.
- **NOT safety functions**: performance optimisation, service efficiency, automation of user decisions, comfort/convenience, quality control of non-safety aspects.

See [references/safety-function-checklist.md](references/safety-function-checklist.md) for the full taxonomy and worked examples.

**Scenario (ii) — Failure or malfunctioning (consequences-based, ¶¶38–43)**
The system constitutes a safety component if its failure or malfunctioning could endanger health, safety, or property. Failure modes include: incorrect outputs (false positives/negatives), loss of function/availability, performance instability/drift, timing/latency errors, misclassification leading to hazardous control decisions. The likelihood must be more than theoretical (¶39).

Worked examples from ¶46:
- Lifts: AI for door closing / obstacle detection → safety component via failure (efficiency intent, but malfunction injures persons).
- Vehicles: lane-assist AI → safety component via failure.
- Agriculture: chemical-spray targeting AI → safety component via failure if persons nearby.
- Smart thermostat (¶48 footnote 5): NOT a safety component except where it controls child-lock or operates around vulnerable users.

Output of Step 3b: if (i) OR (ii) is satisfied → continue to Step 3c. Otherwise, this is not a safety component → skip to Step 4.

#### 3c. Third-party conformity assessment requirement (¶¶50–59)

Look up the conformity assessment procedure required by the relevant Annex I legal act:

- **Modules B, C1, C2, D, D1, E, E1, F, F1, G, H, H1 (Decision 768/2008/EC)** → involve a notified body → third-party conformity assessment required → **YES**.
- **Module A** (pure internal control) without harmonised-standards condition → not third-party → **NO**.
- **Module A conditioned on mandatory application of harmonised standards** (e.g., Toys Safety Regulation, Machinery Regulation, Radio Equipment Regulation) → still classified as high-risk; the option to use Module A is procedural flexibility, not a discretion to escape high-risk classification (¶57; Toys Safety Reg. Recital 15).

If module is A without mandatory-harmonised-standards condition → not high-risk under Art. 6(1).

#### 3d. Section A vs Section B distinction (Annex I; Art. 2(2))

If 3a + 3b + 3c all YES → **high-risk under Art. 6(1)**. Record:
- Annex I citation (specific legal act).
- Whether the legal act is in Annex I **Section A** (NLF-based) — full Chapter III requirements apply.
- Or **Section B** (other Union harmonisation legislation, e.g., aviation, automotive) — only Art. 6(1), 102–109, 112 apply per Art. 2(2).

See [references/annex-i-section-a-vs-b.md](references/annex-i-section-a-vs-b.md) for the full mapping.

### Step 4 — Art. 6(2) / Annex III branch

#### 4a. Map to the eight Annex III areas

Cross-check the system's intended purpose against each of the eight areas. Use the corresponding per-area reference file:

| # | Area | Reference |
|---|------|-----------|
| 1 | Biometrics | [annex-iii-area-1-biometrics.md](references/annex-iii-area-1-biometrics.md) |
| 2 | Critical infrastructure | [annex-iii-area-2-critical-infrastructure.md](references/annex-iii-area-2-critical-infrastructure.md) |
| 3 | Education and vocational training | [annex-iii-area-3-education.md](references/annex-iii-area-3-education.md) |
| 4 | Employment, workers management, access to self-employment | [annex-iii-area-4-employment.md](references/annex-iii-area-4-employment.md) |
| 5 | Access to and enjoyment of essential private and public services and benefits | [annex-iii-area-5-essential-services.md](references/annex-iii-area-5-essential-services.md) |
| 6 | Law enforcement | [annex-iii-area-6-law-enforcement.md](references/annex-iii-area-6-law-enforcement.md) |
| 7 | Migration, asylum, border control management | [annex-iii-area-7-migration.md](references/annex-iii-area-7-migration.md) |
| 8 | Administration of justice and democratic processes | [annex-iii-area-8-justice-democracy.md](references/annex-iii-area-8-justice-democracy.md) |

For each area where there is a use-case match, capture the specific Annex III sub-point (e.g., Nr. 4(a) for recruitment).

#### 4b. Apply the Art. 6(3) exception filter

If a use case matches in Step 4a, check whether the AI system performs **only** one of the following narrow categories (Art. 6(3)):

- **(a) Narrow procedural task** — strictly procedural, no influence on outcome.
- **(b) Improvement of a previously completed human activity** — refining what a human already decided.
- **(c) Detection of decision-making patterns or deviations** — without replacing or influencing previously completed human assessment.
- **(d) Preparatory task to an assessment** relevant to the Annex III use case.

See [references/art-6-3-exception-decision-tree.md](references/art-6-3-exception-decision-tree.md).

#### 4c. Apply the profiling re-exception (Art. 6(3) last sentence)

If the system performs **profiling of natural persons** (Art. 4(4) GDPR — automated processing of personal data to evaluate personal aspects), the Art. 6(3) exception is **excluded** and the system **is** high-risk.

#### 4d. Documentation duty if exception applies (Art. 6(4))

If the exception applies → not high-risk, BUT the provider must:
- Document the reasoning before placing on the market / putting into service (Art. 6(4)).
- Register the system in the EU database per Art. 49(2).

### Step 5 — Art. 25 substantial-modification trap

If the user is not the original provider but is modifying, fine-tuning, or rebranding an existing AI system, flag Art. 25(1):

- (a) Putting their own name/trademark on an existing high-risk system.
- (b) Substantial modification to an existing high-risk system.
- (c) Modifying the intended purpose of a non-high-risk system (including GPAI) such that it becomes high-risk under Art. 6.

If any apply → the user becomes a **provider** of a high-risk system with full Chapter III obligations. Follow up with a role-determination step (provider / deployer / importer / distributor under Art. 3 and Art. 25). The Commission is preparing separate Art. 25 guidelines; this skill flags only.

See [references/art-25-substantial-modification-flag.md](references/art-25-substantial-modification-flag.md).

---

## Output artefacts

Produce all three artefacts unless the user explicitly requests a subset.

### Artefact 1 — Structured decision block (terminal)

```
═══════════════════════════════════════════
EU AI Act — High-Risk Classification Result
═══════════════════════════════════════════
High-risk verdict:        [YES — Art. 6(1) Annex I | YES — Art. 6(2) Annex III Nr. X | NO]
Basis:                    [Safety function / Failure-based / Annex III use-case match]
Annex I citation:         [Legal act + Section A/B] (if applicable)
Annex III citation:       [Nr. X.<sub>] (if applicable)
Art. 6(3) exception:      [N/A | Applied — limb (a/b/c/d) | Excluded by profiling re-exception]
Art. 25 trap:             [Not triggered | Watch — modifying existing system]
Effective date:           [2 December 2027 (Annex III) | 2 August 2028 (Annex I)]
Documentation duty:       [Art. 6(4) (if Art. 6(3) applied) | Chapter III + Art. 11 technical docs]
═══════════════════════════════════════════
```

### Artefact 2 — Practitioner memo (1–2 page narrative)

Markdown memo addressed to a DPO / AI compliance officer. Sections:
1. **System under assessment** — name, provider/deployer, intended purpose (the cleaned Step 2 statement).
2. **Verdict and reasoning** — which branch (6(1) or 6(2)), which sub-test triggered it, which paragraph of the Commission guidelines is the anchor.
3. **Citations** — explicit paragraph numbers from the Commission guidelines and the corresponding article numbers.
4. **Next steps** — flag the follow-on work the verdict triggers: role determination (provider / deployer / importer / distributor), mapping the applicable Chapter III obligations to that role, and producing a formal compliance report.
5. **Open questions** — anything that needs counsel input before finalisation.

### Artefact 3 — JSON interchange artefact

The cross-skill interchange JSON. Schema (matches the existing repo convention):

```json
{
  "skill": "ai-act-high-risk",
  "version": "1.0",
  "assessed_at": "2026-MM-DD",
  "system_name": "<provider-supplied name>",
  "intended_purpose": "<cleaned Step 2 statement>",
  "verdict": "high_risk" | "not_high_risk" | "exempt_art_6_3",
  "basis": {
    "article": "6(1)" | "6(2)" | null,
    "annex": "I" | "III" | null,
    "annex_item": "Nr. X" | "Nr. Y.<sub>" | null,
    "section_a_or_b": "A" | "B" | null
  },
  "art_6_3_exception": {
    "applied": true | false,
    "limb": "a" | "b" | "c" | "d" | null,
    "profiling_excluded": true | false
  },
  "art_25_trap_flag": true | false,
  "effective_date": "2027-12-02" | "2028-08-02",
  "citations": [
    {"source": "Commission Guidelines Annex III ¶123"},
    {"source": "Annex III Nr. 4(a) AI Act"}
  ],
  "next_steps": ["role-determination", "obligation-mapping", "compliance-report"]
}
```

---

## References

- [art-6-general-principles.md](references/art-6-general-principles.md) — Commission's general principles (¶1–14, ¶448–451).
- [art-6-1-annex-i-guidelines.md](references/art-6-1-annex-i-guidelines.md) — Commission's Annex I section (¶15–62).
- [art-6-2-annex-iii-guidelines.md](references/art-6-2-annex-iii-guidelines.md) — Commission's Annex III section (¶63–447).
- [safety-function-checklist.md](references/safety-function-checklist.md) — taxonomy of safety functions from ¶37 box.
- [annex-i-section-a-vs-b.md](references/annex-i-section-a-vs-b.md) — Section A (NLF) vs Section B (other) mapping.
- 8 × per-area Annex III files (see Step 4a table).
- [art-6-3-exception-decision-tree.md](references/art-6-3-exception-decision-tree.md) — exception filter with worked examples.
- [art-25-substantial-modification-flag.md](references/art-25-substantial-modification-flag.md) — quasi-provider trap.
- [ai-omnibus-timeline-postponements.md](references/ai-omnibus-timeline-postponements.md) — postponement citation chain.

## Follow-on activities

A high-risk depth assessment usually sits inside a larger workflow. Once this skill has produced the verdict, the natural next steps are:

- **Broad risk-tier triage** — if the system has not yet been screened across all five tiers (prohibited / high-risk / GPAI / limited / minimal), do that first.
- **Article Q&A** — for any AI Act article question, answer directly from the cited regulation text and Commission guidelines.
- **Role determination** — provider / deployer / importer / distributor, including the Art. 25 quasi-provider trap.
- **Obligation mapping** — once the high-risk verdict is in, map the Chapter III obligations by role and risk tier.
- **Formal compliance report** — assemble the classification rationale and obligation matrix into an audit-ready record.
- **Preliminary triage** — a 15–25 min rapid assessment is a lighter alternative when full Art. 6 depth is not yet warranted.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## Part of the EU AI Act suite

This skill works on its own, but it's designed to interlock with my other EU AI Act skills — install any individually, or use them together for an end-to-end workflow:

- **EU AI Act Quick Assessment** — 15–25 min preliminary triage
- **EU AI Act System Classifier** — risk-tier classification across all five tiers
- **EU AI Act Role Determination** — provider / deployer / importer / distributor (incl. Art. 25)
- **EU AI Act Obligations Mapper** — obligations by role and risk tier
- **EU AI Act Examination Report Generator** — audit-ready compliance report
- **EU AI Act Knowledge Base** — Q&A over the Act + Commission guidelines

Each is available as a separate skill — install only what you need.
