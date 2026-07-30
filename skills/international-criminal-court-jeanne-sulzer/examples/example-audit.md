# Example: auditing ICC citations

Two audit modes. They look superficially similar — both involve a user supplying a document with citations and asking you to clean it up — but the right approach differs.

---

## Mode A — auditing a working draft

The user is preparing their own filing or memo. Citations in the draft come from prior drafts, model recall, secondary summaries, colleagues' notes. The audit treats them as unverified until checked.

### Task

**User:** "Here's the working draft of my chain-of-command memo. Please expand the section on superior responsibility and clean up the citations."

The draft contains, among others:
- An OTP statement on a recent arrest, dated [X].
- A citation to *Prosecutor v. Bemba*, Trial Chamber III judgment, March 2016, for a proposition on *civilian* superior responsibility.
- A citation to a Pre-Trial Chamber decision identified only by approximate description.

### Workflow

1. **Inventory** every ICC citation in the draft, with its document number, date, and the proposition it is being cited for.

2. **Spot-check on its face.** Citation 2 is a red flag immediately — Bemba was a military command-responsibility case (Article 28(a)), not civilian (Article 28(b)). The draft uses it for a 28(b) point. An audit catches this before any web_fetch.

3. **Verify the rest** via the verification workflow. For Bemba, fetch the TJ and read the cited paragraph to confirm whether it actually addresses 28(b) or 28(a). For the OTP statement, locate it on icc-cpi.int. For the underspecified Pre-Trial decision, ask the user for clarification — do not guess.

4. **Report to the user before expanding.** Do not silently fix, do not silently propagate.

   > I've audited the citations in the draft:
   >
   > 1. **OTP statement** — verified on icc-cpi.int.
   > 2. **Bemba Trial Chamber judgment** — document exists, but the cited proposition is a problem. The draft uses Bemba for the *civilian* superior responsibility standard (Article 28(b)), but Bemba is a *military* command responsibility case (Article 28(a)). The paragraph cited addresses 28(a). Two options: (i) recharacterise the citation as 28(a) and address whether the reasoning transfers; or (ii) substitute a case that actually addresses 28(b) — but I would need to identify and verify one. Which would you prefer?
   > 3. **Underspecified Pre-Trial decision** — I can't tell which decision is meant from the draft's description. Could you point me to the document number or a closer description?

5. **Proceed only after the user resolves the flags.** Any new citation introduced during expansion follows the standard verification workflow, with verification levels reported.

### What this catches

- Mis-categorised authorities (Bemba for 28(b))
- Stale paragraph references that no longer match the current public-redacted version
- Citations to confidential or under-seal filings the drafter cannot lawfully see
- Citations that exist only in secondary summaries but not in any Court record

The cost is one or two tool calls per existing citation. The alternative is propagating errors into the user's filing.

---

## Mode B — auditing a finalised Court record

The user supplies an actual ICC filing — a judgment, a decision, a warrant, an OTP brief. The citations in such a document *are* the Court's. The audit task is fundamentally different: not "are these citations correct" but "for downstream work relying on this document, what needs to be fetched and what is off-limits."

### Task

**User:** "Audit the citations in this attached document and flag anything that needs verification."

Document, on reading: *Prosecutor v. Ali Muhammad Ali Abd-Al-Rahman ("Ali Kushayb")*, Situation in Darfur, Sudan, Appeals Chamber, "Decision on the 'Prosecution request for an extension of time to respond to the Defence Appeal Brief'", ICC-02/05-01/20-1311, 19 February 2026.

### First step — identify the document

Before auditing citations, identify what the document actually is. Document headers (case, chamber, document number, date) are reliable; conversational labels users use (e.g. naming the wrong case) are not. If the conversational label and the document's own header disagree, surface the mismatch immediately.

### Workflow

1. **Inventory** all citations in the document, distinguishing:
   - **Internal cross-references** — other filings in the same case (predominate in procedural decisions).
   - **Foundational instruments** — Statute, RPE, Regulations.
   - **External citations** — case law from other ICC cases, secondary sources.

