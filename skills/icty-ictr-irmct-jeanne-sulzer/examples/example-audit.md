# Example — auditing user-supplied documents

Two worked examples of audit mode: a working draft and a final court record. The audit task differs by document type. Step 0 (identify the document) always comes first.

---

## Example A — auditing a working draft

### The document

The user uploads a draft article with this sentence:

> "The Appeals Chamber in *Tadic* (1997) established the three forms of joint criminal enterprise, and the ICTR later applied JCE III in *Akayesu* to convict for genocide."

### Step 0 — Identify

This is a working draft (an article in progress), so the audit task is **accuracy of citations**. Two factual claims are embedded:
1. *Tadić* (1997) Appeals Chamber established the three forms of JCE.
2. *Akayesu* applied JCE III to convict for genocide.

### The audit

**Claim 1 — date and chamber.** The Tadić Appeal Judgment that articulated JCE is **15 July 1999** (IT-94-1-A), not 1997. The 1997 date is the **Trial** Judgment (7 May 1997), which did not articulate the three-category JCE doctrine. The draft conflates the trial and appeal and misdates the appeal. **Flag: date and chamber error.**

**Claim 2 — Akayesu and JCE III.** Akayesu (ICTR-96-4-T, 2 September 1998) is the landmark genocide conviction, but it is not the JCE III case — its reasoning rests on direct responsibility and the elements of genocide, including sexual violence as a genocidal act. Attributing a JCE III holding to Akayesu should be verified and is very likely an error. **Flag: probable mischaracterisation — verify against the judgment; do not assert the JCE III link without it.**

### The output

Report both flags. Correct claim 1 to: *Prosecutor v. Tadić*, Case No. IT-94-1-A, Appeal Judgment (Appeals Chamber), 15 July 1999. For claim 2, tell the user the Akayesu/JCE III link is not supported by what is known of the judgment and must be verified or removed — and do not supply a paragraph to prop up an unverified proposition.

---

## Example B — auditing a final court record

### The document

The user uploads the **Mladić Appeal Judgment** (MICT-13-56-A, 8 June 2021) and asks: "Summarise the disposition and tell me which underlying documents I'd need to cite this properly."

### Step 0 — Identify

This is a **final court record** issued by the Appeals Chamber of the Mechanism. Citations *within* it are by definition Court-issued. The audit task is therefore not "check the citations for accuracy" but **inventory the document and map what downstream work depends on**.

### The audit task

- Confirm identity: *Prosecutor v. Ratko Mladić*, Case No. MICT-13-56-A, Judgment (Appeals Chamber), 8 June 2021. Note the trial-level document it reviews: the ICTY Trial Judgment, Case No. IT-09-92-T, 22 November 2017 — a **different case number** (IT, not MICT) for the same accused. This IT/MICT pairing is exactly what Step 0 exists to catch.
- Note the version: confirm whether the uploaded file is the public, public redacted, or confidential version, and cite accordingly.
- For a downstream citation, the user needs: the appeal judgment (MICT-13-56-A) for the appellate holding and disposition; the trial judgment (IT-09-92-T) for the findings of fact and the original conviction and sentence.
- Respect protective measures: the Mladić record involves protected witnesses. Do not reproduce any protected identifying information that may appear in an unredacted portion.

### The output

A short, faithful summary of the disposition (drawn from the document itself, which is authoritative), plus the two citations the user needs (appeal and trial, with their respective IT/MICT numbers), plus a note on the version cited and a protective-measures caution.

---

## The common thread

In both modes, Step 0 — identifying exactly what document is in front of you, including the correct case number and the IT/ICTR/MICT distinction — is what prevents the most damaging errors. A working draft is audited for citation accuracy; a final record is inventoried and mapped. Neither is treated as a database to be paraphrased from memory.
