# Implementation Checklists — Reference

Action checklists feeding Phase 4 (implementation deep-dive) and deliverable (b) (the compliance
checklist). Priorities: **Immediate** = needed by the applicable date with no transition; **Short-term**
= within the first compliance cycle; **Ongoing** = continuous.

> Code references below point at [code-of-practice-final.md](code-of-practice-final.md). The Code is
> voluntary and adherence is **not conclusive evidence** of compliance — these checklists describe a
> defensible implementation, not a safe harbour.

---

## Provider checklist — Art. 50(1) + 50(2)

| # | Action | Basis | Priority |
|---|--------|-------|----------|
| 1 | Inventory all AI systems that interact with persons or generate synthetic content | — | Prerequisite |
| 2 | Implement proactive AI-interaction disclosure at first interaction (not buried in ToS) | 50(1) | Immediate |
| 3 | For agentic systems: self-disclose in every reasonably-foreseeable human interaction | 50(1); Guidelines para. 28 | Immediate |
| 4 | Integrate digitally signed + time-stamped provenance metadata (C2PA de-facto / IPTC) into the generation pipeline | 50(2); Code Sec. 1 | Immediate |
| 5 | Apply an imperceptible, robust watermark to image/audio/video **and to free-form text > 200 tokens** (the old "provenance certificate" text route is gone; single-layer only for closed physical products or free-form text) | 50(2); Code Sec. 1 M1.1 | Immediate |
| 6 | Deploy a **free-of-charge** detection/verification mechanism (presence + confidence + provider identity), one per marking technique, results signed/downloadable; always free for authorities/researchers/media/civil society; backward-compatible on retirement (< 1m-MAU providers may charge a limited fee) | 50(2); Code Sec. 1 C2 | Immediate |
| 7 | Meet the four criteria **holistically** (effective, interoperable, robust — incl. the "analogue hole" + adversarial attacks — reliable). Remember the statutory floor is "as far as technically feasible"; the two-layer architecture is the Code route, not the statute | 50(2) | Immediate |
| 8 | Non-removal: prohibit stripping in ToS; technical resistance; re-embed after authorised edits | Code Sec. 1 | Short-term |
| 9 | Establish internal testing / robustness regime; (recommended) adversarial red-teaming | Code Sec. 1 | Short-term |
| 10 | Meet the Code's watermark-detection interoperability obligation by **2 Feb 2027** | Code Sec. 1 | Short-term |
| 11 | Annual transparency reporting on marking deployment + known limitations | Code Sec. 1 | Ongoing |
| 12 | (Optional) fingerprinting/logging registry as a complementary layer | Code Sec. 1 | Low |

---

## Deployer checklist — Art. 50(3) + 50(4)

| # | Action | Basis | Priority |
|---|--------|-------|----------|
| 1 | Inventory AI systems performing emotion recognition / biometric categorisation / generating deepfakes | — | Prerequisite |
| 2 | Confirm the use is **not prohibited** under Art. 5(1)(f)/(g) before relying on a 50(3) notice | 50(3) ↔ Art. 5 | Immediate |
| 3 | Implement disclosure notices for permitted emotion-recognition / biometric-categorisation systems | 50(3) | Immediate |
| 4 | Coordinate 50(3) disclosure with GDPR Art. 13/14 (and Art. 35 DPIA where applicable) | 50(3) + GDPR | Immediate |
| 5 | Apply modality-appropriate deepfake labels — mandatory core is the capitalised **"AI"** acronym; **"GENERATED"/"MODIFIED"** is optional & copyright-sensitive; **audio-only needs a mandatory audible disclaimer**; embed by default (overlay only as an equivalent); use the official EU icon set | 50(4); [eu-labelling-icons.md](eu-labelling-icons.md) | Immediate |
| 6 | Verify placement (first exposure, no intervening overlay, survives reshare/download), contrast (≥ 4.5:1 benchmark), size, persistence, and accessibility (alt/ARIA; avoid abbreviations other than "AI") | 50(4)/50(5) | Immediate |
| 7 | For **published text**: put a policy in place naming the person with editorial responsibility (name, role, contact) and publish those details (media service providers under the EMFA may use existing procedures) | 50(4); Code Sec. 2 C4 | Short-term |
| 8 | Establish internal procedures to identify content requiring labelling; train staff; run a review mechanism and act on substantiated mislabelling reports without undue delay | Code Sec. 2 | Short-term |
| 9 | Document every exception claimed (artistic / law-enforcement / public-interest-text-review) with reasoning; note that "primarily commercial" marketing gets no artistic pass | 50(4)/50(6) | Short-term |
| 10 | Re-label artistic content if it leaves its original context | 50(4) | Ongoing |

---

## Both roles — cross-cutting (Art. 50(5))

- Disclosures are **clear, distinguishable, timely** (at the latest at first interaction/exposure) and
  **accessible** — conform to the *applicable* accessibility requirements (Art. 50(5)); assess whether the
  European Accessibility Act (Directive (EU) 2019/882) applies, and use WCAG AA as the design benchmark.
- Decide and record **Code signatory intent** (deadline **22 Jul 2026**).
- Do **not** retrospectively mark/label content already public before 2 Aug 2026 (voluntary only).

---

## SME / startup proportionality

| Measure | Full requirement | Proportionate SME route |
|---------|------------------|--------------------------|
| Metadata embedding | Bespoke C2PA integration | Managed C2PA libraries / API services |
| Watermarking | Custom imperceptible watermarking | Third-party or open-source watermarking services |
| Detection | Self-hosted detection service | Shared detection infrastructure / verification platforms |
| Reporting | Comprehensive transparency report | Simplified report (activation rate + known limitations) |
| Testing | Internal red-teaming | Public benchmark suites; collaborative testing |

National AI regulatory sandboxes (Art. 57–62) are available to test compliance approaches with reduced
regulatory risk.
