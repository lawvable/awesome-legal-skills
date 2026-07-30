#!/usr/bin/env python3
"""
format_citation.py — Formatage bibliographique selon les normes SNE RefLex 2022.

Usage :
    python3 scripts/format_citation.py --type juris_cass --data '{"date":"2023-07-12","chambre":"civ. 1re","pourvoi":"21-12345"}'
    python3 scripts/format_citation.py --from-json results.json

Sortie : Citation formatée sur stdout.
"""

import argparse
import json
import sys
import re

MOIS_ABREGES = {
    1: "janv.", 2: "févr.", 3: "mars", 4: "avr.", 5: "mai", 6: "juin",
    7: "juill.", 8: "août", 9: "sept.", 10: "oct.", 11: "nov.", 12: "déc."
}


def parse_date(date_str):
    """Parse une date ISO (YYYY-MM-DD) ou partielle."""
    if not date_str:
        return None, None, None
    parts = date_str.split("-")
    year = int(parts[0]) if len(parts) >= 1 else None
    month = int(parts[1]) if len(parts) >= 2 else None
    day = int(parts[2]) if len(parts) >= 3 else None
    return year, month, day


def format_date_juridique(date_str):
    """Formate une date au format juridique français : JJ mois abrégé AAAA."""
    year, month, day = parse_date(date_str)
    if not year:
        return "[date inconnue]"
    if not month:
        return str(year)
    mois = MOIS_ABREGES.get(month, f"mois {month}")
    if not day:
        return f"{mois} {year}"
    # 1er pour le premier du mois
    jour = "1er" if day == 1 else str(day)
    return f"{jour} {mois} {year}"


def format_pourvoi(num):
    """Normalise un numéro de pourvoi : XX-XX.XXX."""
    if not num:
        return "[n° inconnu]"
    # Retirer les espaces et caractères parasites
    num = num.strip().replace(" ", "")
    # Vérifier si déjà au bon format
    if re.match(r"^\d{2}-\d{2}\.\d{3}$", num):
        return num
    # Essayer de reformater
    digits = re.sub(r"[^\d]", "", num)
    if len(digits) == 7:
        return f"{digits[:2]}-{digits[2:4]}.{digits[4:]}"
    return num  # Retourner tel quel si format inconnu


def format_juris_cass(data):
    """Cour de cassation : Cass. [ch.], [date], n° [pourvoi]"""
    chambre = data.get("chambre", "[ch.]")
    date = format_date_juridique(data.get("date", ""))
    pourvoi = format_pourvoi(data.get("pourvoi", ""))
    return f"Cass. {chambre}, {date}, n° {pourvoi}"


def format_juris_ce(data):
    """Conseil d'État : CE, [formation], [date], n° [requête]"""
    formation = data.get("formation", "")
    date = format_date_juridique(data.get("date", ""))
    requete = data.get("requete", data.get("numero", "[n°]"))
    formation_str = f", {formation}" if formation else ""
    nom = f", {data['nom']}" if data.get("nom") else ""
    return f"CE{formation_str}, {date}, n° {requete}{nom}"


def format_juris_const(data):
    """Conseil constitutionnel : Cons. const., [date], n° [numéro]"""
    date = format_date_juridique(data.get("date", ""))
    numero = data.get("numero", "[n°]")
    nom = f", {data['nom']}" if data.get("nom") else ""
    return f"Cons. const., {date}, n° {numero}{nom}"


def format_juris_ca(data):
    """Cour d'appel : CA [ville], [chambre], [date], n° RG [numéro]"""
    ville = data.get("ville", "[ville]")
    chambre = data.get("chambre", "")
    date = format_date_juridique(data.get("date", ""))
    rg = data.get("rg", data.get("numero", "[n° RG]"))
    chambre_str = f", {chambre}" if chambre else ""
    return f"CA {ville}{chambre_str}, {date}, n° RG {rg}"


def format_juris_tj(data):
    """Tribunal judiciaire : TJ [ville], [date], n° RG [numéro]"""
    ville = data.get("ville", "[ville]")
    date = format_date_juridique(data.get("date", ""))
    rg = data.get("rg", data.get("numero", "[n° RG]"))
    return f"TJ {ville}, {date}, n° RG {rg}"


