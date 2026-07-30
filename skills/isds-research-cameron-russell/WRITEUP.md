# Design notes on building a RAG-based ISDS research tool for public databases

*Cameron Russell (ccrnyc) · July 2026 · v1.0.0 · AGPL-3.0-only*

Investment arbitration decisions are largely hosted in publicly accessible databases, but legal research tools to search those databases are gated behind expensive subscriptions. I could not find any free, open-source and reliable tool to conduct investment arbitration research. So I built one. 

## 1. The premise: reliability, compliance, and honesty by design

Legal research tools built on large language models fail in two characteristic ways. They **hallucinate** — inventing holdings, paragraph numbers, and even cases — and they **overreach on sources**, scraping databases whose terms don't permit it and then obscuring where any given sentence came from.

This skill treats both as design problems, not prompt problems:

- **No recall.** Every holding, quote, and pinpoint citation must come from text retrieved *in the current session*. If it isn't in the retrieved text, the answer says "not found in the retrieved document." Statements from the model's general knowledge are permitted only when labeled as such, with their basis stated.
- **No corpus.** The tool holds no scraped award database. It retrieves the specific primary document a question needs, on demand, from the institution that published it (ICSID, PCA), under that institution's own terms — attributed, never republished, never bulk-downloaded.
- **No pretend completeness.** Questions are classified by how completely the tool can answer them — from single-document questions (fully answerable) to full-corpus analytics ("most-cited case on X"), which the tool declares it *cannot* answer completely and points to the databases built for that job.
- **Per-source rules, not one policy.** Each source has its own negotiated position, recorded in SKILL.md: ICSID and PCA as primary text under their terms; UNCTAD's ISDS Navigator as discovery metadata via its official Excel export (never scraped, never redistributed — each user downloads their own copy); italaw only as a last-resort, per-document, human-confirmed fallback.

## 2. Architecture

