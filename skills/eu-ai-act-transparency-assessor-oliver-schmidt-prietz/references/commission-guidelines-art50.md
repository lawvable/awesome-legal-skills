# Commission Guidelines on Article 50 (Draft) — Reference

The Commission's **Guidelines on the implementation of the Article 50 transparency obligations** are the
**broad** interpretive instrument: issued under **Art. 96(1)(d)** AI Act, they set out the Commission's
interpretation of Art. 50 for providers, deployers, and competent authorities across the **full scope of
all four duties** (the key difference from the Code, which only covers 50(2)/(4)).

**Status (checked 2026-07-04):** **still draft.** The ~40-page text was published **8 May 2026** and was
open for consultation until **3 June 2026**. The consultation has closed; the Guidelines are expected to be
finalised before 2 August 2026 but are **not yet final** — flag their draft status and web-check on
activation (the official timeline still shows only the 8 May draft, no final entry). Paragraph numbers below
are from the draft and may shift on finalisation.

**Legal weight:** explicitly **non-binding**. Only the **CJEU** can give an authoritative interpretation
of Art. 50. Treat the Guidelines as persuasive interpretive guidance, not black-letter law — and always
flag their draft status to the user.

> Web check on activation: search whether the Guidelines have been finalised/adopted, since this may
> change between this file's reference date and use.

---

## Interpretive moves practitioners should know

### 1. The "obvious" exemption (50(1)) → average-consumer multi-factor test
The Guidelines benchmark the 50(1) "obvious from the circumstances" exemption against the **average
consumer** standard from EU consumer-protection law, applied through a multi-factor test that accounts
for **vulnerable groups** and **AI literacy**. Examples treated as plausibly "obvious": **developer-only
code assistants** and **in-game NPCs**. (Operationalised in
[obviousness-and-exceptions.md](obviousness-and-exceptions.md) §1.)

### 2. Agentic AI → self-disclose where plausible (para. 28)
Where a provider cannot reliably determine whether an **autonomous agent** will interact with a natural
person, the agent must self-disclose its artificial nature in **every situation where such interaction is
reasonably foreseeable** (para. 28). This shifts the default from "disclose where certain" to "disclose
where plausible" — and goes **further than the Act itself**, which does not use the word "agent".

### 3. No retrospective marking/labelling of pre-application outputs
Outputs already in the information ecosystem **before 2 August 2026** do **not** need to be marked or
labelled retrospectively. Voluntary marking is encouraged but not required.

### 4. Penalty band — correct the common error
Non-compliance with Art. 50 sits in the **second-highest** fine band: up to **EUR 15,000,000 or 3% of
worldwide annual turnover** (**EUR 750,000** for EU institutions/bodies) — the precise hook is
**Art. 99(4)(g)** (paras. 140). If you see **€35M / 7%** cited for Art. 50, that is **wrong** — that band is
reserved for Art. 5 prohibited practices.

### 5. Horizontal findings (before the four paragraphs)
- **"Mere distribution" stays outside** (para. 12): an actor merely disseminating/transmitting AI content,
  **including online platforms**, is **not a deployer**.
- **Personal-use carve-out is narrow** (para. 17): the Art. **2(10)** "purely personal non-professional
  activity" exception is lost where the activity **affects public discourse** (a deepfake of a local mayor to
  criticise policy is not covered). **FOSS does not help** — open-source systems remain fully subject to Art. 50.
- **Art. 50/Art. 53 layering** (paras. 23–24): Art. 50 attaches at the **AI-system** layer, Art. 53 at the
  **model** layer; one product can engage both.

### 6. Art. 50(2) scope — what the Guidelines pull IN and carve OUT
- **Not GPAI-specific** (para. 54): **any** system generating synthetic audio/image/video/text is captured,
  **including single-purpose tools** — the Guidelines name a **translation engine**, a voice cloner, and a
  single-domain image generator. → *Machine translation is IN scope* (operationalised in
  [obviousness-and-exceptions.md](obviousness-and-exceptions.md) §2).
- **Source code is exempt** (para. 64): source code, incl. inline comments/docstrings that are part of the
  code artefact. But **standalone documentation** (README, marketing copy, NL explanations generated
  separately) is ordinary text and **re-enters** 50(2). Coding-agent vendors should design disclosures around
  this line, not a blanket "we only generate code".
