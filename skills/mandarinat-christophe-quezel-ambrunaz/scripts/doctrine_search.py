#!/usr/bin/env python3
"""
doctrine_search.py — Recherche doctrinale multi-sources avec identifiants vérifiables.

Interroge en parallèle plusieurs bases ouvertes pour la doctrine juridique et
retourne, pour chaque référence, un identifiant vérifiable (DOI, identifiant HAL,
URL OpenAlex/Isidore). Cet identifiant est destiné à alimenter la colonne 2 du
tableau de vérification pré-livraison : une référence doctrinale sans identifiant
vérifiable est traitée comme « référence non vérifiée ».

Sources interrogées (toutes sans authentification) :
  - HAL          (api.archives-ouvertes.fr)       — archive ouverte FR, domaine droit
  - OpenAlex     (api.openalex.org)                — graphe bibliographique mondial, DOI
  - Crossref     (api.crossref.org)                — registre DOI, résolution/dédoublonnage
  - Isidore      (api.isidore.science)             — moteur SHS francophone (CNRS/Huma-Num)

Usage :
    python3 scripts/doctrine_search.py --query "responsabilité du fait des choses" [options]
    python3 scripts/doctrine_search.py --query "perte de chance" --sources hal,openalex
    python3 scripts/doctrine_search.py --doi "10.1234/abcd"      # résolution Crossref directe

Options :
    --query / -q     Termes de recherche (obligatoire sauf --doi)
    --doi            Résout un DOI précis via Crossref (ignore --query)
    --sources        Liste de sources séparées par des virgules
                     (défaut : hal,openalex,isidore ; crossref sert à la résolution)
    --rows / -n      Nombre de résultats par source (défaut 10)
    --year-from      Borne temporelle basse
    --year-to        Borne temporelle haute
    --raw            Sortie brute non dédoublonnée (debug)

Sortie : JSON structuré sur stdout.
  {
    "query": "...",
    "sources_queried": [...],
    "sources_failed": [...],          # sources injoignables, signalées et non bloquantes
    "count": N,
    "references": [
      {
        "title": "...",
        "authors": ["..."],
        "year": 2021,
        "container": "RTD civ.",       # revue / éditeur / collection
        "doc_type": "ART|OUV|COUV|THESE|...",
        "doi": "10.xxxx/...",          # null si absent
        "verifiable_id": {              # CE QUI ALIMENTE LA COLONNE 2 DU TABLEAU
          "kind": "doi|hal|openalex|isidore",
          "value": "...",
          "url": "https://..."
        },
        "open_access_url": "...",       # null si absent
        "sources": ["hal", "openalex"]  # bases où la référence a été vue (post-dédoublonnage)
      }
    ]
  }

Anti-hallucination : ce script NE FABRIQUE PAS de références. Il rapporte ce que
les API retournent. Une source injoignable est signalée dans "sources_failed" et
n'interrompt pas les autres. Aucune référence n'est complétée ou « devinée ».
"""

import argparse
import json
import re
import sys
import unicodedata
import urllib.parse
import urllib.request
import urllib.error

TIMEOUT = 20
UA = "doctrine_search.py (assistant juridique académique ; recherche doctrine ouverte)"

HAL_BASE = "https://api.archives-ouvertes.fr/search/"
HAL_DOMAIN = "1.shs.droit"
HAL_DOCTYPES = "(ART OR OUV OR COUV OR COMM OR DOUV OR THESE OR HDR)"
HAL_FIELDS = (
    "halId_s,title_s,authFullName_s,producedDateY_i,journalTitle_s,uri_s,"
    "docType_s,doiId_s,citationFull_s,fileMain_s"
)
OPENALEX_BASE = "https://api.openalex.org/works"
CROSSREF_BASE = "https://api.crossref.org/works"
ISIDORE_BASE = "https://api.isidore.science/resource/search"

DEFAULT_SOURCES = ["hal", "openalex", "isidore"]


