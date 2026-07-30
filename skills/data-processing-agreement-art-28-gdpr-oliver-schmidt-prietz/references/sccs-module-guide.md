# SCCs Module Guide — Commission Implementing Decision (EU) 2021/914

This file is loaded **whenever international transfers are in scope** (importer outside the EEA, or accessible from outside the EEA). The 2021 SCCs replaced the 2010 SCCs and the 2001 controller-to-controller SCCs; older versions can no longer be entered into for new transfers (deadline lapsed 27 December 2022).

## The four modules

The 2021 SCCs are **modular**. The parties select the module that matches the relationship between data exporter and data importer for that specific transfer. The wrong module is a substantive defect — you cannot use Module 2 for a controller-to-controller transfer.

| Module | Exporter | Importer | Typical use |
|---|---|---|---|
| **Module 1** | Controller | Controller | Two independent controllers exchanging data (e.g. group-internal between EU and non-EU affiliates with separate purposes; M&A data rooms; co-marketing partnerships where both are controllers) |
| **Module 2** | Controller | Processor | EU controller engages non-EU processor; the most common case in commercial DPAs |
| **Module 3** | Processor | Sub-processor | EU processor engages non-EU sub-processor on behalf of (potentially EU or non-EU) controller |
| **Module 4** | Processor | Controller | Reverse flow: non-EU processor sends back to EU controller (rare; usually about regulated returns of analytic outputs) |

### Quick decision rule

1. **What is the exporter's role for this data?** Controller → Module 1 or 2. Processor → Module 3 or 4.
2. **What is the importer's role?** Controller → Module 1 or 4. Processor → Module 2 or 3.
3. Cross-tabulate. The intersection is your module.

If both parties play different roles for **different processing operations**, you may need **multiple SCCs** (or a single SCC with module-switching for relevant data flows; this is rare and complex — prefer separation).

## Mandatory annexes (apply to all modules)

The SCCs are an *agreement* but they are *operationalised* through three annexes:

| Annex | Content | Where it comes from |
|---|---|---|
| **Annex I.A** | List of parties (full legal names, addresses, contact persons, role for that transfer) | Drafted at signing |
| **Annex I.B** | Description of transfer (categories of data subjects, categories of personal data, sensitive data + safeguards, frequency, nature, purpose, retention, sub-processors when Module 2/3) | **Mirrors DPA Annex 1** — keep aligned |
| **Annex I.C** | Competent supervisory authority | Per Clause 13 — usually the SA where the controller (Module 1/2) or the EU representative (Module 3/4) is established |
| **Annex II** | Technical and organisational measures | **Mirrors DPA Annex 2** — keep aligned |
| **Annex III** | List of sub-processors (Module 2/3 only, where general authorisation applies) | **Mirrors DPA Annex 3** |

**Critical drafting principle**: when SCCs and a DPA exist in parallel, **the DPA annexes and SCC annexes must be kept consistent**. The cleanest approach is to incorporate them by cross-reference: "The TOMs in Annex 2 of this DPA shall constitute Annex II of the Standard Contractual Clauses."

## Docking the SCCs with the DPA

Two architectural choices for combining a DPA with SCCs:

### Option A: Standalone SCCs + DPA
The parties sign two separate documents. The SCCs reference the underlying main contract; the DPA addresses Art. 28 substance.

- **Pro**: Cleanest legal hygiene; SCCs unmodified; clear what governs international transfers vs Art. 28 substance.
- **Con**: Two signature flows; risk of inconsistency between annexes if not maintained jointly.

### Option B: Integrated DPA with SCCs incorporated
The DPA incorporates the SCCs by reference, often as an annex or a "Transfer Schedule" with the SCCs reproduced in full or attached.

- **Pro**: Single document execution; easier to maintain.
- **Con**: Risk of "modifications" that creep into the SCCs (forbidden — see below); risk that the SCCs section gets less attention in negotiation.

**Recommendation**: Option A is cleaner for negotiation-grade engagements; Option B is acceptable for commercial volume work if the DPA explicitly states "The SCCs are incorporated without modification" and the parties resist any temptation to redline them.

### Article 28 docking (under Module 2/3)

The 2021 SCCs are designed to **also satisfy Art. 28 GDPR** for processor relationships under Modules 2 and 3 (see SCC Clause 8 + Annex II). This means in principle a **standalone set of SCCs Module 2 can replace a DPA**.

In practice:
- For purely intra-EEA-with-non-EEA-tail-processing relationships, Module 2 SCCs as standalone document are workable.
- For most commercial relationships, the SCCs are too sparse on commercial issues (audit logistics, liability, term, dispute resolution) — practitioners still execute a separate DPA with SCCs as annex.
- Be alert: a well-drafted Module 2 SCC + tight Annex II already satisfies Art. 28 — do not duplicate the (a)–(h) obligations elsewhere if doing so creates conflicts.

