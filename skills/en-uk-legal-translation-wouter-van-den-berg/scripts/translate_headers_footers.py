"""Translate text in word/headerN.xml and word/footerN.xml files.

OOXML stores page headers and footers in separate XML files alongside
document.xml. These typically contain short boilerplate — signature blocks
("represented by:", "Obligor", "Beneficiary"), draft watermarks
("TERVEZET – MINDEN JOG FENNTARTVA"), document management references, and
page numbers. Because the main translation pipeline only processes
document.xml (and optionally footnotes/endnotes/comments), header/footer
text is silently left in the source language.

This script has THREE modes. The scaffold+apply round-trip is the
recommended path. The legacy dictionary-lookup mode is kept as a
backwards-compatible fallback for documents whose headers/footers contain
only known boilerplate (watermarks, standardised role labels).

MODE 1 — Extract (recommended, first half of the round-trip):
    python translate_headers_footers.py <original.docx> --extract <scaffold.json>

    Reads all word/header*.xml and word/footer*.xml from the .docx,
    extracts every non-empty paragraph, and writes a JSON scaffold. Each
    entry carries its source file, its paragraph index within that file,
    the source text, per-run formatting metadata, and an empty `en`
    field. The operator (with the skill's LLM + lexicons) fills in `en`
    for every entry the same way they fill body paragraphs.json.

    For entries that must be preserved verbatim (project names, entity
    names, pure numbers, reference codes), the operator sets `en` equal
    to `text`, or leaves it null — both produce the same result.

MODE 2 — Apply (recommended, second half of the round-trip):
    python translate_headers_footers.py <original.docx> <output_dir> --apply <scaffold.json>

    Reads the filled-in JSON, groups entries by source file, and writes
    a translated copy of each header/footer XML to <output_dir>/word/.
    For each paragraph whose `en` field is set, replaces the paragraph's
    text while preserving all run properties (w:sz, w:rFonts, w:color,
    w:b, w:i, etc.). Entries with `en == null` or `en == ""` are left
    verbatim.

MODE 3 — Legacy dictionary lookup (fallback):
    python translate_headers_footers.py <original.docx> <output_dir> --language <lang>

    Applies a built-in boilerplate map for the given source language.
    Kept for speed on documents where the only header/footer changes are
    watermarks and standardised role labels. Prints a one-line notice
    recommending the round-trip for documents with free-text headers.

Example:
    # Round-trip (recommended)
    python translate_headers_footers.py original_hu.docx --extract work/hu/headers_footers.json
    # ... operator translates the JSON ...
    python translate_headers_footers.py original_hu.docx work/hu/final --apply work/hu/headers_footers.json

    # Legacy (only if you know the headers only need watermark flips)
    python translate_headers_footers.py original_hu.docx work/hu/final --language hungarian
"""
import sys
import os
import re
import json
import zipfile
import argparse
import lxml.etree as ET

def _check_self_integrity():
    """Detect install-time truncation. Whole-file scan tolerates null-padding."""
    try:
        with open(os.path.abspath(__file__), 'r', encoding='utf-8') as f:
            content = f.read()
    except OSError:
        return
    if '\n# === SKILL FILE COMPLETE ===' not in content:
        msg = (
            "\n" + "=" * 60 + "\n"
            "[skill] FILE INTEGRITY CHECK FAILED — script truncated.\n"
            f"  File: {os.path.abspath(__file__)}\n"
            f"  Size: {len(content):,} bytes (sentinel marker missing).\n"
            "  Re-install the skill from the .skill / .zip archive.\n"
            + "=" * 60 + "\n"
        )
        print(msg, file=sys.stderr)
        sys.exit(3)


_check_self_integrity()



W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

# ──────────────────────────────────────────────────────────────────────
# Legacy dictionary-lookup maps (Mode 3 only).
#
# The scaffold+apply round-trip (Modes 1 & 2) handles arbitrary header
# content correctly because the operator translates each paragraph in
# context with the lexicons. These dictionaries remain only as a
# fast-path fallback for documents whose headers contain nothing but
# standardised boilerplate (watermarks, role labels). They are NOT a
# substitute for the round-trip on anything that has free-text content
# (agreement titles, version labels, month names, initialling boxes,
# custom watermarks, compliance stamps).
# ──────────────────────────────────────────────────────────────────────

