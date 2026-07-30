# Substantial Modification — Art. 3(23), Art. 25(1)(b)

## Legal Definition — Art. 3(23)

> 'substantial modification' means a modification to an AI system after its placing on the market or putting into service that is not foreseen or planned in the initial conformity assessment carried out by the provider and as a result of which the compliance of the AI system with the requirements set out in Chapter III, Section 2 is affected or the intended purpose for which the AI system has been approved is modified.

*German: 'wesentliche Veränderung' bezeichnet eine Veränderung eines KI-Systems nach dessen Inverkehrbringen oder Inbetriebnahme, die vom Anbieter in der ursprünglichen Konformitätsbewertung nicht vorgesehen oder geplant wurde und durch die die Konformität des KI-Systems mit den Anforderungen des Kapitels III Abschnitt 2 beeinträchtigt wird oder die Zweckbestimmung, für die das KI-System zugelassen wurde, geändert wird.*

**Recital:** 128

---

## Three-Step Determination Checklist

### Step 1: Identify the Change

**Questions to determine what was changed:**

| # | Question | Details |
|---|----------|---------|
| 1 | What technical elements were modified? | Model weights, architecture, training data, preprocessing, post-processing, thresholds, decision boundaries |
| 2 | Was the model retrained with new data? | Additional training data, different data sources, expanded data categories |
| 3 | Were any software components changed? | Libraries, frameworks, inference engines, integration layers |
| 4 | Was the deployment environment changed? | Hardware, operating system, cloud platform, edge deployment |
| 5 | Were input or output interfaces modified? | New data inputs, different output formats, changed API contracts |
| 6 | Was the intended purpose or use context changed? | Different user group, different application, different sector |

### Step 2: Assess Foreseeability

**Questions to determine if the change was foreseen:**

| # | Question | Impact |
|---|----------|--------|
| 1 | Is the modification described in the provider's technical documentation? | If YES → likely foreseen |
| 2 | Is the modification covered in the original conformity assessment? | If YES → Art. 25(4) exception applies |
| 3 | Do the provider's operating instructions permit this modification? | If YES → likely foreseen |
| 4 | Did the provider specify parameters or boundaries for permissible changes? | If modification is within → likely foreseen |
| 5 | Is the modification a standard configuration change using provider tools? | If YES → likely foreseen, not substantial |

**Key principle:** If the modification was foreseen AND covered by the conformity assessment → Art. 25(4) exception → NOT a substantial modification under Art. 25(1)(b).

### Step 3: Evaluate Risk Impact

**Questions to determine if compliance requirements are affected:**

| # | Requirement Area | Question | Article |
|---|-----------------|----------|---------|
| 1 | Risk management | Does the change introduce new risks not covered by the original risk management system? | Art. 9 |
| 2 | Data governance | Does the change involve different data categories, sources, or quality? | Art. 10 |
| 3 | Technical documentation | Does the change require updating technical documentation? | Art. 11 |
| 4 | Record keeping | Does the change affect logging or event recording capabilities? | Art. 12 |
| 5 | Transparency | Does the change affect how users understand the system? | Art. 13 |
| 6 | Human oversight | Does the change affect human oversight mechanisms? | Art. 14 |
| 7 | Accuracy/robustness | Does the change affect accuracy, robustness, or cybersecurity? | Art. 15 |
| 8 | Intended purpose | Does the change modify the intended purpose? | Art. 3(12) |

**Determination:** If ANY requirement area is materially affected AND the change was NOT foreseen → **substantial modification**.

---

## Seven Examples of Modifications

### Example 1: Database/Knowledge Update — NOT Substantial

| Aspect | Detail |
|--------|--------|
| Modification | Updating reference database, adding new entries to lookup tables |
| Category | Data update within intended scope |
| Foreseen? | Typically foreseen by provider |
| Risk impact | None — system operates identically with updated data |
| **Conclusion** | **NOT substantial modification** |

### Example 2: Parameter Tuning Within Range — NOT Substantial

| Aspect | Detail |
|--------|--------|
| Modification | Adjusting confidence thresholds, sensitivity settings within provider-defined range |
| Category | Configuration |
| Foreseen? | Explicitly permitted in operating instructions |
| Risk impact | None — within documented operational envelope |
| **Conclusion** | **NOT substantial modification** |

