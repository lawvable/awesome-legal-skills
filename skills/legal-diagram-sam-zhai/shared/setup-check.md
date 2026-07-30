# Setup check (shared)

Session-cached dependency check. Called by `tutorial.md`, `direct.md`, `extract.md`.

## Procedure

1. **Cache first.** If `_setup_ok = true` set this session → skip script. Return ok.
2. **Run script.** `python scripts/check_setup.py`. Parse JSON: `{ok, python_version, installed[], missing[], optional{}}`. The `optional` key lists optional packages with `installed`, `pip_name`, and `purpose`; their absence does not affect `ok`.
3. **On `ok=true`.** Log installed packages. Set `_setup_ok = true`. Return ok.
4. **On `missing` non-empty.** Print exact missing list plus one install line:
   `pip install -r requirements.txt -c constraints.txt`
   - Tutorial mode: halt. "Re-run after installing."
   - Direct mode: one-line message. Offer pasted-text fallback (extraction from `.md`/text needs no third-party deps).
5. **On crash (non-zero exit, no JSON).** Python missing from PATH. Print: "Python not found. Ensure Python 3.9+ installed and on PATH." Do not attempt workaround.
6. **On degenerate `ok=true, installed=[]`.** Warn: "dependency list empty but no errors." Proceed with caution.

## Notes

- Only `.docx`/`.pdf`/`.pptx`/`.xlsx` parsing and HTML export need third-party libs. `.md`, `.txt`, pasted text, and conversation context run on stdlib alone; missing dep never blocks those paths.
- Cache key per session, not per call. Never re-run script after a clean pass.
