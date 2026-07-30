# Source Manifest — Article 50 Transparency Assessor

Audit-grade provenance for every authority this skill relies on. Because the skill stands on **post-cutoff**
soft law (the Jun-2026 Code, the May-2026 draft Guidelines, the EU icon set, the Digital Omnibus grace),
each source below carries an official URL, a legal-status flag, a **last-checked date**, and a *supersedes*
note. On activation, re-verify the **draft / pending** rows and stamp the live status into the report's
**Source-status block** (see [report-template-art50.md](report-template-art50.md)).

> **Last full manifest check:** 2026-07-04. Statuses change month to month — treat any date-flagged row as
> stale until re-checked, and prefer the newer official source if a web result conflicts.

---

## Uncertainty tiers (used throughout the skill's output)

| Marker | Meaning | Instruments here |
|--------|---------|------------------|
| **Settled law** | Black-letter, in force / adopted | Regulation (EU) 2024/1689, Art. 50; Art. 99(4) penalty |
| **Draft guidance** | Commission interpretation, non-binding, not yet final | Art. 50 Guidelines (draft 8 May 2026) |
| **Technical best practice** | Voluntary Code; adherence ≠ conclusive evidence | Code of Practice (final 10 Jun 2026); EU icon set |
| **Open issue** | Adopted-but-unpublished / pending assessment / no CJEU ruling | Digital Omnibus (awaiting OJ); CoP adequacy assessment; any Art. 50 interpretation (CJEU has not ruled) |

---

## Primary law

| Source | Status | Official URL | Last checked | Notes |
|--------|--------|--------------|--------------|-------|
| **Regulation (EU) 2024/1689 (AI Act)** — Art. 50, Art. 3(60), Art. 96(1)(d), Art. 99(4)(g), Art. 113 | **In force** (settled law) | `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689` | 2026-07-04 | Art. 50 **applies from 2 Aug 2026** (Art. 113 general date). Penalty **Art. 99(4)(g)** = up to €15M / 3% (€750k for EU bodies). |

## Digital Omnibus (Omnibus VII on AI) — the 50(2) legacy grace

| Source | Status | Official URL | Last checked | Notes |
|--------|--------|--------------|--------------|-------|
| **Council press release — "final green light"** (29 Jun 2026) | **Adopted by Council; awaiting OJ** (open issue) | `https://www.consilium.europa.eu/en/press/press-releases/2026/06/29/artificial-intelligence-council-gives-final-green-light-to-simplify-and-streamline-rules/` | 2026-07-04 | Confirms the 50(2) grace: grace cut from 6→3 months, **new deadline 2 Dec 2026**. "Published in the OJ **shortly**; enters into force on the **3rd day after** publication." **Supersedes** the "politically agreed 7 May 2026 / conditional" framing. |
| **Digital Omnibus on AI — adopted text (PE-30-2026-INIT)** | Adopted text | `https://data.consilium.europa.eu/doc/document/PE-30-2026-INIT/en/pdf` | 2026-07-04 | Also: high-risk application deferred to 2 Dec 2027 (standalone) / 2 Aug 2028 (embedded); new Art. 5 prohibition on non-consensual intimate / CSAM deepfakes (from Dec 2026); sandbox deadline → 2 Aug 2027; single adequacy-assessment procedure. |
| **EU Law tracker (procedure 2025/359)** | Live tracker | `https://law-tracker.europa.eu/procedure/2025_359?lang=en` | 2026-07-04 | Use to confirm the **OJ publication date** on activation. |

## Code of Practice on Transparency of AI-Generated Content