def _get(url, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def _norm_title(title):
    """Clé de dédoublonnage : minuscules, sans accents ni ponctuation, espaces compactés."""
    if not title:
        return ""
    if not isinstance(title, str):
        title = str(title)
    t = unicodedata.normalize("NFKD", title)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()
    return t


def _norm_doi(doi):
    if not doi:
        return None
    doi = doi.strip().lower()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi)
    return doi or None


# --------------------------------------------------------------------------- #
# HAL
# --------------------------------------------------------------------------- #
def search_hal(query, rows, year_from, year_to):
    terms = query
    q = f"(title_t:({terms}) OR abstract_t:({terms}) OR keyword_t:({terms}))"
    params = {
        "q": q,
        "fq": [f"domain_s:{HAL_DOMAIN}", f"docType_s:{HAL_DOCTYPES}"],
        "fl": HAL_FIELDS,
        "rows": str(rows),
        "sort": "producedDate_tdate desc",
        "wt": "json",
    }
    if year_from or year_to:
        lo = year_from or "*"
        hi = year_to or "*"
        params["fq"].append(f"producedDateY_i:[{lo} TO {hi}]")
    url = HAL_BASE + "?" + urllib.parse.urlencode(params, doseq=True)
    data = _get(url)
    out = []
    for d in data.get("response", {}).get("docs", []):
        doi = _norm_doi(d.get("doiId_s"))
        hal_id = d.get("halId_s")
        out.append({
            "title": d.get("title_s", [None])[0] if isinstance(d.get("title_s"), list) else d.get("title_s"),
            "authors": d.get("authFullName_s", []),
            "year": d.get("producedDateY_i"),
            "container": d.get("journalTitle_s"),
            "doc_type": d.get("docType_s"),
            "doi": doi,
            "verifiable_id": {
                "kind": "doi" if doi else "hal",
                "value": doi or hal_id,
                "url": (f"https://doi.org/{doi}" if doi else d.get("uri_s")),
            },
            "open_access_url": d.get("fileMain_s"),
            "sources": ["hal"],
        })
    return out


# --------------------------------------------------------------------------- #
# OpenAlex
# --------------------------------------------------------------------------- #
def search_openalex(query, rows, year_from, year_to):
    filters = ["type:article|book|book-chapter|dissertation"]
    if year_from:
        filters.append(f"from_publication_date:{year_from}-01-01")
    if year_to:
        filters.append(f"to_publication_date:{year_to}-12-31")
    params = {
        "search": query,
        "per-page": str(rows),
        "filter": ",".join(filters),
    }
    url = OPENALEX_BASE + "?" + urllib.parse.urlencode(params)
    data = _get(url)
    out = []
    for w in data.get("results", []):
        doi = _norm_doi(w.get("doi"))
        oa_id = w.get("id")
        authors = [
            a.get("author", {}).get("display_name")
            for a in w.get("authorships", [])
            if a.get("author", {}).get("display_name")
        ]
        loc = (w.get("primary_location") or {})
        container = (loc.get("source") or {}).get("display_name")
        oa_pdf = (w.get("open_access") or {}).get("oa_url")
        out.append({
            "title": w.get("title"),
            "authors": authors,
            "year": w.get("publication_year"),
            "container": container,
            "doc_type": w.get("type"),
            "doi": doi,
            "verifiable_id": {
                "kind": "doi" if doi else "openalex",
                "value": doi or oa_id,
                "url": (f"https://doi.org/{doi}" if doi else oa_id),
            },
            "open_access_url": oa_pdf,
            "sources": ["openalex"],
        })
    return out