HUNGARIAN_MAP = {
    # Signature block roles
    'Kötelezett': 'Obligor',
    'Jogosult': 'Beneficiary',
    'Hitelező': 'Lender',
    'Adós': 'Borrower',
    'Kölcsönadó': 'Lender',
    'Kölcsönvevő': 'Borrower',
    'Eladó': 'Seller',
    'Vevő': 'Buyer',
    'Bérbeadó': 'Lessor',
    'Bérlő': 'Lessee',
    'Zálogkötelezett': 'Pledgor',
    'Zálogjogosult': 'Pledgee',
    'Kezes': 'Guarantor',
    'Megbízó': 'Principal',
    'Meghatalmazott': 'Attorney-in-Fact',
    'Ügyvezető': 'Managing Director',
    'Igazgatósági tag': 'Board Member',
    'Cégvezető': 'Company Director',
    'Ügyvéd': 'Attorney',
    'Közjegyző': 'Notary Public',
    # Signature formulas
    'képviseli': 'represented by',
    'Képviseli': 'Represented by',
    'Beosztása:': 'Title:',
    'Beosztása': 'Title',
    'Aláírás:': 'Signature:',
    'Aláírás': 'Signature',
    'Név:': 'Name:',
    'Dátum:': 'Date:',
    'Kelt:': 'Dated:',
    'Kelt': 'Dated',
    'napján': '',
    # Countersignature / notarial
    'A jelen okiratot ezennel ellenjegyzem': 'I hereby countersign this deed',
    'Ellenjegyző Ügyvéd': 'Countersigning Attorney',
    'Ellenjegyző ügyvéd': 'Countersigning attorney',
    'KASZ:': 'Bar reg. no.:',
    'KASZ': 'Bar reg. no.',
    # Draft watermarks
    'TERVEZET': 'DRAFT',
    'MINDEN JOG FENNTARTVA': 'WITHOUT PREJUDICE',
    'TOVÁBBI EGYEZTETÉSEK TÁRGYA': 'SUBJECT TO COMMENTS',
    'BIZALMAS': 'CONFIDENTIAL',
    'TITKOS': 'CONFIDENTIAL',
    # Document references
    'oldal': 'page',
    'Oldal': 'Page',
}

ITALIAN_MAP = {
    # Signature block roles
    'Obbligato': 'Obligor',
    'Beneficiario': 'Beneficiary',
    'Mutuante': 'Lender',
    'Mutuatario': 'Borrower',
    'Venditore': 'Seller',
    'Acquirente': 'Buyer',
    'Locatore': 'Lessor',
    'Conduttore': 'Lessee',
    'Garante': 'Guarantor',
    'Mandante': 'Principal',
    'Procuratore': 'Attorney-in-Fact',
    'Amministratore Delegato': 'Managing Director',
    'Legale Rappresentante': 'Legal Representative',
    'Notaio': 'Notary Public',
    'Avvocato': 'Attorney',
    # Signature formulas
    'rappresentato da': 'represented by',
    'Rappresentato da': 'Represented by',
    'Qualifica:': 'Title:',
    'Firma:': 'Signature:',
    'Nome:': 'Name:',
    'Data:': 'Date:',
    # Draft watermarks
    'BOZZA': 'DRAFT',
    'RISERVATO': 'CONFIDENTIAL',
    'SENZA PREGIUDIZIO': 'WITHOUT PREJUDICE',
    'SOGGETTO A COMMENTI': 'SUBJECT TO COMMENTS',
}

GERMAN_MAP = {
    'Schuldner': 'Obligor',
    'Begünstigter': 'Beneficiary',
    'Darlehensgeber': 'Lender',
    'Darlehensnehmer': 'Borrower',
    'Verkäufer': 'Seller',
    'Käufer': 'Buyer',
    'Vermieter': 'Lessor',
    'Mieter': 'Lessee',
    'Bürge': 'Guarantor',
    'Geschäftsführer': 'Managing Director',
    'Notar': 'Notary Public',
    'Rechtsanwalt': 'Attorney',
    'vertreten durch': 'represented by',
    'Vertreten durch': 'Represented by',
    'Unterschrift:': 'Signature:',
    'Name:': 'Name:',
    'Datum:': 'Date:',
    'Titel:': 'Title:',
    'ENTWURF': 'DRAFT',
    'VERTRAULICH': 'CONFIDENTIAL',
    'OHNE PRÄJUDIZ': 'WITHOUT PREJUDICE',
}

FRENCH_MAP = {
    'Débiteur': 'Obligor',
    'Bénéficiaire': 'Beneficiary',
    'Prêteur': 'Lender',
    'Emprunteur': 'Borrower',
    'Vendeur': 'Seller',
    'Acheteur': 'Buyer',
    'Bailleur': 'Lessor',
    'Preneur': 'Lessee',
    'Garant': 'Guarantor',
    'Mandataire': 'Attorney-in-Fact',
    'Gérant': 'Managing Director',
    'Notaire': 'Notary Public',
    'Avocat': 'Attorney',
    'représenté par': 'represented by',
    'Représenté par': 'Represented by',
    'Qualité:': 'Title:',
    'Signature:': 'Signature:',
    'Nom:': 'Name:',
    'Date:': 'Date:',
    'PROJET': 'DRAFT',
    'CONFIDENTIEL': 'CONFIDENTIAL',
    'SANS PRÉJUDICE': 'WITHOUT PREJUDICE',
    'SOUS RÉSERVE': 'SUBJECT TO COMMENTS',
}

SPANISH_MAP = {
    'Deudor': 'Obligor',
    'Beneficiario': 'Beneficiary',
    'Prestamista': 'Lender',
    'Prestatario': 'Borrower',
    'Vendedor': 'Seller',
    'Comprador': 'Buyer',
    'Arrendador': 'Lessor',
    'Arrendatario': 'Lessee',
    'Garante': 'Guarantor',
    'Apoderado': 'Attorney-in-Fact',
    'Director General': 'Managing Director',
    'Notario': 'Notary Public',
    'Abogado': 'Attorney',
    'representado por': 'represented by',
    'Representado por': 'Represented by',
    'Cargo:': 'Title:',
    'Firma:': 'Signature:',
    'Nombre:': 'Name:',
    'Fecha:': 'Date:',
    'BORRADOR': 'DRAFT',
    'CONFIDENCIAL': 'CONFIDENTIAL',
    'SIN PERJUICIO': 'WITHOUT PREJUDICE',
}

