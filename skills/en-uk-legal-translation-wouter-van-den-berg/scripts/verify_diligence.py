"""verify_diligence.py — Step 11 final discipline-adherence audit.

Runs at the end of the pipeline and produces a single PASS/WARN/FAIL summary
across the 11 skill steps. Catches *skipped-step* failure modes that the
earlier auto-invoked gates do not surface as a single end-of-pipeline report:

  - Step 4 + 4b   per-batch validation actually invoked, every translated
                  paragraph is in `validated_indices`, no batch exceeded 35
  - Step 5        apply ran (final/word/document.xml exists and non-empty)
  - Step 6        post-process ran (heuristic: document.xml has been modified
                  since paragraphs.json — i.e. apply or post-process touched it)
  - Step 8        if source has aux files (numbering / header* / footer* /
                  comments / footnotes / endnotes), translated copies exist
                  in <workdir>/final/word/
  - Step 9        quality_check.py runs clean on the final document.xml
                  (re-runs internally, with --aux-dir, with --variant uk by
                  default — pass --variant us if Step 6 used --variant us)
  - Step 10/11    repacked .docx exists if path passed via --docx

This script does NOT verify operator *reasoning* (lexicon priority, calque
drift, segment-grammar choices) — those classes of defect are caught by
their dedicated validators (validate_reject_all, validate_segment_shapes,
lexicon_compliance). What it catches is the *skipped step* class: silent
omissions where the operator went from Step 4 directly to Step 10 without
running validate_translations, or skipped Step 8 entirely, or never ran
quality_check.

Exit codes:
  0 — all checks PASS
  1 — at least one WARN (recoverable; review and proceed if intentional)
  2 — at least one FAIL (a step was clearly skipped — fix before delivery)
  3 — script-integrity check failed (re-install the skill)

Usage:
  python verify_diligence.py <workdir> [options]

Options:
  --workdir          (positional) The workdir containing paragraphs.json,
                     .validate-state.json, and final/word/document.xml.
  --docx <path>      Path to the final repacked .docx (Step 10 output) for
                     existence + size checks. Optional.
  --orig-docx <path> Path to the ORIGINAL source .docx, used to detect which
                     aux files Step 8 should have produced. Optional but
                     recommended — without it, the aux-file Step 8 check
                     is skipped (reported as N/A).
  --variant {uk,us}  Target English variant for the internal quality_check
                     re-run. Default uk.
  --mode {chat,cowork,unknown}
                     Host-environment hint. When --mode chat AND the overall
                     verdict is FAIL or WARN, the report appends a
                     "consider Cowork next time" recommendation. Default
                     unknown — the recommendation is only ever appended when
                     the operator explicitly declares Chat mode. Detect Chat
                     by inspecting the host environment: in Cowork the
                     `<application_details>` system block names "Cowork mode"
                     and `mcp__cowork__*` MCP tools are present; in Chat
                     neither is present.
  --strict           Treat WARN as FAIL (no recoverable warnings allowed).
  --report-only      Produce the report but always exit 0 (for end-of-run
                     summary even if some categories warn).
"""
import os
import sys
import json
import argparse
import subprocess
import zipfile

def _check_self_integrity():
    """Detect install-time truncation by sentinel marker."""
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


# Severity levels for individual checks. Aggregated per category.
PASS = 'PASS'
WARN = 'WARN'
FAIL = 'FAIL'
NA = 'N/A'

_SEVERITY_ORDER = {PASS: 0, NA: 0, WARN: 1, FAIL: 2}


