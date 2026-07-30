# Role Determination Case Studies

Five worked examples applying the role determination framework and Art. 25 quasi-provider assessment. Each case study references the methodology in the parent SKILL.md and supporting reference files.

---

## Case Study 1: SaaS Vendor Providing HR Screening Tool (Provider + Deployer)

### Scenario
**TalentAI GmbH** (Berlin) develops an AI-powered CV screening platform and offers it as SaaS to corporate clients. **MegaCorp AG** (Munich) licenses the platform, configures screening criteria for its open positions, and uses it in its HR department. MegaCorp uses TalentAI's interface under TalentAI's branding with a "Powered by TalentAI" label.

### Role Analysis

| Question | TalentAI GmbH | MegaCorp AG |
|---|---|---|
| System Acquisition | Self-developed | Licensed SaaS from vendor |
| Organizational Relationship | Developing for others | Deploying under own authority |
| Market Status | Placing on EU market | Already deployed |
| Modifications Made | N/A (original developer) | Configuration only (screening criteria within provider's intended range) |

### Role Determination

**TalentAI GmbH:**
- Develops AI system + places on market under own name → **Provider (Anbieter)** under Art. 3(3)
- Full Art. 16 provider obligations apply (Chapter III, Section 2)

**MegaCorp AG:**
- Uses AI system under own authority in professional capacity → **Deployer (Betreiber)** under Art. 3(4)
- Art. 26 deployer obligations apply

### Art. 25 Quasi-Provider Assessment (MegaCorp)

| Trigger | Assessment | Result |
|---|---|---|
| Art. 25(1)(a) — Own name/brand? | MegaCorp uses TalentAI's branding ("Powered by TalentAI"), does NOT present under own brand | Not triggered |
| Art. 25(1)(b) — Substantial modification? | Configuration within provider's intended parameters (screening criteria). See [substantial-modification.md](substantial-modification.md) — configuration ≠ modification | Not triggered |
| Art. 25(1)(c) — Changed intended purpose? | Using for CV screening — exactly TalentAI's intended purpose | Not triggered |

**Result:** MegaCorp remains a **deployer**. No quasi-provider status.

### Key Takeaway
Classic SaaS provider-deployer split. The provider builds and maintains the system; the deployer configures and uses it. As long as the deployer stays within the provider's intended configuration range and does not rebrand, quasi-provider status is not triggered.

---

## Case Study 2: Bank Deploying Credit Scoring AI (Pure Deployer)

### Scenario
**EuroBank SA** (Luxembourg) purchases a credit scoring AI system from **ScoreVendor Ltd** (Ireland). The system is deployed as-is, without modifications, under ScoreVendor's brand. EuroBank uses it to assess consumer loan applications. The system generates creditworthiness scores that EuroBank's loan officers review before making lending decisions.

### Role Analysis

| Question | EuroBank SA |
|---|---|
| System Acquisition | Purchased from vendor (off-the-shelf) |
| Organizational Relationship | Deploying under own authority |
| Market Status | Already on market (placed by ScoreVendor) |
| Modifications Made | No modifications — using as provided |

### Role Determination

**EuroBank SA:** Uses AI under own authority → **Deployer (Betreiber)** under Art. 3(4)

### Art. 25 Quasi-Provider Assessment

| Trigger | Assessment | Result |
|---|---|---|
| Art. 25(1)(a) — Own name/brand? | Using ScoreVendor's branding | Not triggered |
| Art. 25(1)(b) — Substantial modification? | No modifications at all | Not triggered |
| Art. 25(1)(c) — Changed intended purpose? | Using for creditworthiness assessment — ScoreVendor's intended purpose | Not triggered |

**Result:** EuroBank is a **pure deployer**.

### Deployer Obligations (High-Risk System)

Despite being "only" a deployer, EuroBank carries significant obligations because the system is high-risk (Annex III Nr. 5(a)):

| Obligation | Article | Note |
|---|---|---|
| Use per operating instructions | Art. 26(1) | Must follow ScoreVendor's documentation |
| Human oversight | Art. 26(2) | Loan officers must be trained as oversight persons |
| Input data relevance | Art. 26(4) | Ensure applicant data is relevant and representative |
| Monitoring | Art. 26(5) | Monitor system operation, report serious incidents |
| Log retention (6 months) | Art. 26(6) | Must retain automatically generated logs |
| Employee information | Art. 26(7) | Inform works council / employee representatives |
| DPIA | Art. 26(9) | Must complete before deployment |
| FRIA | Art. 27 | **Mandatory** for credit scoring deployers |
| Inform affected persons | Art. 26(11) | Must inform loan applicants of AI use |
| Register deployment | Art. 49(3) | Register use in EU database |

### Key Takeaway
"Pure deployer" does not mean "no obligations." For high-risk systems like credit scoring, deployers have 10+ mandatory obligations (the Art. 26 deployer cluster, plus Art. 4 AI literacy and Art. 50 transparency where applicable). The FRIA requirement (Art. 27) is specifically mandatory for deployers in credit scoring (not just public bodies). Map the full set of deployer obligations to the confirmed role and risk tier as the next step.

---

## Case Study 3: Finetuning Open-Source LLM with Own Branding (Quasi-Provider)

### Scenario
**LegalTech Startup** (Amsterdam) downloads Meta's Llama 3 model (open-source, Apache 2.0 license), finetuned it with LoRA adapters on 50,000 Dutch legal documents, and deploys it as "LegalBot NL" — an AI legal research assistant marketed under LegalTech Startup's brand. The system helps lawyers search case law and summarize legal documents.

### Role Analysis

| Question | LegalTech Startup |
|---|---|
| System Acquisition | Downloaded open-source model |
| Organizational Relationship | Developing derivative system for others + deploying |
| Market Status | Placing on EU market for the first time under own brand |
| Modifications Made | Finetuning with own data + Own brand |

### Art. 25 Quasi-Provider Assessment

| Trigger | Assessment | Result |
|---|---|---|
| Art. 25(1)(a) — Own name/brand? | **YES** — "LegalBot NL" marketed under LegalTech Startup's brand. Users associate the product with LegalTech Startup, not Meta | **TRIGGERED** |
| Art. 25(1)(b) — Substantial modification? | LoRA finetuning = < 1% parameter modification. Per [finetuning-assessment.md](finetuning-assessment.md), PEFT/LoRA is LOW risk for substantial modification. However, domain shift (general → legal) could elevate risk | Likely not triggered (but monitor) |
| Art. 25(1)(c) — Changed intended purpose? | Meta's Llama 3 intended purpose: general-purpose text generation. LegalTech's use: legal research and case law analysis. If this is considered Annex III Nr. 8(a) (administration of justice / legal research), and the original model was not classified as high-risk, purpose change could trigger | Potentially triggered |

**Result:** LegalTech Startup is a **quasi-provider** under Art. 25(1)(a) (own branding) — **at minimum**. This alone is sufficient to trigger full provider obligations.

### Classification Analysis

Before determining full obligations, assess risk classification of "LegalBot NL":
- Annex III Nr. 8(a): AI for administration of justice — includes legal research assistance
- If used by lawyers for case research only (preparatory task) → Art. 6(3)(d) exception possible
- If system influences legal analysis or recommendations → exception may not apply
- Profiling check: legal document analysis typically does not profile natural persons → exception not blocked by profiling

**Most likely classification:** Context-dependent. If purely preparatory (case law search), potentially not high-risk with Art. 6(3)(d). If generating legal analysis that influences decisions, likely high-risk.

### Key Takeaway
Open-source model + own branding = quasi-provider. Art. 25(1)(a) is the most common trap for companies building on open-source AI. Even a minor LoRA finetune combined with own branding triggers full provider obligations. The finetuning level is secondary — the branding alone is decisive. See also [quasi-provider-scenarios.md](quasi-provider-scenarios.md) Scenario 1.

---

## Case Study 4: Research Institute Deploying Open-Source Without Branding (Open-Source Analysis)

### Scenario
**TU Delft** (Netherlands) downloads Mistral 7B (open-source model), deploys it on university servers without modification, and makes it available to researchers for internal text analysis tasks. The system is not branded by TU Delft — it is presented as "Mistral 7B" to users. It is not placed on the EU market — it is used internally only.

### Role Analysis

| Question | TU Delft |
|---|---|
| System Acquisition | Downloaded open-source model |
| Organizational Relationship | Deploying under own authority (internal use) |
| Market Status | Not placed on market — internal deployment only |
| Modifications Made | No modifications — using as provided |

### Open-Source Exemption Analysis (Art. 2(12))

Before role determination, check if the open-source exemption applies to TU Delft's deployment:

| Step | Question | Answer |
|---|---|---|
| Step 1 | Is it an AI system (Art. 3(1))? | Yes — LLM with inference, autonomy, output generation |
| Step 2a | Is it high-risk (Art. 6)? | No — internal research text analysis, no Annex I/III trigger |
| Step 2b | Is it prohibited (Art. 5)? | No |
| Step 2c | Does it trigger Art. 50? | Potentially — if researchers interact with it conversationally (Art. 50(1)) |

If Art. 50 is triggered → open-source exemption under Art. 2(12) does NOT fully apply. Art. 50 obligations remain.

### Role Determination

**TU Delft:** Uses system under own authority in professional context → **Deployer (Betreiber)** under Art. 3(4)

### Art. 25 Quasi-Provider Assessment

| Trigger | Assessment | Result |
|---|---|---|
| Art. 25(1)(a) — Own name/brand? | No — presented as "Mistral 7B" | Not triggered |
| Art. 25(1)(b) — Substantial modification? | No modifications | Not triggered |
| Art. 25(1)(c) — Changed intended purpose? | General text analysis — within Mistral's general purpose | Not triggered |

**Result:** TU Delft is a **deployer** only. No quasi-provider status.

### Applicable Obligations

| Obligation | Applies? | Reasoning |
|---|---|---|
| Art. 4 AI competence | Yes | Always applies — train researchers on AI literacy |
| Art. 50(1) interaction disclosure | Likely yes | If researchers interact conversationally, must disclose AI nature |
| High-risk obligations | No | No Annex I/III trigger for internal research text analysis |
| Art. 26 deployer obligations | No | Only for high-risk systems |

### Key Takeaway
Internal deployment of an unmodified open-source model without rebranding keeps the deployer in a lightweight compliance position. The key factors: (1) no branding, (2) no modification, (3) no purpose change to high-risk, (4) no market placement. Art. 4 (AI competence) and Art. 50(1) (if conversational) are the main obligations.

---

## Case Study 5: System Integrator Reselling Fraud Detection (Quasi-Provider Trap)

### Scenario
**SecureTech Solutions** (Frankfurt) purchases a fraud detection AI system from **FraudGuard Inc.** (US provider). SecureTech (1) rebrands the system as "SecureTech FraudShield," (2) retrains the model on European transaction data (full model retraining), (3) integrates it into its own cybersecurity product suite, and (4) sells the integrated product to EU banks under the "SecureTech" brand.

### Role Analysis

| Question | SecureTech Solutions |
|---|---|
| System Acquisition | Purchased from non-EU vendor |
| Organizational Relationship | Distributing + Integrating into own product + Developing derivative |
| Market Status | Placing on EU market under own brand |
| Modifications Made | Own brand + Substantial technical modification + Finetuning/retraining |

### Art. 25 Quasi-Provider Assessment

| Trigger | Assessment | Result |
|---|---|---|
| Art. 25(1)(a) — Own name/brand? | **YES** — "SecureTech FraudShield" under SecureTech brand. Original FraudGuard branding removed | **TRIGGERED** |
| Art. 25(1)(b) — Substantial modification? | **YES** — Full model retraining with new dataset. Per [finetuning-assessment.md](finetuning-assessment.md), full retraining = HIGH risk of substantial modification. All parameters modified with new European data | **TRIGGERED** |
| Art. 25(3)(a) — Product manufacturer? | **YES** — SecureTech integrates AI into its own cybersecurity product suite, sold under own name | **TRIGGERED** |

**Result:** SecureTech triggers **three** quasi-provider provisions simultaneously. It is unambiguously treated as a **provider** (Anbieter) under Art. 25.

### Classification Analysis

Fraud detection for banks — is it high-risk?
- Annex III Nr. 5(a): Creditworthiness assessment → fraud detection is NOT creditworthiness assessment
- If fraud detection score causes denial of services to individuals → may implicate Nr. 5(a) indirectly
- Generally, fraud detection analyzing transaction patterns (not individual creditworthiness) is not Annex III high-risk

**Most likely classification:** Fraud detection alone is NOT high-risk under Annex III. However, if the system's output affects individual access to financial services (e.g., freezing accounts, blocking transactions for specific persons), an Annex III Nr. 5(a) argument could emerge.

### Obligations Regardless of Risk Tier

Even if the system is not high-risk, SecureTech as provider must:

| Obligation | Basis | Reasoning |
|---|---|---|
| Art. 4 AI competence | Universal | Always applies |
| Art. 50(1) if applicable | If system interacts with persons | Depends on deployment |
| Full Art. 16 provider obligations | If high-risk | Only if classified as high-risk |
| Original provider support | Art. 25(2) | FraudGuard must provide technical docs and cooperate |

### Key Takeaway
This case illustrates the "quasi-provider trap" at its most severe — three independent Art. 25 triggers firing simultaneously. System integrators who rebrand, retrain, and repackage third-party AI systems must assume provider status. The combination of Art. 25(1)(a), (1)(b), and Art. 25(3)(a) leaves no room for argument. Critically, Art. 25(2) requires the original provider (FraudGuard) to cooperate — but SecureTech bears full provider responsibility regardless.

---

## Summary Comparison

| Case | Entity | Primary Role | Quasi-Provider? | Risk Tier | Key Factor |
|---|---|---|---|---|---|
| 1 — SaaS HR | MegaCorp (deployer) | Deployer | No | High-risk (Annex III Nr. 4a) | Configuration ≠ modification |
| 2 — Bank Credit | EuroBank | Deployer | No | High-risk (Annex III Nr. 5a) | Pure deployer, heavy obligations |
| 3 — LLM Finetune | LegalTech Startup | Quasi-provider | **Yes** — Art. 25(1)(a) | Context-dependent | Own branding is decisive |
| 4 — Research Deploy | TU Delft | Deployer | No | Minimal/Limited | No branding, no modification |
| 5 — Integrator | SecureTech | Quasi-provider | **Yes** — Art. 25(1)(a)(b), 25(3)(a) | Likely not high-risk | Triple trigger trap |
