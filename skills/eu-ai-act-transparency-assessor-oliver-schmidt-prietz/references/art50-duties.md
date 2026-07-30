# Article 50 Transparency Duties — Reference

The five transparency duties of Art. 50 AI Act (Regulation (EU) 2024/1689), plus the cross-cutting
exception governance of 50(6). These apply **regardless of risk tier** — even a minimal-risk system
must comply if it triggers any Art. 50 category.

> For the verbatim regulation text and recitals 132–137, cross-reference
> `ai-act-knowledge/references/core/regulation-title-IV-transparency.md` rather than relying on the
> summaries below.

**Penalty for non-compliance:** Tier 2 — up to **EUR 15,000,000 or 3% of total worldwide annual
turnover**, whichever is higher (Art. 99(4)). *Not* the €35M / 7% band — that band is Art. 5
prohibited practices only.

**Who each duty binds:**

| Duty | Binds | Subject matter |
|------|-------|----------------|
| 50(1) | **Provider** | AI-interaction disclosure |
| 50(2) | **Provider** | Machine-readable marking of synthetic output |
| 50(3) | **Deployer** | Emotion-recognition / biometric-categorisation notice |
| 50(4) | **Deployer** | Deepfake + public-interest-text labelling |
| 50(5) | whoever owes (1)–(4) | Delivery quality (clear / distinguishable / timely / accessible) |
| 50(6) | — | Exception governance + implementing-act hook |

A single organisation that is **both** provider and deployer owes the provider duties *and* the
deployer duties.

---

## 1. Art. 50(1) — AI Interaction Disclosure (Provider)

**Legal summary:** Providers must design AI systems intended to interact directly with natural persons
so that those persons are informed they are interacting with an AI system — **unless this is obvious**
from the circumstances and context of use.

| Element | Detail |
|---------|--------|
| Who it binds | Provider (Anbieter) |
| Trigger | AI system interacts directly with natural persons (chatbot, voice agent, AI avatar, autonomous agent) |
| Implementation | Clear, proactive disclosure at the start of the interaction |
| "Obvious" exemption | Benchmarked to the **average consumer** under a multi-factor test — see [obviousness-and-exceptions.md](obviousness-and-exceptions.md) |
| Exception | Authorised law-enforcement / criminal-investigation use with safeguards (50(1) last sentence) |

**Design requirement:** disclosure must be proactive and precede substantive interaction. Burying the
disclosure in terms of service or a privacy policy does **not** satisfy 50(1).

**Agentic AI (draft Guidelines para. 28):** where a provider cannot reliably determine in advance
whether an autonomous agent will interact with a natural person, the agent must self-disclose its
artificial nature in **every situation where human interaction is reasonably foreseeable** — a shift
from "disclose where certain" to "disclose where plausible". The Act itself does not use the word
"agent"; this is an interpretive move in the draft Guidelines (non-binding — see
[commission-guidelines-art50.md](commission-guidelines-art50.md)).

---

## 2. Art. 50(2) — Synthetic-Content Marking (Provider)

**Legal summary:** Providers of AI systems that generate **synthetic audio, image, video, or text**
must ensure outputs are marked in a **machine-readable format** and detectable as artificially
generated or manipulated. The marking must be **effective, interoperable, robust, and reliable**
(the four statutory criteria).

| Element | Detail |
|---------|--------|
| Who it binds | Provider (Anbieter) |
| Trigger | AI system generates synthetic audio, image, video, or text — **not GPAI-specific**; single-purpose tools (e.g. a **translation engine**) are captured (draft Guidelines para. 54) |
| Statutory floor | Marked **machine-readable** + **detectable**; effective/interoperable/robust/reliable **"as far as technically feasible"** given content type, cost, and state of the art. **No specific technique or "two layers" is mandated by the statute.** |
| Code route | The **Code** operationalises this as a **layered** solution (signed metadata + imperceptible watermark) — voluntary best practice, not the floor (see [code-of-practice-final.md](code-of-practice-final.md)) |
| Standard | Marking must survive reasonably foreseeable transformations |
| Exception | Assistive function for standard editing; no substantial alteration of the input data provided by the **deployer** (50(2) last sentence) — see [obviousness-and-exceptions.md](obviousness-and-exceptions.md) |

This is the most technically demanding Art. 50 duty and the one the **Code of Practice** (Section 1,
Providers) operationalises. It is also the **only** Art. 50 duty touched by the Digital Omnibus grace
period — see [timeline-and-grace.md](timeline-and-grace.md).

---

## 3. Art. 50(3) — Emotion Recognition / Biometric Categorisation Notice (Deployer)

**Legal summary:** Deployers of emotion-recognition or biometric-categorisation systems must inform the
natural persons exposed to them of the system's operation, and process personal data in accordance with
applicable Union law.

| Element | Detail |
|---------|--------|
| Who it binds | Deployer (Betreiber) |
| Trigger | System performs emotion recognition (Emotionserkennung) or biometric categorisation |
| Implementation | Clear disclosure of the system's operation to affected persons |
| **Art. 5 gate** | Emotion recognition in the **workplace / education** is *prohibited* (Art. 5(1)(f)); biometric categorisation for sensitive characteristics is *prohibited* (Art. 5(1)(g)). 50(3) applies **only to permitted uses** (e.g. medical, safety, security, entertainment / age-estimation) |
| **Additive & broad** | 50(3) applies **in addition to** any Annex III high-risk or Art. 5 analysis — on its own terms — and covers **all** biometric categorisation, **including systems outside the high-risk classification** (draft Guidelines para. 98). Inferring **age range or gender** for advertising, store analytics or content adaptation still owes a 50(3) notice, even where the system was screened out of the high-risk catalogue. **Race/ethnicity inference is *not* a 50(3) example — it is a prohibited Art. 5(1)(g) categorisation; the Art. 5 gate above governs** |

