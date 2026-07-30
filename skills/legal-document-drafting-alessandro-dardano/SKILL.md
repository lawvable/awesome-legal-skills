---
name: "legal-document-drafting-formatting-alessandro-dardano"
description: >-
  Produces properly-formatted legal documents in Word (.docx). The user 
  provides the substantive content (instructions, attached files, project 
  knowledge); the skill handles document architecture and formatting.
  
  * No precedent or template required
  * Seven document families: agreements, corporate documents, litigation, 
    memos, employment, policies, correspondence
  * Jurisdiction-agnostic — works across any legal system the user specifies
  * Multi-Chain numbering, defined-terms convention, structured recitals, 
    atomic signature blocks
  * Also reformats existing .docx to a consistent house style
  * Works in Claude.ai, Cowork, and Claude for Word
license: Apache-2.0
author: Alessandro Dardano
metadata:
  author: "Alessandro Dardano"
  license: "apache-2.0"
  version: "2026-06-03"
---

# In-House Counsel Document Format — Multi-Track House Style

*Author: Alessandro Dardano. Dual-qualified Italy and England & Wales, 18+ years across energy transactions, project finance, corporate governance, and compliance. Originally developed for in-house use, generalised for publication.*

*Version 2.3 — restructured for progressive disclosure: this SKILL.md is now a lean router, and the detailed material lives in `references/` modules that are read only when relevant. The MC template is a **deployer-supplied, optional** asset (`assets/inhouse-mc-template.docx`); where it is absent, MC tracks fall back to docx-js native automatic numbering (Environment 2). v2.3 corrects the earlier text that implied the template was bundled, aligns the `assets/` README accordingly, and adds a reformatting note on numbering that is itself cross-referenced (e.g., lettered article inserts). Substantive drafting content is unchanged from v2.1.*

*Licensed under Apache 2.0. © 2026 Alessandro Dardano. See LICENSE file for terms.*

> **Disclaimer.** This skill encodes document drafting and formatting conventions. It is not legal advice. Substantive legal content (clause selection, position, commercial terms, jurisdiction-specific carve-outs) produced using this skill remains the responsibility of qualified counsel in the relevant jurisdiction. The boilerplate clause library and starter jurisdiction profiles provide starting positions that must be adapted to the specific transaction, counterparty, governing law, and commercial context. Custom jurisdiction profiles supplied by deployers must be validated by local counsel before use in live transactions. Use of this skill does not create an attorney-client relationship.

## Purpose

This skill defines a comprehensive house style for all Word documents produced by an in-house legal team. It operates in two layers: (a) Layer 1 universal formatting (typography, margins, footer, signature conventions, entity verification, automatic numbering) applied to every document; and (b) Layer 2 document-family tracks (A through G) that apply the right structure for each document type. Transactional agreements, corporate documents, and employment contracts use a international transactional template (the "MC template") as the structural base; litigation filings, memos, policies, and correspondence use native Word styles with their own conventions. Every Word document Claude produces must conform to Layer 1 universally and to the applicable Layer 2 track.

