# Output Templates — Mini-Report, Checklist & Compliance Block — Reference

The Phase 6 deliverables. **Lead with the light §0 blocks below**; produce the heavy artifacts — (a) the
mini-report, (b) the checklist, (c) the portable compliance block — only in **Full** mode or on request.
Fill every bracket; delete rows that are N/A; never leave a determination without a basis. Tag material
statements with an **uncertainty marker** — *[Settled law] / [Draft guidance] / [Best practice] / [Open issue]*.

---

## (0) Lead with this — Bottom line, Readiness, Facts, Source status

Show these four short blocks **first**, as a conversational answer, before any formal artifact. In **Quick
triage** mode these are the *entire* output (then offer to escalate to Full).

```markdown
### Bottom line
- **Role:** [provider / deployer / both]
- **Duties triggered:** [50(1), 50(2), …] — or "none"
- **Earliest deadline:** [date] [uncertainty marker]
- **Biggest gap:** [one line]
- **Load-bearing uncertainty:** [e.g. "2 Dec 2026 grace is [Open issue] until OJ publication"]

### Readiness (operational indicator — NOT legal advice)
- **Readiness:** [Low / Medium / High]
- **Critical blockers:** [N]
- **Must-fix before earliest deadline:** [N]
- **Counsel review needed:** [yes / no] — [why]

### Facts I'm relying on  (correct me before I go further)
- Generates content: [yes/no — modalities]
- Interacts with people: [yes/no — how]
- Role: [provider / deployer / both]
- EU market-placement date: [date] → [new system / legacy]
- [any assumption I had to make]

Source status (checked [date]): Regulation [Settled law] · Art. 50 Guidelines [Draft guidance, 8 May 2026] ·
Code of Practice [final 10 Jun 2026, Best practice; adequacy assessment pending] · Digital Omnibus 2 Dec 2026
grace [adopted 29 Jun 2026, awaiting OJ] · EU icons [published].
```

> **Readiness is an operational triage heuristic, not a legal conclusion.** It flags where work and counsel
> are needed; it does not certify compliance. Keep the disclaimer attached.

---

## (a) Art. 50 Transparency Mini-Report

Emulates the `ai-act-report` Prüfbericht structure, scoped to Art. 50. Output as a fenced markdown block.

```markdown
# EU AI Act — Article 50 Transparency Assessment
## [System Name] — [Date]

---

**Report Reference:** [ref]
**Prepared by:** [name, role]
**Organisation:** [organisation]
**Date:** [date]
**Status:** [Draft / Final]

---

### 1. Subject & Scope
- **System:** [name + one-line description]
- **Modalities generated:** [audio / image / video / text / none]
- **Interaction surface:** [interacts directly with natural persons? yes/no — how]
- **Market-placement date:** [date or planned] — *(drives the 50(2) grace logic)*
- **Scope of this assessment:** Article 50 transparency duties only. Risk-tier classification, role
  determination depth, and the full obligation set are addressed by the related suite skills (§9).

### 2. Role Determination
[Provider / Deployer / Both] — [basis]. 50(1)+(2) bind the provider; 50(3)+(4) bind the deployer.

### 3. Trigger Analysis

| Duty | Binds | Applicable? | Trigger basis | Obviousness / Exception verdict |
|------|-------|-------------|---------------|---------------------------------|
| 50(1) interaction disclosure | Provider | [Yes/No] | [direct interaction with persons] | [Required / Exempt-obvious — basis] |
| 50(2) synthetic-content marking | Provider | [Yes/No] | [generates which modalities] | [Required / Assistive-exception] |
| 50(3) emotion/biometric notice | Deployer | [Yes/No] | [emotion recog / biometric categ] | [Required / Art. 5-prohibited / N/A] |
| 50(4) deepfake / PI-text labelling | Deployer | [Yes/No] | [deepfake per Art. 3(60) / PI text] | [Required / Exception: <which>] |
| 50(5) delivery quality | [owner] | [Yes/No] | [applies to <list>] | [clear/distinguishable/timely/accessible] |

### 4. Implementation Requirements (per triggered duty)
[For 50(2): layered marking — signed+timestamped metadata + imperceptible watermark; four criteria; no
single technique suffices. For 50(4): EU icon set + modality placement + WCAG contrast. For 50(1)/50(3):
notice content, placement, timing. Reference the relevant implementation file.]

### 5. Exceptions Claimed & Justification (Art. 50(6))
[Each exception relied on + documented reasoning. "None claimed" if so.]

### 6. Dated Roadmap
- **22 Jul 2026** — Code initial-signatory form deadline (if signing; later signing possible).
- **2 Aug 2026** — 50(1)/(3)/(4) + 50(2) for newly-placed systems (no transition).
- **2 Dec 2026** — legacy 50(2) marking — Digital Omnibus grace **[Open issue → adopted, awaiting OJ]**
  (EP + Council 29 Jun 2026; in force 3rd day after OJ). Until published, 2 Aug 2026 formally governs legacy
  systems; verify the OJ status.
- **2 Feb 2027** — Code watermark-detection interoperability obligation.

### 7. Gaps & Recommendations
| # | Gap | Required action | Priority | Owner |
|---|-----|-----------------|----------|-------|
| 1 | [gap] | [action] | [High/Med/Low] | [role] |

**Penalty exposure:** non-compliance with Art. 50 → Tier 2, up to **EUR 15,000,000 or 3% of worldwide
annual turnover** (Art. 99(4)). *(Not the €35M/7% Art. 5 band.)*

### 8. Conclusion
[Summary: which duties apply, readiness, earliest binding deadline, top actions.]

---

[ART. 50 TRANSPARENCY COMPLIANCE BLOCK — see (c)]

**Disclaimer:** Structured guidance on Art. 50 transparency under Regulation (EU) 2024/1689, the final
Code of Practice on Transparency of AI-Generated Content (10 Jun 2026), and the Commission's draft Art. 50
Guidelines (8 May 2026). Not legal advice; the Code is voluntary and adherence is not conclusive evidence
of compliance; only the CJEU can authoritatively interpret Art. 50. The Digital Omnibus grace period is
adopted (Council 29 Jun 2026) and awaiting OJ publication. Reassess as the Guidelines are finalised, the
Omnibus text is published, and the Code's adequacy assessment concludes.
```

