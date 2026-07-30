# Obviousness Test, Exceptions & Boundaries — Reference

Every Art. 50 trigger has a release valve — an obviousness exemption (50(1)), an assistive-function
exemption (50(2)), or a set of narrow exceptions (50(4)). This file collects them in one place, plus
the boundary analysis for "is my use case in scope at all?" and the interactions with other AI Act
provisions.

---

## 1. The 50(1) "obvious" exemption — average-consumer benchmark

50(1) does not apply where it is **obvious**, from the circumstances and context of use, that the
person is interacting with an AI system. The draft Commission Guidelines benchmark "obvious" against
the **average consumer** standard borrowed from EU consumer-protection law — a reasonably well-informed,
observant, and circumspect person — applied through a **multi-factor test**:

| Factor | Effect on "obviousness" |
|--------|-------------------------|
| **Context of use** | A clearly labelled "AI assistant" widget is more obviously AI than an unbranded chat window |
| **Target audience** | Adjust for **vulnerable groups** (children, elderly, cognitively impaired) — what is obvious to an average adult may not be |
| **AI literacy** | Lower assumed literacy → higher disclosure burden |
| **Realism of the interaction** | A human-sounding voice agent that never self-identifies is *less* obviously AI, not more |

**Examples the Guidelines treat as plausibly "obvious" (disclosure may not be required):**
- developer-only code assistants used by professional engineers who know they are using an AI tool;
- non-player characters (NPCs) in a video game, where the fictional/game context makes AI nature obvious.

**Default when uncertain:** disclose. The exemption is narrow; the burden of showing obviousness sits
with the provider. For **agentic AI** the default is even stronger — self-disclose in every reasonably
foreseeable human-interaction situation (draft Guidelines para. 28).

---

## 2. The 50(2) assistive-function exemption

The provider marking duty does **not** apply where the AI system:

- performs an **assistive function for standard editing** (spell-check, grammar, basic formatting,
  noise reduction, colour correction); **and**
- does **not substantially alter** the input data provided by the **deployer** or its semantics.
  *(The statute says "input data provided by the deployer" — a defined term, not "the user".)*

**Boundary test:** does the output constitute a *new creative work* or merely an *improved version of
the user's own work*? Generation (new text/images from a prompt) always requires marking. Refinement
(correcting typos, adjusting brightness) does not.

### Boundary analysis (marking/labelling required vs. out of scope)

| WITHIN SCOPE (mark/label) | OUT OF SCOPE | Distinguishing factor |
|---------------------------|--------------|-----------------------|
| AI-generated image from a text prompt | AI brightness/contrast enhancement | Creation vs. enhancement |
| AI voice clone synthesising speech | AI noise reduction on a real recording | Synthetic generation vs. quality improvement |
| AI-generated article published as news | AI spell-checker fixing typos | Substantial alteration vs. assistive function |
| AI face-swap video (deepfake) | AI stabilisation of genuine footage | Identity manipulation vs. technical improvement |
| AI music generated from scratch | AI mastering of a recorded performance | Generation vs. post-processing |
| AI rewrite that changes meaning | AI spell/grammar correction that keeps meaning | Semantic alteration vs. assistive fix |
| **AI translation of existing text (in scope)** | *(not the assistive column)* | A translation **engine** generates new text — see the caution below |

> **Caution — machine translation is IN scope.** Do **not** treat AI translation as an out-of-scope
> "language transfer". The draft Guidelines (para. 54) name **"a translation engine"** as an in-scope
> example of a single-purpose 50(2) generative tool. A translation engine produces new synthetic text, so
> its outputs require 50(2) marking; the assistive/no-substantial-alteration exemption does **not** rescue
> it. (Trivial in-place fixes that preserve meaning — spell-check, grammar — remain assistive.)

### Gray-zone scenarios

1. **AI-assisted creative collaboration** — designer generates AI logo variants, then heavily modifies
   one. Marking required if the AI's contribution is still recognisable as the creative origin; the
   assistive exemption only applies if the human rework is so extensive the AI contribution is no longer
   recognisable (a high threshold).
2. **AI-restored old photographs** — inpainting (filling missing regions) generates new content → mark;
   pure upscaling leans assistive. Mixed restoration workflows → marking is the safer default.
