# Arbitrator-profile table — output template

**Header on every deliverable (profile, comparison sheet, annex Sources sheet):**
`Attorney work product — prepared at counsel's direction for arbitrator selection` (+ ` in [matter]` when the user has named one). Storage/sharing of the run folder is counsel's privilege call — say so in the run log.

Reference specimen: `references/example-profile.md` (trimmed worked example). Reproduce its structure exactly.

## Section order (one md table: Section | Content | Source)

1. **Identity** — name (canonical + aliases seen in sources); nationality [ICSID profile, self-reported]; gender [public self-description; else "not publicly stated"]; languages; affiliation; CV & profile links (CV link first, with visible fetch-blocked note where applicable).
2. **Appointments**\* — ONE unified section merging the Excel and the live ICSID lookup; never split "snapshot" vs "post-snapshot" into separate sections. Rows: total known (Excel count + post-2023 cases listed with *italicized* names + case nos.); by appointing side; by rules; pending; annulment committees. Mixed-source rows cite "both sources\*".
3. **Dissents and separate writings**\*\* — count over the dissentable-decision denominator; list each opinion: *case*, kind, decision + date, [languages] where multi-version.
4. **Issue exposure**† — per issue: "appointed in N, dissented in D".
5. **Experience mix** — sectors, treaties, respondents, investor home states, co-panelists, presidents sat under.
6. **Publications** — issue-relevant titles with links; visible CV-fetch note; content-review offer.
7. **Flags for counsel** (research signals, not findings) — appointing-side asymmetry, repeat appointments (→ IBA Guidelines check by counsel), pairings, then the record-check items as scoped offers.
8. **Source conflicts** (standing row) — every value where sources disagree, both values shown with source names; "none found this run" when empty. Standing caveat in the row: ICSID profiles record appointments HELD, not final tribunal composition — a systematic conflict source against UNCTAD's "(replaced)" markers; never call two partially-overlapping lists "consistent".
9. **Panel designation status** (standing row) — current ICSID Panel of Arbitrators designation from the live profile where retrieved (a lapsed designation is the same class of live signal as an availability check); "not checked this run" is permitted ONLY where no profile fetch occurred — if the profile page was retrieved this run, read the designation from it.

## Wording rules

- **No builder jargon in deliverables or chat:** never "Tier 1", "Tier 2", "Mode 1/2", "engine", "rung", "Seats". Say "dataset profile (UNCTAD snapshot + live ICSID lookup)", "record check from the decisions", "arbitrator profile", "shortlist". A profile's subtitle line is e.g. "Arbitrator profile — prepared with the isds-arbitrators skill", never "Mode 1 profile". **Final step before delivery: scan every user-facing file for the banned terms**; builder notes go to the run log.
- **Availability wording:** death/retirement/unavailability only with a named, dated source; the sourced negative is "no notice found at [sources, dates] — not confirmation; confirm directly"; otherwise "availability-unverified".
- "Appointments" / "appointed in N, dissented in D" — never "seats"/"sat".
- Name sources in full: "UNCTAD 2023 Excel records 1", not "Excel records 1".
- Names: use the dataset's own form; never expand an initial to a full given name without profile-level verification from a named source.
- *Italicize case names.*
- No editorializing parentheticals in section headers; the substance goes to a footnote.
- Conflicting values: show both, name both sources, flag the conflict in the row.

## Footnotes (all assumptions/provisos at the END, keyed in order of first appearance: \*, \*\*, †, ‡)

