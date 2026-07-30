# Example — verifying a single ECCC citation

This example walks through the verification of a single ECCC citation from question to verified output. It illustrates how the workflow in `../references/verification-workflow.md` looks in practice.

## The question

The user asks:

> "What did the Trial Chamber hold on genocide against the Cham in Case 002/02? Give me a citation I can use."

## Step 0 — Identify the document

The user has named:
- The Court: ECCC.
- The case: 002/02.
- The body: Trial Chamber.
- The proposition: genocide against the Cham — meaning the Chamber's findings on the elements of genocide, applied to the Cham minority.
- The artefact: the Trial Judgment in Case 002/02.

The Case 002/02 Trial Judgment was rendered on 16 November 2018. Its document number is E465. The accused at judgment were NUON Chea and KHIEU Samphan (proceedings against IENG Sary terminated upon his death in March 2013; proceedings against IENG Thirith terminated in August 2015).

This identification is the working hypothesis at Step 0. Step 2 will verify it.

## Step 1 — Plan citations

The citation to plan:

- Document: Trial Judgment in Case 002/02.
- Proposition: the Trial Chamber's holding on the actus reus and mens rea of genocide as applied to the Cham, and the resulting finding of guilt for genocide.
- Verification target: paragraph-pinpoint level for the holding; content level for the overall conclusion.

## Step 2 — Verify, with the fallback ladder

### Rung 1 — eccc.gov.kh

Attempt `web_fetch` to the Case 002/02 trial landing page: `https://www.eccc.gov.kh/en/cases/case-002/trial-02`.

Expected outcome: the page lists the major decisions including the Trial Judgment (E465, 16 November 2018) with a link.

Then `web_fetch` the Trial Judgment PDF itself.

Expected outcome: the PDF is large (the Case 002/02 Trial Judgment is over 2,300 pages). The first pages give document identification (Case File No. 002/19-09-2007/ECCC/TC, Trial Judgment, 16 November 2018). The findings on genocide against the Cham appear later in the judgment, in the chapter dedicated to the Cham.

What the verification yields:
- **Existence verified.** Document number, title, date, chamber confirmed.
- **Content verified, in part.** The PDF retrieval surfaced the existence of the Cham genocide finding but not necessarily every paragraph the user might want to cite.
- **Paragraph verified, only for paragraphs actually surfaced in the retrieval.** If a paragraph-pinpoint claim is needed for a specific holding (e.g. on the protected group, on the genocidal intent), the paragraph itself must be in the retrieved content.

### Rung 2 — legal-tools.org

Cross-check the document number and metadata. The Case 002/02 Trial Judgment should appear on legal-tools.org with the same document number and date. If a discrepancy appears, the eccc.gov.kh version controls.

### Rung 3 — OHCHR or UN Rule of Law

The UN Rule of Law database hosts the Case 002/02 Trial Judgment (the UN was a party to the establishment of the Court). Useful as an alternative download point if eccc.gov.kh is slow.

### Rung 4 — Tier 2 summarisation

Academic commentaries (e.g. *Journal of International Criminal Justice*, *International Legal Materials*, the *Asian Journal of International Law*) have analysed the Case 002/02 genocide findings. They can guide the user toward the relevant paragraphs and confirm broad content, but cannot themselves serve as the citation for a Court holding.

For example: an academic article notes that the Trial Chamber found the Cham to be a protected group under the Genocide Convention as a religious and ethnic group. This is *useful* for orientation. It is *not* the citation — the Trial Judgment is. The article's footnote will tell you the paragraph; the verification still rests on the Trial Judgment itself.

## Step 3 — Draft using verified material

Suppose verification gives:
- Existence: confirmed at E465, 16 November 2018, Trial Chamber.
- Content: confirmed that the Trial Chamber found genocide against the Cham, and that this finding rested on the protected-group status of the Cham and the specific intent of the perpetrators.
- Paragraph: a specific paragraph cluster (illustratively, paras. 3422–3514) was surfaced in the retrieval, with the holding on protected-group status in para. 3422 and the holding on specific intent in paras. 3445–3450.

Draft citation:

> The Trial Chamber held that the Cham constituted a protected group under the Genocide Convention as both a religious and an ethnic group. *Prosecutor v. NUON Chea and KHIEU Samphan* (Case 002/02), Trial Chamber, "Trial Judgment", E465, 16 November 2018, para. 3422.
>
> The Trial Chamber further held that the specific intent to destroy the Cham as such was established. *Ibid.*, paras. 3445–3450.

If only existence and broad content (not paragraph) were verified:

> The Trial Chamber found that the Cham constituted a protected group under the Genocide Convention. *Prosecutor v. NUON Chea and KHIEU Samphan* (Case 002/02), Trial Chamber, "Trial Judgment", E465, 16 November 2018 (paragraph content not retrieved in this session — paragraph pinpoint omitted).

## Step 4 — Self-audit

For each sentence in the draft, the model asks: does this trace to project knowledge or to a successful retrieval in this conversation?

- "The Trial Chamber held that the Cham constituted a protected group" — traces to the Trial Judgment, paragraph 3422, retrieved in Step 2.
- "as both a religious and an ethnic group" — same paragraph.
- "The specific intent to destroy the Cham as such was established" — traces to the Trial Judgment, paragraphs 3445–3450, retrieved in Step 2.

If any sentence does not trace, it comes out, or it is softened to what the retrieval supports.

## Common failure modes this example catches

- **Citing the Case 002/02 Trial Judgment without distinguishing it from the Case 002/01 Trial Judgment.** Case 002/01 (E313, 7 August 2014) does not address genocide against the Cham — that charge was tried in 002/02.
- **Citing "Case 002" instead of "Case 002/02".** A precise reader of the citation will notice the missing slash.
- **Citing the appeal judgment (F76, 23 December 2022) when the user wants the Trial Chamber's holding.** The appeal judgment affirmed (with adjustments) but is a different document. (The appeal was orally pronounced on 22 September 2022; cite F76 with the 23 December 2022 written-judgment date — see `../references/citation-format.md`.)
- **Inventing a paragraph number.** If the retrieval did not surface paragraph 3445, you do not have it. Omit the pinpoint or ask for the document.

## What this example does not show

- The handling of confidential filings (where the paragraph the user wants exists only in a confidential version).
- The handling of Khmer-language documents (the Trial Judgment is in English, but some underlying filings cited within it are in Khmer or French).
- The handling of major dissents (the Case 002/02 Trial Judgment contains separate opinions; if the user wants a dissent, name the judge and verify the dissent appears in the retrieved content).

For these, see `../references/verification-workflow.md` and `example-audit.md`.

