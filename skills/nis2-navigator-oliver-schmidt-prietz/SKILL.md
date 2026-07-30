---
name: nis2-navigator
description: |
  NIS2 Compliance Navigator — scope classification, Art. 21 gap analysis (0-4 maturity scoring), and compliance roadmap under EU Directive 2022/2555 with deep German BSIG-neu coverage and profiles for Italy, France, Netherlands, Austria, Spain. Use when: (1) User mentions "NIS2", "NIS-2", "BSIG", "BSIG-neu", "NIS2UmsuCG", "Cyberbeveiligingswet", "Loi Résilience", "NISG", "decreto legislativo 138", (2) User asks if their organization falls under NIS2 or needs a cybersecurity compliance assessment, (3) User mentions essential/important entities, Annex I/II, BSI registration, § 30 BSIG, incident reporting, management body liability, supply chain security, (4) User wants a NIS2 gap analysis, readiness assessment, or compliance roadmap, (5) User asks about NIS2 fines, enforcement, or Nachweispflicht, (6) User asks about NIS2 in any EU Member State.
metadata:
  author: "Oliver Schmidt-Prietz"
  license: "agpl-3.0"
  version: "2026-06-05"
---

# NIS2 Compliance Navigator

Guide users through a full NIS2 compliance assessment: scope determination, Art. 21 gap analysis across 10 risk management measures, and prioritized compliance roadmap. Covers EU Directive 2022/2555 with deep German national transposition (BSIG-neu) and high-level profiles for Italy, France, Netherlands, Austria, and Spain.

## Session Initialization

### 1. Display Disclaimer (show at session start, do not block)

> **Important:** This skill provides structured NIS2 compliance guidance based on EU Directive 2022/2555 and national transposition laws. It is not legal advice. Final compliance decisions should involve your organisation's CISO / Information Security Officer and qualified legal counsel experienced in cybersecurity regulation.

### 2. Web Search on Activation

Search for current regulatory developments before starting — NIS2 transposition is still evolving in many Member States, and enforcement practice is developing rapidly:
```
NIS2 enforcement updates [current year]
NIS2 implementing regulation EU Commission [current year]
```

For the full catalog of official EU and BSI sources, load [references/regulatory-sources.md](references/regulatory-sources.md) when you need to cite specific guidance or direct the user to official resources.

### 3. Determine Jurisdiction Focus

> "Will this assessment focus on (a) EU-level NIS2 Directive obligations, (b) a specific Member State's national law, or (c) both?"

- **EU-level only** → Use Directive references (Art. 21, Art. 23, Annexes I/II)
- **Germany** → Load [references/germany-nis2umsucg.md](references/germany-nis2umsucg.md). Use § references (§ 28, § 30, § 32 BSIG-neu) and BSI-specific obligations
- **Italy, France, Netherlands, Austria, or Spain** → Load [references/eu-jurisdiction-profiles.md](references/eu-jurisdiction-profiles.md). These profiles highlight key national differences — a full deep-dive with local counsel is still necessary. Verify transposition status via web search, since several laws are still in legislative process
- **Both (e.g., EU + Germany)** → Lead with Directive, layer national specifics where they diverge
- **Cross-border group** → Flag that multiple transpositions apply. Load relevant profiles and recommend local counsel per jurisdiction
- **Any other Member State** → The EU-level assessment is fully applicable. National specifics will need separate research

---

## Phase 1: Scope & Classification (~5 minutes)

Determine whether the organization falls under NIS2 and classify as essential or important. This is the most common first question any entity has, and getting the classification right is foundational — it determines enforcement intensity, fine levels, and reporting obligations.

For German entities, mention the BSI's free Betroffenheitsprüfung (betroffenheitspruefung-nis-2.bsi.de) as a complementary first step. Note it only covers scope — our assessment goes further into compliance maturity and roadmap.

Ask questions ONE AT A TIME in this order:

| # | Category | Question |
|---|----------|----------|
| 1 | **Sector** | "What sector(s) does your organization operate in?" Offer Annex I/II categories as reference. |
| 2 | **Services** | "What specific services do you provide within that sector?" (needed for precise Annex mapping) |
| 3 | **Size** | "How many employees does your organization have, and what is your annual turnover and balance sheet total?" |
| 4 | **Group structure** | "Is your organization part of a corporate group? If so, are the NIS2-relevant activities at group or entity level?" |
| 5 | **Special status** | "Do any of these apply: DNS provider, TLD registry, trust service provider, public electronic communications network, sole provider of a critical service in a Member State?" |

### Classification Logic

Load [references/sector-classification.md](references/sector-classification.md) for the full Annex I/II sector mapping and size thresholds.

**Decision tree:**

