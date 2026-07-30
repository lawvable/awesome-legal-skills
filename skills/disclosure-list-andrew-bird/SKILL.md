---
name: "disclosure-list-andrew-bird"
description: "Works out which documents you have to hand over to the other side in a civil case in England & Wales, and builds the formal list. The part it gets right that trips people up is which disclosure regime applies — Practice Direction 57AD (the Disclosure Pilot, now permanent in the Business and Property Courts, with its Models A–E) or standard disclosure under CPR Part 31 everywhere else. It picks the regime, chooses a Model per issue, structures the Disclosure Review Document, and drafts the disclosure certificate for the party to sign personally. Built for litigation juniors, in-house counsel, and small teams without a precedent bank. Use when the user says 'disclosure list', 'PD 57AD', 'Model C', 'extended disclosure', 'List of Documents', 'N265', or needs to work out what must be disclosed."
argument-hint: "[--regime=pd57ad|cpr31] [--model=A|B|C|D|E]"
metadata:
  author: "Andrew Bird"
  license: "mit"
  version: "2026-06-09"
---

# /disclosure-list

1. Identify the regime — PD 57AD (Business and Property Courts: Commercial Court, Chancery Division, TCC, Circuit Commercial, IP, Financial List) or CPR Part 31 (everywhere else, including most county court multi-track cases).
2. Under PD 57AD: select the appropriate Extended Disclosure Model(s) (A–E) per issue. Initial Disclosure is also required.
3. Under CPR 31: apply "standard disclosure" (CPR 31.6) — documents on which a party relies, plus documents that adversely affect own case / support another party's case / are required by a relevant practice direction.
4. Build the List of Documents (N265 form under CPR; Disclosure Review Document under PD 57AD).
5. Apply privilege screening before disclosure.

---

# Disclosure list

## Which regime?

| Court / Division | Regime |
|---|---|
| Business and Property Courts (Commercial, Chancery, TCC, Circuit Commercial, IP, Financial List) | PD 57AD (Disclosure Pilot — now permanent) |
| Other High Court divisions, County Court, fast track and multi-track | CPR Part 31 |
| Small claims track | CPR 27.4 (limited disclosure on directions) |
| Family proceedings | FPR — separate regime not covered here |

## PD 57AD — Extended Disclosure Models

After Initial Disclosure (limited — documents relied on plus those required for the other party to understand the case), the parties agree or the court orders **Extended Disclosure** by issue, using one or more of:

| Model | What it requires |
|---|---|
| **A** | Disclosure confined to known adverse documents (no further search). |
| **B** | Limited disclosure — documents necessary to enable other parties to understand the case being advanced. No proactive search beyond what was done for Initial Disclosure. |
| **C** | Request-based search — disclosure of specific documents or narrow classes specified by request. The narrowest "real search" model. |
| **D** | Narrow search-based disclosure — search for documents likely to be relevant + adverse documents found. The PD 57AD equivalent of standard disclosure. |
| **E** | Wide search — like Model D but including the train-of-enquiry approach (Peruvian Guano style). Available only where necessary to fairly resolve issues, generally where strong reasons. |

Selection happens via the **Disclosure Review Document (DRD)** — a structured negotiation document parties complete and exchange.

## CPR Part 31 — standard disclosure

Disclose:
- Documents on which the party relies (CPR 31.6(a)).
- Documents which adversely affect own case, adversely affect another party's case, or support another party's case (CPR 31.6(b)).
- Documents the party is required to disclose by a relevant practice direction (CPR 31.6(c)).

The duty extends to documents in the party's control (in physical possession, with right to possession, or right to inspect: CPR 31.8).

## Inputs

- Court / division (drives regime).
- Issues for disclosure (PD 57AD) or pleaded issues (CPR 31).
- Custodians (employees, agents, advisers).
- Data sources (email, file shares, document management, messaging apps — including WhatsApp / Signal, dataroom platforms).
- Date range.
- Privilege scope (advice privilege, litigation privilege, WP, common-interest).
- Confidentiality (commercially sensitive, regulatory, third-party).
- Foreign data protection (GDPR — Article 6/49 lawful basis for transfer).

## Workflow

### Step 1 — Regime check
B&P Courts → PD 57AD. Otherwise CPR 31.

### Step 2 — Initial Disclosure (PD 57AD)
Each party serves with Statements of Case: documents relied on + those required for other parties to understand. List of Issues for Disclosure follows in the DRD.

### Step 3 — Issues for disclosure (PD 57AD only)
A focused list — not the same as pleaded issues. Should be issues that disclosure will actually inform.

### Step 4 — Model selection per issue (PD 57AD)
Each issue gets a model. Default to Model C (request-based) where possible; Model D for broader issues; Model E only in exceptional cases.

### Step 5 — Custodian / data-source mapping
Who held the relevant documents; where the data lives; what platforms (Outlook / Gmail / Teams / Slack / WhatsApp / dataroom / paper).

### Step 6 — Search methodology
- Date ranges.
- Custodians.
- Data sources.
- Keywords (PD 57AD requires keyword lists and dedupe approach to be agreed).
- Use of technology-assisted review (TAR / predictive coding) — disclose use in the DRD.

