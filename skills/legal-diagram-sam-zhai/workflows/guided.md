# Guided workflow

Interactive default lane. Digest or elicit, show findings, hand to shared generation core (auto-picks with rationale and offers alternatives). One matter commonly yields several diagrams per session.

## Step 0 — Receive router handoff

The routing gate already detected input, resolved `diagram_scope` (multi-file pop-up), and ran Pass 1. This lane is entered after GATE A. You receive `manifest_cache`, `input_source`, and `diagram_scope`.

- `manifest_cache` present (file or pasted text) → docs path (Step 1A).
- No `manifest_cache` (matter description only, no docs) → intake path (Step 1B).

Do not re-detect input or re-ask scope; the router owns both.

## Step 0.5 — Confirm input

After detecting input, confirm to the user in one plain-English sentence what file or text was read (e.g., "I've read **[filename]**." or "Got your text."). The HTML report is decided later at GATE B (`workflows/generation.md` § Step 5), not here.

Set `source_path` = absolute path to input file if available (file input only; null for pasted text or stdin).

## Step 1A — Digest provided material

Enter `workflows/extract.md` with `skip_confirmation=false` (show digest, do not suppress) and the `manifest_cache` from the router, so extract.md skips Pass 1 and resumes at Pass 2. Returns enriched `ExtractionResult` plus coverage. Go to Step 2.

## Step 1B — Elicit (no docs)

1. Load `shared/elicitation.md`.
2. Identify matter family. If unnamed, ask one line: "What kind of matter? litigation / corporate / compliance / deal / employment / IP / privacy / bankruptcy / tax / real estate / other."
3. Ask that family's curated set (3-5 questions). Accept shorthand; skip answered items.
4. Build `ExtractionResult` from answers; construct coverage map by hand. Go to Step 2.

## Step 2 — Digest ⛔ BLOCKING

Never use field names, JSON, or technical vocabulary. Translate everything to plain English.

Render every populated field as a plain-language section, one per field, in same field order as category map below. Skip absent fields. Hint-only fields get a ⚠ prefix.

Category map (field → plain label):

|Field|Category label|
|---|---|
|obligations|Obligation|
|deadlines|Deadline|
|conditions|Condition|
|documents|Document|
|transfers|Money flow|
|decision_points|Decision|
|events|Key event|
|parties|Party|
|entities|Entity|
|relationships|Relationship|
|ownership_links|Ownership|
|concepts|Key concept|
|risk_items|Risk|
|communications|Communication|
|data_flows|Data flow|
|ip_assets|IP asset|
|legal_authorities|Legal authority|
|witnesses|Witness|
|(all others)|Other finding|

After all sections:
- **⚠ Uncertain:** list hint-only fields with one plain-English line each.
- **Not found:** list absent high-value fields for this matter type (e.g. no parties in a litigation matter). Invite user to supply them.

Then ask: **"Does this look right? Correct a name, add something I missed, or remove anything — then I'll suggest a diagram type."**

⛔ BLOCKING: do not proceed to Step 2.5 until user responds. Accept "looks good" / "yes" to proceed unchanged. Apply plain-English corrections to ExtractionResult before continuing.

If extraction empty after both passes, ask one targeted question and retry once before halting.

## Step 2.5 — Type confirmation gate ⛔ BLOCKING

Run `diagram_selector.py` on enriched extraction. Present recommendation and **wait for an explicit choice before proceeding.**

Output format (no preamble):

> **Recommended:** [plain-language name] — [one-sentence rationale grounded in what was found].
> **Alternatives:**
> - [alt1] — best if [one plain-language reason tied to extraction fields]
> - [alt2] — best if [one plain-language reason tied to extraction fields]
>
> Which would you like, or should I go with the recommendation?

**If user named a diagram type upfront** and it matches recommendation → confirm and proceed. If it conflicts → surface conflict explicitly:

> You asked for a **[user's type]**. For this matter I'd recommend a **[recommended type]** because [reason tied to extraction fields]. Proceed with [user's type], switch to [recommended], or pick an alternative?

Do not call `generation.md` until user responds. Gate counts as one of guided mode's allowed interruptions.

## Step 3 — Generate

Load `workflows/generation.md` with enriched extraction, **confirmed type from Step 2.5**, `mode=guided`, `source_path`, and `digest_rows` from Step 2. Guards, generates, delivers, and loops. The HTML report is decided at GATE B inside generation Step 5.
