# Code of Practice on Transparency of AI-Generated Content (Final) — Reference

The **final** Code of Practice on Transparency of AI-Generated Content was published **10 June 2026**
(following a first draft in December 2025 and a second draft on 3 March 2026). It was drawn up by
independent experts appointed by the AI Office in a multi-stakeholder process under the **Art. 50(7)**
mechanism.

**Scope:** the Code covers **only Art. 50(2)** (provider marking), **Art. 50(4)** (deployer labelling),
and the **Art. 50(5)** cross-cutting information requirement. It does **not** cover 50(1) or 50(3).

**Two sections:**
- **Section 1 — Providers:** marking and detection of AI-generated/manipulated content.
- **Section 2 — Deployers:** labelling of deepfakes and AI-generated/manipulated text.

---

## Status & legal effect (read this first)

| Property | Value |
|----------|-------|
| Published | 10 June 2026 (final) |
| Mechanism | Art. 50(7) codes of practice |
| Binding? | **No — voluntary.** The Art. 50 obligations themselves remain legal obligations regardless |
| Commission status | Undergoing **adequacy assessment** by the Commission and the AI Board (30 Jun 2026) |
| Signing | A signature form (DOCX) must be submitted to the AI Office by **22 July 2026, 18:00 CEST**; signing is **encouraged, not mandatory** |
| Evidentiary weight | **Adherence "does not constitute conclusive evidence of compliance"** (point (a) "Objectives", in both Section 1 and Section 2) |

> **Important nuance.** Do **not** describe Code adherence as a "presumption of conformity". The
> Art. 50(7) transparency Code is softer than the Art. 56 GPAI-Code mechanism: its own text states
> adherence is *not conclusive evidence* of compliance. It is a strong, structured evidentiary anchor —
> not a safe harbour. A signatory still has to actually meet 50(2)/(4).

> The Code does **not** shift the labelling duty: under Section 2, the 50(4) labelling obligation stays
> with the **deployer** — the actor with authority over the AI's use.

---

## Three tiers — don't confuse the statutory floor with the Code architecture

The single most important framing error to avoid is treating the Code's layered architecture as *the law*.
Keep three strata distinct:

| Tier | What it requires | Legal weight |
|------|------------------|--------------|
| **1. Statutory floor — Art. 50(2)** | Outputs **marked in a machine-readable format** and **detectable** as AI-generated/manipulated; the solution **effective, interoperable, robust and reliable** *"as far as this is technically feasible, taking into account the specificities and limitations of the various types of content, the costs of implementation and the generally acknowledged state of the art."* **No specific technique — and no "two layers" — is mandated by the statute.** | **Settled law** (binds every provider in scope) |
| **2. Code route — Section 1** | The **layered architecture** below: **≥ 2 machine-readable layers** (signed metadata + imperceptible watermark), detection, quality, testing. | **Technical best practice** — voluntary; binds signatories; adherence is **not conclusive evidence** of compliance |
| **3. Robust best practice** | Defence-in-depth beyond the Code (richer provenance, fingerprinting, red-teaming, forensic detection). | Recommended, never required |

A non-signatory may meet Tier 1 by a different route, but **bears the burden** of showing it is *at least
as* effective/interoperable/robust/reliable — and should expect more information requests from market
surveillance authorities. The feasibility qualifier in Tier 1 matters most for **text**, **streaming/API
output**, and **SMEs** (see the single-layer exceptions and SME routes below).

## Section 1 — Provider marking (Art. 50(2))

### No single technical solution

The final Code deliberately prescribes **no single technique**, because **no single technique meets all
four statutory criteria** — *effectiveness, interoperability, robustness, reliability* (Art. 50(2)).
For signatories it requires marking with **at least two machine-readable layers** (Commitment 1, Measure 1.1)
so that provenance survives common transformations (screenshots, re-encoding, compression, format
conversion) — subject to two narrow single-layer exceptions (below).

> Drafting note: the final Code **removed** the earlier "fully AI-generated vs AI-assisted" taxonomy
> from the drafts and replaced it with detailed **design and placement** requirements for marks, labels,
> and disclaimers.

### The recommended layers

