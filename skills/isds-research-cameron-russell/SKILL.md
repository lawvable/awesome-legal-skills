---
name: isds-research
version: 1.1.0
maintainer: ccrnyc
license: AGPL-3.0-only
description: Compliant, retrieval-grounded research over investor-State dispute settlement (ISDS) awards and decisions. Use when the user asks about ICSID / investment-treaty arbitration cases, awards, or doctrines (fair and equitable treatment, expropriation, jurisdiction, costs, annulment, etc.) and wants answers grounded in the actual document text with pinpoint citations. Identifies the correct document on the case page, confirms it against the PDF's own first pages, retrieves primary documents on demand from ICSID, PCA, etc., never scrapes or hosts a corpus in violation of applicable terms, and cites only retrieved text.
---

# ISDS Research

Answer questions about ISDS cases by retrieving the **primary documents on demand** and grounding every legal statement in the retrieved text, with pinpoint (paragraph / page) citations. This is a research aid, **not legal advice**.

**Intended users:** lawyers, arbitration practitioners, academics, and students who need *verifiable* ISDS research — every output is research support for the user's own professional judgment: the tool retrieves, cites, and discloses; the user analyzes and concludes.

## Golden rules (read first)

1. **Ground, don't recall.** Every holding, quote, or pinpoint cite MUST come from text you retrieved *this session*. If it isn't in the retrieved text, say "not found in the retrieved document" — never fill the gap from memory. This is the anti-hallucination guarantee. **Framework law too:** a statement of treaty, Convention, or arbitration-rules law (e.g. "Art. 52(6) resubmission presupposes annulment", "improper constitution is the Art. 52(1)(a) ground") made without retrieving the provision's text must carry a basis label ("per general knowledge based on training data and/or websearch — provision text not retrieved this session"); where such a premise is load-bearing for the answer, prefer retrieving the provision (ICSID hosts the Convention and Rules on its own site) — article-number and ground mislabels are a known secondary-reporting failure.
2. **Confirm whether a decision is reciting a party's argument or the tribunal's view.** Decisions often spend significant space reciting the parties' positions before providing the tribunal's analysis. Before quoting or characterizing any passage: (a) **Voice** — verify whether it is the tribunal/committee's own finding or its recital of a party's argument, and attribute quotes, positions, and holdings accordingly (headings can help to identify whether a passage is attributable to a party or the tribunal, but are not definitive). (b) **How held** — when describing a holding, check whether it was unanimous or by majority: read the dispositif, check the case page for dissenting/separate opinions, and state which limbs were unanimous vs. by majority. If the retrieved text doesn't establish it, say so rather than assuming. Note: some user questions will require providing the parties' arguments, not just the tribunal's holdings.
3. **Identify before you download.** A case page can list dozens of documents (award, decisions on jurisdiction, rectification, annulment, dissents, procedural orders). Never assume "the first PDF" is the one you want. List the documents, choose by title + date + proceeding, then **confirm from the document's own first page(s)** before relying on it.
4. **Language is an attribute, not a filter.** Awards are frequently available only in Spanish/French/etc. A non-English award is a valid, relevant result — do not skip it because it isn't in English.
5. **On demand, single documents.** Fetch the specific document the user needs. Never bulk-download or mirror.
6. **Sources and their rules:**
   - **ICSID** (`icsid.worldbank.org` / `icsidfiles.worldbank.org`) — primary text. Permissive robots; Terms allow viewing/downloading for personal, non-commercial use. Do not redistribute; attribute (below).
   - **PCA** (`pca-cpa.org`; documents on `docs.pca-cpa.org`) — primary text for PCA-administered cases (many UNCITRAL investor-State arbitrations). Robots + Terms verified 2026-07-02: the main site's robots is default-only — no bot-specific groups, disallowing only `/wp-admin/` (verified 2026-07-02 for `Claude-User`; re-verified 2026-07-18, incl. `ChatGPT-User`); the document host returns S3 `AccessDenied` for robots.txt (no robots file → no crawl restriction; a 4xx robots response is treated as "allow"); PCA's Terms of Use bar only *commercial* use without permission and impose **no** automated-access restriction. Fetch specific documents on demand for non-commercial research; attribute; do not republish; honor any case-specific restriction (Terms cl.1 — many PCA/UNCITRAL matters are confidential or only partially published). No PCA helper script yet: locate the document on the PCA case page and fetch that URL, then extract as for ICSID.
   - **UNCTAD ISDS Navigator** — discovery / metadata only. You may run these searches yourself via targeted, user-initiated fetches under the platform's own agent token (e.g. `Claude-User`, `ChatGPT-User`). Robots re-verified 2026-07-18: `investmentpolicy.unctad.org` currently publishes no robots.txt and `unctad.org`'s is default-only with no bot-specific rules (an earlier verification, c. 2026-07-01, recorded an explicit ClaudeBot disallow — robots files change; re-verify periodically). Permission therefore rests on UNCTAD's Terms, which permit personal, non-commercial use — the absence of robots restrictions is NOT a licence for bulk collection. Do **not** scrape or paginate the UI; link and attribute, never republish it. **Reliable path for complete category-filtering:** use UNCTAD's official *full-data Excel export* (structured; all filter fields) — that's the intended public data product, not scraping (local non-commercial filtering only; don't republish or build a public derivative DB). Individual Navigator *case pages* are server-rendered and load fine via `web_fetch` (good for targeted single-case metadata — which also carries the ICSID case number for grounding); it's the *filtered search/list* views that are JS-rendered and time out, so enumerate via the Excel export (or a browser render), not by scraping search pages. **Freshness:** the data is dated snapshots refreshed ~1–2×/year and, per UNCTAD, "cannot be deemed exhaustive" (publicly-known cases only; confidential ones excluded) — state the snapshot date and this caveat.
   - **italaw** (`italaw.com`) — **last-resort, per-case-confirmed primary-text fallback**. Reach italaw only after ICSID / PCA / other official sources are exhausted for the specific document. **Default route: the user obtains the document manually and supplies the file** (`--pdf-file`) — italaw's Terms §4.2 expressly permit manual human browsing. An automated fetch is the fallback only, and only under **all** of these conditions: (i) **per-document human confirmation** — show the case + exact italaw URL and obtain an affirmative approval each time; no "approve all", no persistent auto-yes; (ii) **the platform's own user-initiated agent token only** (e.g. `Claude-User` on Claude, `ChatGPT-User` on ChatGPT) — never spoof a human-browser user-agent; (iii) **one document per approval** — never bulk, batch, loop, or deep-link lists; (iv) **reference, don't reproduce** — short pinpoint quotes + cite/link back to the italaw case page; no wholesale reproduction or AI summary substituting for the source; (v) **log each approval** (document, URL, timestamp) in the run log. Keep italaw content out of any build/test corpus (Terms §4.1); non-commercial use only (§§4.3/5.1); re-check robots.txt + Terms periodically (§8.1 lets italaw change them without notice). A single, per-document, human-confirmed fetch is not prohibited under §4.2 of italaw's terms as it does not constitute bulk access or circumvent any italaw access controls. Robots re-verified 2026-07-18: italaw's robots.txt operatively disallows bulk crawlers (`ClaudeBot`, `GPTBot`) but names no user-initiated agent — `Claude-User` and `ChatGPT-User` fall under the permissive `*` rules (crawl-delay 10, trivially satisfied by one-document-per-approval) — and now carries Content-Signals (`search=yes, ai-train=no, use=reference`, framed as an express rights reservation under art. 4 of EU Directive 2019/790): `use=reference` matches condition (iv) exactly, and `ai-train=no` is honored by keeping italaw content out of any build/test corpus. The gate above remains in force unchanged.