### Step 7 — Privilege review
- Advice privilege: communications between solicitor and client for the purpose of legal advice.
- Litigation privilege: communications with third parties (witnesses, experts) where the dominant purpose is for litigation reasonably contemplated.
- WP: settlement correspondence.
- Common interest: shared legal interest with a third party (insurer, co-defendant).

Privileged documents are listed by description, not produced. Redaction of privileged parts is permissible.

### Step 8 — List of Documents

**CPR 31 — N265 List of Documents (or equivalent):**

Three parts:
- Part 1: documents in control, available for inspection.
- Part 2: documents in control, but right or duty to withhold from inspection (privilege).
- Part 3: documents that have been but are no longer in control (when and how parted with).

Plus the **Disclosure Statement** (signed personally — CPR 31.10) certifying the search and the duty.

**PD 57AD — Disclosure Certificate**

Signed by the party (not the solicitor) certifying the search complied with the order and disclosure obligations under the PD. Like the CPR 31.10 statement, any draft Disclosure Certificate the skill produces is **scaffolding, not an executed certificate** — carry the same DRAFT banner across, do not present the certification as made, and the party must sign it personally only once the search has actually been performed.

## Output

Produce the list using the sections below. Render it as the finished List of Documents — do not echo this template back, and do not invent documents, custodians, or sources to fill a section. If a part has nothing in it, say so. Every document listed must trace to a real input the user supplied; the skill scopes and drafts the list, it does not generate the documents that go in it.

### Output template (CPR 31)

# List of Documents — [Case name and claim number]

## Part 1: Documents in our client's control which we do not object to producing for inspection

| ID | Date | Description | Custodian / source |
|---|---|---|---|
| C/1 | [date] | [description] | [custodian] |

## Part 2: Documents in our client's control which we object to producing for inspection

| ID | Date | Description | Ground |
|---|---|---|---|
| C/P/1 | [date] | [generic description] | Legal advice privilege |
| C/P/2 | [date] | [description] | Litigation privilege |
| C/P/3 | [date] | [description] | Without prejudice |

## Part 3: Documents which were but are no longer in our client's control

| Date | Description | When and how parted with | Whereabouts believed |
|---|---|---|---|

## Disclosure Statement (CPR 31.10)

> **DRAFT — NOT AN EXECUTED STATEMENT.** This is scaffolding for a Disclosure Statement, not a completed one. Before it can be filed: the statement must be reviewed; the search it describes must actually have been performed; and it must be signed **personally by the party** under CPR 31.10. Do not file as generated. Do not present the blanks as filled, and do not assert the search was carried out — only the signing party can certify that. Render this with the banner attached and the certification text shown as wording the party must adopt for themselves, not as a statement the model is making.

I, [name], state:
1. My address is [...]. I am [position].
2. I have been authorised to make this disclosure statement on behalf of [party].
3. I am familiar with the issues in this case as set out in [pleadings].
4. I conducted a search for documents that I am required to disclose in accordance with [order / standard disclosure / agreed scope].
5. The search covered [custodians, data sources, date range, keywords].
6. I did not search for [excluded sources — eg paper archives older than 7 years, dormant servers] — give reasons.
7. I certify I understand the duty to disclose and to the best of my knowledge I have carried it out.

Signed: [party — sign personally, CPR 31.10]
Date: [date]

### Output template (PD 57AD Disclosure Review Document, simplified)

# Disclosure Review Document — [Case]

## Section 1A: Initial Disclosure
[Complete — list of documents already provided.]

## Section 1B: Issues for Disclosure
| No. | Issue | Proposed Model | Reasons |
|---|---|---|---|
| 1 | [issue 1] | C | [...] |
| 2 | [issue 2] | D | [...] |

## Section 2: Custodians, sources, date range, keywords
[Table — agreed or proposed per issue.]

## Section 3: Technology
- Use of TAR / predictive coding: [yes/no, model]
- De-duplication, near-duplication, threading: [methodology]

## Section 4: Cost estimate
[Per CPR Part 47 / PD 57AD requirement.]

## Markers

- `[REGIME — confirm court division]`
- `[PRIVILEGE — flagged but not yet reviewed]`
- `[GDPR — cross-border transfer requires Art 6/49 basis]`
- `[SME VERIFY — Model selection per issue]`

## What this skill does not do

- Run the search. It scopes and lists; the search itself happens outside the model and must actually be performed before any list or statement is certified.
- Decide privilege. It flags candidates by description; counsel reviews every flagged document and makes the privilege call.
- Certify anything. The Disclosure Statement (CPR 31.10) and Disclosure Certificate (PD 57AD) are signed personally by the party — the model drafts scaffolding, it does not make the certification.
- Cover Scottish / NI procedure (Commission and Diligence; Schedule 1 RCS).
- Give legal advice. This is a drafting aid that produces a draft for solicitor review. Nothing it generates should be filed as generated — verify the scope, the search, and the privilege calls with counsel before relying on or serving any output.