3. **AI background behind a real presenter** — a realistic synthetic location may be a deepfake of a
   *place* (50(4)); an abstract/fantastical background likely is not, but the synthetic background
   component still needs provider 50(2) marking.
4. **Corporate AI writing assistant** — the AI generates text → provider 50(2) marking applies. Whether
   the *deployer* must also label depends on whether the output is a deepfake (usually not for routine
   business communication); the 50(4) human-review exception may apply to published text, but 50(2)
   provider marking still applies.

---

## 3. The 50(4) deepfake analysis — two steps, not one categorical rule

**Step 1 — Is it even a deepfake? Apply Art. 3(60) properly.** A deepfake is AI-generated or manipulated
**image, audio or video** content that "resembles **existing** persons, objects, places, **entities** or
events" **and** "would falsely appear … to be authentic or truthful." The draft Guidelines (para. 107)
unfold this into **four elements** — use them as the test:

1. **Appreciable resemblance** (not identical, but more than trivial);
2. **Capable of existing in reality** — *stylised/impossible* content is **out** (a sphinx over the Eiffel
   Tower, dragons, elephants driving cars); a **photorealistic invented person or synthetic celebrity is IN**,
   because such a person plausibly could exist — working with a *fictional* likeness does not by itself
   escape the regime;
3. **Persons / objects / places / entities / events**;
4. **False appearance of authenticity** — judged against the **actual audience composition, not a
   hypothetical average person** (para. 108); the threshold **falls** where children or less digitally
   literate viewers are foreseeably exposed; **no deployer intent is required**.

Minor technical edits (colour correction, noise reduction, lighting, re-scaling, compression) typically do
**not** make content a deepfake — but **substantive AI editing of journalistic images can** (para. 109).
Heuristic: *"stylised/impossible" or "minor technical adjustment" → outside; "photorealistic/plausible" or
"substantive edit" → inside.*

**Step 2 — If it is a deepfake, does an exception apply, and how much disclosure survives?** Then run the
table below. The exceptions **soften or remove the disclosure**, they do not change Step 1.

## 3a. The 50(4) exceptions

| Exception | Scope | Conditions |
|-----------|-------|------------|
| **Law enforcement / national security** | 50(4) second subparagraph | Authorised by a competent authority for a specific investigation; never a blanket exemption |
| **Artistic / creative / satirical / fictional** | 50(4) third subparagraph | Content must be recognisable as artistic/fictional in context; deployer applies **proportionate** disclosure (placement may be in credits/description, timing may be at the end, format may be textual) — but "proportionate" ≠ "hidden". **Exception is lost** when the content leaves its original artistic context (e.g. a satirical clip reshared without its framing must be labelled) |
| **Public-interest text — human review** | 50(4) fourth subparagraph | A natural person reviewed the content and bears editorial responsibility; the publisher assumes legal accountability. Applies **only to text** — audio/image/video deepfakes must always be labelled |

**Marketing has no blanket pass — but "never" is too strong.** The test is *not* "is it an ad?" but the
two-step analysis above plus the "**evidently** artistic/creative/fictional" threshold. Per the draft
Guidelines (para. 114), content that is **primarily commercial and recognisable as such** is **excluded**
from the artistic limitation and needs **ordinary full disclosure** — so a persuasive product spot using a
photorealistic synthetic spokesperson (a Step-1 deepfake: an invented-but-plausible person) must be
labelled. Only an **evidently creative or fictional** ad *might* qualify, case by case — "if at all". So:

- **Default for marketing deepfakes: full labelling.** A synthetic brand spokesperson in a normal ad is IN
  and gets no artistic pass.
- **Do not tell the user marketing categorically qualifies** for the exception — but equally, don't assert
  it can *never* apply; apply the "evidently creative/fictional + primarily-informative-not-commercial" test.
- The artistic carve-out, where it does apply, **softens the *form* of disclosure only** — personality
  rights, IP and data-protection duties continue in full (Recital 134; Guidelines para. 116).

---

## 4. Interactions with other AI Act provisions

