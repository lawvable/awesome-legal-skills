# General Legal Lexicon (Base Layer)

English legal terminology and conventions that apply to **all** legal documents regardless of
source language or specific domain. This file is always loaded. In addition, one or more
domain-specific lexicons should be loaded based on the document type:

- `finance-banking.md` — Facility agreements, security documents, pledges, mortgages, bonds, loans, banking regulation, syndicated facilities, AML/KYC, sanctions, Basel
- `corporate-ma-jv.md` — SPAs, SHAs, shareholder loans, transaction deeds, disclosure letters; JVAs, consortium agreements, co-investment agreements; board resolutions, board minutes, shareholder resolutions; powers of attorney and proxies
- `ndas-service-agreements.md` — Non-disclosure agreements, confidentiality agreements; service agreements, SLAs, outsourcing, consultancy, managed services
- `energy-infrastructure.md` — EPC/turnkey contracts, construction agreements, O&M agreements, BOP; PPAs, grid connection, offtake, concessions, renewables, tariffs
- `ip-it-technology.md` — Patents, trade marks, copyright, licensing, R&D, technology transfer; SaaS agreements, software licences, cloud services, development agreements
- `public-procurement.md` — Tenders, concessions, PPP/PFI, state aid, EU procurement directives
- `real-estate.md` — Leases, property transfers, easements, zoning, conveyancing
- `litigation-settlement.md` — Settlement agreements, releases, waivers, dispute resolution, arbitration, civil/administrative/criminal procedure
- `transport-and-insurance.md` — Charter parties, bills of lading, Incoterms, freight, maritime law; insurance policies, reinsurance treaties, claims, subrogation, Lloyd's market
- `trading-capital-markets.md` — ISDA, derivatives, repo, securities lending, EMIR, MiFID
- `consumer-retail.md` — Terms and conditions, franchise, distribution, agency, consumer protection
- `employment.md` — Employment contracts, non-competes, severance, collective bargaining, secondment
- `taxes.md` — CIT, PIT, VAT, transfer pricing, DAC6, Pillar Two, M&A tax
- `permitting-environmental.md` — EIA, IED/IPPC, REACH, CLP, waste, water, soil, climate, CSRD/CSDDD

If a document straddles multiple domains (e.g., an NDA as part of an M&A process), load
both relevant lexicons.

**Note on per-language sub-lexicons.** The English-reference lexicons listed above remain
two distinct files for `finance-banking.md` and `trading-capital-markets.md`. In the
per-language sub-lexicons (`sub-lexicons/<language>-<domain>.md`) the two domains are
consolidated into a single file, `<language>-finance-banking.md`, because the source-side
vocabulary overlaps heavily. So when working on a capital-markets document: load both
reference files, but only the single per-language `<language>-finance-banking.md`.

## Sub-lexicons

Language-specific sub-lexicons (mapping source-language terms to the English terms in this
file) are stored at the skill root as `sub-lexicons/<language>-<domain>.md` (e.g.,
`sub-lexicons/italian-real-estate.md`). If a sub-lexicon exists for the source language,
load it alongside this file. See the main SKILL.md for sub-lexicon instructions.

---

## Contract Formation and General Concepts

| Correct English term | Usage / meaning | Avoid |
|---|---|---|
| enter into (an agreement) | Standard verb for forming a contract | "stipulate", "constitute" |
| create / grant (a right, a security interest) | Standard verb for establishing rights or security interests. Note: "establish a security interest" is also acceptable. | "constitute (a right)" (calque) |
| representations and warranties | Standard formulation for statements of fact and promises by a party | "declarations and warranties", "declarations and guarantees" |
| undertakings (UK finance/LMA) / covenants (M&A/US) / obligations (FIDIC/construction) | Contractual promises a party commits to. Use the term that matches the document's domain and drafting tradition. | — |
| consideration | The thing of value exchanged; a common law concept. Include only where the English-law concept applies. | — |
| conditions precedent | Conditions that must be satisfied before obligations become effective | "suspensive conditions" (civil law calque) |
| recitals | The introductory "whereas" section of a contract | "preambles" or "premises" as clause headings |
| now, therefore, | Standard bridge between recitals and operative provisions | "having established all the above" |

## Efforts and Endeavours Standard

This is one of the most critical translation concepts. English law distinguishes between
levels of effort, and the choice materially changes the obligation:

| Standard | Meaning | Notes |
|---|---|---|
| **best efforts** | Highest standard — must do everything in one's power, even at significant cost or inconvenience | UK alternative: "best endeavours". Default to "best efforts". |
| **all reasonable efforts** | Intermediate — must explore and exhaust all reasonable courses of action | UK alternative: "all reasonable endeavours". Default to "all reasonable efforts". |
| **reasonable efforts** | Lowest standard — must take one reasonable course of action, not necessarily exhaust all options | UK alternative: "reasonable endeavours". Default to "reasonable efforts". |

