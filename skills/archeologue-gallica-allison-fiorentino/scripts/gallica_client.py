#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Client Gallica (BNF) — archéologie des sources juridiques anciennes.

APIs utilisées (publiques, sans clé, stables) :
  - SRU            recherche dans le catalogue et le plein texte océrisé
  - Issues         calendrier des fascicules d'un périodique (ark de titre cb…)
  - ContentSearch  recherche plein texte DANS un document (pages + extraits)
  - RequestDigitalElement (ALTO)  texte océrisé d'une page précise
  - OAIRecord      notice bibliographique d'un document
  - Pagination     structure (nb de vues, numéros de page imprimés)

IMPORTANT : Gallica renvoie 403 aux user-agents de robots ; toutes les
requêtes portent un User-Agent de navigateur. Erreurs DNS transitoires du
proxy : chaque requête est retentée 3 fois avec pause croissante.

Deux familles d'identifiants ark :
  cb…   ark de TITRE de périodique (ex. cb328020951 = JO Débats Chambre) ;
        s'utilise avec annees / fascicules / feuilleter.
  bpt…  ark de DOCUMENT (un fascicule, un livre) ;
        s'utilise avec chercher / texte / notice / pages.

Commandes :
  recherche "mots"        Recherche générale (plein texte océrisé par défaut).
                          --champ texte|titre|auteur|sujet|tout  --exact
                          --de AAAA --a AAAA  --type monographie|fascicule|periodique
                          --max N (déf. 10)  --page N  --tri date|pertinence
  periodique "titre"      Trouver l'ark de titre (cb…) d'un périodique.
  annees <cb…>            Années de fascicules disponibles.
  fascicules <cb…> <AAAA> Fascicules d'une année (ark bpt… + date).
  feuilleter <cb…> "mots" Quels fascicules de CE périodique mentionnent ces
                          mots — le cœur du skill. --de AAAA --a AAAA --max N
  chercher <bpt…> "mots"  Pages du document contenant ces mots, avec extraits.
  texte <bpt…> --vue N    Texte océrisé de la vue N (ou --vue N-M, max 20 vues).
  pages <bpt…>            Correspondance vue ↔ numéro de page imprimé.
  notice <bpt…>           Notice bibliographique complète.

