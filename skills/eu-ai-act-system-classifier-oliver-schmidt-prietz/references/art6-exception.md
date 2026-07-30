# Art. 6(3) Exception — High-Risk Classification Exception

## Legal Text

**Article 6(3) AI Act:**

> By derogation from paragraph 2, an AI system referred to in Annex III shall not be considered to be high-risk where it does not pose a significant risk of harm to the health, safety or fundamental rights of natural persons, including by not materially influencing the outcome of decision making.

> The first subparagraph shall apply where any of the following conditions is fulfilled:

> (a) the AI system is intended to perform a **narrow procedural task**;

> (b) the AI system is intended to **improve the result of a previously completed human activity**;

> (c) the AI system is intended to detect **decision-making patterns or deviations** from prior decision-making patterns and is not meant to replace or influence the previously completed human assessment, without proper human review;

> (d) the AI system is intended to perform a **preparatory task** to an assessment relevant for the purposes of the use cases listed in Annex III.

> **Notwithstanding the first subparagraph, an AI system referred to in Annex III shall always be considered to be high-risk where the AI system performs profiling of natural persons.**

*German: Art. 6 Abs. 3 — Ausnahme von der Hochrisikoeinstufung*

**Recital:** 53

---

## Four Exception Conditions (Art. 6(3)(a)-(d))

Only ONE condition needs to be met for the exception to apply. However, the system must also not pose a significant risk of harm.

### Condition (a): Narrow Procedural Task

**Definition:** The AI system performs a narrow procedural task — i.e., a limited, well-defined, mechanical operation that does not involve judgment on substantive matters.

**Assessment questions:**
1. Is the task narrow and well-defined?
2. Is it procedural (mechanical/administrative) rather than substantive?
3. Does the task NOT involve assessment of individual merits, characteristics, or circumstances?
4. Could the task reasonably be performed by a simple automated process?

**Examples where exception applies:**
- AI system that converts unstructured documents into structured format (e.g., extracting data fields from CVs into a database — without ranking or scoring candidates)
- AI system that categorizes incoming correspondence by topic for routing
- AI system that performs optical character recognition on application forms
- AI system that translates documents for processing

**Examples where exception does NOT apply:**
- AI system that ranks or scores CVs (goes beyond procedural)
- AI system that pre-selects candidates based on criteria (involves substantive assessment)
- AI system that triages applications by quality (involves judgment)

---

### Condition (b): Improving Previously Completed Human Activity

**Definition:** The AI system improves the result of a human activity that has already been completed — i.e., the human has already made the substantive decision, and the AI merely enhances quality, presentation, or format.

**Assessment questions:**
1. Has a human already completed the substantive activity/decision?
2. Does the AI system only enhance, polish, or improve the human's completed work?
3. Does the AI NOT change the substance or direction of the human's decision?
4. Would the human's decision stand even without the AI's improvement?

**Examples where exception applies:**
- Grammar/style checking of a human-written court decision
- Formatting a human-completed assessment report
- Spell-checking a human-drafted immigration decision
- Enhancing image quality of human-captured evidence photos

**Examples where exception does NOT apply:**
- AI suggesting changes to the substance of a decision
- AI rewriting key parts of a human assessment
- AI adding analytical content the human did not produce

---

### Condition (c): Detecting Decision-Making Patterns

**Definition:** The AI system detects patterns or deviations from prior human decision-making, without replacing or influencing the human assessment.

**Assessment questions:**
1. Does the AI system analyze existing human decisions to identify patterns?
2. Does it flag deviations from established patterns?
3. Does it explicitly NOT replace the human's assessment?
4. Does it explicitly NOT influence the human's current decision-making?
5. Is there proper human review of the AI's pattern analysis?

**Examples where exception applies:**
- AI system analyzing past judicial decisions to flag inconsistencies in sentencing (for human review, not automated correction)
- AI system detecting unusual patterns in benefit grant decisions (audit/quality assurance, not decision-making)
- Statistical tool showing decision-makers their own historical patterns for self-awareness

**Examples where exception does NOT apply:**
- AI system that adjusts scores based on detected patterns
- AI system that auto-corrects decisions to align with patterns
- AI system whose pattern analysis is used directly to make new decisions

