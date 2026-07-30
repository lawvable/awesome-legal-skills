# Citation format — ECCC

ECCC citations are precise, hierarchical, and structurally different from ICC citations. This reference encodes the conventions so that an output can be checked against them mechanically.

## The two pieces

For any case-specific document, two pieces of identifying information must appear:

1. **The Case File Number** — the file under which the document was registered.
2. **The Document Number** — the alphanumeric identifier of the specific filing within that case file.

Both are necessary. A citation that gives the title and date but neither identifier is incomplete.

## Case File Number anatomy

Format:

```
[Case Number]/[Date of Introductory Submission, DD-MM-YYYY]/ECCC/[Chamber or Office]
```

Examples:

- `001/18-07-2007/ECCC/TC` — Case 001, introductory submission of 18 July 2007, Trial Chamber
- `002/19-09-2007/ECCC/TC` — Case 002, introductory submission of 19 September 2007, Trial Chamber
- `002/19-09-2007/ECCC/SCC` — same file before the Supreme Court Chamber
- `002/19-09-2007-ECCC/SCC` — variant punctuation occasionally appears; both forms refer to the same file
- `003/07-09-2009/ECCC/OCIJ` — Case 003, Office of the Co-Investigating Judges
- `004/07-09-2009/ECCC/OCIJ` — Case 004, same OCIJ introductory date (Cases 003 and 004 share an introductory submission date because they originated from the second Introductory Submission)

The chamber/office suffix tells you which body had the file at the moment the document was registered. The same case migrates between offices (OCIJ → TC → SCC) as it progresses; the Case File Number suffix reflects the body currently seised.

## Document Number anatomy

Letter prefixes encode the procedural phase:

| Prefix | Phase | Examples |
|---|---|---|
| **A** | Co-Prosecutors' filings (Introductory Submissions, Supplementary Submissions) | `A1`, `A2` |
| **B** | Early case-management documents | `B1`, `B2` |
| **C** | OCIJ investigation-phase filings and orders | `C1`, `C20`, `C160/4` |
| **D** | OCIJ filings, decisions, and orders (including Closing Orders) | `D99` (Case 001 Closing Order), `D427` (Case 002 Closing Order), `D266` (Case 003 Dismissal Order), `D267` (Case 003 Closing Order/Indictment), `D381` (Case 004 Dismissal Order), `D382` (Case 004 Closing Order/Indictment), `D359` (Case 004/02 Dismissal Order), `D360` (Case 004/02 Closing Order), `D308/3` (Case 004/01 Dismissal Order — Im Chaem). The D-series is broader than just Closing Orders: it covers all OCIJ filings and decisions during the investigation phase (e.g. `D48`, `D49`, `D181` are OCIJ decisions in Case 003 on personal jurisdiction). |
| **E** | Trial Chamber filings, decisions, and judgments | `E1` (initial Trial Chamber filing), `E188` (Case 001 Trial Judgment, 26 July 2010), `E141`, `E163/5`, `E284/4/8`, `E313` (Case 002/01 Trial Judgment, 7 August 2014), `E465` (Case 002/02 Trial Judgment, 16 November 2018) |
| **F** | Supreme Court Chamber filings, decisions, and judgments | `F28` (Case 001 Appeal Judgment, 3 February 2012), `F36` (Case 002/01 Appeal Judgment, 23 November 2016), `F76` (Case 002/02 Appeal Judgment, 23 December 2022) |

**E3 sub-series — exhibits in evidence.** Within the Trial Chamber phase, the `E3` document number designates the master exhibit list; individual exhibits are cited as `E3/[number]` (e.g. `E3/4392`). When a judgment cites `E3/4392`, this is an exhibit (typically a witness statement, document seized in investigation, expert report, or photograph) admitted into evidence, not a substantive Chamber filing. Distinguish from other `E[number]` filings, which are Trial Chamber decisions, orders, and submissions.

Sub-numbering uses slashes. `E163/5/1/13` is a sub-document at four levels of nesting within Trial Chamber filing E163. Each slash is a sub-document attached to the document on its left.

Document version suffixes:
- No suffix — the version of record (often a public-redacted version where the underlying filing was confidential)
- `-Public` or `-Redacted` — explicit public version
- `-Confidential` or `-Conf` — confidential version, restricted distribution
- `-Strictly Confidential` — the most restricted distribution category
- `-EN`, `-FR`, `-KH` — language suffixes (English / French / Khmer)

When citing, prefer the public-redacted version if available. If a citation rests on confidential content not available in the public version, the output must say so.

## Chambers and offices — abbreviations

| Abbreviation | Body |
|---|---|
| **OCP** | Office of the Co-Prosecutors |
| **OCIJ** | Office of the Co-Investigating Judges |
| **PTC** | Pre-Trial Chamber |
| **TC** | Trial Chamber |
| **SCC** | Supreme Court Chamber |
| **DSS** | Defence Support Section |
| **VSS** | Victims Support Section |
| **OA** | Office of Administration |

