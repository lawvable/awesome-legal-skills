#!/usr/bin/env python3
"""
fetch_icsid_award.py - identify, confirm, and extract an ICSID decision/award.

Part of the ISDS Research skill. Compliant, on-demand, single-document
retrieval from ICSID (icsid.worldbank.org / icsidfiles.worldbank.org) for
personal, non-commercial research. Does NOT mirror or redistribute.

TWO-STEP, IDENTIFY-BEFORE-YOU-DOWNLOAD FLOW
-------------------------------------------
A single case page can list dozens of documents (award, decisions on
jurisdiction, rectification, annulment, dissents, procedural orders) in several
languages. Grabbing "the first English PDF" is unsafe. So:

  1) LIST    parse the case-detail page into a structured table of every
             published document: proceeding, title, date, and one row per
             available language + URL.
               python fetch_icsid_award.py --case "ARB(AF)/00/2" --list

  2) SELECT  download ONE chosen document, print its first page(s) so the
             caller can CONFIRM it is the intended document (title, parties,
             case number, date), then extract paragraph-aware text / run a query.
               python fetch_icsid_award.py --case "ARB(AF)/00/2" --select 1 \
                   --query "fair and equitable treatment"

LANGUAGE IS AN ATTRIBUTE, NOT A FILTER
--------------------------------------
Awards are frequently available only in Spanish/French/etc.; a non-English award
is a valid, relevant result. Selection ranks by a preferred-language list but
never discards other languages. When the preferred language is unavailable it
falls back to the ORIGINAL-language version and flags that any rendering into the
preferred language would be the assistant's OWN translation (to be labelled as
such). The preferred language is asked once (first run) and stored in a config
file together with the research-folder root (where each topic's memo and
retrieved PDFs are saved); pass --set-prefer-lang / --set-research-root to
record them and --show-config to read them. If the default config location
(beside the script) is not writable -- installed skill folders are commonly
mounted read-only -- the script reports that cleanly (never a traceback) and
the caller passes a writable --config path instead (see SKILL.md, "First run").

Requires: requests, pdfplumber   ->   pip install requests pdfplumber

Why a script (not just web_fetch)? web_fetch truncates very long PDFs (~120k
chars), dropping later paragraphs of a 80-90 page award. Downloading the file and
extracting with pdfplumber gives full, paragraph-numbered coverage.
"""

import argparse
import json
import os
import re
import shutil
import sys
import tempfile
import time
from urllib.parse import quote

import requests

try:
    import pdfplumber
except ImportError:
    sys.exit("Missing dependency: pip install pdfplumber")

UA = ("isds-research-skill/1.1.0 (personal, non-commercial research; "
      "on-demand single-document retrieval)")
HEADERS = {"User-Agent": UA}
CASE_DETAIL = "https://icsid.worldbank.org/cases/case-database/case-detail?CaseNo={}"
DISCLAIMER = "For research only; not legal advice. Verify against the official primary source."


def attribution(url=None, pdf_file=None, source_url=None):
    """Source-aware attribution: institution line chosen by host, plus the URL
    the PDF was actually retrieved from (or local-file provenance)."""
    ref = source_url or url
    host = ""
    if ref:
        m = re.match(r"https?://([^/]+)", ref)
        host = (m.group(1) if m else "").lower()
    if "worldbank.org" in host or "icsid" in host:
        line = ("Source: International Centre for Settlement of Investment Disputes. "
                "Available at https://icsid.worldbank.org.")
    elif "pca-cpa.org" in host:
        line = ("Source: Permanent Court of Arbitration. Available at https://pca-cpa.org. "
                "Used for non-commercial research.")
    elif host:
        line = f"Source: {host}. Verify the issuing institution and its terms of use."
    else:
        line = "Source: user-supplied file; issuing institution not verified from a URL."
    if pdf_file and not source_url:
        line += f"\nLocal file (user-supplied): {pdf_file} — record the official download URL " \
                f"with --source-url for provenance."
    elif ref:
        line += f"\nRetrieved from: {ref}"
    return line

# Config lives beside the script by default (standalone/local use, where the folder
# is writable). Installed skill folders are often mounted READ-ONLY: --show-config
# reports CONFIG_DIR_WRITABLE up front so callers can detect that before any failed
# write, and keep the config instead at a user-chosen writable location passed via
# --config on every call (suggested filename outside the skill folder below).
DEFAULT_CONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user-config.json")
EXTERNAL_CONFIG_NAME = "isds-research-config.json"

