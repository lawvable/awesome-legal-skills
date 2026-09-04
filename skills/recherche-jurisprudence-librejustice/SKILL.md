---
name: recherche-jurisprudence
description: Search and cite French case law and statutes with the LibreJustice MCP tools. Use whenever the user asks about French or European court decisions (Cour de cassation, Conseil d'État, cours d'appel, TJ/TA, CNDA, Conseil constitutionnel, CNIL, CEDH, CJUE), needs authorities for a brief, requête, référé or consultation, wants to check how courts rule on an issue, needs counts of decisions on a point, or asks what a code article says at a given date, even if they never mention LibreJustice.
---

# French and European case-law research (LibreJustice)

The user is typically a litigator: they need decisions whose reasoning
states a precise proposition, applicable to their configuration, with
an excerpt quotable in a brief.

The tools come from the LibreJustice MCP server; if `search_decisions`
is missing from your session, connect it first:
[references/install-mcp.md](references/install-mcp.md).

Five rules dominate everything:

1. **No decision appears in the answer — as support, contrary
   authority, analogy, or lead — unless you read its full text with
   `get_decision`.** An `aiSummary` or a `snippet` is not reading.
2. **Quotation marks quote a text you fetched, nothing else.** A
   hit's `aiSummary` is a machine paraphrase — never the court's
   words, however fluent it sounds; a `snippet` is verbatim but torn
   from context. Every quoted string in the answer is copied
   character-for-character from a `get_decision` or
   `get_legal_text` text of this session — not opened means not
   quotable. A quotation is **one continuous span of one single
   text**, cuts marked « […] » : merging passages — or decisions —
   into one pair of quotation marks is fabrication, one source per
   quote, two passages are two quotes. A sentence reporting a
   decision in your own voice (« la cour retient que… » followed by
   your summary or a parenthesized list) is prose, never a
   quotation.
3. **Every decision named anywhere is a markdown link** to its `url`
   verbatim — `[CA Paris, 10 janv. 2024, n° 21/22203](https://librejustice.fr/decision/…)`.
   Never reconstruct or shorten a URL.