- Retrieved-extract spec: whenever a live profile page is relied on, save the extract with provenance header AND the role/appointing-party labels for every entry used — case numbers alone leave role claims unpreserved. Name each artefact "retrieved - <source> - <subject> <YYYY-MM-DD>.md". **Values in the extract are the page's own text, not a summariser's rendering; where an extraction layer and the page disagree, record the page text and note the conflict.** The spec covers **every primary document a deliverable value rests on, non-ICSID included**: archive it into `retrieved/` with route + date — a fetch logged only in the transcript is not an archived source.
- \* Data freshness: Excel snapshot vs live Navigator vs retrieval date; live layer is ICSID-only, self-reported, and a FLOOR rather than a case list (measured coverage gaps; profile silence is weak evidence of inactivity — combined totals are "at least", never exhaustive); post-2023 UNCITRAL/PCA/SCC invisible — assert nothing; non-treaty/annulment-phase profile cases disclosed but excluded from counts.
- \*\* Dissent counting: named-author published opinions only; silence ≠ proven unanimity; denominator = cases with ≥1 substantive decision (award or decision on jurisdiction/merits-liability/quantum-damages; consent awards, orders, bifurcation, rectification, revision, discontinuances excluded). The snapshot can also UNDERCOUNT separate writings — post-snapshot opinions exist (e.g. a 2024 Declaration on Costs); a record check may add to the count, never only confirm it.
- † Outcomes are tribunal-level, not individual votes; to review individual positions, ask to "check the record" on the topic.
- ‡ Scope: treaty-based ISDS only; commercial appointments and confidential cases invisible; not exhaustive; Jus Mundi/GAR ART for fuller analytics; not legal advice.
- Escape literal markers after bold text (`**Appointments**\*`) so markdown renders them.

## Notes-to-users — make them VISIBLE, and SCOPE every trigger

Every record-check offer and every action the user must take (e.g. CV download-then-upload) is set on the pattern:
`▸ **Want X? Say "check the record on <topic>."**` — the trigger names its topic: "on dissents", "on annulment committees", "on her votes", "on challenges", "on double-hatting", "on counsel patterns", "on publications", "on newer cases", "on intra-EU jurisdiction", "on pending status". Never a bare "check the record".
`▸ **CV auto-fetch is blocked … download and upload it here, or let Claude in Chrome open it.**`

## Companions per profile

Case-list annex (`--annex`, xlsx with Sources sheet) and a PER-SESSION run log named `_run-log <subject> <YYYY-MM-DD>.md` (queries, fetches with dates, weights used, caveats) — never a shared `_run-log.md`, never a force-write past a changed-on-disk rejection. Everything saved to the run folder (`YYYY-MM-DD Arbitrator Search/` by default; the user's own run-naming wins — ask when in doubt). Raw engine dumps and other intermediates go to a `working/` subfolder — only header-carrying deliverables at the run-folder root. One folder per research question is fine; logs are per session.

## Case-list annex columns (fixed spec)

`Case name | Case number | Year initiated | Appointed by | Role | Rules | Case status (tribunal-level) | Substantive decisions | Separate opinions | italaw case page`

- The Sources sheet carries the work-product header as its first row (engine-emitted); add the matter name when one is given.

- "Year initiated" = the year the CASE was initiated (filed) per UNCTAD — NOT the appointment year, which the dataset does not record and which can be later.
- "Appointed by" / "Role" are split from UNCTAD's single label: wing members carry the appointing side (role "Co-arbitrator"); presidents and sole arbitrators show "Not recorded in dataset" unless the ICSID profile or case page supplies the appointing party (parties / Chairman / Secretary-General).
- "Separate opinions" (never "My opinion(s)") lists published individual opinions by this arbitrator in the case; silence is not proof of unanimity.

## Annex formatting (xlsx)

The engine emits this formatting; sheets built by hand (e.g. a comparison sheet, or an annex assembled without the engine) must match it. Cases sheet: bold header row on a light fill, frozen at the top, AutoFilter on; alternating (banded) row shading; fixed column widths with text wrapping on the long columns (every column wide enough that its header label fits on one line — header text never wraps); *case names italicized*; the italaw column written as clickable hyperlinks, never bare URL text. Sources sheet: work-product header row in bold; one wide, wrapped column.

## Comparison sheet (selection runs)

Same wording/footnote rules; one row per candidate × key metrics; ranking weights printed above the table; gender balance line; every finalist links to their profile table.
