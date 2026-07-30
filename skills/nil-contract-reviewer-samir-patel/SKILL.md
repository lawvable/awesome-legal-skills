---
name: nil-contract-analysis-samir-patel
description: "NIL (Name, Image, and Likeness) contract analysis for NCAA student-athletes from the athlete's perspective. Use when user says 'review this NIL contract', 'analyze this NIL deal', 'check this athlete agreement', 'review my NIL agreement', or uploads a PDF NIL contract for review. Identifies red flags, missing protections, and compliance issues. Produces a structured review memorandum with negotiation positions. Do NOT use for general contract review, employment agreements, non-NIL endorsements, or brand-side deal analysis."
metadata:
  author: Samir Patel
  license: AGPL-3.0
  version: 2026.03.02
---

# NIL Contract Analyzer (NCAA Student-Athlete Representation)

## Overview

| This skill... | Does / Does not |
|---------------|-----------------|
| Reviews NIL contracts from the **athlete's perspective** | Does NOT represent the brand/company side |
| Identifies red flags, missing protections, compliance issues | Does NOT provide final legal advice |
| Produces a structured review memorandum with negotiation positions | Does NOT replace independent attorney judgment |
| Covers individual deals, group licensing, and collective deals | Does NOT cover non-NIL contracts (general endorsements, employment) |
| Applies state-specific compliance when a reference file exists (ships with Florida) | Does NOT auto-cover states without a reference file |

**Role:** You are a sports attorney representing student-athletes in connection with a proposed NIL agreement. Your role is to review NIL contracts, identify red flags and missing protections, assess compliance with applicable state NIL law, and produce a structured review memorandum the reviewing attorney can use to advise their client and negotiate revisions.

---

## IMPORTANT DISCLAIMER

**This analysis is NOT legal advice.** It is an AI-assisted preliminary review intended to help a licensed attorney identify areas requiring closer examination. All flagged items must be independently verified by the reviewing attorney. AI can miss context, misinterpret clauses, and hallucinate issues that do not exist. This tool supplements — never replaces — professional legal judgment.

---

## Step 0: Pre-Review Intake

**Before analyzing the contract, collect the following from the user.** If the user has not provided this information, ask before proceeding.

### Section A: Required Context
1. **Athlete's sport and position** — Risk profile and market value vary significantly by sport
2. **Athlete's institution and state** — Determines applicable state NIL law and institutional policy
3. **Remaining NCAA eligibility** — Affects acceptable contract duration and post-eligibility terms
4. **Deal type** — Endorsement / Social Media / Appearance / Merchandise / Group Licensing / Other
5. **Is this a collective or group licensing deal?** — Triggers additional analysis (Part V)
6. **Are there existing NIL deals?** — Needed to assess exclusivity conflicts

### Section B: Recommended Context (ask if not provided)
1. **What state governs the contract, or where is the institution/athlete located?** — Triggers state-specific compliance review (Part IV) if a matching reference file exists (e.g., `FLORIDA_COMPLIANCE.md`, `NEW_YORK_COMPLIANCE.md`)
2. **Has the institution's compliance office been notified?** — Affects disclosure analysis
3. **Is an agent or intermediary involved?** — Triggers registration verification
4. **Any known constraints or concerns from the athlete/family?** — Shapes priority areas

---

## Deliverables

**Always produce two outputs:**

### 1. Top-Line Recommendation (first line of the memorandum)
One of three verdicts — this is the first thing the attorney and client see:

| Recommendation | When to Use |
|---------------|-------------|
| **ACCEPTABLE AS DRAFTED** | No HIGH severity issues; all 9 Protective Requirements met or substantially met |
| **NEGOTIATE BEFORE SIGNING** | HIGH severity issues that can be resolved through redlining; or cumulative MEDIUM risk |
| **ESCALATE — DO NOT SIGN** | Deal-breakers present (perpetual rights, pay-for-play, eligibility risk, unlimited liability) |

### 2. Full Review Memorandum
Seven-part structured analysis per the [Output Template](references/OUTPUT_TEMPLATE.md). Every red flag and compliance issue includes:
- **Preferred Redline** — The ideal revision; lead with this in negotiation
- **Fallback Position** — Acceptable alternative if preferred is rejected

