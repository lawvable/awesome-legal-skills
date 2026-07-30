# Art. 6 General Principles — Practitioner Digest

**Source:** Commission Draft Guidelines on the classification of high-risk AI systems under Article 6 AI Act (2026 draft for stakeholder consultation). Full text: the Commission Draft Guidelines on Art. 6 classification (2026), general principles.

## The two Art. 6 scenarios

- **Art. 6(1) + Annex I**: AI system is a product, or safety component of a product, under Union harmonisation legislation, AND the product requires third-party conformity assessment. (¶7)
- **Art. 6(2) + Annex III**: AI system falls into one of the eight high-risk use-case areas. (¶7)

These are not mutually exclusive. A single system can be high-risk under both branches, in which case the Art. 6(1) integration with sectoral conformity assessment (Art. 8(2), Art. 102–109) governs.

## Prerequisite gate — Art. 3(1) AI system definition

Before any high-risk classification, the system must qualify as an AI system per Art. 3(1) (¶8). If it does not — e.g., a pure rule-based system with no autonomy, no inference, no adaptiveness — the AI Act does not apply at all.

Reference: Commission Guidelines on the definition of an artificial intelligence system, C(2025) 5053 (a separate document from these high-risk guidelines).

## Intended purpose is decisive (¶¶10–13)

The provider's stated intended purpose drives classification under both scenarios. Per Art. 3(12), it is captured in:

- Instructions for use
- Technical documentation
- Promotional or sales materials
- Statements (including ToS, usage policy)

### The GPAI / multi-purpose trap (¶12)

If the provider presents the system as broadly applicable across many contexts and **does not consistently exclude high-risk uses**, the intended purpose is **deemed** to encompass high-risk uses and the system qualifies as high-risk.

In particular:
- Merely asserting in ToS that high-risk use is excluded is **insufficient** if other materials (promotional, examples, product positioning) suggest such uses are feasible and reasonably foreseeable.
- Limitations of use must be clearly, concretely, and coherently described **across all materials**.

This is the canonical trap for general-purpose AI systems deployed for downstream tasks.

### Reasonably foreseeable misuse (Art. 3(13))

By definition outside intended purpose. Captured for risk management context (Art. 9 risk management; Recital 65) but does **not** drive Art. 6 classification.

## Provider self-assessment and oversight (¶13)

Classification is the provider's responsibility, supervised by competent market surveillance authorities. The AI Act service desk and competent authorities may be consulted in case of doubt.

## Art. 25(1) traps — non-providers who become providers (¶14)

Distributors, importers, deployers, or other third parties become subject to **provider** obligations under Art. 25(1) if they:

- **(a)** Put their own name or trademark on an existing high-risk AI system already placed on the market or put into service.
- **(b)** Make a substantial modification to a high-risk AI system that has already been placed on the market or put into service in such a way that it remains a high-risk AI system.
- **(c)** Modify the intended purpose of an AI system (including a general-purpose AI system) that has not been classified as high-risk, such that it **becomes** a high-risk AI system under Art. 6.

See [art-25-substantial-modification-flag.md](art-25-substantial-modification-flag.md) for the flagging workflow and worked examples.

## Status and authority

These guidelines:

- Were issued under Art. 6(5) AI Act (¶3).
- Are **non-binding** (¶6); authoritative interpretation rests with the CJEU.
- Are draft for stakeholder consultation (cover page disclaimer).
- Will be presented on the AI Act Single Information Platform per area.
- Will be reviewed and updated annually per Art. 112(1) AI Act (¶451).
- Are scoped only to Art. 6 classification, not Chapter III compliance (¶4) — those guidelines are forthcoming.

## Where to look next

- For the full safety-component analysis under Art. 6(1): [art-6-1-annex-i-guidelines.md](art-6-1-annex-i-guidelines.md).
- For the Annex III area-by-area examples: [art-6-2-annex-iii-guidelines.md](art-6-2-annex-iii-guidelines.md) + the 8 per-area files.
- For the Art. 6(3) exception filter: [art-6-3-exception-decision-tree.md](art-6-3-exception-decision-tree.md).
- For the Omnibus timeline postponements: [ai-omnibus-timeline-postponements.md](ai-omnibus-timeline-postponements.md).