7. **UNCTAD is required for "which cases" questions — never fake completeness.** When a question needs a *complete set* of cases filtered by a UNCTAD category (issue/breach, treaty, sector, forum, outcome, amount), build it from UNCTAD's data via the local Excel helper: `python scripts/query_unctad_excel.py` (filters, ICSID-case-number extraction, and the mandatory data-freshness footer). Do **not** substitute ICSID, WebSearch, or memory to enumerate cases — ICSID doesn't tag issues, WebSearch isn't exhaustive, and memory hallucinates and is bound by a training cut-off, so each silently misses cases. If you can't reach UNCTAD data, say the set can't be completed and scope the answer; note results are current only to UNCTAD's last snapshot and are non-exhaustive per UNCTAD; indicate to users when answers may be impacted by known data gaps.
8. **Attribute and disclaim** every answer (templates below).

## First run: the UNCTAD Excel (walk the user through one download)

Enumeration ("which cases") questions need UNCTAD's full-data Excel in the skill's `data/` folder. If `scripts/query_unctad_excel.py` prints **`DATA_MISSING`** (or before the first enumeration question, if `data/` has no `.xlsx`), do NOT try to fetch the file yourself and do NOT answer from memory. Instead, tell the user — in your own words, covering all four points:

1. **What's needed:** UNCTAD publishes its full ISDS case dataset as a free Excel download; the skill filters it locally to answer "which cases" questions completely and verifiably.
2. **Why they must download it (not you, not the repo):** UNCTAD's Terms permit personal, non-commercial use but bar redistribution — so the skill doesn't ship the file, and each user obtains their own copy directly from UNCTAD under those terms.
3. **Where:** check the release page for the newest version first — https://investmentpolicy.unctad.org/publications/1303/investment-dispute-settlement-navigator-full-isds-data-release-as-of-31-12-2023-in-excel-format- — latest known direct link (31/12/2023 snapshot): https://investmentpolicy.unctad.org/uploaded-files/document/UNCTAD-ISDS-Navigator-data-set-31December2023.xlsx
4. **Then:** ask them to **upload the downloaded file into the chat so you can save it to the skill's `data/` folder** — that way it persists and is reused in every later session without re-uploading. (Users running locally can just place the file in `data/` themselves.) When you receive the upload, save it to `data/` and confirm.

Award retrieval works without the Excel; only enumeration needs it.

## First run: preferences (ask once — language + where to save)

Before the first retrieval, check whether preferences are on record:

```
python scripts/fetch_icsid_award.py --show-config
```

This prints `CONFIG_PATH` (where the script is looking), `CONFIG_DIR_WRITABLE` (whether that location can store preferences), and the stored preferences or `NO_CONFIG`.

On a platform where this skill has not run before, also run `python scripts/fetch_icsid_award.py --check-env` (dependencies, network egress to the source hosts, config writability — see Platform notes) before the first retrieval.

**Look for an existing config before treating this as a first run.** Installed skill folders are commonly mounted read-only, so the config may live outside the skill folder: if the default path prints `NO_CONFIG`, check the root of the user's ISDS research area (where earlier research folders were saved) for `isds-research-config.json`; if found, pass it on every call: `--config "<research area>/isds-research-config.json"`.

If no config exists anywhere, this is the first run: **ask the user two questions in one interview**, telling them the answers are stored so they are asked once:

1. **Preferred language**, stating the policy you will follow:

> I'll (i) default to providing decisions in your preferred language; (ii) indicate when the original version is in a different language; and (iii) if a decision is not available in your preferred language, tell you which languages it *is* available in on the ICSID website and ask how you'd like to proceed — read one of those versions (e.g. an existing ICSID translation), or have me translate the original myself, flagged as my own, non-authoritative translation.