## Accused-name convention

The ECCC uses the Cambodian naming order: **SURNAME in capitals, then given name**.

| Correct | Incorrect |
|---|---|
| KAING Guek Eav alias Duch | Duch Kaing |
| NUON Chea | Chea Nuon |
| KHIEU Samphan | Samphan Khieu |
| IENG Sary | Sary Ieng |
| IENG Thirith | Thirith Ieng |
| MEAS Muth | Muth Meas |
| IM Chaem | Chaem Im |
| AO An | An Ao |
| YIM Tith | Tith Yim |

In case captions, the form is `Prosecutor v. [SURNAME] [given name]`. Aliases follow with "alias": `Prosecutor v. KAING Guek Eav alias Duch`.

## Severance citations — Case 002, 002/01, 002/02

Case 002 was severed by the Trial Chamber into two separate trial segments. Citing it carelessly produces ambiguity.

- **Case 002** — the original case file, used for documents that pre-date severance (Closing Order, indictment, early Trial Chamber filings) and for filings that affect both segments.
- **Case 002/01** — the first trial segment. Crimes against humanity committed during the course of the movement of population (phases 1 and 2) and at Toul Po Chrey. Judgment 7 August 2014 (E313). Appeal judgment 23 November 2016 (F36).
- **Case 002/02** — the second trial segment. Genocide against the Cham and the Vietnamese, forced marriage, treatment of Buddhists, internal purges, four worksites and three security centres including S-21. Trial Judgment 16 November 2018 (E465). Appeal Judgment 23 December 2022 (F76; the appeal was orally pronounced on 22 September 2022, with the full written judgment published on 23 December 2022 — cite F76 with the 23 December 2022 date).

When citing a document issued before severance, use "Case 002". When citing a document issued after severance that pertains to one segment only, use "Case 002/01" or "Case 002/02" as appropriate. The document number itself does not change between segments — a Trial Chamber filing in Case 002/02 still uses an E-prefix in the same numbering sequence as the broader Case 002.

## Internal Rules — revision discipline

The ECCC Internal Rules have been amended ten times. The current revision is Rev. 10 (27 October 2022). A decision from 2010 applied an earlier revision; the rule it interpreted may differ in number, wording, or both, from the current rule with the same nominal designation.

Citation discipline:

- Always state the revision in force at the date of the cited application: `Internal Rules (Rev. 9), Rule 23 bis(1)`
- For propositions about the current Rules, cite Rev. 10
- For propositions about what the Trial Chamber held in 2014 under Rev. 8, cite Rev. 8

A list of Internal Rules revisions with their dates is in `foundational-texts.md`.

## Foundational texts — short forms

- **UN-Cambodia Agreement** — `UN-Cambodia Agreement, Article 9` (jurisdiction); `Article 13` (rights of the accused)
- **ECCC Law (as amended)** — `ECCC Law, Article 3 new` (Cambodian penal code crimes), `Article 4` (genocide), `Article 5` (crimes against humanity), `Article 6` (grave breaches of the Geneva Conventions of 1949), `Article 7` (destruction of cultural property), `Article 29 new` (modes of individual responsibility — note "new" suffix indicating the renumbered article post-2004 amendment)
- **Internal Rules (Rev. X)** — `Internal Rules (Rev. 10), Rule 23 quater(1)`

The "new" suffix appearing on some Articles of the ECCC Law indicates an article renumbered or replaced by the 2004 amendment. Some sources omit "new"; the rigorous form includes it.

## Worked example

Question: how to cite the Case 002/02 Trial Chamber's analysis of the elements of genocide against the Cham at paragraph 3445.

Verified-content citation:

> *Prosecutor v. NUON Chea and KHIEU Samphan* (Case 002/02), Trial Chamber, "Trial Judgment", E465, 16 November 2018, para. 3445.

If only existence is verified (the document exists at E465, 16 November 2018, but the paragraph text was not retrieved):

> *Prosecutor v. NUON Chea and KHIEU Samphan* (Case 002/02), Trial Chamber, "Trial Judgment", E465, 16 November 2018 (existence verified; paragraph content not retrieved in this session).

## When the citation cannot be completed

If, after verification, you cannot identify the document number or you cannot confirm the date or chamber, the citation is not yet a citation. Either narrow the claim, or tell the user what is missing and ask them to provide the source.

## Canonical reference table — Frequently cited authorities

The ECCC's own *Guide to the ECCC, Volume 2: Jurisprudence* publishes an authoritative "Frequently cited authorities and their abbreviations" table. The entries below are reproduced from that table (Court-issued, Tier 1). When a major ECCC document is cited, prefer the abbreviated form used by the Court itself.

### Legal framework