PORTUGUESE_MAP = {
    'Devedor': 'Obligor',
    'Beneficiário': 'Beneficiary',
    'Mutuante': 'Lender',
    'Mutuário': 'Borrower',
    'Vendedor': 'Seller',
    'Comprador': 'Buyer',
    'Locador': 'Lessor',
    'Locatário': 'Lessee',
    'Garante': 'Guarantor',
    'Procurador': 'Attorney-in-Fact',
    'Diretor-Geral': 'Managing Director',
    'Notário': 'Notary Public',
    'Advogado': 'Attorney',
    'representado por': 'represented by',
    'Representado por': 'Represented by',
    'Cargo:': 'Title:',
    'Assinatura:': 'Signature:',
    'Nome:': 'Name:',
    'Data:': 'Date:',
    'MINUTA': 'DRAFT',
    'CONFIDENCIAL': 'CONFIDENTIAL',
    'SEM PREJUÍZO': 'WITHOUT PREJUDICE',
}

DUTCH_MAP = {
    'Schuldenaar': 'Obligor',
    'Begunstigde': 'Beneficiary',
    'Kredietgever': 'Lender',
    'Kredietnemer': 'Borrower',
    'Verkoper': 'Seller',
    'Koper': 'Buyer',
    'Verhuurder': 'Lessor',
    'Huurder': 'Lessee',
    'Borg': 'Guarantor',
    'Gevolmachtigde': 'Attorney-in-Fact',
    'Directeur': 'Managing Director',
    'Notaris': 'Notary Public',
    'Advocaat': 'Attorney',
    'vertegenwoordigd door': 'represented by',
    'Vertegenwoordigd door': 'Represented by',
    'Functie:': 'Title:',
    'Handtekening:': 'Signature:',
    'Naam:': 'Name:',
    'Datum:': 'Date:',
    'CONCEPT': 'DRAFT',
    'VERTROUWELIJK': 'CONFIDENTIAL',
    'ZONDER VOOROORDEEL': 'WITHOUT PREJUDICE',
}

POLISH_MAP = {
    'Dłużnik': 'Obligor',
    'Beneficjent': 'Beneficiary',
    'Kredytodawca': 'Lender',
    'Kredytobiorca': 'Borrower',
    'Sprzedający': 'Seller',
    'Kupujący': 'Buyer',
    'Wynajmujący': 'Lessor',
    'Najemca': 'Lessee',
    'Gwarant': 'Guarantor',
    'Pełnomocnik': 'Attorney-in-Fact',
    'Prezes Zarządu': 'Managing Director',
    'Notariusz': 'Notary Public',
    'Adwokat': 'Attorney',
    'reprezentowany przez': 'represented by',
    'Reprezentowany przez': 'Represented by',
    'Stanowisko:': 'Title:',
    'Podpis:': 'Signature:',
    'Imię i nazwisko:': 'Name:',
    'Data:': 'Date:',
    'PROJEKT': 'DRAFT',
    'POUFNE': 'CONFIDENTIAL',
    'BEZ USZCZERBKU': 'WITHOUT PREJUDICE',
}

FINNISH_MAP = {
    'Velallinen': 'Obligor',
    'Edunsaaja': 'Beneficiary',
    'Lainanantaja': 'Lender',
    'Lainanottaja': 'Borrower',
    'Myyjä': 'Seller',
    'Ostaja': 'Buyer',
    'Vuokranantaja': 'Lessor',
    'Vuokralainen': 'Lessee',
    'Takaaja': 'Guarantor',
    'Valtuutettu': 'Attorney-in-Fact',
    'Toimitusjohtaja': 'Managing Director',
    'Julkinen notaari': 'Notary Public',
    'Asianajaja': 'Attorney',
    'edustamana': 'represented by',
    'Edustamana': 'Represented by',
    'Tehtävä:': 'Title:',
    'Allekirjoitus:': 'Signature:',
    'Nimi:': 'Name:',
    'Päivämäärä:': 'Date:',
    'LUONNOS': 'DRAFT',
    'LUOTTAMUKSELLINEN': 'CONFIDENTIAL',
}

LANGUAGE_MAPS = {
    'hungarian': HUNGARIAN_MAP,
    'italian': ITALIAN_MAP,
    'german': GERMAN_MAP,
    'french': FRENCH_MAP,
    'spanish': SPANISH_MAP,
    'portuguese': PORTUGUESE_MAP,
    'dutch': DUTCH_MAP,
    'polish': POLISH_MAP,
    'finnish': FINNISH_MAP,
}

def detect_language(all_text):
    """Auto-detect source language from header/footer text content (legacy mode)."""
    text_lower = all_text.lower()
    scores = {}
    for lang, tmap in LANGUAGE_MAPS.items():
        score = 0
        for src in tmap:
            if src.lower() in text_lower:
                score += 1
        if score > 0:
            scores[lang] = score
    if scores:
        return max(scores, key=scores.get)
    return None

