# Changelog

All notable changes to the `icty-ictr-irmct` skill are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this skill adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — initial release

### Added
- `SKILL.md` — entry point, verification-first discipline, standard workflow, the institutional architecture of the ICTY, ICTR and Mechanism, foundational texts, source hierarchy, citation format overview, audit mode, substantive doctrine pointers, sensitive-contexts guidance (protective measures)
- `references/authoritative-sources.md` — Tier 1 / Tier 2 / Never-authoritative hierarchy, with the irmct.org, Case Law Database (cld.irmct.org), Unified Court Records (ucr.irmct.org), legacy icty.org and unictr.irmct.org, and legal-tools.org entry points
- `references/citation-format.md` — case-number anatomy (IT- / ICTR- / MICT-), phase suffixes (-T, -A, -AR72, -S, -R, -ES), party-designation and diacritics conventions, the IT→MICT transition for appeals (Karadžić, Mladić), and a canonical table of frequently cited authorities with verified case numbers and dates
- `references/verification-workflow.md` — fallback ladder (irmct.org → CLD → UCR → legacy sites → legal-tools.org → secondary → ask), verification-level matching, and a hard protective-measures rule (never identify a protected witness; prefer public redacted versions)
- `references/foundational-texts.md` — the ICTY Statute (Res. 827, 1993), the ICTR Statute (Res. 955, 1994), the IRMCT Statute and Transitional Arrangements (Res. 1966, 2010), the three RPEs, and the competence rule that explains the IT/MICT split
- `references/jurisprudence-map.md` — topic-by-topic map of landmark holdings: jurisdiction (Tadić AR72), genocide (Akayesu, Krstić, Karadžić, Mladić), incitement (Akayesu, Media case), crimes against humanity (Tadić, Kunarac), JCE (Tadić Appeal), command responsibility (Čelebići, Blaškić), torture (Furundžija), sexual violence (Akayesu, Kunarac, Furundžija), senior-leadership guilty plea (Kambanda), residual/fugitive function (Kabuga)
- `examples/example-verification.md` — end-to-end verification of the Krstić / Srebrenica-genocide citation, including the trial vs appeal distinction
- `examples/example-audit.md` — a working-draft audit (Tadić JCE date/chamber error; Akayesu/JCE III mischaracterisation) and a final-record audit (Mladić Appeal Judgment, the IT/MICT pairing)

### Skill scope at v1.0.0
- Covers the ICTY (1993–2017), the ICTR (1994–2015), and the IRMCT / Mechanism (2010– ) as a single integrated skill, because the Mechanism continues the functions of both tribunals, hosts their archives, and decided the late appeals under MICT numbers
- Encodes the verification-first methodology shared with the `icc` and `eccc` skills in this repository

### Known limitations
- RPE revision tracking: the skill instructs the model to identify the revision in force at the date of a cited decision but does not include a table of revisions × dates. Users litigating a point that turns on a specific revision should provide that revision to the project knowledge.
- The canonical authorities table covers the most frequently cited landmark judgments; it is not a complete docket. Many significant cases (Galić, Stakić, Stanišić & Simatović, Bagosora et al., Nahimana et al., Butare) are referenced in the jurisprudence map but not given full citation lines — verify each against Tier 1 before citing.
- Dates in the authorities table were verified against Tier 1 sources at authoring time; because public redacted versions sometimes post-date the oral pronouncement, always reconfirm the operative date and version against irmct.org before citing.
