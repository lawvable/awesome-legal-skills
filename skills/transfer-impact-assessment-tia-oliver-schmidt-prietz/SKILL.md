---
name: "transfer-impact-assessment-tia-oliver-schmidt-prietz"
description: "GDPR Transfer Impact Assessment for Chapter V transfers under the EDPB Recommendations 01/2020 six-step methodology, the CNIL TIA Guide (January 2025), and EDPB essential guarantees. Handles transfer qualification, Art. 45 adequacy fast-tracks, Art. 46 full assessments with country profiles for 12 jurisdictions, and balanced Art. 49 derogation analysis. Outputs a Markdown report, a .docx formal TIA, and a JSON delta for RoPA interchange."
metadata:
  author: "Oliver Schmidt-Prietz"
  license: "agpl-3.0"
  version: "2026-06-09"
---

# GDPR Transfer Impact Assessment (TIA) Skill

## Disclaimer (show at session start, do not block)

> **Important:** This skill provides structured GDPR Chapter V transfer assessment guidance based on EDPB Recommendations, CNIL guidance, CJEU case law, and emerging national case law (OLG München 21 U 3882/25 e). It is not legal advice. Involve your DPO and qualified counsel for final decisions, especially where the skill flags a transfer for suspension or restructuring.

## Routing

Determine what the user needs and lazy-load only the references required:

| User Need | Load These References | Action |
|---|---|---|
| Single transfer assessment | `references/edpb-six-steps.md` + relevant country profile + `references/supplementary-measures.md` | Run the 6-step pipeline for one transfer |
| Batch assessment (multiple transfers) | + `references/tia-template.md` + workspace pattern | Build transfer registry; run pipeline per transfer |
| Import from RoPA sidecar | + `references/interchange-delta.md` | Read RoPA sidecar; filter third-country transfers; populate registry |
| Discovery mode (map transfers without RoPA) | + `references/essential-guarantees.md` + `references/transfer-qualification.md` | Run structured discovery for international flows; then assess each |
| Review / update existing TIA | Relevant country profile + `references/supplementary-measures.md` | Re-assess after legal landscape change |
| Supplementary measures only | `references/supplementary-measures.md` + country profile | User already has TIA — help select measures |
| Transfer qualification question ("is this a transfer?") | `references/transfer-qualification.md` | Apply three cumulative criteria; produce qualification finding |
| Art. 49 assessment | `references/art49-derogations.md` | Balanced assessment (EDPB position + judicial counter-position) |
| Schrems II background / case law | `references/schrems-ii-holdings.md` | Explain holdings and TIA implications |
| Specific transfer question | Load relevant reference only | Answer directly |

**docx skill:** `/mnt/skills/public/docx/SKILL.md` in Claude.ai Projects, or `docx-processing-anthropic` in Claude Code. If unavailable, generate Markdown as fallback.

## Session Setup

Three quick questions. Adapt if the user provides rich context upfront — extract answers and confirm rather than asking sequentially.

1. **Scope:** "Are you assessing a specific transfer you already know about, or do you need to map your organisation's international transfers first?"
2. **Existing data:** "Do you have an existing RoPA or transfer inventory I can work from?" *(Skip if Scope = specific transfer)*
3. **Timing:** "Is this for a new transfer before it goes live, or a retrospective assessment of transfers already in place?"

The remaining details — exporter, importer, country, mechanism, data categories — are captured as the natural first step of the assessment pipeline, not as a sterile upfront questionnaire.

## Workspace Pattern (Batch Assessments)

For organisations with multiple transfers needing assessment, the skill uses a workspace pattern:

```
skills/tia-workspace/<org-slug>/
├── transfer-registry.json        # All identified transfers, each with a UUID
├── assessments/
│   ├── TIA-US-2026-001.json     # Per-transfer assessment state
│   ├── TIA-US-2026-001.md       # Per-transfer Markdown report
│   ├── TIA-US-2026-001.docx     # Per-transfer formal document (generated last)
│   └── TIA-IN-2026-002.*
├── outbound/                     # Delta files queued for RoPA
│   └── tia-<uuid>-<timestamp>.delta.json
└── state.json                    # Session checkpoint (current transfer, step, partial findings)
```

Checkpoint after every step. Resume by reading `state.json`.

## Pre-Assessment Gate: Transfer Qualification

Before running the 6-step pipeline, the skill determines whether a "transfer" under Chapter V exists. Apply EDPB Guidelines 05/2021 — three cumulative criteria:

1. **Exporter subject to GDPR** for the processing in question (Art. 3(1) or 3(2)).
2. **Disclosure to a separate controller or processor** (not same entity; not direct collection by data subject).
3. **Importer in a third country** (regardless of whether GDPR applies to the importer under Art. 3).

All three met → Chapter V applies → continue to the TIA requirement check.

Any criterion fails → output a **Transfer Qualification Finding** documenting:
- Which criterion failed and why.
- That Chapter V does not apply to this processing.
- That Art. 5/24/32 safeguards remain mandatory (per Section 4 of the guidelines).
- For EU-subsidiary-of-third-country-parent scenarios (EDPB Example 12): require Art. 28 due diligence on the processor's exposure to extraterritorial law.