**GDPR coordination:** 50(3) explicitly requires compliance with applicable data-protection law.
Deployers must also satisfy GDPR Art. 13/14 information duties and, where applicable, Art. 35 DPIA.

**Order of operations:** first run the **Art. 5** gate (prohibited use → the prohibition governs, a 50(3)
notice cannot cure it); if permitted, the 50(3) notice is owed **regardless of risk tier**.

---

## 4. Art. 50(4) — Deepfake & Public-Interest-Text Labelling (Deployer)

**Legal summary:** Deployers of AI systems that generate or manipulate image, audio, or video content
constituting a **deepfake** must disclose that the content is artificially generated or manipulated.
A parallel duty applies to AI-generated/manipulated **text published to inform the public on matters of
public interest**.

| Element | Detail |
|---------|--------|
| Who it binds | Deployer (Betreiber) |
| Trigger | AI-generated / AI-manipulated content that constitutes a **deepfake** — **Art. 3(60)** (verbatim): image, audio or video content that "**resembles existing persons, objects, places, entities or events and would falsely appear to a person to be authentic or truthful**". The draft Guidelines add a four-element gloss (**appreciable** resemblance · **capable of existing** · the listed subjects · false authenticity **judged by the actual audience**) — apply that test, see [obviousness-and-exceptions.md](obviousness-and-exceptions.md) §3 |
| Implementation | Clear, human-perceptible labelling — mandatory core is the capitalised **"AI"** acronym; use the official **EU icon set** (see [eu-labelling-icons.md](eu-labelling-icons.md)) |
| Exceptions | (1) authorised law enforcement; (2) **evidently** artistic / creative / satirical / fictional works → *proportionate* disclosure (form only; **primarily-commercial** content gets no pass); (3) public-interest **text** under human editorial review/control — see [obviousness-and-exceptions.md](obviousness-and-exceptions.md) |

The labelling duty stays with the **deployer** — the actor with authority over the AI's use — even
where the provider has separately marked the output under 50(2). 50(2) (provider, machine-readable) and
50(4) (deployer, human-facing) are **distinct duties on distinct parties**; do not conflate them.

The Code of Practice (Section 2, Deployers) operationalises this duty.

---

## 5. Art. 50(5) — Delivery Quality (Cross-Cutting)

Not a separate trigger but a **quality standard** governing how every 50(1)–(4) disclosure must be
delivered. Information must be:

- **Clear** — plain language, no jargon, adapted to the audience;
- **Distinguishable** — visually/aurally distinct from surrounding content;
- **Timely** — at the latest at the time of first interaction or exposure, never retroactively;
- **Accessible** — conform to the **applicable accessibility requirements** (Art. 50(5) does *not* name a
  specific directive). Assess whether the **European Accessibility Act** (Directive (EU) 2019/882) applies to
  the product/service, and use **WCAG AA** as the practical design benchmark where a web/mobile UI is involved.

The Code of Practice's 50(5) cross-cutting information requirement is the third element the Code covers
(alongside 50(2) and 50(4)).

---

## 6. Art. 50(6) — Exception Governance & Implementing-Act Hook (Cross-Cutting)

- The 50(2) assistive-function exception is self-executing (provider self-assessment).
- The 50(4) exceptions (law enforcement; artistic; public-interest text) are interpreted **narrowly**.
- The Commission may adopt implementing acts specifying the technical detail of 50(2) marking, and
  approve **codes of practice** under 50(7) as a compliance pathway (see below).
- Exceptions must be **documented** — record which exception is claimed and the justification.

---

## 7. The two soft-law instruments (orientation)

Two official instruments sit beneath Art. 50. They are **not** the same thing and have different scope:

| Instrument | Legal basis | Scope | Status (30 Jun 2026) |
|------------|-------------|-------|----------------------|
| **Commission Guidelines on Art. 50** | Art. 96(1)(d) | *All* of 50(1)–(5) — broad interpretive guidance | **Draft** (8 May 2026; consultation closed 3 Jun 2026); non-binding, CJEU authoritative — see [commission-guidelines-art50.md](commission-guidelines-art50.md) |
| **Code of Practice on Transparency of AI-Generated Content** | Art. 50(7) | *Only* 50(2), 50(4), and the 50(5) info requirement | **Final** (10 Jun 2026); voluntary; under adequacy assessment — see [code-of-practice-final.md](code-of-practice-final.md) |

There is **no separate "Code of Conduct"** for Art. 50. "Codes of conduct" in the AI Act (Art. 95) are
a different, voluntary-high-risk-application mechanism. Art. 50(7) uses the term *codes of practice*.

> Cross-provision interactions (50 ↔ Art. 53 GPAI, 50 ↔ Art. 13 high-risk transparency, 50 ↔ Art. 5
> prohibited practices, 50 ↔ open-source) are catalogued in
> [obviousness-and-exceptions.md](obviousness-and-exceptions.md) §4.
