---
name: "eccc-jeanne-sulzer"
description: "Verification-first methodology for the ECCC (Khmer Rouge Tribunal). Every citation is verified against eccc.gov.kh, the ECCC archive or legal-tools.org. Covers Case File numbering, the 001/002/002-01/002-02 structure, the genocide findings against the Cham and the Vietnamese, and the Internal Rules revision discipline. Research aid, not legal advice. Part of the open-source \"Skills for International Justice\" library — methodology: github.com/jeannesulzer/international-criminal-tribunals-skills"
metadata:
  author: "Jeanne Sulzer"
  license: "cc-by-4.0"
  version: "2026-06-09"
---

# ECCC — Extraordinary Chambers in the Courts of Cambodia

This skill governs every output that touches the Extraordinary Chambers in the Courts of Cambodia. The discipline is simple and the reason for it is concrete: ECCC document numbers are exact, the procedural lineage between filings matters, dates and chambers matter, and a confident-sounding but invented citation in a real filing creates real problems — including for the Cambodian victims and civil parties whose participation was, by design, the heart of these proceedings.

## The discipline in one paragraph

For any case-specific document — decision, judgment, closing order, indictment, filing, OCP submission — verify before citing. "Verify" means `web_fetch` (or equivalent retrieval) to eccc.gov.kh or legal-tools.org in the current conversation. Foundational texts in project knowledge (ECCC Law as amended, UN-Cambodia Agreement, Internal Rules) are the exception; they may be cited directly. Nothing else.

## Verification is gradient, not binary

In practice, `web_fetch` to eccc.gov.kh sometimes succeeds, sometimes returns a page that confirms a document exists but does not surface its paragraph text, and sometimes returns the document only in Khmer or French rather than English. Honest outputs reflect this. Three levels:

- **Existence verified.** Document number, title, date, chamber confirmed against an authoritative source. The Court issued the document, and it is the document the citation names. Sufficient for "X case was decided on Y date by Z Chamber" claims.
- **Content verified.** The fetched text confirms the document says, in substance, what the output claims it says. Sufficient for "the Chamber held that…" claims.
- **Paragraph verified.** The specific cited paragraph(s) contain the cited proposition. Required for any quotation and for any paragraph-pinpoint citation.

Label the level when relevant. Do not silently downgrade — a "Trial Chamber held X" claim that is only existence-verified is not honest if the output doesn't say so. See `references/verification-workflow.md`.

## Standard workflow

**Step 0 — Identify the document(s).** Before anything else, read what is actually in front of you. If the user provides a file, open it and confirm its case, document number, date, chamber. If the user references a document by name ("the Duch appeal judgment", "the Case 002/02 trial judgment"), confirm which document they mean. ECCC severance and renumbering make this especially important: a citation to "the Case 002 trial judgment" is ambiguous between 002/01 and 002/02. Identity errors propagate; the cost of catching them at Step 0 is one read.

**Step 1 — Plan citations.** List every citation that will appear in the output. For each, note the document, the proposition it will support, and the source to verify against.

**Step 2 — Verify, with the fallback ladder.** For each case-specific citation, work the ladder in `references/verification-workflow.md`: eccc.gov.kh → legal-tools.org → cambodia.ohchr.org → search snippet from a Tier 1 domain → academic/Court-record secondary → ask the user for a URL. Capture document number, date, chamber, title, and paragraph numbers. Read the cited passage and confirm it supports the proposition.

**Step 3 — Draft using verified material.** Use the citation format in `references/citation-format.md`. Where verification is partial, say so in the output.

**Step 4 — Self-audit.** Each citation must trace to project knowledge (foundational text) or a successful retrieval in this conversation, with verification level appropriate to the claim. If not, the citation comes out or the claim is softened to what the verification actually supports.

## Foundational texts (cite from project knowledge when present)

- **Agreement between the United Nations and the Royal Government of Cambodia concerning the Prosecution under Cambodian Law of Crimes Committed during the Period of Democratic Kampuchea** (6 June 2003) — "UN-Cambodia Agreement"
- **Addendum to the UN-RGC Agreement on the Transitional Arrangements and the Completion of Work of the Extraordinary Chambers** (entered into force December 2021) — confers the ECCC's residual functions; the residual phase commenced 1 January 2023
- **Law on the Establishment of the Extraordinary Chambers in the Courts of Cambodia for the Prosecution of Crimes Committed during the Period of Democratic Kampuchea** (NS/RKM/0801/12, 10 August 2001; as amended by NS/RKM/1004/006, 27 October 2004) — "ECCC Law" or "ECCC Establishment Law"
- **Internal Rules of the Extraordinary Chambers in the Courts of Cambodia** — currently Rev. 10 (27 October 2022); earlier revisions remain cited in older decisions

