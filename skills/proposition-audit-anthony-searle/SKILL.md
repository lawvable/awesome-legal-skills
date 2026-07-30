---
name: "proposition-audit-anthony-searle"
description: "Post-hoc verification and trust audit of AI-generated factual and interpretive claims. Classifies claims by type and salience, routes them to domain-appropriate sources, scores trustworthiness on a tiered scale with an Interpolated verdict for plausible-but-unsupported detail, and assesses rhetorical fairness on interpretive claims. Designed for clinical-negligence and healthcare-law practice in England and Wales, with general applicability beyond."
metadata:
  author: "Anthony Searle"
  license: "apache-2.0"
  version: "2026-05-31"
---

# Proposition Audit — AI Output Trust Verification

## Profile

- **Jurisdiction:** England and Wales (the maintained domain-routing profile; other jurisdictions illustrated under Step 2).
- **Practice area:** Clinical negligence and healthcare law (the maintained example domain; the methodology generalises to any field where AI-drafted factual content needs structured verification).
- **Intended user:** A practitioner verifying AI-generated factual or interpretive content before professional reliance — publication, court use, formal external use, or internal reliance.

## Purpose

AI-generated research, statistics, citations, and factual claims require structured verification before professional use. This skill provides a systematic post-hoc audit — classifying each claim by type and salience, searching domain-appropriate sources, scoring trustworthiness transparently, and flagging what needs attention.

This complements rather than replaces rigour during generation. It is an independent verification layer applied to completed output.

## The Verification Process

### Step 1: Agree the Threshold

Before beginning verification, ask what minimum standard applies to this use case. Offer these defaults if the user has no preference:

- **Publication or formal external use** (skeleton arguments, blog posts, published advice, court documents, regulatory submissions, external correspondence on file): 90%+ (empirical), Accurate (legal), Fair (rhetorical). Remove or independently verify anything below threshold.
- **Internal working documents** (drafts circulated for review, internal research notes, working files): 70%+. Flag claims below threshold but they may be retained with caveats.
- **Exploratory research** (early-stage research to identify avenues for further investigation): 50%+. The purpose is to identify which claims merit further investigation, not to produce a final verified output.

### Step 2: Extract and Classify Claims

Extract each distinct factual or interpretive claim from the output. Break composite sentences into their constituent sub-claims — each gets verified independently, because a sentence can be half-right and half-wrong. Where a single sentence contains claims of different types (a citation plus an empirical figure, for example), split it; each sub-claim is classified and scored independently.

**Classify each claim by type:**

- **Empirical fact** — a verifiable statement about the world (a statistic, a date, a named event). Verify by source corroboration.
- **Citation or reference** — a claimed source, case, study, or authority. Verify by locating the primary source and confirming it says what is attributed to it.
- **Legal or regulatory proposition** — a statement about the law, regulation, or procedural rules. Verify by locating the primary legislative or judicial source and assessing whether the proposition accurately reflects it. Source-counting alone is insufficient here because legal accuracy depends on interpretive precision, not volume of agreement.
- **Interpretive or analytical claim** — a conclusion drawn from evidence ("this suggests X", "the trend indicates Y"). These cannot be verified by corroboration. Instead, assess whether the underlying evidence exists, whether the reasoning is sound, whether credible counter-interpretations exist, and whether the opposing position is presented fairly (see rhetorical fairness in Step 4). Flag rather than score.

**Then assign each claim a salience level:**

- **Load-bearing** — the surrounding argument turns on this claim. The argument fails or substantially weakens if the claim is wrong.
- **Supporting** — strengthens the argument but is not strictly necessary to it.
- **Illustrative** — used by way of example, colour, or background. The argument is unaffected by removal.

Salience determines proportionate remediation in Step 5. Load-bearing claims warrant Tier-1 corroboration; illustrative claims warrant a quick pass. Apply uniform scrutiny only if every claim is genuinely load-bearing, which is rare.

