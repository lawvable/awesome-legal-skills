---
name: "icty-ictr-irmct-jeanne-sulzer"
description: "Verification-first methodology for the ICTY, the ICTR and the Residual Mechanism (IRMCT). Citations are verified against irmct.org, the Case Law and Unified Court Records databases, and legal-tools.org. Handles the IT/ICTR to MICT case-number transition (Karadžić, Mladić) and the protective-measures rule. Research aid, not legal advice. Part of the open-source \"Skills for International Justice\" library - methodology: github.com/jeannesulzer/international-criminal-tribunals-skills"
metadata:
  author: "Jeanne Sulzer"
  license: "cc-by-4.0"
  version: "2026-06-09"
---

# ICTY / ICTR / IRMCT — the ad hoc tribunals and the Mechanism

This skill governs every output that touches the International Criminal Tribunal for the former Yugoslavia, the International Criminal Tribunal for Rwanda, and the International Residual Mechanism for Criminal Tribunals. The discipline is simple and the reason for it is concrete: these tribunals produced the foundational jurisprudence of modern international criminal law, their case numbers and document references are exact, and a fabricated citation in this field misrepresents the holdings on which the entire field rests — and on which victims of the Srebrenica and Rwanda genocides, among others, obtained justice.

## The discipline in one paragraph

For any case-specific document — judgment, decision, indictment, appeal judgment, sentencing judgment, filing, OTP submission — verify before citing. "Verify" means `web_fetch` (or equivalent retrieval) to irmct.org, the legacy ICTY/ICTR sites, the Unified Court Records (UCR) database, or legal-tools.org in the current conversation. Foundational instruments (the ICTY Statute, the ICTR Statute, the IRMCT Statute, the Rules of Procedure and Evidence of each) may be cited from project knowledge when present. Nothing else may be cited from memory.

## Verification is gradient, not binary

In practice, retrieval to these sources usually succeeds. Three levels:

- **Existence verified.** Case number, party name, document type, date, and chamber confirmed against an authoritative source. Sufficient for "X was convicted of genocide in case Y."
- **Content verified.** The fetched text confirms the document says, in substance, what the output claims it says. Sufficient for "the Chamber held that …".
- **Paragraph verified.** The specific cited paragraph(s) contain the cited proposition. Required for any quotation and for any paragraph-pinpoint citation.

Label the level where relevant. Do not silently downgrade — a "the Appeals Chamber held X" claim that is only existence-verified is not honest if the output doesn't say so. See `references/verification-workflow.md`.

## Standard workflow

**Step 0 — Identify the document(s).** Before anything else, read what is actually in front of you. If the user provides a file, open it and confirm the case number, party name, document type, date, and chamber. **Identity errors propagate**: confusing ICTY case IT-94-1 (Tadić) with a Mechanism case number, or attributing an ICTR holding to the ICTY, corrupts everything downstream. The same accused may appear under an ICTY/ICTR number *and* a later MICT number (e.g. Karadžić: ICTY IT-95-5/18, then MICT-13-55 on appeal). Resolve this at Step 0.

**Step 1 — Plan citations.** List every citation that will appear in the output. For each, note the proposition it supports and the source to verify against.

**Step 2 — Verify with the fallback ladder.** For each case-specific citation, work the ladder in `references/verification-workflow.md`: irmct.org / UCR database → legacy ICTY or ICTR site → legal-tools.org → secondary source (clearly labelled) → ask the user. Capture case number, document type, chamber, date, and paragraph. Confirm the cited passage supports the proposition.

**Step 3 — Draft using verified material.** Use the citation format in `references/citation-format.md`. Where verification is partial, say so in the output.

**Step 4 — Self-audit.** Each citation must trace either to project knowledge (foundational text) or to a successful retrieval in this conversation, with verification level appropriate to the claim. If not, the citation comes out or the claim is softened to what the verification actually supports.

## Foundational texts (cite from project knowledge when present)

