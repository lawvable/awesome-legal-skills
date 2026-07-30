# Art. 6(4) Documentation Requirement — Non-High-Risk Annex III Systems

## Legal Basis

**Article 6(4) AI Act:**

> The provider who considers that an AI system referred to in Annex III is not high-risk shall document the assessment referred to in paragraph 3 before that AI system is placed on the market or put into service. Such provider shall be subject to the registration obligation referred to in Article 49(2). For the purpose of the assessment referred to in paragraph 3, the Commission shall, after consulting the Board, and no later than 2 February 2026, provide guidelines specifying the practical implementation of this Article.

*German: Dokumentationspflicht fuer die Bewertung nach Art. 6 Abs. 3*

**Recital:** 53

---

## Who Does This Apply To?

**Scope:** Providers (Anbieter) of AI systems that:
1. Fall under one of the 8 Annex III application areas, AND
2. Are classified as NOT high-risk because the Art. 6(3) exception applies

**This does NOT apply to:**
- Systems that do not trigger Annex III at all (they are simply minimal/limited risk)
- Systems classified as high-risk (they have full Chapter III obligations instead)
- Deployers — only providers bear this documentation obligation

---

## Required Documentation Content

The Art. 6(4) documentation must demonstrate that all Art. 6(3) requirements are satisfied. The following elements should be included:

### Element 1: System Identification

| Field | Content |
|---|---|
| System name and version | [Full name, version number] |
| Provider name and contact | [Legal entity, address, contact] |
| Intended purpose (Zweckbestimmung) | [Per Art. 3(12)] |
| Annex III category triggered | [Nr. X(y) — with full description] |
| Date of assessment | [Date] |

### Element 2: Art. 6(3) Condition Analysis

Document which of the four conditions (a)-(d) is fulfilled:

**Condition (a) — Narrow procedural task (enge Verfahrensaufgabe):**
- What is the task performed?
- Why is it narrow (limited, well-defined)?
- Why is it procedural (mechanical, no substantive judgment)?
- Could the task be performed by a simple automated process?

**Condition (b) — Improving previously completed human activity:**
- What human activity was already completed?
- How does the AI system improve (not change) the result?
- Does the human's decision stand without the AI's improvement?

**Condition (c) — Detecting decision-making patterns:**
- What decisions does the system analyze?
- Does it detect patterns or deviations only?
- Confirmation: system does NOT replace or influence the human assessment
- Is there proper human review of pattern analysis?

**Condition (d) — Preparatory task:**
- What assessment is the AI system preparing for?
- Does the actual decision remain with a human?
- Is the AI's output used as input, not as the decision itself?

### Element 3: Significant Risk of Harm Assessment

Even with a condition (a)-(d) met, the exception only applies if the system does not pose a significant risk of harm. Document:

| Assessment Question | Answer | Reasoning |
|---|---|---|
| Can the system's output affect health? | [Yes/No] | [explanation] |
| Can the system's output affect safety? | [Yes/No] | [explanation] |
| Can the system's output affect fundamental rights? | [Yes/No] | [explanation] |
| Does the system materially influence decision outcomes? | [Yes/No] | [explanation] |
| What is the severity of potential harm if errors occur? | [Low/Medium/High] | [explanation] |
| How many persons are potentially affected? | [estimate] | [explanation] |

**Overall harm assessment:** [No significant risk / Significant risk identified]

### Element 4: Profiling Exclusion Confirmation

**Critical check — Art. 6(3) last sentence:**

The exception does NOT apply if the system performs profiling of natural persons (as defined in Art. 4(4) GDPR).

| Profiling Indicator | Present? | Reasoning |
|---|---|---|
| Uses personal data of identified/identifiable persons | [Yes/No] | [explanation] |
| Evaluates personal aspects (performance, economic situation, health, preferences, reliability, behavior, location) | [Yes/No] | [explanation] |
| Analyzes or predicts individual-level characteristics | [Yes/No] | [explanation] |
| Assessment relates to specific individuals (not aggregate) | [Yes/No] | [explanation] |

**Profiling determination:** [No profiling / Profiling present — exception CANNOT apply]

### Element 5: Registration (Art. 49(2))

| Registration Aspect | Status |
|---|---|
| Registered in EU database (Art. 49(2)) | [Yes / Pending — date] |
| Registration reference number | [number or "to be assigned"] |
| Provider registration in EU database (Art. 49(1)) | [Yes — reference] |

---

## Documentation Template

```markdown
# Art. 6(4) Non-High-Risk Assessment Documentation

## 1. System Identification
- **System name:** [name]
- **Version:** [version]
- **Provider:** [legal entity]
- **Intended purpose:** [description per Art. 3(12)]
- **Annex III category triggered:** Nr. [X]([y]) — [description]
- **Assessment date:** [date]
- **Prepared by:** [name, role]

## 2. Art. 6(3) Condition Fulfilled
**Condition relied upon:** [a / b / c / d]

**Analysis:**
[Detailed explanation of why the selected condition is met, with
reference to the specific facts of the system's operation]

## 3. Significant Risk of Harm Assessment
**Conclusion:** [No significant risk of harm identified]

**Reasoning:**
[Explanation covering health, safety, and fundamental rights dimensions.
Address severity, likelihood, and scope of potential harm.]

## 4. Profiling Exclusion
**Conclusion:** [System does NOT perform profiling of natural persons]

**Reasoning:**
[Explanation of why the system's processing does not constitute
profiling under Art. 4(4) GDPR. Address each indicator.]

## 5. Registration
- **EU database registration:** [status and reference]
- **Provider registration:** [status and reference]

## 6. Conclusion
Based on this assessment, [system name] falls within Annex III Nr. [X]([y])
but qualifies for the Art. 6(3) exception under condition ([letter]).
The system is classified as NOT high-risk.

This documentation is made available to relevant national competent
authorities upon request per Art. 6(4).

---
Signed: [name, role]
Date: [date]
```

---

## Common Pitfalls

1. **Forgetting the profiling check:** Many providers analyze conditions (a)-(d) but overlook the profiling re-exception in the last sentence of Art. 6(3). If profiling is present, the entire exception fails regardless of which condition is met.

2. **Confusing "narrow procedural task" with "narrow use case":** Condition (a) requires the *task* to be narrow and procedural, not just the use case. An AI system used in a narrow context but performing substantive judgment does not qualify.

3. **Treating Art. 6(4) as optional:** This is a legal obligation, not a recommendation. Failure to document the assessment before placing on market constitutes non-compliance.

4. **Missing registration:** Art. 49(2) registration in the EU database is a separate, additional obligation that must be fulfilled alongside the documentation. The Art. 6(4) assessment alone is insufficient.

5. **Not reassessing after changes:** If the system's functionality, intended purpose, or deployment context changes, the Art. 6(3) assessment must be re-evaluated. A change may void the exception and reclassify the system as high-risk.

---

## Cross-References

- **Art. 6(3) exception analysis:** apply the four exception limbs (narrow procedural task; improve a previously completed human activity; detect deviation from prior decision patterns; preparatory task) together with the profiling re-exception in the Art. 6(3) final subparagraph.
- **Classification workflow:** the inputs here assume a completed risk-tier classification (AI-system test under Art. 3(1); prohibited / high-risk / GPAI / limited / minimal).
- **Report generation:** the Art. 6(4) content produced here can be folded into a formal compliance report.
- **Existing Art. 6(4) summary:** See [low-risk-obligations.md](low-risk-obligations.md) Section "Art. 6(4) Documentation Requirement"