Civil law systems typically have a single, undifferentiated standard of care (e.g., the
standard of a reasonable person, or the "diligent businessman" standard). When translating
such concepts, determine which English standard is closest based on the context and the
weight of the obligation. If in doubt, use "reasonable efforts" (the least onerous standard)
and flag it for the reviewing lawyer.

When the user requests US English output, use "efforts" throughout. When the user requests
UK English output, still default to "efforts" but note that "endeavours" is the traditional
UK alternative. The documents produced should be consistent — do not mix "efforts" and
"endeavours" in the same document.

## Boilerplate / Miscellaneous Provisions

| Correct English term | Usage / meaning | Avoid |
|---|---|---|
| miscellaneous | Preferred heading for general/boilerplate provisions (UK). "General Provisions" or "General" is also acceptable. | "final provisions" |
| governing law and jurisdiction | Standard heading for choice of law and dispute forum. May be split into separate "Governing Law" and "Jurisdiction" or "Dispute Resolution" clauses. | "applicable law and competent court" (calque) |
| dispute resolution | Standard heading when a contract includes arbitration, mediation, or expert determination provisions alongside or instead of court jurisdiction | — |
| service of process | Mechanism for delivering legal documents to a party | "election of domicile" (civil law calque) |
| severability | Clause dealing with partial invalidity of provisions | "partial invalidity", "partial nullity" as heading |
| amendment (UK) / modification (US) | Changes to the agreement. Default to "amendment" for UK-style drafting. | — |
| notices | Clause specifying how formal communications are delivered | "communications", "contact details" as heading |
| waiver | Relinquishment of a right; distinct from "release" or "discharge" under English law | — |
| assignment | Transfer of rights/obligations under the agreement to a third party | — |
| successors and assigns | Standard phrase for who is bound after the original parties | "successors and those who acquired title" |
| entire agreement | Clause stating the contract is the complete agreement between the parties | — |
| counterpart | Each signed copy of the agreement | "exemplar", "specimen" |
| forms part of (this Agreement) | Standard way to say an annex or schedule is incorporated | "integral part" (calque) |
| order of precedence | Clause establishing which document prevails in case of conflict | "conflict of provisions", "prevalence" |
| freedom from encumbrances | Confirmation that assets are free from third-party rights | "absence of charges" |

## Common Clause Headings and Concepts

These appear across virtually all contract types:

| Correct English term | Usage / meaning | Avoid |
|---|---|---|
| term and termination | Standard heading for the clause governing duration and ending of the contract | "duration and withdrawal" |
| force majeure | **Canonical definition** — unforeseeable events beyond the parties' control (natural disaster, war, pandemic, terrorism, government action) excusing performance where expressly provided for in the contract. English common law does not imply a force-majeure doctrine; it depends entirely on the contractual clause. Retain the French term "force majeure" — treated as an English legal term of art. Domain variants: in insurance and transport, usually narrower and often listed exhaustively; in energy/EPC, typically paired with a relief-event regime (FIDIC); in IT/SaaS, often excludes economic hardship and industrial action. | "act of God" (archaic, and narrower — limited to natural forces); "unforeseeable event" (imprecise); frustration (distinct English common-law doctrine applying in absence of force-majeure clause) |
| limitation of liability | Contractual cap or exclusion on a party's liability | "limitation of damages" |
| liability cap | The maximum aggregate liability under the agreement | — |
| indemnity (UK) / indemnification (US) | An obligation to compensate for loss. Default to "indemnity" for UK drafting. | — |
| confidentiality | Standard heading for the clause imposing secrecy obligations | "secrecy", "non-disclosure" (as a clause heading within a broader agreement) |
| without prejudice | Reservation of rights; does not waive any right not expressly waived | — |
| notwithstanding | Override language — "notwithstanding Clause X" means "despite what Clause X says" | — |
| subject to | Conditional language — "subject to Clause X" means "conditional on / qualified by Clause X" | — |
| material adverse change (MAC) / material adverse effect (MAE) | A significant negative change or effect on the business, assets, or financial condition | — |

## Good Faith

"Good faith" has very different weight in common law and civil law jurisdictions. In English
law, there is no general implied duty of good faith (though this is evolving, and specific
duties of good faith can be contractually agreed). In most civil law systems, good faith is a
pervasive and mandatory principle. When translating a civil law "good faith" clause, render it
faithfully as "good faith" — but be aware that an English lawyer reading the translation may
interpret it differently from a civil law lawyer. Do not add or remove good faith obligations
that are not in the source text.

## Persons, Entities and Roles

