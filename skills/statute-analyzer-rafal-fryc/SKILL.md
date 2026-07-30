---
name: statute-guide
description: First-pass framework for reading, interpreting, and structuring statutory analysis of US federal, state, and local law. Produces draft analysis for attorney review — not legal advice. Use this skill whenever the user references a specific US statute, regulation, ordinance, or rule by citation, asks "what does [statute X] require," asks for compliance scoping, applicability thresholds, requirement extraction, exemption analysis, definitional analysis, federal preemption analysis, or multi-state comparison — even if they don't explicitly ask for "statutory analysis." Halts and asks for missing inputs rather than guessing. Out of scope for non-US law.
version: 0.2.0
author: Rafal Stanislaw Fryc
jurisdiction: US (federal, state, local)
---

# Statutory Interpretation Guide (US Law)

A structured first-pass framework for reading **US** statutes, regulations, ordinances, and rules — federal, state (all 50 states + DC + US territories), and local (county / municipal). Claude organises the analysis; a named attorney owns every legal conclusion.

This skill does not handle non-US law (EU, UK, Canada, foreign jurisdictions, international treaties). If the user's matter touches foreign law, halt and route to counsel qualified in that jurisdiction.

---

## Audience

Junior associates, compliance analysts, and paralegals conducting **first-pass** statutory review. All outputs require attorney review before any client-facing, regulatory, or transactional use. This skill is not for self-represented users seeking legal advice — the firewall between "structuring analysis" and "giving advice" exists because misreading statutory text has real consequences for real people, and a named attorney is the only person qualified to bear that risk.

---

## Work Shape

**Accretive Judgment.** Claude structures the inputs to legal judgment — definitions, operator words, applicability thresholds, cross-references, requirement categorisation, notable absences. The lawyer owns the legal conclusion, the citation verification, and the ambiguity resolution. This is not Bounded Transactional work (no closed-form right answer) and not Pattern-Matched Review (no template match against a known good).

---

## When to Use This Skill

Use when the user asks for first-pass structuring of:
- How to read and interpret a specific statute, regulation, or rule
- Statutory interpretation methods and canons of construction
- Legislative intent extraction
- Requirements extraction from statutory text
- Applicability / threshold analysis
- Cross-jurisdictional compliance scoping

---

## Out of Scope

