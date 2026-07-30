# Report Template — Dokumentierter Pruefbericht

## Template Structure

This template follows the structure of the "Dokumentierter Pruefbericht (Kurzfassung)" from the KI-Compliance Starterpaket, adapted for English-language assessments with German legal term preservation.

---

## Required Sections

### Section 1: Introduction
**Purpose:** Frame the assessment scope, methodology, and limitations.

**Quality criteria:**
- Clear statement of purpose
- Explicit methodology references (AI Act, Commission guidelines, standards)
- Honest statement of limitations
- Date and version control

---

### Section 2: System Description
**Purpose:** Document the AI system being assessed.

**Required content per Starterpaket structure:**

| Sub-section | Content | Source |
|-------------|---------|--------|
| 2.1 General information | Name, version, provider, type | User input |
| 2.2 Technical description | How the system works | Provider documentation + user |
| 2.3 Deployment context | Use case, users, affected persons | User input |
| 2.4 Data flows | Input data, output data, storage | Provider documentation + user |

**From Starterpaket Part 1 (Stammdaten):**
- Service Owner (Fachabteilung)
- Professionally responsible person (Fachlich Verantwortlich)
- Technically responsible person (Technisch Verantwortlich)
- Department/organizational unit

**From Starterpaket Part 2 (KI-Beschaffung):**
- Development path: internally developed / externally contracted / purchased
- Provider information
- Documentation provided by provider

**From Starterpaket Part 3 (Anwendungsszenario):**
- Intended use statement
- Interaction type: none / indirect / direct
- Impact on humans: none / partial / full
- Decision impact: none / low / medium / high / very high
- Integration approach: no adaptation / workflow integration / substantial adaptation

---

### Section 3: Scope Exclusions (Art. 2)
**Purpose:** Systematically check all exclusion categories.

**Quality criteria:**
- Each exclusion category addressed with Yes/No + reasoning
- If exclusion applies: cite specific article and stop analysis
- If open-source: include full Checklist I or II analysis

---

### Section 4: Scope of Application
**Purpose:** Determine AI system status, role, and territorial scope.

**Quality criteria:**
- 7-criteria Art. 3(1) analysis with reasoning per criterion
- Clear determination with confidence level
- Role determination with Art. 25 analysis
- Territorial scope with specific Art. 2(1) basis

---

### Section 5: Intended Purpose (Art. 3(12))
**Purpose:** Document and compare provider's intended purpose with actual use.

**Quality criteria:**
- Quote from provider documentation (Zweckbestimmung per Art. 3 Nr. 12)
- Actual deployment description
- Gap analysis — any deviation triggers Art. 25(1)(c) assessment

---

### Section 6: Risk Classification
**Purpose:** Classify the system through all risk tiers.

**Sub-sections must include:**

**6.1 Art. 5 screening:** Table with all 8 prohibited categories
- Each category assessed individually
- "Possibly" entries require detailed follow-up recommendation

**6.2 High-risk assessment:**
- 6.2.1 Annex I (all 18 product categories)
- 6.2.2 Annex III (all 8 application categories)
- 6.2.3 Art. 6(3) exception (if Annex III triggered)
- 6.2.4 Customer profiling assessment (if applicable)

**6.3 GPAI assessment** (if applicable):
- GPAI model determination
- FLOP threshold check
- Systemic risk indicators

**6.4 Art. 50 transparency obligations:**
- All 4 transparency triggers assessed

---

### Section 7: Applicable Obligations
**Purpose:** Map obligations to role + risk tier.

**Quality criteria:**
- Complete obligation matrix with legal citations
- Priority classification (immediate/short-term/ongoing/periodic)
- RACI assignments
- Status tracking (addressed/partial/not addressed)

---

### Section 8: Risk Flags & Recommendations
**Purpose:** Highlight issues requiring human legal judgment.

**Quality criteria:**
- Honest flagging of uncertainty areas
- Actionable recommendations with priorities
- GDPR cross-references where applicable
- Suggested follow-up skills

---

### Section 9: Conclusion
**Purpose:** Summarize classification and readiness.

**Quality criteria:**
- Clear classification statement
- Compliance readiness assessment
- Top 3 priority actions
- Reassessment recommendation

---

## Report Quality Checklist

Before finalizing the report, verify:

| # | Check | Status |
|---|-------|--------|
| 1 | Every legal determination has article citation | [ ] |
| 2 | Every Yes/No has written reasoning | [ ] |
| 3 | All Art. 5 categories screened | [ ] |
| 4 | All Annex I categories checked (if relevant) | [ ] |
| 5 | All Annex III categories checked | [ ] |
| 6 | Art. 6(3) exception analyzed (if Annex III triggered) | [ ] |
| 7 | Profiling re-exception checked | [ ] |
| 8 | Role determination includes Art. 25 analysis | [ ] |
| 9 | GDPR cross-references identified | [ ] |
| 10 | Uncertainty areas flagged | [ ] |
| 11 | Follow-up actions specified | [ ] |
| 12 | Disclaimer included | [ ] |
| 13 | Date and version included | [ ] |
| 14 | Methodology section cites all sources | [ ] |
| 15 | Web search results incorporated (if any) | [ ] |
