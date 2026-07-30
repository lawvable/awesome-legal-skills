"""legal-cite — logika weryfikacji brzmienia przepisu z OFICJALNEGO źródła.

Pobiera dokładny tekst cytowanego artykułu (api.sejm.gov.pl dla prawa PL,
EUR-Lex dla prawa UE) i zwraca TYLKO ten artykuł — nie cały akt. Akty są
cache'owane w obrębie sesji procesu. AKTUALNE brzmienie (tekst jednolity),
nie pierwotne z dnia ogłoszenia.
"""
from __future__ import annotations

import html as _html
import re

import httpx

# --- Akty PL → ELI: api.sejm.gov.pl/eli/acts/{pub}/{year}/{pos}/text.html ---
# pos = pozycja w Dzienniku Ustaw (poz. N)
PL_ACTS: dict[str, dict] = {
    "KC":       dict(pub="DU", year=1964, pos=93,   name="Kodeks cywilny"),
    "KP":       dict(pub="DU", year=1974, pos=141,  name="Kodeks pracy"),
    "KSH":      dict(pub="DU", year=2000, pos=1037, name="Kodeks spółek handlowych"),
    "KPC":      dict(pub="DU", year=1964, pos=296,  name="Kodeks postępowania cywilnego"),
    "KK":       dict(pub="DU", year=1997, pos=553,  name="Kodeks karny"),
    "PrAut":    dict(pub="DU", year=1994, pos=83,   name="Prawo autorskie i prawa pokrewne"),
    "u.r.p.":   dict(pub="DU", year=1982, pos=145,  name="Ustawa o radcach prawnych"),
    "u.ś.u.d.e.": dict(pub="DU", year=2002, pos=1204, name="Ustawa o świadczeniu usług drogą elektroniczną"),
    "u.z.n.k.": dict(pub="DU", year=1993, pos=211,  name="Ustawa o zwalczaniu nieuczciwej konkurencji"),
    "u.p.k.":   dict(pub="DU", year=2014, pos=827,  name="Ustawa o prawach konsumenta"),
    "UODO":     dict(pub="DU", year=2018, pos=1000, name="Ustawa o ochronie danych osobowych"),
    # sprawy kredytu konsumenckiego / SKD: art. 45 sankcja kredytu darmowego, art. 30 obowiązki
    "u.k.k.":   dict(pub="DU", year=2011, pos=715,  name="Ustawa o kredycie konsumenckim"),
    "UKK":      dict(pub="DU", year=2011, pos=715,  name="Ustawa o kredycie konsumenckim"),
}

# --- Akty UE → EUR-Lex (tekst polski), klucz = CELEX ---
EU_ACTS: dict[str, dict] = {
    "RODO":   dict(celex="32016R0679", name="Rozporządzenie 2016/679 (RODO/GDPR)"),
    "DSA":    dict(celex="32022R2065", name="Rozporządzenie 2022/2065 (DSA)"),
    "AI Act": dict(celex="32024R1689", name="Rozporządzenie 2024/1689 (AI Act)"),
    "AIA":    dict(celex="32024R1689", name="Rozporządzenie 2024/1689 (AI Act)"),
    "NIS2":   dict(celex="32022L2555", name="Dyrektywa 2022/2555 (NIS2)"),
    "DGA":    dict(celex="32022R0868", name="Rozporządzenie 2022/868 (DGA)"),
    "DMA":    dict(celex="32022R1925", name="Rozporządzenie 2022/1925 (DMA)"),
    # sprawy kredytu konsumenckiego / SKD: dyrektywa o kredycie konsumenckim
    "CCD":          dict(celex="32008L0048", name="Dyrektywa 2008/48/WE (kredyt konsumencki)"),
    "2008/48":      dict(celex="32008L0048", name="Dyrektywa 2008/48/WE (kredyt konsumencki)"),
    "dyrektywa 2008/48": dict(celex="32008L0048", name="Dyrektywa 2008/48/WE (kredyt konsumencki)"),
}