PARA_RE = re.compile(r"^\s*(\d{1,3})\.\s")          # paragraph markers like "154. "
BRACKET_PARA_RE = re.compile(r"^\s*\[(\d{1,4})\]\s")  # bracketed markers like "[324] " (e.g. Iberdrola v. Guatemala)


def para_marker(line, rx):
    """Match a paragraph marker with the document's detected convention regex.
    Returns (number, line_with_marker_stripped) or None."""
    m = rx.match(line)
    if m:
        return int(m.group(1)), rx.sub("", line, count=1)
    return None


def detect_marker_convention(page_texts):
    """Pick the document's paragraph-marker convention: "154. " vs "[324] ".

    Documents use ONE convention for operative paragraphs; matching both at once
    lets the wrong one win locally (e.g. Iberdrola: a "N."-style table of contents
    gets tagged ¶1–13 before the real bracketed "[1]" markers begin, shadowing
    them). So we count raw line-initial candidates for each convention across the
    whole document and use only the dominant one. Ties/absence default to "N. "
    (the ICSID norm)."""
    dotted = bracket = 0
    for text in page_texts:
        for line in text.split("\n"):
            if PARA_RE.match(line):
                dotted += 1
            elif BRACKET_PARA_RE.match(line):
                bracket += 1
    return (BRACKET_PARA_RE, "[N] ") if bracket > dotted else (PARA_RE, "N. ")
# All-caps structural headings that legitimise a paragraph-numbering restart
# (per-Part/Chapter numbering, e.g. Methanex Final Award). Uppercase-only match:
# title-case running footers ("Part II - Chapter B - Page 6") must NOT match.
HEADING_RE = re.compile(
    r"^(?:ANNEX\s+\w+\s+TO\s+)?"
    r"(?:PART\s+[IVXLCDM0-9]+|CHAPTER\s+[A-Z0-9]+|SECTION\s+[A-Z0-9]+|"
    r"ANNEX\s+\w+|APPENDIX\s+\w+)\b[^a-z]*$")
TAG_RE = re.compile(r"<(h3|h4|p)\b[^>]*>(.*?)</\1>", re.S | re.I)
SPAN_RE = re.compile(r"<span[^>]*>(.*?)</span>", re.S | re.I)
A_PDF_RE = re.compile(r'<a\b[^>]*href="([^"]+?\.pdf)"[^>]*>(.*?)</a>', re.S | re.I)
DATE_RE = re.compile(r"\(([^()]*\b\d{4}\b[^()]*)\)")
CASENO_RE = re.compile(r"(ARB(?:\s*\(AF\))?/\d{2}/\d{1,2}|UNCT/[A-Z0-9/]+|CONC/\d{2}/\d+)", re.I)

LANG_CODES = {
    "english": "en", "spanish": "es", "french": "fr", "arabic": "ar",
    "german": "de", "portuguese": "pt", "russian": "ru", "chinese": "zh",
    "italian": "it", "dutch": "nl",
}


# --------------------------------------------------------------------------- #
# Config (preferred language, asked once on first run)
# --------------------------------------------------------------------------- #
def load_config(path):
    try:
        with open(path) as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


def save_config(path, cfg):
    with open(path, "w") as fh:
        json.dump(cfg, fh, indent=2)


def config_writable(path):
    """Can `path` be (re)written? Checks the file itself if it exists, else its
    parent directory. os.access reflects read-only mounts (EROFS) as well as
    permissions, so this detects an installed skill's read-only folder without
    side effects."""
    p = os.path.abspath(path)
    if os.path.exists(p):
        return os.access(p, os.W_OK)
    parent = os.path.dirname(p) or "."
    return os.path.isdir(parent) and os.access(parent, os.W_OK)


# --------------------------------------------------------------------------- #
# HTTP
# --------------------------------------------------------------------------- #
def polite_get(url, **kw):
    """GET with a descriptive UA and a courtesy delay (respect the host)."""
    time.sleep(1.0)
    r = requests.get(url, headers=HEADERS, timeout=60, **kw)
    r.raise_for_status()
    return r