1. **Sector match** → Map to Annex I (high criticality) or Annex II (other critical)
2. **Size test** → Medium: ≥50 employees OR (turnover >€10M AND balance sheet >€10M). Large: ≥250 employees OR (turnover >€50M AND balance sheet >€43M)
3. **Essential entity** if: Annex I + large, OR qualified trust service provider, TLD registry, DNS provider, public comms provider, central public administration, or KRITIS operator (DE)
4. **Important entity** if: Annex I + medium, OR Annex II + medium/large
5. **Regardless-of-size**: Check special categories in reference file
6. **Out of scope** if: Below medium thresholds AND no special status
7. **DORA check**: Financial entities under DORA are excluded from NIS2 Art. 21 and Art. 23 — redirect to DORA compliance (DORA acts as lex specialis with its own equivalent requirements)
8. **CIR check**: Digital infrastructure/provider entities face additional binding requirements under CIR 2024/2690 beyond Art. 21 — flag early

**Group structure:** Apply the size test at the level where the NIS2-relevant service operates. Consolidated figures apply with operational integration. Independent entities within a group: assess separately.

### Classification Output

> **SCOPE DETERMINATION**
> - Sector: [Annex I/II sector and sub-sector]
> - Size classification: [Small / Medium / Large]
> - Entity category: **[Essential / Important / Out of Scope]**
> - Basis: [Directive Art. / national law reference]
> - Special flags: [DORA exclusion / CIR applies / Regardless-of-size / None]
>
> *If Germany:* BSI registration [required/not required], status [completed / overdue]

**Example:** A German managed IT services provider with 120 employees and €25M turnover in the ICT service management sector (Annex I) → Annex I, medium enterprise, **essential entity** (MSPs are essential regardless of size). BSI registration required (overdue since 6 March 2026). CIR 2024/2690 applies. This entity faces both proactive BSI supervision and the additional CIR technical requirements — communicate this clearly because it significantly increases the compliance scope compared to a typical important entity.

If **Out of Scope** → inform user, suggest voluntary adoption (supply chain pressure from in-scope customers is increasingly common), and end assessment. Otherwise proceed to Phase 2.

---

## Phase 2: Art. 21 Gap Analysis (~15 minutes)

Walk through the 10 risk management measures from Art. 21(2)(a)–(j) / § 30 BSIG-neu. The purpose is rapid maturity scoring — enough to identify critical gaps and prioritize, not a full audit. This keeps the assessment accessible for entities encountering NIS2 for the first time while still producing actionable output.

Load [references/art21-measures.md](references/art21-measures.md) for measure descriptions, scoring criteria, and ISO 27001 references.

### Assessment Approach

For each measure, ask ONE targeted question, then score on a 0–4 scale:

| Score | Level | Description |
|-------|-------|-------------|
| 0 | **Non-existent** | No awareness, no measures |
| 1 | **Ad hoc** | Informal, reactive, person-dependent |
| 2 | **Defined** | Documented but inconsistently applied |
| 3 | **Managed** | Consistently implemented, monitored, reviewed |
| 4 | **Optimized** | Continuously improved, measured, integrated into enterprise risk management |

### ISO 27001 References

For each measure, include a brief reference to relevant ISO 27001:2022 Annex A controls. Many organizations approaching NIS2 already have ISO 27001, so this mapping creates immediate practical value — "you already satisfy Art. 21(2)(a) through your A.5.1 and A.5.2 controls" is the kind of output that saves hours of consultant time.

### The 10 Measures

Walk through each measure sequentially. For each:
1. Briefly explain what NIS2 requires (1–2 sentences)
2. Ask the targeted assessment question
3. Score based on the user's response — explain your reasoning so the user understands and can challenge the score
4. Note key gaps if score ≤ 2

Detailed measures, questions, and scoring criteria are in [references/art21-measures.md](references/art21-measures.md).

### Gap Analysis Output

After scoring all 10 measures, present a summary table:

```markdown
## NIS2 Gap Analysis Summary

| # | Measure (Art. 21(2)) | Maturity (0-4) | Status |
|---|---------------------|----------------|--------|
| a | Risk analysis & IS policies | [score] | [🔴/🟡/🟢] |
| b | Incident handling | [score] | [🔴/🟡/🟢] |
| c | Business continuity & crisis mgmt | [score] | [🔴/🟡/🟢] |
| d | Supply chain security | [score] | [🔴/🟡/🟢] |
| e | Network & IS acquisition/dev/maint | [score] | [🔴/🟡/🟢] |
| f | Effectiveness assessment | [score] | [🔴/🟡/🟢] |
| g | Cyber hygiene & training | [score] | [🔴/🟡/🟢] |
| h | Cryptography & encryption | [score] | [🔴/🟡/🟢] |
| i | HR security & access control | [score] | [🔴/🟡/🟢] |
| j | MFA & secure communications | [score] | [🔴/🟡/🟢] |

**Overall Score: [X] / 40**
**Overall Rating: [🔴 Critical / 🟡 Needs Improvement / 🟢 On Track]**
```

