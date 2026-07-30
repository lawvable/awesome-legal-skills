# Finetuning Assessment — AI Act Substantial Modification Analysis

## Overview

Finetuning is a spectrum of techniques with varying implications for Art. 25(1)(b) quasi-provider status. This reference provides a graduated risk assessment framework.

---

## Finetuning Categories

### Level 1: Parameter-Efficient Fine-Tuning (PEFT) — LOW Risk

**Techniques:** LoRA, QLoRA, prefix tuning, prompt tuning, adapter layers

**Technical description:**
- Base model weights remain frozen
- Small trainable adapter modules added alongside frozen layers
- Typically modifies < 1% of total parameters
- Original model can be recovered by removing adapter

**Risk assessment factors:**

| Factor | Assessment | Impact |
|--------|-----------|--------|
| Base model integrity | Preserved — weights unchanged | LOW |
| Reversibility | High — adapter can be removed | LOW |
| Behavioral change scope | Targeted — specific task/domain adaptation | LOW |
| Data governance impact | Limited — adapter training data is narrowly scoped | LOW |
| Accuracy/bias impact | Moderate — adapter can introduce domain-specific biases | MEDIUM |
| Provider foreseeability | Often foreseen — many providers design for PEFT | LOW |

**Typical conclusion:** PEFT/LoRA finetuning is **unlikely** to constitute a substantial modification, particularly when:
- The provider's documentation anticipates adapter-based customization
- The training data is within the system's intended domain
- The adapter does not fundamentally change output categories or decision boundaries

**Potential triggers for re-assessment:**
- Adapter trained on data from a different domain than intended
- Adapter significantly changes decision boundaries for sensitive categories
- Adapter trained on data that introduces protected characteristic biases

---

### Level 2: Layer-Wise Finetuning — MEDIUM Risk

**Techniques:** Unfreezing and retraining specific model layers (typically top/final layers), transfer learning with partial weight updates

**Technical description:**
- Selected layers are unfrozen and retrained with new data
- Lower layers (feature extraction) typically remain frozen
- Upper layers (task-specific) are modified
- Modifies 5-50% of total parameters depending on layers selected

**Risk assessment factors:**

| Factor | Assessment | Impact |
|--------|-----------|--------|
| Base model integrity | Partially compromised — retrained layers diverge | MEDIUM |
| Reversibility | Moderate — requires original weights backup | MEDIUM |
| Behavioral change scope | Significant — retrained layers change model behavior | MEDIUM |
| Data governance impact | Significant — new training data governance required | MEDIUM |
| Accuracy/bias impact | High — weight changes can shift accuracy and bias profile | HIGH |
| Provider foreseeability | Often NOT foreseen unless explicitly documented | MEDIUM-HIGH |

**Typical conclusion:** Layer-wise finetuning **may** constitute a substantial modification, requiring case-by-case analysis:

**Assessment checklist:**
1. How many layers were retrained? (More layers = higher risk)
2. Were output/decision layers modified? (YES = higher risk)
3. Was new training data from a different domain? (YES = higher risk)
4. Did the finetuning change accuracy metrics significantly? (YES = higher risk)
5. Did the provider explicitly permit this level of modification? (NO = higher risk)
6. Were Art. 9-15 compliance requirements affected? (YES = substantial modification)

---

### Level 3: Full Model Retraining — HIGH Risk

**Techniques:** Complete weight initialization/retraining, training from scratch with new data, major architectural modifications combined with retraining

**Technical description:**
- All or substantially all model weights are retrained
- Training data may be entirely different from original
- Model behavior may diverge significantly from original
- Effectively creates a new model variant

**Risk assessment factors:**

| Factor | Assessment | Impact |
|--------|-----------|--------|
| Base model integrity | Lost — new weights throughout | HIGH |
| Reversibility | None — original model replaced | HIGH |
| Behavioral change scope | Comprehensive — entire model behavior changes | HIGH |
| Data governance impact | Full — entirely new data governance required | HIGH |
| Accuracy/bias impact | Complete — all accuracy/bias characteristics changed | HIGH |
| Provider foreseeability | Almost never foreseen | HIGH |