> **Optional .docx export:** do not re-implement Word generation. If the user wants a formatted document,
> hand the report to the `ai-act-report` skill (its Phase 4 Word export) — a cross-reference, not a copy.

---

## (b) Per-Obligation Compliance Checklist

Emulates the obligations-matrix style. Output as a fenced block.

```markdown
## Art. 50 Compliance Checklist — [System] — [Date]

| # | Duty | Binds | Triggered | Required action | Status | Gap flag | Deadline |
|---|------|-------|-----------|-----------------|--------|----------|----------|
| 1 | 50(1) interaction disclosure | Provider | [Yes/No] | Proactive AI disclosure at first interaction | [✓/◐/✗] | [gap note] | 2 Aug 2026 |
| 2 | 50(2) metadata marking (Code route) | Provider | [Yes/No] | Signed + timestamped manifest (C2PA de-facto) | [✓/◐/✗] | [gap note] | 2 Aug 2026 (legacy: 2 Dec 2026*) |
| 3 | 50(2) watermark layer | Provider | [Yes/No] | Imperceptible robust watermark; **text > 200 tokens must be watermarked** | [✓/◐/✗] | [gap note] | 2 Aug 2026 |
| 4 | 50(2) detection mechanism | Provider | [Yes/No] | Detection **free of charge**, per technique; interop by 2 Feb 2027 | [✓/◐/✗] | [gap note] | 2 Feb 2027 (interop) |
| 5 | 50(3) emotion/biometric notice | Deployer | [Yes/No] | Notice to exposed persons + GDPR 13/14 | [✓/◐/✗] | [gap note] | 2 Aug 2026 |
| 6 | 50(4) deepfake label | Deployer | [Yes/No] | EU icon + modality placement | [✓/◐/✗] | [gap note] | 2 Aug 2026 |
| 7 | 50(5) delivery quality | [owner] | [Yes/No] | Clear/distinguishable/timely/accessible | [✓/◐/✗] | [gap note] | (with the above) |

Gap-flag legend: ✓ in place · ◐ partial · ✗ GAP · N/A not triggered
SUMMARY: [X] duties triggered · [Y] GAPs · earliest deadline [date]
*2 Dec 2026 legacy-marking grace is ADOPTED (Council 29 Jun 2026), awaiting OJ publication; until published, 2 Aug 2026 formally governs legacy systems.
```

---

## (c) Portable Compliance Block

Plain text, vocabulary-aligned with the classifier's `ASSESSMENT CONTEXT` block so it round-trips.

```
ART. 50 TRANSPARENCY COMPLIANCE BLOCK (paste into next skill)
System: [name]
Role(s): [provider / deployer / both]
50(1) interaction disclosure: [Required / Exempt-obvious / N/A] — [basis]
50(2) synthetic-content marking: [Required / Assistive-exception / N/A] — [grace status]
50(3) emotion/biometric notice: [Required / Art.5-prohibited / N/A]
50(4) deepfake/PI-text labelling: [Required / Exception:<which> / N/A]
50(5) delivery quality: [applies to <list> / N/A]
Any 50 trigger active: [true / false]
Earliest deadline: [date] (50(2) legacy grace 2 Dec 2026 — adopted 29 Jun 2026, awaiting OJ)
Code of Practice signatory intent: [yes / no / undecided]
Source: ai-act-transparency v<X.Y>
```

> **Interchange note:** this skill emits the plain-text block above. It does **not** emit RoPA's
> `interchange-schema.json` (that is RoPA's contract). The `Any 50 trigger active: true/false` boolean
> maps conceptually onto RoPA's existing `art50_transparency` activity field, but populating that field
> is RoPA's inbound-adapter job — no RoPA-shaped JSON leaves this skill.