### 4.1 Art. 50 ↔ Art. 53 (GPAI) — a value-chain dependency, **not** an Art. 53 duty
**Get the legal hook right.** Art. **50(2)** binds providers of **AI systems**, expressly "**including
general-purpose AI systems**", and is **not GPAI-specific** (draft Guidelines para. 54). It attaches at the
**AI-system layer**. Art. **53** attaches at the **model layer** and is a *different* set of duties —
notably **Art. 53(1)(d)**, which is the **training-data content summary** obligation (a "sufficiently
detailed summary about the content used for training"). **Art. 53(1)(d) does not require marking capability,
and there is no Art. 53 duty to comply with 50(2).**

What actually happens across the chain:

- A generative AI **system** that uses a GPAI **model** must itself mark its outputs under **50(2)**; the
  model provider separately satisfies its **model-level documentation** duties under Art. 53.
- Marking is easiest when built upstream, so the model provider is **encouraged** to implement marking at
  the model level (draft Guidelines paras. 24, 70 — a "strongly suggested best practice"), and the **Code**
  expects this of its **signatories** (Measure 1.1.2). This is a **value-chain dependency / best practice**,
  not a black-letter Art. 53 obligation.
- Note the **divergence**: the Guidelines merely *encourage* model-level marking, while the Code treats it
  as a signatory commitment — so a non-signatory model provider may lean on the softer Guidelines wording
  and leave downstream system providers dependent on it. Flag that dependency to the user.

### 4.2 Art. 50 ↔ Art. 13 (High-Risk Transparency)
Art. 50 applies **on top of** Art. 13. Art. 13 = detailed technical transparency to professional
deployers; Art. 50 = public-facing disclosure of AI nature / provenance. A high-risk system that also
interacts with persons or generates content owes **both**.

### 4.3 Art. 50 ↔ Art. 5 (Prohibited Practices)
- 50(3) ↔ 5(1)(f): emotion recognition in workplace/education is prohibited; 50(3) disclosure cannot
  cure a prohibition — the Art. 5 violation takes precedence.
- 50(3) ↔ 5(1)(g): biometric categorisation for sensitive characteristics is prohibited; 50(3) only
  covers non-sensitive categorisation (e.g. age estimation).
- 50(1) ↔ 5(1)(a): concealing AI involvement to manipulate behaviour can trigger both a 50(1) breach
  and the Art. 5(1)(a) deception prohibition.

### 4.4 Art. 50 ↔ Open-Source Exemption
Art. 2(12) exempts certain free-and-open-source AI systems from most AI Act requirements — but **Art. 50
is explicitly excluded from that exemption** (draft Guidelines confirm FOSS remains fully subject to
Art. 50). Open-source chatbots (50(1)), image generators (50(2)), and voice/deepfake tools (50(2)/(4)) must
still comply.

### 4.5 Personal-use carve-out (Art. 2(10)) — narrower than it reads
The "purely personal non-professional activity" exclusion in **Art. 2(10)** is **limited where the activity
affects public discourse** (draft Guidelines para. 17): a deepfake of a local mayor shared on social media to
criticise policy **cannot** hide behind the personal-use exception. Treat "it's just personal use" with
suspicion whenever the output reaches a public audience or touches public debate.

### 4.6 "Mere distribution" is not deployment
An actor whose role is limited to **disseminating or transmitting** AI-generated content — **including
online platforms** — is **not a deployer** within Art. 50 (draft Guidelines para. 12); the 50(4) labelling
duty stays with the deployer that has authority over the AI's use. Where many actors feed one brand or
marketplace, uniformity is a **contractual** question, not a statutory one.

### 4.7 50(2) scope carve-outs from the draft Guidelines (quick reference)
Detailed in [commission-guidelines-art50.md](commission-guidelines-art50.md); the boundaries a practitioner
hits most often:
- **Source code is exempt** (para. 64) — including inline comments/docstrings that are part of the code —
  but **standalone docs** (README, marketing copy, natural-language explanations generated separately) are
  ordinary text and **re-enter** 50(2).
- **B2B/industrial is narrow** (para. 81): *strictly technical* output **and** a *limited, pre-defined
  internal* professional audience — **cumulative**; any external recipient reinstates the duty.
- **In-game generation** (para. 82): synthetic content generated *as part of gameplay* leans out of scope
  (obvious fictional context, no deceptive purpose) — scenario-specific, not unconditional.
