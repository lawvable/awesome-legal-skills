---
name: "nuremberg-tokyo-jeanne-sulzer"
description: "Verification-first methodology for the post-WWII tribunals: the IMT at Nuremberg, the twelve Nuremberg Military Tribunals, and the IMTFE at Tokyo. Citations are verified against the official records (Blue/Green Series, Pritchard-Zaide) and the digital archives (Avalon, Harvard NTP, UVA IMTFE). Guards the four classic traps (IMT vs NMT; Nuremberg vs Tokyo; Charter article numbers; majority judgment vs separate opinions, e.g. the Pal dissent). Research aid, not legal advice. Part of the open-source \"Skills for International Justice\" library — methodology: github.com/jeannesulzer/international-criminal-tribunals-skills"
metadata:
  author: "Jeanne Sulzer"
  license: "cc-by-4.0"
  version: "2026-06-10"
---

# Nuremberg + Tokyo — the post-WWII international military tribunals

This skill governs every output that touches the three post-WWII military tribunals: the International Military Tribunal at Nuremberg (IMT), the twelve subsequent United States Nuremberg Military Tribunals (NMT), and the International Military Tribunal for the Far East at Tokyo (IMTFE). The discipline is simple and the reason for it is concrete: these tribunals are the doctrinal matrix of modern international criminal law. The London Charter's Article 6, the Tokyo Charter's Article 5, and the Nuremberg Principles formulated by the International Law Commission in 1950 are the source from which the Rome Statute, the ICTY/ICTR Statutes, the ECCC Law, and every modern international criminal jurisdiction descends. A confidently-stated but invented "Nuremberg held that …" or "Tokyo held that …" misrepresents the very foundation on which the field rests.

## The discipline in one paragraph

For any case-specific citation — the IMT Judgment, an individual defendant's conviction, a subsequent NMT case, an IMTFE finding, a passage of Robert Jackson's opening, a separate opinion at Tokyo, an exhibit — verify before citing. "Verify" means `web_fetch` (or equivalent retrieval) to the Avalon Project, the Harvard Nuremberg Trials Project, the Stanford Taube Archive of the IMT, the University of Virginia IMTFE Digital Collection, the ICC Legal Tools Database, the Library of Congress, the UN Audiovisual Library, JACAR (Japan Center for Asian Historical Records), or one of the other Tier 1 sources listed in `references/authoritative-sources.md`. Foundational instruments — the London Agreement and IMT Charter, the Tokyo Charter, Control Council Law No. 10, the ILC 1950 Nuremberg Principles, UNGA Resolutions 95(I) and 177(II) — may be cited from project knowledge when present. Nothing else may be cited from memory.

## Verification is gradient, not binary

Three levels:

- **Existence verified.** Defendant, charge, verdict, and date confirmed against an authoritative source. Sufficient for "X was convicted at Nuremberg" or "Y was sentenced to death at Tokyo".
- **Content verified.** The fetched text confirms the proposition in substance. Sufficient for "the Tribunal held that …".
- **Page or volume verified.** The specific cited page (Blue Series, Green Series, Pritchard-Zaide volumes) contains the cited proposition. Required for any quotation.

Label the level where relevant. The Judgments are massively quoted across the field, and partial paraphrases drift quickly. See `references/verification-workflow.md`.

## Standard workflow

**Step 0 — Identify the document.** Before anything else, distinguish:

- The **IMT** (the four-power trial of the major war criminals at Nuremberg, 1945-46) vs the twelve subsequent **NMT** trials (US Military Tribunals at Nuremberg under Control Council Law No. 10, 1946-49) vs the **IMTFE** (the Tokyo Trial, 1946-48). Different tribunals, different legal bases, different defendants, different sources.
- The **London Charter** (treaty of 8 August 1945, IMT) vs the **Tokyo Charter** (MacArthur's Special Proclamation of 19 January 1946, IMTFE). Often conflated; they are distinct instruments with significant differences.
- The **"Blue Series"** (the IMT proceedings, 42 volumes) vs the **"Green Series"** (the NMT proceedings, 15 volumes) vs the **Pritchard-Zaide volumes** (the IMTFE proceedings, 22-27 volumes published by Garland 1981-1987).

**Step 1 — Plan citations.** List the citations that will appear in the output and the proposition each supports.

**Step 2 — Verify with the fallback ladder.** For each citation, work down the ladder in `references/verification-workflow.md`.

**Step 3 — Draft using verified material.** Use the citation format in `references/citation-format.md`. Where verification is partial, say so.

**Step 4 — Self-audit.** Each citation must trace to project knowledge or to a successful retrieval in this conversation, with the verification level appropriate to the claim.

## Foundational texts (cite from project knowledge when present)

### Nuremberg side

- **Agreement for the Prosecution and Punishment of the Major War Criminals of the European Axis** (London, 8 August 1945), 82 U.N.T.S. 280 — the "London Agreement" or "London Charter".
- **Charter of the International Military Tribunal**, annexed to the London Agreement — the "IMT Charter". Key articles: 1 (establishment), 6 (subject-matter — crimes against peace, war crimes, crimes against humanity), 7 (no immunity), 8 (superior orders), 9-10 (criminal organisations), 14-15 (Chief Prosecutors), 19 (no technical rules of evidence), 26 (Judgment final).
- **Control Council Law No. 10** (Punishment of Persons Guilty of War Crimes, Crimes against Peace and against Humanity, 20 December 1945) — legal basis for the twelve NMT trials; Article II(1)(c) drops the armed-conflict nexus that appears in IMT Charter art. 6(c).

### Tokyo side

- **Special Proclamation by the Supreme Commander for the Allied Powers** (Tokyo, 19 January 1946) — General Douglas MacArthur's proclamation establishing the IMTFE.
- **Charter of the International Military Tribunal for the Far East**, issued by MacArthur on 19 January 1946 — the "Tokyo Charter" or "IMTFE Charter". Modelled on the IMT Charter but with notable differences:
  - **Article 5** establishes jurisdiction over three classes of crime: **Class A** (crimes against peace), **Class B** (conventional war crimes), **Class C** (crimes against humanity). The Tribunal applied Class A as the primary basis of conviction.
  - The President is appointed by MacArthur, not chosen by the judges.
  - Eleven judges from eleven Allied nations.
- **Rules of Procedure of the IMTFE** (announced 25 April 1946, with subsequent amendments).
- **Instrument of Surrender of Japan** (2 September 1945) — the legal predicate.

### Shared / cross-cutting

- **UNGA Resolution 95(I)**, 11 December 1946 — "Affirmation of the Principles of International Law recognized by the Charter of the Nürnberg Tribunal".
- **UNGA Resolution 177(II)**, 21 November 1947 — mandate to the International Law Commission to formulate the Nuremberg Principles.
- **Principles of International Law recognized in the Charter of the Nürnberg Tribunal and in the Judgment of the Tribunal**, ILC, 1950 (*Yearbook of the International Law Commission*, 1950, Vol. II) — the seven Nuremberg Principles.

If not in project knowledge, retrieve from the sources listed in `references/authoritative-sources.md`. See `references/foundational-texts.md`.

## The institutional architecture (get this right)

### IMT — International Military Tribunal at Nuremberg

- Established: **London Agreement, 8 August 1945**
- Seat: **Nuremberg, Germany**
- Trial dates: **20 November 1945 – 1 October 1946** (proceedings began 14 November; opening statements 20-21 November; judgment 30 September – 1 October 1946)
- Composition: four judges (one from each of the four Allied powers — US, UK, USSR, France), plus alternates
- Chief Prosecutors: Robert H. Jackson (US), Hartley Shawcross (UK), Roman Rudenko (USSR), François de Menthon then Auguste Champetier de Ribes (France)
- Defendants: 24 indicted; 22 tried (Ley suicide, Krupp unfit); 12 death sentences, 3 life, 4 terms, 3 acquittals (Schacht, von Papen, Fritzsche), 1 in absentia (Bormann)
- Six organisations indicted; three declared criminal (Leadership Corps of the Nazi Party, Gestapo and SD, SS); three acquitted (SA, Reich Cabinet, General Staff and High Command)

### NMT — Twelve subsequent US Nuremberg Military Tribunals

- Held: **Nuremberg, October 1946 – April 1949**
- Legal basis: **Control Council Law No. 10**
- Tribunals: US judges only, in six tribunals operating in parallel; twelve cases tried
- Lead authority: Brigadier General Telford Taylor (Chief of Counsel for War Crimes)
- The twelve cases (in shorthand): Doctors' Trial, Milch, Justice Case, Pohl, Flick, IG Farben (Krauch et al.), Hostages Case (List et al.), RuSHA (Greifelt et al.), Einsatzgruppen (Ohlendorf et al.), Krupp, Ministries (Weizsäcker et al.), High Command (von Leeb et al.)

### IMTFE — International Military Tribunal for the Far East

- Established: **MacArthur's Special Proclamation of 19 January 1946**
- Seat: **Tokyo, Japan** (former building of the Japanese Ministry of War, Ichigaya)
- Trial dates: **3 May 1946 – 12 November 1948** (proceedings commenced 29 April 1946; judgment read 4-12 November 1948)
- Composition: **eleven judges** from eleven nations — Australia (Sir William Webb, President), Canada, China, France (Henri Bernard), India (Radhabinod Pal), Netherlands (B.V.A. Röling), New Zealand, the Philippines (Delfin Jaranilla), the Soviet Union, the United Kingdom, the United States
- Chief Prosecutor: Joseph B. Keenan (US)
- Defendants: **28 indicted; 25 judged** (Matsuoka and Nagano died during trial; Ōkawa declared mentally unfit). 7 death sentences (Tojo, Hirota, Doihara, Itagaki, Kimura, Matsui, Mutō), 16 life imprisonment, 1 twenty-year term (Tōgō), 1 seven-year term (Shigemitsu)
- Five **separate opinions** published outside the court — including the famous **Pal dissent** (acquittal of all), **Röling dissent**, **Bernard dissent**, **Webb separate opinion**, **Jaranilla separate opinion**. These are not part of the operative Judgment but are extensively cited in scholarship and in post-colonial legal critique.

## Source hierarchy

**Tier 1 (authoritative):**

*Primary record (the trials' own outputs):*
- **The Blue Series** — *Trial of the Major War Criminals before the International Military Tribunal*, 42 vols. (IMT 1947-1949)
- **The Green Series** — *Trials of War Criminals Before the Nuernberg Military Tribunals under Control Council Law No. 10*, 15 vols. (US GPO 1949-1953)
- **The Pritchard-Zaide volumes** — *The Tokyo War Crimes Trial*, ed. R J Pritchard & S M Zaide, 22-27 vols. (Garland Publishing, New York 1981-1987) — the published transcripts of IMTFE proceedings

*Digital authoritative archives:*
- **Avalon Project at Yale Law School** (`https://avalon.law.yale.edu/subject_menus/imt.asp`) — IMT Charter, Indictment, selected proceedings, Judgment, Jackson statements
- **Harvard Nuremberg Trials Project** (`https://nuremberg.law.harvard.edu/`) — ~1 million pages, 690 boxes, digitised 1998-2017; the largest dedicated IMT/NMT digital corpus
- **Stanford Taube Archive of the IMT** (Stanford Libraries, opened 2021) — 250,000+ pages, 5,000+ trial records, **multilingual transcripts** in English, French, German, Russian
- **University of Virginia IMTFE Digital Collection** (`https://imtfe.law.virginia.edu/`) — the dedicated digital hub for the Tokyo Trial
- **ICC Legal Tools Database** (`https://www.legal-tools.org/`) — IMTFE complete English transcripts and exhibits, plus IMT and NMT materials
- **JACAR — Japan Center for Asian Historical Records** (National Archives of Japan) — IMTFE transcripts in English AND Japanese
- **UN Audiovisual Library of International Law** (`https://legal.un.org/avl/`) — UNGA Resolutions 95(I), 177(II), ILC 1950 Nuremberg Principles

*Tier 1 institutional repositories (US, UK, Japan):*
- **Library of Congress** (`https://www.loc.gov/`) — Blue Series and Green Series digitisations
- **National Archives (NARA, USA)** — RG 153, 238, 549
- **Imperial War Museums (UK)** — Records of the IMT and IMTFE (FO 645 series for IMT; FO 648 series for IMTFE)
- **Hoover Institution Library & Archives, Stanford** — IMTFE records collection
- **Peace Palace Library, The Hague** — Tokyo Trial research guide and holdings

*Tier 1 university collections (specialised):*
- **Creighton University — Delaney Tokyo Trial Papers** — IMTFE materials donated by US prosecution staff
- **University of Hawaii at Manoa — War Crimes Documentation Initiative (WCDI)** (`https://manoa.hawaii.edu/wcdi/`) — Asia-Pacific war crimes trials, including IMTFE prosecution exhibits
- **University of Connecticut — Dodd Papers** — papers of Thomas J. Dodd, US Executive Trial Counsel at the IMT
- **University of North Dakota Nuremberg Trials Digital Collection**
- **Robert H. Jackson Center** (`https://www.roberthjackson.org/`) — Jackson's papers and speeches

**Tier 2 (secondary, must be labelled):**
- **International Nuremberg Principles Academy** (`https://www.nurembergacademy.org/`) — the contemporary institutional voice on the Nuremberg legacy
- **United States Holocaust Memorial Museum** (`https://encyclopedia.ushmm.org/`) — authoritative on historical context; Tier 2 for legal propositions
- **Academic commentary** — Telford Taylor, *The Anatomy of the Nuremberg Trials*; Whitney R. Harris, *Tyranny on Trial*; Bradley F. Smith, *Reaching Judgment at Nuremberg*; Robert E. Conot, *Justice at Nuremberg*; Kevin Jon Heller, *The Nuremberg Military Tribunals and the Origins of International Criminal Law*; for Tokyo — Richard H. Minear, *Victors' Justice*; Yuma Totani, *The Tokyo War Crimes Trial*; Neil Boister & Robert Cryer, *The Tokyo International Military Tribunal: A Reappraisal* (OUP 2008); B.V.A. Röling & Antonio Cassese, *The Tokyo Trial and Beyond*; the *Journal of International Criminal Justice* symposia on Tokyo
- **Shanghai Jiao Tong University Press — Database of the Tokyo Trials Literature** (subscription) — text-searchable English transcripts

**Never authoritative:** Wikipedia, Grokipedia, social media, AI-generated summaries, blogs.

See `references/authoritative-sources.md` for the full hierarchy with URLs.

## Citation format

Five distinct citation modes — see `references/citation-format.md` for worked examples:

1. **Charter / Statute provisions** — *IMT Charter*, art. 6; *Tokyo Charter*, art. 5; *Control Council Law No. 10*, art. II(1)(c)
2. **The IMT Judgment** — Blue Series Vol. I or Vol. XXII, or Oxford ICL form *France et al. v. Göring et al.*, [1946] 22 IMT 203
3. **NMT cases** — *United States v. [Defendant]*, Green Series Vol. [n]
4. **The IMTFE Judgment** — *International Military Tribunal for the Far East v. Araki et al.*, Judgment of 4-12 November 1948, in Pritchard-Zaide Vol. 20 (Judgment and Annexes); separate opinions in Vol. 21
5. **Nuremberg Principles** — *Nuremberg Principles*, ILC 1950, Principle [I-VII]

See `references/citation-format.md` for the names-and-spellings tables (22 IMT defendants, 28 IMTFE defendants, 11 IMTFE judges).

## Audit mode

When the user supplies a document containing Nuremberg / Tokyo citations:
- **Working drafts**: verify each citation against Tier 1. Watch for **the four classic traps** — (1) IMT vs NMT, (2) IMT/Nuremberg vs IMTFE/Tokyo, (3) IMT Charter Art. 6 categories vs Tokyo Charter Class A/B/C, (4) majority Judgment vs separate opinions (especially Pal, often quoted as "the Tribunal said" when it is in fact dissent).
- **Final published texts**: treat as inventory; identify the editions, translations, and volumes cited.

See `examples/example-audit.md`.

## Substantive doctrine — pointers

Where the field's central doctrines originate at Nuremberg and Tokyo:

- **Crimes against humanity as an autonomous category** → IMT Charter art. 6(c); Tokyo Charter art. 5(c) (rarely applied at Tokyo, the bulk of convictions there rested on Class A and Class B); Control Council Law No. 10 art. II(1)(c) — the CCL No. 10 formulation drops the armed-conflict nexus and is the doctrinal step forward
- **Individual criminal responsibility under international law** → IMT Charter art. 6 (closing words); IMT Judgment, "Crimes against international law are committed by men, not by abstract entities…"
- **No immunity for heads of State and senior officials** → IMT Charter art. 7; Tokyo Charter art. 6 (parallel provision). Doctrinal line to the Mayaleh / Al-Assad rulings of the French Cour de cassation (Ass. plén., 25 July 2025) and to Rome Statute Article 27
- **Superior orders not a defence** → IMT Charter art. 8; Tokyo Charter art. 6; NMT refinements (the "moral choice" qualification, Einsatzgruppen Case and High Command Case)
- **Aggressive war as "the supreme international crime"** → IMT Judgment; central holding of the IMTFE Judgment (most Tokyo convictions rested on Class A)
- **Criminal organisations** → IMT Charter arts. 9-10; SS, Gestapo/SD, and Leadership Corps declared criminal; SA, Reich Cabinet, General Staff and High Command acquitted as organisations
- **Crimes against humanity without armed-conflict nexus** → developed at the NMT (Justice Case, Einsatzgruppen Case) under CCL No. 10
- **Hirohito's non-indictment** → a deliberate prosecutorial / political choice at Tokyo; central to the post-colonial critique of the IMTFE
- **The Pal dissent** → a substantive challenge to the legality of the entire proceedings, on grounds of *nullum crimen sine lege*, victors' justice, and the colonial context; foundational text of post-colonial international legal critique
- **The Nuremberg Principles (ILC 1950)** — Principles I-VII; the codification of the Nuremberg / Tokyo heritage as customary international law

The skill does not encode doctrine line by line; the Charters, the Judgments, the NMT cases, and the ILC formulation do that. For each, verify the specific passage through the workflow before citing. See `references/jurisprudence-map.md`.

## Sensitive contexts

These tribunals adjudicated the Holocaust, the mass killings on the Eastern Front, medical experimentation in the camps, the Nanjing Massacre, the Bataan Death March, sexual slavery (the "comfort women" issue was raised but not adjudicated at Tokyo — a known critique of the IMTFE), and biological warfare (Unit 731 — controversially not prosecuted at Tokyo). Outputs are read by descendants of victims, by historians of the period, and by jurists who treat the Judgments as foundational. Maintain factual precision, avoid sensationalism, avoid Holocaust comparisons that the record does not support, and never minimise. Use historical names of places correctly (Auschwitz, Treblinka, Sobibór, Bełżec; Nanjing/Nanking, Manila, Bataan; SS, SD, Gestapo, Einsatzgruppen, Kempeitai, Unit 731). The Tribunals' findings about specific atrocities are part of the historical record by virtue of the Judgments — quoting them accurately matters.

## What this skill is not

- Not legal advice. Outputs are research and drafting aids.
- Not a substitute for the Blue Series, the Green Series, the Pritchard-Zaide volumes, or the underlying primary documents.
- Not exhaustive: this skill covers IMT + NMT + IMTFE. Other contemporary trials (the Eichmann trial in Israel, the Frankfurt Auschwitz trials, the Demjanjuk trial in Germany, the Class B/C trials at Yokohama, Manila, Singapore, Khabarovsk, etc.) are NOT covered by this skill and require their own analysis.
- Not endorsed by any institution. This is an independent open-source project.

## Reference files

- `references/authoritative-sources.md` — full source hierarchy, URLs, and indication of what each archive covers
- `references/citation-format.md` — citation rules for IMT Charter, IMT Judgment (Blue Series + Oxford ICL), NMT cases (Green Series), IMTFE Charter, IMTFE Judgment (Pritchard-Zaide), separate opinions, Nuremberg Principles, UNGA Resolutions; defendants tables
- `references/verification-workflow.md` — fallback ladder, the four classic traps (IMT/NMT, IMT/IMTFE, Charter categories, Judgment vs separate opinions), translation discipline
- `references/foundational-texts.md` — London Agreement, IMT Charter, CCL No. 10, MacArthur Special Proclamation, Tokyo Charter, UNGA Res. 95(I) and 177(II), ILC Nuremberg Principles 1950
- `references/jurisprudence-map.md` — topic-by-topic map of holdings across IMT, NMT, and IMTFE
- `references/defendants-and-judges.md` — names, spellings, charges, fates for the 22 IMT defendants and the 28 IMTFE defendants; the 11 IMTFE judges with their opinions
- `examples/example-verification.md` — verifying one Nuremberg citation and one Tokyo citation end-to-end
- `examples/example-audit.md` — auditing user-supplied documents, with traps to watch for