def fail_fetch(url, what, exc):
    """Print a clean FETCH FAILED block (no traceback) and exit 5.

    Mirrors the CONFIG NOT SAVED contract: a network failure is an expected,
    documented outcome with a next step, never a stack trace.
    """
    print("\n===== FETCH FAILED (host unreachable or refused the request) =====")
    print(f"While: {what}")
    print(f"Tried: {url}")
    print(f"Error: {exc.__class__.__name__}: {exc}")
    print("Do NOT retry the same fetch blindly, do NOT fetch the document by hand,\n"
          "and NEVER substitute an unofficial mirror. Diagnose first: run --check-env\n"
          "to see which source hosts this environment can reach. If egress to this\n"
          "host is blocked, or the host refuses this client (e.g. HTTP 403), follow\n"
          "the Retrieval fallback ladder in SKILL.md: a JS-capable browser render of\n"
          "the case page plus --doc-url (rung 2), or a user-supplied copy of the\n"
          "official document via --pdf-file <path> --source-url <official URL>\n"
          "(rung 3). The CONFIRM identity check still runs on every fallback route.")
    print("=====")
    sys.exit(5)


# --------------------------------------------------------------------------- #
# Parse the case page into a structured document table
# --------------------------------------------------------------------------- #
def _strip(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


def lang_code(label):
    low = label.lower()
    for name, code in LANG_CODES.items():
        if name in low:
            return code
    return None


def parse_documents(html):
    """Return an ordered list of document records parsed from the case page.

    Each record: {index, proceeding, subsection, title, date, languages:[{
        language, lang_code, original, translated, url}]}.
    Only <p> blocks that actually contain a downloadable PDF link are kept.
    """
    m = re.search(r'<div id="materials"[^>]*>(.*?)(?=<div id="[^"]+" class="tab-pane|\Z)',
                  html, re.S | re.I)
    materials = m.group(1) if m else html

    docs, proceeding, subsection, idx = [], None, None, 0
    for t in TAG_RE.finditer(materials):
        tag, inner = t.group(1).lower(), t.group(2)
        if tag == "h3":
            proceeding, subsection = _strip(inner), None
        elif tag == "h4":
            subsection = _strip(inner)
        else:  # <p>
            links = A_PDF_RE.findall(inner)
            if not links:
                continue
            span = SPAN_RE.search(inner)
            title_raw = _strip(span.group(1)) if span else _strip(inner)
            dm = DATE_RE.search(title_raw)
            date = dm.group(1).strip() if dm else None
            title = _strip(DATE_RE.sub("", title_raw)).strip(" ();,")
            langs = []
            for url, label in links:
                label = _strip(label)
                langs.append({
                    "language": label,
                    "lang_code": lang_code(label),
                    "original": "original" in label.lower(),
                    "translated": "translat" in label.lower(),
                    "url": url,
                })
            idx += 1
            docs.append({
                "index": idx, "proceeding": proceeding, "subsection": subsection,
                "title": title or title_raw, "date": date, "languages": langs,
            })
    return docs


def print_document_table(docs):
    for d in docs:
        head = f"[{d['index']}] {d['title']}"
        if d["date"]:
            head += f" — {d['date']}"
        if d["proceeding"]:
            head += f"   ({d['proceeding']})"
        print(head)
        for lg in d["languages"]:
            print(f"        - {lg['language']:<22} -> {lg['url']}")
    print("\n--- machine-readable ---")
    print("JSON_DOCS=" + json.dumps(docs, ensure_ascii=False))


# --------------------------------------------------------------------------- #
# Language selection
# --------------------------------------------------------------------------- #
def match_language(langs, token):
    """Return the language dict whose label/code matches token, else None."""
    w = (token or "").strip().lower()
    if not w:
        return None
    for lg in langs:
        if w in lg["language"].lower() or w == (lg["lang_code"] or ""):
            return lg
    return None


def resolve_language(doc, prefer, have_pref, explicit):
    """Decide which language version to retrieve.

    Returns (status, chosen_or_None, available_labels) where status is:
      'ok'     -> proceed with chosen version
      'choose' -> preferred language unavailable (or none set + multiple exist):
                  do NOT substitute; ask the user which listed language to use
      'none'   -> no versions, or an explicit --lang that isn't available
    """
    langs = doc["languages"]
    labels = [lg["language"] for lg in langs]
    if not langs:
        return "none", None, labels
    if explicit:
        lg = match_language(langs, explicit)
        return ("ok", lg, labels) if lg else ("none", None, labels)
    for want in prefer:
        lg = match_language(langs, want)
        if lg:
            return "ok", lg, labels
    if have_pref:
        return "choose", None, labels          # preferred not available -> ask the user
    if len(langs) == 1:
        return "ok", langs[0], labels          # nothing to choose
    return "choose", None, labels              # no preference + multiple versions -> ask


def print_language_choice(doc, prefer, have_pref, prefer_display, labels):
    """Report that the document isn't in the preferred language and ask how to proceed.

    Deliberately does NOT download anything: the caller must ask the user, because
    the ICSID page does not always make clear which language is authoritative, and
    the user may prefer an existing ICSID translation over an assistant translation.
    """
    print("\n===== LANGUAGE CHOICE NEEDED (do not auto-substitute) =====")
    head = f"Document: [{doc['index']}] {doc['title']}"
    if doc.get("date"):
        head += f" ({doc['date']})"
    print(head)
    if have_pref:
        want = prefer_display or (prefer[0] if prefer else "your preferred language")
        print(f"Preferred language ({want}) is NOT available for this document on the ICSID website.")
    else:
        print("No preferred language is on record and this document exists in more than one language.")
    print("Available on the ICSID website:")
    for l in labels:
        print(f"  - {l}")
    print("The page labels show original vs. translation where given, but do not always establish which\n"
          "language is authoritative. ASK THE USER how to proceed: read one of the versions listed above\n"
          "(e.g. an existing ICSID translation), or have the assistant translate the original itself\n"
          "(its own translation, which is NOT authoritative).")
    print(f'Then re-run with the choice:  --select {doc["index"]} --lang "<language>"')
    print("=====")


# --------------------------------------------------------------------------- #
# PDF text extraction
# --------------------------------------------------------------------------- #
def extract_paragraphs(pdf_path, max_forward_gap=8, heading_window=8):
    """Return [{page, para, text, section, section_label}] with hardened paragraph
    detection, including per-Part/Chapter numbering restarts.

    ISDS decisions usually number paragraphs sequentially (1, 2, 3, … N), in one of
    two marker conventions: "154. " or bracketed "[324] " (e.g. Iberdrola v.
    Guatemala). The document's dominant convention is detected in a pre-scan and
    ONLY that convention is matched (see detect_marker_convention) — matching both
    at once lets the wrong one win locally (a "N."-style table of contents would
    shadow the real "[1]"–"[13]" markers). A bare marker regex also matches stray
    numbers — footnote markers, page/running-header digits, and numbered items
    inside quoted statutes/treaties — which were previously mis-tagged as
    paragraphs (e.g. a spurious "¶28" sitting between ¶308 and ¶313).

    Hardening 1 (sequential window): a candidate marker is accepted as a real
    paragraph only if its number is the next expected one, or a small forward step
    within `max_forward_gap` (tolerating a few markers the extractor missed).
    Numbers below what we've already reached, or a large jump ahead, are rejected —
    those lines are kept as ordinary text so no content is lost.

    Hardening 2 (numbering restarts — the Methanex pathology): some
    awards restart paragraph numbering per Part/Chapter (e.g. Methanex Final Award,
    2005). A document-wide `expected` counter rejects every post-restart marker and
    collapses whole chapters into unnumbered blocks. Fix: a candidate "1." that
    breaks the sequence is accepted as a NEW SECTION only when an all-caps
    structural heading (PART …/CHAPTER …/SECTION …/ANNEX … TO …) appeared within
    the last `heading_window` lines. Heading-confirmed restarts reset `expected`;
    cites become section-relative and carry the heading verbatim (page footers like
    "Part II - Chapter B - Page 6" are title-case and thus excluded). Restart-like
    markers WITHOUT a confirming heading (quoted rules/statutes) stay rejected.

    Residual limits (documented, tunable): a numbered list quoted early in a
    section whose values fall inside the forward window can still be misread; a run
    of >max_forward_gap genuinely missed markers will desync until the next
    confirmed section heading; restarts under heading conventions this regex does
    not recognize are NOT recovered — the caller is warned when the rejection
    pattern suggests that (see main). The required verification step (re-checking
    each cited ¶ against the text) is the backstop.
    """
    items = []
    expected = 1        # next paragraph number expected within the current section
    section = 1
    section_label = None
    last_heading, since_heading = None, 10 ** 9
    rejected_restart_candidates = 0   # "1." after progress, no confirming heading
    with pdfplumber.open(pdf_path) as pdf:
        page_texts = [(p.extract_text() or "") for p in pdf.pages]
    marker_rx, marker_style = detect_marker_convention(page_texts)
    if marker_style != "N. ":
        print(f"[*] Paragraph-marker convention detected: {marker_style!r}", file=sys.stderr)
    for pageno, text in enumerate(page_texts, start=1):
        cur_para, buf = None, []
        for line in text.split("\n"):
            stripped = line.strip()
            if HEADING_RE.match(stripped) and len(stripped) <= 60:
                last_heading, since_heading = stripped, 0
            else:
                since_heading += 1
            pm = para_marker(line, marker_rx)
            if pm:
                n, stripped_line = pm
                in_window = expected <= n <= expected + max_forward_gap
                is_restart = (not in_window and n == 1 and expected > 1
                              and last_heading is not None
                              and since_heading <= heading_window)
                if in_window or is_restart:
                    if buf:
                        items.append({"page": pageno, "para": cur_para,
                                      "text": " ".join(buf).strip(),
                                      "section": section,
                                      "section_label": section_label})
                        buf = []
                    if is_restart:
                        section += 1
                        section_label = last_heading
                    elif (cur_para is None and section == 1
                          and section_label is None
                          and since_heading <= heading_window):
                        section_label = last_heading  # first section's heading
                    cur_para = n
                    expected = cur_para + 1
                    line = stripped_line
                elif n == 1 and expected > 1:
                    rejected_restart_candidates += 1
            buf.append(line.strip())
        if buf:
            items.append({"page": pageno, "para": cur_para,
                          "text": " ".join(buf).strip(),
                          "section": section,
                          "section_label": section_label})
    return items, rejected_restart_candidates


def first_pages(pdf_path, n):
    """Return (joined_text, total_pages) for the first n pages."""
    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)
        text = "\n".join((p.extract_text() or "") for p in pdf.pages[:n])
    return text, total