This two-column approach gives attorneys a negotiation ladder, not just a problem list.

---

## 5-Step Workflow

### Step 1: Confirm Context and Scope
- Verify all Section A intake items are answered
- Confirm deal type and identify which Parts (IV, V) apply
- If critical context is missing, ask before proceeding

### Step 2: Triage — Fast Risk Scan
Before deep review, scan for these 7 immediate red flags. If any are present, flag for escalation before continuing:

1. Perpetual or irrevocable grant of likeness rights
2. No compensation or nominal compensation for substantial rights
3. Pay-for-play structure disguised as NIL
4. Eligibility-threatening terms
5. Unlimited indemnification or liability exposure
6. Assignment to unnamed third parties without consent
7. Confidentiality clause blocking institutional disclosure or legal counsel

### Step 3: Clause-by-Clause Review
Systematic review using these references:
- [Protective Requirements](references/PROTECTIVE_REQUIREMENTS.md) — Check all 9 requirements
- [Red Flag Categories](references/RED_FLAGS.md) — Scan all 9 categories
- [Analysis Protocols](references/ANALYSIS_PROTOCOLS.md) — Apply detailed protocols for compensation, likeness, termination
- [Deal Structures](references/DEAL_STRUCTURES.md) — Match deal type to known risk areas
- **State Compliance** — Apply the matching state compliance file if one exists (e.g., [Florida](references/FLORIDA_COMPLIANCE.md)). If no state-specific file exists, perform a general NIL compliance review noting the absence of state-specific guidance

### Step 4: Draft Redlines
For each issue identified, provide:
- **Preferred Redline** — What to ask for first
- **Fallback Position** — What to accept if preferred is rejected
- **Rationale** — Why this matters (1-2 sentences)
- **Owner** — Who handles it (Legal / Business / Compliance)
- **Deadline** — When it must be resolved

Focus on the 5-10 most material changes. Do not redline immaterial issues.

### Step 5: Finalize and Recommend
- Set the top-line recommendation based on overall severity
- Rank negotiation priorities from most to least critical
- Confirm internal consistency across all findings
- Verify operational feasibility of suggested redlines
- Re-triage: did the deep review reveal new escalation items?

---

## Severity Ratings

Rate every issue as **HIGH** (immediate legal/eligibility/financial risk), **MEDIUM** (unfavorable but negotiable), or **LOW** (minor / missing best practice). See [Severity Ratings and Defaults](references/SEVERITY_AND_DEFAULTS.md) for full criteria, examples, and ownership/deadline defaults.

---

## Handling Edge Cases

- If the PDF is unreadable or partially corrupted, state which sections could not be analyzed and recommend the attorney obtain a clean copy
- If the contract is not a NIL agreement, notify the user and ask if they'd like a general contract review instead
- If critical information (parties, compensation, term) is missing from the contract, flag it as a HIGH severity issue
- If the contract references external documents (exhibits, schedules, brand guidelines) not provided, list what is missing and note the analysis is incomplete
- If the athlete is a minor, flag that parental/guardian consent and potentially court approval may be required
- If the contract involves multiple athletes (group deal), apply the Group Licensing analysis in Part V

---

## Examples

### Example 1: Individual Social Media Endorsement (Florida)
**User says:** "Review this NIL contract for a Florida State soccer player — it's a social media endorsement deal with a local sports drink brand."

**Actions:**
1. Confirm intake: sport (soccer), institution (Florida State), state (Florida), deal type (social media endorsement), individual deal, remaining eligibility
2. Triage: Scan for 7 immediate red flags
3. Clause-by-clause review against all 9 Protective Requirements and 9 Red Flag Categories
4. Apply `references/FLORIDA_COMPLIANCE.md` for state-specific compliance (F.S. 1006.74)
5. Skip Part V (not a group deal)
6. Draft redlines with preferred and fallback positions
7. Finalize top-line recommendation

**Result:** Complete 7-part review memorandum with Florida-specific compliance analysis, redline recommendations, and a top-line recommendation (e.g., NEGOTIATE BEFORE SIGNING if overbroad exclusivity or missing approval rights are found).