2. **Where research folders should be saved** — the local folder that will hold each topic's memo and retrieved PDFs (see Research folders below). Suggest the project's existing folder on the user's local hard drive if one is visible; otherwise ask the user to name a location they can see and keep. Never propose a temporary, hidden, or sandbox-scratch location. If the user's chosen location is not reachable from the current environment (e.g. a cloud sandbox that cannot write to the user's disk), still record the **user's** path as `research_root` — never a sandbox or session path — and deliver the files for download per Research folders item 6.

Then record both. If `CONFIG_DIR_WRITABLE=yes`, the default location (inside the skill folder) works:

```
python scripts/fetch_icsid_award.py --set-prefer-lang "English" --set-research-root "<research area path>"
```

If `CONFIG_DIR_WRITABLE=no` (read-only skill folder), **ask the user where preferences should live** (suggested default: the root of the research area they just chose — fold this into the same interview), then record with an explicit path and pass the same `--config` on **every** later call, in this and future sessions:

```
python scripts/fetch_icsid_award.py --config "<research area>/isds-research-config.json" \
    --set-prefer-lang "English" --set-research-root "<research area path>"
```

A failed config write never tracebacks: the script prints a `CONFIG NOT SAVED` block with these same instructions and exits with code 3. Never drop the user's answer or silently fall back to re-asking next session — store it at the writable location the user chose.

## Workflow

**Before you answer — the workflow gate (applies to every request, including one-paragraph lookups).**

A request that names a case or passage is a retrieval task, not a question you may answer from the document text — or from memory, a search snippet, or a copy you already have — directly. The brevity of the request never shortens the workflow: "just quote paragraph 154" is still a grounded retrieval that must be configured, filed, and logged. Before you deliver any case text, in order:

1. **Preferences on record?** Run `--show-config` (and, on first use per platform, `--check-env`). A config that has a language but **no `research_root` is incomplete** — you must still ask the research-folder half of the first-run interview. If nothing is on record, run the full interview. Do not infer a research location, and do not proceed on a language-only config.
2. **Retrieve only through the script.** If dependencies are missing, install them; where you cannot, fall back to the script's own `--pdf-file` route or a documented degraded mode and disclose it. Never bypass the script to fetch a document by hand: an ad-hoc download skips the CONFIRM identity check and may pull a non-canonical copy (an exhibit filed in another case, a mirror) instead of the official document.
3. **Folder + document + memo.** Create or locate the topic folder under `research_root`, retrieve and CONFIRM the document, save the PDF, and write the memo (or, for a repeat-topic quick lookup, follow Research folders item 5).
4. **Files reach the user.** Deliver every file to the user's storage and say where (Research folders item 6).

If you are about to quote the document before steps 1–3 are done, stop: you are not using the skill, only imitating its output.

1. **Identify the case (or discover cases).** Get the ICSID case number (e.g. `ARB(AF)/00/2`) or name. For cross-institution or "which cases" discovery, follow the **discovery ladder** (degrade gracefully, disclose at each step):
   1. **Excel helper first** — `python scripts/query_unctad_excel.py …` gives the complete UNCTAD-tagged set up to the snapshot date (see Source routing below).
   2. **Recency window (after the snapshot):** the Navigator's *search/list* views are JS-rendered — `web_fetch` times out on them — so live filtered discovery needs a JS-capable render (an optional prerequisite — **Claude in Chrome** on Claude, or the platform's browsing/agent mode elsewhere), keeping to the specific searches the request needs; never bulk-crawl.
   3. **No JS-capable render available?** Supplement with ICSID's own live case database for the ICSID subset (server-rendered), and/or targeted `WebSearch` — but present these as *non-exhaustive pointers*, never as the complete set (golden rule 7).
   4. Whatever the path, state what the coverage is and what may be missed. Individual Navigator *case pages* (named-case lookups) never need Chrome — they are server-rendered and fetchable by numeric id.

   Then hand each ICSID case off to the retrieval steps below for grounded text. For non-ICSID cases: **PCA**-administered, published matters are groundable too (fetch the specific document — see Sources); other forums (e.g. SCC) yield metadata + the official link only.

2. **List the documents** on the case page:
   ```
   python scripts/fetch_icsid_award.py --case "ARB(AF)/00/2" --list
   ```
   This prints every published document — proceeding, title, date, and one row per available language + URL — plus a machine-readable `JSON_DOCS=` line.

3. **Choose the target document** by title + date + proceeding (e.g. "Award of the Tribunal (May 29, 2003)", not the "Introductory Note"; the right proceeding if there was an annulment). If the choice is unambiguous, pick it. **If several documents plausibly match, ask the user which one** rather than guessing.

4. **Retrieve + CONFIRM.** Download the chosen document and read its first page(s):
   ```
   python scripts/fetch_icsid_award.py --case "ARB(AF)/00/2" --select 1 --query "fair and equitable treatment"
   ```
   The script prints a **CONFIRM** block (case-page label, detected case number, first-page text). Verify the title, parties, case number, and date match the document you intended. If they don't, stop and re-select. Language selection follows the policy below; the script downloads full text (not truncated) and extracts paragraph-aware passages.