2. **For internal cross-references**, flag:
   - **Public vs confidential.** Confidential documents (`-Conf`, `-Conf-Exp`) cannot be cited from this decision alone — downstream work must use the `-Red` version. List the confidential references separately.
   - **Whether substantive reliance is intended.** Cross-references to procedural prior decisions (e.g. an earlier extension order) usually need only the document number; cross-references to underlying judgments or trial records need to be fetched for any substantive reliance.

3. **For foundational instruments**, confirm against project knowledge (Rome Statute, etc.) or the current text on icc-cpi.int.

4. **For external citations**, run the standard verification workflow.

5. **Report** as an inventory, organised by what the user's downstream work would need to do with each item.

### Sample output

> Document identified: *Prosecutor v. Abd-Al-Rahman*, Appeals Chamber, ICC-02/05-01/20-1311, 19 February 2026. Situation: Darfur, Sudan. (Note: the conversational reference to this as the "El Hichri document" appears to be a mislabelling — this is the Abd-Al-Rahman/Sudan case, not anything in the Libya situation.)
>
> **Citations inventory:**
>
> *Foundational instruments — citable directly from project knowledge:*
> - Rome Statute, Article 81(1)(b) — basis for the Defence Notice of Appeal
> - Regulations of the Court, regulations 31, 35(2), 58, 59(1) — procedural basis for the decision
>
> *Internal cross-references — public, citable but verify before substantive reliance:*
> - Trial Judgment, ICC-02/05-01/20-1240, 6 October 2025 — for any reliance on the substance of the conviction, fetch the judgment.
> - Sentencing Judgment, ICC-02/05-01/20-1281-Red, 9 December 2025 — cite the public redacted version.
> - Decision on modalities of victim participation, ICC-02/05-01/20-1299 (A), 23 January 2026 — verify for any victim-participation analysis.
> - Decision on Application for Extension to File Defence Appeal Brief, ICC-02/05-01/20-1285 (A), 15 December 2025 — relevant for regulation 35(2) "good cause" standard.
>
> *Internal cross-references — confidential, do not cite from this document:*
> - ICC-02/05-01/20-1240-AnxB-Conf (Annex B to the Trial Judgment) — cite the `-Red` counterpart.
> - ICC-02/05-01/20-1281-Conf and -Conf-Anx (confidential Sentencing Judgment and annex) — cite the `-Red` Sentencing Judgment.
> - ICC-02/05-01/20-1303-Conf (Defence Appeal Brief) — cite the `-Red` filed on 4 February 2026.
>
> *One internal point to flag:* the decision notes that the Prosecution was notified of the Appeal Brief on 2 February 2026, while the public redacted version was filed on 4 February 2026. Downstream work citing the Appeal Brief should use the date appropriate to the audience (notification date for procedural posture; filing date for the public document).
>
> **Verification status:** Document identity verified from the document's own header. External cross-corroboration on icc-cpi.int could not be completed in this conversation (the site returned 403 on direct fetches; see `references/verification-workflow.md`). The audit relies on the document's internal consistency and standard ICC document-numbering conventions. For substantive reliance on any of the cross-referenced filings, fetch them via the fallback ladder before citing.

### Why this mode is different

- The document's own citations are not subject to "are they real?" audit — they are the Court's. The question is how downstream work uses them.
- The confidential/public distinction is the dominant audit axis, not citation accuracy.
- Identity verification (is this document what the conversation says it is?) is more important than citation verification, because getting the case wrong derails everything.

### What this mode catches

- Document identity mismatches between the user's label and the document itself.
- Confidential references that downstream work cannot lawfully cite.
- Internal inconsistencies (date mismatches, redaction status changes between filings).
- Foundational instrument references that need to be quoted with care.

---

## Choosing the mode

If in doubt, ask. A heuristic:

- **Working draft** = the user wrote it (or is editing material from colleagues), the citations are claims being made, the audit is "are these claims supported?"
- **Court record** = the Court issued it, the citations are part of the Court's record, the audit is "how do I work with this document?"

Mixing the modes produces unhelpful output in both directions: running a working-draft audit on a Court record looks pedantic about things the user can't change; running a Court-record inventory on a working draft misses errors in the user's own work.