### Step 3: Search for Sources

Search for independent corroboration using sources appropriate to the claim type. Do not verify from training data alone — every claim needs an active web search, because the whole point of this skill is to check what the model "knows" against external reality.

**Source tiers:**

- **Tier 1 (Definitive):**
  - *Clinical:* Cochrane reviews, NICE guidelines, SIGN guidelines, royal college guidance (RCOG, RCS, RCP, RCPCH), peer-reviewed journals in the relevant specialty.
  - *Legal:* Primary legislation (legislation.gov.uk), reported judicial decisions (caselaw.nationalarchives.gov.uk, BAILII), Civil Procedure Rules and Practice Directions, the relevant procedural rules of the forum.
  - *Statistical:* Office for National Statistics, official government data, primary research datasets.
  - *General empirical:* Peer-reviewed journals, regulatory bodies' official outputs.
- **Tier 2 (Authoritative):** Established news organisations (original reporting, not syndicated), university research centres, recognised professional and industry bodies, Law Commission reports, Hansard, MDU/MPS guidance.
- **Tier 3 (Supporting):** Reputable industry reports, recognised expert commentary, specialist trade publications, established practitioner blogs.

**Domain-specific search routing:**

Generic web search performs poorly for technical claims — it surfaces secondary reporting rather than primary sources. Route accordingly:

- *Clinical or medical claims* → PubMed, Cochrane Library, NICE, SIGN, and relevant specialty guidelines before general web search.
- *Legal claims (England and Wales)* → legislation.gov.uk, caselaw.nationalarchives.gov.uk, BAILII, and the relevant procedural rules before general web search.
- *Legal claims (other jurisdictions, illustrative)* → CourtListener and Westlaw for US, EUR-Lex for EU, the relevant primary-source service for other jurisdictions. The UK routing above is the maintained profile; others are illustrative and should be confirmed against the jurisdiction's actual primary-source register.
- *Statistical claims* → locate the primary dataset or study, not secondary reporting of it.
- *Quantum or arithmetic claims (multiplier × multiplicand, periodical-payments calculations, life-expectancy adjustments, schedule-of-loss workings)* → recompute deterministically against the inputs the source provided. Do not search; arithmetic is verifiable by recomputation, and web search performs poorly on numeric reasoning.

### Step 4: Score Each Claim

Score empirical facts and citations on a 0–100% scale. Weight source quality above quantity — one definitive source is worth more than several weak ones, because a Cochrane review settling a clinical question is more reliable than three news articles paraphrasing each other. Two special verdicts (Unverifiable, Interpolated) sit outside the numerical scale and take precedence in their respective failure modes.

| Score | Label | Meaning |
|-------|-------|---------|
| 90–100 | **Verified** | Confirmed by at least one Tier 1 source, or two Tier 2 sources with no contradictions. |
| 70–89 | **Likely accurate** | Supported by Tier 2 sources, or one Tier 1 source with minor caveats (figures close but not exact). |
| 50–69 | **Partially supported** | Some corroboration exists but with qualifications, outdated sources, or imprecise alignment with the claim as stated. |
| 30–49 | **Weakly supported** | Only Tier 3 corroboration, or a single non-definitive source. |
| 10–29 | **Poorly supported** | Sources found but none credible or relevant. |
| 0–9 | **Contradicted** | Credible sources directly contradict the claim. |
| — | **Unverifiable** | Search tools unable to surface adequate sources to assess this claim. Not a score — a transparency flag. Does not imply the claim is false. |
| — | **Interpolated** | Special verdict (typical underlying score 30–59). The cited source exists and partially supports the claim, but plausible details have been added that the source does not contain. Distinct from "Partially supported" because the issue is invented detail, not imprecision. The most dangerous AI failure in legal writing because it produces fluent, source-shaped sentences that the cited authority does not actually support. Use this label in preference to "Partially supported" or "Weakly supported" whenever the failure mode is interpolation, and note the interpolated content explicitly in the caveat. |