def cite(it, multi_section=False):
    """Pin-cite for an extracted block. In a document with confirmed numbering
    restarts, paragraph numbers are only meaningful WITHIN a section, so the cite
    carries the section heading verbatim (fallback: a section ordinal)."""
    base = f"para {it['para']} (p.{it['page']})" if it["para"] else f"p.{it['page']}"
    if multi_section and it["para"]:
        label = it.get("section_label") or f"section {it.get('section', '?')}"
        return f"{label}, {base}"
    return base


# --------------------------------------------------------------------------- #
# Environment check
# --------------------------------------------------------------------------- #
def check_env(config_path):
    """--check-env: report dependencies, network egress to each source host, and
    config writability, so the caller can choose the full pipeline or a degraded
    mode (see SKILL.md, "Platform notes") BEFORE the first retrieval fails
    mid-answer. Never raises; exit code 0 = PASS, 4 = DEGRADED."""
    ok = True
    print("===== ISDS-RESEARCH ENVIRONMENT CHECK =====")
    print(f"python            : {sys.version.split()[0]}")
    for mod, note in (("requests", "required (HTTP retrieval)"),
                      ("pdfplumber", "required (PDF text extraction)"),
                      ("openpyxl", "optional (UNCTAD Excel enumeration)")):
        try:
            m = __import__(mod)
            print(f"dep  {mod:<13}: OK {getattr(m, '__version__', '')}".rstrip())
        except ImportError:
            if mod == "openpyxl":
                print(f"dep  {mod:<13}: WARN missing - {note}; pip install {mod}")
            else:
                ok = False
                print(f"dep  {mod:<13}: FAIL missing - {note}; pip install {mod}")
    probes = (
        ("icsid.worldbank.org", "case pages",
         "https://icsid.worldbank.org/cases/case-database/case-detail?CaseNo=ARB/07/30"),
        ("icsidfiles.worldbank.org", "document PDFs",
         "https://icsidfiles.worldbank.org/icsid/ICSIDBLOBS/OnlineAwards/C259/DS11957_En.pdf"),
        ("investmentpolicy.unctad.org", "UNCTAD Navigator",
         "https://investmentpolicy.unctad.org/"),
        ("pca-cpa.org", "PCA case pages", "https://pca-cpa.org/en/cases/"),
    )
    for host, what, url in probes:
        try:
            r = requests.get(url, headers={**HEADERS, "Range": "bytes=0-2047"},
                             timeout=15, stream=True)
            status = r.status_code
            r.close()
            if status in (200, 206):
                print(f"net  {host:<27}: OK HTTP {status} ({what})")
            else:
                print(f"net  {host:<27}: WARN HTTP {status} ({what}) - host reachable; "
                      f"non-200 may be bot protection or a moved probe URL")
        except Exception as exc:
            ok = False
            print(f"net  {host:<27}: FAIL {type(exc).__name__}: {exc}")
        time.sleep(0.5)
    print(f"config path       : {os.path.abspath(config_path)}")
    writable = config_writable(config_path)
    print(f"config writable   : "
          f"{'yes' if writable else 'NO - choose a writable --config path (SKILL.md, First run)'}")
    cfg = load_config(config_path)
    print(f"config present    : "
          f"{json.dumps(cfg, ensure_ascii=False) if cfg else 'no (run the first-run interview)'}")
    rr = cfg.get("research_root")
    if rr:
        state = ("OK" if (os.path.isdir(rr) and os.access(rr, os.W_OK))
                 else "MISSING/UNWRITABLE - re-ask the user")
        print(f"research_root     : {rr} [{state}]")
    print("VERDICT: " + ("PASS - full retrieval pipeline available" if ok else
                         "DEGRADED - use the fallback modes in SKILL.md 'Platform notes'"))
    print("===== END ENVIRONMENT CHECK =====")
    return 0 if ok else 4


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description="Identify, confirm, and extract an ICSID award/decision.")
    ap.add_argument("--case", help="ICSID case number, e.g. ARB(AF)/00/2")
    ap.add_argument("--case-url", help="ICSID case-detail URL")
    ap.add_argument("--list", action="store_true", help="list all documents on the case page, then stop")
    ap.add_argument("--select", type=int, help="1-based index (from --list) of the document to retrieve")
    ap.add_argument("--doc-url", help="explicit PDF URL to retrieve (skips index selection)")
    ap.add_argument("--pdf-file", help="local PDF path to use instead of downloading (e.g. a user-supplied "
                    "document from a host this environment cannot reach); still confirmed and extracted normally")
    ap.add_argument("--source-url", help="with --pdf-file: the official URL the user downloaded the PDF from "
                    "(recorded in the attribution line for provenance)")
    ap.add_argument("--lang", help="explicit language version for the selected document (e.g. 'english' or 'es'); "
                                   "use after the user chooses when the preferred language isn't available")
    ap.add_argument("--prefer-lang", help="preferred language ranking, e.g. 'english,spanish' or 'en,es'")
    ap.add_argument("--query", default=None, help="phrase to locate in the selected document")
    ap.add_argument("--save-pdf", help="also save the downloaded PDF to this path (research-folder "
                    "convention: '<folder>/<Short name>, <Inst> <case-no with hyphens>, <Short title>, "
                    "<YYYY-MM-DD>.pdf'); parent folders are created")
    ap.add_argument("--confirm-pages", type=int, default=2, help="leading pages to show for confirmation")
    ap.add_argument("--max-chars", type=int, default=2000, help="max chars per printed passage")
    ap.add_argument("--config", default=DEFAULT_CONFIG, help="path to preferences config json")
    ap.add_argument("--set-prefer-lang", help="record a preferred language in the config and exit")
    ap.add_argument("--set-research-root", help="record where research folders (each topic's memo + "
                    "retrieved PDFs) are saved; may be combined with --set-prefer-lang")
    ap.add_argument("--show-config", action="store_true", help="print the stored preferences and exit")
    ap.add_argument("--check-env", action="store_true", help="check dependencies, network egress to the "
                    "source hosts, and config writability; print a PASS/DEGRADED report and exit")
    args = ap.parse_args()

    # --- config-only operations ---------------------------------------------
    if args.check_env:
        sys.exit(check_env(args.config))
    if args.set_prefer_lang or args.set_research_root:
        cfg = load_config(args.config)
        if args.set_prefer_lang:
            cfg["preferred_language"] = args.set_prefer_lang
        if args.set_research_root:
            cfg["research_root"] = args.set_research_root
        try:
            save_config(args.config, cfg)
        except OSError as exc:
            print("\n===== CONFIG NOT SAVED (location not writable) =====")
            print(f"Tried: {os.path.abspath(args.config)}")
            print(f"Error: {exc}")
            print("This location cannot store preferences (typical cause: an installed skill\n"
                  "folder mounted read-only). Do NOT retry the same path, and do NOT drop the\n"
                  "user's answer. ASK THE USER where preferences should live (suggested\n"
                  "default: the root of their ISDS research area -- the same place research\n"
                  "folders are saved), then re-run with a writable path, e.g.:\n"
                  f'  --config "<research area>/{EXTERNAL_CONFIG_NAME}" '
                  '--set-prefer-lang "..." [--set-research-root "..."]\n'
                  "and pass that same --config on EVERY later call, in this and future sessions.")
            print("=====")
            sys.exit(3)
        recorded = ", ".join(f"{k} = {cfg[k]!r}"
                             for k in ("preferred_language", "research_root") if k in cfg)
        print(f"Recorded {recorded} in {os.path.abspath(args.config)}")
        return
    if args.show_config:
        cfg = load_config(args.config)
        writable = config_writable(args.config)
        print(f"CONFIG_PATH={os.path.abspath(args.config)}")
        print(f"CONFIG_DIR_WRITABLE={'yes' if writable else 'no'}")
        if cfg:
            print(json.dumps(cfg, ensure_ascii=False))
        else:
            print("NO_CONFIG (first run: ask the user (1) their preferred language and "
                  "(2) where research folders and preferences should be saved -- see "
                  'SKILL.md, "First run")')
        if not writable:
            print("# NOTE: this config location is NOT writable (installed skill folders often "
                  "are read-only).\n# Store preferences at a user-chosen writable location and "
                  f'pass --config "<folder>/{EXTERNAL_CONFIG_NAME}" on every call.')
        return

    if not (args.case or args.case_url or args.doc_url or args.pdf_file):
        ap.error("provide --case or --case-url (or --doc-url to fetch a specific PDF, "
                 "or --pdf-file for a local PDF).")

    cfg = load_config(args.config)
    if args.prefer_lang is not None:
        prefer = [p for p in args.prefer_lang.split(",") if p.strip()]
        have_pref = True
    elif cfg.get("preferred_language"):
        prefer = [cfg["preferred_language"]]
        have_pref = True
    else:
        prefer, have_pref = [], False

    # --- resolve the target document ----------------------------------------
    chosen_url, chosen_doc, chosen_lang = args.doc_url, None, None

    if not chosen_url and not args.pdf_file:
        case_url = args.case_url or CASE_DETAIL.format(quote(args.case, safe="()/"))
        print(f"[1] Case page: {case_url}", file=sys.stderr)
        try:
            page = polite_get(case_url).text
        except requests.RequestException as exc:
            fail_fetch(case_url, "fetching the case page (document list)", exc)
        docs = parse_documents(page)
        if not docs:
            sys.exit("No documents parsed from the case page. Do NOT guess a URL. The page may be "
                     "JS-rendered or restructured: retry via a JS-capable browser render (e.g. Claude "
                     "in Chrome, or the assistant's browsing mode) or open the case page "
                     "manually and pass --doc-url.")
        if args.list or not args.select:
            print(f"[2] {len(docs)} document(s) found:", file=sys.stderr)
            print_document_table(docs)
            if not args.select:
                print("\nNext: choose the right document by title/date, then re-run with "
                      "--select <n> (add --query to search it).", file=sys.stderr)
            return
        if args.select < 1 or args.select > len(docs):
            sys.exit(f"--select {args.select} out of range (1..{len(docs)}).")
        chosen_doc = docs[args.select - 1]
        status, chosen_lang, labels = resolve_language(chosen_doc, prefer, have_pref, args.lang)
        if status == "none":
            if args.lang:
                sys.exit(f'--lang "{args.lang}" is not available for this document. '
                         f'Available: {", ".join(labels) or "none"}.')
            sys.exit("This document has no downloadable language versions listed.")
        if status == "choose":
            print_language_choice(chosen_doc, prefer, have_pref, args.prefer_lang, labels)
            return
        chosen_url = chosen_lang["url"]
        print(f"[2] Selected [{chosen_doc['index']}] {chosen_doc['title']}"
              f"{' — ' + chosen_doc['date'] if chosen_doc['date'] else ''} "
              f"[{chosen_lang['language']}]", file=sys.stderr)

    if args.pdf_file:
        print(f"[3] Local PDF (user-supplied): {args.pdf_file}", file=sys.stderr)
    else:
        print(f"[3] Document PDF: {chosen_url}", file=sys.stderr)

    # --- obtain the PDF (download, or use local file), confirm, extract -----
    with tempfile.TemporaryDirectory() as td:
        if args.pdf_file:
            if not os.path.exists(args.pdf_file):
                sys.exit(f"ERROR: --pdf-file not found: {args.pdf_file}")
            pdf_path = args.pdf_file
        else:
            pdf_path = os.path.join(td, "doc.pdf")
            try:
                with polite_get(chosen_url, stream=True) as r:
                    with open(pdf_path, "wb") as fh:
                        for chunk in r.iter_content(8192):
                            fh.write(chunk)
            except requests.RequestException as exc:
                fail_fetch(chosen_url, "downloading the document PDF", exc)

        confirm_text, total_pages = first_pages(pdf_path, args.confirm_pages)
        print(f"[4] Downloaded ({total_pages} pages). Extracting text...", file=sys.stderr)

        # ---- CONFIRMATION block (verify this is the intended document) ----
        print("\n===== CONFIRM THIS IS THE RIGHT DOCUMENT =====")
        if chosen_doc:
            print(f"Case-page label : {chosen_doc['title']}"
                  f"{' (' + chosen_doc['date'] + ')' if chosen_doc['date'] else ''}")
            print(f"Proceeding      : {chosen_doc.get('proceeding') or '-'}")
        if chosen_lang:
            print(f"Language        : {chosen_lang['language']}")
        print(f"Total pages     : {total_pages}")
        if confirm_text.strip():
            found = CASENO_RE.findall(confirm_text)
            if found:
                print(f"Case no. in text: {found[0]}")
            print(f"--- first {args.confirm_pages} page(s), first 1200 chars ---")
            print(confirm_text.strip()[:1200])
        else:
            print("[!] First pages have NO extractable text (likely a scanned image). "
                  "Cannot auto-confirm; the file may need OCR or manual verification before you rely on it.")
        print("===== END CONFIRMATION =====\n")

        items, rejected_restarts = extract_paragraphs(pdf_path)

        if args.save_pdf:
            dest = os.path.abspath(args.save_pdf)
            os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
            shutil.copyfile(pdf_path, dest)
            print(f"[*] PDF saved to: {dest}", file=sys.stderr)

    print(f"[5] Extracted {len(items)} paragraph blocks.", file=sys.stderr)

    # --- numbering-restart reporting -----------------------------------------
    n_sections = max((it["section"] for it in items), default=1)
    multi_section = n_sections > 1
    if multi_section:
        print(f"[!] Paragraph numbering RESTARTS in this document: {n_sections} sections "
              f"detected via structural headings. Paragraph cites below are SECTION-RELATIVE "
              f"(heading quoted verbatim, e.g. 'PART IV - CHAPTER D, para 7'). Always give the "
              f"section alongside the paragraph number; verify each heading against the document.")
        for lbl in dict.fromkeys((it["section_label"] or f"section {it['section']}")
                                 for it in items):
            print(f"      - {lbl}")
    numbered = sum(1 for it in items if it["para"])
    if rejected_restarts >= 3 and numbered < max(1, len(items)) // 2:
        print(f"[!] WARNING: most extracted blocks carry NO paragraph number, and "
              f"{rejected_restarts} restart-like markers ('1.'/'[1]' after progress) were rejected "
              f"for lack of a recognized structural heading. The document's paragraph markers may "
              f"follow a convention this script does not recognize (recognized: 'N. ' and '[N] '), "
              f"or numbering may restart under unrecognized headings. Do NOT trust the paragraph "
              f"cites here: fall back to page-based cites or a visual (rasterized) check.")

    # --- optional query -----------------------------------------------------
    if args.query:
        q = args.query.lower()
        hits = [it for it in items if q in it["text"].lower()]
        if not hits:
            print(f'\nNo passage matching "{args.query}" found in the retrieved document. '
                  f'Report this honestly; do NOT answer from memory.')
        for it in hits:
            print(f"\n--- {cite(it, multi_section)} ---\n{it['text'][:args.max_chars]}")
    else:
        for it in items:
            print(f"[{cite(it, multi_section)}] {it['text'][:200]}")

    print(f"\n{attribution(url=chosen_url, pdf_file=args.pdf_file, source_url=args.source_url)}\n{DISCLAIMER}")


if __name__ == "__main__":
    main()