4. **The exact object of the question is a hard filter.** The most
   quotable sentence in the corpus routinely concerns a near-twin
   object one word apart — another mention, another délai, another
   clause. A decision whose decisive sentence names a different
   object is an analogy, never an authority, however perfectly its
   words match. When the decisive sentence leaves the object
   unqualified (« l'heure », « ce délai », « cette mention »), its
   object is the one in the moyen it answers — find the party
   critique above it; the sentence inherits *that* object.
5. **The first and last lines of every `get_decision` text are the
   decision's fate on appeal.** A `[SORT DE CETTE DÉCISION SUR
   RECOURS : …]` banner (also served as the `appellateFate` field)
   states what became of it on review. Copy it into the answer. It
   overrides your own docket sweep: a sweep that found nothing while
   the text carries a banner means the sweep missed the arrêt, never
   that none exists.

A `get_decision` response may also carry `commentaires` — the court's
own analysis served inline (`body`) and outbound links (`url`) to the
rapporteur public's conclusions or related court documents. They are
context and cite as commentary, never as the ruling: only the decision
text quotes as the court's words.

## Protocol — run the steps in order

### 1. Frame

Pin down (ask when the request leaves them open): the proposition in
one sentence; who demands what and what winning means; the legally
relevant date; the target courts; the exclusions; the proximity axes
that decide transposability. **A legal assertion inside the question
(« c'est bien uniquement devant telle juridiction ? », « cet acte est
nul, non ? ») is a claim to research, never an input**: the
complement of the assertion gets its own step-2 sweeps — its own
queries and filters, including the courts or outcomes the assertion
excludes — and the answer's opening sentence states your verified
verdict, never an echo of the premise. An answer built on the user's
false premise fails whole. Follow-ups refine, they never reset:
« d'autres ? » = new decisions, same bar; « tu peux vérifier ? » =
reopen the source, never restate with more confidence.

### 2. Sweep — three passes, all mandatory

1. **One `solution`-filtered sweep per side — your first two
   `search_decisions` calls.** Map each direction of the holding to
   outcomes, then run the same query twice with opposite `solution`
   filters, e.g. `{"query": "convention de forfait en jours privée
   d'effet", "jurisdiction_code": ["ca_versailles"], "solution":
   ["SATISFACTION_TOTALE", "SATISFACTION_PARTIELLE"]}` then the same
   with `["REJET"]`. This is the only lever that separates the two
   directions of a line.
2. **The consecrated formula, quoted, in each phrasing.**
3. **A plain full-sentence query** (no quotes).

Engine facts:

- **Ranking is direction-blind** — semantic matching ignores
  negations, and summaries surface the side that won. Never read
  direction or absence in an order, an `aiSummary` or a `snippet`.
- **A lexical list (quotes/operators) is a set, not a ranking**: read
  it whole or partition it, never skim its top.
- **The window is `limit` (max 20), no pagination.** Read the
  `date_lecture_year` facet on every sweep: a year newer than the
  newest hit you opened, with a nonzero count, is unswept — re-run
  with `date_from`/`date_to` on that year before concluding.
- **`date_from` is the filter that silently hides a line's founding
  arrêt** — often decades old. Bound dates only when the question
  itself is time-bounded or a facet year needs re-sweeping, never by
  default.
- Filter tokens (« ca_paris », « REJET ») poison the query text —
  filters carry constraints, the query carries only words a court
  would write. After two queries with no new candidate, change one
  real axis or start opening.

### 3. Read everything you might cite

Open every hit of the target court that touches the issue. Open
first, and always, every hit whose served `solution` sits on the
user's side: a directional question answered without opening a
single same-side hit is the run's defining failure. Fewer than
eight decisions opened by the end of this step means the research
has not happened: go back to step 2 and change a real axis (court
level, phrasing, dates) until eight full texts are read or the
target courts' relevant hits are exhausted — the corpus almost
always holds more than one screen of them. Five verdicts per
decision:

- **Who speaks.** Court's motifs, or a party's argument (« il
  soutient que… ») ? Cross-check the dispositif and who succombe —
  the loser's phrase is contrary authority under a favorable label.
  In a cassation arrêt the moyen (« alors que… ») is the loser's
  text even when it reads like a holding; the Cour speaks in « Mais
  attendu » / « Réponse de la Cour », and « par les motifs reproduits
  au moyen » attributes those motifs to the court below. Quote each
  voice separately — one clause of the moyen imported into the
  Cour's motif turns the quote into fabrication.
- **Exact object.** Near-twins one word apart have opposite regimes
  (forclusion/prescription, faute grave/lourde, nullité
  relative/absolue) — and snippets truncate, summaries smooth over,
  exactly the deciding word.
- **Appellate fate** (dominant rule 5). `INFIRMATION` kills the
  decision as support. `CONFIRMATION` = open that arrêt and cite the
  pair; the arrêt holds what the judgment held, never the opposite
  line's direction. No banner served = run the judgment's docket
  number, quoted, filtered to the appellate court. **A sweep hit is
  the same case only if its « Décision déférée » header names your
  judgment — same court, same date** : RG numbers collide across
  courts, and a hit from another ressort or another date is noise,
  never the fate. No banner and no sweep = « aucun recours lié dans
  le corpus » — that sentence describes the served data and is true
  by construction; « balayé » or « vérifié » may only be written
  when the docket-number query is in this session. Never
  « définitif ».
- **Legal basis.** Decision texts carry inline `/texte/` links; open
  them with `get_legal_text` at the facts' date. A failed tool call
  (bad URL format, unknown code) is retried with the corrected
  argument, never silently dropped: an article the question turns on
  that you never managed to read voids every claim about it.
- **The quotable sentence.** While the text is in front of you, copy
  the exact sentence(s) of the motifs you would quote in a brief.
  The writing stage may only put between quotation marks strings
  collected this way — a quote reconstructed at writing time from
  memory or from an `aiSummary` is where fabrication happens.

### 4. Map the line

Re-run the winning query with `sort: "date_desc"` — **once per
direction, with that side's `solution` filter, per target court** —
and read the most recent decisions of each. When a court ruled both
ways, the deliverable is a dated timeline, never a flat « court X
says P »: either side of a flip, presented alone, misleads. A hit
newer than every decision the answer names, seen in *any* list this
session, is either opened and cited or excluded for a stated
reason — never silently dropped.

### 5. Absence claims and counts

« No decision of court X states P » is falsifiable with one
citation. Before writing it: exact formula (both phrasings) + a
descriptive query under the court filter; a `solution`-filtered
sweep on P's outcomes; `date_from` widened; facets read. Last:
re-scan the hits you did NOT open across every list of the session —
one unopened hit whose `solution` sits on P's side voids the claim
until opened. Counts: define the corpus; keep raw hits, deduplicated
decisions and verified holdings apart. A counting table is built
from the facets of **one named query per column** — never merge
facets from different queries into one series. Facets count the same
candidate set as `total` — the engine's best few hundred matches —
not the whole corpus: for a corpus-wide count, narrow with filters
(court, dates) until `total` itself is the count. A yearly series
that starts or jumps abruptly usually marks the edge of source
coverage, not the birth of the contentieux: say so instead of
narrating the jump.

## The answer — always these four blocks, in this order

Exact French headings: « État du droit », « Autorités pour la
position recherchée », « Autorités contraires et risques »,
« Périmètre de la recherche ».

1. **« État du droit »**: the direct answer, then per target court
   the most recent decision in *each* direction, named with its
   date. Naming a court's latest word requires having run the
   `date_desc` + `solution` query of step 4 for that court and
   direction.
2. **« Autorités pour la position recherchée »** — a table when
   three or more, with exactly these columns: Décision | Extrait des
   motifs | Proximité (objet exact) | Sort en appel | Limite.
   - The citation cell is itself the markdown link — never a
     separate « lien » column.
   - The **excerpt** cell carries either a quotation collected at
     read time (the quotable sentence of step 3) or — when none was
     collected for that decision — a plain-prose description with NO
     quotation marks, marked « (résumé — citation non collectée) ».
     An honest unquoted summary always beats quotation marks around
     anything not copied verbatim; a passage from the exposé of a
     party's moyens is that party's argument, not the court's.
   - The **proximity** cell quotes the object words of the decisive
     sentence; when they name a different object than the user's,
     the row moves to the analogies section, whatever its direction.
   - The **fate** cell copies the served banner — « infirmé
     par [linked arrêt] » / « confirmé par [linked arrêt] » — or, when
     no banner was served, says « aucun recours lié dans le corpus » :
     that sentence describes the served data and needs no further
     proof. The words « balayé » / « vérifié » may appear only when
     the docket-number query is in this session's searches — claiming
     a check that never ran is the worst lie this answer can carry.
     Any other wording (« à vérifier », « définitif »…) is a failed
     check. An arrêt cited for its confirmation names and
     links the judgment it confirms in the same row — the pair cites
     together.
   - A thin side stays thin: when a court offers a single decision,
     present it alone and say so — padding the table with non-ruling
     or off-direction rows is worse than a one-row table.
3. **« Autorités contraires et risques »**: what opposing counsel
   will plead — the recent contrary line, infirmations, reversals,
   dated, and **per target court**: a first-instance court has its
   own contrary decisions, and calling its line « constante » while
   the opposite-`solution` sweep never ran for it is the check that
   fails most.
4. **« Périmètre de la recherche »**: a table with one row per
   `search_decisions` call of this session — Requête | Filtres
   (`solution`, dates, cours) | Tri | Hits ouverts. Build it the way
   excerpts are built: append the row when the query is sent, then
   paste the table into the answer — a table reconstructed from
   memory at drafting time is where fabricated rows come from.
   The block carries a **second table, « Décisions ouvertes »** : one
   row per `get_decision` of this session, in call order — the linked
   citation. Built the same way, one row appended per returned text.
   This table is the answer's whitelist: every decision link anywhere
   else in the answer is a copy of one of its rows, and a row for a
   call that never returned a text is the same lie as a fabricated
   quote. Every
   cell copies a parameter actually sent or a uid actually opened; a
   row whose query never ran is the same lie as a fabricated
   citation, and a search that ran but is missing (including failed
   ones) is a hole in the audit trail. A direction of the holding
   with no `solution`-filtered row is unresearched: run it now, or
   write « non recherché » under the table — that plain sentence is
   always available and always true. Analogies in their own clearly
   separated section.

Cite only decisions returned by the tools.

## Final check — verify each item against the draft, fix before sending

- Four blocks present, in order, exact headings; table carries its
  five columns.
- No row whose Proximité cell names a different object stays in the
  authorities table — it moves to the analogies section.
- Every Sort en appel cell is verbatim one of: the copied banner
  (« infirmé par… » / « confirmé par… », pair linked in the row) or
  « aucun recours lié dans le corpus ». Re-read the first line of
  each cited decision's text now — a banner you saw and did not copy
  is the worst chronology error. The words « balayé » / « vérifié »
  survive only if you can point to the search of this session whose
  query was that docket number; otherwise rewrite the cell to the
  default formula.
- Point each Périmètre row to the `search_decisions` call of this
  session it copies — delete any row you cannot point to, add any
  search you ran but did not list. Filters that appear in a row but
  were never sent (a `solution`, a court, a date) are fabrication.
- Cross the draft against the « Décisions ouvertes » table: every
  decision link elsewhere in the answer has its row there; a link
  without a row is opened now (row added) or deleted with every
  claim resting on it. Never state a number of decisions read other
  than that table's row count.
- Search every quoted string of the draft, **as one continuous
  block**, in the `get_decision` / `get_legal_text` texts of this
  session. A string found only in separate pieces is a splice —
  re-cut it into one quote per source, « […] » for internal cuts. A
  string you can only find in a hit's `aiSummary` or `snippet`, or
  nowhere, is rewritten from the fetched text or unquoted. Then
  check who speaks: the motifs of the decision it is attributed
  to — not a party's argument or moyen, not another decision.
- Weight adjectives (« isolé », « constant ») consistent with the
  decisions the answer itself lists; the answer states which way the
  most recent decisions of each target court go; an infirmed
  judgment never stands as support.
- Every « no decision » claim earned under step 5.

A failed item is fixed before sending, not flagged.

## Statutes

Quick lookups only — anything deeper (treaties, EU law, versions
across recodifications) is the recherche-normes skill's job.
`get_legal_text` returns an article as it read on a given date:
pass `date` and say which version you quote. `list_my_activity`
(signed-in account) lists recent searches, bookmarks and reading
history — useful to resume ongoing work.