## What can NOT be modified in the SCCs

The Implementing Decision permits adding clauses (Clause 2(a) — additional safeguards) and modifying the optional docking clause for new parties (Clause 7), but the **substantive clauses cannot be modified**. Common attempts to modify that are **not permitted**:

- Capping liability of the data importer below what Clause 12 provides.
- Diluting Clause 14 (assessment of laws of third country) by replacing it with "the parties agree no further assessment is needed".
- Removing Clause 15 (notification of access requests by public authorities).
- Reducing Clause 16 (suspension/termination right of data exporter).
- Limiting third-party-beneficiary rights of data subjects (Clause 3).

Such modifications **invalidate the SCCs** as a transfer mechanism. If the importer demands them, there is no SCCs deal — alternative mechanisms must be considered (BCRs, derogations under Art. 49, no transfer).

## Transfer Impact Assessment (TIA)

Following the Schrems II judgment (CJEU C-311/18) and SCC Clause 14, the parties must assess whether the law of the third country (a) provides essentially equivalent protection or (b) does not — and if not, whether **supplementary measures** can fill the gap.

A TIA is **mandatory for every transfer** under SCCs (or BCRs); it is the parties' obligation, not the supervisory authority's job to police.

Minimum TIA content:
1. Description of transfer (mirrors Annex I.B).
2. Identification of importer's country and applicable laws.
3. Assessment of those laws' compatibility with EU essential equivalence (problematic regimes: surveillance laws permitting bulk access, lack of redress mechanisms, data-localisation requirements with foreign-government access).
4. Assessment of practical risk (has the importer received government access requests? can the importer resist them?).
5. Supplementary measures: technical (encryption with keys held outside the third country, pseudonymisation), contractual (warranty clauses, transparency obligations), organisational (policies for handling government requests).
6. Conclusion: transfer permissible / permissible with measures / not permissible.

The TIA is referenced in this DPA skill but **drafted via a separate skill** if available. Include in the DPA / SCC bundle a recital confirming a TIA has been conducted.

## Special-status third countries

| Status | Mechanism | Notes |
|---|---|---|
| **Adequacy decision** (UK, Switzerland, Japan, South Korea, Canada (commercial), New Zealand, Israel, Argentina, Uruguay, Faroe Islands, Guernsey, Isle of Man, Jersey, Andorra) | **No SCCs needed** for transfers to recipients in these countries (subject to scope of decision) | Verify scope: e.g., the Japan adequacy is limited to private-sector commercial activities |
| **EU–US Data Privacy Framework (DPF)** | Importer self-certified under DPF: **no SCCs needed**; verify certification status on the DPF list at the time of transfer | DPF replaced Privacy Shield (July 2023). DPF certifications are subject to the same Schrems-style scrutiny; some risk of future invalidation. |
| **EU–UK** | UK adequacy decision through 27 June 2025, then likely renewed; UK is the easiest destination | Watch for renewal status |
| **Other countries (US non-DPF, India, China, etc.)** | SCCs + TIA required | China and Russia in particular: high TIA bar; supplementary measures usually required |

For DPF transfers, the DPA should still address the scenario where the importer ceases to be DPF-certified — a fallback mechanism (SCCs + TIA) should be triggered.

## Common defects in SCC sections of DPAs

1. **Empty Annexes** — SCCs signed with Annex I.A populated but I.B / II / III blank. Renders the SCCs operationally meaningless.
2. **Wrong module** — Module 2 used for what is actually a controller-to-controller transfer (Module 1).
3. **Stale module** — referencing the 2010 SCCs (no longer valid).
4. **No TIA** — SCCs cited as the transfer mechanism but no TIA conducted; Clause 14 obligation breached.
5. **DPF as sole basis without fallback** — relying solely on importer's DPF certification with no fallback if certification lapses.
6. **Modifications to substantive clauses** — see above; invalidates SCCs.
7. **Inconsistency between SCC annexes and DPA annexes** — different sub-processor lists, different TOMs descriptions; one or both will be wrong by definition.
8. **Sub-processor SCCs missed** — if the EU processor uses a non-EU sub-processor, that flow needs Module 3 SCCs between the EU processor and the non-EU sub-processor; commonly forgotten.
9. **Onward transfer silence** — non-EU importer further transfers to its own non-EU sub-processors with no SCC chain.

## Output integration

When this guide is loaded, the DPA output (whether DRAFT or REVIEW) must:

- Identify the module(s) needed for each transfer flow in scope.
- Confirm Annexes I.A / I.B / I.C / II / III are populated (or flag gaps).
- Confirm a TIA exists or flag the requirement.
- For DRAFT: provide the SCC integration approach (Option A standalone or Option B integrated).
- For REVIEW: flag any of the nine common defects above.