# ──────────────────────────────────────────────────────────────────────
# Run-property helpers (shared between scaffold extraction and legacy).
# Intentionally small — we only need enough metadata for the operator to
# see what formatting applies to each run when filling in `en`.
# ──────────────────────────────────────────────────────────────────────

# ECMA-376 ST_OnOff: true|false|1|0|on|off (case-insensitive).
# 'off' added to the falsy set.
_ST_ONOFF_FALSE = {'false', '0', 'off'}

def _has_prop(rpr, prop_name):
    if rpr is None:
        return False
    elem = rpr.find(f'{{{W}}}{prop_name}')
    if elem is None:
        return False
    val = elem.get(f'{{{W}}}val')
    if val is not None and val.strip().lower() in _ST_ONOFF_FALSE:
        return False
    return True

def _get_font_info(rpr):
    if rpr is None:
        return None, None
    font_elem = rpr.find(f'{{{W}}}rFonts')
    font = font_elem.get(f'{{{W}}}ascii') if font_elem is not None else None
    sz_elem = rpr.find(f'{{{W}}}sz')
    sz = sz_elem.get(f'{{{W}}}val') if sz_elem is not None else None
    return font, sz

def _get_color(rpr):
    if rpr is None:
        return None
    c = rpr.find(f'{{{W}}}color')
    return c.get(f'{{{W}}}val') if c is not None else None

def _iter_own_runs(p_elem):
    """Yield w:r descendants of p_elem that DO NOT belong to a nested w:p.

    Header/footer XML frequently contains text boxes (`w:txbxContent`) and
    structured document tags (`w:sdtContent`) that hold their own child
    paragraphs. A naive `p_elem.iter(w:r)` would pick up those inner runs
    and treat the outer paragraph as if it owned all descendant text.
    When the apply step then clears "all w:t except the first", it wipes
    out the nested paragraphs' text.

    This helper walks the w:r descendants and filters out any whose path
    to p_elem crosses another w:p — those belong to a nested paragraph
    and will be handled when `tree.iter(w:p)` reaches them directly.
    """
    p_tag = f'{{{W}}}p'
    for r in p_elem.iter(f'{{{W}}}r'):
        ancestor = r.getparent()
        is_nested = False
        while ancestor is not None and ancestor is not p_elem:
            if ancestor.tag == p_tag:
                is_nested = True
                break
            ancestor = ancestor.getparent()
        if not is_nested:
            yield r
def _classify_runs(p_elem):
    """Classify every direct-child <w:r> of p_elem by its semantic role.

    Returns a list of dicts (one per run, in document order):
      {
        'run': <w:r element>,
        'role': 'static_text' | 'field_begin' | 'field_instr' |
                'field_separate' | 'field_cached_result' | 'field_end' |
                'other',
        'field_type': <field type name (e.g. "PAGE")> if inside a field,
        't_elem': <w:t element> if role is static_text or field_cached_result,
        'text': <text content> if t_elem present,
      }

    Field-region detection: a run with <w:fldChar fldCharType="begin"/>
    opens a region; subsequent runs with <w:instrText> name the field
    type; a run with <w:fldChar fldCharType="separate"/> ends the
    instruction phase; subsequent <w:t> runs are field-cached results;
    a <w:fldChar fldCharType="end"/> closes the region.

    Runs that are NOT inside any field region and that have a <w:t>
    are role 'static_text'. Runs that are inside a field region's
    cached-result phase are role 'field_cached_result'.
    """
    classified = []
    in_field = False
    in_cached_result = False
    current_field_type = None
    for r in _iter_own_runs(p_elem):
        fldChar = r.find(f'{{{W}}}fldChar')
        instrText = r.find(f'{{{W}}}instrText')
        t = r.find(f'{{{W}}}t')
        info = {'run': r, 'role': 'other', 'field_type': current_field_type,
                't_elem': None, 'text': ''}
        if fldChar is not None:
            ftype = fldChar.get(f'{{{W}}}fldCharType')
            if ftype == 'begin':
                in_field = True
                in_cached_result = False
                current_field_type = None
                info['role'] = 'field_begin'
            elif ftype == 'separate':
                in_cached_result = True
                info['role'] = 'field_separate'
                info['field_type'] = current_field_type
            elif ftype == 'end':
                in_field = False
                in_cached_result = False
                ft = current_field_type
                current_field_type = None
                info['role'] = 'field_end'
                info['field_type'] = ft
        elif instrText is not None and in_field:
            # Extract field type from the first whitespace-delimited token
            instr = (instrText.text or '').strip()
            if instr:
                # First token is the field type (PAGE, NUMPAGES, DATE, ...)
                tokens = instr.split()
                if tokens and current_field_type is None:
                    current_field_type = tokens[0].upper()
                info['field_type'] = current_field_type
            info['role'] = 'field_instr'
        elif t is not None and t.text is not None:
            info['t_elem'] = t
            info['text'] = t.text
            if in_field and in_cached_result:
                info['role'] = 'field_cached_result'
                info['field_type'] = current_field_type
            elif not in_field:
                info['role'] = 'static_text'
            else:
                # in_field but not in cached_result phase (e.g. between begin
                # and separate); rare. Treat as 'other' — not translatable.
                info['role'] = 'other'
                info['field_type'] = current_field_type
        classified.append(info)
    return classified