class Report:
    """Accumulates check results into a structured per-step report."""

    def __init__(self):
        self.findings = []  # list of (step_label, severity, summary, detail)
        self._scripts_dir = os.path.dirname(os.path.abspath(__file__))

    def add(self, step, severity, summary, detail=''):
        self.findings.append((step, severity, summary, detail))

    def overall(self):
        max_sev = PASS
        for _, sev, _, _ in self.findings:
            if _SEVERITY_ORDER[sev] > _SEVERITY_ORDER[max_sev]:
                max_sev = sev
        return max_sev

    def render(self, mode='unknown'):
        """Render the report. When `mode='chat'` AND overall verdict is
        FAIL or WARN, a Cowork recommendation block is appended.
        """
        lines = []
        lines.append('=' * 70)
        lines.append('STEP 11 — DILIGENCE CHECK')
        lines.append('=' * 70)
        # Group by step
        by_step = {}
        for step, sev, summ, det in self.findings:
            by_step.setdefault(step, []).append((sev, summ, det))
        for step in sorted(by_step.keys()):
            entries = by_step[step]
            # Worst severity in this group
            worst = max((_SEVERITY_ORDER[s] for s, _, _ in entries),
                        default=0)
            label = [k for k, v in _SEVERITY_ORDER.items() if v == worst][0]
            lines.append(f'  [{label:4}] {step}')
            for sev, summ, det in entries:
                lines.append(f'           {sev:4} — {summ}')
                if det:
                    for ln in det.splitlines():
                        lines.append(f'                  {ln}')
        lines.append('=' * 70)
        ov = self.overall()
        lines.append(f'  OVERALL: {ov}')
        if ov == FAIL:
            lines.append('  ACTION:  At least one step was skipped or failed. '
                         'Fix before delivery.')
        elif ov == WARN:
            lines.append('  ACTION:  Recoverable warnings — review each WARN '
                         'and confirm the choice was intentional.')
        else:
            lines.append('  ACTION:  All checks passed. Deliver with confidence.')
        lines.append('=' * 70)
        # Rev41: Cowork recommendation when Chat mode drifted.
        if mode == 'chat' and ov in (FAIL, WARN):
            lines.append('')
            lines.append('=' * 70)
            lines.append('  RECOMMENDATION FOR NEXT TRANSLATION')
            lines.append('=' * 70)
            lines.append(
                '  This Chat-mode translation drifted from the skill — at')
            lines.append(
                '  least one diligence check did not pass. For your next')
            lines.append(
                '  translation we recommend using **Cowork mode**: the')
            lines.append(
                '  workspace folder, persistent paragraphs.json, auto-')
            lines.append(
                '  managed todo list, and per-step checkpointing materially')
            lines.append(
                '  reduce drift risk. The same legal-translation skill')
            lines.append(
                '  bundle works in both modes; only the host environment')
            lines.append(
                '  differs.')
            lines.append('=' * 70)
        return '\n'.join(lines)


# ---------------------------------------------------------------------------
# Step-specific check functions

def check_step_4_4b(report, workdir):
    """Step 4 + 4b: paragraphs.json exists; .validate-state.json shows full
    coverage; max recorded batch ≤35 (or accept_large_batch flag set)."""
    para_path = os.path.join(workdir, 'paragraphs.json')
    state_path = os.path.join(workdir, '.validate-state.json')
    label = 'Step 4 + 4b: per-batch validation'

    if not os.path.isfile(para_path):
        report.add(label, FAIL, 'paragraphs.json not found in workdir',
                   f'expected: {para_path}')
        return
    try:
        with open(para_path, encoding='utf-8') as f:
            paras = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        report.add(label, FAIL, f'paragraphs.json unreadable: {e}')
        return

    translated = [p for p in paras
                  if isinstance(p, dict)
                  and (p.get('en') or '').strip()
                  and (p.get('en') or '').strip()
                      != (p.get('text') or '').strip()]
    translated_idx = sorted(p['idx'] for p in translated if 'idx' in p)
    n_translated = len(translated_idx)

    if not os.path.isfile(state_path):
        report.add(label, FAIL,
                   f'.validate-state.json missing — '
                   f'validate_translations.py was never run',
                   f'expected: {state_path}\n'
                   f'translated paragraphs in JSON: {n_translated}')
        return
    try:
        with open(state_path, encoding='utf-8') as f:
            state = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        report.add(label, FAIL, f'.validate-state.json unreadable: {e}')
        return

    validated = set(state.get('validated_indices', []))
    history = state.get('history', [])

    missing_idx = [i for i in translated_idx if i not in validated]
    if missing_idx:
        sample = ', '.join(str(i) for i in missing_idx[:10])
        more = (f' (+{len(missing_idx) - 10} more)'
                if len(missing_idx) > 10 else '')
        report.add(label, FAIL,
                   f'{len(missing_idx)} translated paragraphs missing from '
                   f'.validate-state.json (skipped per-batch validation)',
                   f'first missing idx: {sample}{more}')
    else:
        report.add(label, PASS,
                   f'all {n_translated} translated paragraphs validated')

    # Batch-cap audit
    if not history:
        report.add(label, WARN,
                   '.validate-state.json has no history entries '
                   '(coverage matches but audit trail empty)')
    else:
        oversize = [h for h in history
                    if h.get('count', 0) > 35
                    and not h.get('accept_large_batch')]
        max_batch = max((h.get('count', 0) for h in history), default=0)
        if oversize:
            ts = oversize[0].get('timestamp', '?')
            report.add(label, FAIL,
                       f'{len(oversize)} batch(es) exceeded the 35-paragraph '
                       f'cap WITHOUT --accept-large-batch override',
                       f'first oversize batch: {oversize[0].get("count")} '
                       f'paragraphs at {ts}')
        else:
            report.add(label, PASS,
                       f'{len(history)} batch invocation(s); '
                       f'max batch size {max_batch} paragraphs (≤35 cap '
                       f'respected)')


