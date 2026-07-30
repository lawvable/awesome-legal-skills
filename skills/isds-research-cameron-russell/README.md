# ISDS Research skill

This is a retrieval-grounded research aid for investor-State dispute settlement (ISDS) awards. It answers questions on investment dispute cases and topics by retrieving **primary documents on demand** from ICSID, PCA, and other official sources to ground answers in the actual award text, with pinpoint (paragraph / page) citations. It complies with the terms of the public databases on which it relies; it never scrapes or hosts a corpus, and it cites only text it actually retrieved.

**Not legal advice.**

## How to install in Claude

1. **Download the skill.** Download the packaged ZIP file here: https://github.com/ccrnyc/isds-research/releases/latest/download/isds-research.zip (alternatively, download from this repo's [Releases page](../../releases)).
2. **Ensure "Cloud code execution and file creation" is enabled so skills can run**. On Free/Pro/Max plans: go to Settings > Capabilities > and make sure "Cloud code execution and file creation" is turned on. On Team/Enterprise plans: your organization Owner enables Skills under Organization settings > Skills.
3. **Upload the skill.** Go to Customize > Skills, click "+" or "Add"  → "Upload a skill", and select the ZIP. Select the skill and toggle it on.

To use the skill, just ask an ISDS question — e.g. *"How did the tribunal in Tecmed v. Mexico articulate the fair and equitable treatment standard?"* your assistant will invoke the skill automatically.

For full functionality, see **Network requirements** below. Depending on your assistant and platform, you may also need to adjust network settings and folder permissions so the assistant can reach the source websites and save files to a local folder — running `--check-env` first reports whether dependencies, network access, and a writable research folder are in place, and flags what to fix.

## How to install in ChatGPT

Skills in ChatGPT follow the same open Agent Skills standard, so the same ZIP is used. As of July 2026, OpenAI lists Skills as available on ChatGPT Business, Enterprise, Edu, and Healthcare plans (plus Codex and the API); if no **Skills** section appears in your ChatGPT profile menu, your plan may not include them yet.

1. **Download the skill** — same ZIP as above.
2. **Upload the skill.** If your plan shows a **Skills** section, open your profile menu → **Skills** → **Create** → **Upload from your computer**, and select the ZIP; uploaded skills are scanned by OpenAI and may be marked "Needs Review" or "Blocked" before they can be used. **If no Skills section appears** (e.g. on free accounts), install through the Codex CLI instead: unzip the same archive into your Codex skills directory — `unzip isds-research-*.zip -d ~/.codex/skills` — which yields `~/.codex/skills/isds-research/SKILL.md`. The install path varies by plan; the skill content is identical.
3. **Run the environment check** in a new chat — ask ChatGPT to run the skill's `--check-env` (see `SKILL.md` → Platform notes). If the code sandbox cannot reach the source hosts, the skill still works in the degraded modes described there (built-in browsing fetch with disclosed truncation, or you upload the PDF and it is processed with `--pdf-file`).

## What's here