def _field_aware_text_and_fields(p_elem):
    """Return (text_with_placeholders, fields_list, has_fields).

    For paragraphs with no field regions: returns the flat text + empty
    fields list + False — caller can use the legacy code path.

    For paragraphs with fields: returns text with `<<TYPE>>` placeholders
    substituted at each field's cached-result position; a list of
    {"type", "cached_result"} dicts in document order; True.
    """
    classified = _classify_runs(p_elem)
    has_field = any(c['role'].startswith('field_') for c in classified)
    if not has_field:
        # Legacy path: just concat all static text
        texts = [c['text'] for c in classified
                 if c['role'] == 'static_text']
        return ''.join(texts), [], False

    text_parts = []
    fields = []
    seen_types = []
    for c in classified:
        if c['role'] == 'static_text':
            text_parts.append(c['text'])
        elif c['role'] == 'field_cached_result':
            ftype = c['field_type'] or 'FIELD'
            text_parts.append(f'<<{ftype}>>')
            fields.append({
                'type': ftype,
                'cached_result': c['text'],
            })
            seen_types.append(ftype)
        # field_begin / field_instr / field_separate / field_end / other
        # contribute no visible text
    # Edge case: a field with no separate (no cached result run) — emit
    # the placeholder anyway based on instrText alone.
    # Walk for begin-without-separate: scan classified for begin then
    # end without an intervening field_cached_result.
    # (Skip for simplicity in the common case; instrText-only fields are
    # rare in real documents and are handled by the legacy fall-through
    # if seen.)
    return ''.join(text_parts), fields, True


def _apply_with_fields(p_elem, en_text, expected_fields):
    """Field-aware apply: distribute en_text static segments across the
    paragraph's static-text runs by field-zone, leaving field-cached-result
    runs and field-structure runs untouched.

    Splits en_text on `<<TYPE>>` placeholders matching the paragraph's
    field types in document order, producing N+1 static parts for N
    fields. Each part is placed into the *zone* of static_runs between
    the corresponding field boundaries:

      zone 0: static_runs before the first field_begin
      zone i: static_runs between field i's field_end and field (i+1)'s
              field_begin
      zone N: static_runs after the last field's field_end

    Within a zone, the entire part text goes into the FIRST run of that
    zone; remaining runs in the zone are emptied. This preserves the
    rendered text exactly while keeping every original run shell (so
    `w:rPr`, `w:rsid`, fonts, and cached field results survive).

    Returns True on success.
    """
    classified = _classify_runs(p_elem)
    if not any(c['role'].startswith('field_') for c in classified):
        return False

    # Walk classified, assign each static_run to its zone (counter
    # increments at every field_end).
    zone = 0
    zones = {}  # zone_index -> [list of static_run dicts in document order]
    for c in classified:
        if c['role'] == 'field_end':
            zone += 1
            continue
        if c['role'] == 'static_text':
            zones.setdefault(zone, []).append(c)

    # Number of fields seen.
    n_fields_in_doc = sum(1 for c in classified if c['role'] == 'field_begin')

    # Split en_text on placeholders.
    placeholder_re = re.compile(r'<<[A-Z][A-Z0-9_]*>>')
    parts = placeholder_re.split(en_text)
    if not parts:
        return False

    # If the translator preserved exactly the right number of placeholders
    # we expect len(parts) == n_fields_in_doc + 1. If they dropped some,
    # pad with empty strings; if they added some (rare — translator used
    # extra placeholders), merge the extras into the last part.
    expected_parts = n_fields_in_doc + 1
    if len(parts) < expected_parts:
        parts = parts + [''] * (expected_parts - len(parts))
    elif len(parts) > expected_parts and expected_parts > 0:
        head = parts[:expected_parts - 1]
        tail = ''.join(parts[expected_parts - 1:])
        parts = head + [tail]

    # Assign each part to its zone.
    XML_SPACE = '{http://www.w3.org/XML/1998/namespace}space'
    for zi in range(expected_parts):
        zone_runs = zones.get(zi, [])
        part = parts[zi] if zi < len(parts) else ''
        if not zone_runs:
            # Translator inserted text in a zone that has no static runs.
            # Cannot place it without manufacturing new runs; drop it
            # silently — translator should have used the placeholder.
            continue
        # Put all of `part` in the first run of the zone, empty the rest.
        first = zone_runs[0]
        if first['t_elem'] is not None:
            first['t_elem'].text = part
            first['t_elem'].set(XML_SPACE, 'preserve')
        for c in zone_runs[1:]:
            if c['t_elem'] is not None:
                c['t_elem'].text = ''
                c['t_elem'].set(XML_SPACE, 'preserve')

    # Field-cached-result runs are LEFT UNTOUCHED — Word will re-compute
    # them at render time. The cached values stay as-is.
    return True



def _para_text(p_elem):
    """Concatenate this paragraph's own w:t text (excluding nested paragraphs)."""
    parts = []
    for r in _iter_own_runs(p_elem):
        for t in r.findall(f'{{{W}}}t'):
            if t.text:
                parts.append(t.text)
    return ''.join(parts)