# --------------------------------------------------------------------------- #
# Isidore (SHS francophone)
# --------------------------------------------------------------------------- #
def search_isidore(query, rows, year_from, year_to):
    # API REST publique d'Isidore — réponse JSON (structure imbriquée propre à Isidore).
    params = {
        "q": query,
        "output": "json",
        "replies": str(rows),
    }
    url = ISIDORE_BASE + "?" + urllib.parse.urlencode(params)
    data = _get(url)
    out = []
    replies = (
        data.get("response", {})
        .get("replies", {})
        .get("content", {})
        .get("reply", [])
    )
    if isinstance(replies, dict):
        replies = [replies]

    def _pick_text(node):
        """Isidore renvoie souvent des champs multilingues [{'$': '...'}] ; on extrait une chaîne."""
        if node is None:
            return None
        if isinstance(node, str):
            return node
        if isinstance(node, dict):
            return node.get("$") or node.get("text") or node.get("value")
        if isinstance(node, list):
            for item in node:
                txt = _pick_text(item)
                if txt:
                    return txt
        return None

    for r in replies:
        if not isinstance(r, dict):
            continue
        meta = r.get("isidore", {})
        uri = r.get("@uri")
        handle_url = meta.get("url")
        title = _pick_text(meta.get("title"))
        # Auteurs
        authors = []
        creators = meta.get("enrichedCreators", {}).get("creator")
        if isinstance(creators, dict):
            creators = [creators]
        for c in (creators or []):
            if isinstance(c, dict):
                name = c.get("@normalizedAuthor") or " ".join(
                    filter(None, [c.get("firstname"), c.get("lastname")])
                )
                if name:
                    authors.append(name)
        # Année
        date = meta.get("date", {})
        year = None
        if isinstance(date, dict):
            y = date.get("year") or date.get("normalizedDate")
            m = re.search(r"\d{4}", str(y or ""))
            year = int(m.group()) if m else None
        # Type et conteneur
        doc_type = None
        types = meta.get("types", {})
        if isinstance(types, dict):
            doc_type = _pick_text(types.get("type"))
        container = None
        source = meta.get("source", {})
        if isinstance(source, dict):
            container = _pick_text(source.get("name"))

        if year_from and year and year < year_from:
            continue
        if year_to and year and year > year_to:
            continue
        # Identifiant vérifiable : le handle Isidore (10670/...) résout via https://hdl.handle.net/
        verif_url = handle_url or (f"https://hdl.handle.net/{uri}" if uri else None)
        out.append({
            "title": title,
            "authors": authors,
            "year": year,
            "container": container,
            "doc_type": doc_type,
            "doi": None,
            "verifiable_id": {
                "kind": "isidore",
                "value": uri,
                "url": verif_url,
            },
            "open_access_url": handle_url,
            "sources": ["isidore"],
        })
    return out


# --------------------------------------------------------------------------- #
# Crossref — résolution / enrichissement DOI
# --------------------------------------------------------------------------- #
def resolve_crossref(doi):
    url = f"{CROSSREF_BASE}/{urllib.parse.quote(doi)}"
    data = _get(url)
    msg = data.get("message", {})
    authors = [
        " ".join(filter(None, [a.get("given"), a.get("family")]))
        for a in msg.get("author", [])
    ]
    year = None
    for k in ("published-print", "published-online", "issued"):
        parts = (msg.get(k) or {}).get("date-parts")
        if parts and parts[0]:
            year = parts[0][0]
            break
    title = msg.get("title", [None])
    title = title[0] if isinstance(title, list) and title else title
    container = msg.get("container-title", [None])
    container = container[0] if isinstance(container, list) and container else container
    return {
        "title": title,
        "authors": authors,
        "year": year,
        "container": container,
        "doc_type": msg.get("type"),
        "doi": _norm_doi(doi),
        "verifiable_id": {
            "kind": "doi",
            "value": _norm_doi(doi),
            "url": f"https://doi.org/{_norm_doi(doi)}",
        },
        "open_access_url": None,
        "sources": ["crossref"],
    }