5. **Apply the language policy.** If the document is available in the user's preferred language, the script retrieves it and proceeds. **If it is not, the script stops and does NOT substitute another language** — it prints `LANGUAGE CHOICE NEEDED` with the languages the document *is* available in. Tell the user those languages and **ask how they want to proceed**: you often cannot tell from the ICSID page whether one language is authoritative or both are equally authoritative, and the user may prefer an existing ICSID translation (e.g. the English translation of a Spanish original) over a translation you produce. Only after the user chooses do you retrieve that version: `--select N --lang "<choice>"`. In your answer: always state which language you retrieved and whether the page labels it original or translation; note that exact wording is authoritative only in the original where one is indicated; and if the user asks you to translate the original yourself, **label it clearly as your own, non-authoritative translation.**

6. **Answer, grounded.** Quote the relevant passage; give the paragraph number (and page). **Page convention:** when the document's printed page numbers diverge from the PDF's page indices (common in ICSID Reports reprints and repaginated scans), cite both in the format **"p. X (PDF p. Y)"** — printed page first, PDF page in parentheses; when they coincide, a single page number suffices. If the user's point isn't in the retrieved text, say so plainly.

7. **Verify (required).** Before sending, confirm each quote and paragraph number actually appears in the retrieved text. If you cannot verify it, remove it.

8. **Attribute + disclaim.**

## Worked example (single-document question, end to end)

**Question:** "How did the tribunal in Tecmed v. Mexico articulate the fair and equitable treatment standard?"

```
python scripts/fetch_icsid_award.py --case "ARB(AF)/00/2" --list
#  → structured document table, e.g.:
#    [1] Award of the Tribunal — May 29, 2003 — Original proceeding — Spanish, English
#    [2] Introductory Note — …
python scripts/fetch_icsid_award.py --case "ARB(AF)/00/2" --select 1 --query "fair and equitable treatment"
```

The script prints a **CONFIRM** block (case-page label; detected case number `ARB(AF)/00/2`; first-page text showing *Técnicas Medioambientales Tecmed, S.A. v. United Mexican States*, Award, May 29, 2003) — verify title, parties, case number, and date before relying on it — then the matching passages with `para N (p.M)` locators.

**Expected answer shape (abbreviated):**

> The tribunal articulated the FET standard as requiring "…exact passage quoted verbatim from the text retrieved this session…" (Award, ¶154 (p. 61)). Retrieved: English version; the ICSID page also carries the Spanish original — exact wording is authoritative in the original where one is indicated.
>
> Source: International Centre for Settlement of Investment Disputes. Available at https://icsid.worldbank.org.
> For research only; not legal advice. Verify against the official primary source.

This example deliberately does **not** reproduce the ¶154 text: under golden rule 1, the quote must come from the document retrieved in *your* session — never from this file, and never from memory.

## What this tool can answer — and how completely (say so every time)

This tool has deliberate limits: it holds no scraped corpus and has no access to subscription research databases (Investor-State LawGuide (ISLG), Jus Mundi) and no full-text search over italaw (single-document retrieval only, under the last-resort gate in Sources). Acknowledging those limits is part of the design — never paper over them. Classify each question and disclose accordingly:

1. **Single-document questions** ("how did case X discuss topic Y?") — fully answerable: retrieve, confirm, quote with pinpoints. No completeness caveat needed (language/translation flags still apply).
2. **Bounded-set comparisons** ("compare how X, Y and Z treat topic A") — fully answerable *within the named set*, and the answer may rely on those cases alone. **But then run the completeness check (required):** using training knowledge plus a targeted `WebSearch`, consider whether a full treatment of the topic would implicate other cases, lines of authority, or materials you cannot access — and list them as *unexamined leads*, expressly not analyzed. Never let a synthesis generalize from the bounded set to "the law" without this step. (A bounded set can read as a settled trend when the set happens to sit on one side of a doctrinal split — most contested doctrines have a competing line of authority the named cases exclude; the completeness check exists to surface it.)
3. **Enumeration by UNCTAD-taggable category** ("which cases arose from the Venezuelan nationalizations?") — answerable from the UNCTAD data via the Excel helper, with the standing disclosures: treaty-based cases only (contract-only or domestic-investment-law-only disputes are excluded by UNCTAD's methodology), publicly known cases only, snapshot freshness. Where the filter depends on free-text fields (e.g. summary of dispute), note that some rows have empty summaries: filter broadly (respondent/year), review, and say what the method was.
4. **Analytics over the full corpus** ("what is the most-cited case on topic Z?", "how often does arbitrator N dissent?") — NOT completely answerable: that requires citation analytics or full-text search over a complete database this tool does not have. Say exactly that, then — if useful — give a general-knowledge answer clearly labeled as such, stating its basis — training data and/or websearch, as appropriate ("based on general knowledge from training data and/or websearch, not a database search, the leading case is …"), and point the user to ISLG / Jus Mundi for the authoritative answer.

Framing for users: what this tool does well is *verifiable* research — primary-text retrieval with pinpoint cites and honest provenance. What it deliberately does not do is pretend to database-completeness it doesn't have.

## Research folders (persist each topic's memo + documents)

Every research question on a **new topic** gets a local folder in the user's project (workspace), so the memo and the primary documents survive the session and follow-ups build on prior work:

1. **Create the folder** under the user's stored research root (config key `research_root`, set in the first-run interview; if it is missing, or the stored path no longer exists or is not writable, ask the user where research folders should go and update the config with `--set-research-root` — never guess). Name it `YYYY-MM-DD <topic>` (today's date + a short topic label), e.g. `2026-01-15 FET legitimate expectations`. Never create it in a temporary, hidden, or sandbox-scratch location: the folder must be somewhere the user can see and keep.
2. **Save the memo there** as markdown, following the **Memo house style** below. The memo carries the pinpoint cites, the data-freshness footer, attribution, and disclaimer.
3. **Save every retrieved decision PDF there**, using `--save-pdf` on the fetch script, named:
   `<Short case name>, <Institution> <case number>, <Short doc title>, <YYYY-MM-DD decision date>.pdf`
   e.g. `Tecmed v Mexico, ICSID ARB(AF)-00-2, Award, 2003-05-29.pdf`
   (Hyphens replace `/` in case numbers — slashes are illegal in filenames.)