- **Statute of the International Criminal Tribunal for the former Yugoslavia** — annexed to the report of the Secretary-General pursuant to UN Security Council **Resolution 808 (1993)**, adopted by **Resolution 827 (1993)** of 25 May 1993, as subsequently amended. "ICTY Statute".
- **Statute of the International Criminal Tribunal for Rwanda** — adopted by UN Security Council **Resolution 955 (1994)** of 8 November 1994, as subsequently amended. "ICTR Statute".
- **Statute of the International Residual Mechanism for Criminal Tribunals** — annexed to UN Security Council **Resolution 1966 (2010)** of 22 December 2010. "IRMCT Statute" or "Mechanism Statute".
- **Rules of Procedure and Evidence** of the ICTY, of the ICTR, and of the Mechanism — each amended many times; the revision in force at the date of a cited decision controls.
- **Transitional Arrangements** annexed to Resolution 1966 (2010) — govern which institution (tribunal or Mechanism) has competence over a given proceeding by reference to the date of filing.

If not in project knowledge, retrieve from irmct.org/en/documents/basic-documents before citing. See `references/foundational-texts.md`.

## The institutional architecture (get this right)

- **ICTY** — established 25 May 1993 (Res. 827); seat in The Hague; **closed 31 December 2017**. Jurisdiction: serious violations of international humanitarian law committed in the territory of the former Yugoslavia since 1991.
- **ICTR** — established 8 November 1994 (Res. 955); seat in Arusha; **closed 31 December 2015**. Jurisdiction: genocide and other serious violations committed in Rwanda, and by Rwandans in neighbouring States, between 1 January and 31 December 1994.
- **IRMCT / MICT / "the Mechanism"** — established 22 December 2010 (Res. 1966). **Arusha branch operational 1 July 2012** (ICTR functions); **The Hague branch operational 1 July 2013** (ICTY functions). One President, one Prosecutor, one Registrar common to both branches. Continues the jurisdiction, rights, obligations, and essential functions of the two tribunals; cannot issue new indictments (save for contempt and false testimony).

**Competence rule:** under the Transitional Arrangements (Res. 1966), the Mechanism has competence over an appeal where the notice of appeal was filed on or after the branch's commencement date. This is why late ICTY cases (Karadžić, Mladić, Šešelj, Stanišić & Simatović) were decided on appeal by the **Mechanism** under MICT case numbers, even though the trial was an ICTY proceeding under an IT case number.

## Source hierarchy

**Tier 1 (authoritative):** irmct.org (the Mechanism, which hosts the legacy of both tribunals), the Unified Court Records database (ucr.irmct.org), the Case Law Database (cld.irmct.org), the legacy sites icty.org and unictr.irmct.org, and legal-tools.org. Always citable.
**Tier 2 (secondary, must be labelled):** UN documents (un.org), academic commentary (Journal of International Criminal Justice, Schabas, Cassese, Mettraux), trial-monitoring and NGO reports, journalism. Never authoritative on the tribunals' own findings.
**Never authoritative:** Wikipedia, Grokipedia, social media, AI summaries, blogs.

See `references/authoritative-sources.md`.

## Citation format

ICTY, ICTR, and Mechanism citations are precise and structurally specific. The anatomy:

1. **Party designation** — *Prosecutor v. [Surname]* (e.g. *Prosecutor v. Tadić*). Some cases are known by a nickname in parentheses (e.g. *Prosecutor v. Delalić et al.* (**Čelebići**); *Prosecutor v. Kunarac et al.* (**Foča**)).
2. **Case number** — encodes the tribunal and year:
   - **ICTY**: `IT-[year]-[number]` (e.g. `IT-94-1` Tadić; `IT-98-33` Krstić; `IT-96-23 & IT-96-23/1` Kunarac et al.; `IT-09-92` Mladić)
   - **ICTR**: `ICTR-[year]-[number]` (e.g. `ICTR-96-4` Akayesu; `ICTR-97-23` Kambanda)
   - **IRMCT**: `MICT-[year]-[number]` (e.g. `MICT-13-55` Karadžić; `MICT-13-56` Mladić; `MICT-13-38` Kabuga)
3. **Phase / document suffix** — `-T` (Trial Chamber), `-A` (Appeals Chamber), `-AR72` and similar (interlocutory appeals), `-PT` (pre-trial), `-R` (review), `-ES` (enforcement of sentence), `-S` (sentencing). E.g. `IT-94-1-AR72` is the Tadić interlocutory appeal on jurisdiction; `ICTR-96-4-T` is the Akayesu trial judgment; `MICT-13-56-A` is the Mladić appeal judgment.
4. **Document title, chamber, date, paragraph** — e.g. *Prosecutor v. Akayesu*, Case No. ICTR-96-4-T, Judgment (Trial Chamber), 2 September 1998, para. 731.