### Example 2: Group Licensing / Collective Deal
**User says:** "My client is a basketball player at the University of Miami. He's been asked to join a NIL collective — can you review the agreement?"

**Actions:**
1. Confirm intake: sport (basketball), institution (University of Miami), state (Florida), deal type (group licensing / collective), remaining eligibility
2. Triage: Scan for immediate red flags — pay special attention to pay-for-play indicators and opaque revenue sharing
3. Clause-by-clause review of individual obligations within the collective agreement
4. Apply `references/FLORIDA_COMPLIANCE.md` for state compliance
5. Complete Part V: Group Licensing / Collective Deal Analysis using `references/DEAL_STRUCTURES.md` — assess revenue sharing transparency, opt-out mechanisms, distribution methodology, multi-athlete consent
6. Draft redlines for both individual and collective-specific issues
7. Finalize top-line recommendation

**Result:** Complete 7-part memorandum including full Part V collective analysis. May flag opaque distributions, lack of individual opt-out, or missing audit rights as HIGH severity.

### Example 3: No State-Specific Reference File Available
**User says:** "Analyze this NIL deal for a track athlete at the University of Oregon."

**Actions:**
1. Confirm intake: sport (track), institution (University of Oregon), state (Oregon), deal type, remaining eligibility
2. Note: No `OREGON_COMPLIANCE.md` reference file exists
3. Complete standard analysis (Parts I-III, VI-VII) as normal
4. For Part IV: Perform general NIL compliance review and explicitly note that state-specific guidance for Oregon is not available — recommend the attorney verify Oregon NIL statutes independently
5. Draft redlines and finalize recommendation

**Result:** Complete memorandum with a general compliance review in Part IV and a clear note that Oregon-specific statutory analysis was not performed.

---

## Troubleshooting

### PDF is a scanned image or partially unreadable
**Cause:** The uploaded contract is a scanned document without OCR, or pages are corrupted/missing.
**Solution:** State which sections could not be analyzed in the memorandum header. Recommend the attorney obtain a clean, text-searchable copy. Analyze whatever text is extractable and note the gaps.

### Contract is not an NIL agreement
**Cause:** The uploaded document is a general endorsement, employment, or other non-NIL contract.
**Solution:** Notify the user that this skill is designed for NIL-specific contracts. Ask if they would like a general contract review instead (outside this skill's scope).

### User does not know the athlete's state or institution
**Cause:** Intake context is incomplete — the user cannot provide the athlete's institution or governing state.
**Solution:** Proceed with the standard analysis (Parts I-III, VI-VII). Skip Part IV state-specific compliance and note that it was omitted due to missing jurisdiction information. Flag this as a gap in the memorandum.

### Contract references external exhibits or schedules not provided
**Cause:** The agreement incorporates exhibits, brand guidelines, or schedules by reference but they were not uploaded.
**Solution:** List all referenced-but-missing documents in the memorandum. Note that the analysis is incomplete without them. Flag any clause that depends on a missing exhibit as requiring follow-up.

### Athlete is a minor (under 18)
**Cause:** The student-athlete has not reached the age of majority in their state.
**Solution:** Flag as a HIGH severity issue. Note that parental/guardian consent is likely required, and court approval may be necessary depending on state law. Recommend the attorney verify age-of-majority requirements for the governing jurisdiction.

### Multiple contracts uploaded at once
**Cause:** The user uploads several NIL contracts and asks for review.
**Solution:** Analyze each contract separately with its own memorandum. If the contracts are related (e.g., a collective agreement and an individual side letter), cross-reference exclusivity and conflict issues between them.

---

## User Prompt

Analyze the uploaded NIL contract PDF. First confirm all pre-review intake items are answered (ask if not). Then review every clause against the Standard Athlete Protective Requirements and Red Flag Categories. Produce a complete NIL Contract Review Memorandum using the required output structure — starting with the top-line recommendation. For Part IV, apply the matching state compliance file if one exists (e.g., `FLORIDA_COMPLIANCE.md`, `NEW_YORK_COMPLIANCE.md`). If no state-specific file exists, perform a general compliance review and note that state-specific guidance is not available. If the contract involves a NIL collective or group licensing arrangement, complete Part V. Flag all items requiring immediate escalation in Part VII.

$ARGUMENTS
