# CIPO Canadian Trademarks Database — Query Syntax Cheat Sheet

## Endpoints

- **Search:** https://ised-isde.canada.ca/cipo/trademarks-search/
- **Trademarks Examination Manual:** https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en/trademarks/trademarks-examination-manual
- **Madrid System reference (CIPO designation):** https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en/trademarks/madrid-system-international-trademark-registration

## Search philosophy in Canada

CIPO does **not** mechanically silo by Nice class the way USPTO examiners do. Confusion is examined across the register without strict class limitation, although class still informs the nature-of-wares analysis under s. 6(5)(c). When running a knockout, do not skip cross-class hits.

The current UI supports:

- Trademark text field (with implicit phonetic scoring)
- Owner / applicant / agent fields
- Application / registration number
- Status (Active / Inactive / All)
- Goods and services keyword
- Nice class
- Vienna code (for design marks — see below)
- Disclaimer / claim type filters

## Recommended query bundles per knockout

```
1. EXACT — all status:
   Trademark = "MARKNAME"
   Status = All

2. PHONETIC / starts-with:
   Trademark = MARKNAME (no quotes; CIPO applies phonetic scoring)

3. ROOT wildcard:
   Trademark = MARKNAME*
   (catches family marks)

4. OWNER:
   Owner = "Owner Name Inc."

5. GOODS-LED:
   Goods/Services keyword = [primary goods term]
   Nice class = [N]
   (catches descriptive senior users in same field)
```

## Vienna codes (design marks)

Canada uses the **Vienna Classification** for figurative elements, not USPTO design codes. Common categories:

- 1.x — Celestial bodies
- 2.x — Human beings
- 3.x — Animals
- 5.x — Plants
- 26.x — Geometric figures
- 27.x — Forms of writing (numerals, letters)

If the mark has design elements, run the Vienna search separately from the wordmark search and combine results in the conflict matrix.

## Per-record extraction

For each potentially conflicting Canadian mark, capture:

1. Status (Registered, Pending, Allowed, Abandoned, Expunged)
2. Owner — and current owner via assignment if changed
3. Filing date and registration date
4. Date of first use in Canada (if claimed)
5. Goods/services (full Nice-class recitation, post-2019 amendments)
6. Disclaimers
7. Section 9 official mark status (s. 9(1)(n) — federal/provincial bodies, universities, public authorities — these have outsized blocking power and should be flagged immediately)
8. Examination correspondence (if available) — confusion objections cited against the mark are gold

## Special Canadian considerations to surface in the memo

- **Official marks under s. 9** — public authorities can register "official marks" that block all later confusing marks regardless of class. If a s. 9 mark surfaces, escalate immediately.
- **s. 22 depreciation of goodwill** — famous marks in Canada have a parallel cause of action (Veuve Clicquot Ponsardin v Boutiques Cliquot Ltée, 2006 SCC 23) even without confusion, if the senior mark is famous and use of the junior mark would depreciate goodwill.
- **s. 7(b) passing off** — common-law / unregistered rights are protected. Common-law searches are not optional in Canada; reputation in a geographic area gives priority.
- **CUSMA / NAFTA legacy filings** — pre-2019 Canadian applications that did not require Nice classification may have very broad goods/services. Read the recitation literally, not by class label.
- **Quebec language considerations** — French-language presence and Charter of the French Language (Bill 96) implications if the client plans to do business in Quebec. Not a registrability issue per se, but worth noting in the recommendations section.