See `references/citation-format.md` for the full convention and `references/jurisprudence-map.md` for the landmark holdings and where they live.

## Audit mode depends on document type

When the user supplies a document, the right audit task depends on what kind of document it is:

- **Working drafts** (briefs, memos, submissions in progress): audit citations for accuracy. Existence and proposition need verification.
- **Final court records** (judgments, decisions issued by the Chambers): citations within the document are by definition Court-issued. The audit task shifts to inventorying which referenced documents downstream work depends on, and distinguishing public from confidential or redacted versions.

In either mode, Step 0 (identify the document) comes first. See `examples/example-audit.md`.

## Substantive doctrine — pointers

The skill does not encode doctrine line by line; the foundational texts and the tribunals' own judgments do that. For starting points (subject-matter holdings) the landmark authorities are mapped in `references/jurisprudence-map.md`, including:

- **Genocide** → *Akayesu* (ICTR-96-4, first genocide conviction by an international court; rape as a constitutive act of genocide); *Krstić* (IT-98-33, Srebrenica as genocide); *Karadžić* and *Mladić* (Mechanism appeals on Srebrenica genocide)
- **Direct and public incitement to genocide** → *Akayesu*; the "Media case" *Nahimana et al.* (ICTR-99-52)
- **Crimes against humanity** → *Tadić* (IT-94-1, the foundational chapeau and nexus holdings); *Kunarac et al.* (IT-96-23, enslavement and rape as crimes against humanity)
- **War crimes / the law of armed conflict** → *Tadić* interlocutory appeal (IT-94-1-AR72, the existence and classification of armed conflict; individual criminal responsibility under customary international law)
- **Joint Criminal Enterprise (JCE)** → *Tadić* Appeal Judgment (IT-94-1-A) is the foundational articulation of JCE I, II and III at the ad hoc tribunals — note this is the source the ECCC and other courts engaged with and sometimes departed from
- **Command / superior responsibility** → *Čelebići* (*Delalić et al.*, IT-96-21); *Blaškić* (IT-95-14)
- **Torture** → *Furundžija* (IT-95-17/1)
- **Sexual violence as an international crime** → *Akayesu* (ICTR-96-4); *Kunarac et al.* (IT-96-23)
- **Guilty plea by a head of government** → *Kambanda* (ICTR-97-23)

For any of these, verify the specific decision and paragraph through the workflow before citing.

## Sensitive contexts

These tribunals adjudicated the Srebrenica genocide, the genocide against the Tutsi in Rwanda, mass sexual violence, and the siege of Sarajevo. Outputs may be read by survivors, victims' associations, and the communities concerned. Maintain factual precision, avoid sensationalism, respect protective measures (many witnesses testified under pseudonym or with redactions — never attempt to identify a protected witness), and use the public, non-confidential versions of documents. Where a document exists in a public redacted version and a confidential version, cite the public version and say so.

## What this skill is not

- Not legal advice. Outputs are research and drafting aids.
- Not a substitute for the tribunals' records.
- Not exhaustive — where the foundational text or a verified decision is silent, say so.
- Not endorsed by the Mechanism, the United Nations, or any tribunal. This is an independent open-source project.

## Reference files

- `references/authoritative-sources.md` — source hierarchy and URL patterns specific to the ICTY, ICTR, and Mechanism
- `references/citation-format.md` — case-number anatomy, phase suffixes, party-designation conventions, the IT/ICTR/MICT distinction, and a table of frequently cited authorities
- `references/verification-workflow.md` — step-by-step procedure, fallback ladder, partial-verification handling, protective-measures discipline
- `references/foundational-texts.md` — the three Statutes, the Rules of Procedure and Evidence, and the Transitional Arrangements, and how to work with them
- `references/jurisprudence-map.md` — topic-by-topic map of the landmark holdings across the two tribunals and the Mechanism
- `examples/example-verification.md` — verifying a single citation end-to-end
- `examples/example-audit.md` — auditing user-supplied documents (working drafts and final records)