| Long citation | Short form |
|---|---|
| Agreement between the UN and the Royal Government of Cambodia… (entered into force 29 April 2005, 2329 U.N.T.S. 117) | **UN-RGC Agreement** |
| Law on the Establishment of Extraordinary Chambers… (as amended 27 October 2004, NS/RKM/1004/006) | **ECCC Law** |
| Internal Rules (Rev. 10), as revised on 27 October 2022 | **Internal Rules** |

### Practice Directions

| Long citation | Short form |
|---|---|
| Practice Direction ECCC/01/2007/Rev. 8 (7 March 2012) — Filing of Documents | **PD on the Filing of Documents** |
| Practice Direction 02/2007/Rev. 1 (27 October 2008) — Victim Participation | **PD on Victim Participation** |
| Practice Direction ECCC/03/2007/Rev. 1 (29 April 2008) — Protective Measures | **PD on Protective Measures** |

### Case 001 — KAING Guek Eav alias Duch

| Document | Number | Date | Short form |
|---|---|---|---|
| Closing Order indicting Duch | **D99** | 8 August 2008 | Case 001, Closing Order |
| Decision on Appeal against Closing Order | **D99/3/42** | 5 December 2008 | Case 001, Decision on Closing Order Appeal |
| Judgment | **E188** | 26 July 2010 | Case 001, Judgment |
| Appeal Judgment | **F28** | 3 February 2012 | Case 001, Appeal Judgment |

### Case 002 — pre-severance documents (Nuon Chea, Khieu Samphan, Ieng Sary, Ieng Thirith)

| Document | Number | Date | Short form |
|---|---|---|---|
| Closing Order | **D427** | 15 September 2010 | Case 002, Closing Order |
| Decision on Khieu Samphan's Appeal against the Closing Order | **D427/4/15** | 21 January 2011 | Case 002, Decision on Closing Order Appeal (Khieu Samphan) |
| Decision on Appeals by Nuon Chea and Ieng Thirith against the Closing Order | **D427/2/15 & D427/3/15** | 15 February 2011 | Case 002, Decision on Closing Order Appeals (Nuon Chea and Ieng Thirith) |
| Decision on Ieng Sary's Appeal against the Closing Order | **D427/1/30** | 11 April 2011 | Case 002, Decision on Closing Order Appeal (Ieng Sary) |

### Case 002/01 (Nuon Chea, Khieu Samphan)

| Document | Number | Date | Short form |
|---|---|---|---|
| Judgment | **E313** | 7 August 2014 | Case 002/01, Judgment |
| Appeal Judgment | **F36** | 23 November 2016 | Case 002/01, Appeal Judgment |

### Case 002/02 (Nuon Chea, Khieu Samphan)

| Document | Number | Date | Short form |
|---|---|---|---|
| Judgment | **E465** | 16 November 2018 | Case 002/02, Judgment |
| Appeal Judgment | **F76** | 23 December 2022 | Case 002/02, Appeal Judgment |

### Case 003 — MEAS Muth

| Document | Number | Date | Short form |
|---|---|---|---|
| Order Dismissing the Case | **D266** | 28 November 2018 | Case 003, Dismissal Order |
| Closing Order (Indictment) | **D267** | 28 November 2018 | Case 003, Closing Order (Indictment) |
| Considerations on Appeals against Closing Orders | **D266/27 & D267/35** | 7 April 2021 | Case 003, Considerations on Closing Order Appeals |

### Case 004 — YIM Tith

| Document | Number | Date | Short form |
|---|---|---|---|
| Order Dismissing the Case | **D381** | 28 June 2019 | Case 004, Dismissal Order |
| Closing Order (Indictment) | **D382** | 28 June 2019 | Case 004, Closing Order (Indictment) |
| Considerations on Appeals against Closing Orders | **D381/45 & D382/43** | 17 September 2021 | Case 004, Considerations on Closing Order Appeals |

### Case 004/01 — IM Chaem

| Document | Number | Date | Short form |
|---|---|---|---|
| Closing Order (Reasons) — Dismissal | **D308/3** | 10 July 2017 | Case 004/01, Dismissal Order |
| Considerations on Closing Order Appeal | **D308/3/1/20** | 28 June 2018 | Case 004/01, Considerations on Closing Order Appeal |

### Case 004/02 — AO An

| Document | Number | Date | Short form |
|---|---|---|---|
| Order Dismissing the Case | **D359** | 16 August 2018 | Case 004/02, Dismissal Order |
| Closing Order (Indictment) | **D360** | 16 August 2018 | Case 004/02, Closing Order (Indictment) |
| Considerations on Appeals against Closing Orders | **D359/24 & D360/33** | 19 December 2019 | Case 004/02, Considerations on Closing Order Appeals |

**Source for the entire table**: ECCC, *Guide to the Extraordinary Chambers in the Courts of Cambodia, Volume 2: Jurisprudence*, "Frequently cited authorities and their abbreviations", available at `https://eccc.gov.kh/sites/default/files/Guide_Vol_2_Manuscript_EN_latest.pdf`.

