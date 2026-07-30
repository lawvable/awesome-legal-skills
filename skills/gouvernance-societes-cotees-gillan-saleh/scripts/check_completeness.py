#!/usr/bin/env python3
"""
Détecteur de complétude et de cohérence des index — skill gouvernance-emetteurs-cotes
=====================================================================================

Outil de garde-fou. Il NE corrige rien et NE juge rien : il SIGNALE des points à
confronter au PDF source. Un signalement n'est pas une erreur automatique — c'est
une zone où l'index pourrait être incomplet ou incohérent, à vérifier à la source.

Cinq détecteurs indépendants (activables à la carte) :

  D1  series        Sous-point « - **X.Y** : » sans citation à côté d'un voisin de
                    même série qui en a une (motif des « thèmes à venir » HCGE 4.x).
  D2  skeleton      Sous-section #### au corps vide ou squelettique (ni citation,
                    ni référence de page, texte quasi nul) — titre posé sans contenu.
  D3  quotes        Déséquilibre des guillemets « » dans un fichier — signe d'une
                    citation tronquée ou mal fermée à la copie.
  D4  substitute    Renvoi-substitut (« figure p. X », « disponible sur demande »…)
                    là où la donnée elle-même aurait dû être restituée (checklist 11).
  D5  disparity     Outlier de densité dans une série homogène (AMF_YYYY, HCGE_YYYY) :
                    un millésime nettement plus pauvre que la médiane de sa série,
                    sur lignes / sous-sections / citations / références de page.

Usage :
    python3 check_completeness.py [repertoire] [--only D1,D5] [--quiet]

Code retour : 1 si au moins un signalement « fort » (D1, D2, D3) ; 0 sinon.
D4 et D5 sont indicatifs (n'affectent pas le code retour) car plus sujets au
contexte : un renvoi peut être légitime, un rapport source peut être réellement
plus mince.
"""
import re, glob, sys, statistics
from collections import defaultdict

# ---------------------------------------------------------------- helpers
TITLE_RE = re.compile(r'^(#{1,4})\s+(.*)$')
PAGE_RE  = re.compile(r'\bp\.\s?\d+', re.I)
QUOTE_OPEN, QUOTE_CLOSE = '«', '»'

def load(f):
    return open(f, encoding='utf-8').read().split('\n')

def has_quote(s):  return QUOTE_OPEN in s and QUOTE_CLOSE in s
def has_page(s):   return bool(PAGE_RE.search(s))

# ---------------------------------------------------------------- D1 : séries inline
def d1_series(files):
    flagged = []
    for f in files:
        series = []
        for i, ln in enumerate(load(f)):
            m = re.match(r'^\s*-\s*\*\*(\d+\.\d+)\*\*\s*[:：]', ln)
            if m:
                series.append((i + 1, m.group(1), has_quote(ln), ln.strip()))
        groups = defaultdict(list)
        for idx, lab, cit, txt in series:
            groups[lab.rsplit('.', 1)[0]].append((idx, lab, cit, txt))
        for _, items in groups.items():
            if len(items) >= 2:
                cits = [it[2] for it in items]
                if any(cits) and not all(cits):
                    for idx, lab, cit, txt in items:
                        if not cit:
                            flagged.append((f, idx, f"[{lab}] {txt[:88]}"))
    return flagged

# ---------------------------------------------------------------- D2 : sous-sections squelettiques
# Corps d'un titre #### = lignes jusqu'au prochain titre de niveau <= 4.
# Squelettique = ni citation, ni page dans le corps, et < MIN_CHARS car. utiles.
# Exclusion : un #### au corps STRICTEMENT vide suivi immédiatement d'un autre titre
# est un conteneur / intertitre de regroupement (mapping vers la grille A-M) — légitime.
MIN_CHARS = 60
PAGE_IN_TITLE = re.compile(r'\(?p\.\s?\d+', re.I)
def _bodies(lines):
    titles = [(i, len(m.group(1)), m.group(2).strip())
              for i, ln in enumerate(lines)
              for m in [TITLE_RE.match(ln)] if m]
    for k, (i, lvl, label) in enumerate(titles):
        end = titles[k + 1][0] if k + 1 < len(titles) else len(lines)
        next_is_title = (k + 1 < len(titles))
        body = [l for l in lines[i + 1:end] if l.strip()]
        yield i, lvl, label, body, next_is_title

def d2_skeleton(files):
    flagged = []
    for f in files:
        for i, lvl, label, body, next_is_title in _bodies(load(f)):
            if lvl != 4:
                continue
            body_text = ' '.join(body).strip()
            useful = len(re.sub(r'[\s\-*>|]', '', body_text))
            # conteneur : vide ET suivi d'un titre → intertitre de regroupement, on ignore
            if useful == 0 and next_is_title:
                continue
            has_cit = any(has_quote(l) for l in body)
            has_pg  = any(has_page(l) for l in body)
            if not has_cit and not has_pg and useful < MIN_CHARS:
                flagged.append((f, i + 1, f"#### {label[:80]}  (corps : {useful} car. utiles)"))
    return flagged