_HEADERS = {"User-Agent": "legal-cite/0.1 (+https://github.com/apiotrowski-afk/legal-cite-pl)"}

# cache per-proces: klucz aktu → tekst (strip HTML) całego aktu
_cache: dict[str, str] = {}


def _resolve(act: str, table: dict) -> str | None:
    """Dopasowuje kod aktu odpornie na końcowe kropki i wielkość liter
    (u.k.k./u.k.k/UKK → ten sam akt)."""
    if act in table:
        return act
    norm = act.lower().rstrip('.')
    idx = {k.lower().rstrip('.'): k for k in table}
    return idx.get(norm)


_SUP = str.maketrans("¹²³⁴⁵⁶⁷⁸⁹⁰", "1234567890")


def parse_citation(raw: str) -> dict | None:
    """Parsuje cytat: 'art. N[a][¹] [ust./§ M] [pkt/lit. X] KOD' → {art, ustep, act}.
    Obsługuje sufiks literowy (36a), indeks górny (385¹/385[1]/385(1)) i § jako
    jednostkę redakcyjną (KC numeruje paragrafami)."""
    m = re.match(
        r'(?:art\.|§)\s*'
        r'(\d+[a-z]?(?:\s*(?:[¹²³⁴⁵⁶⁷⁸⁹]+|\[\d+\]|\(\d+\)|\^\d+))?)\s*'  # numer art. + opc. indeks
        r'(?:(?:ust\.|§)\s*(\d+\w?))?\s*'                                 # ustęp ALBO paragraf
        r'(?:(?:pkt|lit\.)\s*\S+\s*)?(.+)',                               # pkt/lit ignorowane; kod aktu
        raw.strip(), re.IGNORECASE,
    )
    if not m:
        return None
    return {
        "art": m.group(1).strip(),
        "ustep": m.group(2),
        "act": m.group(3).strip().rstrip('.').strip(),
    }


def _art_regex(raw_art: str) -> str:
    """Buduje fragment regex dopasowujący numer artykułu w tekście źródła,
    tolerancyjnie na spacje. 385¹→'385\\s+1' (źródło: „Art. 385 1 ."),
    36a→'36\\s*a', 45→'45'."""
    s = re.sub(r'([¹²³⁴⁵⁶⁷⁸⁹⁰]+)', lambda mm: ' ' + mm.group(1).translate(_SUP), raw_art.strip())
    s = re.sub(r'\s*[\[\(\^]\s*(\d+)\s*[\]\)]?', r' \1', s)  # [1]/(1)/^1 → " 1"
    s = re.sub(r'\s+', ' ', s).strip()
    parts = s.split(' ')
    if len(parts) == 2 and parts[1].isdigit():               # baza + indeks górny
        return rf'{re.escape(parts[0])}\s+{re.escape(parts[1])}'
    mlet = re.match(r'^(\d+)([a-zA-Z])$', parts[0])
    if mlet:                                                  # sufiks literowy 36a
        return rf'{mlet.group(1)}\s*{mlet.group(2)}'
    return re.escape(parts[0])


def _strip_html(raw_html: str) -> str:
    # 1) usuń <script>/<style> WRAZ z treścią — api.sejm.gov.pl wstrzykuje strukturę
    #    aktu jako JSON w <script>, inaczej kradłby dopasowanie nagłówka „Art. N.".
    raw_html = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', ' ', raw_html,
                      flags=re.IGNORECASE | re.DOTALL)
    # 2) strip tagów → 3) DEKODUJ encje (kluczowe: nagłówki to „Art.&nbsp;45." —
    #    &nbsp; to twarda spacja \xa0; po unescape regex „Art.\s*N." łapie) →
    # 4) zwiń białe znaki (w tym \xa0) do zwykłej spacji.
    text = re.sub(r'<[^>]+>', ' ', raw_html)
    text = _html.unescape(text)
    return re.sub(r'\s+', ' ', text).strip()