If not in project knowledge, retrieve from eccc.gov.kh/en/about/legal-framework before citing. For the Internal Rules, the revision number matters: a 2010 decision cites the Internal Rules then in force (likely Rev. 5 or 6), not the current revision. Cross-check which revision was in force at the time of the cited decision. See `references/foundational-texts.md`.

## The Court's own jurisprudence digest

The ECCC has published an official two-volume *Guide to the Extraordinary Chambers in the Courts of Cambodia*:

- **Volume 1: Establishment, Operations and Cases** — the institutional and procedural guide
- **Volume 2: Jurisprudence** — a comprehensive catalogue of the ECCC's jurisprudence organised by topic (jurisdiction; crimes; individual criminal responsibility; fair trial rights; procedure; sentencing; Civil Party action; administration of justice)

Volume 2 is the canonical roadmap for finding the Chamber that first established a given principle. **Use it as a starting point**, then verify the specific decision and paragraph through the workflow in `references/verification-workflow.md`. The Guide is Tier 1 (Court-issued) but is not a substitute for the underlying decision: a Guide entry pointing at a Trial Chamber paragraph is the map, not the territory.

## Source hierarchy

**Tier 1 (authoritative):** eccc.gov.kh (including the official two-volume *Guide to the ECCC*, the *Lexicon*, the *Bibliography*, and the *Jurisprudence* page), archive.eccc.gov.kh (the official ECCC Archive, over 2 million pages), legal-tools.org. Always citable.
**Tier 2 (secondary, must be labelled):** OHCHR Cambodia (`cambodia.ohchr.org`) — including the *Annotated Cambodian Code of Criminal Procedure* (2nd ed. 2015) which annotates the Cambodian Code with ECCC jurisprudence; UN Rule of Law (`un.org/ruleoflaw`); Cambodia Tribunal Monitor; Documentation Center of Cambodia (DC-Cam); Ciorciari & Heindel, *Hybrid Justice* (University of Michigan Press, 2014, open access); Jørgensen, *The Elgar Companion to the ECCC* (2018); academic journals. Never authoritative on Court findings. Always in a clearly separate part of the output.
**Never authoritative:** Wikipedia, social media, AI summaries, blogs.

See `references/authoritative-sources.md`.

## Citation format

ECCC citations are precise and structurally different from ICC citations. Two pieces matter for every case-specific citation:

1. **The Case File Number** — the file under which the document was registered, in the form `[Case Number]/[Date of Introductory Submission, DD-MM-YYYY]/ECCC/[Chamber or Office]`. Example: `002/19-09-2007/ECCC/TC` (Case 002, introductory submission of 19 September 2007, before the Trial Chamber).
2. **The Document Number** — a short alphanumeric identifier indicating procedural phase and sequence within the case file. Letter prefixes encode the phase:
   - **A** — Co-Prosecutors' filings (e.g. Introductory Submission)
   - **B** — Case-management documents in the early phase
   - **C** — OCIJ investigation-phase filings and orders
   - **D** — OCIJ Closing Orders and final investigation documents
   - **E** — Trial Chamber filings, decisions, and judgments
   - **F** — Supreme Court Chamber filings, decisions, and judgments
   
   Sub-numbering uses slashes: `E163/5/1/13` is a sub-document within filing E163 of the Trial Chamber phase.

Decisions cite by case file number, document number, chamber, title, date, paragraph.

Short forms for the most common categories:
- **ECCC Law**: `ECCC Law, Article 5` (war crimes), `ECCC Law, Article 6` (genocide), `ECCC Law, Article 4` (crimes against humanity — but check current numbering as amendments renumber)
- **Internal Rules**: `Internal Rules, Rule 23` (civil parties) — and **always state the revision in force** at the date of the cited application: `Internal Rules (Rev. 9), Rule 23 bis(1)`
- **UN-Cambodia Agreement**: `UN-Cambodia Agreement, Article 9` (jurisdiction)
- **Decisions**: `Prosecutor v. [Accused] (Case [Number]), [Chamber], "[Title]", [Document Number], [Date], para. [X]`

See `references/citation-format.md` for the full guide, document-number anatomy, accused-name conventions (ECCC uses SURNAME in capitals first, e.g. KAING Guek Eav), and the handling of severance citations between Case 002/01 and 002/02.

## Audit mode depends on document type

When the user supplies a document, the right audit task depends on what kind of document it is:

- **Working drafts** (briefs, memos, submissions in progress): audit citations for accuracy. Existence and proposition both need verification.
- **Final Court records** (judgments, closing orders, decisions the Chambers have issued): citations within the document are by definition Court-issued. The audit task shifts to inventorying which referenced documents downstream work will need to fetch, distinguishing public from confidential versions (ECCC frequently issues public-redacted, confidential, and strictly-confidential versions of the same filing), and flagging anything internally inconsistent.

