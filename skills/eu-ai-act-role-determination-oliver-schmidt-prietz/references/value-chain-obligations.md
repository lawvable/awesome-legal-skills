# Value Chain Obligations — Art. 22-25 AI Act

## Overview

The AI Act establishes obligations for each actor in the AI value chain: providers, authorized representatives, importers, distributors, and product manufacturers. Art. 25 creates the quasi-provider mechanism to prevent responsibility gaps.

---

## Art. 22 — Authorized Representative Obligations

**Who:** Natural or legal person established in the EU, mandated by a non-EU provider.

**Obligations:**

| # | Obligation | Description |
|---|-----------|-------------|
| 1 | Verify conformity assessment | Ensure provider has carried out conformity assessment (Art. 43) |
| 2 | Keep documentation | Maintain technical documentation + conformity assessment documentation for 10 years |
| 3 | Provide information to authorities | Cooperate with national competent authorities upon request |
| 4 | Registration | Ensure registration in EU database (Art. 49) |
| 5 | Terminate mandate if non-compliance | If provider does not comply → terminate mandate and inform market surveillance authority |

**Written mandate must include (Art. 22(2)):**
- Obligation to maintain all provider documentation
- Authority to act on behalf of provider toward authorities
- Power to cooperate with authorities

---

## Art. 23 — Importer Obligations (Einführer)

**Who:** EU-established entity placing a third-country provider's AI system on the EU market.

**Before placing on market:**

| # | Obligation | Article |
|---|-----------|---------|
| 1 | Verify conformity assessment completed | Art. 23(1) |
| 2 | Verify technical documentation exists | Art. 23(1) |
| 3 | Verify provider has appointed authorized representative | Art. 23(1) |
| 4 | Verify CE marking | Art. 23(1) |
| 5 | Verify provider is identified | Art. 23(2) |

**Ongoing obligations:**

| # | Obligation | Article |
|---|-----------|---------|
| 6 | Ensure storage/transport does not compromise compliance | Art. 23(3) |
| 7 | Inform provider and market surveillance if non-compliance suspected | Art. 23(4) |
| 8 | Keep documentation for 10 years | Art. 23(5) |
| 9 | Provide information to authorities upon request | Art. 23(6) |
| 10 | Cooperate with authorities | Art. 23(7) |

---

## Art. 24 — Distributor Obligations (Händler)

**Who:** Entity in the supply chain (not provider or importer) making AI system available.

**Before making available:**

| # | Obligation | Article |
|---|-----------|---------|
| 1 | Verify CE marking present | Art. 24(1) |
| 2 | Verify provider identified | Art. 24(1) |
| 3 | Verify importer identified (if applicable) | Art. 24(1) |
| 4 | Verify EU declaration of conformity exists | Art. 24(1) |

**Ongoing obligations:**

| # | Obligation | Article |
|---|-----------|---------|
| 5 | Not make available if non-compliance known/suspected | Art. 24(2) |
| 6 | Inform provider/importer if non-compliance suspected | Art. 24(3) |
| 7 | Ensure storage/transport does not compromise compliance | Art. 24(4) |
| 8 | Cooperate with authorities | Art. 24(5) |

---

## Art. 25 — Quasi-Provider Obligations

**Who:** Any distributor, importer, deployer, or third party that triggers one of the Art. 25(1) scenarios.

### Art. 25(1) — Becomes Provider When:

| Scenario | Trigger | Effect |
|----------|---------|--------|
| (a) | Put own name/brand on high-risk system | Full provider obligations (Art. 16) |
| (b) | Made substantial modification to high-risk system | Full provider obligations (Art. 16) |
| (c) | Changed intended purpose making system high-risk | Full provider obligations (Art. 16) |

### Art. 25(2) — Original Provider Support Duty

> Where the circumstances referred to in paragraph 1 occur, the provider that initially placed the AI system on the market or put it into service shall no longer be considered to be the provider of that specific AI system for the purposes of this Regulation. That initial provider shall, **without undue delay**, upon request of the new provider, and to the extent technically feasible:

> (a) provide the relevant technical documentation;
> (b) provide information and documentation necessary for the conformity assessment of the AI system;
> (c) provide any other information that is relevant for the new provider to comply with this Regulation.

