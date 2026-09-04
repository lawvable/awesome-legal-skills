# ISDS Arbitrators skill

**isds-arbitrators** is an arbitrator research tool for investor-State dispute settlement (ISDS), built for arbitration counsel. It produces reliable, structured, and thorough insights into arbitrators' experience, and can identify, evaluate, and rank the suitability of arbitrators for specific disputes. The tool flags decisions and publications that bear on the issues in the dispute, checks an arbitrator's caseload, and suggests additional issues for counsel's consideration prior to nomination.

**Evaluate named arbitrators.** Ask about any arbitrator (or several) and receive a structured profile: appointments by appointing party, case lists, dissents, annulment work, issue track records (e.g. fair and equitable treatment, expropriation, jurisdiction), tribunal composition, double-hatting, and challenge history. Every figure is grounded in the UNCTAD ISDS Navigator dataset (a workbook you download yourself) plus a targeted live lookup of the arbitrator's ICSID profile, with sources and dates disclosed.

**Find and rank arbitrators for your case.** Describe the case (e.g. Claimant-side or Respondent-side, applicable treaty and rules, issues, sector, language) and the tool screens the full arbitrator pool and returns a ranked shortlist with transparent, user-adjustable ranking weights, a comparison sheet, and a full profile for every finalist.

**Check the record.** On request, the tool digs deeper on any issue (e.g. dissents, challenges, publications) by retrieving and reading the actual decisions (via its companion skill, isds-research), so characterizations rest on primary documents with pinpoint citations, not secondary source summaries.

This is a research aid. It covers publicly available treaty-based ISDS cases only — commercial arbitration and confidential proceedings are not visible — and complies with the terms applicable to public databases. Final arbitrator choice is left for counsel. Deliverables carry attorney-work-product headers and state their data freshness.

**Not legal advice.**

## How to install in Claude

1. **Download the skill.** Download the packaged ZIP file here: https://github.com/ccrnyc/isds-arbitrators/releases/latest/download/isds-arbitrators.zip (alternatively, download from this repo's [Releases page](../../releases)). The skill is also listed on [Lawve](https://lawve.ai/@cameron-russell).
2. **Ensure "Cloud code execution and file creation" is enabled so skills can run.** On Free/Pro/Max plans: go to Settings > Capabilities and make sure "Cloud code execution and file creation" is turned on. On Team/Enterprise plans: your organization Owner enables Skills under Organization settings > Skills.
3. **Upload the skill.** Go to Customize > Skills, click "+" or "Add" → "Upload a skill", and select the ZIP. Select the skill and toggle it on.

To use the skill, just ask — e.g. *"Tell me about arbitrator Brigitte Stern"* or *"Help me choose a co-arbitrator for an Energy Charter Treaty renewables dispute"* — and your assistant will invoke it automatically.