**Important distinctions:**

- "Not found" is not "contradicted." If web search cannot surface adequate sources, mark the claim **Unverifiable** rather than scoring it low. The distinction matters because a low score implies evidence was found and was weak, while Unverifiable means the audit itself has a gap. The user can then decide whether to seek verification through other means.
- For citation claims, score whether the source exists and says what is attributed to it. Partial accuracy (correct case name, wrong paragraph reference) sits at 50–69 with the discrepancy noted; invented sub-claims attached to a real citation sit at Interpolated.
- Where a claim is close to accurate but imprecise (a rounded statistic, a slightly misstated date), note the discrepancy rather than simply passing or failing it.

**Legal and regulatory propositions** receive a qualitative assessment instead of a numerical score:

- **Accurate** — Reflects the primary source precisely.
- **Broadly accurate** — Reflects the substance but with minor imprecision a careful reader would notice.
- **Incomplete or misleading** — Omits material qualification or context that changes the proposition's effect.
- **Inaccurate** — Misstates the primary source.

State the primary source consulted and any interpretive nuance. Numerical scoring is inappropriate here because legal accuracy is about interpretive precision, not corroboration volume.

**Interpretive or analytical claims** are not scored. Flag four dimensions:

- *Evidence base* — does the underlying evidence the claim relies on exist?
- *Logical soundness* — does the inference from evidence to conclusion hold?
- *Counter-interpretations* — do material counter-arguments or counter-interpretations exist that the claim does not engage with?
- *Rhetorical fairness* — how is the opposing position presented? Use one of:
  - **Fair** — the opposing position is represented as its strongest version.
  - **Slanted** — selection bias in presentation; only weaker parts of the opposing view are surfaced.
  - **Strawman** — a weakened or distorted version of the opposing view is attacked.
  - **Uncharitable** — the opposing view is presented in a form its proponents would not recognise.

For case-comment, analytical writing, and skeleton arguments, rhetorical fairness is often the substantive failure mode — the AI may be factually accurate but argumentatively unfair to the losing side. The fairness assessment matters at least as much as the factual scoring for this category.

### Step 5: Produce the Audit Report

Present the report as structured inline text by default. Produce an HTML artifact only if explicitly requested or if the output contains more than 15 individually verified claims.

Include:

1. **Summary** — total claims verified, breakdown by type and salience, overall confidence assessment as a narrative (not a single averaged number — averages obscure the difference between "mostly solid with one bad load-bearing claim" and "uniformly mediocre across illustrative claims").
2. **Claim-by-claim results** — each claim quoted verbatim from the original output, its classification (type + salience), score or qualitative assessment, sources consulted (with URLs where available), and any caveats.
3. **Source disagreements** — where authoritative sources consulted disagreed on the same point (NICE vs RCOG on a clinical question; majority and dissenting reasoning in a leading case; ONS vs research-paper figures on the same metric), present the disagreement explicitly rather than averaging the sources. Guideline and authority conflict is often the substantive point in a clinical-negligence dispute and should be surfaced as a finding.
4. **Action items** — claims below the applicable threshold, calibrated to salience:
   - *Load-bearing claims below threshold* — remediate before reliance; the argument cannot proceed on an unverified load-bearing claim.
   - *Supporting claims below threshold* — remediate where practicable; may be retained with explicit caveats if remediation is disproportionate.
   - *Illustrative claims below threshold* — remove without rebuilding the argument; an illustrative claim that cannot be verified is not worth the audit risk.

## Limitations and assumptions

This skill produces a structured audit; it does not produce certainty. Specific limitations:

- **Paywalled sources.** Where the primary source is behind a paywall (Westlaw, LexisNexis, certain medical journals), the skill flags the citation and consults the abstract where available, but the body is not retrieved. The verdict is reported with a "paywalled — abstract only" caveat. Obtain full-text verification through institutional access before relying on a paywalled-only assessment of a load-bearing claim.
- **Web search dependence.** This skill is useless without active web search. If the host platform's web-search tool is unavailable or rate-limited, the skill cannot perform the verification step and must report each empirical and citation claim as Unverifiable with the cause. Do not run this skill without confirming web search is available.
- **What this skill does NOT do.** Three things complementary skills do better and should be reached for where the failure mode dominates:
  - *Internal consistency checks across multiple LLM critics and a cross-family disagreement signal at generation time:* see [Verity (Johnny Ryan / ICCL Enforce)](https://github.com/johnnyryan/Verity), designed to run during generation as an MCP the primary model calls.
  - *Citation-fidelity scoring of attached citations* — does the cited source support the proposition attributed to it, even when the source is provided? See [mhalle's claim-audit](https://github.com/mhalle/claim-audit), designed for post-hoc audit of citation provenance.
  - *Reasoning-trace verification of step-by-step inferences:* outside the scope of any structured-audit skill. Requires manual review.
- **Complementary use.** Where the failure mode dominates, reach for the complementary skills above directly. The three are good together: in-generation hallucination minimisation (Verity), post-hoc citation-fidelity scoring (mhalle's claim-audit), and post-hoc claim-type-classified verification with domain-routed search and rhetorical-fairness assessment (this skill).

## Principles

1. Every empirical and citation claim is treated as unverified pending an active search against a domain-appropriate source. The model's prior knowledge is not the audit source — only retrievable, current material is.
2. Source quality outweighs source quantity. One definitive source is sufficient for a high score.
3. Use the **Unverifiable** flag — not a low score — when search cannot surface adequate sources. A low score implies evidence was found and was weak; Unverifiable means the audit itself has a gap, and the user can then decide whether to seek verification through other means.
4. Legal propositions require interpretive assessment against primary sources, not source-counting.
5. Salience determines proportionate remediation. Spend audit budget where the argument turns, not uniformly across every claim.
6. The audit informs the practitioner; it does not adjudicate. The verdict columns describe how strongly the evidence supports each proposition. The professional decision sits with the user.
7. Do not silently pass over claims that are difficult to verify. If verification is impractical for a particular claim, say so explicitly and explain why.

## Example

Source text:

> "In *Smith v Jones* [2024] EWHC 999 (KB), the High Court held that the standard of care for a junior doctor is the same as that for a consultant, following *Bolam v Friern Hospital Management Committee* [1957] 1 WLR 582."

Audit at publication threshold:

- **Sub-claim 1.** *"Smith v Jones [2024] EWHC 999 (KB)"* — citation; load-bearing; **Contradicted** (0–9). caselaw.nationalarchives.gov.uk and BAILII return no judgment under this neutral citation. The case is fabricated.
- **Sub-claim 2.** *"The standard of care for a junior doctor is the same as that for a consultant"* — legal proposition; load-bearing; **Inaccurate**. The settled position is that a junior doctor is held to the standard appropriate to the post they occupy, not to the standard of a consultant. The authority is the Court of Appeal in *Wilsher v Essex AHA* [1987] QB 730 (per Mustill LJ), not *Bolam*.
- **Sub-claim 3.** *"following Bolam v Friern Hospital Management Committee [1957] 1 WLR 582"* — citation; load-bearing; **Inaccurate**. *Bolam* exists and is the general professional-negligence test (the responsible-body-of-medical-opinion test) but does not address the junior-doctor calibration. The proposition is properly attributed to *Wilsher*.

Action items: at publication threshold every sub-claim fails. Rewrite the paragraph — substitute *Wilsher v Essex AHA* [1987] QB 730 as the authority for the junior-doctor standard, remove the fabricated *Smith v Jones* citation, and recast the proposition to reflect the actual test (standard of the post occupied) rather than the consultant-equivalence framing.