async def _fetch_pl(info: dict) -> str | None:
    """Pobiera AKTUALNY tekst aktu (tekst jednolity), nie pierwotny z dnia
    ogłoszenia. api.sejm `/text.html` pod pozycją oryginału zwraca brzmienie
    pierwotne (np. KC 1964 — „PRL", bez art. 385¹). Dlatego z metadanych bierzemy
    najnowszy tekst jednolity z dostępnym HTML; oryginał = fallback."""
    key = f"PL:{info['pub']}:{info['year']}:{info['pos']}"
    if key in _cache:
        return _cache[key]
    base = "https://api.sejm.gov.pl/eli/acts"
    async with httpx.AsyncClient(follow_redirects=True, timeout=25, headers=_HEADERS) as c:
        positions: list[tuple] = []
        try:
            meta = (await c.get(f"{base}/{info['pub']}/{info['year']}/{info['pos']}")).json()
            for ent in (meta.get("references") or {}).get("Inf. o tekście jednolitym", []):
                parts = (ent.get("id") or "").split("/")
                if len(parts) == 3:
                    positions.append(tuple(parts))  # (pub, year, pos) tekstu jednolitego
        except (httpx.HTTPError, ValueError, KeyError):
            pass
        positions = positions[:4]  # najnowsze TJ (świeże bywają bez HTML — pomijamy puste)
        positions.append((info["pub"], str(info["year"]), str(info["pos"])))  # fallback oryginał
        for pub, year, pos in positions:
            try:
                resp = await c.get(f"{base}/{pub}/{year}/{pos}/text.html")
            except Exception:
                continue
            if resp.status_code == 200 and len(resp.text) > 3000:
                text = _strip_html(resp.text)
                if len(text) > 1500:
                    _cache[key] = text
                    return text
    return None


async def _fetch_eu(info: dict) -> str | None:
    key = f"EU:{info['celex']}"
    if key in _cache:
        return _cache[key]
    url = (f"https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/"
           f"?uri=CELEX:{info['celex']}")
    async with httpx.AsyncClient(follow_redirects=True, timeout=30, headers=_HEADERS) as c:
        resp = await c.get(url)
    if resp.status_code != 200:
        return None
    _cache[key] = _strip_html(resp.text)
    return _cache[key]


def _cut_ustep(art_text: str, ustep: str) -> str | None:
    # ustęp „N." LUB paragraf „§ N." (KC); granica = następna jednostka tej samej rangi
    m = re.search(rf'(?:§\s*)?(?<!\d){re.escape(ustep)}\.\s', art_text)
    if not m:
        return None
    ust_start = m.start()
    nxt = re.search(r'(?:§\s*)?(?<!\d)\d+\.\s', art_text[m.end():])
    ust_end = m.end() + nxt.start() if nxt else len(art_text)
    return art_text[ust_start:ust_end].strip()


def extract_pl_article(text: str, art: str, ustep: str | None) -> str | None:
    frag = _art_regex(art)
    m = None
    # Tekst jednolity zawiera fragmenty ustaw zmieniających z własnymi numerami
    # artykułów. Dwa filtry łącznie:
    #  1. Case-sensitive: nagłówki artykułów w PL aktach to „Art. N." (wielka A);
    #     odesłania w tekście to „art. N." (mała a) — np. „ustawy zmienianej w art. 8."
    #  2. Cudzysłów: cytaty z ustaw zmieniających zapisywane jako „ Art. N." —
    #     sprawdzamy 120 znaków wstecz; jeśli poprzedza je „/"/stanowią → pomijamy.
    for prefix in (rf'Art\.\s*{frag}\s*\.', rf'§\s*{frag}\s*\.'):
        for candidate in re.finditer(prefix, text):  # case-sensitive (brak IGNORECASE)
            pre = text[max(0, candidate.start() - 120):candidate.start()]
            if re.search(r'[„„"\']|stanowi[ąa][\s:„"\']', pre):
                continue  # wewnątrz cytatu z ustawy zmieniającej
            m = candidate
            break
        if m:
            break
    if m is None:
        return None
    nxt = re.search(r'\b(?:Art\.|§)\s*\d+', text[m.end():])
    end = m.end() + nxt.start() if nxt else min(m.start() + 4000, len(text))
    art_text = text[m.start():end].strip()
    return _cut_ustep(art_text, ustep) if ustep else art_text