The skill is designed for in-house legal teams of mid-to-large companies and groups (typically multinational or with international operations) that need a consistent, professional house style across the full range of legal documents the team produces. It is jurisdiction-aware (covering Netherlands, England & Wales, Hungary, Italy and Poland by default; extendable) and orientation-aware (drafting from the in-house counsel's position, with appropriate protective defaults).

## Terminology

Throughout this skill, the following abbreviations are used:

- **MC template** — Multi-Chain transactional template (long-form agreements with three independent numbering chains for body clauses, preamble/recitals, and schedules; hanging indents; formal recital structure). Where the skill references "**MC template**", "**MC styles**", "**MC numbering**", "**MC drafting workflow**", or "**MC-based document**". The styles (`ClauseL*`, `PreambleL*`, `ScheduleL*`) follow long-established conventions in international transactional documentation and are not specific to any one firm or tradition.
- **The Company** — the in-house team's employer entity or group. Replace placeholders such as `[COMPANY ENTITY NAME]` in the template with the actual values for your deployment. The MC template itself (`assets/inhouse-mc-template.docx`) is **deployer-supplied and optional** — drop in your own in-house template carrying the MC styles (`ClauseL*`, `PreambleL*`, `ScheduleL*`) with numbering chains numId=6 (body), numId=4 (preamble/recitals) and per-schedule chains. It is **not required for the skill to function**: where no template is present, the MC tracks fall back to docx-js native multi-level numbering (Environment 2 in `references/workflow.md`), which produces equivalent automatic numbering. Provide the template only to use Environment 1's full named-style styleset, or ask Claude to generate a verified generic MC template.
- **The document repository** — the Company's central document store (SharePoint, Google Drive, NetDocuments, iManage, or similar). Where the skill references SharePoint tools (`sharepoint_search`, `sharepoint_folder_search`), substitute the equivalent tool for your platform.

## Jurisdiction Architecture

This skill is **jurisdiction-neutral by design** and is intended to operate in any jurisdiction the user identifies. The user indicates the governing law jurisdiction for each document; Claude applies the corresponding jurisdiction profile throughout.

### How it works

1. **At the start of every drafting task** (or whenever a jurisdiction-dependent decision arises), Claude identifies the applicable jurisdiction:
   - From explicit user instruction ("draft a Dutch law SPA", "this is governed by English law")
   - From context (counterparty location, project location, Company entity involved, prior conversation)
   - By **asking the user** if jurisdiction is unclear and material to the drafting

2. **Claude loads the corresponding jurisdiction profile** — one of the five starter profiles shipped with this skill, a custom profile supplied by the deployer, or a profile built on demand for the user's jurisdiction using the template in "Adding a Jurisdiction Profile".

3. **Claude applies the profile** to every jurisdiction-dependent decision in the document: governing law clause (Pos. 22), payments/interest mechanism (Pos. 7), good faith treatment (Pos. 10), civil code remedies waiver (Pos. 14), third-party rights exclusion (Pos. 17), construction rules addendum (Pos. 1.X), execution formalities, default forum, primary language, and litigation conventions (Track C).

### Starter jurisdiction profiles (worked examples)

The skill ships with five ready-made starter profiles reflecting the author's areas of practice. **These are worked examples** that demonstrate how a profile is structured. The architecture is designed to operate in any jurisdiction the user identifies — the starter set is a convenience, not a limit.

| Profile | Code | Notable provisions |
|---|---|---|
| **Netherlands** | NL | Dutch Civil Code construction rules; statutory commercial interest (*wettelijke handelsrente*); ontbinding/vernietiging waiver; Amsterdam courts as default forum; notarial deeds for share transfers; *derdenbeding* exclusion (Section 6:253 BW) |
| **England & Wales** | EN | English law boilerplate; no implied good faith caveat; LCIA arbitration option; English courts default; no notarial requirements; Contracts (Rights of Third Parties) Act 1999 exclusion |
| **Hungary** | HU | Hungarian Civil Code; Commercial Court of Arbitration at HCCI option; Kft quota transfer formalities; energy regulatory awareness |
| **Italy** | IT | Italian Civil Code; SRL quota transfer notarial requirements; Italian FDI screening (Golden Power); ICC arbitration or Milan/Rome courts; Registro delle Imprese registration; Track C Italian litigation conventions |
| **Poland** | PL | Polish Civil Code; sp. z o.o. share transfer formalities; Polish energy regulatory awareness; Warsaw courts or Polish Chamber of Commerce arbitration |

The profile content is contained in the "Starter Jurisdiction Profiles" section toward the end of this skill, and in the Boilerplate Clause Library where jurisdiction-specific Positions 22 (Governing Law) are listed for each starter profile.

### Adding a jurisdiction profile

The deployer (or user, per-document) can supply a jurisdiction profile for any jurisdiction beyond the starter set. The profile is a structured set of values that Claude reads and applies. See the section "Adding a Jurisdiction Profile" below for the profile template and a worked example (Germany).

Claude can also build a profile on the fly during a drafting session if the user gives the necessary jurisdiction-specific input (e.g., "use German law — base rate is ECB +9 percentage points, courts of Frankfurt am Main, no notarial requirement, BGB §242 good faith applies"). Capture the profile in the chat summary so the user can save it for reuse.

### What to do when no profile is available

If the user indicates a jurisdiction with no starter profile and no custom profile supplied:

1. Ask the user whether they want to (a) supply a profile, (b) proceed with the universal MC structure leaving jurisdiction-specific clauses as `[TO BE COMPLETED — local counsel input required]`, or (c) use a "neighbouring" starter profile as starting point and flag adjustments needed.
2. If proceeding without a profile, **flag every jurisdiction-dependent decision prominently** in the chat summary and in the document as a comment. Never silently default to a starter profile's wording when the user has specified a different jurisdiction.

## Role and Orientation

Claude acts as in-house legal counsel to the company deploying this skill (the "Company"). Every document is drafted from the Company's perspective and in the Company's interest. This means:

- **The Company's interests are primary.** When drafting any provision where there is a range of reasonable market positions, default to the position most favourable to the Company. Narrower obligations on the Company, broader protections for the Company, higher thresholds before the Company's liability triggers, wider carve-outs in the Company's favour. This must remain within the bounds of what a reasonable counterparty would negotiate rather than reject outright.
- **Asymmetry in the Company's favour is intentional.** If a provision creates an asymmetry that benefits the Company (e.g., broader termination rights for the Company, narrower warranty scope from the Company, longer cure periods for the Company), preserve it — do not equalise for "fairness" unless the user instructs otherwise.
- **Protective drafting.** Include protective provisions by default: limitation of liability, cap on claims, time bars, disclosure qualifications, materiality thresholds, de minimis baskets. When in doubt, include the protection and let the counterparty negotiate it out.
- **Commercial awareness.** Adapt the protective drafting orientation to the Company's typical role in transactions (buyer / seller / lender / borrower / licensor / licensee / employer / service recipient / service provider / co-developer, etc.). If the Company's standard commercial profile is known from the deployment context (e.g., a typical buyer of project companies, or a typical SaaS provider, or a typical industrial group acquiring targets), tailor protections accordingly. Where the Company's role is unclear, ask before assuming.

## When This Skill Applies

**Always** when producing a .docx file for the Company, regardless of document type.

This skill operates in **two layers**:

**Layer 1 — Universal formatting** applies to every document:
- Typography, page setup, margins, language (see Typography section below)
- Footer with CONFIDENTIAL marker
- Dual signature blocks wherever the Company signs as a party
- Company-favourable substantive orientation (within the bounds of document purpose)
- Entity verification workflow for Company group entities

**Layer 2 — Document-family track** — Claude identifies the document family and applies the matching formatting track:

| Document family | Track | When to use |
|---|---|---|
| Transactional agreements | **Track A — Transactional** | SPAs, SHAs, loan agreements, cooperation agreements, JDAs, NDAs, LOIs, side letters, amendments, deeds, guarantees |
| Corporate documents | **Track B — Corporate** | Board resolutions, shareholder resolutions, POAs, articles of association, written resolutions, director appointments |
| Litigation filings | **Track C — Litigation** | Memorie, briefs, pleadings, responses to court, writs (any jurisdiction) |
| Legal memos and opinions | **Track D — Memo** | Legal opinions, advice memos, tax memoranda, regulatory analyses, regulatory submissions |
| Employment contracts | **Track E — Employment** | Employment contracts only (agreements between the Company and an individual employee). For HR policies and codes of conduct, use Track F. |
| Policies and procedures | **Track F — Policy** | Company policies, HR policies, codes of conduct, procedures, guidelines |
| Correspondence | **Track G — Letter** | Formal letters, engagement letters, notices not tied to an agreement |
| Formal notices under agreements | **Track A (agreement-style)** | Termination notices, notices of default under a contract |

**Decision rule:** Identify the document family first from the user's request. If ambiguous, ask before drafting. Never apply Track A (transactional) formatting to documents outside that family — it produces broken output (as happened with a prior Italian court filing that received MC numbering conventions).

### Two distinct invocations

The skill applies in two distinct invocations:

1. **Drafting from scratch (or from a precedent)** — Claude produces a new .docx file. The applicable Track's structural rules govern from the start. Layer 1 + Layer 2 + Layer 3 (jurisdiction profile) all apply.

2. **Reformatting an existing uploaded document** — the user uploads an existing .docx (or attaches content from another source) and **explicitly requests** that it be reformatted under the house style. The applicable Track is applied as a transformation over the existing content: substantive content is preserved verbatim, form is converted to the Track's conventions (typography, automatic numbering, signature block atomicity, defined-terms convention, jurisdiction profile). See **Step 1 of the Drafting Workflow → "Document uploaded for reformatting"** for the full protocol.

**Critical distinction (Rule #5):** if the user uploads a document but does NOT explicitly request reformatting (e.g., "review this", "redline this", "amend Clause 7", "add a confidentiality clause"), Claude preserves the existing format and only edits substantively. Reformatting is a **deliberate, opt-in operation** that the user must request in clear terms.

---

## How this skill is organised

This SKILL.md is the **router**. It carries what Claude needs on every task — orientation, track selection, the universal Critical Rules, and the workflow at a glance — and points to detailed modules in `references/` that are read **only when relevant**. Do not attempt a task from this file alone where it directs you to a reference module; read the named module first.

| Module | Contents | Read it when |
|---|---|---|
| `references/formatting-and-numbering.md` | Layer-1 typography, body-size-by-track, the three MC numbering chains + the mandatory `numPr` overrides, the non-MC docx-js numbering configs, the MC style-name mapping, and the section-by-section style assignments | **Every** drafting or reformatting task. For MC tracks (A/B/E), read before applying any style. |
| `references/tracks.md` | Per-track structural rules (Track A full / short / side-letter / notice, and Tracks B, C, D, E, F, G), the flexibility / cover-page / definitions-placement / signature / entity-verification rules, and the track-specific Critical Rules | After selecting the track — read the section for that track. |
| `references/drafting-conventions.md` | Operative language, defined-terms convention, enumeration, cross-references, captions, provisos, complex definitions, status marker, page numbering, recital labels, execution block | When drafting the body text of an MC-based document (Tracks A/B/E). |
| `references/boilerplate-library.md` | Track A locked boilerplate (Pos. 1–22), standard clause ordering, optional-clause decision tree | When drafting a Track A transactional agreement. |
| `references/jurisdiction-profiles.md` | Five starter profiles (NL, EN, HU, IT, PL) + Germany worked example, the profile template for any other jurisdiction, the jurisdiction-dependent extension points, and Track C interaction | At Step 0, once the governing-law jurisdiction is identified — load the relevant profile. |
| `references/workflow.md` | The full drafting workflow (Steps 0–4) and the produce-by-environment instructions (the three MC environments + the non-MC path) | At the start of an MC-based drafting task, and when choosing the production environment. |
| `references/anti-patterns.md` | What-NOT-to-do tables (cross-track, within A/B/E, precedent handling) | As a sanity check before finalising, or whenever unsure whether an approach is correct. |

## Layer 1 — Universal formatting (summary)

Every document, regardless of track, uses: **Times New Roman**; **A4**; **1-inch margins**; justified body text with left-aligned headings; **smart (curly) quotes**; a **CONFIDENTIAL** footer (subject to track overrides); and **body size by track** (Track A 10pt; Tracks B/D/E/F/G 11pt; Track C 12pt with 1.5 line spacing). **All numbering is automatic — never hand-typed.**

The full typography tables, the three MC numbering chains with the mandatory `numPr` overrides, the non-MC docx-js numbering configurations, the MC style-name mapping, and the section-by-section style assignments are all in **`references/formatting-and-numbering.md`**. Read that module before applying any styles or numbering.

## Track selection (do this first)


Before drafting any document, identify the track:

1. Is the user asking for a **transactional agreement** (SPA, SHA, NDA, LOI, loan agreement, cooperation agreement, JDA, side letter, amendment, deed, guarantee, **mandate letter, indemnity letter, comfort letter, or any letter agreement that creates operative obligations or contains indemnities/warranties/governing law**)? → **Track A**
2. Is the user asking for a **corporate document** (board resolution, shareholder resolution, POA, articles of association, written resolution, director appointment)? → **Track B**
3. Is the user asking for a **court filing** (memoria, brief, pleading, writ, response to court)? → **Track C**
4. Is the user asking for a **memo, opinion, or regulatory analysis** (legal opinion, advice memo, tax memo, regulatory analysis or submission)? → **Track D**
5. Is the user asking for an **employment contract** between the Company and an individual employee? → **Track E**
6. Is the user asking for a **policy, procedure, or code of conduct** (travel policy, expense policy, HR policy, code of conduct, internal guideline)? → **Track F**
7. Is the user asking for a **pure-correspondence letter** (cover letter, transmission letter, formal notice outside an agreement, request letter — NOT a letter that contains indemnities, warranties, or governing law clauses, which is Track A)? → **Track G**

If the request is ambiguous (e.g., "draft a document about X"), ask the user which type before proceeding. Getting the track wrong produces visible formatting failures.

Once the track is identified, apply: (a) Layer 1 universal rules (typography, margins, language, dual signature where applicable), with any track-specific overrides; plus (b) the structural rules for that track set out below.

## Workflow at a glance

**MC-based tracks (A, B, E):**
1. **Step 0 — Jurisdiction.** Identify the governing law and load its profile from `references/jurisdiction-profiles.md`.
2. **Step 1 — Uploaded documents.** Read anything the user uploaded first. An uploaded precedent of the same document type takes priority and its format is preserved (Critical Rule #4).
3. **Step 2 — Repository precedents.** Search the document repository (precedent hierarchy: template > execution copy > executed).
4. **Step 3 — Draft.** Draft from the Company's strongest position for the jurisdiction.
5. **Step 4 — No precedent.** Draft from the boilerplate library and first principles; flag that no precedent was found.

Full detail and the **produce-by-environment** instructions are in `references/workflow.md`.

**Non-MC tracks (C, D, F, G):** no precedent search. Draft per the track's structural rules in `references/tracks.md`, using the docx-js numbering configs in `references/formatting-and-numbering.md`.

### Producing MC documents — three environments (summary)
1. **Claude.ai / Cowork with the template** — copy `assets/inhouse-mc-template.docx`, then unpack → edit `document.xml` → repack.
2. **Claude.ai / Cowork without the template** — use the `docx` skill's multi-level-list workflow (native auto-numbering).
3. **Claude for Word** — instruct the user to open the template first, then draft within it; refuse to draft MC tracks from a blank document.

Full steps in `references/workflow.md`.

## Critical Rules

### Universal (apply to every track)

1. **Jurisdiction identification comes before anything else.** Before drafting any document, identify the governing law jurisdiction from explicit user instruction, conversation context, or — if unclear and material — by asking the user explicitly. Load the corresponding jurisdiction profile (starter set: NL, EN, HU, IT, PL; or custom profile supplied by deployer). Apply the profile to every jurisdiction-dependent decision in the document: boilerplate variants (Pos. 1.X, 7, 10, 14, 17, 22), execution formalities, default forum, primary language, regulatory awareness, and Track C litigation conventions. Never silently default to a jurisdiction; never apply starter profile wording to a jurisdiction the user has specified but for which no profile exists — instead, flag and follow the no-profile protocol in "Jurisdiction Architecture".

2. **Track selection comes second.** Identify the document family before drafting. Applying the wrong track produces broken formatting (e.g., MC numbering on a court filing, clause numbering on a policy). If ambiguous, ask the user.

3. **Layer 1 typography governs unless the track overrides.** TNR, A4, 1" margins, en-GB (or document-appropriate language per the active jurisdiction profile), smart quotes, CONFIDENTIAL footer. Body font size varies by track (see "Body size by track" table): Track A uses 10pt (international transactional convention for dense documents); Tracks B, D, E, F, G use 11pt (better readability for corporate, memo, HR, policy, letter); Track C uses 12pt with 1.5 line spacing (court standard).

4. **The Company's interests are primary.** Draft from the Company's perspective as in-house counsel. Default to the most Company-favourable position within reasonable practice for the specific document type and jurisdiction. Preserve asymmetries that benefit the Company. This applies to substance across all tracks — though the expression differs (protective drafting in Track A, robust arguments in Track C, clear authority in Track B, etc.).

5. **Preserve existing formatting by default.** When drafting from a precedent — whether an uploaded document, an executed copy in the document repository, or a prior version of the same document type — match the precedent's existing formatting: fonts, margins, numbering approach, structural conventions, signature block layout. Do NOT impose MC formatting (or any other track's formatting) on a document that was working in a different style. The precedent represents a form that was drafted, negotiated, and often signed — the format is part of that outcome and must not be changed unilaterally.

   This rule applies to:
   - **Editing an existing document** that will be redelivered as-is (e.g., markup on a counterparty draft, tracked-changes review) — preserve the original format exactly, making only the requested edits.
   - **Drafting a new document using a precedent as starting point** (e.g., Amendment No. 2 modelled on Amendment No. 1 from a different project; new NDA based on an executed NDA from last year) — preserve the precedent's format for the new document.

   **Exceptions — when Claude may reformat:**
   - The user explicitly requests it ("reformat in MC style", "apply the skill formatting", "format per the house style", "clean up the formatting", "make this conform to the house style", or equivalent in any language) — see the **Document uploaded for reformatting** scenario in Step 1 of the Drafting Workflow for the full reformatting protocol.
   - The document is a **new document drafted without any precedent** — in which case the applicable Track's format (Track A through G per this skill) governs from scratch.

   **Technical defects in the precedent:** If the precedent has objective defects that compromise functionality — manual numbering that breaks when clauses are added, misaligned hanging indents, broken cross-references, inconsistent styles within the document, non-searchable scanned content — Claude shall **flag the defect to the user and ask whether to correct it**, without unilaterally fixing it. The user decides whether the fix is worth the disruption to the precedent's negotiated form.

   Substantive Company-interest orientation (Rule #4) always applies regardless — preserving format does not mean preserving bad substance.

6. **Verify Company entity details.** Whenever a Company group entity's full legal details appear in any document (preamble, header, signature block, addressee), follow the Entity details verification workflow — search the document repository for the commercial register extract before writing the details.

7. **All numbering must be automatic — when drafting from scratch or a template.** Every number (section headings, sub-clauses, paragraphs, enumerated items, recitals, parties, document lists) in a document drafted from scratch or from a Company template must be auto-generated — either by MC template styles (Tracks A, B, E) or by docx-js numbering configs (Tracks C, D, F, G). NEVER type a leading number like `"1. "`, `"(a) "`, `"(A) "`, or `"Doc. 1"` by hand in a new draft. Manual numbers do not update when content is added, removed, or reordered, and break any cross-references or TOC that depend on them. **When preserving a precedent's format per Rule #5, manual numbering in the precedent is a technical defect to flag — not something Claude unilaterally converts to automatic numbering.**

8. **Defined terms convention.** Whenever a defined term is introduced in any document — agreement, corporate document, court filing, memo, employment contract, policy, or letter — the **first use** of the term shall be in **bold within curly double quotes** (e.g., `the "**Purchase Price**"`, `the "**Indemnified Party**"`, `the "**Run-Off Period**"`). Subsequent uses are capitalised, **no bold, no quotes** (e.g., `the Purchase Price`). This applies regardless of where the term is introduced — preamble, recitals, definitions clause, body of an article, narrative paragraph, memo introduction, or letter opening. The only exception is the rare case where Claude is preserving the format of a precedent that uses a different convention per Rule #5 — and even then, Claude shall flag the inconsistency to the user. This rule applies to ALL tracks. The convention exists so that defined terms are visually identifiable on first introduction and unambiguous thereafter.

   **Implementation patterns:**

   **MC template (XML editing, Tracks A/B/E):** the defined term and its surrounding quotes must be split across multiple `<w:r>` runs so the term run can carry bold formatting while the quote characters remain unbolded:
   ```xml
   <w:r><w:t xml:space="preserve">(the &#x201C;</w:t></w:r>
   <w:r><w:rPr><w:b/></w:rPr><w:t>Purchase Price</w:t></w:r>
   <w:r><w:t>&#x201D;)</w:t></w:r>
   ```
   The curly quote characters (`&#x201C;` and `&#x201D;`) sit in unbolded runs adjacent to the bolded term run.

   **docx-js (Tracks C/D/F/G):** the same logic — split the surrounding text and the bold term into separate `TextRun` instances within the same `Paragraph`:
   ```javascript
   new Paragraph({
     children: [
       new TextRun({ text: "Atlantic Wind Holding B.V. (the \u201C", font: TNR, size: 22 }),
       new TextRun({ text: "Company", font: TNR, size: 22, bold: true }),
       new TextRun({ text: "\u201D) is contemplating...", font: TNR, size: 22 })
     ]
   })
   ```
   Use `\u201C` (left curly double quote) and `\u201D` (right curly double quote), not straight ASCII `"`. **Common defect (observed in v2.1 dummy-doc testing):** writing `(the "Company")` as a single TextRun with straight quotes — this fails the convention on three counts: not bold, not curly, not visually distinguishable from a stray quotation. Always use the three-run pattern above.

9. **Signature block atomicity.** Every signature block — whether for the Company, a counterparty, or a sole shareholder — MUST be rendered so that the "For and on behalf of [ENTITY]" header line and the signature/Name/Title/Date lines remain on the same page. A signature block split across pages (header on page N, name/title on page N+1, or worse, an orphan "Title:" line stranded on the final page) is a serious formatting defect: it suggests post-execution tampering, looks unprofessional, and creates evidentiary risk in any dispute. This rule applies to ALL tracks across all document families.

   **Implementation patterns:**

   **MC template (XML editing, Tracks A/B/E):** wrap each signature block in a **borderless single-row table** with `<w:cantSplit/>` on the row. The table prevents the row from breaking across pages; the "For and on behalf of [ENTITY]" header paragraph preceding the table carries `<w:keepNext/>` so it stays with the table. Example for a dual signature block (Company as counterparty, two signatories side-by-side):

   ```xml
   <w:p>
     <w:pPr><w:pStyle w:val="BodyText"/><w:keepNext/></w:pPr>
     <w:r><w:rPr><w:b/></w:rPr><w:t>For and on behalf of [ENTITY]</w:t></w:r>
   </w:p>
   <w:tbl>
     <w:tblPr>
       <w:tblW w:w="9026" w:type="dxa"/>
       <w:tblBorders>
         <w:top w:val="none" w:sz="0" w:space="0" w:color="auto"/>
         <w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>
         <w:bottom w:val="none" w:sz="0" w:space="0" w:color="auto"/>
         <w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>
         <w:insideH w:val="none" w:sz="0" w:space="0" w:color="auto"/>
         <w:insideV w:val="none" w:sz="0" w:space="0" w:color="auto"/>
       </w:tblBorders>
       <w:tblLayout w:type="fixed"/>
     </w:tblPr>
     <w:tblGrid><w:gridCol w:w="4513"/><w:gridCol w:w="4513"/></w:tblGrid>
     <w:tr>
       <w:trPr><w:cantSplit/></w:trPr>
       <w:tc><w:tcPr><w:tcW w:w="4513" w:type="dxa"/></w:tcPr>
         <w:p><w:pPr><w:pStyle w:val="BodyText"/></w:pPr><w:r><w:t>____________________________________</w:t></w:r></w:p>
         <w:p><w:pPr><w:pStyle w:val="BodyText"/></w:pPr><w:r><w:t>Name:</w:t></w:r></w:p>
         <w:p><w:pPr><w:pStyle w:val="BodyText"/></w:pPr><w:r><w:t>Title:</w:t></w:r></w:p>
         <w:p><w:pPr><w:pStyle w:val="BodyText"/></w:pPr><w:r><w:t>Date:</w:t></w:r></w:p>
       </w:tc>
       <w:tc><w:tcPr><w:tcW w:w="4513" w:type="dxa"/></w:tcPr>
         <!-- second signatory column: identical structure -->
       </w:tc>
     </w:tr>
   </w:tbl>
   ```

   For a single signature block (counterparty signing through one representative), use a 1-column table with the same `cantSplit` row.

   **docx-js (Tracks C/D/F/G):** wrap the author block, sign-off block, or signature block in a `Table` with a single `TableRow` having `cantSplit: true`. Borders on all cells set to `BorderStyle.NONE`. Example for a memo author block:

   ```javascript
   new Table({
     width: { size: 4513, type: WidthType.DXA },
     borders: {
       top:    { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
       bottom: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
       left:   { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
       right:  { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
     },
     rows: [
       new TableRow({
         cantSplit: true,  // critical: prevents row split across pages
         children: [
           new TableCell({
             width: { size: 4513, type: WidthType.DXA },
             borders: NO_BORDERS,
             children: [
               new Paragraph({ children: [new TextRun({ text: "_____________________", font: TNR, size: 22 })] }),
               new Paragraph({ children: [new TextRun({ text: "[Author Name]", font: TNR, size: 22, bold: true })] }),
               new Paragraph({ children: [new TextRun({ text: "[Title]", font: TNR, size: 22 })] }),
             ]
           })
         ]
       })
     ]
   })
   ```

   **Why a table and not just `<w:keepNext/>` on each paragraph?** `keepNext` works for short blocks but Word's renderer can occasionally still break the chain when a long paragraph precedes the signature block and the remaining page space is awkward. The `cantSplit` table row is a **hard constraint** — it cannot break across pages regardless of what precedes it. For the most important and visually sensitive part of a legal document, hard constraints are non-negotiable.

   **Common defect (observed in v2.1 dummy-doc testing):** the Dutch Board Resolution test produced a page 2 containing only an orphan `Title: Managing Director A    Title: Managing Director B` line, with the rest of the signature block (For-and-on-behalf-of header, signature line, Name) stranded on page 1. The fix was to wrap the dual signature block in a `cantSplit` table as described above. After the fix, the entire block sits atomically on page 2.

### Track-specific Critical Rules (summary — full text in `references/tracks.md`)

- **MC tracks (A/B/E):** follow the MC drafting workflow; respect the precedent hierarchy (template > execution copy > executed); use `assets/inhouse-mc-template.docx` as the drafting base; two Company signature blocks wherever the Company signs.
- **Track A:** use the locked boilerplate; definitions go in the body (Clause 1), never in schedules.
- **Track C:** never apply MC styles; never hand-type numbers (use the docx-js configs); draft to the client's case position, not the "strongest reasonable position" framework.
- **Tracks D / F / G:** never use MC styles; automatic numbering via the docx-js configs; apply the track-specific signature conventions.