| Correct English term | Usage / meaning | Avoid |
|---|---|---|
| person | Includes both natural persons and legal entities unless otherwise defined | "subject" (calque) |
| third party | Any person who is not a party to the agreement | — |
| competent authority | Government body or regulatory authority with relevant powers | — |
| assets | Property and rights owned by a party (commercial context) | "patrimony", "heritage" (calques) |
| estate | Property of a deceased person or insolvent entity (succession/insolvency only) | Using "estate" in commercial contexts |

## Corporate Identifiers

| Correct English term | Usage / meaning | Avoid |
|---|---|---|
| registered office | Official legal address of a company | — |
| principal place of business | Main operational location | "operating office" (calque) |
| tax identification number | Unique identifier for tax purposes | "tax code" (calque) |
| VAT registration number | VAT identifier | "VAT number" as a defined term |
| companies register / trade register | Public register where company information is filed | Confusing with the institution that maintains it |
| share capital | Nominal value of a company's issued shares | — |
| articles of association (UK) / by-laws (US) | See canonical definition in corporate-ma-jv.md. | — |
| casting vote | A deciding vote exercisable by the chairman to break a tie | "double vote" |

## Cross-Reference Conventions

| Element | Correct English | Avoid | Notes |
|---|---|---|---|
| Internal sections | Clause (UK) / Section (US) | Article (for internal refs) | "Article" is correct for legislation and articles of association/by-laws |
| Sub-sections | paragraph | subsection, comma | — |
| Attachments | Schedule (UK) or Annex (EU/international) | — | Match the source document's convention; Appendix also acceptable |
| Introductory statements | Recital | Preamble, Whereas clause | — |
| Earlier/later in document | above / below | "that precedes" / "that follows" | — |
| Self-reference | this Deed / this Agreement | "the present deed", "the present agreement" | — |

## Party References

- Use the defined party name consistently: "the Grantor", "the Borrower" (with "the" and
  capitalised)
- In definitions, the term being defined appears without "the"
- **"hereby"** is the standard way to express present-tense performative acts in legal English
  (e.g., "the Grantor hereby pledges")

## Latin Terms to Keep

These Latin terms are conventional in English legal documents and should not be translated:

inter alia, mutatis mutandis, pari passu, pro rata, bona fide, vis-à-vis, de facto, de jure,
prima facie, sui generis, et seq., ibid., supra, infra, ad hoc, ab initio, ultra vires,
intra vires, per se, in rem, in personam, lex loci, locus standi, pro forma, ex parte,
inter vivos, mortis causa, ipso facto, sine die

## Grammar and Style

When translating into English legal register from any source language, apply these rules:

- **"Shall" vs "will" / "must"**: UK legal English traditionally uses "shall" for imposing
  obligations ("the Borrower shall repay"). Modern plain-English drafting and some US
  practice prefer "will" or "must". Match the drafting convention of the source document's
  likely audience. If the source document is from a magic circle or top-tier City law firm
  context, "shall" is expected. If the user has no preference, default to "shall" for UK
  and "will" or "must" for US.