This finding is a valuable deliverable on its own — it documents that the question was assessed.

### TIA Requirement Check (when all three criteria met)

- **Art. 45 adequacy?** → Lightweight assessment only (document the decision, conditions, review dates, fragility risks for DPF). Use the relevant country profile.
- **Art. 49 derogation?** → Art. 49 assessment path (load `art49-derogations.md`). Balanced framing; document justification.
- **Art. 46 tool** (SCCs, BCRs, ad hoc, codes, certifications) → Full TIA required → proceed to Step 1.

## Assessment Pipeline (Steps 1–6)

Reference: `references/edpb-six-steps.md`. Full detail there; SKILL.md captures the key flow.

### Step 1: Know Your Transfer

Capture (from discovery, RoPA import, or direct user input): exporter, importer, country, data categories, subjects, purpose, volume, frequency, data format, onward transfers. Confirm completeness. Flag onward transfers for separate assessment.

### Step 2: Identify the Transfer Tool

Document the Chapter V mechanism: adequacy / SCCs (module) / BCRs / ad hoc / code / certification. Note execution dates and SA authorisations as relevant.

**After identifying the primary mechanism:** Ask "Could any Art. 49 derogation apply as a primary or alternative basis for this transfer?" If yes → also run Art. 49 assessment as parallel/backup path.

### Step 3: Assess Third-Country Law and Practices

Load the relevant country profile. Three blocks:

**Block A — Data protection framework.** General law, SA, rights, remedies.

**Block B — Surveillance / access laws.** For each relevant law: apply the four essential guarantees (clear rules / necessary & proportionate / independent oversight / effective remedies). Rate each as adequate / concerns / insufficient.

**Block C — Practical risk assessment (Rosenthal-inspired).** Importer's request history, realistic targeting basis, plaintext access necessity, realistic authority interest in this data.

**Step 3 Conclusion — three-way fork (CNIL methodology):**

1. **Transfer tool effective** → proceed to Step 6.
2. **Transfer tool not effective, supplementary measures needed** → proceed to Step 4.
3. **Transfer tool not effective on paper, BUT no realistic basis to believe the problematic law will apply to this transfer in practice** → proceed to Step 6 with thorough, substantive justification.

Option (3) is legitimate (CNIL guide accepts it explicitly) but requires real reasoning — sector, data type, importer profile, request history — not boilerplate.

### Step 4: Supplementary Measures

Triggered when Step 3 returns conclusion (2). Load `references/supplementary-measures.md`. Auto-suggest measures matched to identified gaps. User reviews / accepts / customises. Then assess: do selected measures effectively close the gaps?

If yes → proceed. If no → the transfer cannot proceed as structured. Options: restructure (different importer, different country, different architecture) or suspend.

### Step 5: Implementation Action Plan

Document: measures to implement, owners, due dates, contractual amendments (SCC Annex II edits, side letters), technical changes (encryption, pseudonymisation pipelines), timeline.

### Step 6: Re-assessment Triggers

Document: standing triggers (adequacy review dates, DPF fragility), event-driven (new law, SA action, importer government request, certification change), periodic (12-month default, shorter for high-risk). Set the next review date.

## Outputs

Four deliverables (the user picks what they need):

1. **Markdown TIA Report** — in-session preview. Sections mirror Steps 1–6.
2. **.docx Formal TIA Document** — for the compliance file. Uses `references/tia-template.md` structure with CNIL-style tables, cover page, sign-off block (assessor + DPO), annex with country profile summary.
3. **JSON Interchange Sidecar** — delta file conforming to `interchange-inbound-schema.json` v1.0. Patches `tia_ref`, `tia_status`, `supplementary_measures[]`, `tia_completed_date`, `tia_review_date`. Lands in `skills/ropa-workspace/<org-slug>/inbound/`. See `references/interchange-delta.md`.
4. **Transfer Risk Summary** — one-page executive overview for batch assessments. Per-transfer row: destination, mechanism, verdict, key risk, measures. No numerical scores.

## Cross-Skill Integration

**Inbound from RoPA:** Read sidecar (`<org-slug>-ropa-sidecar.json`) → filter entries with third-country transfers → pre-populate Step 1 → track `activity_id` UUIDs.