**Typical conclusion:** Full model retraining is **very likely** a substantial modification triggering Art. 25(1)(b), unless the original provider explicitly anticipated and included this in the conformity assessment.

---

## Meta-Level Assessment Factors

Beyond the technical level of finetuning, assess these overarching factors:

### Factor 1: Domain Shift

| Question | Low Risk | High Risk |
|----------|----------|-----------|
| Is the finetuning data from the same domain as original training? | Same domain | Different domain |
| Does finetuning change the application context? | Same context | Different context |
| Does finetuning change the target population? | Same population | Different population |

### Factor 2: Output Impact

| Question | Low Risk | High Risk |
|----------|----------|-----------|
| Do outputs change in nature? | Same output types | Different output types |
| Do decision boundaries shift? | Minor adjustments | Significant shifts |
| Are new output categories added? | No | Yes |
| Do accuracy metrics change significantly? | < 5% change | > 5% change |

### Factor 3: Risk Profile

| Question | Low Risk | High Risk |
|----------|----------|-----------|
| Does finetuning affect protected characteristics? | No | Yes |
| Does finetuning change bias profile? | Minimal change | Significant change |
| Does finetuning affect safety-critical outputs? | No | Yes |
| Does finetuning change the set of affected persons? | No | Yes |

### Factor 4: Provider Documentation

| Question | Low Risk | High Risk |
|----------|----------|-----------|
| Does provider explicitly permit this finetuning? | Yes, documented | Not mentioned |
| Is finetuning covered by conformity assessment? | Yes | No |
| Does provider provide finetuning guidelines? | Yes, with parameters | No guidelines |
| Does provider offer finetuning support/validation? | Yes | No |

---

## Graduated Risk Matrix

```
FINETUNING RISK ASSESSMENT

Technique: [PEFT/Layer-wise/Full retraining]

| Factor | Assessment | Risk |
|--------|-----------|------|
| Finetuning level | [PEFT/Layer-wise/Full] | [LOW/MEDIUM/HIGH] |
| Domain shift | [Same/Related/Different] | [LOW/MEDIUM/HIGH] |
| Output impact | [Minimal/Moderate/Significant] | [LOW/MEDIUM/HIGH] |
| Risk profile change | [None/Minor/Major] | [LOW/MEDIUM/HIGH] |
| Provider documentation | [Permitted/Silent/Prohibited] | [LOW/MEDIUM/HIGH] |
| Art. 9-15 compliance impact | [None/Some/Significant] | [LOW/MEDIUM/HIGH] |

Overall risk: [LOW / MEDIUM / HIGH]

Recommendation:
- LOW: Likely NOT substantial modification — continue as deployer
- MEDIUM: POTENTIALLY substantial — seek detailed Art. 25 legal analysis
- HIGH: Likely SUBSTANTIAL modification — assume quasi-provider obligations
```

---

## Practical Guidance

### What deployers should do before finetuning:

1. **Review provider documentation** — check for finetuning permissions and constraints
2. **Document the modification** — record what was changed, why, and how
3. **Assess impact on Art. 9-15** — evaluate effect on each compliance requirement
4. **Evaluate data governance** — ensure finetuning data meets Art. 10 requirements
5. **Test accuracy and bias** — compare pre- and post-finetuning performance
6. **Consult original provider** — leverage Art. 25(2) cooperation duty
7. **Seek legal assessment** — for any Medium or High risk finetuning

### If quasi-provider status is triggered:

1. **Accept provider obligations** — Art. 16, Art. 8-15
2. **Conduct new conformity assessment** — unless covered by Art. 25(4)
3. **Update technical documentation** — including finetuning details
4. **Register in EU database** — as new provider
5. **Engage original provider** — invoke Art. 25(2) support obligation
