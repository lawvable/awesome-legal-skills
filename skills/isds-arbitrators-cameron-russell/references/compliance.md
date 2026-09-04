# Per-source compliance rules (two-gate test: robots for the actual user-agent + site Terms; Terms bind regardless of robots)

| Source | Status | Rules |
|---|---|---|
| UNCTAD Excel | user's own download | local only, NEVER ships or redistributes; personal non-commercial per UNCTAD terms |
| UNCTAD case pages (`/cases/{id}/x`) | cleared | server-rendered by id; ids are non-sequential — never guess or increment; no bulk walking |
| UNCTAD Navigator search UI | JS-only | user-initiated Chrome rendering only; no scripted pagination/harvest |
| ICSID case pages + icsidfiles PDFs | cleared | targeted, user-initiated; ICSID attribution: "Source: The International Centre for Settlement of Investment Disputes. Available at https://icsid.worldbank.org." |
| ICSID arbitrator DB — per-person `profile?cvid=N` | cleared 2026-08-02 | server-rendered; targeted per-candidate fetches only; data is self-reported (ICSID's own disclaimer) — label it; never bulk-harvest profiles or build a content database from them |
| ICSID arbitrator DB — listing page | JS-only | user's browser (Chrome) or user-saved PDF; `parse_icsid_cvids.py` rebuilds the name→cvid map from a user save. The shipped map is a list of URLs identifying public profile pages — sharing URLs is not redistribution of site content |
| PCA case pages | cleared | non-commercial, targeted; honor case-specific confidentiality notes |
| italaw | links only | Terms §4.2 bars automated access; the user downloads manually (single, human-confirmed, per-document); never fetched by the tool |
| CV hosts (chambers, SIAC, IAI, universities) | typically block fetchers | link + tell the user visibly: download-then-upload, or Claude in Chrome live with the user's permission |
| Jus Mundi, GAR ART, Arbitrator Intelligence, ISLG | excluded | never accessed; every output refers users there for fuller analytics (capability honesty) |
| **Any other host** — incl. "mirrors" of decisions | **NOT cleared (default-deny)** | absence from this table means NOT cleared, never "unregulated"; before any fetch, run the two-gate test, NAME the host, and record both results in the run log — without that record, links only, and nothing from the host may ground a table value |

Global: no scraping-and-hosting of corpora; outputs are the user's own work product + links, never proxied documents; "Retrieved from: URL" + date on every retrieved item; not-legal-advice disclaimer on every deliverable.
