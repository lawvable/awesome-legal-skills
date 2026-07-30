# USPTO TESS / TSDR — Query Syntax Cheat Sheet

## Endpoints

- **Search (current UI):** https://tmsearch.uspto.gov/
- **Search (legacy / advanced operators):** https://tmsearch.uspto.gov/search/search-information
- **TSDR (status & file wrapper):** https://tsdr.uspto.gov/#caseNumber=<SERIAL>&caseType=SERIAL_NO&searchType=statusSearch
- **Trademark Manual of Examining Procedure (TMEP):** https://tmep.uspto.gov/
- **ID Manual (acceptable identifications):** https://idm-tmng.uspto.gov/

## Important — current UI vs. legacy syntax

USPTO replaced legacy TESS with a new search interface in late 2023 (`tmsearch.uspto.gov`). The legacy `[BI]`, `[IC]`, `[CC]` field-tag operators **do not reliably parse in the new free-text search box**. They still work in the **Expert Search / Advanced** mode and in many third-party mirrors, and they remain the clearest way to communicate intent. When directing the user, give both forms:

- **New UI (Basic Search):** the user types the term into the free-text box, then uses the form's filter chips for class, status, and owner.
- **New UI (Expert Search):** click "Expert Search" — legacy tag syntax (`marname[BI] AND 009[IC]`) parses normally here.
- **Legacy operators (below):** present these as the canonical query and tell the user to paste into Expert Search, or to translate by hand into the Basic form fields.

| Legacy tag | New-UI Basic field equivalent |
|---|---|
| `[BI]` Basic Index | Free-text search box |
| `[CM]` Combined Mark | Free-text search box (default) |
| `[IC]` International Class | "International Class" filter chip |
| `[GS]` Goods/Services | "Goods and Services" filter |
| `[ON]` Owner | "Owner" filter |
| `[LD]` Live/Dead | "Status" filter (Live / Dead / All) |
| `[CC]` Design Code | "Design Code" filter |
| `[FD]` Filing Date | "Filing Date" date range |
| `[SN]` Serial Number | "Serial Number" filter |

If the user reports zero results after pasting the legacy syntax into the Basic box, redirect them to Expert Search.

## Field tags (legacy syntax, used in Expert Search and as the canonical query form)

| Tag | Field |
|---|---|
| `[CM]` | Combined Mark (default search) |
| `[BI]` | Basic Index — full-text mark |
| `[ON]` | Owner Name |
| `[GS]` | Goods & Services |
| `[IC]` | International Class |
| `[CC]` | Design Code (USPTO) |
| `[LD]` | Live/Dead |
| `[FD]` | Filing Date |
| `[RD]` | Registration Date |
| `[SN]` | Serial Number |
| `[RN]` | Registration Number |

## Operators

- `AND`, `OR`, `NOT`
- `*` — right-truncation wildcard (`alpha*`)
- `?` — single-character wildcard
- `$` — pluralization / family root
- Quotes for exact phrases

## Recommended query bundles per knockout

For a word mark `MARKNAME` in Class N:

```
1. EXACT — all status:
   marname[BI] AND `live`[LD] OR `dead`[LD]

2. EXACT in target class:
   marname[BI] AND N[IC]

3. PHONETIC / typo cluster (build from the SOUNDEX patterns below):
   (marname OR marqname OR markname OR marcname OR markknayme OR
    marknaim OR marknaem)[BI]

4. ROOT / wildcard:
   mark*[BI] AND N[IC]

5. OWNER (if known senior user):
   "Owner Name Inc"[ON]
```

## SOUNDEX-style substitution patterns

When building phonetic alternates, walk these substitutions across the mark:

| Phoneme | Common spellings |
|---|---|
| K-sound | c, k, ck, q, ch, qu |
| S-sound | s, c, ss, sc, ps, z |
| F-sound | f, ph, gh |
| J-sound | j, g (before e/i), dg, dj |
| Long A | a, ai, ay, ei, eigh |
| Long E | e, ee, ea, ie, ei, y |
| Long I | i, y, ie, igh, uy |
| Long O | o, oa, ow, oe, ough |
| Long U | u, oo, ew, ue, oo, ou |
| Schwa | a, e, i, o, u (any unstressed) |
| Silent E | drop / add terminal e |

Doubling and dropping consonants (one R vs two; m vs mm) catches a lot of near-misses.

## Design-code searches (logo / stylized marks)

If the mark has any visual element, design codes are mandatory. The USPTO Design Search Code Manual is at https://tmdesigncodes.uspto.gov/. Common high-traffic categories:

- 01.x — Celestial bodies, natural phenomena
- 02.x — Human beings
- 03.x — Animals
- 05.x — Plants
- 26.x — Geometric figures and solids (very common — circles, squares, triangles, abstract logos)
- 27.x — Forms of writing (stylized letters, monograms)

For a typical "stylized wordmark inside a shape" combine the letter form code with the geometric shape code, e.g. `27.03.01[CC] AND 26.01.21[CC]`.

A design-code knockout is **not** a substitute for a vendor designer search (Corsearch / CompuMark) — flag that limitation.

## TSDR pull — what to extract per conflict

For each potentially conflicting mark, capture from TSDR:

1. Status (Live / Dead, registered / pending / abandoned)
2. Owner (current — check assignment chain)
3. Class(es) and full goods/services recitation
4. Filing basis (1(a) use, 1(b) ITU, 44(d) foreign priority, 44(e) foreign reg, 66(a) Madrid)
5. First-use date and first-use-in-commerce date (if 1(a))
6. Office action history (any §2(d) refusals citing other marks — informs strength)
7. Disclaimers, translations, transliterations
8. Renewal / §8 / §15 status

The file wrapper often reveals whether the mark is contested, has narrow scope from amendments, or has been the subject of a TTAB proceeding.
