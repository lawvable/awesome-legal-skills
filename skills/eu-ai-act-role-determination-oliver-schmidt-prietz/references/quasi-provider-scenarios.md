# Quasi-Provider Scenarios — Art. 25 AI Act

## Legal Text — Art. 25(1)

> Any distributor, importer, deployer or other third party shall be considered to be a provider of a high-risk AI system for the purposes of this Regulation and shall be subject to the obligations of the provider under Article 16, in any of the following circumstances:

> (a) they put their name or trademark on a high-risk AI system **already placed on the market or put into service**, without prejudice to contractual arrangements stipulating that the obligations are otherwise allocated;

> (b) they make a **substantial modification** to a high-risk AI system that has already been placed on the market or put into service in such a way that it remains a high-risk AI system pursuant to Article 6;

> (c) they **modify the intended purpose** of an AI system, including a general-purpose AI system, which has not been classified as high-risk and has already been placed on the market or put into service in such a way that the AI system becomes a high-risk AI system in accordance with Article 6.

*German: Wesentliche Veränderung (Art. 25 Abs. 1 Buchst. b), Zweckänderung (Art. 25 Abs. 1 Buchst. c)*

**Recitals:** 84, 128

---

## Scenario 1: Own Name or Brand — Art. 25(1)(a)

### Description

An entity places its own name, trademark, or brand on a high-risk AI system that was originally developed and placed on the market by another provider (white-labeling, rebranding).

### Trigger Conditions

| Condition | Description |
|-----------|-------------|
| High-risk system | System is already classified as high-risk |
| Already on market | Original provider has placed it on market |
| Rebranding | New entity adds own name/trademark |
| Public-facing | System is presented to users/market under new brand |

### Assessment Questions

1. "Does your organization present this AI system to customers or users under your own name, brand, or trademark?"
2. "Do end users associate the system with your organization rather than the original provider?"
3. "Have you removed or replaced the original provider's branding?"
4. "Do marketing materials, documentation, or user interfaces show your organization as the system provider?"

### Consequence

If YES to any → organization is treated as **provider** with full Art. 16 obligations:
- New conformity assessment required (unless contractual allocation per Art. 25(1)(a) caveat)
- CE marking under own responsibility
- Technical documentation obligations
- Post-market monitoring
- Incident reporting

### Contractual Exception

Art. 25(1)(a) includes "without prejudice to contractual arrangements stipulating that the obligations are otherwise allocated." This means obligations may be contractually shared — but:
- The rebranding entity remains the visible provider to authorities and market
- Contractual allocation does not release from public-law obligations entirely
- Both parties should clearly document responsibility allocation

---

## Scenario 2: Substantial Modification — Art. 25(1)(b)

### Description

An entity makes a substantial modification (wesentliche Veränderung) to an already-deployed high-risk AI system, and the system remains high-risk after the modification.

### Trigger Conditions

| Condition | Description |
|-----------|-------------|
| High-risk system | System was/remains high-risk |
| Already on market/in service | Originally placed on market by another provider |
| Substantial modification | Change meets Art. 3(23) definition |
| System remains high-risk | Post-modification classification unchanged |

### What is "Substantial Modification"? — Art. 3(23)

See [substantial-modification.md](substantial-modification.md) for detailed analysis.

> 'substantial modification' means a modification to an AI system after its placing on the market or putting into service that is not foreseen or planned in the initial conformity assessment carried out by the provider and as a result of which the compliance of the AI system with the requirements set out in Chapter III, Section 2 is affected or the intended purpose for which the AI system has been approved is modified.

### Consequence

If substantial modification is confirmed → organization becomes **new provider**:
- Must conduct new conformity assessment
- Must produce new technical documentation
- Must comply with Art. 16 provider obligations
- Original provider's CE marking may no longer be valid

### Art. 25(2) Support Obligation

> Where a new provider referred to in paragraph 1 modifies the intended purpose or the AI system, the original provider shall, upon request, and without undue delay:
> (a) provide technical documentation;
> (b) provide other information necessary for the conformity assessment;
> (c) cooperate with the new provider.

The original provider MUST cooperate and provide support to the new (quasi-)provider.

---

## Scenario 3: Changed Intended Purpose — Art. 25(1)(c)

### Description

An entity changes the intended purpose (Zweckbestimmung) of a non-high-risk AI system in a way that makes it high-risk.

### Trigger Conditions

| Condition | Description |
|-----------|-------------|
| Originally NOT high-risk | System was classified as non-high-risk (or not yet classified) |
| Intended purpose changed | Entity uses system for different purpose than provider intended |
| Becomes high-risk | New purpose brings system under Art. 6 / Annex III |