# --------------------------------------------------------------------------- #
# Dédoublonnage
# --------------------------------------------------------------------------- #
def dedupe(refs):
    """Fusionne par DOI (priorité), puis par titre normalisé."""
    by_doi = {}
    by_title = {}
    order = []
    for r in refs:
        doi = r.get("doi")
        key = None
        if doi and doi in by_doi:
            key = ("doi", doi)
        elif doi:
            by_doi[doi] = r
            key = ("doi", doi)
            order.append(key)
            continue
        else:
            nt = _norm_title(r.get("title"))
            if nt and nt in by_title:
                key = ("title", nt)
            elif nt:
                by_title[nt] = r
                key = ("title", nt)
                order.append(key)
                continue
            else:
                order.append(("raw", id(r)))
                by_title[("raw", id(r))] = r
                continue
        # Fusion : on enrichit la référence déjà vue
        store = by_doi if key[0] == "doi" else by_title
        existing = store[key[1]]
        for s in r.get("sources", []):
            if s not in existing["sources"]:
                existing["sources"].append(s)
        # Compléter les champs manquants sans écraser
        for f in ("doi", "container", "year", "open_access_url", "doc_type"):
            if not existing.get(f) and r.get(f):
                existing[f] = r[f]
        if not existing.get("authors") and r.get("authors"):
            existing["authors"] = r["authors"]
        # Préférer un identifiant DOI si l'un des doublons en porte un
        if (existing["verifiable_id"]["kind"] != "doi") and r["verifiable_id"]["kind"] == "doi":
            existing["verifiable_id"] = r["verifiable_id"]
    result = []
    seen = set()
    for key in order:
        store = by_doi if key[0] == "doi" else by_title
        ref = store.get(key[1])
        if ref is not None and id(ref) not in seen:
            result.append(ref)
            seen.add(id(ref))
    return result


def main():
    parser = argparse.ArgumentParser(description="Recherche doctrinale multi-sources.")
    parser.add_argument("--query", "-q", help="Termes de recherche")
    parser.add_argument("--doi", help="Résout un DOI précis via Crossref (ignore --query)")
    parser.add_argument("--sources", default=",".join(DEFAULT_SOURCES),
                        help="Sources : hal,openalex,isidore (crossref = résolution)")
    parser.add_argument("--rows", "-n", type=int, default=10, help="Résultats par source")
    parser.add_argument("--year-from", type=int)
    parser.add_argument("--year-to", type=int)
    parser.add_argument("--raw", action="store_true", help="Sortie non dédoublonnée")
    args = parser.parse_args()

    if args.doi:
        try:
            ref = resolve_crossref(args.doi)
            print(json.dumps({"doi": args.doi, "references": [ref], "count": 1},
                            ensure_ascii=False, indent=2))
        except Exception as e:
            print(json.dumps({"doi": args.doi, "error": str(e), "references": []},
                            ensure_ascii=False, indent=2))
            sys.exit(1)
        return

    if not args.query:
        parser.error("--query est requis (ou utiliser --doi)")

    requested = [s.strip().lower() for s in args.sources.split(",") if s.strip()]
    dispatch = {
        "hal": search_hal,
        "openalex": search_openalex,
        "isidore": search_isidore,
    }

    all_refs = []
    queried, failed = [], []
    for src in requested:
        fn = dispatch.get(src)
        if not fn:
            failed.append({"source": src, "error": "source inconnue"})
            continue
        try:
            refs = fn(args.query, args.rows, args.year_from, args.year_to)
            all_refs.extend(refs)
            queried.append(src)
        except urllib.error.URLError as e:
            failed.append({"source": src, "error": f"injoignable : {e}"})
        except Exception as e:  # noqa: BLE001 — on signale toute panne sans bloquer
            failed.append({"source": src, "error": str(e)})

    # Enrichissement DOI optionnel via Crossref si DOI présent mais métadonnées pauvres
    refs = all_refs if args.raw else dedupe(all_refs)

    out = {
        "query": args.query,
        "sources_queried": queried,
        "sources_failed": failed,
        "count": len(refs),
        "references": refs,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
