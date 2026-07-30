# Art. 6(2) + Annex III — Index and Orchestration

**Source:** Commission Draft Guidelines on the classification of high-risk AI systems under Article 6 AI Act (2026 draft for stakeholder consultation), Section IV. Full text: the Commission Draft Guidelines on Art. 6 classification (2026), Annex III section.

This file is the **index** for Annex III analysis. The eight Annex III areas each have their own per-area reference file with use-case mapping, worked examples, and exception-filter notes. This file orchestrates them and consolidates horizontal issues.

## The eight Annex III areas

| # | Area (Annex III Nr.) | Per-area reference |
|---|----------------------|---------------------|
| 1 | Biometrics — Nr. 1 | [annex-iii-area-1-biometrics.md](annex-iii-area-1-biometrics.md) |
| 2 | Critical infrastructure — Nr. 2 | [annex-iii-area-2-critical-infrastructure.md](annex-iii-area-2-critical-infrastructure.md) |
| 3 | Education and vocational training — Nr. 3 | [annex-iii-area-3-education.md](annex-iii-area-3-education.md) |
| 4 | Employment, workers management — Nr. 4 | [annex-iii-area-4-employment.md](annex-iii-area-4-employment.md) |
| 5 | Essential private and public services — Nr. 5 | [annex-iii-area-5-essential-services.md](annex-iii-area-5-essential-services.md) |
| 6 | Law enforcement — Nr. 6 | [annex-iii-area-6-law-enforcement.md](annex-iii-area-6-law-enforcement.md) |
| 7 | Migration, asylum, border control — Nr. 7 | [annex-iii-area-7-migration.md](annex-iii-area-7-migration.md) |
| 8 | Justice and democratic processes — Nr. 8 | [annex-iii-area-8-justice-democracy.md](annex-iii-area-8-justice-democracy.md) |

## Workflow

1. **Map intended purpose to areas.** For each Annex III area, check the per-area reference and see whether the system's intended purpose matches a listed use case. Multiple matches are possible; capture each with the specific Annex III sub-point (e.g., Nr. 4(a) for recruitment).
2. **Apply the Art. 6(3) exception filter.** If a match exists, run the four-limb filter — see [art-6-3-exception-decision-tree.md](art-6-3-exception-decision-tree.md).
3. **Apply the profiling re-exception.** If profiling of natural persons is involved, the Art. 6(3) exception is unavailable — the system remains high-risk.
4. **Document the reasoning.** If the exception applies, document under Art. 6(4) and register under Art. 49(2).

## Horizontal issues that apply across all eight areas

### Human involvement (Section 2.1)

The fact that a human is "in the loop" does not, by itself, defeat high-risk classification. The high-risk classification turns on **intended purpose**, not on operational human oversight. Whether a human reviews the AI's output is relevant for Chapter III oversight obligations (Art. 14), not for Art. 6 classification.

### Limitations to natural persons (Section 2.2)

Several Annex III use cases are scoped to AI systems that act upon, or evaluate, **natural persons**. AI systems acting only on legal persons, abstract events, or non-personal data may fall outside those specific use cases.

### Complex systems and services (Section 2.3)

An AI system embedded in a larger product or service is assessed on its own intended purpose. The wrapper product's purpose does not automatically bind the AI system, nor vice versa.

### "Intended to be used" (Section 2.4)

Annex III wording "AI systems intended to be used to..." mirrors Art. 3(12) — the provider's intended purpose is decisive. The GPAI / multi-purpose trap (general principles ¶12) applies: broad applicability without consistent exclusion of high-risk uses → deemed to encompass high-risk uses.

### "On behalf of" (Section 2.5)

Where Annex III uses "on behalf of" (e.g., law enforcement on behalf of public authority), the legal relationship determines applicability — not the contractor's commercial framing.

### "In so far as use is permitted under Union or national law" (Section 2.6)

This phrasing in Annex III items does **not** make high-risk classification conditional on lawfulness. It clarifies that lawfulness under other Union/national law is a separate question. An unlawful system is not exempted from high-risk classification merely because its use is illegal — the AI Act still applies to its placing on the market.

### The Art. 6(3) filter (Section 2.7)

The four-limb filter (narrow procedural task, improvement of completed human activity, detection of patterns/deviations, preparatory task) **excludes** the system from high-risk if it falls entirely within one of those limbs.

The **profiling re-exception** (Art. 6(3) last sentence) **overrides** the filter: if the system performs profiling of natural persons (Art. 4(4) GDPR), the filter is unavailable and the system remains high-risk.

The provider's burden:
- Self-assess whether the filter applies.
- Document reasoning under Art. 6(4).
- Register under Art. 49(2).
- Protection against circumvention (Section 2.7.4) — the filter cannot be invoked artificially (e.g., by carving the system into narrow components to avoid integrated high-risk classification).

See [art-6-3-exception-decision-tree.md](art-6-3-exception-decision-tree.md) for the full filter logic with worked examples.

## Sources

- Commission Guidelines Annex III (full text): the Commission Draft Guidelines on Art. 6 classification (2026), Annex III section
- Annex III AI Act (verbatim regulation text): the verbatim text of Regulation (EU) 2024/1689 (Annex I / Annex III / Art. 6 / Art. 111 / Art. 113)
- Art. 6(2), Art. 6(3), Art. 6(4), Art. 4(4) GDPR (profiling definition)
- Art. 49(2) AI Act (EU database registration)