4. **Follow-up questions on the same topic** (e.g. "wasn't this also addressed in a recent decision by X?") do NOT get a new folder: update the existing memo in place (extend, correct, add a dated "Updated" note), and download any additional decisions into the same folder under the same naming convention.
5. **Quick lookups (repeat topic).** A narrow request — quote, locate, or check a single passage — on a topic that already has a folder gets **no new folder**. Save any newly retrieved PDF into the existing folder (skip if a confirmed identical copy is already there) and **always** append a dated provenance line to that folder's `_run-log.md` (the passage, its voice attribution, the pinpoint cite, and how it was verified). Then place the substantive result by whether it answers a **new question** or **re-touches one an existing memo already covers**: if no memo in the folder covers this question, write a short new dated memo in the same folder (brief is fine, but the always-required memo parts — house-style scope rule — still apply); if an existing memo covers it, update that memo in place (extend, correct, add a dated note). Reserve run-log-only (no memo) for genuinely ephemeral checks that yield no quotable work product (e.g. confirming whether a paragraph mentions a term). A quick lookup on a genuinely **new topic** still gets its own folder and memo.
6. **Files must reach the user's storage.** In cloud or sandboxed sessions the assistant's working directory is not the user's disk: a file that exists only in the session workspace is NOT saved. Deliver the memo and every PDF to the user's research root (via the environment's file-delivery/commit mechanism where one exists), and state in the final answer, in plain language, exactly where each file was placed. If delivery fails or is unavailable, say so explicitly and provide the files for download — never describe a scratch-only copy as "saved".
7. **Compliance:** these are local, personal-use copies (permitted by ICSID's and PCA's terms for non-commercial use). Never commit them to a public repo and never republish them; if the project folder is a git repo, ensure the research folders are gitignored.
8. **Privilege note:** when the research supports client work, the memo and folder contents may constitute attorney work product — store them in the client/matter file system under the firm's protocols, and treat where they are saved or shared as a privilege decision for the attorney. The compliance rules in this skill govern *source terms* only; they say nothing about privilege.

## Memo house style

Structure every research memo as follows:

1. **Header:** title; date; the question presented as asked, including its sub-questions.
2. **Bottom line:** the direct answer, briefly. Consistency requirement: the bottom line must not compress away distinctions the grounded sections establish (e.g., which limbs of a dispositif were unanimous vs. by majority).
3. **"How to read this memo & data freshness" note:** one short block stating the grounding rule (every holding, quote, and pinpoint comes from documents retrieved and text-extracted this session, except where expressly flagged), what the flags used in the memo mean, and the not-legal-advice line; describe any limits on the data (snapshot dates and recency gaps).
4. **Per-case grounded sections:** each opens with document identification (exact document title, deciding body, date, page count, saved filename, CONFIRM result) and any retrieval note (delisted document, second-hand grounding, language/translation); then the holdings with ¶/page pinpoints.
5. **Enumeration section** (where the question includes a "how many / which cases" component): method, count, and the standing disclosures (treaty-based only; publicly known only; snapshot freshness).
6. **Completeness check / unexamined leads** (required for bounded-set comparisons): the cases, lines of authority, and cross-cutting issues not examined, expressly labeled as unexamined; note if the leads list is one-sided (e.g., only the adverse line, when unexamined authorities exist on both sides).
7. **Cross-check with training data:** state whether the answer provided accords with general knowledge based on training data and/or websearch (as appropriate — say which) regarding the topic.
8. **Retrieval trail and weak points:** what was retrieved and confirmed, what failed and why, and a candid statement of where the answer is weakest.
9. **Sources & attribution + disclaimer** (templates below).

**Scope — which parts apply (by deliverable class):** parts 1, 2, 3, 7, 8 and 9 (header; bottom line; how-to-read & data freshness; cross-check with training data; retrieval trail and weak points; sources & attribution + disclaimer) are **required for every memo**, whatever the question class — for enumeration-only answers each may be brief, but none may be omitted (the training-data cross-check doubles as a sanity check on a surprising count). Parts 4, 5 and 6 are **conditional on the question class**: per-case grounded sections (4) whenever holdings or decisions are discussed; the enumeration section (5) whenever a count or case-set is given; the completeness check (6) whenever the answer rests on a bounded set of authorities. Charts and tables follow the non-memo deliverables rules in the next section.

**Drafting checklist — verify before saving:** (a) every quote and pinpoint appears in the retrieved text (golden rule 1; workflow step 7); (b) voice correctly attributed throughout — tribunal/committee finding vs. party argument (golden rule 2(a)); (c) unanimity/majority stated for each holding where the record shows it (golden rule 2(b)); (d) the bottom line is consistent with the grounded sections; (e) every statement not grounded in retrieved primary text carries its flag (secondary-sourced status items use the standard `[LIVE / secondary …]` tag — see the labeling rule in Source routing); (f) any disagreement between sources encountered during the run is surfaced with both values and both sources — never silently resolved (see the Conflict rule in Source routing).

## Charts, tables, and other non-memo deliverables

The grounding discipline is format-independent: a chart is a set of factual claims, and every rule above applies to it. For any non-memo deliverable (chart, timeline, table, dataset extract):

1. **Per-datum traceability.** Every fact shown — dates, names, counts, amounts, event markers — must be traceable to an identified source, held to the same rules as memo text: retrieved primary text first; institutional metadata (case-page document lists, dataset fields) identified as such; nothing from unaided recall.
2. **Provenance on the artifact itself.** The deliverable carries a source note (SVG `<desc>`/footnote, table caption) listing the sources used and which data each supports. Approximations and metadata-only data points are disclosed **on the artifact**, not only in a log — a chart travels without its folder.
3. **Flags travel with the data.** Any datum not grounded in retrieved primary text or the local dataset carries its flag on the artifact (the `[LIVE / secondary …]` tag, or "per <metadata source>"), per the Labeling rule.
4. **Lightweight run log (required).** Record in the research folder's `_run-log.md`: each data series → its source (with pinpoint or field name), what was verified and how, and what is approximate or unresolved (including any source conflicts, per the Conflict rule).
5. **Counts shown are counts checked.** Any aggregate displayed (e.g. "6 challenges") must state exactly what is being counted (published decisions vs. underlying applications, and the like) and be re-verified against the fullest retrieved source before it goes on the artifact.

## Source routing (which source answers what)

The UNCTAD Excel snapshot in `data/` is dated (31/12/2023); the live Navigator is itself only refreshed ~biannually (a dated snapshot too); only the institutions' own pages are current. Route by question type:

1. **Enumeration ("which cases…")** → the Excel helper, never memory/WebSearch (golden rule 7):
   ```
   python scripts/query_unctad_excel.py --respondent Argentina --status "favour of investor"
   python scripts/query_unctad_excel.py --breach-found "Umbrella clause" --count-only
   python scripts/query_unctad_excel.py --list-values STATUS
   ```
   Include the script's DATA FRESHNESS footer in the answer. A question with no stated time bound (e.g. "how many cases has X faced?") runs to today and therefore always extends past the snapshot. If the question's time scope extends past the snapshot date, say the Excel cannot cover it and supplement via live discovery (a JS-capable render of the Navigator search if available — the search/list views are JS-rendered and `web_fetch` times out on them; or ICSID's live list for the ICSID subset), disclosing coverage limits.
2. **Named-case status / metadata** → three buckets:
   - *Concluded before the snapshot, no follow-on sensitivity* → Excel data suffices.
   - *Pending at the snapshot, initiated after it, or anything potentially touching follow-on proceedings (annulment / set-aside / resubmission / rectification / enforcement)* → verify live. Rows the helper flags `LIVE_CHECK` need this. Named-case verification needs **no browser**: Navigator case pages are server-rendered and `web_fetch`-able, and resolve by numeric id with any slug (`/investment-dispute-settlement/cases/{id}/x`). Cross-check the institution's live page (ICSID case-detail / PCA). **Order matters: attempt the institution's page and the Navigator case page BEFORE falling back to WebSearch for follow-on status, and log each attempt (success, block, or not-found) in the run log** — a successful institutional fetch upgrades the item from secondary reporting to institutional metadata; a logged block is itself the documented degradation path. Obtain a Navigator case id compliantly — from a targeted WebSearch for the case's Navigator URL or from the Excel's link/DECISIONS fields — **never by guessing or incrementing ids** (a wrong id silently resolves to a different case).
   - *Events after the live Navigator's own update date* → the Navigator cannot answer at any fidelity; go to the institution's live page or targeted WebSearch.
   - **Labeling rule (required):** any status or follow-on item that could not be verified against an institutional page or retrieved primary text — because it post-dates the snapshots, or because the institutional page was unreachable and secondary reporting (targeted WebSearch / press) was used instead — must carry this standard tag **in the memo itself**, not only in a run log: `[LIVE / secondary — as of <YYYY-MM-DD>, per <source type>; verify at <institutional page>]`. Where the authoritative source is **not** an arbitral-institution or UNCTAD page — e.g. a national-court follow-on such as a set-aside by the courts of the seat — the verify element instead names the primary decision and a concrete locator: `verify against <primary judgment cite> at <locator>`, the locator being the court's own website or a public law database (e.g. CanLII, BAILII); never leave the verify element without a locator. Any **money figure** drawn from secondary reporting additionally carries "figure not verified against primary text" — amounts are what secondary reporting most often gets wrong. The tag applies equally to **any post-snapshot count or projection** — including the query helper's cached freshness figures (e.g. a "+N cases since the snapshot" delta derived from the DATA FRESHNESS footer): carry the footer's own "NOT verified now — last known observation <date>" qualifier into the deliverable, and never restate a cached or shipped-default figure as current fact — the freshness cache is machine-local and the script's fallback constant ages, so neither is evidence of the Navigator's state today.
3. **Holdings, quotes, reasoning** → never from any metadata source; always the primary document text via the list→select→confirm pipeline above.
4. **Bars (always):** no italaw fetch outside the last-resort, per-document confirmation gate (see the italaw entry in Sources, golden rule 6, and fallback ladder rung 3 — human-supplied file remains the default; never unconfirmed, never bulk); no id-walking/bulk enumeration of Navigator case pages (targeted, user-initiated lookups only); footers must state the Excel snapshot date and, where used, the Navigator's update date; ground, don't recall.

**Conflict rule (required):** when two retrieved or authoritative sources disagree on a fact — a date, an amount, a count, a status, or a **legal characterization** (a Convention or treaty article number, an annulment ground, a cause of action) — do **not** silently select one. Legal characterizations also get a domain sanity check before being carried: if a secondary source's article label contradicts the provision's settled content (e.g. "improper constitution" labeled Art. 52(1)(d) when that is the 52(1)(a) ground), treat that as a source conflict even if only one source states it. Surface both values in the deliverable itself, identify each source and its class (retrieved primary text / institutional page or document list / dataset metadata / secondary reporting), and flag the conflict as **unresolved** unless a retrieved primary document settles it. Where the fact matters to the answer, say which value the answer provisionally follows and why (primary text outranks institutional metadata; institutional metadata outranks secondary reporting).

Note: the Excel names follow-on decisions but carries **no links to the decision documents** — for follow-on document retrieval use the case's Navigator page or route to ICSID/PCA.

## Retrieval fallback ladder (when the institution's page doesn't yield the document)

Try each rung in order; in the memo, disclose which rung produced each document. Never fill from memory.

1. **Institution page via the script** (`--case`/`--case-url` + `--list`). If the document list is empty, do NOT guess URLs; diagnose the cause (JS-rendered page — rung 2 fixes it — vs. "no documents published by the institution") before proceeding.
2. **JS-capable render, then `--doc-url`.** ICSID case pages are inconsistently server-rendered per case; a real browser resolves the JS ones. Open the case page, identify the document row (title + date + proceeding + language, per golden rule 3), copy the exact PDF href, and pass it to the script with `--doc-url` (the CONFIRM check still runs). Prerequisites vary by platform: on Claude, the Claude in Chrome extension must be installed, signed in, and have site access enabled (a "blocked by your organization's policy" error means site access is off; a Chrome restart may be needed after enabling it); on other platforms, use the assistant's browsing/agent mode where it can render JS pages. **If the rendered page also lists no documents, the institution publishes none for this case** — rung 2 cannot help; record that finding and move to rung 3.
3. **User-supplied copy (`--pdf-file --source-url`).** Ask the user to obtain the document manually and supply the file — from the institution if they can reach it, or from a source whose terms permit *manual* access (italaw permits manual human browsing — manual supply is the **default** route for italaw documents). **Harvest a concrete URL first (required):** before (or at) the rung-3 stop, check UNCTAD's metadata for a per-document link — the Navigator case page's decisions/documents fields and the Excel's DECISIONS field often carry one. If it points at italaw, hand that exact URL to the user for manual download; if it points at an institution, use `--doc-url` directly instead. **If the user declines to download manually,** an automated italaw fetch of that single document is permitted as the fallback — but only under the per-document confirmation gate in the italaw entry under Sources (golden rule 6): re-present the exact URL, obtain a fresh affirmative approval, fetch under the platform's own user-initiated agent token (never a spoofed browser UA), and log the approval; the CONFIRM check still runs. In a **non-interactive run** where no user can be asked, record the harvested URL in the memo's unretrieved-lead entry so the user can act on it later — a concrete link, not a generic "e.g., italaw". Record provenance with `--source-url`; corroborate identity via the CONFIRM block plus an independent cross-check where available (e.g., the URL's presence in UNCTAD's dataset). *Malformed-PDF guard:* third-party copies may crash pdfplumber (xref RecursionError) — sanity-check with `pdftotext`, repair with `qpdf <in> <out>` before extraction, save the original as the archival copy, and note the repair in the memo's retrieval note.
4. **Companion-decision grounding ("as recounted in").** If the document is unavailable through rungs 1–3 (e.g., a delisted award), its holdings may be quoted as recounted in a retrieved companion decision (annulment, resubmission, related award), under four rules: (1) flag every recounted cite at the pinpoint; (2) distinguish the companion decision's *own* recitals and findings from *party characterizations* it reports, and attribute party voice explicitly; (3) prefer passages the companion decision quotes **verbatim** from the missing document over passages it merely paraphrases; (4) where available, cross-corroborate the recounted holding in a second, independently retrieved document — and before recording cross-corroboration as unachievable, run a targeted search for **related awards or decisions that quote or restate the missing document** (parallel cases on the same measures or treaty often quote a delisted award verbatim; check first any related cases named in the memo's own 'Cross-check with training data' section), and retrieve any that are institution-published.
5. **Unretrieved lead.** If no rung succeeds, record the document as an unretrieved lead and say so in the memo: state what was attempted and why retrieval failed. Never fill the gap from memory.

## Failure-mode guards

- **Empty document list.** If `--list` returns nothing, do **not** guess a PDF URL — follow the **Retrieval fallback ladder** above. Two distinct causes, diagnosed per case, not per site: some ICSID case pages inject the document list client-side via JavaScript (rung 2 resolves them), while for others the institution **publishes no documents at all** (a rendered browser shows the same empty list — no amount of rendering helps; go to rung 3). In a headless/unaided run with no JS render and no user available, the correct terminal outcome is rung 5: record the document as an *unretrieved lead*.
- **Scanned PDF.** If the CONFIRM block reports no extractable text on the first pages, the file is likely a scanned image. Do not claim to have confirmed it; flag that it needs OCR or manual verification before you rely on it or quote from it.
- **Blocked document host.** If the environment cannot reach the document host (e.g. a sandbox egress block on `docs.pca-cpa.org`), do NOT substitute an unofficial mirror. Ask the user to download the document from the official case page themselves and upload it; then process it with `--pdf-file <path>` (confirmed and extracted exactly like a download) and save it into the research folder under the naming convention. A failed fetch never tracebacks: the script prints a `FETCH FAILED` block naming the URL, the error, and the fallback routes, and exits with code 5.
- **Paragraph numbers visible but not extractable.** Some awards (e.g. Philip Morris v. Uruguay) render paragraph numbers that are not in the PDF's text layer, so extraction yields page-level blocks with no ¶ numbers; in the hardest variant the margin numbers are drawn as **image objects** (e.g. ConocoPhillips v. Venezuela, Award, 8 March 2019 — the extractor desyncs after the front matter and most blocks come back unnumbered). Do not settle for page-only cites. **Locate first:** where the numbers are image objects, each body page typically carries one small image per paragraph that begins on it, so the per-page image count (pdfplumber `page.images`), cumulated across body pages, maps paragraph numbers to pages — use it to estimate the target page instead of rasterizing hundreds of pages. **Then verify visually:** rasterize the estimated page plus neighbours from the *saved* PDF (`pdftoppm -png -r 110 -f <first> -l <last> <pdf> <prefix>`), read the printed margin numbers (a consecutive run around the target pins it unambiguously), and match each quoted passage to the paragraph number you can see, cross-checking the transcription against the PDF's extractable text layer. Cite ¶ + page, and disclose in the memo that the ¶ numbers were read visually from the rendered pages.
- **Paragraph numbering restarts per Part/Chapter.** Some awards (e.g. Methanex v. USA, Final Award 2005) restart ¶ numbering in each Part/Chapter, so a document-wide ¶ number is meaningless. The fetch script detects restarts confirmed by structural headings and prints **section-relative** cites carrying the heading verbatim (e.g. `PART IV - CHAPTER D, para 7 (p.278)`); when it reports restarts, always give the section alongside the ¶ number in the memo and verify each heading against the document. The script also auto-detects the document's marker convention — `154. ` or bracketed `[324] ` (e.g. Iberdrola v. Guatemala) — and matches only the dominant one. If it instead **warns** that most blocks are unnumbered and markers follow a convention it does not recognize, do not trust ¶ cites from the extraction: fall back to page-based cites or the rasterize-and-read guard above.
- **Exhibit copies are not the document.** A decision hosted as another case's *exhibit* (e.g. `CLA-xxx` on ICSID's server) may be commentary or a partial copy — the CONFIRM block will reveal a book chapter or excerpt. Never rely on it without confirming it is the full primary text; prefer the issuing institution's own copy.