def _para_runs(p_elem):
    """Extract per-run metadata for this paragraph's own runs.

    Excludes runs belonging to nested paragraphs (text boxes, content
    controls) — those are handled when tree.iter(w:p) reaches them as
    paragraphs in their own right.
    """
    runs = []
    char_offset = 0
    for r in _iter_own_runs(p_elem):
        rpr = r.find(f'{{{W}}}rPr')
        text_parts = []
        for child in r:
            ctag = child.tag.split('}')[1] if '}' in child.tag else child.tag
            if ctag == 't' and child.text:
                text_parts.append(child.text)
        text = ''.join(text_parts)
        if not text:
            continue
        bold = _has_prop(rpr, 'b')
        italic = _has_prop(rpr, 'i')
        font, sz = _get_font_info(rpr)
        color = _get_color(rpr)
        run_info = {
            'start': char_offset,
            'end': char_offset + len(text),
            'text': text,
            'bold': bold,
            'italic': italic,
        }
        if font:
            run_info['font'] = font
        if sz:
            run_info['sz'] = sz
        if color:
            run_info['color'] = color
        runs.append(run_info)
        char_offset += len(text)
    return runs

# ──────────────────────────────────────────────────────────────────────
# MODE 1 — Extract to JSON scaffold.
# ──────────────────────────────────────────────────────────────────────

def extract_to_scaffold(docx_path, out_json):
    """Read all header/footer XMLs and write a scaffold JSON for operator translation.

    Scaffold entry shape (mirrors body paragraphs.json where it matters):
        {
          "idx": <global index across all header/footer paragraphs>,
          "source": "word/header1.xml",
          "p_idx": <paragraph index within that source file>,
          "text": "<source text>",
          "runs": [ {"start": ..., "end": ..., "text": ..., "bold": ..., ...}, ... ],
          "en": null,
          "en_runs": null
        }

    Only non-empty paragraphs are emitted; empty paragraphs (pure whitespace,
    page number fields, tab-only lines) are skipped — there is nothing to
    translate. The apply step walks the XML from scratch so it sees every
    paragraph including skipped ones and leaves them untouched.
    """
    entries = []
    global_idx = 0
    hf_names = []
    with zipfile.ZipFile(docx_path, 'r') as zf:
        hf_names = sorted([
            n for n in zf.namelist()
            if (n.startswith('word/header') or n.startswith('word/footer'))
            and n.endswith('.xml')
        ])
        if not hf_names:
            print('No word/header*.xml or word/footer*.xml found in this .docx.')
            return False
        for name in hf_names:
            data = zf.read(name)
            tree = ET.fromstring(data)
            for p_idx, p in enumerate(tree.iter(f'{{{W}}}p')):
                # Rev37: detect fields and emit placeholders so the
                # translator does not "translate" cached field results.
                fa_text, fa_fields, has_fields = _field_aware_text_and_fields(p)
                # Fall back to legacy text if the field-aware path
                # produced something inconsistent (defensive).
                text = fa_text if has_fields else _para_text(p)
                if not text.strip():
                    continue
                entry = {
                    'idx': global_idx,
                    'source': name,
                    'p_idx': p_idx,
                    'text': text,
                    'runs': _para_runs(p),
                    'en': None,
                    'en_runs': None,
                }
                if has_fields:
                    entry['fields'] = fa_fields
                entries.append(entry)
                global_idx += 1
    os.makedirs(os.path.dirname(os.path.abspath(out_json)), exist_ok=True)
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=1)
    print(
        f'Extracted {len(entries)} non-empty paragraph(s) from '
        f'{len(hf_names)} header/footer file(s) to {out_json}.'
    )
    print(
        'Fill the "en" field for every entry that needs translating, the '
        'same way you fill body paragraphs.json. Entries left at null '
        '(or with en == text) are preserved verbatim by --apply.'
    )
    return True

# ──────────────────────────────────────────────────────────────────────
# MODE 2 — Apply scaffold JSON back onto header/footer XMLs.
# ──────────────────────────────────────────────────────────────────────

def _apply_paragraph_text(p_elem, en_text):
    """Write `en_text` into the paragraph's first non-empty w:t and clear the rest.

    Preserves every run's properties (w:sz, w:rFonts, w:color, w:b, w:i,
    field codes, tab stops, w:br line breaks). Run structure is unchanged;
    only text content is replaced. The first run's formatting controls the
    whole paragraph in the translated output — which is correct for the
    vast majority of header/footer content (single-formatting paragraphs).

    Paragraphs with mid-paragraph formatting changes (e.g. bold project
    name followed by italic version label) collapse to the first run's
    formatting. If that is a problem on a given document, the operator can
    supply per-run en text via en_runs in a future scaffold version; for
    now, hand-edit the XML as a last resort.

    Returns True if anything was changed.
    """
    # Find w:t elements that sit directly under a real w:r AND that belong
    # to this paragraph (not to a nested w:p inside a text box or content
    # control). _iter_own_runs filters out nested-paragraph runs so the
    # replacement does not clobber adjacent paragraphs' content.
    t_elems = []
    for r in _iter_own_runs(p_elem):
        for t in r.findall(f'{{{W}}}t'):
            t_elems.append(t)
    if not t_elems:
        return False
    first = t_elems[0]
    first.text = en_text
    first.set(f'{{http://www.w3.org/XML/1998/namespace}}space', 'preserve')
    for t in t_elems[1:]:
        t.text = ''
    return True