---

### Condition (d): Preparatory Task

**Definition:** The AI system performs a preparatory task to an assessment relevant for the Annex III use cases — i.e., it prepares information or materials that a human will use for the actual assessment.

**Assessment questions:**
1. Is the AI system performing a task that is preparatory to the actual decision?
2. Does the actual assessment/decision remain with a human?
3. Is the AI's output used as input for human decision-making, not as the decision itself?
4. Does the AI NOT determine the outcome of the assessment?

**Examples where exception applies:**
- AI system that gathers and organizes relevant case law for a judge (who makes the decision)
- AI system that extracts key data points from applications for human review
- AI system that summarizes medical records for human diagnostic assessment
- AI system that creates a structured comparison of candidate qualifications (without scoring/ranking)

**Examples where exception does NOT apply:**
- AI system that produces a recommendation score the human typically follows
- AI system whose "preparation" effectively pre-determines the decision
- AI system that presents information in a way designed to steer the human toward a particular decision

---

## The Profiling Re-Exception (Art. 6(3) Last Sentence)

**CRITICAL:** Even if one of the four conditions (a)-(d) would apply, the exception is **overridden** if the AI system performs **profiling of natural persons**.

### Definition of Profiling — Art. 4(4) GDPR

> 'profiling' means any form of automated processing of personal data consisting of the use of personal data to evaluate certain personal aspects relating to a natural person, in particular to analyse or predict aspects concerning that natural person's performance at work, economic situation, health, personal preferences, interests, reliability, behaviour, location or movements.

### Profiling Assessment

**Does the system perform profiling?**

| Indicator | Description | Result |
|-----------|-------------|--------|
| Uses personal data | System processes data relating to identified/identifiable persons | [Yes/No] |
| Evaluates personal aspects | System assesses characteristics, traits, or qualities of individuals | [Yes/No] |
| Analyzes or predicts | System analyzes current state or predicts future behavior/characteristics | [Yes/No] |
| Individual-level assessment | Assessment relates to specific individuals, not aggregate statistics | [Yes/No] |

**If ANY indicator is "Yes"** → profiling is likely present → Art. 6(3) exception does NOT apply → system remains **high-risk**.

### Practical Implications

The profiling re-exception means that most AI systems in the employment, credit, and law enforcement contexts will remain high-risk even if they would otherwise qualify under conditions (a)-(d), because they typically involve:
- Evaluating individual candidate qualities (employment — Nr. 4)
- Assessing individual creditworthiness (services — Nr. 5a)
- Assessing individual risk levels (law enforcement — Nr. 6)

---

## Art. 6(3) Exception Analysis Workflow

```
Step 1: Does the AI system fall under Annex III?
├─ NO → Not high-risk (via Annex III)
└─ YES → Continue

Step 2: Does the system perform profiling of natural persons?
├─ YES → EXCEPTION DOES NOT APPLY → System is HIGH-RISK
└─ NO → Continue

Step 3: Does any condition (a)-(d) apply?
├─ (a) Narrow procedural task? → If YES, exception may apply
├─ (b) Improving completed human activity? → If YES, exception may apply
├─ (c) Detecting decision patterns (without replacing)? → If YES, exception may apply
└─ (d) Preparatory task to assessment? → If YES, exception may apply

Step 4: Does the system pose significant risk of harm?
├─ YES → Exception does NOT apply → System is HIGH-RISK
└─ NO → Exception APPLIES → System is NOT high-risk

Result: [High-Risk / Not High-Risk (Art. 6(3) exception)]
```

---

## Art. 6(4) Documentation Requirement

**Important:** Even when Art. 6(3) exception applies and the system is classified as NOT high-risk:

> The provider of the AI system shall document the assessment [of why Art. 6(3) applies] before that system is placed on the market or put into service, and shall provide that documentation to relevant national competent authorities upon request.

This documentation requirement applies to all Annex III systems classified as non-high-risk under Art. 6(3). The provider must:
1. Document the assessment showing which condition (a)-(d) is met
2. Explain why the system does not pose significant risk of harm
3. Confirm the system does not perform profiling
4. Keep documentation available for authority requests
5. Register the system in the EU database (Art. 49(2))