**Key implications:**
- Original provider **loses** provider status for that specific system
- Original provider **must cooperate** with new provider
- Cooperation must be "without undue delay"
- Limited by "technically feasible" — cannot be required to share trade secrets beyond what's needed
- This creates a **handover obligation**, not merely a courtesy

### Art. 25(3) — Product Manufacturers

| Scenario | Trigger | Effect |
|----------|---------|--------|
| (a) | Manufacturer places high-risk AI system on market with own product under own name | Provider obligations apply to manufacturer |
| (b) | Manufacturer puts high-risk AI system into service under own name after market placement | Provider obligations apply to manufacturer |

### Art. 25(4) — Foreseen Modifications Exception

If the modification was:
1. **Foreseen** by the original provider, AND
2. **Covered** in the initial conformity assessment

→ Art. 25(1)(b) does NOT apply → no quasi-provider status from modification.

**Practical guidance:** Providers should document foreseeable modifications in their conformity assessment and operating instructions to protect deployers from inadvertent quasi-provider status.

---

## Value Chain Responsibility Matrix

### High-Risk AI System Value Chain

```
PROVIDER (Art. 3(3))
│ Develops system + conformity assessment + CE marking
│ Art. 16-17 obligations (full set)
│
├─→ AUTHORIZED REPRESENTATIVE (Art. 3(5))
│   Acts on behalf of non-EU provider
│   Art. 22 obligations
│
├─→ IMPORTER (Art. 3(6))
│   Brings to EU market from third country
│   Art. 23 obligations (verification + documentation)
│
├─→ DISTRIBUTOR (Art. 3(7))
│   Makes available on EU market
│   Art. 24 obligations (verification + non-supply if non-compliant)
│
└─→ DEPLOYER (Art. 3(4))
    Uses under own authority
    Art. 26 obligations (use, monitor, report)
    │
    └─→ IF MODIFICATION/REBRANDING/PURPOSE CHANGE
        → Art. 25 quasi-provider → Art. 16 provider obligations
```

### Responsibility by Obligation Type

| Obligation Type | Provider | Deployer | Importer | Distributor |
|----------------|----------|----------|----------|-------------|
| Conformity assessment | PRIMARY | — | Verify | Verify |
| Technical documentation | Create | — | Maintain | — |
| CE marking | Apply | — | Verify | Verify |
| Risk management system | Create + maintain | Support + input | — | — |
| Human oversight | Design mechanisms | Implement + operate | — | — |
| Data governance | Implement | Input data relevance | — | — |
| Monitoring | Design capability | Active monitoring | — | — |
| Logging | Design capability | Retain logs (6 months) | — | — |
| Incident reporting | To authority + deployer | To provider + authority | Inform provider | Inform provider |
| Registration (EU DB) | Register | Register use | — | — |
| Cooperation with authorities | YES | YES | YES | YES |
| Post-market monitoring | Implement system | Contribute data | Report issues | Report issues |

---

## Cooperation and Information Flow

### Provider → Deployer (Art. 13)

Provider must provide to deployer:
- Instructions for use (Art. 13)
- Information about capabilities and limitations
- Performance metrics (accuracy, robustness)
- Known risks and mitigation measures
- Human oversight requirements and guidance
- Intended purpose documentation
- Technical specifications relevant to deployment

### Deployer → Provider (Art. 26(5), Art. 72)

Deployer must inform provider about:
- Serious incidents (without undue delay)
- Malfunctions that could constitute serious incidents
- Risks identified during use
- Post-market monitoring data

### Art. 25(2) Handover (Quasi-Provider Situation)

Original provider must provide to new provider:
- Technical documentation (full set per Art. 11)
- Conformity assessment documentation
- Any information needed for the new provider to fulfill obligations

---

## Penalties by Actor

| Actor | Max Penalty (Art. 99) |
|-------|----------------------|
| Provider (non-compliance with high-risk requirements) | EUR 15,000,000 or 3% of global turnover |
| Provider (prohibited practice) | EUR 35,000,000 or 7% of global turnover |
| Deployer (non-compliance with Art. 26) | EUR 15,000,000 or 3% of global turnover |
| Importer (non-compliance with Art. 23) | EUR 15,000,000 or 3% of global turnover |
| Distributor (non-compliance with Art. 24) | EUR 15,000,000 or 3% of global turnover |
| SME/startup | Proportionality applies — lower thresholds |
| Incorrect/misleading information to authorities | EUR 7,500,000 or 1% of global turnover |