- **Adjective placement**: English places adjectives before the noun ("existing and future
  plants", not "plants existing and future").
- **Articles**: English uses articles consistently ("the Borrower", not just "Borrower").
- **Indefinite articles**: "an Event", "an Enforcement Event" (not "a Event").
- **Passive constructions**: Many source languages overuse passive voice; adapt to active
  voice where it reads more naturally in English.
- **Sentence length**: It is acceptable to break very long source-language sentences into two
  English sentences if this aids clarity, provided the legal meaning is preserved.
- **Double negatives**: Simplify in English ("cannot not" → "must" / "shall necessarily").
- **Word order in enumerations**: Ensure natural English order ("all existing and future
  receivables", not "receivables existing and future").

## Calendar Conventions — MANDATORY (all source languages)

All dates in the English translation must be in full Gregorian (Western) form:
`29 November 2017`, `1 April 2023`, `15 March 1989`. Many legal systems draft
dates in non-Gregorian calendars; convert every such date to its Gregorian
equivalent before it appears in the English output.

Calendars commonly encountered in legal documents:

- **Japanese** — era system (和暦): 令和 / Reiwa, 平成 / Heisei, 昭和 / Showa,
  大正 / Taisho, 明治 / Meiji.
- **Republic of China (Taiwan)** — ROC year (民國). ROC + 1911 = Gregorian.
- **Thai** — Buddhist Era (พ.ศ. / B.E.). B.E. − 543 = Gregorian.
- **Hijri / Islamic** — A.H. (ھ). Lunar; conversion is non-trivial — use a
  table or trusted converter.
- **Korean Dangun** — rare in modern legal drafting. Dangun − 2333 = Gregorian.
- **Hebrew Anno Mundi** — A.M. Rare in modern legal drafting.

**Rule (strict): convert every date to Gregorian.** Do NOT preserve the
source-language era name in the output, not even parenthetically. The English
document must read as if it were drafted in Gregorian throughout — no
`Reiwa 5`, no `Heisei 29`, no `Minguo 110`, no `B.E. 2566`, no
`A.H. 1445`.

For language-specific era tables, conversion details, and placeholder handling
(blanks like Japanese `〇` in unfilled date cells), see the relevant
`<language>-general-legal.md` sub-lexicon.

## UK vs US English

Default to **UK English** spelling and conventions for European legal documents. Use US
English only if the user specifies or the document context clearly requires it (e.g.,
documents governed by US law).

Key differences to maintain consistently:

| UK English (default) | US English (on request) |
|---|---|
| favour, honour, colour | favor, honor, color |
| organise, recognise | organize, recognize |
| programme (but: program for software) | program |
| defence, licence (noun), practice (noun) | defense, license (noun), practice (noun) |
| Clause | Section |
| Schedule | Exhibit |
| completion | closing |
| amendment | modification |
| indemnity | indemnification |
| best endeavours (traditional UK) / best efforts | best efforts |
| whilst (traditional) | while |

When producing UK English output, be consistent throughout the document. Do not mix UK
and US conventions.

## Cover Pages and Administrative Phrasing

Cover pages, title blocks, and signature blocks are the **first thing the reader sees**.
They use formulaic administrative language that is especially prone to calques — phrases
that translate word-for-word but read unnaturally in English. Always re-read the cover page
as a standalone piece of English and rephrase any construction that a native speaker would
not write.

| Correct English | Avoid | Notes |
|---|---|---|
| authorised representative | "representative acting on behalf of the organisation" | Civil law languages use verbose constructions; English is concise |
| Authorised signatory: [name] | "Authorised representative and signature: [name]" | A person is a **signatory** (noun: the person who signs); "signature" is the mark on paper. On cover pages and signature blocks, always use **signatory** when referring to the person. Never write "authorised representative and signature" — this is a direct calque from Hungarian ("jogosult képviselő és aláírás") and Italian ("rappresentante autorizzato e firma"). Correct forms: "Authorised signatory", "Signatory", "Signed by" |
| Title: [Managing Director] | "Position: …" / "Function: …" / "Capacity: …" | In English signature blocks, the label over the signatory's role is always **"Title"** — never "Position", "Function", "Capacity", or "Role". This applies no matter what the source uses: Dutch *Functie*, Italian *Qualifica*, French *Fonction*, German *Funktion* / *Stellung*, Spanish *Cargo*, Portuguese *Cargo*, Polish *Stanowisko*, Hungarian *Beosztás*. Translate all of these as "Title". The value under "Title:" is the officer's corporate title — "Managing Director", "Director", "Chief Executive Officer", "Authorised Signatory", etc. Do not invent a title if the source gives a generic word like *Directeur* — render it as "Managing Director" for Dutch/French-style *directeur* when the signatory is a company director, "Director" when plainly a board member. |
| Application under Call [reference] | "for the grant application under the above Call" / "Application under the 'Call'..." / "for the grant application entitled" | **Be direct and concise.** Put the call reference number right next to "Call" — do not use vague relative clauses like "under the above Call" or "for the grant application under...". The reader must immediately see which call this is. If the source also names the programme, append it: "Application under Call [reference] — [Programme name]". Never truncate, never use indirect phrasing. |
| Applicant: [name] | "Applicant organisation: [name]" | Drop "organisation" when the entity name makes it obvious |
| signed by | "signed and authenticated by" | "Authenticated" is redundant in English unless a specific authentication process applies |
| on behalf of [entity] | "in the name and on behalf of [entity]" | Unless a legal distinction between "in the name of" and "on behalf of" is intentional |
| [Title], dated [date] | "the [Title] bearing the date of [date]" | Verbose calque common in civil law instruments |
| pursuant to | "on the basis of and pursuant to" | Pick one; do not stack both |
| duly authorised | "duly invested with powers" / "endowed with necessary powers" | Calques from civil law power-of-attorney language |

**Cover page completeness rule:** Every field on the cover page must be translated **in
full**. Never truncate a phrase, drop a reference number, or leave a field partially
translated. Cover pages are the first thing the reader sees — an incomplete or cut-off
field immediately signals poor translation quality. After translating the cover page,
re-read it as standalone English and verify: (a) every field is complete, (b) no source-
language fragments remain, (c) the wording is what a native English speaker would write,
(d) "signature" is not used where "signatory" is meant.

## Definitions Section

When a document contains a definitions section:

- Definitions must be **reordered alphabetically by the English defined term**
- The source language often has a different alphabetical order — always re-sort
- Multi-paragraph definitions (with sub-items or examples) must stay grouped together
- Use the bundled `reorder_definitions.py` script after applying translations