def format_code_article(data):
    """Article de code : Art. [numéro] [code abrégé]"""
    numero = data.get("numero", "[n°]")
    code = data.get("code", "[code]")
    # Ajouter "L. " ou "R. " si présent dans le numéro mais pas le préfixe
    return f"Art. {numero} {code}"


def format_loi(data):
    """Loi : Loi n° [numéro] du [date] [titre]"""
    numero = data.get("numero", "[n°]")
    date = format_date_juridique(data.get("date", ""))
    titre = data.get("titre", "")
    titre_str = f" {titre}" if titre else ""
    return f"Loi n° {numero} du {date}{titre_str}"


def format_decret(data):
    """Décret : Décr. n° [numéro] du [date]"""
    numero = data.get("numero", "[n°]")
    date = format_date_juridique(data.get("date", ""))
    return f"Décr. n° {numero} du {date}"


def format_ordonnance(data):
    """Ordonnance : Ord. n° [numéro] du [date]"""
    numero = data.get("numero", "[n°]")
    date = format_date_juridique(data.get("date", ""))
    return f"Ord. n° {numero} du {date}"


def format_doctrine_article(data):
    """Article de doctrine : NOM Init., « Titre », Revue Année, p. X"""
    auteur = data.get("auteur", "[AUTEUR]")
    titre = data.get("titre", "[Titre]")
    revue = data.get("revue", "[Revue]")
    annee = data.get("annee", "[Année]")
    page = data.get("page", "")
    page_str = f", p. {page}" if page else ""
    return f'{auteur}, « {titre} », {revue} {annee}{page_str}'


def format_doctrine_ouvrage(data):
    """Ouvrage : NOM Init., Titre, Éditeur, Année[, Xe éd.]"""
    auteur = data.get("auteur", "[AUTEUR]")
    titre = data.get("titre", "[Titre]")
    editeur = data.get("editeur", "[Éditeur]")
    annee = data.get("annee", "[Année]")
    edition = data.get("edition", "")
    edition_str = f", {edition}" if edition else ""
    return f"{auteur}, {titre}, {editeur}, {annee}{edition_str}"


def format_doctrine_these(data):
    """Thèse : NOM Init., Titre, thèse Université, Année"""
    auteur = data.get("auteur", "[AUTEUR]")
    titre = data.get("titre", "[Titre]")
    universite = data.get("universite", "[Université]")
    annee = data.get("annee", "[Année]")
    return f"{auteur}, {titre}, thèse {universite}, {annee}"


FORMATTERS = {
    "juris_cass": format_juris_cass,
    "juris_ce": format_juris_ce,
    "juris_const": format_juris_const,
    "juris_ca": format_juris_ca,
    "juris_tj": format_juris_tj,
    "code_article": format_code_article,
    "loi": format_loi,
    "decret": format_decret,
    "ordonnance": format_ordonnance,
    "doctrine_article": format_doctrine_article,
    "doctrine_ouvrage": format_doctrine_ouvrage,
    "doctrine_these": format_doctrine_these,
}


def main():
    parser = argparse.ArgumentParser(description="Formatage de citation juridique (RefLex SNE 2022)")
    parser.add_argument("--type", "-t", choices=list(FORMATTERS.keys()), help="Type de référence")
    parser.add_argument("--data", "-d", help="Données JSON de la référence")
    parser.add_argument("--from-json", "-f", help="Fichier JSON contenant une liste de références à formater")

    args = parser.parse_args()

    if args.from_json:
        with open(args.from_json, "r", encoding="utf-8") as f:
            refs = json.load(f)
        results = []
        for ref in refs:
            ref_type = ref.get("type", "")
            formatter = FORMATTERS.get(ref_type)
            if formatter:
                results.append({"type": ref_type, "citation": formatter(ref.get("data", {}))})
            else:
                results.append({"type": ref_type, "error": f"Type inconnu : {ref_type}"})
        print(json.dumps(results, ensure_ascii=False, indent=2))
    elif args.type and args.data:
        data = json.loads(args.data)
        formatter = FORMATTERS[args.type]
        print(formatter(data))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
