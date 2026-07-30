#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
normaliser.py - moteur deterministe de la skill normalisation-juridique-fr.

Applique sur un .docx les corrections DETERMINISTES :
  - typographiques (apostrophes, insecables, guillemets, ordinaux, ligatures...) ;
  - lexicales sures (stipuler->disposer, anglicismes surs, pleonasmes univoques).
Par defaut tout est applique en EDITION DIRECTE (sans suivi des modifications).
Avec --track-lexical, les substitutions lexicales sont posees en revisions Word.
La reversibilite repose sur la RECONSTRUCTION depuis l'original (cf. registre).
"""
import argparse
import copy
import datetime
import json
import os
import re
import zipfile

from lxml import etree

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML = "http://www.w3.org/XML/1998/namespace"

NBSP = "\u00A0"   # espace insecable
NNBSP = "\u202F"  # espace fine insecable
RQUO = "\u2019"   # apostrophe courbe
LAQUO = "\u00AB"
RAQUO = "\u00BB"
EMDASH = "\u2014"


def qn(tag):
    p, l = tag.split(":")
    return "{%s}%s" % (W if p == "w" else XML, l)


def _matches(pattern, text, repl_func):
    out = []
    for m in re.finditer(pattern, text):
        repl = repl_func(m)
        if repl is not None and repl != m.group(0):
            out.append((m.start(), m.end(), repl))
    return out


# ----- regles typographiques -----
def r_apostrophes(text):
    return _matches(r"(?<=\w)'", text, lambda m: RQUO)


def r_suspension(text):
    return _matches(r"\.\.\.+", text, lambda m: "…")


def r_ponctuation_basse(text):
    return _matches(r" +(?=[,.])", text, lambda m: "")


def r_guillemets(text):
    idx = [m.start() for m in re.finditer(r'"', text)]
    if not idx or len(idx) % 2 != 0:
        return []
    out = []
    for k, pos in enumerate(idx):
        if k % 2 == 0:
            out.append((pos, pos + 1, LAQUO + NNBSP))
        else:
            out.append((pos, pos + 1, NNBSP + RAQUO))
    return out


def r_civilites(text):
    return _matches(r"\bMr\b\.?", text, lambda m: "M.")


def r_ordinaux(text):
    out = []
    out += _matches(r"\b1[èe]re\b", text, lambda m: "1re")
    out += _matches(r"\b(\d+)[èe]me\b", text, lambda m: m.group(1) + "e")
    out += _matches(r"\b(\d+)ième\b", text, lambda m: m.group(1) + "e")
    out += _matches(r"\b(\d+)è\b", text, lambda m: m.group(1) + "e")
    return out


OE_WORDS = {
    "oeil": "œil", "oeillet": "œillet", "oeillade": "œillade",
    "oedeme": "œdème", "oedème": "œdème", "oesophage": "œsophage",
    "oesophagien": "œsophagien", "oecumenique": "œcuménique",
    "oecuménique": "œcuménique", "foetus": "fœtus", "foetal": "fœtal",
    "foetale": "fœtale", "oestrogene": "œstrogène", "oestrogène": "œstrogène",
    "oedipien": "œdipien", "oedipe": "Œdipe",
}
OE_RE = re.compile(r"\b(" + "|".join(OE_WORDS) + r")\b", re.IGNORECASE)


def r_ligatures_oe(text):
    out = []
    out += _matches(r"oeu", text, lambda m: "œu")
    out += _matches(r"Oeu", text, lambda m: "Œu")
    out += _matches(r"OEU", text, lambda m: "ŒU")
    for m in OE_RE.finditer(text):
        w = m.group(0)
        repl = OE_WORDS[w.lower()]
        if w[:1].isupper():
            repl = repl[:1].upper() + repl[1:]
        if repl != w:
            out.append((m.start(), m.end(), repl))
    return out


def r_insecables_ponctuation(text):
    out = []
    out += _matches(r" (?=[;?!])", text, lambda m: NNBSP)
    out += _matches(r" (?=:)", text, lambda m: NBSP)
    out += _matches(LAQUO + " ", text, lambda m: LAQUO + NNBSP)
    out += _matches(" " + RAQUO, text, lambda m: NNBSP + RAQUO)
    return out


def r_insecables_references(text):
    out = []
    out += _matches(
        r"(?:\bart\.|\bal\.|\bp\.|\bpp\.|\bvol\.|\bt\.|\bch\.|\bfasc\.|\bcol\.|§|\bL\.|\bR\.|\bD\.) (?=\d)",
        text, lambda m: m.group(0)[:-1] + NBSP)
    out += _matches(r"\bart\. (?=[LRD]\.)", text, lambda m: "art." + NBSP)
    out += _matches(r"n° ?(?=\d)", text, lambda m: "n°" + NBSP)
    out += _matches(r"(?:M\.|Mme|Mmes|Mlle|Me|Mes|Mgr|Dr|Pr) (?=[A-ZÉÈÀÂÎÔÇ])",
                    text, lambda m: m.group(0)[:-1] + NBSP)
    out += _matches(r"(?<=\d) ?(?=[%€])", text, lambda m: NNBSP)
    return out


def r_tirets(text):
    return _matches(r"(?<=\S)\s*" + EMDASH + r"\s*", text, lambda m: NBSP + EMDASH + " ")


def r_espaces_multiples(text):
    return _matches(r" {2,}", text, lambda m: " ")


def r_majuscules_sures(text):
    out = []
    out += _matches(r"\bEtat\b", text, lambda m: "État")
    out += _matches(r"\bEtats\b", text, lambda m: "États")
    return out


TYPO_RULES = [
    ("apostrophes", "Apostrophes droites -> courbes", "typographie", r_apostrophes),
    ("suspension", "Points de suspension (... -> …)", "typographie", r_suspension),
    ("ponctuation_basse", "Espace parasite devant , et .", "typographie", r_ponctuation_basse),
    ("guillemets", "Guillemets francais", "typographie", r_guillemets),
    ("civilites", "Civilite Mr -> M.", "typographie", r_civilites),
    ("ordinaux", "Ordinaux (1ere -> 1re, 2eme -> 2e)", "typographie", r_ordinaux),
    ("ligatures_oe", "Ligatures oe -> œ (manœuvre, œuvre)", "typographie", r_ligatures_oe),
    ("insecables_ponct", "Insecables fines (; : ! ? « »)", "typographie", r_insecables_ponctuation),
    ("insecables_ref", "Insecables des references (art., n°, p., %, M.)", "typographie", r_insecables_references),
    ("tirets", "Espacement des tirets cadratins", "typographie", r_tirets),
    ("espaces_multiples", "Espaces multiples", "typographie", r_espaces_multiples),
    ("majuscules_sures", "Majuscules accentuees (sures)", "typographie", r_majuscules_sures),
]
TYPO_N = {key: i + 1 for i, (key, *_r) in enumerate(TYPO_RULES)}


# ----- regles lexicales sures -----
SUBJECT_RE = re.compile(
    r"\b(loi|lois|article|articles|art\.|décret|règlement|ordonnance|code|"
    r"alinéa|texte|disposition|dispositions)\b", re.IGNORECASE)
STIPULER_RE = re.compile(
    r"\bstipul(?:e|ent|ait|aient|é|ée|és|ées|er)\b", re.IGNORECASE)

ANGLICISMES_SURS = {
    "digital": "numérique", "deadline": "échéance", "feedback": "retour",
    "brainstorming": "remue-méninges", "overview": "vue d" + RQUO + "ensemble",
    "checker": "vérifier", "forwarder": "transmettre", "switcher": "basculer",
    "booker": "réserver", "customiser": "personnaliser", "upgrader": "mettre à niveau",
    "downloader": "télécharger", "uploader": "téléverser", "scheduler": "planifier",
    "dispatcher": "répartir", "briefer": "informer", "sponsoriser": "parrainer",
}
ANGLI_RE = re.compile(r"\b(" + "|".join(re.escape(k) for k in ANGLICISMES_SURS) + r")\b",
                      re.IGNORECASE)


def _preserve_case(old, new):
    return new[:1].upper() + new[1:] if old[:1].isupper() else new


def _stipuler_new(old):
    base = {"stipule": "dispose", "stipulent": "disposent", "stipulait": "disposait",
            "stipulaient": "disposaient", "stipuler": "disposer",
            "stipulé": "disposé", "stipulée": "disposée",
            "stipulés": "disposés", "stipulées": "disposées"}
    return base.get(old.lower(), old.lower().replace("stipul", "dispos"))


def lx_stipuler(text):
    out = []
    for m in STIPULER_RE.finditer(text):
        if SUBJECT_RE.search(text[max(0, m.start() - 60):m.start()]):
            old = m.group(0)
            out.append((m.start(), m.end(), old, _preserve_case(old, _stipuler_new(old))))
    return out


def lx_anglicismes(text):
    out = []
    for m in ANGLI_RE.finditer(text):
        old = m.group(0)
        out.append((m.start(), m.end(), old, _preserve_case(old, ANGLICISMES_SURS[old.lower()])))
    return out


PLEONASMES = [
    (re.compile(r"\bvoire\s+même\b", re.IGNORECASE), "voire"),
    (re.compile(r"\bau jour d['’]aujourd['’]hui\b", re.IGNORECASE), "aujourd’hui"),
    (re.compile(r"\bpallier\s+à\b", re.IGNORECASE), "pallier"),
]


def lx_pleonasmes(text):
    out = []
    for rx, repl in PLEONASMES:
        for m in rx.finditer(text):
            old = m.group(0)
            out.append((m.start(), m.end(), old, _preserve_case(old, repl)))
    return out


LEX_RULES = [
    ("stipuler_disposer", "stipuler -> disposer (texte normatif)", "lexique", lx_stipuler),
    ("anglicismes_surs", "Anglicismes (noyau sur)", "lexique", lx_anglicismes),
    ("pleonasmes", "Pleonasmes univoques (voire même, pallier à)", "lexique", lx_pleonasmes),
]
LEX_N = {key: len(TYPO_RULES) + 1 + i for i, (key, *_r) in enumerate(LEX_RULES)}


def catalog():
    c = {}
    for key, libelle, cat_, _f in TYPO_RULES:
        c[TYPO_N[key]] = (key, libelle, cat_)
    for key, libelle, cat_, _f in LEX_RULES:
        c[LEX_N[key]] = (key, libelle, cat_)
    return c


def _set_text(node, value):
    node.text = value
    if value != value.strip():
        node.set(qn("xml:space"), "preserve")


def _excerpt(s, n=40):
    s = s.replace("\n", " ")
    return (s[: n - 1] + "…") if len(s) > n else s


def _new_run(rpr, text, deleted=False):
    r = etree.Element(qn("w:r"))
    if rpr is not None:
        r.append(copy.deepcopy(rpr))
    t = etree.SubElement(r, qn("w:delText") if deleted else qn("w:t"))
    t.set(qn("xml:space"), "preserve")
    t.text = text
    return r


def _wrap(tag, wid, author, date, child):
    el = etree.Element(qn(tag))
    el.set(qn("w:id"), str(wid))
    el.set(qn("w:author"), author)
    el.set(qn("w:date"), date)
    el.append(child)
    return el


def _in_revision(node):
    p = node.getparent()
    while p is not None:
        if p.tag in (qn("w:ins"), qn("w:del")):
            return True
        p = p.getparent()
    return False


def apply_to_tree(root, ctx):
    # ---- TYPO : edition directe des <w:t> ----
    for key, libelle, cat, func in TYPO_RULES:
        if key in ctx["disabled_rules"]:
            continue
        n = TYPO_N[key]
        for t in root.iter(qn("w:t")):
            if _in_revision(t):
                continue
            txt = t.text or ""
            if not txt:
                continue
            spans = func(txt)
            if not spans:
                continue
            spans.sort(key=lambda s: s[0])
            new, last = [], 0
            for (a, b, repl) in spans:
                ctx["counter"][key] = ctx["counter"].get(key, 0) + 1
                ci = ctx["counter"][key]
                if ("%d.%d" % (n, ci)) in ctx["disabled_occs"]:
                    new.append(txt[last:b])
                    last = b
                    continue
                new.append(txt[last:a])
                new.append(repl)
                last = b
                ctx["record"](n, key, libelle, cat, "determin", "direct",
                              ctx["part"], txt[a:b], repl, _excerpt(txt[max(0, a - 15):b + 5]))
            new.append(txt[last:])
            joined = "".join(new)
            if joined != txt:
                _set_text(t, joined)

    # ---- LEXICAL (deterministe) ----
    if ctx.get("track"):
        _lexical_tracked(root, ctx)
    else:
        _lexical_direct(root, ctx)


def _lexical_direct(root, ctx):
    for key, libelle, cat, func in LEX_RULES:
        if key in ctx["disabled_rules"]:
            continue
        n = LEX_N[key]
        for t in root.iter(qn("w:t")):
            if _in_revision(t):
                continue
            txt = t.text or ""
            if not txt:
                continue
            spans = func(txt)
            if not spans:
                continue
            spans.sort(key=lambda s: s[0])
            out, last = [], 0
            for (a, b, old, new) in spans:
                ctx["counter"][key] = ctx["counter"].get(key, 0) + 1
                ci = ctx["counter"][key]
                if ("%d.%d" % (n, ci)) in ctx["disabled_occs"]:
                    out.append(txt[last:b])
                    last = b
                    continue
                out.append(txt[last:a])
                out.append(new)
                last = b
                ctx["record"](n, key, libelle, cat, "determin", "direct",
                              ctx["part"], old, new, _excerpt(txt[max(0, a - 15):b + 5]))
            out.append(txt[last:])
            joined = "".join(out)
            if joined != txt:
                _set_text(t, joined)


def _lexical_tracked(root, ctx):
    pending = []
    for r in list(root.iter(qn("w:r"))):
        parent = r.getparent()
        if parent is None or parent.tag in (qn("w:ins"), qn("w:del")):
            continue
        tc = r.findall(qn("w:t"))
        if len(tc) != 1:
            continue
        txt = tc[0].text or ""
        if not txt:
            continue
        rpr = r.find(qn("w:rPr"))
        matches = []
        for key, libelle, cat, func in LEX_RULES:
            if key in ctx["disabled_rules"]:
                continue
            for (a, b, old, new) in func(txt):
                matches.append((a, b, old, new, key, libelle, cat))
        if not matches:
            continue
        matches.sort(key=lambda s: s[0])
        filtered, cur = [], -1
        for mm in matches:
            if mm[0] >= cur:
                filtered.append(mm)
                cur = mm[1]
        nodes, last, produced = [], 0, False
        for (a, b, old, new, key, libelle, cat) in filtered:
            n = LEX_N[key]
            ctx["counter"][key] = ctx["counter"].get(key, 0) + 1
            ci = ctx["counter"][key]
            if ("%d.%d" % (n, ci)) in ctx["disabled_occs"]:
                continue
            if txt[last:a]:
                nodes.append(_new_run(rpr, txt[last:a]))
            wd = ctx["next_wid"]()
            wi = ctx["next_wid"]()
            nodes.append(_wrap("w:del", wd, ctx["author"], ctx["date"], _new_run(rpr, old, True)))
            nodes.append(_wrap("w:ins", wi, ctx["author"], ctx["date"], _new_run(rpr, new)))
            ctx["record"](n, key, libelle, cat, "determin", "tracked",
                          ctx["part"], old, new, _excerpt(txt[max(0, a - 15):b + 5]),
                          w_ids=[wd, wi])
            last = b
            produced = True
        if not produced:
            continue
        if txt[last:]:
            nodes.append(_new_run(rpr, txt[last:]))
        pending.append((r, nodes))
    for r, nodes in pending:
        parent = r.getparent()
        i = list(parent).index(r)
        parent.remove(r)
        for off, node in enumerate(nodes):
            parent.insert(i + off, node)


NOTE_PARTS = ["word/footnotes.xml", "word/endnotes.xml"]


def parts_for_scope(names, scope):
    out = ["word/document.xml"]
    if scope in ("all", "body+notes"):
        out += [p for p in NOTE_PARTS if p in names]
    return out


def max_wid(trees):
    mx = 0
    for tr in trees.values():
        for el in tr.iter():
            v = el.get(qn("w:id"))
            if v and v.lstrip("-").isdigit():
                mx = max(mx, int(v))
    return mx


def run_apply(in_path, out_path, registry_path, scope="all",
              disabled_rules=None, disabled_occs=None, author="Claude - normalisation",
              track=False):
    disabled_rules = set(disabled_rules or [])
    disabled_occs = set(disabled_occs or [])
    date = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    with zipfile.ZipFile(in_path) as z:
        entries = {n: z.read(n) for n in z.namelist()}
    target_parts = parts_for_scope(entries, scope)
    parser = etree.XMLParser(remove_blank_text=False)
    trees = {p: etree.fromstring(entries[p], parser) for p in target_parts}
    wid = [max_wid(trees)]
    groupes, editions = {}, []

    def next_wid():
        wid[0] += 1
        return wid[0]

    def record(n, key, libelle, cat, regime, type_edition, part, avant, apres, contexte, w_ids=None):
        g = groupes.get(n)
        if g is None:
            g = {"n": n, "cle": key, "libelle": libelle, "categorie": cat,
                 "regime": regime, "type_edition": type_edition, "actif": True,
                 "occurrences": 0, "exemples": []}
            groupes[n] = g
        g["occurrences"] += 1
        ex = "%s -> %s" % (_excerpt(avant, 22), _excerpt(apres, 22))
        if len(g["exemples"]) < 3 and ex not in g["exemples"]:
            g["exemples"].append(ex)
        editions.append({"n": n, "i": g["occurrences"], "cle": key, "regime": regime,
                         "partie": part.replace("word/", "").replace(".xml", ""),
                         "actif": True, "avant": avant, "apres": apres,
                         "contexte": contexte, "w_ids": w_ids or []})

    for p in target_parts:
        ctx = {"part": p, "disabled_rules": disabled_rules, "disabled_occs": disabled_occs,
               "counter": {}, "record": record, "next_wid": next_wid,
               "author": author, "date": date, "track": track}
        apply_to_tree(trees[p], ctx)
        entries[p] = etree.tostring(trees[p], xml_declaration=True, encoding="UTF-8", standalone=True)

    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in entries.items():
            z.writestr(name, data)

    reg = {"version": "1.0"}
    if os.path.exists(registry_path):
        try:
            reg = json.load(open(registry_path, encoding="utf-8"))
        except Exception:
            reg = {"version": "1.0"}
    jug_g = [g for g in reg.get("groupes", []) if g.get("regime") == "jugement"]
    jug_e = [e for e in reg.get("editions", []) if e.get("regime") == "jugement"]
    reg.update({
        "version": "1.0",
        "document_original": os.path.abspath(in_path),
        "document_corrige": os.path.abspath(out_path),
        "horodatage": date, "auteur_revisions": author, "scope": scope,
        "track_lexical": track,
        "groupes": sorted(groupes.values(), key=lambda g: g["n"]) + jug_g,
        "editions": editions + jug_e,
        "regles_desactivees": sorted(disabled_rules),
        "occurrences_desactivees": sorted(disabled_occs),
    })
    os.makedirs(os.path.dirname(os.path.abspath(registry_path)), exist_ok=True)
    json.dump(reg, open(registry_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return reg


def main():
    ap = argparse.ArgumentParser(description="Normalisation juridique - moteur deterministe")
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("apply")
    a.add_argument("--in", dest="inp", required=True)
    a.add_argument("--out", dest="out", required=True)
    a.add_argument("--registry", required=True)
    a.add_argument("--scope", default="all", choices=["all", "body", "body+notes"])
    a.add_argument("--author", default="Claude - normalisation")
    a.add_argument("--track-lexical", action="store_true",
                   help="poser les substitutions lexicales en revisions (defaut: direct)")
    args = ap.parse_args()
    if args.cmd == "apply":
        reg = run_apply(args.inp, args.out, args.registry, args.scope,
                        author=args.author, track=args.track_lexical)
        ng = len([g for g in reg["groupes"] if g["regime"] == "determin"])
        print("OK : %d groupe(s) deterministe(s), %d modification(s)." % (ng, len(reg["editions"])))
        print("Corrige  : %s" % reg["document_corrige"])
        print("Registre : %s" % os.path.abspath(args.registry))


if __name__ == "__main__":
    main()