## Platform notes

This skill follows the open Agent Skills standard (`SKILL.md` + `scripts/`) and is designed to run on any platform that implements it. Everything above is platform-neutral unless it names a platform expressly. Differences that matter:

1. **Environment check (first use on any platform).** Run `python scripts/fetch_icsid_award.py --check-env` before the first retrieval: it reports the Python version, dependencies (`requests` and `pdfplumber` required; `openpyxl` for enumeration), network egress to each source host, and the config location and writability, ending in a PASS / DEGRADED verdict. Choose the full pipeline or a degraded mode from the result — and disclose the mode in the answer.
2. **Code sandbox without network egress.** If the sandbox cannot reach the source hosts, the retrieval script cannot fetch. Degrade honestly, in order: (a) the assistant's built-in page fetch/browsing to identify the correct document on the case page (golden rule 3 still applies) and retrieve it — disclosing that built-in fetches may truncate long documents (~120k chars ≈ 38 pp), so coverage may be partial; (b) the user downloads the PDF from the official source and uploads it; process with `--pdf-file` — fully offline, preserving the whole pipeline (CONFIRM, extraction, verification). Never present a truncated fetch as full coverage.
3. **Persistence differs by session type, not by vendor.** Where the user has a persistent, user-visible folder (e.g., a connected project folder in Claude Cowork, or a local filesystem in a CLI), the Research folders and First-run rules apply as written. Where the session has no persistent, user-visible filesystem — ChatGPT today, and equally a plain claude.ai chat with no connected folder — say so: deliver the memo and PDFs as downloads, note that preferences cannot persist across sessions there and the first-run interview recurs each session (a platform limit, not an error), and expect the UNCTAD Excel in `data/` to need re-uploading per session. Mitigation: keep `isds-research-config.json` at the root of the user's research area and have the user re-supply it at session start (passed via `--config`), so the stored answers are confirmed rather than re-asked.
4. **Fetch-agent compliance is per-platform, and dated.** Robots.txt status for each source, for the user-initiated tokens `Claude-User` and `ChatGPT-User`, was verified 2026-07-18 and is recorded in the per-source entries above (Sources, golden rule 6): as of that date every source permits both tokens; italaw operatively disallows only the bulk crawlers `ClaudeBot`/`GPTBot`, which this skill never uses. On any other platform, verify that platform's user-initiated token against each source's robots.txt before automated fetching; never spoof a human-browser user-agent; and do not rely on any platform's position that robots may not bind user-initiated agents (OpenAI states this for `ChatGPT-User`) — this skill treats robots as binding. Site Terms obligations (non-commercial use, no redistribution, italaw's manual-default and per-document gate) are platform-agnostic. The helper scripts always send their own declared user-agent (`isds-research-skill/<version>`). Robots files change — re-verify periodically and re-date these notes.

## Attribution and disclaimer

- Source line (ICSID requires attribution):
  `Source: International Centre for Settlement of Investment Disputes. Available at https://icsid.worldbank.org.`
- PCA source line (for PCA-sourced material):
  `Source: Permanent Court of Arbitration. Available at https://pca-cpa.org. Used for non-commercial research.`
- Disclaimer:
  `For research only; not legal advice. Verify against the official primary source.`

## Notes

- Issue-agnostic: FET, expropriation, jurisdiction, costs, annulment, etc.
- Be polite when fetching: the script sets a descriptive User-Agent and sleeps between requests.
- Keep retrieved documents local to the session; never republish.
- Built-in fetch fallback: if the script can't run, the assistant's built-in page fetch (`web_fetch` or the platform's equivalent) on a confirmed PDF URL works but **truncates very long PDFs (~120k chars ≈ 38 pp)**, so it can silently drop later paragraphs (e.g. a holding at ¶154 / p.61). Prefer the script for full coverage; if you must use `web_fetch`, say that coverage may be partial.
