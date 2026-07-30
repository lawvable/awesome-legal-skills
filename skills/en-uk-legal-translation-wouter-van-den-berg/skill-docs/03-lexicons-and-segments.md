> **Pre-flight.** You should be entering this step having completed the previous step. **SKILL.md governs every step's discipline; if you have not read SKILL.md in full this session, STOP and `Read('SKILL.md')` before continuing.** Hard Rules from SKILL.md apply to this step too. **In Chat mode (no workspace folder, no auto-managed todo list) the same discipline applies — do not skim this step doc, do not bundle batches, do not skip the per-step Internal compliance check at the bottom.** **If this turn began from a compacted transcript, the compaction summary does NOT count as having read this step doc — `Read()` it now in full before any tool call.**

### Step 3: Identify document type and read the lexicons

*[Internal compliance check — do not echo or paraphrase to the user. Re-read every rule in this step before executing. Do not deviate from any line of the skill. Do not bundle work, skip checks, or "interpret for efficiency" — every prior deviation has produced output below the quality the skill is designed to deliver. The skill's hard gates block deviations anyway; complying upfront is always faster than running into a gate and re-authoring paragraphs.json.]*

Read the first ~20 paragraphs to identify:
- **Source language** (Italian, French, German, Spanish, Portuguese, Dutch, Finnish, Hungarian, Polish, Chinese, Japanese, etc.)
- **Legal domain** — project finance, M&A, corporate, IP, real estate, etc.
- **Document type** — deed, agreement, resolution, notice, etc.

#### MANDATORY: read the lexicons end-to-end before drafting the first paragraph

The single most common failure mode of this skill is **partial lexicon reading
followed by calque drift**. The reference lexicons and the language sub-lexicons
contain "Avoid" columns that are **binding rules, not suggestions**. Skimming the
first half of a lexicon and starting to translate is how calques like
*"this present agreement"* (NL *deze onderhavige overeenkomst*), *"framework
conditions"* (NL *randvoorwaarden*), *"environs fund"* (NL *omgevingsfonds*),
or *"in more concrete terms"* (NL *concretiseren*) end up in a final output —
each of these is explicitly listed in the Avoid column of a lexicon that the
drafter technically "read". Do not rely on memory of the lexicon — open it,
scroll to the end, and treat the Avoid columns as a blocklist.

Rules for this step:

1. **Read `references/general-legal.md` in full, end-to-end**, before drafting
   any paragraph.
2. **Read each applicable domain lexicon in full, end-to-end.** Do not stop
   part-way on the basis that "the rest looks like content I'll never hit".
3. **Read each applicable language sub-lexicon in full, end-to-end.** Sub-lexicons
   are the only place where language-specific calques are documented.
4. While translating, every time you reach for a phrase that translates a civil-law
   formulaic construction (party blocks, self-reference, signature blocks, recitals,
   termination boilerplate, *onderhavige* / *presente* / *présent* / *vorliegend*
   fillers, adverbial stackings like "on the basis of and pursuant to"), **pause
   and re-check the Avoid columns**. If your candidate rendering is listed
   there, pick the preferred one next to it.
5. **Anti-drift rule.** Reading a lexicon once at the top of the task and then
   relying on memory for the rest of the translation has repeatedly produced
   calque drift (see the failure examples above). Re-open the relevant sub-lexicon
   at each fresh batch and re-scan the Avoid columns for the kinds of constructions
   you know the upcoming paragraphs will contain (e.g. termination clauses before
   Batch 5, dispute-resolution clause before Batch 6). This repetition is cheap
   and it is the only reliable way to stop the drift.
6. The automated compliance scan (Step 4d below as a manual run, plus the auto-run
   inside Step 10 `repack_docx.py`) will block repack if any documented Avoid-column
   phrase survives to the output. It is cheap — run it early and often, not just
   at the end.

**Always read the base English lexicon first, in full:**
- `references/general-legal.md` — Universal English legal terms, structural conventions, grammar rules

**Then read each relevant domain-specific English lexicon in full:**
- `references/finance-banking.md` — Facility agreements, security documents, pledges, mortgages, bonds, loans, banking regulation, syndicated facilities, AML/KYC, sanctions, Basel/CRD
- `references/corporate-ma-jv.md` — Unified lexicon for M&A (SPAs, transaction deeds, disclosure letters, warranty/indemnity), JVs (JVAs, SHAs, shareholder loans, consortium and co-investment agreements), corporate resolutions (board and shareholder resolutions, minutes, EGM/OGM, governance, voting), and powers of attorney / proxies (notarial and private POAs, apostille/legalisation, meeting proxies)
- `references/taxes.md` — Tax law and tax procedure: direct/indirect taxes, VAT, withholding tax, residency and PE, double tax treaties, transfer pricing, anti-avoidance (BEPS, Pillar Two, GAAR, CFC), tax compliance, audits, rulings, disputes, M&A tax interface, customs and excise
- `references/ndas-service-agreements.md` — Unified lexicon for NDAs / confidentiality agreements and undertakings, AND for service agreements, SLAs, outsourcing, consultancy, managed services, master services agreements and SOWs
- `references/energy-infrastructure.md` — EPC/turnkey contracts, construction, O&M, BOP, PPAs, grid connection, offtake, concessions, renewables, tariffs
- `references/ip-it-technology.md` — Combined IP (patents, trademarks, copyright, licensing, R&D, technology transfer) and IT/SaaS (software licences, cloud services, development agreements)
- `references/transport-and-insurance.md` — Combined shipping/transport (charter parties, bills of lading, Incoterms, freight, maritime law) and insurance/reinsurance (policies, treaties, claims, subrogation, Lloyd's market)
- `references/permitting-environmental.md` — Environmental law and permitting: EIA/SEA, IED integrated permits, water, waste, nature (Natura 2000), chemicals (REACH/CLP), contaminated land, ELD, climate (EU ETS, CBAM, Fit for 55, CSRD/CSDDD, Taxonomy), construction and zoning, Aarhus Convention
- `references/public-procurement.md` — Tenders, concessions, PPP/PFI, state aid, EU procurement directives
- `references/real-estate.md` — Leases, property transfers, easements, zoning, conveyancing
- `references/litigation-settlement.md` — Civil, administrative and criminal litigation; settlement agreements, releases, waivers, dispute resolution, arbitration
- `references/trading-capital-markets.md` — ISDA, derivatives, repo, securities lending, EMIR, MiFID
- `references/consumer-retail.md` — Terms and conditions, franchise, distribution, agency, consumer protection
- `references/employment.md` — Employment contracts, non-competes, severance, collective bargaining, secondment

If a document straddles multiple domains (e.g., an NDA prepared in the context of an M&A
transaction, or a shareholder loan sitting alongside an SHA), read both relevant lexicons.

**Then read the language-specific sub-lexicons:**

Sub-lexicons are bundled **inside the skill folder** at `<skill-path>/sub-lexicons/` and cover
all 11 supported languages (Chinese, Dutch, Finnish, French, German, Hungarian, Italian,
Japanese, Polish, Portuguese, Spanish) across 14 domains. Files are named
`<language>-<domain>.md` — e.g. `italian-general-legal.md`, `polish-ip-it-technology.md`,
`german-corporate-ma-jv.md`.

**Note on Finance & Banking + Trading & Capital Markets.** In the per-language sub-lexicons
the two domains are consolidated into one file, `<language>-finance-banking.md`, because
their vocabulary overlaps heavily (debt instruments, securities, exchange regulation) and
translators typically need both at once. The trading & capital markets entries appear as a
section inside that file. The two cross-language English-reference lexicons,
`references/finance-banking.md` and `references/trading-capital-markets.md`, remain split as
two separate files. So when working on a capital-markets document: read both reference files
above, but only the single `<language>-finance-banking.md` sub-lexicon.

Resolve the skill path from the SKILL.md location you are currently reading and list the
matching sub-lexicons with a simple glob:

```bash
ls "<skill-path>/sub-lexicons/" | grep -E "^<language>-" | sort
```

Read the relevant sub-lexicons for the document's language and domain(s) — typically
`<language>-general-legal.md` plus one or two domain files (e.g. `italian-finance-banking.md`
for a facility agreement). Sub-lexicons map source-language legal terms to correct English
equivalents and are the single best source of terminology consistency for this skill.

If the document is in a language not covered by the bundled sub-lexicons, proceed with
translation using the English reference lexicons alone — no sub-lexicon is required to
complete the translation.

**Sub-lexicons are read-only during translation.** Do not create new sub-lexicon files, and
do not edit existing ones, at runtime. This includes adding a missing term, "correcting" a
translation you disagree with, or appending notes. If you find a gap or a term you think
should be changed, surface it to the user at the end of the translation so they can decide
whether to update the sub-lexicon offline. Any expansion or correction of sub-lexicon
content is handled as a deliberate skill update by the user, not as a side effect of a
translation run. This rule applies even if the "Create mode" or "Write" tools are available
to you.

### Step 3b: Scaffold en_segments for character-fragmented tracked-change clusters — MANDATORY if source has TCs

Source-language concept drafts occasionally contain tracked-change edits authored
letter by letter — a single word or ordinal is replaced by a different word through
a long series of 1–3 character `ins` / `del` splits. In English, the correct edit
is almost always a **whole-word** replacement (e.g. "Clause 12" → "Clause 13"), not
a character-level one — so the segment-aware translator cannot produce a clean
English redline against the fragmented source structure without explicit guidance.

Run the detector once, before drafting translations:

```bash
python <skill-path>/scripts/coalesce_fragmented_tcs.py <workdir>/paragraphs.json
```

The script scans every paragraph with `has_track_changes: true`, detects
contiguous character-level ins/del clusters that reassemble to a coherent single
word/ordinal on each of the Accept and Reject sides, and **writes a pre-filled
`en_segments` skeleton** into each flagged paragraph. It does **not** modify
`tc_segments` — the source XML structure still has all its character-level runs,
so the skeleton has one `en_segments` entry for every `tc_segments` entry. Inside
each detected cluster the skeleton contains:

- a `<<TRANSLATE: ins='<accepted-word>' (accepted)>>` placeholder on the first
  `ins` segment,
- a `<<TRANSLATE: del='<rejected-word>' (rejected)>>` placeholder on the first
  `del` segment,
- the empty string `""` on every other segment (intermediate ins, del, and
  regular runs that collectively make up the fragmented cluster).

Outside the cluster the skeleton leaves `en: ""` so the translator still fills in
the normal paragraph text.

At translation time (Step 4) the translator:

1. replaces each `<<TRANSLATE: …>>` placeholder with the final English
   (e.g. `"Clause 13"` on the ins side, `"Clause 12"` on the del side);
2. fills in the surrounding non-cluster `en_segments` entries with normal
   translations;
3. leaves the empty-string slots inside the cluster **as `""`** — these are the
   deliberate "clear this run" markers that `apply_translations_textmatch.py`
   uses to empty the matching source runs so no orphan source letters leak into
   the English redline.

Idempotent: re-running the script on an already-scaffolded paragraphs.json
re-detects the same clusters and writes the same skeleton. Exits cleanly with
`"No character-fragmented TC clusters detected. Nothing to do."` when no
clusters match.

See "Scrambled / character-fragmented whole-word edits" under Step 4 for the
rationale and the canonical Spanish road-use example.

If the source document has no tracked changes, this step is a no-op and can be
skipped.

#### TC marker counts may legitimately differ between source and output

Three mechanisms can reduce `<w:ins>` / `<w:del>` counts in the final English
document without losing any tracked-change information:

1. `coalesce_fragmented_tcs.py` collapses character-level source edits into
   whole-word English edits — e.g. five character-level ins/del pairs in a
   source edit of `Duodécima → Decimotercera` become a single whole-word
   pair `Clause 12 → Clause 13` in English, because character-level edits
   do not survive word-level translation.
2. `strip_noop_tracked_changes.py` (Step 8 / apply stage) removes no-op
   orthographic pairs — tracked changes whose only effect in the source is a
   Spanish accent / punctuation / diacritic change with no English analogue —
   and strips any empty `<w:ins>` / `<w:del>` wrappers left behind.
3. Empty run wrappers left after text replacement are compacted away during
   the apply step.

On a typical Spanish `.doc → .docx` redline you should expect the `<w:ins>`
count to drop by roughly 10–25% (insertion counts shrink more than deletion
counts, because Spanish conversion artefacts cluster on the insertion side).
This is a quality improvement, not a defect. If you are handing the file to a
reviewer who compares marker counts side-by-side, mention this upfront so the
reduction is not mistaken for lost content — an Accept All / Reject All
simulation is the correct way to confirm TC coverage, not marker arithmetic.

## Internal compliance check — 03-lexicons-and-segments

Before moving to the next step, confirm:

- [ ] You read all relevant English reference lexicons in full **in this document's session** (do not rely on lexicon reads from a previous document)
- [ ] You read every applicable per-language sub-lexicon in full **in this document's session** (sub-lexicon Avoid-column entries that fit Document N-1 may not fit Document N — re-Read or you will drift)
- [ ] For TC documents, you scaffolded `en_segments` (Step 3b) before translating
- [ ] You did NOT skim the lexicons or summarise — you read them end-to-end

If any check is uncertain, STOP. Re-read this file. Do not proceed.

**Next:** `skill-docs/04-translate.md`