Traffic light: 🔴 = 0–1, 🟡 = 2, 🟢 = 3–4. Overall: 🔴 ≤ 15, 🟡 16–29, 🟢 ≥ 30.

**Example:** A mid-sized logistics company (important entity) might score: (a) Risk analysis 2 🟡 — policy exists but last reviewed 18 months ago; (d) Supply chain 1 🔴 — ad hoc checks only, no contractual clauses; (j) MFA 3 🟢 — enforced for all remote and privileged access. Overall 19/40, 🟡 Needs Improvement. Top priorities: supply chain security and incident handling.

---

## Phase 3: Compliance Roadmap

Generate a prioritized remediation roadmap based on the gap analysis.

For German entities, align with the BSI's 6-phase #nis2know Roadmap and reference BSI-Standards 200-2/200-3 as implementation resources — this gives the roadmap additional authority when presented to German management.

### Prioritization Framework

Essential entities face proactive supervision, so their gaps are more urgent at every maturity level:

| | Maturity 0 | Maturity 1 | Maturity 2 |
|--|-----------|-----------|-----------|
| **Essential entity** | P1 — Immediate | P1 — Immediate | P2 — Short-term |
| **Important entity** | P1 — Immediate | P2 — Short-term | P3 — Medium-term |

Measures at maturity 3–4 → maintenance mode (not in roadmap).

- **P1 — Immediate** (0–3 months): Fundamental gaps, acute risk
- **P2 — Short-term** (3–6 months): Significant gaps, structured remediation
- **P3 — Medium-term** (6–12 months): Enhancement to full maturity

### Roadmap Output

For each gap: (1) Measure, (2) Current state, (3) Target state, (4) 2–3 key actions, (5) Effort (S/M/L/XL), (6) Priority with timeline.

### Germany-Specific Items

If jurisdiction includes Germany, load [references/germany-nis2umsucg.md](references/germany-nis2umsucg.md) and add: BSI registration status, § 38 management body obligations, Nachweispflicht deadline (Dec 2028), § 32 incident reporting readiness, KRITIS-Dachgesetz interaction if applicable.

### Management Briefing (Art. 20 / § 38 BSIG)

Include a management body section in every roadmap. NIS2 Art. 20 explicitly creates management body engagement requirements, and Germany's § 38(2) BSIG adds personal liability. This section is often the most persuasive part of the assessment — it transforms the abstract compliance obligation into something personal for the individuals in the room:

> **Management Body Obligations**
> - Approve risk management measures (Art. 20(1) / § 38(1) BSIG)
> - Undergo regular cybersecurity training (Art. 20(2) / § 38(3) BSIG) — not delegable
> - Oversee implementation — execution can be delegated to CISO, oversight cannot
> - *Germany:* Personal liability for damages from non-compliance (§ 38(2) BSIG)

---

## Output: Final Assessment Report

Combine all three phases using the template in [references/templates.md](references/templates.md).

**Report structure:**
1. Executive Summary (scope verdict, overall score, top 3 priorities)
2. Scope & Classification Detail
3. Gap Analysis Scoring Table
4. Prioritized Compliance Roadmap
5. Management Body Obligations
6. Jurisdiction-Specific Requirements (if applicable)
7. Recommended Next Steps

---

## Key Guardrails

The non-obvious pitfalls that trip up real assessments:

1. **Self-assessment obligation** — No official notification from authorities. Entities must determine their own status. Many don't realize they're in scope
2. **Supply chain cascading** — Out-of-scope organizations increasingly face contractual NIS2 requirements from in-scope customers
3. **Dual incident reporting** — NIS2 (24h/72h/1-month to national authority) and GDPR (72h to DPA) run in parallel for incidents involving personal data. Different timelines, recipients, and content
4. **Size threshold trap** — The OR/AND logic catches companies small by headcount but large by revenue
5. **DORA carve-out** — Financial entities under DORA are excluded from NIS2 measures and reporting. Redirect, don't assess
6. **CIR 2024/2690** — Digital infrastructure entities face additional binding requirements beyond Art. 21
7. **Commission amendments (Jan 2026)** — Proposed, not in force. Mention for strategic awareness only

## More EU regulation skills

This skill works standalone. Explore my other EU digital-regulation skills via the interactive skill page linked in the README, or at OneZero Legal (https://onezero.legal).
