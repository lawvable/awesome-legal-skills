# Research Routing

Use this reference whenever an assessment requires external research. Select sources by the
question they can answer, not by brand familiarity.

## Capability census

Inspect the current tool descriptions before asking the user about access. Check every
inventory layer the host exposes: immediately visible tools, tool-search results, and deferred,
lazy-loaded, plugin, app, or connector registries. A connector absent from the first layer is
not necessarily unavailable. If tool search is available, search separately for:

- primary law, citator, quotation verification, and case-status tools;
- law-review, working-paper, scholarly-index, and library tools;
- peer-reviewed empirical research and data tools;
- legislation, regulation, government-record, and multi-jurisdiction tools; and
- user-authorized libraries or document stores.

Do not call unrelated tools merely to inventory them. Choose the first tool based on its
description, make the first necessary read-only research call, and treat authentication or
permission failure as unavailability. Follow tool-specific prerequisites, including a
required fetch, full-record retrieval, or opinion-analysis call.

When the user names a source or connector, also search by that product name and attempt it
before substituting. A user-named source wins when it is available; use it for the lane it can
answer and supplement it with more authoritative sources where necessary. If it cannot be
used, state whether it was absent, disconnected, unauthorized, or failed on invocation.

Examples are nonexclusive:

| Research lane | Suitable capabilities | Public fallback |
| --- | --- | --- |
| Primary law | Legal search, citator, case-status, statutes and regulations | Official courts, legislatures, agencies, and trusted public repositories |
| Legal preemption | Legal scholarship, library indexes, working papers, user library | SSRN, law-review sites, institutional repositories, scholarly web search |
| Empirical warrant | Peer-reviewed paper search, data repositories, discipline-specific indexes | Primary studies, official datasets, university repositories |
| Comparative or foreign law | Multi-jurisdiction legal search and official gazettes | Courts, legislatures, ministries, and treaty organizations |
| User corpus | Zotero or authorized document-storage and retrieval tools | Files supplied in the conversation |

Use an academic-paper connector such as Consensus, OpenAlex, Semantic Scholar, or an equivalent
for empirical or interdisciplinary premises and as a supplementary preemption search for a
publication-grade legal thesis. These indexes can surface legal-academic work, including older
articles that ordinary web results miss. Fetch or open the full record when the connector
requires that step before citation. Do not treat an index's failure to find a paper as proof
that no legal scholarship exists, and do not use it to verify holdings. Use legal-research
connectors such as Midpage, CourtListener, Descrybe, or equivalents when available for the
functions their descriptions support; product names are examples, not hard dependencies.

## Source hierarchy

Prefer sources in this order when they answer the same question:

1. controlling primary authority or original data;
2. full text of the scholarship being classified;
3. authoritative treatises, systematic reviews, and institutional sources;
4. credible commentary that identifies or explains primary material; and
5. snippets or aggregations only as leads, never as final support.

Verify quotations against the full source. For cases, verify the proposition, court,
jurisdiction, date, precedential status, and adverse treatment when material. For empirical
claims, identify the study design, population, measure, uncertainty, and whether later work
confirms or undermines the result.

## Preemption search

Search at least these formulations when applicable:

- the thesis in the user's language;
- synonyms for the doctrinal or theoretical labels;
- the mechanism or method without the desired conclusion;
- the proposed remedy, payoff, or institutional actor;
- the strongest contrary thesis; and
- known leading authors, cases, statutes, and foundational works.

Search forthcoming and working-paper sources. A new technology or factual setting does not
create claim novelty if the analytical move is old.

For each serious candidate source, record:

| Source | Thesis | Mechanism or method | Evidence | Scope | Payoff | Material difference |
| --- | --- | --- | --- | --- | --- | --- |

Classify the source only after examining enough full text to support the classification.

## Fallback and user questions

If a connector is missing, unavailable, or unauthorized, continue with suitable public
sources. Ask the user about access only when:

- a proprietary collection is likely to contain decisive material not otherwise searchable;
- the user specifically requested that collection or connector; or
- the user's private library or unpublished work is necessary to answer the question.

State what access would change. Do not stall an otherwise useful provisional assessment.

Decide the research ladder once per lane:

1. use a source or connector the user expressly named, if functioning;
2. otherwise use a suitable connected capability discovered in the host;
3. otherwise use authoritative public sources and ordinary web search; and
4. otherwise proceed without that lane only if a useful provisional assessment remains
   possible, lower confidence, and disclose the omission.

## Research record

Include:

- search date and any cutoff date;
- jurisdiction and field;
- tools, databases, websites, and user corpora actually used;
- representative queries and terminology variants;
- important sources read in full;
- inaccessible collections and failed or unauthorized tools;
- unresolved adverse authority, empirical uncertainty, or likely preemption; and
- the next highest-value searches.

Calibrate confidence to coverage. Distinguish “no preemption located” from “the claim is
novel,” and distinguish absence of evidence from evidence of absence.
