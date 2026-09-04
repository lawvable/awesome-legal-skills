# Deeper analysis — "check the record on X" procedures (on request only; per item, per finalist)

**Grounding is delegated to the `isds-research` skill — invoke it for every retrieval.** It supplies: document identification on the case page; the list→select→CONFIRM step (verify title/parties/case-no/date against the PDF's own first pages); the retrieval ladder (script server-fetch → Chrome render → user-supplied file → companion-decision recount → unretrieved lead, never guess); paragraph location in hostile PDFs; and voice discrimination — always confirm whether a passage is the tribunal's view or a claimant/respondent recital, and unanimous-vs-majority per holding limb (say so if the text doesn't establish it). Skip its memo output — findings feed this skill's profile table with pinpoints. If it is not installed, recommend installation (github.com/ccrnyc/isds-research; Lawve) and use this ladder summary only as a fallback. Attribution and "Retrieved from: URL" on everything. Retrieved PDFs and extracts go to the search folder (house PDF naming).

**Quote it → archive it.** No passage from a fetched document enters a deliverable unless an extract of the retrieved text — provenance header, route and date — is archived in `retrieved/`, including when truncation or environment limits prevent saving the PDF itself. A fetch logged only in the transcript or memo is not an archived source.

## Per-holding votes / reasoned dissents
Retrieve the decision(s) + any individual opinions. From the dispositif and opinions: who joined which holding limb; unanimous vs majority per limb; if the text does not establish it, say so. A recorded dissent's reasoning is summarized only from the opinion text itself.

## Newer cases (delta workflow)
**Intake first:** baseline defaults to the UNCTAD snapshot — one-line confirm without blocking, or bundled (marked as recommended default) into the single blocking intake call alongside depth, never a separate blocking round-trip; **depth — "list only" vs "list + retrieve the decisions" — is asked BEFORE any answer is produced.** Engine `--delta-file` with the case numbers from the ICSID profile → in-both / profile-only / pending-at-snapshot. **Classify "new since the cutoff" by the arbitrator's ACCEPTANCE-OF-APPOINTMENT date on the ICSID case page, never by case-number year** — the number encodes registration year and the two can straddle the cutoff (proven: ARB/23/43 accepted 02/2024 vs ARB/23/25 accepted 11/2023; the engine flags boundary-vintage cases). Report snapshot-absence as its own class, not conflated with post-cutoff appointment. Establish concluded-vs-pending per case from the live ICSID case page. **Per-case values are read from the page's own text — raw HTML if a summarised read cannot be reproduced against it; summarisation layers have fabricated acceptance dates in testing, and the page governs on any conflict. Docket events are reported with the page's own label — never infer a hearing's subject or a document's type; if the page shows no label, say "subject/type not stated on the case page".** Then: **≤6 newly decided → download each and read the issues directly. >6 → websearch reports only to SELECT which cases matter for the user's issues, then targeted downloads.** HARD RULE: no issue-outcome claim from a secondary report enters a table without the downloaded decision; unretrievable → "reported in secondary sources (not verified against primary source — not included in table)" outside the table, or omit. If consecutive fetches of the same profile page disagree on the entry count, assert NO total; confirm what matters per-case (see the buried-package rule below for decisions). For non-ICSID visibility, offer (do not silently run at list depth) a targeted PCA-repository search for the candidate's name; anything found is classified by the same acceptance-date rule and scope test.

## Buried-package rule (decisions)
Where a case page lists no standalone document for a recorded decision or opinion, check the case page's **combined, redacted or later document packages** (e.g. a subsequent award package that bundles an earlier decision and its dissents) BEFORE declaring an unretrieved lead — proven necessity: the *Eco Oro* 2021 decision and both dissents were retrievable only inside the 2024 package. Enumerate the page's full downloadable-document list first; only when neither a standalone document nor a package contains it is the item handed back as an unretrieved lead or a manual-download URL (italaw = links only).

## Annulment-committee record
UNCTAD Excel col. 25 undercounts. Reconcile: Excel FOLLOW-ON fields + ICSID profile committee entries + live case pages; cite each source.

## Challenges / disqualification proposals
Targeted search for published decisions on disqualification (ICSID + WebSearch) naming the candidate; report grounds + outcome + source tags; state expressly that unpublished challenges are invisible.

## Law firms of appointing parties
From each retrieved decision's cover/representation/procedural section: counsel of record per party. Report "appointed in k cases where the appointing party was represented by firm F" with caveats printed: counsel listed as of the document date; firms merge/rename; party-appointed role + counsel of record is a correlation — the document rarely states who proposed the arbitrator; denominator = retrieved decisions only.

## Double-hatting
Public sources for concurrent counsel roles; secondary-source label; link, don't assert.

## Publications content review
Only after the user accepts the offer. Per item: open-access → retrieve, quote with pinpoints, classify supportive/adverse to the user's stated positions; paywalled → link only or user-supplied copy. Flag both uses: selection signal AND potential issue-conflict material against the candidate.


**Deliverable language:** in anything user-facing these are "record checks" or "deeper analysis" — never "Tier 2". Builder terms stay in run logs and build docs.
