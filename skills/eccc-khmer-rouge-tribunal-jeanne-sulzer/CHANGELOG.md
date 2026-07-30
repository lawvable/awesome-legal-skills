# Changelog

All notable changes to the `eccc` skill are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this skill adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.2] — 2026-06-02

### Fixed
- Internal Rules revision table (`references/foundational-texts.md`): the 12 June 2007 original was mislabelled "Rev. 1"; renamed it "Original (unnumbered)" and inserted the genuine **Rev. 1 (1 February 2008)**. Verified against the ECCC legal-framework revision history.

## [1.2.1] — 2026-05-30

### Changed
- Editorial consistency pass (suite-wide review): removed a decorative star from a `jurisprudence-map.md` heading and replaced tick check-marks in the examples with plain text, to match the suite's no-symbol house style.

### Fixed
- Corrected the example-file paths in the [1.2.0] entry (`examples/`, not `references/`).

## [1.2.0] — integrated the Court's canonical authorities table and added a jurisprudence map

### Added
- Canonical "Frequently cited authorities and their abbreviations" reference table reproduced from the *Guide Vol. 2* into `citation-format.md`. Confirms and supplies document numbers, dates, and Court-preferred short forms for: UN-RGC Agreement, ECCC Law, Internal Rules; the 3 main Practice Directions; and the principal documents for Case 001 (D99, D99/3/42, E188, F28), Case 002 pre-severance (D427 and its appeal sub-numbers), Case 002/01 (E313, F36), Case 002/02 (E465, F76), Case 003 (D266, D267, D266/27 & D267/35), Case 004 (D381, D382, D381/45 & D382/43), Case 004/01 (D308/3, D308/3/1/20), Case 004/02 (D359, D360, D359/24 & D360/33).
- New `references/jurisprudence-map.md`: a topic-by-topic map of the ECCC's principal holdings, organised by the eight chapters of the *Guide Vol. 2* (Jurisdiction; Crimes; Individual criminal responsibility; Fair trial rights; Procedure; Sentencing; Civil Party action; Administration of justice). Particularly developed for Civil Party reparations (chapter 7), JCE (chapter 3.4), and Genocide (chapter 2.3).
- E188 (Case 001 Judgment) and F28 (Case 001 Appeal Judgment) — confirmed and added.
- Case 001 Appeal Judgment paras 45–80 referenced as the foundational holding on personal jurisdiction (two-category structure of "senior leaders / most responsible" and the policy/jurisdictional distinction).
- The three Practice Directions (Filing of Documents, Victim Participation, Protective Measures) documented in `citation-format.md`.

### Confirmed (no change needed)
- Document numbers D427, E313, F36, E465, F76 — all confirmed against the canonical table.

### Notes
- The *Guide Vol. 2* canonical table records the Case 001 Trial Judgment as "26 July 2007, E188". The verdict date is 26 July 2010; "26 July 2007" appears to be a typographical error in the Guide. The document number E188 is correct.

## [1.1.0] — integrated ECCC's own jurisprudence resources

### Added
- Reference to the official two-volume *Guide to the Extraordinary Chambers in the Courts of Cambodia* (Volume 1: Establishment, Operations and Cases; Volume 2: Jurisprudence). Volume 2 is the canonical jurisprudence catalogue and is now referenced throughout the skill.
- The Addendum to the UN-Cambodia Agreement (December 2021) added to `foundational-texts.md` as a third foundational instrument, with the eight residual functions enumerated.
- The ECCC Archive (`archive.eccc.gov.kh`, over 2 million pages) added to Tier 1 sources.
- ECCC Lexicon, Bibliography, Jurisprudence index page, and interactive Timeline added to Tier 1 URL patterns.
- Cambodia Annotated Code of Criminal Procedure (OHCHR, 2nd ed. 2015) added to Tier 2.
- Ciorciari & Heindel, *Hybrid Justice* (2014, open access); Jørgensen, *Elgar Companion to the ECCC* (2018) added to Tier 2 academic.
- E3 exhibit sub-series documented in `citation-format.md`.

### Changed
- 1973 → 1961 Vienna Convention on Diplomatic Relations (the correct convention referenced by ECCC Law Article 8).
- JCE caveat tightened in `SKILL.md` and `foundational-texts.md` using the digest's own characterisation: "judicially recognised as a form of commission".
- Subject-matter jurisdiction pointers expanded to include Article 7 (Hague Convention 1954) and Article 8 (Vienna Convention 1961), with note that no ECCC Case contained specific charges under either.

## [1.0.0] — initial release

### Added
- `SKILL.md` — entry point, verification-first discipline, standard workflow, foundational texts, source hierarchy, citation format overview, audit mode, substantive doctrine pointers, sensitive-contexts guidance
- `references/authoritative-sources.md` — Tier 1 / Tier 2 / Never-authoritative hierarchy with URL patterns specific to the ECCC
- `references/citation-format.md` — Case File Number anatomy, document-number letter-prefix system (A/B/C/D/E/F), accused-name convention (SURNAME first, in capitals), severance handling (Case 002, 002/01, 002/02), Internal Rules revision discipline
- `references/verification-workflow.md` — step-by-step procedure, fallback ladder, partial-verification handling, Khmer/French/English language discipline
- `references/foundational-texts.md` — the UN-Cambodia Agreement, the ECCC Law (as amended), the Internal Rules (Rev. 10 and earlier)
- `examples/example-verification.md` — end-to-end verification of a representative ECCC citation
- `examples/example-audit.md` — working-draft audit and finalised-record audit, worked through on representative ECCC documents

### Skill scope at v1.0.0
- Covers all four cases on the ECCC docket: Case 001 (KAING Guek Eav alias Duch), Case 002 (NUON Chea, KHIEU Samphan, IENG Sary, IENG Thirith), with the severance into Case 002/01 and Case 002/02; Case 003 (MEAS Muth); Case 004 (IM Chaem, AO An, YIM Tith)
- Encodes the verification-first methodology shared with the `icc` skill in this repository

### Known limitations
- Internal Rules revision tracking: the skill instructs the model to identify and cite the revision in force at the date of the cited application, but does not include a table of revisions × dates. Users with substantial litigation depending on a particular revision should provide that revision to the project knowledge.
- Khmer-language documents: the skill is built around English-language verification. For Khmer-original sources (the Cambodian-law components, the Cambodian penal code, original-language Closing Orders), verification by a Khmer reader remains necessary; the skill flags this rather than masking it.