**Companion skill (strongly recommended):** install [isds-research](https://github.com/ccrnyc/isds-research) (also on [Lawve](https://lawve.ai/@cameron-russell)). Whenever a record check requires retrieving and reading the underlying decisions, this skill delegates the retrieval and grounding methodology to isds-research. Without it, record checks fall back to a summary retrieval ladder with less depth.

## What's here

- `SKILL.md` — the agent skill: the two workflows (profiles; case-based selection), compliance guardrails, hard sourcing rules, and the delivery checklist every run must pass.
- `references/` — the profile output template (fixed section order, footnote conventions, annex column spec), the deeper-analysis playbook for record checks, a worked example profile, and the per-source compliance table.
- `scripts/query_arbitrators.py` — the query engine over the UNCTAD Excel: name resolution (alias-safe, never merges name variants on similarity), per-arbitrator profile extraction, shortlist screening (`--shortlist --issue ... --rules ... --role ... --treaty ...`) with pool-normalised, user-adjustable ranking weights (`--weights`; `--raw-scores` for legacy raw counts), full per-case annex export (`--annex`), and a delta workflow for cases newer than the snapshot (`--delta-file`).
- `scripts/parse_icsid_cvids.py` — rebuilds the name → ICSID-profile-page map from your own saved copy of ICSID's arbitrator listing page.
- `assets/` — `icsid-cvid-map.json` (name → public ICSID profile-page URL) and `curated-aliases.json` (verified name variants only).
- `data/` — where **your own copy** of UNCTAD's official full-data Excel lives. **The file is not included in this repo** — UNCTAD's terms bar redistribution; see below.

## Get the UNCTAD data (required, one download)

The dataset layer runs on UNCTAD's official full-data Excel, which is **not included in this repo**: UNCTAD's [Terms of Use](https://investmentpolicy.unctad.org/pages/1048/terms-and-conditions-of-use) permit personal, non-commercial use but bar redistribution, so each user downloads their own copy directly from UNCTAD (free, no registration):

1. Check UNCTAD's [release page](https://investmentpolicy.unctad.org/publications/1303/investment-dispute-settlement-navigator-full-isds-data-release-as-of-31-12-2023-in-excel-format-) for the full-data release; as of this writing the latest is the **31/12/2023 snapshot** (1,332 cases): [direct download](https://investmentpolicy.unctad.org/uploaded-files/document/UNCTAD-ISDS-Navigator-data-set-31December2023.xlsx).
2. Put the `.xlsx` in this skill's `data/` folder (any filename with the UNCTAD schema is accepted; the engine validates the header row and prints a load-verification line). In a chat you can simply upload the file and ask your assistant to save it into the skill's `data/` folder — see `data/README.txt` for how cloud sessions persist it.

If you run the engine without the file, it prints these same instructions instead of failing cryptically.

## Install & run

```
pip install openpyxl

# a profile
python scripts/query_arbitrators.py --arbitrator "Stern"

# a shortlist: Energy Charter Treaty, FET issue, respondent-side co-arbitrator
python scripts/query_arbitrators.py --shortlist --treaty "Energy Charter" \
    --issue "Fair and equitable treatment" --role "Arbitrator" --respondent-gate

# the full per-case annex for one arbitrator
python scripts/query_arbitrators.py --arbitrator "Stern" --annex "stern-annex.xlsx"
```

Shortlists always print the ranking weights in force; adjust them with `--weights your-weights.json`. Scores are normalised against the candidate pool so no single high-volume metric dominates; `--raw-scores` restores plain raw-count scoring.

The engine is the corpus-wide layer only. The skill's full workflow adds, per candidate: a targeted live lookup of the arbitrator's ICSID profile page, an availability check against named, dated sources, CV and publications screening, and (on request) record checks grounded in the retrieved decisions.

## Network requirements

The skill fetches targeted pages directly, so the environment running it needs outbound access to:

- `icsid.worldbank.org` — per-arbitrator profile pages and case-detail pages
- `investmentpolicy.unctad.org` — your own download of the UNCTAD Excel; individual case pages
- `pca-cpa.org` / `docs.pca-cpa.org` — PCA case pages and documents (record checks)

CV hosts (chambers, universities, arbitral institutions) usually block automated fetch; the skill links them and tells you visibly — download-then-upload, or a browser extension you control. italaw is links-only by design: the user downloads manually. Any settings change is yours to make — the skill never modifies your settings.

## What this tool does well and does not do

**Does well:** grounded arbitrator research with disclosed sources. Every profile states what each figure rests on (UNCTAD snapshot, live ICSID lookup, or a retrieved decision), quarantines unverified secondary-source claims outside the tables, and never resolves conflicting values silently — it shows both or says "not established."

**Honest limits you should know:**

- **The ICSID profile page is a floor, never a complete case list.** Testing measured roughly 77% coverage of ICSID-numbered appointments for one heavy-load arbitrator, with no pattern explaining the omissions. Counts built on it are "at least", never "is", and absence from the profile is weak evidence of inactivity.
- **Snapshot data ages.** The Excel is a 31/12/2023 snapshot; for active arbitrators it materially understates current activity. Every output carries a data-freshness footer; newer cases are handled by a live delta workflow, classified by the arbitrator's acceptance date, never by case-number year.
- **Availability is never assumed.** Death, retirement, or unavailability is never asserted without a named, dated source, and no candidate is screened out on an unverified availability premise.

**Deliberately does not:** recommend or rank-order the appointment decision itself; assert personal "win rates" or individual votes without the retrieved decisions; cover commercial (non-treaty) arbitration; access Jus Mundi, GAR ART, Arbitrator Intelligence, or italaw by automated fetch; run any bulk harvest. For fuller analytics, every output refers you to the subscription databases built for that job.

## Compliance notes

- **Targeted, user-initiated lookups only.** No bulk harvesting, no id-walking, no scraping-and-hosting. Hosts not in the skill's compliance table are treated as not cleared (default-deny) until a documented two-gate check (robots for the actual user-agent + site terms) is run and recorded.
- **ICSID:** targeted fetches of public case and profile pages, with ICSID's attribution line on outputs; arbitrator-profile data is self-reported (ICSID's own disclaimer) and labeled as such.
- **UNCTAD:** the Excel is your own download, used locally and never redistributed; case pages are fetched individually by id, never walked.
- **`assets/icsid-cvid-map.json`** is a list of URLs identifying ICSID's public profile pages, rebuilt from a user-saved copy of the public listing page — sharing URLs, not site content.
- **Work product:** profiles and shortlists are dispute-related work papers; every deliverable carries an attorney-work-product header, and where files are stored or shared is counsel's privilege call.

## License

Copyright (C) 2026 Cameron Russell (ccrnyc). Licensed under the **GNU Affero General Public License v3.0** (`AGPL-3.0-only`) — see [LICENSE](LICENSE). This program comes with ABSOLUTELY NO WARRANTY. The license covers the skill's code and documentation only; retrieved documents and the UNCTAD dataset remain governed by their own sources' terms (see Compliance notes).