- **B2B/industrial is narrower than it sounds** (para. 81): **cumulative** conditions — output *strictly
  technical* **and** intended only for a *limited, pre-defined internal* professional audience. **Any**
  external recipient (customer, supplier, contractor) reinstates the duty. "We only use it internally" is not
  enough on its own.
- **In-game generation** (para. 82): synthetic content generated *as part of gameplay* — obvious fictional
  context + no deceptive purpose ⇒ relief from marking; scenario-specific, not unconditional.
- **Detection is half the duty** (para. 65): read with 50(5), detection means must be available to third
  parties **at the latest at exposure** — a marking-only compliance story is incomplete.

### 7. Art. 50(1) — the negative catalogue
The Guidelines give an unusually explicit list of what **does not** satisfy 50(1) (para. 35): disclosure
buried in **T&Cs**, **machine-readable signals alone**, generic references to an "**assistant**", and
statements like "**this system uses LLMs**" — **all fail**. Several are common practice today, so 50(1)
requires an *active redesign* of disclosures, not just maintenance. Obviousness is anchored in the UCPD
**average-consumer** standard with a **vulnerable-group** sensitivity layer (paras. 40–42); for
general-audience systems and **AI companions** (named), the "obvious" exemption is largely closed.

### 8. Art. 50(3) — broader than the high-risk lens
Two points (para. 98): (a) the 50(3) notice duty applies **in addition to** any Annex III high-risk or
Art. 5 analysis, on its own terms; (b) it covers **all biometric categorisation**, **including systems
outside the high-risk classification** — inferring **age range or gender** for advertising, store
analytics or content adaptation still owes a 50(3) notice when operating in the Union, even where the
provider screened the system out of the high-risk catalogue (inferring **race/ethnicity** is instead a
*prohibited* Art. 5(1)(g) categorisation, not a 50(3)-notice case).

### 9. Art. 50(4) — the four-element deepfake test
The Guidelines unfold Art. 3(60) into four elements (para. 107) and judge "false authenticity" against the
**actual audience** (para. 108), not an average person; **substantive** AI edits of journalistic images can
create a deepfake even though minor technical edits do not (para. 109); the **"evidently" artistic** limb
excludes **primarily-commercial** content (para. 114) and softens the *form* of disclosure only, leaving
personality/IP/data-protection rights intact (Recital 134; para. 116). Full operational test in
[obviousness-and-exceptions.md](obviousness-and-exceptions.md) §3.

---

## How the two instruments divide the work

| | Commission Guidelines | Code of Practice |
|---|----------------------|------------------|
| Legal basis | Art. 96(1)(d) | Art. 50(7) (assessed via Art. 56(6)) |
| Drafted by | The Commission | Independent experts (AI Office process) |
| Scope | **All** of 50(1)–(5) | **Only** 50(2), 50(4), 50(5) |
| Status (2026-07-04) | **Draft** (8 May 2026; consultation closed 3 Jun) | **Final** (10 Jun 2026), under adequacy assessment (pending) |
| Binding? | No (CJEU authoritative; but MSAs/AI Office likely to follow, divergence must be justified) | No (voluntary; adherence ≠ conclusive evidence) |
| Reach | Everyone in scope | Signatories (a compliance-demonstration vehicle); non-signatories bear the burden of showing an equally effective/interoperable/robust/reliable route |

Use the **Guidelines** for interpretation across the whole of Art. 50 (especially 50(1)/50(3), which the
Code does not touch); use the **Code** ([code-of-practice-final.md](code-of-practice-final.md)) for the
*how* of 50(2) marking and 50(4) labelling.

### Where they diverge — model-level marking
The clearest divergence is **upstream (GPAI model-level) marking**. The **Guidelines** merely *encourage*
GPAI model providers to implement marking at the model level, even where they would not formally fall within
Art. 50 (paras. 24, 70) — a "strongly suggested best practice". The **Code** treats model-level marking as a
**commitment for its signatories** (Measure 1.1.2). So a GPAI model provider that is **not** a Code signatory
can rely on the softer Guidelines wording — creating a dependency for downstream system providers, who still
owe 50(2) on their own outputs. Neither instrument makes this an **Art. 53** duty (Art. 53(1)(d) is the
training-data summary — a frequent mis-citation to correct).