The pipeline is diagrammed in the [README](README.md#design-the-rag-pipeline). Its distinctive machinery is less the retrieval than the *refusal paths*:

- **Identify → CONFIRM.** A case page can list dozens of documents. The tool lists them all, selects by title + date + proceeding, then confirms the choice against the document's own first pages before relying on it. A mismatch stops the run.
- **The language interview.** Awards are often published only in Spanish or French. Language is treated as an attribute, not a filter: the tool never silently substitutes a translation — it stops, reports which languages exist, and asks.
- **A five-rung fallback ladder** for documents the institution's page doesn't yield (JS-rendered pages, blocked hosts, delisted awards), ending in an honest terminal state: the *unretrieved lead*, disclosed in the memo, never filled from memory.
- **Flags that travel.** Anything not grounded in retrieved primary text carries its label into the deliverable itself — `[LIVE / secondary …]` tags on unverified status items, basis labels on general-knowledge statements, a mandatory data-freshness footer on every enumeration.
- **A Conflict rule.** When two sources disagree — a date, an amount, an article number, an attributed quotation — the tool surfaces both values with their source classes and marks the conflict unresolved unless a retrieved primary document settles it. Section 4 below shows why this rule earns its keep.
- **Paragraph-aware extraction** that survives real-world PDFs: per-document marker-convention detection (`154.` vs. bracketed `[324]`), section-relative citations when numbering restarts per Part/Chapter, and a rasterize-and-read guard for PDFs whose paragraph numbers exist only visually.

## 3. How it was evaluated

The skill went through a 10-item evaluation designed to hit every feature and failure mode: language policy on a Spanish-only award, a blocked-host path requiring user-supplied files, a delisted award reachable only through companion-decision grounding, staleness routing, chart grounding, a planted date conflict, and enumeration questions with exact-count pass conditions.

The pipeline separated roles to keep grading honest: **one model executed each item unaided** (minimal prompt: the question, the skill path, a run folder), **a different model graded** each run against a 12-dimension rubric with a source inventory, and **every grader finding was adjudicated** by independent recomputation before any grade became final.

Results (post-adjudication):

| Item | Subject | Grade |
|------|---------|-------|
| 01 | Metalclad — FET/transparency + set-aside trap | A− |
| 02 | Iberdrola — language policy (aided) | A− |
| 03 | Saluka/Methanex — PCA path (aided) | A− |
| 04 | African-states enumeration chart | A− |
| 05 | Arbitrator / most-cited split question | A− |
| 06 | ConocoPhillips — rectification | A |
| 07 | Eiser — delisted award | B+ |
| 08 | Rockhopper — staleness routing | B+ |
| 09 | Charanne — SCC forum honesty | A− |
| 10 | CMS — docket-metadata chart | A− |

**Overall: A−.** Across the set: zero hallucinated citations, zero barred-source fetches, zero pretend-retrievals. The adjudication pipeline sustained 48 of 48 grader findings with 0 grader errors. The two B+ runs share one signature — the executor stopped one verification step short of what the record allowed — a verification-depth issue, never a grounding-integrity one. Every skill gap the eval surfaced was fixed and committed before release; several of the failure-mode guards in SKILL.md are direct descendants of eval findings.

*(A "Ready" verdict was also obtained from the independent Claude for Legal skill-design QA against the Legal Skill Design Framework — thirteen design parameters plus legal-specific failure modes — as the pre-listing gate.)*

## 4. Sidebar: *Saluka's* foundational "police powers" doctrine is premised on a holding that the *Methanex* tribunal never made

The strongest argument for the Conflict rule arrived uninvited, during eval item 03. That eval surfaced a misattributed quotation that was relied on in a foundational case addressing police powers - an error that appears to have gone largely unnoticed and unremarked in investment arbitration literature - thus demonstrating the reliability and value of this tool.

The *Saluka v. Czech Republic* Partial Award (PCA, 17 March 2006) is a leading authority on the police-powers doctrine. At ¶262, the tribunal quotes what it presents as the words of the *Methanex v. USA* Final Award (3 August 2005), decided seven months earlier:

> "As the tribunal in *Methanex Corp. v. USA* said recently in its final award, '[i]t is a principle of customary international law that, where economic injury results from a bona fide regulation within the police powers of a State, compensation is not required.'"

Footnote 12 gives the cite: *Methanex … Final Award, 3 August 2005, 44 ILM 1343, para. 410*.

**That sentence does not appear in the official Methanex Final Award.** A full-text search of the 307-page award (retrieved from the respondent State's own archive) finds no such sentence — and the phrase "police power(s)" appears *nowhere in the award at all*. The four occurrences of "police" in the entire text all refer to literal police forces. Methanex's actual holding is worded differently and adds a qualifier Saluka's version drops: a non-discriminatory regulation for a public purpose enacted with due process is "not deemed expropriatory and compensable **unless specific commitments** had been given" (Part IV, Ch. D ¶7).

Two caveats, as per the tool's requirements. First, Saluka cites the ILM reprint — a different edition with its own continuous paragraph numbering that was not retrieved — so the finding is that the quoted sentence is absent from the *official* text, not a claim about what any reprint contains; the edition-independent core (no "police powers" language anywhere in Methanex) is robust either way. Second, the run did not silently resolve the conflict: the memo surfaced both sources, their classes, and the discrepancy as unresolved — which is precisely what the Conflict rule is for. The executor flagged it; the independent grader re-verified it from scratch; the adjudication sustained it.

The doctrinal irony writes itself: *Saluka*, the award that consolidated the modern "police powers" exception, appears to have done so partly by re-labeling — in quotation marks — a holding that never used the term. Twenty years of subsequent citation practice have not, to our knowledge, made this discrepancy common knowledge (and a quick search reveals that some practitioners continue to propagate Saluka's phantom quote and citation). A retrieval-grounded tool noticed it on its third eval item, because it is structurally incapable of assuming a quotation exists without looking.

## 5. What this tool is not

It is not a database (no full-text search over a corpus), not a citator, not an analytics engine, and not legal advice. It will decline, in so many words, to name "the most-cited case" on anything — and will tell you which subscription databases can. Those limits are design, not shortfall: the tool's one job is research you can *verify* — every claim either pinned to retrieved primary text or labeled with what it actually rests on.

---

*Source: primary documents referenced above were retrieved from the publishing institutions (ICSID; PCA; the respondent State's archive for Methanex) under their respective terms. For research only; not legal advice. Verify against the official primary sources.*
