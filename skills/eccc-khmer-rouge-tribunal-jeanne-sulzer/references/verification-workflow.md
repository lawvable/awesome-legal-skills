# Verification workflow — ECCC

This reference is the operational step-by-step for verifying any ECCC citation before it appears in an output. It expands on `SKILL.md` § "Standard workflow".

## Before starting

Read the user's request twice. Identify:

1. Which Court? (Confirm it is the ECCC and not another tribunal — the conversation may move between bodies.)
2. Which case? (001 / 002 / 002/01 / 002/02 / 003 / 004)
3. Which document type? (closing order, indictment, judgment, decision, order, filing)
4. Which proposition does the citation support? (Be specific about what the citation is for. Citations exist to support claims; if you do not know what claim, you cannot judge whether the citation supports it.)

## The fallback ladder

Work each rung in order. Move down only when the rung above fails or returns insufficient information.

### Rung 1 — eccc.gov.kh

The Court's own website. For most documents this is the canonical source.

Approach:
- For known document numbers, attempt `web_fetch` to the case-page (e.g. `https://www.eccc.gov.kh/en/cases/case-002/trial-02`) and locate the document by number or title.
- For known judgments or major decisions, the URL pattern `https://www.eccc.gov.kh/sites/default/files/documents/courtdoc/[date]/[Filename].pdf` is common; the date appears in the path.
- For the Internal Rules and foundational texts, `https://www.eccc.gov.kh/en/about/legal-framework` and `https://www.eccc.gov.kh/en/document/legal/internal-rules`.

What "succeeds" looks like:
- A page or PDF that confirms document number, title, date, chamber.
- For paragraph-pinpoint claims, the actual paragraph text in the retrieved content.

What "partial" looks like:
- A page listing the document by title but without the document itself.
- A PDF whose first pages confirm document identity but whose later paragraphs (where the cited proposition lives) were not retrieved in the session.

In either partial case, label the verification level accordingly.

### Rung 2 — legal-tools.org

The ICC Legal Tools Database hosts ECCC documents. Useful when eccc.gov.kh is slow, blocked, or returns a 403. The document number and metadata should match eccc.gov.kh; where they diverge, the eccc.gov.kh version controls.

Approach:
- Search by case name and document number.
- Verify that the metadata (case, document number, date, chamber) matches the citation being verified.

### Rung 3 — OHCHR Cambodia / UN Rule of Law

`https://cambodia.ohchr.org/en/rule-of-law/eccc-decisions` and `https://www.un.org/ruleoflaw/`. These hosts have curated subsets of ECCC documents (in particular Tier 1 documents reposted by the UN). Useful when the eccc.gov.kh PDF is the same file but hosted on a UN domain that is more reliably retrievable.

### Rung 4 — Tier 2 summarisation

Academic articles, Cambridge Core International Legal Materials, Journal of International Criminal Justice, Cambodia Tribunal Monitor. These do not give you the document; they give you a summary of the document, with citations.

What this is good for:
- Confirming existence and broad content of a major decision.
- Finding the document number and date when the user has given you only a description.

What this is not good for:
- Paragraph-pinpoint citation. A Tier 2 source summarising paragraph 3445 of the Case 002/02 Trial Judgment is not itself paragraph 3445. The summarised proposition may be the same, but the citation rests on the Tier 2 source, not the Court's text.

### Rung 5 — ask the user

If the document is recent, redacted, or otherwise not retrievable, ask the user to provide a URL or copy. Do not invent. Do not approximate. The cost of asking is a single short message; the cost of fabricating is the user filing an inaccurate citation.

## Partial-verification handling

When verification is partial, the output must say so. Three conventions:

- **Existence-only verification, paragraph claim** — soften to a content-level claim, or move the paragraph reference out of the proposition and into a "see also" note that the user can verify before filing.
- **Content verified, no paragraph access** — keep the proposition; omit the paragraph pinpoint; note in the citation: "*(paragraph content not retrieved in this session — paragraph pinpoint omitted)*".
- **Existence-only verification, broad claim** — keep the broad claim ("the Trial Chamber addressed JCE in this judgment") but not specifics ("the Trial Chamber held that JCE III is not customary international law"). Use only the level of specificity the verification supports.

A worked example is in `../examples/example-verification.md`.

## Language discipline

ECCC documents exist in three official languages: English, Khmer (ខ្មែរ), and French. Many decisions are issued in English only. Some foundational texts and Cambodian-law components exist primarily in Khmer.

When verifying:
- For an English citation pointing at an English-language document, English suffices.
- For a citation that depends on the original Cambodian-law instrument (e.g. the 1956 Penal Code, the unamended Establishment Law), the Khmer version controls. If the output rests on the English translation, flag that.
- For divergences between English and French versions of the same Court document (rare but possible), note the divergence and ask the user which version is being relied on.

## Redaction discipline

ECCC frequently issues confidential and public-redacted versions of the same document. When verifying a citation:

- Identify which version the citation rests on (the document number suffix, if any, tells you).
- Prefer the public-redacted version if it contains the cited proposition.
- If the citation rests on confidential content not present in the public version, the output must say so. The user may have legitimate access to confidential filings; the model does not, and citing confidential paragraph numbers that the model cannot see is fabrication.

## When you have done it right

A verified citation, by the time it appears in an output, traces to:

- A foundational text in project knowledge (if it is the UN-Cambodia Agreement, ECCC Law, or Internal Rules), OR
- A `web_fetch` to a Tier 1 source in this conversation, with the relevant content visible in the retrieval, OR
- A `web_fetch` to a Tier 2 source labelled as such, with the verification level honestly stated.

Anything else is not yet a citation.