- `SKILL.md` — the agent skill: workflow, compliance guardrails, attribution/disclaimer, and the golden rule (ground, don't recall).
- `WRITEUP.md` — design notes: why it's built this way, how it was evaluated (10-item adjudicated eval; version 1.0 graded overall A−), and the *Saluka*→*Methanex* phantom-citation finding.
- `scripts/fetch_icsid_award.py` — lists the documents on an ICSID case page, downloads the one you select, shows its first page(s) so you can confirm it is the right document, then extracts paragraph-aware text (full PDF, no truncation), with optional query matching. Handles both paragraph-marker conventions (`154. ` and bracketed `[324] `, auto-detected) and per-Part/Chapter numbering restarts (e.g. Methanex): heading-confirmed restarts yield section-relative cites ("PART IV - CHAPTER D, para 7"); unrecognized numbering conventions trigger an explicit warning to fall back to page-based cites.
- `scripts/query_unctad_excel.py` — filters the local UNCTAD full-data Excel snapshot (`data/`) for "which cases" questions: any combination of respondent, treaty, outcome, breach, sector, rules, year, arbitrator, free text; extracts ICSID case numbers (they live inside the case-name/link text, not a dedicated column); flags rows whose snapshot data is presumptively stale (`LIVE_CHECK`: pending at snapshot, follow-on pending, or recent activity); and appends a mandatory data-freshness footer (snapshot date, UNCTAD's non-exhaustive caveat, and a throttled ≤1×/day live check of the Navigator's "Updated as of" date, degrading to "last known" when offline).
- `data/` — where **your own copy** of UNCTAD's official full-data Excel lives (1,332 cases in the 31/12/2023 release; the live Navigator runs ~2 years ahead of it). **The file is not included in this repo** — UNCTAD's terms bar redistribution; see the download section below. Used locally for non-commercial filtering only, never republished.

## Get the UNCTAD data (required, one download)

The skill's "which cases…" (enumeration) features run on UNCTAD's official full-data Excel, which is **not included in this repo**: UNCTAD's [Terms of Use](https://investmentpolicy.unctad.org/pages/1048/terms-and-conditions-of-use) permit personal, non-commercial use but bar redistribution, so each user downloads their own copy directly from UNCTAD (free, no registration):

1. Check UNCTAD's [release page](https://investmentpolicy.unctad.org/publications/1303/investment-dispute-settlement-navigator-full-isds-data-release-as-of-31-12-2023-in-excel-format-) for the full-data release; as of this writing the latest is the **31/12/2023 snapshot**: [direct download](https://investmentpolicy.unctad.org/uploaded-files/document/UNCTAD-ISDS-Navigator-data-set-31December2023.xlsx).
2. Put the `.xlsx` in this skill's `data/` folder. In a chat (Claude Cowork / claude.ai, ChatGPT, etc.), you can simply **upload the file and ask your assistant to save it into the skill's `data/` folder** — where the platform persists skill files across sessions, it is reused without re-uploading (see `SKILL.md` → Platform notes).

If you run the skill without the file, `query_unctad_excel.py` prints these same instructions (`DATA_MISSING`) instead of failing cryptically. Award retrieval (`fetch_icsid_award.py`) works without the Excel; only enumeration needs it.

## Install & run

```
pip install requests pdfplumber openpyxl

# (first use on any platform) check dependencies, network egress, and config writability
python scripts/fetch_icsid_award.py --check-env

# (first run, asked once) record your preferred language and where research
# folders (each topic's memo + retrieved PDFs) should be saved
python scripts/fetch_icsid_award.py --set-prefer-lang "English" --set-research-root "<your research folder>"

# 1) list every document on the case page (proceeding, title, date, languages)
python scripts/fetch_icsid_award.py --case "ARB(AF)/00/2" --list

# 2) select one, confirm it from its first page, and search it
python scripts/fetch_icsid_award.py --case "ARB(AF)/00/2" --select 1 --query "fair and equitable treatment"
```

Step 2 prints a CONFIRM block (case-page label, detected case number, first-page text) so you can verify the document before relying on it, then the matching passages with `para N (p.M)` citations, plus the required ICSID attribution and a not-legal-advice disclaimer.

**Language** is treated as an attribute, not a filter: awards available only in Spanish/French/etc. are valid results. The tool retrieves your preferred language when it exists; when it doesn't, it does not silently substitute — it lists the languages the document *is* available in and asks how you want to proceed (read an existing ICSID version, or get a flagged, non-authoritative translation of the original), because the page doesn't always establish which language is authoritative. Supply the choice with `--select N --lang "<language>"`.

**Preferences & read-only installs.** Preferences (language, research-folder root) live by default in `scripts/user-config.json` beside the script. Installed skill folders are often mounted read-only: `--show-config` reports this up front (`CONFIG_DIR_WRITABLE=no`), and a failed save prints a clear `CONFIG NOT SAVED` block (exit code 3) instead of a traceback. In that case keep the config at a writable location of your choice — conventionally `isds-research-config.json` at the root of your research folder — and pass `--config "<research folder>/isds-research-config.json"` on each call; in Claude, the skill asks you once where preferences should live and reuses that location in later sessions.

## Network requirements

The scripts fetch documents and metadata directly, so the environment running them needs outbound access to these official hosts:

- `icsid.worldbank.org` — case-detail pages
- `icsidfiles.worldbank.org` — the document PDFs
- `investmentpolicy.unctad.org` — your own download of the UNCTAD Excel, and the helper's freshness check
- `pca-cpa.org` / `docs.pca-cpa.org` — PCA case pages and documents

**italaw is deliberately not on this list.** The default route for italaw documents is you downloading them manually in your browser (see Compliance notes) — the tool needs no italaw network access unless you explicitly approve the gated, per-document fallback.

**Please add these sites to your allow list to use the tool's full functionality.**

- **claude.ai / Cowork on Team or Enterprise plans:** network access is controlled by your organization Owner. If the scripts report blocked hosts, discuss with the Owner whether these domains can be added to the allow list (or network access enabled).
- **Claude Code:** approve the per-domain network prompts on first use, or pre-allow the hosts under `sandbox.network.allowedDomains` in your `settings.json`.
- **ChatGPT:** the Skills code sandbox's network policy is not documented; run `--check-env` after installing. If the hosts are unreachable, use the degraded modes in `SKILL.md` → Platform notes.

Any settings change is yours to make — the skill never modifies your settings. These domains govern the skill's *scripts*; your assistant's built-in web fetch/browsing (and, on Claude, the optional Claude in Chrome) is governed separately by the platform's own settings.

## Discovery & data freshness (graceful degradation)

"Which cases…" questions follow a **discovery ladder** — each rung degrades gracefully to the next, and the answer always discloses which rung it stands on:

1. **Local UNCTAD Excel** (`scripts/query_unctad_excel.py`) — the complete, filterable set of UNCTAD-tagged cases up to the snapshot date (currently 31/12/2023). Primary and sufficient for questions bounded by the snapshot.
2. **Live Navigator search** — for the recency window after the snapshot. The Navigator's search/list views are JS-rendered, so this rung requires a JS-capable browser render — on Claude, the optional Claude in Chrome extension (install: https://code.claude.com/docs/en/chrome); on other platforms, the assistant's browsing/agent mode. Targeted searches only; never bulk-crawled.
3. **Without Chrome** — the skill does *not* fail or fake completeness: it supplements with ICSID's own live case database (server-rendered) for the ICSID subset and/or targeted web search, expressly flagged as non-exhaustive pointers rather than a complete set.

Named-case lookups never need a browser: individual Navigator case pages are server-rendered and resolve by numeric id (`/investment-dispute-settlement/cases/{id}/{any-slug}`). Note the freshness layers: Excel snapshot (31/12/2023) < live Navigator (itself a ~biannual snapshot; currently 31/12/2025) < the institutions' own live pages (ICSID/PCA) — truly current status comes only from the last layer. The helper's `LIVE_CHECK` flag marks rows whose snapshot data is presumptively stale; its freshness check requires outbound network (works on a normal machine / Claude Code; some sandboxes block it, in which case it reports "NOT verified now" and continues).

## Design (the RAG pipeline)

```mermaid
flowchart TD
    Q["User question"] --> C{"Classify the question<br/>(disclosure classes 1&ndash;4)"}

    C -->|"enumeration:<br/>which cases?"| E["UNCTAD Excel helper<br/>(query_unctad_excel.py)<br/>+ mandatory DATA FRESHNESS footer"]
    E -->|"time scope past<br/>the snapshot"| CH["Live Navigator search (JS render,<br/>browser-capable agent) or ICSID live list /<br/>targeted web search &mdash; flagged non-exhaustive"]
    C -->|"named case:<br/>holdings, quotes"| L["List documents on the case page<br/>(fetch_icsid_award.py --list)"]
    C -->|"full-corpus<br/>analytics"| X["Declared NOT completely answerable;<br/>labeled general-knowledge pointer;<br/>refer to ISLG / Jus Mundi"]

    L --> S["Select by title + date + proceeding<br/>(ask the user if ambiguous)"]
    S --> CF{"CONFIRM against the<br/>document's own first pages"}
    CF -->|"mismatch"| S
    CF -->|"match"| LANG{"Available in the user's<br/>preferred language?"}
    LANG -->|"no"| ASK["STOP &mdash; list available languages,<br/>ask how to proceed"]
    ASK --> EXT
    LANG -->|"yes"| EXT["Paragraph-aware extraction<br/>(marker-convention detection;<br/>section-relative cites on restarts)"]
    EXT --> V["Verify: every quote and pinpoint<br/>re-checked against the retrieved text"]
    V --> A["Grounded answer / memo:<br/>pinpoint cites, flags, freshness footer,<br/>attribution + disclaimer"]

    L -.->|"empty list / blocked host /<br/>delisted document"| F["Fallback ladder:<br/>1. institution page &rarr; 2. JS render &rarr;<br/>3. user-supplied file (italaw last-resort gate) &rarr;<br/>4. companion-decision grounding &rarr;<br/>5. unretrieved lead (disclosed)"]
    F -.-> CF
```

1. **Discovery** — the ladder above: local UNCTAD Excel → JS-rendered Navigator search (a browser-capable agent, e.g. Claude in Chrome) → ICSID live list / targeted web search with disclosed limits. ICSID's own case database (permissive robots) for ICSID cases; never bulk-harvested.
2. **Identify** — fetch the ICSID case-detail page and parse *all* published documents into a structured table (proceeding, title, date, and every available language + URL), rather than grabbing "the first English PDF".
3. **Confirm** — download the selected document and read its first page(s) to verify title, parties, case number, and date match the intended document before relying on it.
4. **Extract** — pdfplumber, page-by-page, detecting paragraph numbers so answers carry pinpoint cites (full PDF, no truncation).
5. **Ground** — answer only from retrieved text; if a point isn't there, say so.
6. **Verify** — confirm every quote/paragraph appears in the retrieved text before sending.

## What this tool does well and does not do

**Does well:** verifiable research. Single-document questions ("how did *Tecmed* treat proportionality?") get pinpoint-cited answers grounded in the confirmed primary text. Bounded comparisons ("compare X, Y, Z on topic A") get the same, plus a required completeness check that flags — as expressly unexamined leads — any other cases or lines of authority a full treatment of the topic would need. Category enumeration ("which treaty cases arose from the Venezuelan nationalizations?") runs on UNCTAD's official dataset with its scope and snapshot date disclosed.

**Deliberately does not:** corpus analytics. There is no scraped award corpus here (by design — see Compliance notes) and no access to subscription databases (Investor-State LawGuide, Jus Mundi, italaw full-text). So questions like "the most-cited case on topic Z" or "how often does arbitrator N dissent" cannot be answered completely; the tool says so, offers a clearly-labeled general-knowledge pointer, and refers the user to the databases built for that job. The tool is designed to be honest about its limits: every answer states what was actually examined and what wasn't.

## Compliance notes

- **ICSID** Terms permit viewing/downloading for personal, non-commercial use; no redistribution or derivative database. Attribution required (the script emits it).
- **UNCTAD** is discovery/metadata only; its robots blocks bulk/training crawlers and its Terms bar compiling/redistributing its dataset — so it is used human-directed or via targeted user-initiated agent fetches (`Claude-User` / `ChatGPT-User`), never bulk-harvested.
- **italaw** is a **last-resort, per-case-confirmed fallback only**: official sources (ICSID/PCA) first; the default route is the user downloading the document manually (italaw's Terms expressly permit manual browsing); an automated fetch happens only with per-document human confirmation, under the platform's own user-initiated agent token, one document per approval, reference-don't-reproduce, and logged. italaw content never enters any build/test corpus. See the italaw entry in SKILL.md for the full conditions.
- Polite access: descriptive User-Agent, courtesy delay between requests, single-document on-demand only.
- Robots.txt for every host above re-verified 2026-07-18 for `Claude-User` and `ChatGPT-User` — see `SKILL.md` → Platform notes and the per-source entries there. Robots files change; re-verify periodically.

## License

Copyright (C) 2026 Cameron Russell (ccrnyc). Licensed under the **GNU Affero General Public License v3.0** (`AGPL-3.0-only`) — see [LICENSE](LICENSE). This program comes with ABSOLUTELY NO WARRANTY. The license covers the skill's code and documentation only; retrieved documents and the UNCTAD dataset remain governed by their own sources' terms (see Compliance notes).

## Known constraints

- `web_fetch` (the no-code fallback) truncates very long PDFs at ~120k characters, which silently drops the later paragraphs of a long award — a holding deep in the document simply vanishes from view. The script avoids this by downloading the file and extracting with pdfplumber — run it where the host (`icsidfiles.worldbank.org`) is reachable. Note `icsidfiles.worldbank.org` returns 403 on a bare-domain request but serves real PDF paths normally; some sandboxes block the host at the network proxy, in which case run locally or in a network-capable environment.
- ICSID case-detail pages are inconsistently rendered per case: most carry the document links in the initial HTML (plain `requests` sees them), but some inject the list client-side. When the document list comes back empty, the skill does not guess — it diagnoses the cause and falls back to a JS-capable render or asks for the document URL (see the retrieval fallback ladder in SKILL.md).
