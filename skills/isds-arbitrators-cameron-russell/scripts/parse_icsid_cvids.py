#!/usr/bin/env python3
"""Build a name -> cvid map from a user-saved copy of the ICSID
'Arbitrators, Conciliators and Ad Hoc Committee Members' listing page
(PDF print with live link annotations). The cvid link is anchored on the
'CV' cell; the person's name sits on the same visual row. Local-use only;
the map is not shipped (ICSID no-derivative-works term)."""
import glob, json, re, sys
from pypdf import PdfReader
import pdfplumber

CVID_RE = re.compile(r"profile\?cvid=(\d+)")
SKIP = {"cv", "case", "count:", "count"}
out, conflicts, unnamed = {}, [], 0

for f in sorted(glob.glob(sys.argv[1] if len(sys.argv) > 1 else "*.pdf")):
    reader = PdfReader(f)
    with pdfplumber.open(f) as pdf:
        for ppg, wpg in zip(reader.pages, pdf.pages):
            annots = ppg.get("/Annots")
            if annots is None:
                continue
            annots = annots.get_object()
            words = wpg.extract_words()
            H = float(wpg.height)
            for a in annots:
                o = a.get_object()
                act = o.get("/A")
                if not act:
                    continue
                act = act.get_object()
                m = CVID_RE.search(str(act.get("/URI") or ""))
                if not m:
                    continue
                cvid = m.group(1)
                x0, y0, x1, y1 = [float(v) for v in o["/Rect"]]
                top, bottom = H - y1, H - y0
                mid = (top + bottom) / 2
                # words on the same visual row (vertical midpoint inside word box)
                row = [w for w in words if w["top"] - 3 <= mid <= w["bottom"] + 3]
                name_words = [w["text"] for w in sorted(row, key=lambda w: w["x0"])
                              if w["text"].lower() not in SKIP
                              and not w["text"].isdigit()]
                name = " ".join(name_words).strip()
                if not name:
                    unnamed += 1
                    continue
                if name in out and out[name] != cvid:
                    conflicts.append((name, out[name], cvid))
                out[name] = cvid

print(f"entries: {len(out)}; conflicts: {len(conflicts)}; cvid links w/o name: {unnamed}",
      file=sys.stderr)
for c in conflicts[:15]:
    print("CONFLICT:", c, file=sys.stderr)
json.dump(dict(sorted(out.items())), open("icsid-cvid-map.json", "w"),
          indent=1, ensure_ascii=False)