def apply_from_scaffold(docx_path, scaffold_json, output_dir):
    """Read a filled-in scaffold JSON and write translated header/footer XMLs.

    For each header/footer source file referenced in the scaffold:
      - Parse the original XML from the .docx.
      - For each paragraph whose scaffold entry has a usable `en`,
        replace that paragraph's text while preserving run properties.
      - Write the result to <output_dir>/<source_path>.

    Entries whose `en` is null, empty, or equals the source `text` are
    treated as "preserve verbatim" — their XML paragraph is left exactly
    as it was, and the output file is still written (so repack_docx.py's
    --headers-footers-dir picks up every file consistently).
    """
    with open(scaffold_json, 'r', encoding='utf-8') as f:
        entries = json.load(f)

    # Group entries by source file.
    by_source = {}
    for e in entries:
        by_source.setdefault(e['source'], []).append(e)

    written = []
    changed_counts = {}
    with zipfile.ZipFile(docx_path, 'r') as zf:
        available = set(zf.namelist())
        for source, file_entries in by_source.items():
            if source not in available:
                print(f'WARNING: scaffold references {source} but it is not in the .docx; skipping.')
                continue

            # Map p_idx -> (en_text, fields_list_or_None) for non-trivial entries.
            apply_map = {}
            for e in file_entries:
                en = e.get('en')
                if en is None:
                    continue
                en_str = str(en)
                if en_str.strip() == '':
                    continue
                if en_str == e.get('text'):
                    # operator chose to preserve verbatim — no replacement needed.
                    continue
                apply_map[e['p_idx']] = (en_str, e.get('fields'))

            data = zf.read(source)
            tree = ET.fromstring(data)
            changes = 0
            if apply_map:
                for p_idx, p in enumerate(tree.iter(f'{{{W}}}p')):
                    if p_idx not in apply_map:
                        continue
                    en_text, fields_list = apply_map[p_idx]
                    if fields_list:
                        # Rev37: field-aware apply preserves field structure.
                        if _apply_with_fields(p, en_text, fields_list):
                            changes += 1
                    else:
                        if _apply_paragraph_text(p, en_text):
                            changes += 1

            out_path = os.path.join(output_dir, source)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            serialized = ET.tostring(
                tree, xml_declaration=True, encoding='UTF-8', standalone=True
            )
            with open(out_path, 'wb') as f:
                f.write(serialized)
            written.append(source)
            changed_counts[source] = changes

    total_changes = sum(changed_counts.values())
    print(
        f'Applied translations to {len(written)} file(s), '
        f'{total_changes} paragraph replacement(s) total.'
    )
    for src in written:
        print(f'  {src}: {changed_counts[src]} paragraph(s) replaced')
    if total_changes == 0:
        print(
            'NOTE: no paragraphs were replaced — every scaffold entry either had '
            'en == null, en == "", or en == text. Verify the scaffold is filled in.'
        )
    return total_changes > 0

# ──────────────────────────────────────────────────────────────────────
# MODE 3 — Legacy dictionary-lookup translation.
# Retained for back-compat and for watermark-only documents.
# ──────────────────────────────────────────────────────────────────────

def merge_split_runs(paragraph, tmap):
    """Merge adjacent w:r runs that form a known term when concatenated."""
    runs = list(paragraph.findall(f'{{{W}}}r'))
    changed = False
    i = 0
    while i < len(runs) - 1:
        t1 = runs[i].find(f'{{{W}}}t')
        t2 = runs[i + 1].find(f'{{{W}}}t')
        if t1 is not None and t2 is not None and t1.text and t2.text:
            combined = t1.text + t2.text
            for src_key in sorted(tmap.keys(), key=len, reverse=True):
                if (src_key.lower() in combined.lower()
                        and src_key.lower() not in t1.text.lower()
                        and src_key.lower() not in t2.text.lower()):
                    colon_run = None
                    if i + 2 < len(runs):
                        t3 = runs[i + 2].find(f'{{{W}}}t')
                        if t3 is not None and t3.text and t3.text.strip() == ':':
                            colon_run = runs[i + 2]
                    translated = tmap.get(src_key, src_key)
                    if colon_run is not None and not translated.endswith(':'):
                        t1.text = translated + ':'
                        paragraph.remove(runs[i + 1])
                        paragraph.remove(colon_run)
                    else:
                        t1.text = translated
                        paragraph.remove(runs[i + 1])
                    t1.set(f'{{{W}}}space', 'preserve')
                    changed = True
                    runs = list(paragraph.findall(f'{{{W}}}r'))
                    break
            else:
                i += 1
                continue
            continue
        i += 1
    return changed