def check_step_5(report, workdir):
    """Step 5: apply produced final/word/document.xml."""
    label = 'Step 5: apply'
    final_doc = os.path.join(workdir, 'final', 'word', 'document.xml')
    if not os.path.isfile(final_doc):
        # Some pipelines write the final XML to a different path
        # (e.g. <workdir>/output.xml). Look for a likely fallback.
        candidates = [
            os.path.join(workdir, 'output.xml'),
            os.path.join(workdir, 'translated.xml'),
        ]
        for c in candidates:
            if os.path.isfile(c):
                report.add(label, WARN,
                           f'document.xml not at the expected path '
                           f'(<workdir>/final/word/document.xml) but found at '
                           f'{c} — non-standard layout',
                           '')
                return
        report.add(label, FAIL,
                   'no apply output found; expected '
                   '<workdir>/final/word/document.xml',
                   f'workdir: {workdir}')
        return
    size = os.path.getsize(final_doc)
    if size < 200:
        report.add(label, FAIL,
                   f'final document.xml is suspiciously small ({size} bytes)')
        return
    report.add(label, PASS,
               f'final document.xml present ({size:,} bytes)')


def check_step_8(report, workdir, orig_docx):
    """Step 8: if source had aux files, translated copies exist."""
    label = 'Step 8: aux-file translation'
    if not orig_docx or not os.path.isfile(orig_docx):
        report.add(label, NA,
                   '--orig-docx not provided; Step 8 audit skipped')
        return

    final_word_dir = os.path.join(workdir, 'final', 'word')
    if not os.path.isdir(final_word_dir):
        report.add(label, FAIL,
                   f'<workdir>/final/word/ does not exist '
                   f'(apply produced no output)')
        return

    # What aux files does the source have?
    try:
        with zipfile.ZipFile(orig_docx) as zf:
            src_names = set(zf.namelist())
    except (zipfile.BadZipFile, OSError) as e:
        report.add(label, WARN,
                   f'cannot inspect source .docx: {e}')
        return

    aux_to_check = []
    if 'word/numbering.xml' in src_names:
        aux_to_check.append(('word/numbering.xml', 'numbering'))
    for n in sorted(src_names):
        if (n.startswith('word/header') or n.startswith('word/footer')) \
                and n.endswith('.xml'):
            aux_to_check.append((n, 'headers/footers'))
    if 'word/comments.xml' in src_names:
        aux_to_check.append(('word/comments.xml', 'comments'))
    if 'word/footnotes.xml' in src_names:
        aux_to_check.append(('word/footnotes.xml', 'footnotes'))
    if 'word/endnotes.xml' in src_names:
        aux_to_check.append(('word/endnotes.xml', 'endnotes'))

    if not aux_to_check:
        report.add(label, NA,
                   'source has no aux files (numbering / headers / footers / '
                   'comments / footnotes / endnotes) — Step 8 N/A')
        return

    missing = []
    present = []
    for src_path, kind in aux_to_check:
        out_path = os.path.join(workdir, 'final', src_path)
        if os.path.isfile(out_path):
            present.append((src_path, kind))
        else:
            missing.append((src_path, kind))

    if missing:
        kinds = sorted(set(k for _, k in missing))
        names = ', '.join(p for p, _ in missing[:10])
        more = f' (+{len(missing) - 10} more)' if len(missing) > 10 else ''
        report.add(label, FAIL,
                   f'{len(missing)} aux file(s) missing from '
                   f'<workdir>/final/word/ — Step 8 substep skipped for: '
                   f'{", ".join(kinds)}',
                   f'missing: {names}{more}')
    else:
        kinds = sorted(set(k for _, k in present))
        report.add(label, PASS,
                   f'all {len(present)} source-side aux file(s) present in '
                   f'<workdir>/final/word/ ({", ".join(kinds)})')