### Assessment Questions

1. "What was the original intended purpose specified by the provider (Art. 3(12))?"
2. "How is your organization actually using the system?"
3. "Does the new use fall within an Annex III category?"

### Common Examples

| Original Purpose | Changed Purpose | High-Risk? |
|-----------------|----------------|------------|
| General chatbot (customer service) | HR screening assistant (evaluating candidates) | YES — Annex III Nr. 4a |
| Image classification (product quality) | Biometric identification (employee access) | YES — Annex III Nr. 1a |
| Text summarization (research) | Legal case analysis (judicial support) | YES — Annex III Nr. 8a |
| Sentiment analysis (marketing) | Emotion recognition (workplace monitoring) | PROHIBITED — Art. 5(1)(f) |

### Consequence

If intended purpose change triggers high-risk → organization becomes **provider**:
- Full Art. 16 provider obligations
- New conformity assessment required
- Must register in EU database
- Must comply with all Chapter III, Section 2 requirements

---

## Scenario 4: Product Manufacturer (System as Component) — Art. 25(3)(a)

### Description

A product manufacturer places on the market or puts into service a high-risk AI system together with their product under their own name or trademark.

### Trigger Conditions

| Condition | Description |
|-----------|-------------|
| Product manufacturer | Entity manufactures a physical or digital product |
| AI system integrated | High-risk AI system is incorporated into the product |
| Own name/trademark | Product bears manufacturer's branding |
| Placing on market | Product+AI system are made available together |

### Assessment Questions

1. "Do you manufacture a product that incorporates this AI system?"
2. "Is the product sold under your name or trademark?"
3. "Is the AI system a component of the product as placed on market?"

### Common Examples

- Car manufacturer integrating third-party autonomous driving AI
- Medical device manufacturer using AI diagnostic module
- Industrial robot manufacturer incorporating AI motion control
- Smart home device manufacturer with embedded AI assistant

### Consequence

Product manufacturer is treated as **provider** of the high-risk AI system and bears Art. 16 obligations.

---

## Scenario 5: Product Manufacturer (Post-Market) — Art. 25(3)(b)

### Description

A product manufacturer puts into service a high-risk AI system bearing their name or trademark after the AI system has already been placed on the market by another entity.

### Trigger Conditions

| Condition | Description |
|-----------|-------------|
| Product manufacturer | Same as Scenario 4 |
| AI already on market | AI system was previously placed on market by original provider |
| Manufacturer branding | AI system now bears manufacturer's name |
| Putting into service | Manufacturer activates/deploys the AI system |

### Consequence

Same as Scenario 4 — manufacturer assumes provider obligations.

---

## Art. 25(4) Exception — Foreseen Modifications

**Legal text:**

> Paragraph 1(b) shall not apply where:
> - the modification was foreseen by the provider, AND
> - the modification was covered in the initial conformity assessment

### Assessment Questions

1. "Does the original provider's documentation specifically describe the type of modification you made?"
2. "Was the modification included in the scope of the original conformity assessment?"
3. "Does the provider's technical documentation or operating instructions explicitly permit this modification?"

If YES to all → Art. 25(4) applies → no quasi-provider status triggered.

**Example:** A provider's operating instructions state that the model can be finetuned with customer-specific data within specified parameters and this was included in the conformity assessment. A deployer finetuning within those parameters does not become a quasi-provider.

---

## Summary: Quasi-Provider Risk Matrix

| Scenario | Action | Risk Level | Art. 25 Reference |
|----------|--------|------------|-------------------|
| Rebranding/white-labeling | Adding own name/brand | HIGH | Art. 25(1)(a) |
| Finetuning (PEFT/LoRA) | Adapter-only modification | LOW | Art. 25(1)(b) — likely not substantial |
| Finetuning (layer-wise) | Partial weight modification | MEDIUM | Art. 25(1)(b) — case-by-case |
| Full retraining | Complete model retraining | HIGH | Art. 25(1)(b) — likely substantial |
| Purpose change (same risk) | Different use, same risk tier | MEDIUM | Art. 25(1)(c) if becomes high-risk |
| Purpose change (higher risk) | Non-HR use → HR use | HIGH | Art. 25(1)(c) |
| Product integration | AI in own product | HIGH | Art. 25(3)(a-b) |
| Configuration within range | Using provider's settings | NONE | Not a modification |
| Foreseen modification | Covered by provider's CA | NONE | Art. 25(4) exception |