def translate_xml(xml_bytes, tmap):
    """Translate all w:t text in an XML tree using the translation map (legacy)."""
    tree = ET.fromstring(xml_bytes)
    changes = []
    for p in tree.iter(f'{{{W}}}p'):
        if merge_split_runs(p, tmap):
            changes.append('  [merged split runs]')
    sorted_entries = sorted(tmap.items(), key=lambda x: len(x[0]), reverse=True)
    for t_elem in tree.iter(f'{{{W}}}t'):
        if not t_elem.text:
            continue
        original = t_elem.text
        translated = original
        for src, tgt in sorted_entries:
            if src in translated:
                translated = translated.replace(src, tgt)
        if translated != original:
            t_elem.text = translated
            changes.append(f'  "{original.strip()}" → "{translated.strip()}"')
    if changes:
        return ET.tostring(tree, xml_declaration=True, encoding='UTF-8',
                           standalone=True), changes
    return None, []

def translate_headers_footers_legacy(orig_docx, output_dir, language=None):
    """Legacy dictionary-lookup mode (Mode 3)."""
    print(
        'NOTE: running legacy dictionary-lookup mode. For any header/footer '
        'that contains free-text content (agreement titles, version labels, '
        'month names, custom watermarks), prefer the scaffold+apply round-trip '
        '(--extract then --apply). Dictionary lookup only handles pre-listed '
        'boilerplate and silently leaves everything else in the source language.',
        file=sys.stderr,
    )
    with zipfile.ZipFile(orig_docx, 'r') as zf:
        hf_files = [n for n in zf.namelist()
                     if (n.startswith('word/header') or n.startswith('word/footer'))
                     and n.endswith('.xml')]
        if not hf_files:
            print('No header/footer XML files found in this .docx.')
            return False
        all_text = []
        file_contents = {}
        for name in hf_files:
            data = zf.read(name)
            file_contents[name] = data
            tree = ET.fromstring(data)
            for t in tree.iter(f'{{{W}}}t'):
                if t.text:
                    all_text.append(t.text)
    full_text = ' '.join(all_text)
    if language is None:
        language = detect_language(full_text)
        if language:
            print(f'Auto-detected header/footer language: {language}')
        else:
            print('No translatable text detected in headers/footers.')
            return False
    tmap = LANGUAGE_MAPS.get(language.lower())
    if not tmap:
        print(f"No translation map for language '{language}'.")
        return False
    total_changes = 0
    written_files = []
    for name, data in file_contents.items():
        translated_data, changes = translate_xml(data, tmap)
        if translated_data:
            out_path = os.path.join(output_dir, name)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, 'wb') as f:
                f.write(translated_data)
            written_files.append(name)
            total_changes += len(changes)
            print(f'\n{name}:')
            for c in changes:
                print(c)
    if total_changes:
        print(f'\nTranslated {total_changes} item(s) across {len(written_files)} file(s).')
        print(f'Written: {", ".join(written_files)}')
    else:
        print('\nNo translatable text found in headers/footers (all numeric/symbol content).')
    return total_changes > 0

# ──────────────────────────────────────────────────────────────────────
# CLI dispatch.
# ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=(
            'Translate word/headerN.xml and word/footerN.xml files. '
            'Prefer --extract + --apply (scaffold round-trip); fall back '
            'to --language (legacy dictionary lookup) only for watermark-only '
            'documents.'
        )
    )
    parser.add_argument('original', help='Original .docx file')
    parser.add_argument(
        'output_dir', nargs='?', default=None,
        help='Output directory (required for --apply and --language modes)',
    )
    parser.add_argument(
        '--extract', metavar='SCAFFOLD_JSON',
        help='Extract header/footer paragraphs to a JSON scaffold for translation',
    )
    parser.add_argument(
        '--apply', metavar='SCAFFOLD_JSON',
        help='Apply a filled-in scaffold back to translated header/footer XMLs',
    )
    parser.add_argument(
        '--language',
        help=(
            'Legacy dictionary-lookup mode. Source language: hungarian, '
            'italian, german, french, spanish, portuguese, dutch, polish, finnish.'
        ),
        default=None,
    )
    args = parser.parse_args()

    # Validate mutually-exclusive modes.
    modes = [bool(args.extract), bool(args.apply), bool(args.language)]
    if sum(modes) == 0:
        parser.error(
            'choose one of --extract, --apply, or --language. '
            'Recommended: --extract then (after translating the JSON) --apply.'
        )
    if sum(modes) > 1:
        parser.error('--extract, --apply, and --language are mutually exclusive.')

    if args.extract:
        # Surface the same English-passthrough rule the body translator
        # already follows, at the moment the operator is about to decide
        # what to write into the scaffold. No detection, no tagging —
        # just a reminder. If a header/footer paragraph is already in
        # English, copy it verbatim into "en" (or leave it null, which
        # also preserves verbatim); do not rewrite or polish.
        print(
            'REMINDER: If a header/footer below is already in English, copy the\n'
            "source into 'en' verbatim. Do not rewrite or polish — the parties\n"
            'wrote those words and will read them back.\n'
        )
        ok = extract_to_scaffold(args.original, args.extract)
        sys.exit(0 if ok else 1)

    if args.apply:
        if not args.output_dir:
            parser.error('--apply requires the output_dir positional argument.')
        ok = apply_from_scaffold(args.original, args.apply, args.output_dir)
        sys.exit(0 if ok else 1)

    # Legacy --language mode
    if not args.output_dir:
        parser.error('--language requires the output_dir positional argument.')
    translate_headers_footers_legacy(args.original, args.output_dir, language=args.language)

# === SKILL FILE COMPLETE ===
