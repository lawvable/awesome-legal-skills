# Example — auditing a user-supplied ECCC document

This example walks through two audit modes for documents supplied by the user: a working draft (citations need verification) and a finalised Court record (citations are by definition Court-issued; the audit task shifts).

## Working draft — audit citations for accuracy

### The scenario

The user uploads a 15-page memo entitled "Civil Party Reparations at the ECCC — Lessons from Case 002/02 for Future Practice". The memo contains 27 footnotes citing ECCC documents. The user asks: *"Can you audit this for me before I send it?"*

### Step 0 — Identify the document

Open the memo. Confirm:
- It is a working draft, not a Court record. (No Case File Number, no document number, no signature line of a Chamber.)
- It is written by the user — note the author convention.
- It cites the ECCC — confirm that all 27 footnotes are ECCC citations, not citations to other tribunals.

### Step 1 — Inventory the citations

List each citation. For each, note:
- Document type (judgment, decision, closing order, Internal Rule, ECCC Law article, academic source)
- Case (001 / 002 / 002/01 / 002/02 / 003 / 004 / N/A)
- Document number
- Date
- Chamber
- Paragraph or article referenced
- Proposition supported

A typical inventory entry:

| # | Type | Case | Doc no. | Date | Chamber | Para/Art | Proposition |
|---|---|---|---|---|---|---|---|
| 1 | Trial Judgment | 002/02 | E465 | 16 Nov 2018 | TC | para. 4377 | reparations regime |
| 2 | Internal Rule | n/a | n/a | Rev. 9 | n/a | Rule 23 quater(1) | civil party application |

### Step 2 — Verify each citation

Work the fallback ladder for each:
- Tier 1 (eccc.gov.kh, legal-tools.org) for case-specific citations.
- Project knowledge (if present) for foundational instruments.
- Tier 2 for academic sources (and confirm the academic source itself exists and says what the user attributes to it).

For each, record the verification level: existence / content / paragraph.

### Step 3 — Output the audit

Return the audit as a numbered list mirroring the user's footnotes. For each:
- **Verified** — when document, date, chamber, and paragraph are all confirmed and the proposition is supported.
- **Existence verified; content not confirmed** — when the document is real but the cited proposition could not be confirmed in this session. Recommend the user open the document at the cited paragraph before filing.
- **Discrepancy** — when verification surfaces a mismatch. Examples:
  - The citation gives "Case 002/01" but the document number E465 is the Case 002/02 Trial Judgment.
  - The citation gives "Rev. 8" but Rule 23 quater(1) was introduced in Rev. 9; the cited rule does not exist in Rev. 8.
  - The citation gives "17 November 2018" but the Case 002/02 Trial Judgment is 16 November 2018.
- **Cannot verify** — when no Tier 1 source confirms the document exists. Ask the user for the URL or filename.

### Common findings in working drafts

- **Internal Rule revision drift.** A memo from 2020 cites "Internal Rules, Rule 23 bis(1)" without revision. Audit task: identify which revision applied to the events discussed and which revision applies today (Rev. 10); flag the divergence if any.
- **Severance ambiguity.** "Case 002 Trial Judgment, para. X" — does the user mean E313 (002/01) or E465 (002/02)? Both are "Case 002 Trial Judgments" loosely speaking. Audit task: identify which and propose the correct citation.
- **Accused-name order.** "Chea Nuon" instead of "NUON Chea". Audit task: flag and propose the ECCC-correct form.
- **Article number without "new" suffix.** "ECCC Law, Article 29" — the post-2004 amended article is "Article 29 new". Audit task: flag and propose the rigorous form, noting that the omission is common in older sources.
- **Closing Order document number.** Citations to "the Case 002 Closing Order" without document number — the document number is D427. Audit task: complete the citation.

## Finalised Court record — different audit task

### The scenario

The user uploads the Case 002/02 Trial Judgment (E465, 16 November 2018) and asks: *"Help me trace the Chamber's reasoning on the Cham genocide. What other documents will I need to consult?"*

### Step 0 — Identify the document

Open the PDF. Confirm:
- Case File Number on the cover page: `002/19-09-2007/ECCC/TC`.
- Document number: `E465`.
- Date: 16 November 2018.
- Issuing body: Trial Chamber.
- Status: this is a Court record. Citations within it are by definition Court-issued.

Once identity is confirmed, the audit task is *not* to verify the document's internal citations — they were Court-issued. The audit task is to **inventory** what downstream work will need.

### What the audit produces

A structured inventory of:

1. **Referenced ECCC documents** — every internal cross-reference (to other filings in Case 002, to the Closing Order D427, to PTC decisions, to Trial Chamber filings, to expert reports). For each, note the document number, whether it is public or confidential, and whether a public version exists.

2. **Referenced ECCC jurisprudence** — citations to the Case 001 Trial Judgment and Appeal Judgment, to the Case 002/01 Trial Judgment and Appeal Judgment, to PTC decisions on JCE and other major procedural rulings.

3. **Referenced foundational provisions** — every ECCC Law article cited, every Internal Rule cited (with revision in force at the relevant time), every UN-Cambodia Agreement provision cited.

4. **Referenced external international jurisprudence** — citations to ICTY, ICTR, SCSL, ICJ, ICC, and other tribunals' decisions, used by the ECCC for comparative or interpretive reasoning.

5. **Referenced treaties and customary law sources** — 1948 Genocide Convention, 1949 Geneva Conventions, 1954 Hague Convention, 1961 Vienna Convention on Diplomatic Relations, customary international humanitarian law.

6. **Referenced expert and witness materials** — expert reports, witness transcripts, civil party applications. Distinguish those available in public form from those that remain confidential.

### Distinguishing public and confidential

ECCC frequently issues documents in three versions: public-redacted, confidential, and strictly confidential. The Trial Judgment cites all three. For the user's downstream work:

- Public-redacted versions are accessible on eccc.gov.kh.
- Confidential versions are accessible only to parties (the user, as a former civil party lawyer or counsel, may or may not have access in any given case).
- Strictly confidential versions are accessible only to a narrower set.

The audit flags which referenced documents the user will need party access to retrieve.

### Internal consistency

A finalised Court record is presumptively internally consistent (the Chamber has signed it). The audit should still flag:
- Any apparent typographical errors in document numbers or dates.
- Any reference to a document number that does not match the document the Chamber describes (rare, but it happens).
- Any reference to a paragraph in another judgment where the cross-referenced paragraph does not appear to address what the Chamber says it addresses (very rare; usually a copy-edit slip).

These are minor. The point of flagging is so the user, in downstream work, can decide whether to rely on the Chamber's characterisation or to look up the underlying document.

## What this example does not show

- The audit of a closing order (D-series document), which has its own structural conventions.
- The audit of a PTC decision involving JCE, which requires close attention to the JCE I / II / III distinction.
- The audit of a civil party application, which is governed by Rule 23 *bis* / *ter* / *quater* and where the revision in force at the date of application matters.

For these, the workflow in `../references/verification-workflow.md` applies, with the audit framing of this document.

## Cross-references

- `../SKILL.md` — entry point and standard workflow
- `../references/verification-workflow.md` — the fallback ladder
- `../references/citation-format.md` — citation conventions
- `example-verification.md` — a single citation worked through end-to-end

