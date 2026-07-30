#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
registre.py - recapitulatif et reversibilite de la skill normalisation-juridique-fr.

Sous-commandes :
  recap        affiche le tableau compact (agrege par regle)
  undo  SPEC   defait des groupes/occurrences : "3, 7-10, 12" ou "7.2" ou "tout"
  redo  SPEC   retablit
  add-jugement enregistre une reecriture de jugement (revision deja posee)
  verify       controle d'idempotence et de coherence

Deterministe : undo/redo reconstruisent le .docx depuis l'original.
Jugement     : undo/redo rejettent/retablissent les revisions par w:id.
"""
import argparse
import json
import os
import re
import sys
import tempfile
import zipfile

from lxml import etree

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import normaliser as N


def load(p):
    return json.load(open(p, encoding="utf-8"))


def save(reg, p):
    json.dump(reg, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def type_label(g):
    return "détermin." if g["regime"] == "determin" else g.get("categorie", "jugement").upper()


def recap(reg):
    rows = [g for g in reg.get("groupes", []) if g.get("actif", True) and g.get("occurrences", 0) > 0]
    rows.sort(key=lambda g: g["n"])
    if not rows:
        return "Aucune modification active."
    headers = ["N°", "Règle", "Type", "Occ.", "Exemple (avant -> après)"]
    data = [[str(g["n"]), g["libelle"], type_label(g), str(g["occurrences"]),
             (g["exemples"][0] if g.get("exemples") else "")] for g in rows]
    widths = [max(len(h), *(len(r[i]) for r in data)) for i, h in enumerate(headers)]

    def line(cells):
        return "| " + " | ".join(c.ljust(widths[i]) for i, c in enumerate(cells)) + " |"

    out = [line(headers), "|" + "|".join("-" * (w + 2) for w in widths) + "|"]
    out += [line(r) for r in data]
    total = sum(g["occurrences"] for g in rows)
    out.append("")
    out.append("Total : %d modification(s) sur %d règle(s)." % (total, len(rows)))
    out.append("Pour revenir en arrière : « défais 3, 7-10, 12 » (groupe) ou "
               "« défais 7.2 » (occurrence) ; « refais ... » pour rétablir.")
    return "\n".join(out)


def parse_spec(spec, reg):
    spec = spec.strip().lower()
    if spec in ("tout", "all", "*"):
        return set(), set(), True
    groups, occs = set(), set()
    for tok in re.split(r"[,\s]+", spec):
        tok = tok.strip()
        if not tok:
            continue
        if re.fullmatch(r"\d+\.\d+", tok):
            occs.add(tok)
        elif re.fullmatch(r"\d+-\d+", tok):
            a, b = map(int, tok.split("-"))
            groups.update(range(min(a, b), max(a, b) + 1))
        elif re.fullmatch(r"\d+", tok):
            groups.add(int(tok))
    return groups, occs, False


def n_to_key(reg):
    return {g["n"]: g["cle"] for g in reg.get("groupes", [])}


def reject_wids(corrige_path, wids):
    wids = set(str(w) for w in wids)
    with zipfile.ZipFile(corrige_path) as z:
        entries = {n: z.read(n) for n in z.namelist()}
    changed = False
    for part in ["word/document.xml", "word/footnotes.xml", "word/endnotes.xml"]:
        if part not in entries:
            continue
        root = etree.fromstring(entries[part])
        for tag in (N.qn("w:ins"), N.qn("w:del")):
            for el in list(root.iter(tag)):
                if el.get(N.qn("w:id")) not in wids:
                    continue
                parent = el.getparent()
                idx = list(parent).index(el)
                if tag == N.qn("w:ins"):
                    parent.remove(el)
                else:
                    for r in el.findall(N.qn("w:r")):
                        for dt in r.findall(N.qn("w:delText")):
                            dt.tag = N.qn("w:t")
                        parent.insert(idx, r)
                        idx += 1
                    parent.remove(el)
                changed = True
        entries[part] = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)
    if changed:
        with zipfile.ZipFile(corrige_path, "w", zipfile.ZIP_DEFLATED) as z:
            for name, data in entries.items():
                z.writestr(name, data)
    return changed


def apply_toggle(reg, reg_path, spec, in_path, out_path, activate):
    groups, occs, tout = parse_spec(spec, reg)
    cat = N.catalog()
    determin_ns = set(cat.keys())
    n2k = {n: cat[n][0] for n in cat}
    for g in reg.get("groupes", []):
        if g["regime"] == "jugement":
            n2k[g["n"]] = g["cle"]
    jug_ns = {g["n"] for g in reg.get("groupes", []) if g["regime"] == "jugement"}
    dis_rules = set(reg.get("regles_desactivees", []))
    dis_occs = set(reg.get("occurrences_desactivees", []))
    touched_jug = False

    if tout:
        groups = determin_ns | jug_ns

    for n in groups:
        if n in determin_ns:
            key = n2k.get(n)
            if activate:
                dis_rules.discard(key)
            else:
                dis_rules.add(key)
            for o in list(dis_occs):
                if o.split(".")[0] == str(n):
                    dis_occs.discard(o)
        elif n in jug_ns:
            for g in reg["groupes"]:
                if g["n"] == n:
                    g["actif"] = activate
            for e in reg["editions"]:
                if e["n"] == n:
                    e["actif"] = activate
            touched_jug = True

    for o in occs:
        n = int(o.split(".")[0])
        if n in determin_ns:
            if activate:
                dis_occs.discard(o)
            else:
                dis_occs.add(o)
        elif n in jug_ns:
            for e in reg["editions"]:
                if "%d.%d" % (e["n"], e["i"]) == o:
                    e["actif"] = activate
                    touched_jug = True

    save(reg, reg_path)
    reg2 = N.run_apply(in_path, out_path, reg_path, scope=reg.get("scope", "all"),
                       disabled_rules=dis_rules, disabled_occs=dis_occs,
                       author=reg.get("auteur_revisions", "Claude - normalisation"),
                       track=reg.get("track_lexical", False))
    if touched_jug:
        inactive = [w for e in reg2.get("editions", [])
                    if e.get("regime") == "jugement" and not e.get("actif", True)
                    for w in e.get("w_ids", [])]
        if inactive:
            reject_wids(out_path, inactive)

    determin_touched = any(n in determin_ns for n in groups) or \
        any(int(o.split(".")[0]) in determin_ns for o in occs)
    active_jug = any(e.get("regime") == "jugement" and e.get("actif", True)
                     for e in reg2.get("editions", []))
    warn = ""
    if determin_touched and active_jug:
        warn = ("\nNote : reconstruction deterministe effectuee ; reposer les "
                "reecritures de jugement actives si elles ont disparu.")
    return reg2, warn


def add_jugement(reg, reg_path, cle, libelle, categorie, avant, apres, wids):
    existing = [g for g in reg.get("groupes", []) if g["regime"] == "jugement" and g["cle"] == cle]
    if existing:
        g = existing[0]
    else:
        nmax = max([gg["n"] for gg in reg.get("groupes", [])] + [8])
        g = {"n": nmax + 1, "cle": cle, "libelle": libelle, "categorie": categorie,
             "regime": "jugement", "type_edition": "tracked", "actif": True,
             "occurrences": 0, "exemples": []}
        reg.setdefault("groupes", []).append(g)
    g["occurrences"] += 1
    ex = "%s -> %s" % (N._excerpt(avant, 22), N._excerpt(apres, 22))
    if len(g["exemples"]) < 3:
        g["exemples"].append(ex)
    reg.setdefault("editions", []).append({
        "n": g["n"], "i": g["occurrences"], "cle": cle, "regime": "jugement",
        "partie": "document", "actif": True, "avant": avant, "apres": apres,
        "contexte": "", "w_ids": [int(w) for w in wids if str(w).strip()]})
    save(reg, reg_path)
    return g["n"], g["occurrences"]


def verify(reg, reg_path):
    corr = reg["document_corrige"]
    tmp_reg = os.path.join(tempfile.gettempdir(), "_normjur_verify.json")
    tmp_doc = os.path.join(tempfile.gettempdir(), "_normjur_verify.docx")
    r2 = N.run_apply(corr, tmp_doc, tmp_reg, scope=reg.get("scope", "all"),
                     track=reg.get("track_lexical", False))
    redo = len([e for e in r2["editions"] if e.get("regime") == "determin"])
    for f in (tmp_reg, tmp_doc):
        try:
            os.remove(f)
        except OSError:
            pass
    msgs = ["Idempotence deterministe : %s (%d modification(s) residuelle(s))."
            % ("OK" if redo == 0 else "A VERIFIER", redo)]
    ng = len([g for g in reg.get("groupes", []) if g.get("occurrences", 0) > 0])
    msgs.append("Coherence : %d groupe(s), %d edition(s) consignee(s)."
                % (ng, len(reg.get("editions", []))))
    return "\n".join(msgs)


def main():
    ap = argparse.ArgumentParser(description="Registre de normalisation")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("recap")
    p.add_argument("--registry", required=True)
    for name in ("undo", "redo"):
        p = sub.add_parser(name)
        p.add_argument("spec")
        p.add_argument("--registry", required=True)
        p.add_argument("--in", dest="inp", required=True, help="document ORIGINAL")
        p.add_argument("--out", dest="out", required=True, help="document corrige (cible)")
    p = sub.add_parser("add-jugement")
    p.add_argument("--registry", required=True)
    p.add_argument("--cle", required=True)
    p.add_argument("--libelle", required=True)
    p.add_argument("--categorie", default="stylistique")
    p.add_argument("--avant", required=True)
    p.add_argument("--apres", required=True)
    p.add_argument("--wids", default="")
    p = sub.add_parser("verify")
    p.add_argument("--registry", required=True)

    args = ap.parse_args()
    reg = load(args.registry)
    if args.cmd == "recap":
        print(recap(reg))
    elif args.cmd in ("undo", "redo"):
        reg2, warn = apply_toggle(reg, args.registry, args.spec, args.inp, args.out,
                                  activate=(args.cmd == "redo"))
        print(recap(reg2))
        if warn:
            print(warn)
    elif args.cmd == "add-jugement":
        n, i = add_jugement(reg, args.registry, args.cle, args.libelle, args.categorie,
                            args.avant, args.apres, args.wids.split(","))
        print("Jugement enregistre : groupe %d, occurrence %d." % (n, i))
    elif args.cmd == "verify":
        print(verify(reg, args.registry))


if __name__ == "__main__":
    main()