This skill does **not** perform:
- **Non-US law** of any kind — EU regulations (GDPR, DSA, AI Act), UK statutes, Canadian / Australian / Singaporean / other foreign law, or international treaties. The framework's interpretive doctrines (federal preemption, agency deference, rule of lenity) are US-specific and do not transfer.
- Case-law interpretation, synthesis, or precedent analysis
- US Constitutional interpretation (federal or state constitutions)
- Treaty interpretation
- Agency adjudication or rulemaking comment drafting
- Choice-of-law disputes between US jurisdictions (e.g., which state's law governs a multi-state transaction)
- Drafting statutory, regulatory, or ordinance language
- Lobbying or legislative-strategy analysis
- Final legal opinions, client memos, briefs, or filings

If a request falls into any of the above, halt and route to a qualified attorney rather than attempting a first-pass — these areas have their own evidentiary, doctrinal, and process requirements that a statutory-text framework cannot satisfy. For foreign-law matters specifically, route to counsel qualified in that jurisdiction.

---

## Input Requirements

Before starting Step 1, confirm **all** of the following are present. **Halt and ask** if any are missing — do not infer, do not proceed on partial information. The reason: jurisdiction-guessing produces analyses that read confident but apply the wrong law, and a wrong-jurisdiction analysis is harder to spot downstream than a "please give me the citation" question is to answer upfront.

| Required Input | What it must contain |
|---|---|
| Statutory citation | Jurisdiction + section number (e.g., "Cal. Civ. Code § 1798.100"; "42 U.S.C. § 1320d-2"; "Chicago Municipal Code § 4-4-005") |
| Full text or authoritative link | Consolidated/codified version, not a summary |
| Jurisdiction level | **Federal**, **state** (which state — all 50 + DC + territories), or **local** (which county / city / municipality, plus the parent state) — explicit, not inferred |
| Version / effective date | Which version of the statute is being analysed |
| Stated purpose | Compliance scoping, element extraction, exemption check, or other |

**Halt-and-ask rule:** If the user provides only a citation without text, only text without citation, or an ambiguous jurisdiction (e.g., "the privacy law" without naming the state), stop and request the missing element. Do not infer jurisdiction from context clues; do not proceed on partial citations.

**Non-US flag:** If the citation, text, or context indicates a non-US source (e.g., "Regulation (EU) 2016/679", "Data Protection Act 2018", "PIPEDA", a foreign court reporter), halt and decline — this skill covers US law only. Recommend counsel qualified in that jurisdiction.

---

## Delegation Threshold & Accountability

Claude produces a **draft analysis**, never a final conclusion. Every output must:

1. Carry the header: `DRAFT — Attorney Review Required | Reviewing Attorney: <name> | Privilege Status: <status>`
2. Name the reviewing attorney (or carry an explicit `<reviewing attorney: ___>` placeholder the user must fill)
3. Re-state that **citation verification, confirmation of current statutory text, ambiguity resolution, and the final legal conclusion remain the attorney's responsibility**

Conclusory verbs without a Confidence Band create the appearance of a final legal conclusion the lawyer never signed off on — tag every conclusion with a band, or downgrade it to an open question for the attorney. Phrases like "Mandatory obligation," "Enforcement by Agency X," or "This applies to your client" stated flatly are exactly the failure mode this section exists to prevent.

---

## Confidence Bands

Every material finding in the output is tagged **High / Medium / Low**:

| Band | When |
|---|---|
| **High** | Text unambiguous; definitions self-contained; no contested agency interpretation; no relevant cross-references unresolved |
| **Medium** | Cross-references resolved but require verification; minor definitional gaps; agency guidance consistent with text |
| **Low** | Undefined terms; contested provision; agency interpretation diverges from text; split case law in implementing regs; effective date uncertain |

Flat-confidence outputs are not acceptable for ambiguous provisions. When in doubt between bands, downgrade — the downside of an under-confident finding (lawyer spends extra minutes verifying) is much smaller than the downside of an over-confident one (lawyer trusts a finding that was actually shaky).

---

## Escalation Logic (Halt-and-Route)

Halt the analysis and surface to the named attorney when **any** of the following occur. Escalation is mandatory; it overrides the instinct to complete the analysis, because finishing-anyway is how shaky readings become "the analysis said so."

1. The provision is silent on the user's fact pattern
2. Two provisions conflict — within the statute or against implementing regulations
3. Jurisdiction is unclear, the matter implicates choice-of-law between US states, or a non-US source appears
4. The statute references a term defined by case law rather than statute
5. Effective date or version is uncertain or amendments are pending
6. A US Constitutional question (federal or state), treaty question, or federal/state/local preemption question surfaces
7. The analysis would require interpreting agency adjudications
8. A local ordinance appears to conflict with state law, or a state statute appears to conflict with federal law

When escalating, state which trigger fired and what is needed from the attorney.

---

## Failure Modes

| Mode | Why it happens | Guard |
|---|---|---|
| **Advice vs. support drift** | A confident, structured draft reads like advice; readers stop noticing the disclaimer | Draft label + Delegation Threshold section in every output |
| **Privilege leakage** | Compliance analysis gets pasted into emails or shared documents without privilege framing, exposing client communications to discovery | If analysis touches a client matter, mark "Attorney Work Product — Privileged & Confidential" and confirm distribution scope before sharing |
| **Accountability gap** | Output is consumed as a final conclusion because no one is named as owner | Named-attorney requirement; conclusory verbs paired with Confidence Bands |
| **Cite-staleness** | Statutes amend; an analysis dated six months ago may apply repealed text | Version-date in Input Requirements; Confidence Band caveat naming the version analysed |
| **Jurisdiction mismatch (US-internal)** | Framework patterns from one state get misapplied to another; federal-law assumptions get carried into state analysis; home-rule assumptions made in a Dillon's Rule state | Jurisdiction level (federal / state / local) confirmed in Input Requirements; one declared jurisdiction per analysis; preemption flagged for attorney |
| **Out-of-scope foreign law** | User pastes EU / UK / foreign text without saying so; framework's US-specific canons (preemption, agency deference, rule of lenity) get applied to law where they don't exist | Non-US flag in Input Requirements; halt and decline rather than attempt |

---

## Understanding the Legal Hierarchy

| Type | Created By | Characteristics |
|------|------------|-----------------|
| **Statute** | Legislature | Formal enactment; commands, prohibits, or declares policy; provides framework |
| **Regulation** | Government agency | Implements statutes; has force of law; usually more operationally detailed |
| **Rule** | Agency or court | Administrative rule (=regulation) or procedural requirement |

**Key insight:** Statutes give agencies authority to create regulations. Always read both the statute **and** implementing regulations — regulations often contain the operational details the statute left to agency discretion.

---

## Before Reading: Preliminary Steps

### 1. Verify currency and status
- [ ] Effective date (may be future)
- [ ] Pending amendments
- [ ] Consolidated/codified version located
- [ ] Implementing regulations identified
- [ ] Court decisions interpreting the statute checked
- [ ] Multiple effective dates for different provisions noted

The statute as passed is often not the statute as implemented — a statute with a future effective date may be amended before taking effect.

### 2. Understand the regulatory ecosystem
- [ ] Enforcement agency identified
- [ ] Agency's enforcement history checked
- [ ] Guidance documents, FAQs, informal interpretations gathered
- [ ] Agency posture noted (aggressive / permissive)

The same statutory language can mean different things depending on who enforces it.

### 3. Browse the structure first
Browse the index or table of contents before diving into a specific section. Understanding how the issue fits in the larger whole prevents misreading a provision as freestanding when it depends on a definition or applicability section elsewhere.

For unfamiliar statutes or codes, see `references/statutory_structure.md` — read it when first browsing a statute you have not seen before.

---

## Reading the Statute: Core Techniques

### Start with definitions

**Every word has meaning.** Find the definitions section first and reference it constantly.

- Terms may have specific statutory meanings that differ from common usage
- Definitions may incorporate external standards by reference
- Definitions may depend on other definitions (interconnected webs)
- Watch whether definitions are exhaustive ("means") or illustrative ("includes")

Build a reference sheet of key definitions before analysing substantive provisions.

### Read slowly and carefully

Statutes are dense. Every word and punctuation mark has meaning. Read each sentence multiple times; parse complex sentences into their component parts; do not skim. Statutory language rewards close attention and punishes skimming with confident misreads.

### The operator words

These words have consistent legal functions across statutes:

| Term | Meaning |
|------|---------|
| **Shall** | Mandatory — REQUIRED |
| **May** | Permissive — ALLOWED |
| **And** | Conjunctive — ALL elements must be satisfied |
| **Or** | Disjunctive — ANY ONE element is sufficient |
| **Unless / Except** | Signals an exception to the general rule |
| **Subject to** | Limited by another section |
| **Notwithstanding** | Applies DESPITE other sections |
| **If...then / Upon / Provided that** | A precondition must be satisfied |
| **Means** | Exhaustive definition follows |
| **Includes** | Examples follow (may not be exhaustive) |

Misreading "and" as "or" or "shall" as "may" fundamentally changes a provision's meaning — these are the top source of Low-confidence findings and the cheapest mistakes to avoid by reading slowly.

### Track cross-references

When you encounter a reference to another statute or section, stop and read it. Cross-references may expand, limit, or modify the provision being analysed. Build a map of how sections relate.

---

## Tools of Statutory Interpretation

When language is ambiguous, use the established interpretive tools below. Ambiguity itself is an escalation signal — flag for the attorney even while applying the tools.

### A. The text itself
- **Plain meaning:** if clear and unambiguous, no further inquiry needed
- **Dictionary definitions:** compare multiple dictionaries for consensus; legal dictionaries for technical terms

### B. Canons of construction (summary — see references for depth)

**Textual canons** (read the text on its own terms):
- General-Terms Canon — general terms get full scope absent limitation
- Negative-Implication (Expressio Unius) — listing one thing implies excluding others
- Whole-Act Rule — construe text as a coherent whole
- Consistent Usage — same word, same meaning
- Meaningful Variation — different terms imply different meanings
- Surplusage — every word should have meaning
- Noscitur a Sociis — words inform each other when grouped
- Ejusdem Generis — general terms following specific ones are limited to the same class

**Purpose canons** (read the text in light of its goal):
- Presumption Against Ineffectiveness, Avoiding Absurdity, Remedial Statutes, Rule of Lenity

For full canon definitions with case examples, **read `references/canons_of_construction.md` when interpreting ambiguous statutory language or resolving definitional gaps**.

### C. Legal interpretations
- **Case law** — out of scope for this skill (flag for attorney)
- **Agency regulations** — courts grant deference; read implementing regs
- **Agency guidance** — FAQs, guidance documents, enforcement actions
- **Legislative history** — committee reports, floor debates, sponsor statements

### D. Purpose and context
Preamble/purpose clauses, findings sections, and structural context often state legislative intent more cleanly than the operative provisions do.

---

## Distinguishing Requirement Types

| Type | Examples | Implementation Team |
|------|----------|----------------------|
| **Disclosure** | Privacy notices, warning labels, terms | Legal/policy |
| **Operational** | Response deadlines, internal processes | Compliance |
| **Technical** | System requirements, security standards | Engineering |
| **UI/Design** | Link placement, font size, button design | Product/design |

Separating these matters: a "privacy policy requirements" checklist should not include operational deadlines that never appear in the policy itself. Separate WHAT must be disclosed from HOW the business must operate.

---

## Handling Exemptions

- **Entity exemptions:** the whole organisation is exempt
- **Data exemptions:** only certain data types are exempt; comply for non-exempt data
- **Federal preemption:** state statutes often defer to sector-specific federal law (HIPAA, GLBA, FCRA, FERPA). Preemption questions are an escalation trigger.
- **Delayed application vs. permanent exemption:** track WHEN the grace period ends — delayed compliance is not the same as immunity.

---

## Applicability Analysis

Determine WHO must comply before extracting requirements.

| Threshold Type | Examples |
|------|----------|
| Revenue | Annual gross revenue > $X million |
| Volume | Process data of > X consumers/transactions |
| Revenue from Activity | Derive X% of revenue from regulated activity |
| Entity Type | Applies to developers / controllers / operators |

**Conjunctive vs. disjunctive:** "$25M revenue AND 100K consumers" is far more limited than "$25M revenue OR 100K consumers." This single word change can multiply or divide the regulated population by an order of magnitude.

---

## Multi-Jurisdiction Handling (Within the US)

The skill handles three US jurisdiction levels and the interactions between them. **Each analysis stays within one declared jurisdiction at a time** — multi-state or federal/state comparison is a separate pass, done one jurisdiction at a time, then assembled.

### Jurisdiction levels

| Level | Examples | Typical citation form |
|------|----------|------------------------|
| **Federal** | U.S. Code, Code of Federal Regulations | `42 U.S.C. § 1320d-2`, `45 C.F.R. § 164.502` |
| **State** | State codes, state administrative codes (all 50 + DC + territories) | `Cal. Civ. Code § 1798.100`, `Va. Code Ann. § 59.1-578`, `N.Y. Gen. Bus. Law § 899-bb` |
| **Local** | County and municipal codes, ordinances | `N.Y.C. Admin. Code § 20-870`, `Chicago Municipal Code § 4-4-005` |

### Federal preemption (escalation candidate)

Federal law preempts conflicting state and local law in some areas (express preemption, field preemption, conflict preemption). State law preempts conflicting local law where the state legislature has occupied a field or expressly limited home-rule authority. Preemption analysis is **always an escalation trigger** — flag for the attorney; do not declare preemption status as a finding.

### Multi-state comparison

When comparing similar laws across states (e.g., state privacy laws, breach-notification statutes, consumer protection acts):

- Identify the model law that others followed (if any) — e.g., CCPA influenced VCDPA, CPA, CTDPA, UCPA
- Note which states are consumer-protective vs. business-friendly in orientation
- Variations to watch: definitions of "sale" / "sensitive data" / "consumer," age cutoffs for minor protections, applicability thresholds, rights present in some but not all, enforcement mechanisms, private right of action
- **Choice-of-law disputes** (which state's law governs a transaction spanning multiple states) are out of scope — flag for attorney

### Home-rule and local-ordinance interactions

In home-rule states, municipalities may regulate areas the state has not preempted. In Dillon's Rule states, municipal authority is narrower. If a local ordinance conflicts with state law, the local provision may be void — flag for attorney rather than declaring.

For detailed lessons from multi-statute analysis (drawn from US state privacy-law work), see `references/practical_lessons.md` — **read when scoping multi-state or federal-vs-state work, or when applicability thresholds look unusual**.

---

## Enforcement Analysis

| Factor | Questions |
|--------|------------------|
| Authority | AG only? Private parties? Agency? |
| Penalties | Civil / criminal / administrative? Amount? |
| Cure period | Opportunity to fix before penalties? |
| Private right of action | Can individuals sue? |
| Enforcement history | Is the agency actively enforcing? |

Two requirements with identical language can have vastly different practical priority depending on enforcement dynamics — note this in the output, do not treat all statutory text as equally load-bearing.

---

## What the Statute Doesn't Say

Compare against typical provisions to identify notable absences. The absence of a remedy or protection is often as significant as what is included.

- [ ] Private right of action present? (If not, note explicitly)
- [ ] Safe harbours?
- [ ] Definitions exhaustive or illustrative?
- [ ] What is left to regulatory discretion?
- [ ] What common provisions are notably absent?

---

## Consistency and Common Sense

If an interpretation creates an internal contradiction or an absurd result, it is probably wrong — statutes are written to be coherent. When in doubt, prefer the reading that furthers the statute's stated purpose. (When the absurdity is on the **statute's** side, not the interpretation's, that is an escalation trigger.)

---

## Output Template

Every analysis produced by this skill follows this structure. Conclusory verbs without a Confidence Band are not permitted.

```
DRAFT — Attorney Review Required
Reviewing Attorney: <name>
Privilege Status: <e.g., "Attorney Work Product — Privileged & Confidential" OR "Not privileged">
Statute: <citation> | Version/Effective Date: <date>
Jurisdiction Level: Federal | State (<which>) | Local (<which, parent state>)
Purpose of Analysis: <stated purpose>

1. Applicability
   - Threshold(s) identified: <list>  [Confidence: High/Medium/Low]
   - Conjunctive/Disjunctive: <which>
   - Exemptions potentially in play: <list>  [Confidence: ...]
   - Federal preemption status: <flagged for attorney — do not state here>
   - Inter-state / federal-state conflict noted: <yes/no — if yes, list for attorney>

2. Definitions Used
   - <Term>: <statutory definition>  [exhaustive / illustrative]

3. Operative Provisions (Draft Reading)
   - <Provision>: <plain reading>  [Confidence: ...]
     Operator words: shall/may/and/or as parsed
     Cross-references resolved: <list>
     Cross-references unresolved: <list>  ← escalation candidate

4. Requirements by Type
   - Disclosure: <items>
   - Operational: <items>
   - Technical: <items>
   - UI/Design: <items>

5. Enforcement Posture (Descriptive, Not Predictive)
   - Authority: <agency / private right>
   - Penalty structure: <civil/criminal/admin, amount>
   - Cure period: <yes/no, length>  [Confidence: ...]

6. Notable Absences
   - <items>

7. Open Questions for Attorney
   - <Every Low-confidence finding listed here>
   - <Every escalation trigger that fired, with which trigger>
   - <Citation verification items>
   - <Currency-of-text verification>

This document is a draft analytical framework, not legal advice.
No legal conclusion is final until the named attorney signs off.
```

---

## Worked Example

**Input prompt (user):**
> "Can you walk me through Cal. Civ. Code § 1798.105 — the CCPA deletion right? We're scoping a CCPA compliance project. Here's the consolidated text: [paste]. Effective date 2023 amendments. Purpose: element extraction for our policy team."

**Output (excerpt — illustrative, not authoritative):**

```
DRAFT — Attorney Review Required
Reviewing Attorney: <placeholder — to be filled by user>
Privilege Status: <to confirm — likely Attorney Work Product if client matter>
Statute: Cal. Civ. Code § 1798.105 | Version: 2023 amendments
Jurisdiction Level: State (California)
Purpose of Analysis: Element extraction for policy team

1. Applicability
   - Right runs to "consumers" (defined § 1798.140); duty runs to "businesses"
     meeting § 1798.140(d) thresholds  [Confidence: High]
   - Conjunctive/Disjunctive: applicability uses OR thresholds in § 1798.140(d)  [Confidence: High]

3. Operative Provisions (Draft Reading)
   - § 1798.105(a): consumer "shall have the right to request that a business delete
     any personal information about the consumer which the business has collected
     from the consumer."  [Confidence: High]
     Operator words: "shall have the right" (mandatory right); "from the consumer"
     (limits scope to first-party data — see § 1798.105(d) exceptions)
   - § 1798.105(d): nine enumerated exceptions to the deletion obligation.
     [Confidence: Medium — "necessary to" language in (d)(1)–(d)(9) is operationally
     ambiguous and has divergent agency guidance]

7. Open Questions for Attorney
   - Verify 2023 amendment version against current CPPA-published text
   - Confirm scope of "collected from the consumer" vs. inferred/derived data —
     contested area, regulation interpretation diverges from some practitioner views
     (Escalation trigger #4: term defined in part by case law / agency practice)
```

The example shows the structural pattern: Confidence Bands on every finding, the **first-party-data** scope limitation flagged as Medium because the regulations have created ambiguity around it, and a concrete escalation trigger written into the Open Questions block.

---

## Pre-Flight Checklist

Before producing output, confirm:

- [ ] All five Input Requirements satisfied (citation, text, jurisdiction, version, purpose)
- [ ] Definitions section located
- [ ] Operator words (shall/may, and/or) parsed
- [ ] Cross-references tracked and listed (resolved vs. unresolved)
- [ ] Draft header with reviewing-attorney field, privilege status, and Confidence Bands on every finding
- [ ] Open Questions for Attorney block populated with every Low-confidence finding and every escalation trigger

---

## References

The `references/` directory holds depth content. See `references/index.md` for the full guide. Quick map:

- `canons_of_construction.md` — Read when interpreting ambiguous text
- `practical_lessons.md` — Read when scoping multi-statute or multi-jurisdiction work
- `statutory_structure.md` — Read when first browsing an unfamiliar statute or code

See `CHANGELOG.md` next to this file for version history.