In either mode, Step 0 (identify the document) comes first. Do not start auditing citations until the document's identity — case, document number, date, chamber — is confirmed against the document itself.

See `examples/example-audit.md` for both modes worked through.

## Substantive doctrine — pointers

The skill does not encode doctrine line by line; the foundational texts and the ECCC's own judgments do that. For starting points (subject-matter jurisdiction is set by ECCC Law Articles 3 new to 8):

- **Genocide** → ECCC Law, Article 4 (referring to the 1948 Genocide Convention); see Case 002/02 trial and appeal judgments on genocide against the Cham and the Vietnamese
- **Crimes against humanity** → ECCC Law, Article 5; see Duch trial judgment and Case 002/01 and 002/02 judgments on persecution, extermination, enslavement, deportation, imprisonment, torture, rape (as the underlying act of "other inhumane acts" in older decisions; later expressly), forced marriage, enforced disappearance, other inhumane acts
- **Grave breaches of the 1949 Geneva Conventions** → ECCC Law, Article 6 (limited to the armed conflict with Vietnam)
- **Domestic crimes under the 1956 Cambodian Penal Code** → ECCC Law, Article 3 new (homicide, torture, religious persecution)
- **Destruction of cultural property under the 1954 Hague Convention** → ECCC Law, Article 7 (in practice no Case contained specific charges under Article 7)
- **Crimes against internationally protected persons under the 1961 Vienna Convention on Diplomatic Relations** → ECCC Law, Article 8 (in practice no Case contained specific charges under Article 8)
- **Modes of liability** → ECCC Law, Article 29 new: planning, instigating, ordering, committing, aiding and abetting; superior responsibility. **Joint Criminal Enterprise (JCE)** is not listed in Article 29 new; the ECCC's own *Guide to the ECCC, Volume 2: Jurisprudence* records that JCE was "judicially recognised as a form of commission" at the ECCC. The applicability of JCE — including the contested JCE III — was the subject of major rulings: see in particular the Pre-Trial Chamber's 2010 decision in Case 002 on JCE, the Case 002/01 Trial Judgment, and the Case 002/01 Appeal Judgment.
- **Civil party participation and reparations** → Internal Rules, Rules 23, 23 bis, 23 ter, 23 quater, and the civil party reparations framework articulated across the Case 001, 002/01 and 002/02 judgments and amended Internal Rules

For case-law interpretation of any of these, follow the workflow.

## Sensitive contexts

ECCC matters involve genocide (against the Cham, against the Vietnamese), forced marriage and gender-based violence, the killings at S-21 / Tuol Sleng, mass killings at execution sites, forced movement of population, forced labour, and the deaths of approximately 1.7 to 2.2 million people during the Democratic Kampuchea period (17 April 1975 – 6 January 1979). Survivors, civil parties, and the families of victims are alive and continue to engage with the Court's record. Use the language the Court itself uses. Avoid sensational framing. Anonymise civil party names unless the user confirms they are public (e.g. as protected identities have been used in many filings; the public versions of judgments are the safer source).

## What this skill is not

- Not legal advice. Outputs are research and drafting aids.
- Not a substitute for the Court's own filings.
- Not exhaustive — where the foundational text or a verified decision is silent, say so.
- Not a substitute for the Khmer-language versions of ECCC documents, which are the original-language versions for the Cambodian-law components. Where the Khmer and English diverge, the question must be raised with the user.

## Reference files

- `references/authoritative-sources.md` — source hierarchy and URL patterns
- `references/citation-format.md` — citation rules with worked examples, including document-number anatomy, accused-name conventions, and the canonical Court-issued reference table of frequently cited authorities (Closing Orders, Trial Judgments, Appeal Judgments per Case)
- `references/case-documents-quick-reference.md` — quick lookup table of principal documents per Case with case-file numbers, status notes (deceased accused, severed proceedings, residual phase), and chamber abbreviations
- `references/verification-workflow.md` — step-by-step procedure, fallback ladder, partial-verification handling
- `references/foundational-texts.md` — the four foundational instruments (UN-RGC Agreement, Addendum, ECCC Law, Internal Rules) and how to work with them
- `references/jurisprudence-map.md` — topic-by-topic map of the ECCC's principal holdings, built from the Court's own *Guide to the ECCC, Volume 2: Jurisprudence*
- `examples/example-verification.md` — verifying a single citation end-to-end
- `examples/example-audit.md` — auditing user-supplied documents (both working drafts and finalised Court records)