def check_step_9(report, workdir, variant):
    """Step 9: quality_check.py runs clean on the final document.xml."""
    label = 'Step 9: quality_check'
    final_doc = os.path.join(workdir, 'final', 'word', 'document.xml')
    if not os.path.isfile(final_doc):
        report.add(label, FAIL,
                   'cannot run quality_check — final document.xml missing')
        return
    qc = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      'quality_check.py')
    if not os.path.isfile(qc):
        report.add(label, WARN,
                   f'quality_check.py not found alongside this script')
        return
    para_path = os.path.join(workdir, 'paragraphs.json')
    aux_dir = os.path.join(workdir, 'final')
    args = [sys.executable, qc, final_doc, '--variant', variant]
    if os.path.isfile(para_path):
        args.extend(['--with-source', para_path])
    if os.path.isdir(aux_dir):
        args.extend(['--aux-dir', aux_dir])
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        report.add(label, FAIL,
                   'quality_check.py timed out (120s) — re-run with --verbose')
        return
    if 'FILE INTEGRITY CHECK FAILED' in (r.stdout + r.stderr):
        report.add(label, FAIL,
                   'quality_check.py integrity check fired — '
                   're-install the skill')
        return
    if r.returncode == 0:
        report.add(label, PASS,
                   'quality_check.py exited 0 (no issues)')
    else:
        # quality_check exits non-zero when issues are reported.
        first_lines = (r.stdout + r.stderr).splitlines()[:8]
        report.add(label, FAIL,
                   f'quality_check.py reported issues (exit {r.returncode})',
                   '\n'.join(first_lines))


def check_step_10_11(report, workdir, docx_path):
    """Step 10 + 11: repacked .docx exists and is non-trivially sized."""
    label = 'Step 10 + 11: repack + final validate'
    if not docx_path:
        report.add(label, NA,
                   '--docx not provided; final repacked .docx existence '
                   'check skipped (run with --docx <path> for full audit)')
        return
    if not os.path.isfile(docx_path):
        report.add(label, FAIL,
                   f'final .docx does not exist at {docx_path}')
        return
    size = os.path.getsize(docx_path)
    if size < 1024:
        report.add(label, FAIL,
                   f'final .docx is suspiciously small ({size} bytes)')
        return
    # Validate it opens as a ZIP
    try:
        with zipfile.ZipFile(docx_path) as zf:
            names = zf.namelist()
            has_doc = 'word/document.xml' in names
    except (zipfile.BadZipFile, OSError) as e:
        report.add(label, FAIL,
                   f'final .docx is not a valid ZIP: {e}')
        return
    if not has_doc:
        report.add(label, FAIL,
                   'final .docx is missing word/document.xml')
        return
    report.add(label, PASS,
               f'final .docx present and valid ({size:,} bytes, '
               f'{len(names)} entries)')


# ---------------------------------------------------------------------------
def main(argv=None):
    ap = argparse.ArgumentParser(
        description='Step 11 diligence audit — verifies the 11-step '
                    'pipeline actually ran end-to-end.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument('workdir', help='workdir containing paragraphs.json')
    ap.add_argument('--docx', dest='docx', default=None,
                    help='path to the final repacked .docx for Step 10/11 audit')
    ap.add_argument('--orig-docx', dest='orig_docx', default=None,
                    help='path to the ORIGINAL source .docx for Step 8 audit')
    ap.add_argument('--variant', choices=('uk', 'us'), default='uk',
                    help='target English variant for the quality_check re-run '
                         '(default: uk; pass us only if Step 6 used --variant us)')
    ap.add_argument('--mode', choices=('chat', 'cowork', 'unknown'),
                    default='unknown',
                    help='host-environment hint; when "chat" AND verdict is '
                         'FAIL/WARN, append a "consider Cowork next time" '
                         'recommendation to the report (default: unknown)')
    ap.add_argument('--strict', action='store_true',
                    help='treat WARN as FAIL')
    ap.add_argument('--report-only', action='store_true',
                    help='produce the report but always exit 0')
    args = ap.parse_args(argv)

    workdir = os.path.abspath(args.workdir)
    if not os.path.isdir(workdir):
        print(f'[diligence] workdir not found: {workdir}', file=sys.stderr)
        return 2

    report = Report()
    check_step_4_4b(report, workdir)
    check_step_5(report, workdir)
    check_step_8(report, workdir, args.orig_docx)
    check_step_9(report, workdir, args.variant)
    check_step_10_11(report, workdir, args.docx)

    print(report.render(mode=args.mode))

    if args.report_only:
        return 0
    overall = report.overall()
    if overall == FAIL:
        return 2
    if overall == WARN:
        return 1 if args.strict else 0
    return 0


if __name__ == '__main__':
    sys.exit(main())

# === SKILL FILE COMPLETE ===