def extract_eu_article(text: str, art: str, ustep: str | None) -> str | None:
    m = re.search(rf'\bArtykuł\s+{re.escape(art)}\b', text, re.IGNORECASE)
    if not m:
        return None
    nxt = re.search(r'\bArtykuł\s+\d+\b', text[m.end():], re.IGNORECASE)
    end = m.end() + nxt.start() if nxt else min(m.start() + 5000, len(text))
    art_text = text[m.start():end].strip()
    return _cut_ustep(art_text, ustep) if ustep else art_text


async def verify_article(citation: str) -> str:
    """Zwraca dokładne brzmienie cytowanego przepisu ze źródła oficjalnego.
    Format: 'art. N [ust. M] KOD' (np. 'art. 45 u.k.k.', 'art. 28 ust. 3 RODO')."""
    parsed = parse_citation(citation)
    if not parsed:
        return (f"❌ Nierozpoznany format: '{citation}'\n"
                f"Użyj: 'art. N [ust. M] KOD' — np. 'art. 45 u.k.k.'\n"
                f"Lista kodów: list_acts().")
    act, art, ustep = parsed["act"], parsed["art"], parsed["ustep"]
    ref = f"art. {art}" + (f" ust. {ustep}" if ustep else "")
    pl_key = _resolve(act, PL_ACTS)
    eu_key = _resolve(act, EU_ACTS)

    if pl_key:
        info = PL_ACTS[pl_key]
        try:
            text = await _fetch_pl(info)
        except httpx.TimeoutException:
            return f"❌ Timeout pobierania {info['name']} z api.sejm.gov.pl"
        if text is None:
            return f"❌ Nie udało się pobrać {info['name']} (sieć/ELI)"
        result = extract_pl_article(text, art, ustep)
        if not result:
            return f"❌ {ref} nie znaleziony w {info['name']}. Sprawdź numer artykułu."
        return f"📜 **{info['name']}**, {ref}\n(źródło: api.sejm.gov.pl)\n\n{result}"

    if eu_key:
        info = EU_ACTS[eu_key]
        try:
            text = await _fetch_eu(info)
        except httpx.TimeoutException:
            return f"❌ Timeout pobierania {info['name']} z EUR-Lex"
        if text is None:
            return f"❌ Nie udało się pobrać {info['name']} z EUR-Lex"
        result = extract_eu_article(text, art, ustep)
        if not result:
            return f"❌ {ref} nie znaleziony w {info['name']}. Sprawdź numer artykułu."
        return f"📜 **{info['name']}**, {ref}\n(źródło: EUR-Lex, PL)\n\n{result}"

    known = ", ".join(dict.fromkeys(list(PL_ACTS) + list(EU_ACTS)))
    return f"❌ Nieznany kod aktu: '{act}'\nObsługiwane: {known}"


def list_acts() -> str:
    """Lista obsługiwanych kodów aktów z pełnymi nazwami."""
    pl = "\n".join(f"  {k:<16} → {v['name']}" for k, v in PL_ACTS.items())
    eu = "\n".join(f"  {k:<16} → {v['name']}" for k, v in EU_ACTS.items())
    return ("📚 Obsługiwane kody aktów\n\n"
            f"Prawo PL (api.sejm.gov.pl):\n{pl}\n\n"
            f"Prawo UE (EUR-Lex, PL):\n{eu}")