Sortie : JSON sur stdout. En cas d'échec : {"error": ..., "fix": ...}.
Chaque document renvoyé inclut ses URL de consultation et d'image (IIIF).
"""

import argparse
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request

BASE = "https://gallica.bnf.fr"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}


def die(msg, fix=None):
    out = {"error": msg}
    if fix:
        out["fix"] = fix
    print(json.dumps(out, ensure_ascii=False, indent=2))
    sys.exit(1)


def emit(obj):
    print(json.dumps(obj, ensure_ascii=False, indent=2))


def http_get(url, timeout=60):
    last = None
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:
            last = e
            time.sleep(2 * (attempt + 1))
    msg = str(last)
    if "403" in msg:
        die("Gallica a refusé la requête (403).",
            "Réessayer dans quelques minutes ; vérifier que l'URL est bien "
            "formée. Le User-Agent navigateur est déjà envoyé.")
    if "resolution" in msg.lower() or "dns" in msg.lower() or "denied" in msg.lower():
        die("Réseau inaccessible : " + msg,
            "Vérifier que gallica.bnf.fr figure dans Paramètres > Capacités > "
            "Domaines autorisés, puis relancer (les erreurs DNS du proxy sont "
            "souvent transitoires).")
    die("Échec après 4 tentatives : " + msg, "Relancer la commande.")


def clean(txt):
    """Décoder les entités HTML/XML imbriquées et normaliser les espaces."""
    if txt is None:
        return ""
    for _ in range(3):
        new = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), txt)
        new = (new.replace("&amp;", "&").replace("&lt;", "<")
                  .replace("&gt;", ">").replace("&apos;", "'")
                  .replace("&quot;", '"'))
        if new == txt:
            break
        txt = new
    txt = re.sub(r"<span class='highlight'>|</span>", "**", txt)
    txt = re.sub(r"<[^>]+>", " ", txt)
    return re.sub(r"\s+", " ", txt).strip()


def doc_urls(ark, vue=None):
    u = {"consulter": "%s/ark:/12148/%s" % (BASE, ark)}
    if vue:
        u["consulter"] += "/f%d.item" % vue
        u["image"] = "%s/iiif/ark:/12148/%s/f%d/full/1500,/0/native.jpg" % (BASE, ark, vue)
    return u


# ---------------------------------------------------------------- SRU ----

CHAMPS = {
    "texte": "gallica all",        # plein texte océrisé + métadonnées
    "titre": "dc.title all",
    "auteur": "dc.creator all",
    "sujet": "dc.subject all",
    "tout": "gallica all",
}

TYPES = {
    "monographie": "monographie",
    "fascicule": "fascicule",
    "periodique": "publication en série imprimée",
    "manuscrit": "manuscrit",
    "image": "image",
}


def sru_query(query, maximum=10, start=1, collapsing=None, tri=None):
    params = {
        "operation": "searchRetrieve",
        "version": "1.2",
        "query": query,
        "maximumRecords": str(maximum),
        "startRecord": str(start),
    }
    if collapsing is not None:
        params["collapsing"] = "true" if collapsing else "false"
    url = BASE + "/SRU?" + urllib.parse.urlencode(params)
    xml = http_get(url).decode("utf-8", "replace")
    total_m = re.search(r"<srw:numberOfRecords>(\d+)</srw:numberOfRecords>", xml)
    total = int(total_m.group(1)) if total_m else 0
    records = []
    for rec in re.split(r"<srw:record>", xml)[1:]:
        def all_of(tag):
            return [clean(v) for v in re.findall(r"<dc:%s>(.*?)</dc:%s>" % (tag, tag), rec, re.S)]
        idents = all_of("identifier")
        ark = None
        for i in idents:
            m = re.search(r"ark:/12148/([a-z0-9]+)", i)
            if m:
                ark = m.group(1)
                break
        r = {
            "ark": ark,
            "titre": (all_of("title") or [""])[0],
            "auteur": ", ".join(all_of("creator"))[:200] or None,
            "date": (all_of("date") or [None])[0],
            "type": next((t for t in all_of("type")
                          if t in ("monographie imprimée", "fascicule",
                                   "publication en série imprimée",
                                   "manuscrit", "image", "carte")), None),
            "droits": next((d for d in all_of("rights")
                            if "domaine" in d or "restricted" in d or "use" in d), None),
        }
        if ark:
            r["url"] = doc_urls(ark)["consulter"]
        records.append(r)
    return total, records


def cmd_recherche(a):
    parts = []
    terme = '"%s"' % a.mots if (a.exact or " " in a.mots) else a.mots
    parts.append("%s %s" % (CHAMPS[a.champ], terme))
    if a.type:
        parts.append('dc.type all "%s"' % TYPES[a.type])
    if a.de:
        parts.append('gallicapublication_date>="%s/01/01"' % a.de)
    if a.a:
        parts.append('gallicapublication_date<="%s/12/31"' % a.a)
    q = " and ".join(parts)
    if a.tri == "date":
        q += " sortby dc.date/sort.ascending"
    total, records = sru_query(q, maximum=a.max, start=1 + (a.page - 1) * a.max)
    emit({"requete_cql": q, "total": total, "page": a.page,
          "resultats": records,
          "note": "total = documents (les fascicules d'un même périodique sont "
                  "regroupés ; utiliser feuilleter pour les détailler)."})


def cmd_periodique(a):
    q = 'dc.title all "%s" and dc.type all "publication en série imprimée"' % a.titre
    total, _ = sru_query(q, maximum=1)
    if total == 0:
        q = 'dc.title all "%s"' % a.titre
    xml_total, records = sru_query(q, maximum=8)
    out = []
    seen = set()
    for r in records:
        ark = r.get("ark") or ""
        if ark.startswith("cb") and ark not in seen:
            seen.add(ark)
            out.append({"ark_titre": ark, "titre": r["titre"],
                        "periode_cataloguee": r.get("date"),
                        "url": "%s/ark:/12148/%s/date" % (BASE, ark)})
    if not out:
        die("Aucun périodique trouvé pour « %s »." % a.titre,
            "Essayer un titre plus court, ou consulter "
            "references/periodiques.md pour le catalogue déjà résolu.")
    emit({"periodiques": out,
          "suite": "annees <ark_titre> pour les années réellement numérisées."})


# ------------------------------------------------------------- Issues ----

def cmd_annees(a):
    ark = a.ark.replace("/date", "")
    xml = http_get("%s/services/Issues?ark=ark:/12148/%s/date" % (BASE, ark)).decode("utf-8", "replace")
    years = re.findall(r"<year>(\d{4})</year>", xml)
    tot = re.search(r'totalIssues="(\d+)"', xml)
    if not years:
        die("Aucune année trouvée pour %s." % ark,
            "Vérifier qu'il s'agit bien d'un ark de titre (cb…) et que le "
            "périodique est numérisé (commande periodique).")
    emit({"ark_titre": ark, "fascicules_total": int(tot.group(1)) if tot else None,
          "premiere_annee": years[0], "derniere_annee": years[-1],
          "annees": years})


def cmd_fascicules(a):
    ark = a.ark.replace("/date", "")
    xml = http_get("%s/services/Issues?ark=ark:/12148/%s/date&date=%s"
                   % (BASE, ark, a.annee), timeout=90).decode("utf-8", "replace")
    issues = [{"ark": m.group(1), "date": clean(m.group(2)),
               "url": doc_urls(m.group(1))["consulter"]}
              for m in re.finditer(r'<issue ark="([^"]+)"[^>]*>([^<]*)</issue>', xml)]
    if not issues:
        die("Aucun fascicule pour %s en %s." % (ark, a.annee),
            "Lancer d'abord la commande annees pour les années disponibles.")
    emit({"ark_titre": ark, "annee": a.annee, "nb": len(issues),
          "fascicules": issues})


def cmd_feuilleter(a):
    ark = a.ark.replace("/date", "")
    parts = ['arkPress all "%s_date"' % ark,
             'gallica all "%s"' % a.mots]
    if a.de:
        parts.append('gallicapublication_date>="%s/01/01"' % a.de)
    if a.a:
        parts.append('gallicapublication_date<="%s/12/31"' % a.a)
    q = " and ".join(parts) + " sortby dc.date/sort.ascending"
    total, records = sru_query(q, maximum=a.max, collapsing=False)
    hits = [{"ark": r["ark"], "date": r["date"], "url": r.get("url")}
            for r in records if r["ark"]]
    emit({"ark_titre": ark, "expression": a.mots,
          "fascicules_contenant_l_expression": total,
          "affiches": len(hits), "fascicules": hits,
          "suite": "chercher <ark> \"%s\" pour localiser les pages et lire "
                   "les extraits." % a.mots})


# ------------------------------------------------- ContentSearch/ALTO ----

def cmd_chercher(a):
    url = "%s/services/ContentSearch?ark=%s&query=%s" % (
        BASE, a.ark, urllib.parse.quote(a.mots))
    if a.page > 1:
        url += "&startResult=%d" % ((a.page - 1) * 10 + 1)
    xml = http_get(url).decode("utf-8", "replace")
    count = re.search(r'countResults="(\d+)"', xml)
    items = []
    for m in re.finditer(r"<item>(.*?)</item>", xml, re.S):
        blk = m.group(1)
        pid = re.search(r"<p_id>PAG_(\d+)</p_id>", blk)
        content = re.search(r"<content>(.*?)</content>", blk, re.S)
        vue = int(pid.group(1)) if pid else None
        it = {"vue": vue, "extrait": clean(content.group(1)) if content else ""}
        if vue:
            it.update(doc_urls(a.ark, vue))
        items.append(it)
    emit({"ark": a.ark, "expression": a.mots,
          "occurrences_pages": int(count.group(1)) if count else 0,
          "page_de_resultats": a.page, "extraits": items,
          "suite": "texte %s --vue N pour lire la page entière." % a.ark})


def alto_page(ark, vue):
    raw = http_get("%s/RequestDigitalElement?O=%s&E=ALTO&Deb=%d"
                   % (BASE, ark, vue))
    # L'en-tête annonce ISO-8859-1 mais le contenu est en UTF-8.
    xml = raw.decode("utf-8", "replace")
    words, line = [], []
    for m in re.finditer(r"<(String|SP|TextLine)\b[^>]*>", xml):
        tag = m.group(1)
        if tag == "String":
            c = re.search(r'CONTENT="([^"]*)"', m.group(0))
            if c:
                line.append(clean(c.group(1)))
        elif tag == "TextLine" and line:
            words.append(" ".join(line))
            line = []
    if line:
        words.append(" ".join(line))
    return "\n".join(words)


def cmd_texte(a):
    m = re.match(r"^(\d+)(?:-(\d+))?$", a.vue)
    if not m:
        die("--vue attend un numéro (12) ou un intervalle (12-15).")
    v1 = int(m.group(1))
    v2 = int(m.group(2)) if m.group(2) else v1
    if v2 - v1 + 1 > 20:
        die("Maximum 20 vues par appel.", "Découper l'intervalle.")
    pages = []
    for v in range(v1, v2 + 1):
        pages.append({"vue": v, "texte": alto_page(a.ark, v),
                      **doc_urls(a.ark, v)})
    emit({"ark": a.ark, "pages": pages,
          "avertissement": "Texte océrisé brut : coquilles OCR possibles, "
          "vérifier sur l'image avant toute citation."})


def cmd_pages(a):
    xml = http_get("%s/services/Pagination?ark=%s" % (BASE, a.ark)).decode("utf-8", "replace")
    nb = re.search(r"<nbVueImages>(\d+)</nbVueImages>", xml)
    corres = [{"vue": int(m.group(2)), "page_imprimee": m.group(1)}
              for m in re.finditer(r"<numero>([^<]*)</numero>\s*<ordre>(\d+)</ordre>", xml)]
    emit({"ark": a.ark, "nb_vues": int(nb.group(1)) if nb else None,
          "correspondance": corres[:400]})


def cmd_notice(a):
    xml = http_get("%s/services/OAIRecord?ark=%s" % (BASE, a.ark)).decode("utf-8", "replace")
    fields = {}
    for tag in ("title", "creator", "date", "publisher", "description",
                "subject", "type", "rights", "source", "relation", "language"):
        vals = [clean(v) for v in re.findall(r"<dc:%s>(.*?)</dc:%s>" % (tag, tag), xml, re.S)]
        if vals:
            fields[tag] = vals if len(vals) > 1 else vals[0]
    if not fields:
        die("Notice introuvable pour %s." % a.ark)
    fields["url"] = doc_urls(a.ark)["consulter"]
    emit(fields)


# --------------------------------------------------------------- main ----

def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("recherche")
    s.add_argument("mots")
    s.add_argument("--champ", choices=CHAMPS, default="texte")
    s.add_argument("--exact", action="store_true")
    s.add_argument("--type", choices=TYPES, default=None)
    s.add_argument("--de", type=int, default=None)
    s.add_argument("--a", type=int, default=None)
    s.add_argument("--max", type=int, default=10)
    s.add_argument("--page", type=int, default=1)
    s.add_argument("--tri", choices=("pertinence", "date"), default="pertinence")
    s.set_defaults(f=cmd_recherche)

    s = sub.add_parser("periodique")
    s.add_argument("titre")
    s.set_defaults(f=cmd_periodique)

    s = sub.add_parser("annees")
    s.add_argument("ark")
    s.set_defaults(f=cmd_annees)

    s = sub.add_parser("fascicules")
    s.add_argument("ark")
    s.add_argument("annee")
    s.set_defaults(f=cmd_fascicules)

    s = sub.add_parser("feuilleter")
    s.add_argument("ark")
    s.add_argument("mots")
    s.add_argument("--de", type=int, default=None)
    s.add_argument("--a", type=int, default=None)
    s.add_argument("--max", type=int, default=15)
    s.set_defaults(f=cmd_feuilleter)

    s = sub.add_parser("chercher")
    s.add_argument("ark")
    s.add_argument("mots")
    s.add_argument("--page", type=int, default=1)
    s.set_defaults(f=cmd_chercher)

    s = sub.add_parser("texte")
    s.add_argument("ark")
    s.add_argument("--vue", required=True)
    s.set_defaults(f=cmd_texte)

    s = sub.add_parser("pages")
    s.add_argument("ark")
    s.set_defaults(f=cmd_pages)

    s = sub.add_parser("notice")
    s.add_argument("ark")
    s.set_defaults(f=cmd_notice)

    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