**Outbound to RoPA:** Emit delta file per assessed transfer (see Output #3). The delta is owned by RoPA after writing.

**DPIA trigger:** If Step 3 reveals high-risk processing (Art. 9 special categories + systematic monitoring + third-country risk), flag for the user: "Consider whether a DPIA is required under Art. 35. This transfer's risk profile may meet DPIA threshold criteria." Do NOT auto-trigger DPIA Sentinel — just flag.

## Legal Precision Points

These are areas where Claude's training knowledge may be imprecise. Always apply these rules:

1. **A TIA is only required for Art. 46 transfers.** Adequacy (Art. 45) and Art. 49 derogations do not require a TIA — but each needs its own documentation (adequacy: decision ref + conditions; Art. 49: justification + applicable sub-provision).

2. **"Transfer" has no legal definition in the GDPR.** EDPB Guidelines 05/2021 define three cumulative criteria. Direct collection from data subject ≠ transfer (Example 1). Remote access from third country by processor = transfer (Example 11). Employee on business trip accessing own employer's data ≠ transfer (Example 8).

3. **Onward transfers need separate assessment.** Each hop in the chain (controller → processor → sub-processor in third country) is a separate transfer under Chapter V and requires its own analysis.

4. **The DPF is not blanket US adequacy.** Only covers organisations that are (a) subject to FTC/DoT jurisdiction AND (b) actively DPF-certified. Always verify current certification at dataprivacyframework.gov. Non-certified US recipients need SCCs + TIA per `country-profiles/us-non-dpf.md`.

5. **DPF political fragility is a live risk.** The DPF rests on EO 14086 (executive-branch construct). It can be rescinded by a future US administration. For long-term transfers, maintain SCCs as a fallback alongside DPF reliance.

6. **Adequacy decisions can have conditions and expiry dates.** Japan: supplementary rules apply. UK: renewed Dec 2025, valid until 27 Dec 2031 (joint Commission/EDPB review before any renewal). Canada: PIPEDA-regulated organisations only. Republic of Korea: PIPA-regulated only. Document conditions; track review dates.

7. **Art. 49 is not statutorily limited to "last resort."** That framing is EDPB guidance (Guidelines 2/2018), not statute. OLG München (21 U 3882/25 e, 11.05.2026) accepted Art. 49(1)(b) for routine transfers by a global service where the contract is inherently international. CJEU rapporteur Judge von Danwitz has indicated Art. 49 may cover more transfer scenarios than the EDPB acknowledges. Document which position the practitioner is relying on; both are defensible.

8. **"Necessary for contract performance" means the transfer is necessary, not just the contract.** But where the service is inherently cross-border (OLG München), transfer and contract are intertwined. Document the inherently international nature of the service.

9. **Supplementary measures must be effective, not just present.** Encryption with exporter-held keys only helps if the importer does NOT need to decrypt. A challenge clause only helps if the importer has a realistic legal avenue. Document the effectiveness assessment for each measure, including "when NOT effective" conditions.

10. **The "no reason to believe" escape valve is legitimate but must be documented.** CNIL Step 3 conclusion option (3) — transfer tool not effective on paper, but no realistic basis to believe the problematic law will apply — requires substantive justification (sector, data type, importer profile, request history), not boilerplate assertion.

11. **SCCs cannot be modified.** Only optional clauses can be filled in; parties can be added via the docking clause (Clause 7). Supplementary measures sit alongside the SCCs (typically in Annex II or a side agreement), not inside the SCC text.

12. **The controller is responsible even when the processor initiates the transfer.** Per EDPB Guidelines 05/2021 Example 7: where a processor transfers to a sub-processor in a third country, the controller remains responsible under Art. 28 and Chapter V.

13. **EU subsidiaries of third-country companies can trigger transfer issues without an actual transfer.** EDPB Guidelines 05/2021 Example 12: if the EU processor is subject to extraterritorial surveillance law (e.g., the CLOUD Act via its US parent), compliance with a government access request would *become* a transfer. Assess this under Art. 28 before engaging the processor.

14. **A TIA must be done BEFORE the transfer begins.** Per Schrems II and EDPB Recommendations 01/2020, the assessment is a pre-condition for an Art. 46 transfer. Retrospective TIAs for existing transfers are common in practice but represent a compliance gap; document the gap and close it.

15. **Re-assessment is not optional.** Art. 46 mechanisms require ongoing monitoring. Legislative changes (new surveillance law), case law (Schrems III when it lands), SA enforcement actions in the recipient country, importer's receipt of a government access request, and political developments (DPF rescission risk) all trigger re-evaluation. Default periodic review: 12 months.

## References

- GDPR Chapter V (Arts. 44–49)
- CJEU C-311/18 (Schrems II)
- EDPB Recommendations 01/2020 v2.0 (supplementary measures)
- EDPB Recommendations 02/2020 (essential guarantees)
- EDPB Guidelines 05/2021 v2.0 (Art. 3 / Chapter V interplay)
- EDPB Guidelines 2/2018 (Art. 49 derogations)
- CNIL TIA Guide (final version, January 2025)
- OLG München, 21 U 3882/25 e (11.05.2026)
- Implementing Decision (EU) 2023/1795 (EU-US DPF)
- Rosenthal EU SCC TIA Toolbox (v1.10, patched September 2025)

Full citations in `references/sources.md`.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## Related GDPR skills

This skill works standalone, but pairs well with my other EU data-protection skills — install any on its own or combine them:

- **DPIA Sentinel** — Art. 35 Data Protection Impact Assessments
- **GDPR Breach Sentinel** — Art. 33/34 breach response & notification
- **Privacy Notice Generator** — Art. 13/14 privacy notices
- **DPA Art. 28** — controller–processor agreements (AVV)
- **Legitimate Interest** — Art. 6(1)(f) LIA / balancing test
