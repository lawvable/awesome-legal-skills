# Verification workflow

The operational procedure for getting any ICC citation into an output. Read this any time you are about to draft something containing ICC citations.

## The discipline

For any case-specific document — judgment, decision, warrant, filing, OTP statement — verify before citing. Verification means retrieving the document from icc-cpi.int or legal-tools.org (or another Tier 1 source) in the current conversation. Foundational texts in project knowledge are the only exception.

The reason: ICC document numbers are exact, paragraph numbers are exact, and the cost of an invented citation in real work — a filed brief, a published article, an internal memo a colleague relies on — is high. Two to five `web_fetch` calls per citation is the correct cost.

## Verification is gradient

In practice, retrieval is unreliable. icc-cpi.int sometimes returns 403. Some documents are only on legal-tools.org. Some are paywalled in academic databases. Treat verification as having three levels, and apply them per-claim, not per-document:

| Level | What is confirmed | Use it for |
|---|---|---|
| **Existence** | Document number, title, date, chamber against a Tier 1 source | "X case was decided on Y date by Z Chamber" |
| **Content** | The retrieved text confirms the document holds, in substance, what the output claims | "The Chamber held that…" |
| **Paragraph** | The cited paragraph(s) contain the cited proposition | Any quotation, any paragraph-pinpoint |

If the output's claim is "Z Chamber held X in paragraph N", paragraph-level verification is required. If the claim is "the Chamber convicted on Y date", existence-level is enough. Match the verification to the claim.

When verification stops short of what the claim needs, either: (a) soften the claim to match what is verified, or (b) flag in the output that the paragraph-level pinpoint is provisional pending fetch.

## The fallback ladder

When the first attempt fails, work the ladder. Stop at the first level that gives you what the claim needs.

**1. icc-cpi.int direct fetch.** The case page or court-record URL.

**2. legal-tools.org.** The ICC Legal Tools Database; comprehensive, including older filings.

**3. Search-engine snippet from a Tier 1 domain.** `web_search` for the document number plus `icc-cpi.int` or `legal-tools.org`. If a result excerpts the relevant passage from a Tier 1 page, that excerpt is existence-verifying (the document exists and the search engine pulled real text from a Tier 1 URL) but generally not paragraph-verifying (snippets are short and not always paragraph-aligned).

**4. Court press release on icc-cpi.int.** ICC press releases summarise decisions in the Court's own voice. They establish existence and broad holding, not paragraph text.

**5. Authoritative secondary databases.** Oxford ORIL (opil.ouplaw.com) hosts the Court's own structured summaries; some academic databases mirror filings. Existence-verifying when the database cites the document number; not paragraph-verifying unless the source includes the full text.

**6. Ask the user for a URL.** The user may have direct access (e.g. through a Court-records portal) that the skill does not.

**Never** invent a paragraph number to fill a gap. If verification stops at level 4, the output stops at level-4 claims.

## Standard workflow

**Step 0 — Identify the document.** Before listing citations or fetching anything, read what is actually in front of you. If the user provides a file, open it and confirm its case, document number, date, chamber against the document's own header. If the user references a document by name ("the Lubanga reparations order"), confirm which one (there are several; appellate amendments matter). Identity errors propagate; one read at Step 0 prevents them.

**Step 1 — Build the citation list.** Before drafting, list every citation that will appear, with the proposition each will support and the source to verify against.

**Step 2 — Verify each citation.** Work the ladder for each. Capture: document number (with all suffixes), date as printed, chamber, title verbatim, paragraph numbers. Read the cited passage and confirm it supports the proposition. Record the verification level reached.

**Step 3 — Draft using verified material.** Match the verification level to the claim. Where partial, label.

**Step 4 — Self-audit.** Walk through every citation in the output. For each:
- Is it from project knowledge (foundational text) or a successful retrieval in this conversation?
- Does the cited proposition match what was retrieved?
- Is the verification level appropriate to the claim?

If any answer is no, fix it or remove the citation.

## Worked example

**User**: "Draft a paragraph on the Bemba effective control test under Article 28, with citations."

**Step 0 — identify the documents.** Bemba has two decisive judgments: Trial Chamber III conviction (21 March 2016, `ICC-01/05-01/08-3343`) and Appeals Chamber acquittal (8 June 2018, `ICC-01/05-01/08-3636-Red`). A memo on effective control that does not address the acquittal would be misleading. Both documents must be in the citation list.

**Step 1 — citation list.**
- Bemba TJ on the effective-control standard, expected paragraphs in the Article 28 / command-responsibility section.
- Bemba AJ on the set-aside and its reasoning.

**Step 2 — verify.**

```
web_fetch("https://www.icc-cpi.int/court-record/icc-01/05-01/08-3343")
```

If this succeeds: read the Article 28 section. Note the paragraphs articulating the standard. Verification: paragraph-level.

If this returns 403: fall back to legal-tools.org → search snippet → press release. Each gives a different verification level. The output must then match. If only the press release is reachable, the output can say "the Trial Chamber's articulation of effective control" but cannot quote or pinpoint to a paragraph.

Repeat for the AJ.

**Step 3 — draft.**

> Under Article 28(a) of the Rome Statute, a military commander incurs criminal responsibility for crimes committed by forces under his effective command and control. The Trial Chamber in *Bemba* articulated effective control as requiring the material ability to prevent or repress crimes [*Prosecutor v. Bemba*, Trial Chamber III, "Judgment pursuant to Article 74 of the Statute", ICC-01/05-01/08-3343, 21 March 2016, paras [verified]]. **This judgment was set aside on appeal.** The Appeals Chamber acquitted Mr Bemba by majority, finding that the Trial Chamber had erred on two grounds: convicting him for criminal acts that fell outside the scope of the confirmed charges, and in its assessment of the measures he took to prevent and repress crimes by the MLC contingent in the CAR [*Prosecutor v. Bemba*, Appeals Chamber, ICC-01/05-01/08-3636-Red, 8 June 2018, paras [verified]].

The `[verified]` placeholders are filled from the actual retrieved content. If retrieval stopped at level 4, the draft instead says: "The Trial Chamber articulated effective control as requiring the material ability to prevent or repress crimes (TJ paragraph references to be confirmed against the full text)."

**Step 4 — self-audit.**
- TJ exists, content matches, paragraphs verified: yes
- AJ exists, content matches, paragraphs verified: yes
- Article 28(a) used (not the non-statutory "28(1)"), matching the Statute's numbering: yes

## What this discipline buys and costs

**Cost:** two to five `web_fetch` calls per substantive citation. For a brief with twenty citations, this can be the bulk of the work.

**Buys:**
- No invented document numbers
- No misremembered holdings
- Honest verification status on each claim
- Secondary material clearly separable from Court findings
- Output that a downstream user can rely on as a starting point for real work

The skill exists because this discipline does not happen automatically. Following it under time pressure is the test.