# ---------------------------------------------------------------- D2b : sections statistiques maigres
# Sous-section dont l'intitulé annonce une page (donc du contenu source existe) mais
# dont le corps est un placeholder « (Statistiques sur…) », ou ne contient AUCUN
# chiffre, ou fait < STAT_CHARS car. → la donnée chiffrée n'a pas été restituée.
STAT_CHARS = 90
def d2b_thin_stats(files):
    flagged = []
    for f in files:
        for i, lvl, label, body, _ in _bodies(load(f)):
            if lvl != 4 or not PAGE_IN_TITLE.search(label):
                continue
            body_text = ' '.join(body).strip()
            if not body_text:
                continue  # vide pur traité par D2
            useful = len(re.sub(r'[\s\-*>|]', '', body_text))
            placeholder = bool(re.match(r'^\(\s*[A-ZÉÀ]', body_text))
            has_num = bool(re.search(r'\d', body_text))
            if placeholder or not has_num or useful < STAT_CHARS:
                tag = 'placeholder' if placeholder else ('sans chiffre' if not has_num else 'court')
                flagged.append((f, i + 1, f"[{tag}] #### {label[:72]}"))
    return flagged

# ---------------------------------------------------------------- D3 : guillemets déséquilibrés
def d3_quotes(files):
    flagged = []
    for f in files:
        txt = '\n'.join(load(f))
        o, c = txt.count(QUOTE_OPEN), txt.count(QUOTE_CLOSE)
        if o != c:
            flagged.append((f, 0, f"{o} « pour {c} » (écart {o - c:+d}) — citation tronquée ?"))
    return flagged

# ---------------------------------------------------------------- D4 : renvois-substituts (indicatif)
SUBSTITUTE_RE = re.compile(
    r'(disponible sur demande|sur demande\b|figure (?:au|à la|en) p|'
    r'voir (?:le )?(?:tableau|détail|annexe)\b|détail(?:s)? (?:en|au) p|'
    r'non (?:reproduit|restitué|détaillé))', re.I)
def d4_substitute(files):
    flagged = []
    for f in files:
        for i, ln in enumerate(load(f)):
            if SUBSTITUTE_RE.search(ln):
                flagged.append((f, i + 1, ln.strip()[:90]))
    return flagged

# ---------------------------------------------------------------- D5 : disparité de série (indicatif)
SERIE_RE = re.compile(r'index_(AMF|HCGE)_(20\d\d)\.md$')
RATIO = 0.5  # un millésime sous 50 % de la médiane de sa série est signalé
def metrics(f):
    lines = load(f)
    txt = '\n'.join(lines)
    return {
        'lignes':       len(lines),
        'sous-sect.':   sum(1 for l in lines if l.startswith('#### ')),
        'citations':    len(re.findall(r'«[^»]*»', txt)),
        'réf. page':    len(PAGE_RE.findall(txt)),
    }
def d5_disparity(files):
    series = defaultdict(list)
    for f in files:
        m = SERIE_RE.search(f)
        if m:
            series[m.group(1)].append((m.group(2), f, metrics(f)))
    report = []
    for fam, items in sorted(series.items()):
        if len(items) < 3:
            continue
        keys = items[0][2].keys()
        med = {k: statistics.median(it[2][k] for it in items) for k in keys}
        for year, f, mt in sorted(items):
            low = [k for k in keys if med[k] and mt[k] < RATIO * med[k]]
            if low:
                detail = ', '.join(f"{k} {mt[k]} (méd. {med[k]:.0f})" for k in low)
                report.append((fam, year, f, detail))
    return report

# ---------------------------------------------------------------- runner
CHECKS = {
    'D1':  ('Séries inline incomplètes',       d1_series,     True),
    'D2':  ('Sous-sections squelettiques',     d2_skeleton,   True),
    'D2b': ('Sections statistiques maigres',   d2b_thin_stats, True),
    'D3':  ('Guillemets déséquilibrés',        d3_quotes,     True),
    'D4':  ('Renvois-substituts (indicatif)',  d4_substitute, False),
}

def main(argv):
    directory = '.'
    only = None
    quiet = False
    for a in argv:
        if a == '--quiet': quiet = True
        elif a.startswith('--only'): only = set(a.split('=', 1)[1].split(',')) if '=' in a else None
        elif not a.startswith('--'): directory = a
    files = sorted(glob.glob(directory.rstrip('/') + '/index_*.md'))
    if not files:
        print(f"Aucun index_*.md dans {directory!r}"); return 2

    strong = set()
    for code, (label, fn, is_strong) in CHECKS.items():
        if only and code not in only: continue
        res = fn(files)
        print(f"\n{'='*70}\n{code} — {label} : {len(res)} signalement(s)")
        if res:
            cur = None
            for f, ln, msg in res:
                short = f.split('/')[-1]
                if short != cur: print(f"  {short}"); cur = short
                loc = f"L{ln} " if ln else ""
                print(f"      {loc}{msg}")
            if is_strong:
                strong.update((f, ln) for f, ln, _ in res)
        elif not quiet:
            print("  (rien)")

    if only is None or 'D5' in only:
        rep = d5_disparity(files)
        print(f"\n{'='*70}\nD5 — Disparité de série (indicatif) : {len(rep)} millésime(s) outliers")
        for fam, year, f, detail in rep:
            print(f"  {fam} {year} : {detail}")
        if not rep and not quiet:
            print("  (séries homogènes)")

    print(f"\n{'='*70}")
    print(f"Bilan : {len(strong)} point(s) distinct(s) à confronter au PDF source (D1-D3).")
    print("D4/D5 indicatifs — contexte requis (renvoi légitime ? rapport réellement mince ?).")
    return 1 if strong else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