| Source | Status | Official URL | Last checked | Notes |
|--------|--------|--------------|--------------|-------|
| **Code of Practice — policy page** | **Final (10 Jun 2026); voluntary; under adequacy assessment** (technical best practice / open issue) | `https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content` | 2026-07-04 | Covers only **50(2), 50(4), 50(5)**. Adequacy assessment by Commission + AI Board **still pending**; signatures are **conditional** on a positive assessment (Art. 50(7) → 56(6)). |
| **Code of Practice — full text (PDF)** | Final text | `https://ec.europa.eu/newsroom/dae/redirection/document/129555` | 2026-07-04 | The authoritative wording for the two-layer marking rule, the 200-token text threshold, detection, and Section 2 labelling. |
| **Signing the Code — FAQ + signature form** | Live | `https://digital-strategy.ec.europa.eu/en/faqs/signing-code-practice-transparency-ai-generated-content` · form DOCX `https://ec.europa.eu/newsroom/dae/redirection/document/129548` | 2026-07-04 | **Initial-signatory deadline 22 Jul 2026, 18:00 CEST** (list published before 2 Aug 2026); later signing allowed. Sign Section 1 (providers) and/or Section 2 (deployers) — whole sections, not individual commitments. |

## Commission Guidelines on Article 50

| Source | Status | Official URL | Last checked | Notes |
|--------|--------|--------------|--------------|-------|
| **Draft Art. 50 Guidelines (8 May 2026)** | **Draft** (draft guidance) | `https://digital-strategy.ec.europa.eu/en/library/draft-guidelines-implementation-transparency-obligations-certain-ai-systems-under-article-50-ai-act` | 2026-07-04 | Issued under **Art. 96(1)(d)**; covers **all** of Art. 50. **Consultation closed 3 Jun 2026**; finalisation expected before 2 Aug 2026 but **not yet final**. Para. references used in this skill: 12, 17, 23–24, 28, 35, 40–42, 54, 64, 65, 70, 81, 82, 98, 107–116, 140–141. |

## EU labelling icon set (Code Section 2, Annex 1)

| Source | Status | Official URL | Last checked | Notes |
|--------|--------|--------------|--------------|-------|
| **EU Icons for labelling AI-generated content** | Published (technical best practice; **optional**) | `https://digital-strategy.ec.europa.eu/en/policies/eu-icons-labelling-ai-generated-content` | 2026-07-04 | **Three icons** — *Basic*, *Fully AI-Generated*, *Partially AI-Modified* — each in **4 variations** (black / white / ±50% transparency). Icons are optional and **do not establish compliance by themselves**. A task force will add an **audio** version + interactive second layer. |
| **Icon assets** | Downloadable | SVG `https://ec.europa.eu/newsroom/dae/redirection/document/129546` · PNG `https://ec.europa.eu/newsroom/dae/redirection/document/129547` | 2026-07-04 | Freely usable without attribution; non-signatory use is not a signal of adherence. |

## Secondary commentary (persuasive, not authoritative)

| Source | Status | URL | Last checked | Notes |
|--------|--------|-----|--------------|-------|
| Bird & Bird — "The Final Transparency Code of Practice" (22 Jun 2026) | Law-firm insight | `https://www.twobirds.com/en/insights/2026/taking-the-eu-ai-act-to-practice-the-final-transparency-code-of-practice` | 2026-07-04 | Source for the 200-token rule, single-layer exceptions, detection-fee nuance, third-icon (Basic) reading, GENERATED/MODIFIED copyright sensitivity. |
| Bird & Bird — "Reading the Commission's draft Art. 50 Guidelines" (15 May 2026) | Law-firm insight | `https://www.twobirds.com/en/insights/2026/taking-the-eu-ai-act-to-practice-reading-the-commissions-draft-article-50-guidelines` | 2026-07-04 | Source for the four-element deepfake test, the 50(2) scope carve-outs (translation in-scope, source-code, B2B, games), the 50(1) negative catalogue, the 50(3) breadth point, and the model-level-marking divergence. |

---

## What still needs a live check on activation

1. **Digital Omnibus OJ publication date** — once published, the 2 Dec 2026 grace is fully in force (drop the "awaiting OJ" caveat). Tracker: procedure 2025/359.
2. **Art. 50 Guidelines finalisation** — flip "draft" → "final" and note any changed paragraph numbering.
3. **CoP adequacy assessment** — a positive Commission/AI-Board opinion changes the evidentiary weight of signing.
4. **Initial signatory list** — published before 2 Aug 2026; once the major providers converge it becomes the de-facto standard.
5. **Icon task-force additions** — audio icon + interactive second layer.
