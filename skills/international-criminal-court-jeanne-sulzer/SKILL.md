---
name: "icc-jeanne-sulzer"
description: "Research, drafting, and analysis involving the International Criminal Court (Rome Statute system). Enforces a verification-first methodology — every case-law, decision, filing, warrant, and statement citation is verified against an authoritative primary source (icc-cpi.int, legal-tools.org) in the current conversation before it appears in an output. Foundational texts (Rome Statute, Elements of Crimes, RPE, Regulations of the Court) may be cited from project knowledge when present. Use whenever the user is working with ICC case law, OTP statements, ASP documents, or ICC procedure."
metadata:
  author: "Jeanne Sulzer"
  license: "cc-by-4.0"
  version: "2026-06-05"
---

# ICC skill

## Core discipline

For any case-specific document — judgment, decision, warrant, filing, OTP
statement — **verify before citing**. Verification means retrieving the
document from a Tier 1 source (icc-cpi.int, legal-tools.org, asp.icc-cpi.int)
in the current conversation. The four foundational texts (Rome Statute,
Elements of Crimes, Rules of Procedure and Evidence, Regulations of the
Court) are the only exception, and only when they are present in project
knowledge.

Nothing else may be cited from memory. Inventing a document number, a date,
or a paragraph reference is the single failure mode this skill exists to
prevent.

## When to use this skill

- The user asks a question that requires citing ICC case law, decisions,
  warrants, OTP statements, ASP resolutions, or ICC procedural texts.
- The user supplies an ICC filing or judgment for analysis or audit.
- The user is drafting something — a memo, a brief section, a research
  note — that will reference ICC instruments or case law.
- The user asks about Rome Statute interpretation, command responsibility,
  modes of liability, war crimes / crimes against humanity / genocide /
  aggression elements, victim participation, reparations, or other
  Statute-grounded questions.

If the question is about another tribunal (ICTY, ICTR, MICT, SCSL, STL,
ECCC, KSC, or hybrid mechanisms), this skill does not apply — use the
relevant tribunal's skill or, if none exists, surface that to the user.

## Workflow

The full procedure is in `references/verification-workflow.md`. The short
form:

1. **Identify the document.** Read what is actually in front of you; if the
   user names a case or document, disambiguate against the document's own
   header before proceeding. (Bemba TJ vs. Bemba AJ; Ntaganda 2017
   interlocutory vs. 2021 final appeal — identity errors propagate.)
2. **List every citation that will appear** in the planned output, with the
   proposition each supports.
3. **Verify each citation.** Work the fallback ladder:
   icc-cpi.int → legal-tools.org → search-result snippet from a Tier 1
   domain → ICC press release → authoritative secondary database (e.g.
   OUP ORIL) → ask the user. Stop at the first level that satisfies what
   the claim needs.
4. **Match verification level to claim.** Three levels: **Existence**
   (document, number, date, chamber), **Content** (the document holds, in
   substance, what the output says it holds), **Paragraph** (the cited
   paragraph contains the cited proposition). Pinpoint quotations require
   paragraph-level verification. If verification stops short, soften the
   claim or flag it explicitly.
5. **Draft using verified material.** Use the citation formats in
   `references/citation-format.md`.
6. **Self-audit.** Walk every citation in the draft: from project knowledge
   or from this conversation's retrieval? Does the proposition match? Is
   the verification level appropriate to the claim?

## Reference materials

Read these as needed; they are the operational detail behind the workflow
above.

- `references/authoritative-sources.md` — Tier 1 / Tier 2 / do-not-cite
  source hierarchy; the icc-cpi.int 403 fallback ladder.
- `references/citation-format.md` — exact formats for the Rome Statute,
  Elements of Crimes, RPE, Regulations, decisions, warrants, OTP
  statements, ASP documents. Includes the Article 28 numbering discipline
  — the Rome Statute uses `28(a)` (military commanders) and `28(b)` (other
  superiors), with no numbered paragraphs; the non-statutory `28(1)/(2)`
  form is the trap to avoid.
- `references/verification-workflow.md` — the full operational procedure,
  the three-level verification gradient, a worked Bemba example.
- `references/foundational-texts.md` — the four foundational texts and
  what is *not* foundational (case law, OTP policy papers, most ASP
  resolutions, Regulations of the Registry/OTP, professional codes).

## Worked examples

- `examples/example-verification.md` — two end-to-end examples: full
  paragraph-level verification (Bemba effective control) and partial
  verification when icc-cpi.int blocks (Ntaganda 2017 jurisdiction).
- `examples/example-audit.md` — two audit modes: working draft (the user
  wrote it; citations are claims to be checked) vs. finalised Court record
  (the Court issued it; citations are part of the record, and the audit
  is about how downstream work uses them).

## What this skill is not

- **Not legal advice.** Outputs are research and drafting aids for users
  who understand international criminal law.
- **Not a substitute for primary documents.** A skill that follows this
  workflow can produce accurate citations and disciplined drafts; only the
  user can decide what to do with them.
- **Not endorsed by the Court.** Independent open-source project.

## Hard rules

These are non-negotiable. Edits or workarounds that weaken them defeat the
skill.

1. No case-specific citation from memory. Verify in-conversation.
2. Public-redacted (`-Red`) versions only in public outputs. Confidential
   filings (`-Conf`, `-Conf-Exp`) are not citable from a public output,
   ever — even when the user has lawful access to the confidential version,
   cite the `-Red` counterpart.
3. The Statute's own numbering governs. For Article 28, that means
   `Article 28(a)` (military commanders) and `Article 28(b)` (other
   superiors) — not the non-statutory `28(1)/(2)` form — in anything that
   will be filed, read by judges or counsel, or quote the Statute.
4. Secondary sources (HRW, Amnesty, UN bodies, academic commentary, news)
   are clearly separable in the output and never used to establish what
   the Court has said or held.
5. icc-cpi.int 403s are structural, not failures. Work the fallback ladder;
   do not abandon a real citation because the direct fetch was blocked.
