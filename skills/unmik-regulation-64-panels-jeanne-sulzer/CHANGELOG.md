# Changelog — reg-64-kosovo skill

All notable changes to the Regulation 64 Panels (Kosovo) skill are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0-draft] — 2026-06-02

### Fixed
- `references/verification-workflow.md` (Trap 1): corrected the KSC founding-instrument number to **Law No. 05/L-053** (was "04/L-274").

### Added

- Initial draft of the `reg-64-kosovo` skill — thirteenth skill in the Skills for International Justice series
- `SKILL.md` covering:
  - Reg. 64 Panel verification discipline (existence / content / paragraph levels)
  - Institutional architecture: Phase 1 (early 2000, ad hoc), Phase 2 (UNMIK Reg. 2000/6 of 15 February 2000), Phase 3 (UNMIK Reg. 2000/64 of 15 December 2000)
  - Reg. 64 panel composition: 3 professional judges, minimum 2 international, presiding judge international
  - Case-by-case designation mechanism: petition → DJA recommendation → SRSG approval → DJA designation
  - KWECC abandoned autumn 2000 in favour of integrated Reg. 64 mechanism
  - UNMIK-to-EULEX transition (17 February 2008 independence; 9 December 2008 EULEX full operational capability)
  - Reg. 64 vs KSC distinction (institutional, temporal, geographic) — explicitly flagged
- `references/foundational-texts.md` — UNSC Res 1244 (1999), UNMIK Regulations 1999/1, 2000/6, 2000/64, 2001/2, 2001/9 (Constitutional Framework), 2003/25 (Provisional Criminal Code), 2003/26 (Provisional CPC); Yugoslav Federal Criminal Code 1976 continuity; Joint Action 2008/124/CFSP (EULEX); Law 2008/03-L053; Constitution of the Republic of Kosovo
- `references/authoritative-sources.md` — source hierarchy: unmik.unmissions.org legacy archive, EULEX archives, legal-tools.org, USIP Michael Hartmann reports, OSCE Mission in Kosovo trial monitoring, ICTJ reports, academic monographs (Cerone, Reidy, Cohen, Strohmeyer)
- `references/citation-format.md` — district court case-numbering conventions, Reg. 64 Panel marking, multilingual (Albanian / Serbian / English) citation forms
- `references/verification-workflow.md` — fallback ladder, Reg. 64-specific traps (KSC distinction, KWECC abandoned not established, EULEX in Kosovo not The Hague, temporal applicability of substantive law, panel composition precision, Reg. 64 ≠ ordinary district court panel)
- `references/jurisprudence-map.md` — institutional periods (Phases 0–3), substantive coverage (war crimes, inter-ethnic crimes, organised crime, terrorism), case typology (resurrection, venue-change, mixed panels, retrials, joint indictments), comparative positioning (SPSC, WCC-BiH, KSC, ICTY)
- `examples/example-verification.md` — end-to-end verification of Reg. 2000/64 Section 2.2 composition rule, with three common variation traps
- `examples/example-audit.md` — auditing a user-supplied passage with six categorical errors (institutional misidentification, operative date, composition framing, substantive law temporality, KWECC misattribution, EULEX geographic error)

### Sources consulted (project-level research notes)

- UNMIK official archive — unmik.unmissions.org
- USIP — Michael E. Hartmann, "International Judges and Prosecutors in Kosovo" reports
- ECFR reports on Kosovo rule of law
- ICTJ — Kosovo transitional justice reports
- OSCE Mission in Kosovo — Legal Systems Monitoring Section reports
- Hybrid Justice project — comparative scholarship
- John Cerone — academic articles on Reg. 64 Panels in *Journal of International Criminal Justice*
- Hansjörg Strohmeyer — *American Journal of International Law* on UNMIK and UNTAET parallel administration
- David Cohen — East-West Center comparative reports on internationalised judicial mechanisms
- Reed Brody — comparative scholarship on internationalised prosecutions
- Romano, Nouwen, Stahn — taxonomies of hybridised criminal jurisdictions

### Known limitations

- Reg. 64 Panel jurisprudence is **archivally fragmented**; no single authoritative case index exists comparable to ICC CourtRecords or ICTY Records Database
- Case verification typically requires consultation of multiple sources
- High-quality academic literature exists in English; primary case materials are in Albanian, Serbian, and English; verification across language versions may be necessary for substantive claims
- The 2008-2009 transition period is particularly poorly archived in the standalone Reg. 64 framing (much of the relevant material is in EULEX archives, which have their own access constraints)

### Verification methodology

This skill follows the verification-first methodology defined in the parent repository's `METHODOLOGY.md`. The five cumulative criteria for jurisdiction selection were applied:

1. **Subject-matter jurisdiction over international crimes** — Reg. 64 Panels prosecuted war crimes under Yugoslav Federal Criminal Code 1976 (Chapter XVI) and from 2004 the Provisional Criminal Code; ethnic crimes also addressed
2. **Structural internationalised element** — UNMIK Reg. 2000/64 legal basis (UN-administered framework), composition requirement of majority international judges, SRSG approval mechanism
3. **Limited temporal and material jurisdiction** — operational 2000-2008/2009; case-by-case designation for "important or sensitive" cases; specific to Kosovo territorial scope
4. **Structured public documentation** — UNMIK official archive, EULEX archive, legal-tools.org, OSCE trial monitoring, academic monographs (fragmented but substantial)
5. **Substantial doctrinal contribution to international criminal justice** — Reg. 64 is the prototypical "integration model" of internationalised judicial administration; influential in subsequent design debates (cited in Romano/Nouwen/Stahn taxonomies of graduated hybridity); empirical case study in literature on rule of law in post-conflict transitions

### Status

**Draft — not yet validated by a Kosovo-based or UNMIK-veteran international criminal lawyer.** Pre-publication review encouraged.

---

## Notes for future versions

- v1.1 candidates: add structured case-table of high-profile Reg. 64 prosecutions (Mitrovica venue-change cases, March 2004 riot prosecutions); deeper treatment of EULEX continuation cases
- v2.0 candidates: integrate post-2018 EULEX Strengthening Mission and full transition to national judiciary; integrate verified academic citations from Cerone, Reidy, Cohen with paragraph-level accuracy
