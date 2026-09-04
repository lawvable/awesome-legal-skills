---
name: recherche-normes
description: Find and quote statutory and regulatory law with the LibreJustice MCP tools — French codes at any date, EU law, treaties and bilateral accords, foreign codes (59 countries), collective agreements, BOFiP, circulaires. Use whenever the user asks what a text says or said at a given date, which version or which text applies to a situation, needs the exact wording of a provision for a brief, or works with foreign or international law in French litigation, even if they never mention LibreJustice.
---

# Statutory research (LibreJustice)

The user is typically a litigator: they need the exact provision, in
the version in force at the legally relevant date, linked and quoted
verbatim. A paraphrase from memory is not a deliverable — models
misremember article numbers and miss amendments; every quoted
provision comes from `get_legal_text`.

The referential goes far beyond French codes: EU law, international
treaties (including bilateral accords), the codes of 59 foreign
countries, collective agreements, BOFiP. Map and counts:
[references/corpus.md](references/corpus.md). Observed failure modes:
[references/traps.md](references/traps.md). Foreign and international
law: [references/foreign-law.md](references/foreign-law.md).

The tools come from the LibreJustice MCP server; if `get_legal_text`
is missing from your session, connect it first:
[references/install-mcp.md](references/install-mcp.md).

## Iron rules

1. **Never quote a provision from memory.** Fetch it with
   `get_legal_text`, quote verbatim, link the article
   (`[Article 7 bis de l'Accord franco-algérien du 27 décembre
   1968](https://librejustice.fr/texte/…)` — the `url` verbatim).
2. **Date before text.** Identify the legally relevant date first —
   the attacked decision, the facts, the contract — pass it as
   `date`, and say which version you quote (its validity window is in
   the response). The version in force today is the wrong one for
   most litigation.
3. **Name texts by their official name.** The `code` filter resolves
   slugs and exact official names, not usual names — « CEDH » and
   « Convention européenne des droits de l'homme » fail where
   « Convention de sauvegarde des droits de l'homme et des libertés
   fondamentales » works. When unsure, recover the slug from
   `facets.code` or from an inline `/texte/` link in a decision.

A `get_legal_text` response may also carry `commentaires` — doctrine
anchored on the article, served inline (`body`) or as outbound links
(`url`). Context, never the norm: only the article text quotes as the
provision.

## Three access paths, cheapest first

1. **Text and article known** — compose the URL directly:
   `https://librejustice.fr/texte/{code-slug}/{article-key}`
   (`code-civil`/`47`, `code-de-la-famille-sen`/`40`,
   `accord-franco-algerien-du-27-decembre-1968`/`7-bis`; keys are
   lowercase, `l761-1` for L. 761-1). A wrong slug errors back with
   the closest ones — guessing then correcting is one call, a search
   is two.
2. **Text known, article unknown** — `search_legal_texts` with the
   `code` filter (slug or exact name) and a descriptive French query
   on the subject. Within one named text, ranking is reliable.
3. **Text unknown** — descriptive query plus the `jurisdiction`
   filter (`FR`, `UE`, `INTL`, or an ISO country code `SN`, `DZ`,
   `BE`…), then read `facets.code` to see which texts concentrate the
   matches and re-query with the winner. Ranking is domestic-first: a
   bare descriptive query ranks French, EU and treaty law above the
   59 foreign corpora, and naming the country in the query (« divorce
   au sénégal ») scopes it to that country's law instead. A query
   that IS a text's name — official or usual (« code civil du
   sénégal ») — returns the text itself as a num-less first hit whose
   `url` is the `/texte/{slug}` entry point: the cheapest way to
   recover a slug. Still **don't trust a bare descriptive search
   beyond its top hits**: the corpus is ~2 million articles dominated
   by circulaires and arrêtés, the `total` is OR-matched noise, and
   body-text sources keep crowding treaty searches — the
   `jurisdiction` and `code` filters remain the robust path.

## Versions, renumbering, silence

- The response carries the full version timeline. When a text was
  recodified or an article renumbered (CESEDA 2021: L. 313-11 →
  L. 423-23; code du travail 2008), **query both numbers** — each key
  has its own timeline and the decisive one depends on your date.
- « Not found » with a `date` means no version in force at that date
  under that key — not that the rule did not exist. Re-fetch without
  `date` to see the timeline, then chase the earlier numbering.
- Abrogated texts stay served: the code de la nationalité française
  or an old CESEDA article at its date is one `date` away.
- Hits may repeat one article once per version — deduplicate by URL.

## Legal orders and hierarchy

State which legal order a provision belongs to, and flag the
hierarchy when orders collide: a bilateral accord is lex specialis
(the accord franco-algérien governs Algerian residence permits and
derogates from the CESEDA), EU law primes national law in its field,
the Convention de sauvegarde primes statute. When the question spans
orders, fetch the provisions on each side — never assume the code
tells the whole story.

## Chain with case law

Both directions, and always both in a dispute:

- Text → decisions: `search_decisions` with `legal_instrument` (any
  slug: a French code, a treaty, a foreign code) or `legal_article`
  (`accord-franco-algerien-du-27-decembre-1968|7-bis`) finds the
  decisions applying the provision — then the recherche-jurisprudence
  skill takes over.
- Decision → texts: decision full texts carry inline `/texte/` links on
  every cited provision; open them with `get_legal_text` rather than
  searching again.

## Present each provision

- The linked citation with the official text name and article number,
  `url` verbatim as the link target.
- Which version: validity dates, and why that version governs the
  case (rule 2).
- The verbatim excerpt — never truncate a sentence in a way that
  drops a condition or a negation.
- For foreign and aggregated sources, the provenance when reliability
  matters: each hit carries a `source` field (official publishers
  like legifrance, eur-lex, fedlex, dri.gouv.sn vs aggregators like
  jafbase or archive.org — see corpus.md).

## Don't waste calls

- Known article → compose the URL, skip the search.
- The version timeline arrives with every fetch — no second call to
  ask « since when ».
- One search with the right filter beats five filterless
  reformulations; after two queries with no new candidate, change the
  filter (code, jurisdiction), not the synonyms.
