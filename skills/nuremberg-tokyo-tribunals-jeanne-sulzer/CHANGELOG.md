# Changelog

All notable changes to the `nuremberg-tokyo` skill are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this skill adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] — 2026-06-02

### Fixed
- IMTFE defendant tables (`references/defendants-and-judges.md`, `references/citation-format.md`): corrected Takasumi Oka's rank to **Vice Admiral**. Verified against the UVA IMTFE digital collection.

## [1.0.0] — initial release

### Added
- `SKILL.md` — entry point covering the **IMT** (1945-46), the twelve subsequent **NMT** trials under Control Council Law No. 10 (1946-49), and the **IMTFE** (1946-48) as a single integrated skill; verification-first discipline, standard workflow, the four classic traps (IMT/NMT, Nuremberg/Tokyo, Charter terminology, majority vs separate opinions), foundational texts inventory, source hierarchy with ~15 Tier 1 sources, citation format overview, audit mode, substantive doctrine pointers, sensitive-contexts guidance
- `references/foundational-texts.md` — London Agreement (82 U.N.T.S. 280) and IMT Charter as annexed; Control Council Law No. 10 and Art. II(1)(c); MacArthur's Special Proclamation of 19 January 1946 and the Tokyo Charter (Article 5 Class A/B/C, Article 6 responsibility); IMTFE Rules of Procedure (25 April 1946); UNGA Res. 95(I) of 11 December 1946; UNGA Res. 177(II) of 21 November 1947; ILC 1950 Nuremberg Principles
- `references/authoritative-sources.md` — comprehensive Tier 1 / Tier 2 / Never-authoritative hierarchy. Tier 1 covers: the three official published records (Blue Series 42 vols, Green Series 15 vols, Pritchard-Zaide IMTFE 22-27 vols); the digital authoritative archives (Avalon Project at Yale, Harvard Nuremberg Trials Project, Stanford Taube Archive of the IMT, University of Virginia IMTFE Digital Collection, ICC Legal Tools Database, JACAR, UN Audiovisual Library); the institutional repositories (Library of Congress, NARA, Imperial War Museums, Hoover Institution, Peace Palace Library); and specialised university collections (Creighton Delaney Tokyo Papers, University of Hawaii WCDI, UConn Dodd Papers, North Dakota, Jackson Center). Tier 2 covers Nuremberg Academy, USHMM, the major academic commentary on Nuremberg (Taylor, Harris, Smith, Conot, Heller, Schabas, Kelsen) and Tokyo (Minear, Totani, Boister-Cryer, Röling-Cassese, Tanaka-McCormack-Simpson)
- `references/citation-format.md` — five citation modes (Charter provisions, IMT Judgment, NMT cases, IMTFE Judgment with mandatory majority-vs-separate-opinion identification, Nuremberg Principles); diacritics tables (22 IMT defendants, 28 IMTFE defendants); the four counts at the IMT; Class A/B/C at the IMTFE; criminal organisations findings
- `references/verification-workflow.md` — separate fallback ladders for IMT/NMT and for IMTFE citations; capture fields; verification-level matching; **the four classic traps** explicitly enumerated; translation discipline (English/French/German/Russian at Nuremberg; English/Japanese at Tokyo)
- `references/foundational-texts.md` (covered above)
- `references/jurisprudence-map.md` — fourteen topic-by-topic sections covering doctrine across IMT, NMT, and IMTFE: legality of the tribunals (*nullum crimen*), crimes against peace, war crimes, crimes against humanity (with the IMT/CCL No. 10/IMTFE divergence on the armed-conflict nexus), criminal organisations doctrine, individual criminal responsibility, no immunity (with the line to *Mayaleh* / *Al-Assad* 25 July 2025), superior orders, conspiracy (with the IMT/IMTFE doctrinal divergence), command responsibility, the Hirohito non-indictment, the Pal dissent, the Nuremberg Principles, and the twelve NMT cases
- `references/defendants-and-judges.md` — dedicated reference: 22 IMT defendants with diacritics, positions, sentences; the four IMT counts; criminal organisations findings; 28 IMTFE defendants with positions and sentences; the Hirohito non-indictment; Class A/B/C; 11 IMTFE judges with their separate opinions; IMT and IMTFE chief prosecutors
- `examples/example-verification.md` — verifying one Nuremberg citation (the famous "men, not abstract entities" passage from the IMT Judgment) and one Tokyo citation (the Pal dissent on aggressive war), end-to-end
- `examples/example-audit.md` — three audits illustrating Trap 1 (IMT/NMT confusion via the Einsatzgruppen Case), Trap 2 (Nuremberg/Tokyo Charter article number confusion), and Trap 4 (Pal dissent attributed to "the Tribunal")

### Skill scope at v1.0.0
- Covers the **IMT** (the four-power International Military Tribunal at Nuremberg, 1945-46), the **twelve subsequent NMT** trials (US Military Tribunals at Nuremberg under Control Council Law No. 10, 1946-49), and the **IMTFE** (the International Military Tribunal for the Far East at Tokyo, 1946-48) as a single integrated skill
- Encodes the same verification-first methodology as the `icc`, `eccc`, and `icty-ictr-irmct` skills in this repository, adapted to the Nuremberg + Tokyo corpus with its multiple authoritative archives
- Positions the post-WWII tribunals as the doctrinal matrix from which the Rome Statute, the ICTY/ICTR Statutes, the ECCC Law, and the modern formulations of crimes against humanity, no-immunity, superior orders, and individual responsibility descend
- Distinguishes IMT and IMTFE precisely, treats Pal's dissent and the Hirohito non-indictment with the seriousness they deserve in post-colonial legal scholarship, and provides explicit Class A/B/C terminology guidance for the IMTFE

### Known limitations
- Other contemporary trials (the Eichmann trial in Israel; the Frankfurt Auschwitz trials; the Demjanjuk trial in Germany; the Class B/C trials at Yokohama, Manila, Singapore, Khabarovsk, and other Asia-Pacific sites; the trials of Japanese B/C-class war criminals in the colonies) are NOT covered by this skill and require their own analysis
- Specific page-pinpoints in the Blue Series, Green Series, and Pritchard-Zaide volumes are left for verification at runtime — pagination varies between editions and translations (Blue Series in English/French/German/Russian; Pritchard-Zaide in English)
- The 22-IMT-defendants and 28-IMTFE-defendants tables record fates at first instance; later clemencies, sentence commutations, and the fate of survivors over decades are not detailed here
- The Pal dissent runs to over 1,000 pages in original typescript; the Pritchard-Zaide condensed version is in Vol. 21. Specific section pagination should be verified against the edition the user has
- The Shanghai Jiao Tong University Press text-searchable Tokyo Trials database is a Tier 1 resource but is subscription-only — users without subscription should rely on UVA, ICC Legal Tools, JACAR, and Pritchard-Zaide