| Layer | Role | Sufficiency |
|-------|------|-------------|
| **Digitally signed + time-stamped metadata** | Primary. Embed provenance at generation using an open, interoperable standard (e.g. C2PA manifest; IPTC fields for images): system/provider identifier, generation timestamp, AI-generated/manipulated declaration, content type. Digitally signed; signature verification publicly accessible; embedded in the file, not merely linked | Primary layer |
| **Imperceptible, hard-to-remove watermark** | Primary. Must not degrade quality or be human-perceptible under normal conditions; must survive compression, resizing, cropping, re-encoding, screenshot capture; provider offers a verification mechanism | Primary layer |
| **Fingerprinting / perceptual hashing** | Complementary. Registry of content hashes enabling post-hoc verification when metadata/watermark are stripped | **Not sufficient alone** |
| **Logging** | Complementary. Records of generation events | **Not sufficient alone** |

The two **primary** layers are signed/time-stamped metadata **plus** an imperceptible robust watermark.
Fingerprinting and logging are **complementary measures** that do not, on their own, discharge 50(2).

> **Standards note.** The Code text refers to **"established standards"**, not to a named one. **C2PA** is
> the de-facto industry reference for the signed-metadata layer (with IPTC fields for images) — treat it as
> *the leading option*, not a legal mandate.

### Text marking — the 200-token rule (changed in the final Code)

The most consequential change from the drafts concerns **text**. The earlier drafts allowed a "provenance
certificate" (a signed manifest) as an **alternative** route for text; the **final Code dropped that
option**. Now:

- **imperceptible watermarking must be applied to any free-form text longer than 200 tokens**;
- the only carve-out is **"very short text" below the 200-token threshold**;
- because text watermarks are inherently less reliable, **detection may be restricted to verified expert
  users** (unlike image/audio/video, where public detection is expected for content that can reach the public).

Do **not** repeat the older "text is the least mature modality, use available techniques" framing as if it
were the current rule — the 200-token watermark obligation now governs for signatories.

### Two single-layer exceptions

The two-layer expectation relaxes to **a single layer** in exactly two cases (Measure 1.1):

1. **Closed physical products** — a generative system embedded in a closed, technically controlled physical
   product from which the output cannot escape. This exception is **conditional on containment**: as soon as
   the output can be **exported and shared online**, the full two-layer expectation returns.
2. **Free-form text** — which by its nature cannot carry metadata, so it is addressed through a single
   **watermark** layer. This is **inherent to the text modality** and does **not** change when the text is
   shared online (free-form text is normally shared) — text over 200 tokens stays watermark-only.

### Detection is half the duty (Commitment 2)

**Marking and detection are two obligations, not one** — read with Art. 50(5), the detection means must be
available to third parties **at the latest at the point of exposure** to the content (draft Guidelines
para. 65). A compliance story that covers only the marking leg misses half of 50(2). Concretely, the Code
asks providers to:

- offer a **detection solution free of charge**, covering **every marking technique** the provider uses
  (a public specification, downloadable software, or a cloud API);
- return results that are **clear, accessible and downloadable in a signed format**;
- keep access **always free** for **authorities, researchers, media and civil society** — a provider with
  **fewer than 1,000,000 monthly users** and high operational costs **may** charge a *limited, proportionate*
  fee for heavy commercial use, but not to those groups;
- on retiring a solution, replace it with a **backward-compatible** one so previously marked content stays
  analysable;
- (optional) offer a **forensic** mechanism for markings that have been stripped from the content.

The marking + detection must satisfy the four statutory criteria, **assessed holistically**:

- **Effectiveness** — marking embedded in a very high proportion of generated content;
- **Interoperability** — open standards; cross-platform detection;
- **Robustness** — survives ordinary processing, the **"analogue hole"** (print-and-scan, screen recording),
  and **deliberate adversarial attacks**;
- **Reliability** — low false-positive / false-negative rates.

> **Interoperability phases in.** For **metadata**-based markings, established standards apply **from the
> Code's applicability date**. For **watermark detection**, providers have until **2 February 2027** to put
> an interoperability solution in place (a public access point, an embedded signpost, a shared consortium
> route, or comparable) — a Code-specific milestone, distinct from the statutory 2 Aug 2026 / adopted
> 2 Dec 2026 dates. See [timeline-and-grace.md](timeline-and-grace.md).

