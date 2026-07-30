# Art. 6(3) exception — decision tree

## When this applies

Art. 6(3) provides an exception: an AI system that **would otherwise** be high-risk under Annex III is **not** high-risk if it falls into one of four narrow categories AND does not perform profiling of natural persons.

The Art. 6(3) exception applies ONLY to Annex III (Art. 6(2)) — NOT to Annex I (Art. 6(1)).

## The four limbs

### (a) Narrow procedural task

The system performs only a narrow procedural task. Strict reading: no influence on outcome.

Worked example (anti-pattern):
- AI that triages incoming emails by topic but does not score, rank, or make decisions → likely (a).
- AI that ranks candidates by fit score → NOT (a) — it influences the hiring decision.

### (b) Improvement of a previously completed human activity

The system improves the result of a human activity already completed.

Worked example:
- AI that polishes recruiter-drafted feedback text → likely (b).
- AI that drafts the initial feedback for a recruiter to edit → NOT (b) — the human activity has not yet been completed.

### (c) Detection of decision-making patterns or deviations

The system detects patterns or deviations from prior decision-making patterns without replacing or influencing prior human assessment.

Worked example:
- AI that flags consistency anomalies in past hiring decisions for HR audit → likely (c).
- AI that scores new candidates against patterns of past hires → NOT (c) — it influences new assessments.

### (d) Preparatory task to an assessment

The system performs preparatory work to an Annex III-relevant assessment but does not itself perform the assessment.

Worked example:
- AI that summarises CVs for recruiter review → likely (d).
- AI that produces a shortlist of best-fit candidates → NOT (d) — that is the assessment, not preparatory.

## The profiling re-exception (Art. 6(3) last sentence)

**Even if one of (a)–(d) applies, the exception is excluded if the system performs profiling of natural persons.**

Profiling defined per Art. 4(4) GDPR: any form of automated processing of personal data to evaluate certain personal aspects (work performance, economic situation, health, preferences, interests, reliability, behaviour, location, movements).

If profiling is involved → exception unavailable → system remains high-risk.

## Documentation duty if exception applies (Art. 6(4))

If you conclude the exception applies:
1. **Document the reasoning** before placing on the market or putting into service.
2. **Register in the EU database** per Art. 49(2).

## Sources

- Art. 6(3) AI Act (verbatim text in the verbatim text of Regulation (EU) 2024/1689 (Annex I / Annex III / Art. 6 / Art. 111 / Art. 113)).
- Art. 6(4) AI Act (documentation duty).
- Art. 49(2) AI Act (EU database registration).
- Art. 4(4) GDPR (profiling definition).
