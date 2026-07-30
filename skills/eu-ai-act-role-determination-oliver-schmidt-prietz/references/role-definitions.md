# AI Act Role Definitions — Art. 3(3)-(7)

## Provider (Anbieter) — Art. 3(3)

**Legal definition:**

> 'provider' means a natural or legal person, public authority, agency or other body that develops an AI system or a general-purpose AI model or that has an AI system or a general-purpose AI model developed and places it on the market or puts the AI system into service under its own name or trademark, whether for payment or free of charge.

*German: 'Anbieter' bezeichnet eine natürliche oder juristische Person, Behörde, Einrichtung oder sonstige Stelle, die ein KI-System oder ein KI-Modell mit allgemeiner Zweckbestimmung entwickelt oder entwickeln lässt und es unter ihrem eigenen Namen oder ihrer eigenen Marke in Verkehr bringt oder das KI-System unter ihrem eigenen Namen oder ihrer eigenen Marke in Betrieb nimmt, sei es entgeltlich oder unentgeltlich.*

**Key elements:**
1. **Develops or has developed** — includes in-house development AND commissioning development by third party
2. **Places on market OR puts into service** — either making it available (market) or first real-world use (service)
3. **Under own name or trademark** — the crucial attribution element
4. **Payment not required** — free systems also count

**Who is a provider:**
- Company that builds and sells an AI system
- Company that commissions development and markets it under own brand
- Open-source developer who publishes an AI system (limited obligations)
- Company that develops AI for internal use and puts it into service under own name

**Recitals:** 83-85

---

## Deployer (Betreiber) — Art. 3(4)

**Legal definition:**

> 'deployer' means a natural or legal person, public authority, agency or other body using an AI system under its authority, except where the AI system is used in the course of a personal non-professional activity.

*German: 'Betreiber' bezeichnet eine natürliche oder juristische Person, Behörde, Einrichtung oder sonstige Stelle, die ein KI-System in eigener Verantwortung verwendet, es sei denn, das KI-System wird im Rahmen einer persönlichen und nicht beruflichen Tätigkeit verwendet.*

**Key elements:**
1. **Uses** — actual deployment and operation of the AI system
2. **Under its authority** — the deployer has control over how the system is used
3. **Professional context** — excludes purely personal/household use
4. **No development required** — the deployer typically obtains the system from a provider

**Who is a deployer:**
- Company that purchases an AI recruitment tool from a vendor and uses it
- Hospital deploying a medical AI diagnostic tool
- Bank using a third-party credit scoring AI system
- Government agency using an AI system for benefit processing
- Employer using AI for employee monitoring

**Recitals:** 86-87

---

## Authorized Representative (Bevollmächtigter) — Art. 3(5)

**Legal definition:**

> 'authorised representative' means a natural or legal person located or established in the Union who has received and accepted a written mandate from a provider of an AI system or a general-purpose AI model to, respectively, carry out and perform on its behalf the obligations and procedures established by this Regulation.

**Key elements:**
- Must be established in the EU
- Acts on behalf of a non-EU provider
- Written mandate required
- Carries out provider obligations within the EU

**When needed:** Non-EU providers who place AI systems on the EU market must designate an authorized representative (Art. 22).

---

## Importer (Einführer) — Art. 3(6)

**Legal definition:**

> 'importer' means a natural or legal person located or established in the Union that places on the market an AI system that bears the name or trademark of a natural or legal person established in a third country.

*German: 'Einführer' bezeichnet eine in der Union ansässige oder niedergelassene natürliche oder juristische Person, die ein KI-System in Verkehr bringt, das den Namen oder die Marke einer in einem Drittland niedergelassenen natürlichen oder juristischen Person trägt.*

**Key elements:**
1. **Located/established in EU** — the importer must be in the EU
2. **Places on market** — makes the system available on EU market
3. **Bears name of third-country person** — the system carries the original (non-EU) provider's branding
4. **Not the developer** — the importer did not develop the system

**Who is an importer:**
- EU company that distributes a US-built AI system in Europe under the US company's brand
- EU distributor bringing Chinese AI hardware into the EU market

**Obligations:** Art. 23 — importers must verify CE marking, documentation, and provider compliance.

**Recitals:** 88

---

## Distributor (Händler) — Art. 3(7)

**Legal definition:**

> 'distributor' means a natural or legal person in the supply chain, other than the provider or the importer, that makes an AI system available on the Union market.

*German: 'Händler' bezeichnet eine natürliche oder juristische Person in der Lieferkette, die weder Anbieter noch Einführer ist und ein KI-System auf dem Unionsmarkt bereitstellt.*

**Key elements:**
1. **In the supply chain** — intermediary between provider/importer and deployer
2. **Not provider or importer** — residual category
3. **Makes available on EU market** — supplies, resells, or distributes

**Who is a distributor:**
- IT reseller offering AI software from a provider
- Technology marketplace hosting third-party AI systems
- System integrator who distributes (but does not modify) AI systems

**Obligations:** Art. 24 — distributors must verify conformity marking and not supply non-compliant systems.

**Recitals:** 89

---

## Role Determination Logic

### Decision Tree

```
START: Assess the organization's relationship to the AI system

1. Did the organization develop the AI system (or have it developed)?
   AND does it place on market / put into service under own name?
   ├─ YES → PROVIDER (Art. 3(3))
   └─ NO → Continue

2. Does the organization use the AI system under own authority
   in professional capacity?
   ├─ YES → DEPLOYER (Art. 3(4))
   │         (but check Art. 25 quasi-provider risk — Phase 3)
   └─ NO → Continue

3. Does the organization import the AI system from third country
   to place on EU market (bearing third-country provider's name)?
   ├─ YES → IMPORTER (Art. 3(6))
   └─ NO → Continue

4. Does the organization make the AI system available on EU market
   (not as provider or importer)?
   ├─ YES → DISTRIBUTOR (Art. 3(7))
   └─ NO → Continue

5. Does the organization integrate the AI system into its product
   as a product manufacturer?
   ├─ YES → Product manufacturer — see Art. 25(3)
   │         (may be treated as PROVIDER)
   └─ NO → Role unclear — seek legal counsel
```

### Multiple Roles

An organization may simultaneously be:
- **Provider** of system A AND **deployer** of system B
- **Provider** (self-developed system) AND **deployer** (purchased vendor system)
- **Distributor** AND **deployer** (distributes AND uses the system)
- **Importer** AND **deployer** (imports AND uses the system)

Each role carries its own set of obligations. Assess per system.

---

## Commission Value Chain Guidance

The Commission has emphasized the following principles for value chain responsibility:

1. **Provider bears primary responsibility** for high-risk system compliance
2. **Deployer must ensure proper use** within the provider's intended purpose
3. **Each actor in the chain is responsible** for actions within their control
4. **Art. 25 prevents responsibility gaps** — modifications that affect compliance transfer provider obligations
5. **Cooperation duty** — all actors must cooperate with market surveillance authorities (Art. 21)