Providers also commit to internal testing, transparency reporting, and (recommended) adversarial
red-teaming of marking robustness, and to **non-removal** measures (best-efforts to preserve metadata;
contractual prohibition on stripping marks; neither placing nor advertising circumvention tools; technical
resistance where feasible; re-embedding after authorised editing).

### Model-level marking & the provider→deployer bridge

Two provisions matter for the value chain (and correct a common mis-citation):

- The 50(2) obligation formally sits with the **AI-system provider**. Because systems inherit their
  behaviour from upstream models, model providers are **encouraged** to watermark **already at model level
  before release** (Measure 1.1.2) so downstream systems inherit a compliant solution. This is a
  **value-chain best practice**, *not* an Art. 53 duty (Art. 53(1)(d) is the training-data-summary
  obligation — see [obviousness-and-exceptions.md](obviousness-and-exceptions.md) §4.1).
- Providers are **encouraged** to offer an **in-product option** letting deployers apply a perceptible
  Section 2 (50(4)) label at the point of generation (Measure 1.4) — the technical bridge between provider
  marking and deployer labelling.

---

## Section 2 — Deployer labelling (Art. 50(4))

Deployers must label deepfake content with a clear, human-perceptible disclosure. The final Code moved
to **detailed design and placement requirements** and finalised an official **EU icon set** for the
purpose — see [eu-labelling-icons.md](eu-labelling-icons.md) for the icons, contrast/size/persistence
specs, and per-modality placement rules.

The label's **mandatory core is the capitalised "AI" acronym** (English); the **GENERATED / MODIFIED**
second layer is **optional** and copyright-sensitive; **audio-only content needs a mandatory audible
disclaimer** at the start. Full mandatory/optional split, the three icons, and per-modality placement are in
[eu-labelling-icons.md](eu-labelling-icons.md).

Deployers also commit to: internal procedures for identifying content that requires labelling; staff
training; a **review mechanism** that acts on substantiated mislabelling reports without undue delay; and
documenting which labelling decisions and **exceptions** (artistic / law-enforcement / public-interest-text
review) were applied and why. For **published text** (Commitment 4), a deployer that is **not** an
editorially regulated media service provider must put a **policy** in place that **names the person holding
editorial responsibility (name, role, contact) and publishes those contact details**; **media service
providers** under the European Media Freedom Act may rely on their existing editorial procedures. The
exceptions and their narrow limits are in [obviousness-and-exceptions.md](obviousness-and-exceptions.md) §3.

---

## SME proportionality

The Code acknowledges marking can burden smaller organisations and points to proportionate routes:
managed C2PA-embedding libraries/APIs instead of bespoke integration; third-party or open-source
watermarking services; shared detection infrastructure; simplified reporting. National AI regulatory
sandboxes (Art. 57–62) are available to test compliance approaches with reduced regulatory risk.

---

## What this skill must get right about the Code

1. It is **final (10 Jun 2026)** and **voluntary**, under **adequacy assessment** (still pending; a positive
   Commission/AI-Board opinion is what gives signing its evidentiary value).
2. It covers **only 50(2), 50(4), 50(5)** — not 50(1)/50(3).
3. Adherence is **not conclusive evidence** of compliance (not a "presumption of conformity").
4. Separate the **statutory floor** (machine-readable + detectable, four criteria *as far as technically
   feasible*) from the **Code route** (**≥ 2 layers**: signed metadata + imperceptible watermark;
   fingerprinting/logging complementary). No two-layer mandate exists in the statute itself.
5. **Text > 200 tokens must be watermarked**; the old "provenance certificate" route for text is **gone**.
   Single-layer only for **closed physical products** and **free-form text**.
6. **Detection is half the duty** — free-of-charge, per-technique, signed downloadable results, always free
   for authorities/researchers/media/civil society.
7. The **labelling duty stays with the deployer**; model-level marking is **encouraged best practice**, not
   an Art. 53 duty.
8. **Initial-signatory deadline 22 Jul 2026**; **watermark-detection interoperability from 2 Feb 2027**.