### Example 3: PEFT/LoRA Adapter Training — Likely NOT Substantial

| Aspect | Detail |
|--------|--------|
| Modification | Training a LoRA adapter with domain-specific data; base weights unchanged |
| Category | Lightweight finetuning |
| Foreseen? | Depends on provider documentation |
| Risk impact | Low — base model unchanged, adapter adds targeted capability |
| **Conclusion** | **Likely NOT substantial**, but assess: (a) does adapter change output behavior materially? (b) does domain data introduce new risk categories? |

### Example 4: Layer-Wise Finetuning — POTENTIALLY Substantial

| Aspect | Detail |
|--------|--------|
| Modification | Retraining specific layers of the model with new data |
| Category | Moderate finetuning |
| Foreseen? | Unlikely unless explicitly permitted |
| Risk impact | Medium — may change model behavior, accuracy, bias profile |
| **Conclusion** | **Potentially substantial** — requires detailed assessment of which layers, how much data, and whether Art. 9-15 requirements are affected |

### Example 5: Full Model Retraining — Likely Substantial

| Aspect | Detail |
|--------|--------|
| Modification | Complete retraining of model with new/expanded dataset |
| Category | Full retraining |
| Foreseen? | Very unlikely to be foreseen |
| Risk impact | High — fundamentally changes model behavior, accuracy, bias |
| **Conclusion** | **Likely substantial modification** — triggers Art. 25(1)(b) |

### Example 6: Change of Deployment Context — Potentially Substantial

| Aspect | Detail |
|--------|--------|
| Modification | Using system in different sector/context than provider intended (but same technical function) |
| Category | Context change |
| Foreseen? | Not foreseen if outside provider's intended purpose |
| Risk impact | May bring system under different Annex III category |
| **Conclusion** | **Potentially substantial** — may also trigger Art. 25(1)(c) if intended purpose changes |

### Example 7: Architecture Modification — Substantial

| Aspect | Detail |
|--------|--------|
| Modification | Changing model architecture (adding layers, changing attention mechanism, modifying embeddings) |
| Category | Architectural change |
| Foreseen? | Not foreseen |
| Risk impact | High — fundamentally alters system capabilities and behavior |
| **Conclusion** | **Substantial modification** — triggers Art. 25(1)(b) |

---

## Decision Matrix

```
SUBSTANTIAL MODIFICATION ASSESSMENT

Change identified: [description]

Step 1: Nature of change
☐ Data/reference update within scope
☐ Configuration within documented range
☐ PEFT/adapter (base model unchanged)
☐ Layer-wise finetuning
☐ Full retraining
☐ Architecture modification
☐ Deployment context change
☐ Purpose change

Step 2: Foreseeability
☐ Described in provider documentation
☐ Covered by conformity assessment
☐ Permitted in operating instructions
☐ Within specified parameter range
☐ NOT foreseen in any documentation

Step 3: Compliance impact
☐ Risk management affected (Art. 9)
☐ Data governance affected (Art. 10)
☐ Technical documentation affected (Art. 11)
☐ Logging affected (Art. 12)
☐ Transparency affected (Art. 13)
☐ Human oversight affected (Art. 14)
☐ Accuracy/robustness affected (Art. 15)
☐ Intended purpose modified

DETERMINATION:
☐ NOT a substantial modification → Continue as deployer
☐ POTENTIALLY substantial → Seek detailed legal analysis
☐ SUBSTANTIAL MODIFICATION → Art. 25(1)(b) triggers quasi-provider status
```

---

## Key Principles from Recital 128

1. **Purpose-centric:** The definition of "intended purpose" is anchored in the provider's documentation (Art. 3(12))
2. **Foreseeability test:** If the provider explicitly contemplated the modification, it is not "substantial"
3. **Risk-based assessment:** The significance of the modification is measured by its impact on compliance requirements
4. **Continuous learning distinction:** AI systems designed for continuous post-deployment learning should account for expected evolution in the conformity assessment — expected learning is not a "modification"
5. **Practical threshold:** Minor adjustments, bug fixes, and routine maintenance are not substantial modifications
