# Authoritative ICC sources

Sources that may be cited, and how to access them. Read this whenever verifying a citation or deciding whether a source is authoritative.

## Tier 1 — primary, authoritative

### icc-cpi.int — the official Court website

Authoritative for everything the Court itself issues.

Entry points:
- Cases: `https://www.icc-cpi.int/cases`
- Situations: `https://www.icc-cpi.int/situations`
- Court records: `https://www.icc-cpi.int/court-record/icc-[situation]/[case]-[filing]`
- News and statements: `https://www.icc-cpi.int/news`
- OTP statements: filter the news page to OTP-issued items.

**Fetch reliability.** Direct `web_fetch` on icc-cpi.int returns 403 in a non-trivial fraction of requests. This is structural — not a one-off. When it happens, do *not* abandon the icc-cpi.int citation; the document still exists and is authoritative. Instead:

1. Search for the document number plus `icc-cpi.int`. The Court's own press release is usually the first hit and confirms document number, title, date, chamber, and holding-in-substance — that is, verification levels A and B (see `verification-workflow.md`).
2. If a paragraph-specific (level C) citation is needed, try Legal Tools (below) for the full text.
3. Search-result snippets from the `icc-cpi.int` domain are themselves Court content and can be cited at level A/B with the disclosure that the full PDF was not retrievable.

When the fetch *does* succeed, capture from the official page:
- Document number, exactly as printed, including suffix (`-Red`, `-Conf-Exp`, `-Anx1`, `-tENG`).
- Date in the form printed by the Court.
- Chamber.
- Title — verbatim.
- Paragraph(s) you plan to cite.

### legal-tools.org — ICC Legal Tools Database

Comprehensive collection of ICC documents and related international criminal law materials. Usually the fastest path to a full text when icc-cpi.int blocks. Entry: `https://www.legal-tools.org/`; search: `https://www.legal-tools.org/search`.

Documents have unique LTD identifiers (e.g. `LTD-12345`). Prefer the ICC document number for citation; you may include the Legal Tools URL as a retrievability aid.

### asp.icc-cpi.int — Assembly of States Parties

Authoritative for:
- ASP resolutions
- Statute amendments (Kampala and subsequent)
- Budget and audit documents
- Independent expert review reports

Entry: `https://asp.icc-cpi.int/`

## Tier 2 — secondary (must be labelled)

Useful for context. Never authoritative on what the Court has said. Always in a clearly separate part of the output (e.g. a "Context" section, or footnotes plainly marked as secondary).

- **Coalition for the ICC** (CICC) — civil-society coalition
- **Human Rights Watch**, **Amnesty International** — NGO reports
- **UN bodies** — Panels of Experts, Commissions of Inquiry, FFMs, OHCHR. Authoritative on facts they investigate; never on ICC findings.
- **Academic journals** — JICJ, LJIL, EJIL, AJIL, ICLR; OUP commentaries (Schabas, Triffterer/Ambos)
- **Mainstream news** — Reuters, AP, AFP, BBC, major broadsheets
- **Specialist journalism** — IJ-Monitor, Justice Info, Opinio Juris
- **OUP ORIL** (`opil.ouplaw.com`) — editorially curated case entries with the Court's own document references; useful for confirming citation details when icc-cpi.int isn't reachable.

When citing secondary material:
- Format that cannot be confused with a Court document.
- Separate part of the output.
- Never used to establish what the Court held. Used only for context, background, or the wider debate.

## Not authoritative — do not cite

- Wikipedia
- Personal blogs that don't quote primary documents (if a blog quotes a Court document, cite the Court document)
- Social media posts
- AI-generated summaries from any tool
- Party press releases (party submission, not Court finding)
- Trial-monitoring summaries as a substitute for the underlying transcript or decision

## Practical notes

- **Redactions.** Cite only the public (`-Red`) version unless the user lawfully has the confidential version. Never cite a confidential filing from memory.
- **Translations.** ICC working languages are English and French. Note `-tENG` / `-tFRA` where translation status matters.
- **Corrigenda.** Documents are sometimes reissued with `-Corr` / `-Corr2` suffixes. Cite the corrected version.
- **Under seal / ex parte.** Treat as unverifiable for any output.

## Fallback ladder when icc-cpi.int returns 403

In order:

1. `web_search` for `[document number] icc-cpi.int` → ICC press release (Tier 1A; supports verification levels A and B).
2. `web_search` for `[document number] legal-tools.org` → full text (Tier 1B; supports level C if the document is retrievable).
3. `web_fetch` against legal-tools.org URLs that appear in search results.
4. `web_search` for the document on OUP ORIL or in a Court-published "Summary of the Judgment" PDF (Tier 1 / Tier 2 mix; supports levels A and B).
5. If none of the above produces enough, report the level achieved and the gap — do not invent.

When following this ladder, document in the output what was actually checked. The user benefits more from "verified at level B via the Court's press release; full text not retrieved" than from a citation that looks complete but isn't.
