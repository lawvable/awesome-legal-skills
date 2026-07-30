# Direct workflow

Power-user front-end. Read every signal in one pass, resolve input, hand enriched extraction to shared generation core. Hard cap of one interruption.

## Step 0 — Read remaining signals

The routing gate already resolved the input source and ran Pass 1 (`manifest_cache`). This lane is entered after GATE A. Read the rest from the user message: (a) diagram type (exact Mermaid type / legal category / "recommend" / nothing); (b) output preferences (path override / matter_type override). The HTML report is a separate gate (GATE B), decided after the diagram is drawn.

## Step 1 — Enter Pass 2 with the router manifest

- **`manifest_cache` present** (file or pasted text) → enter `workflows/extract.md` with `skip_confirmation=true` and `manifest_cache`, so extract.md skips Pass 1 and resumes at Pass 2.
- **No `manifest_cache`** (matter description only) → synthesise `ExtractionResult` from the context window; build the coverage map by hand.

**Interruption policy (hard cap 1).** Proceed at confidence ≥ 0.50. Halt only if extraction is fully empty (`is_empty()`) with no input text available. Input resolution, the missing-file case, and the no-input prompt are handled by the routing gate before this lane loads.

## Step 2 — Type intent

- **Diagram type named** (plain word like "org chart" or "timeline", or technical type) → map plain word via `shared/diagram-type-map.md` § Plain-language names, then pass through fixed (core flags a clear mismatch once, then honours it).
- **Legal category given** → map via `shared/diagram-type-map.md`; ambiguous row defers to selector.
- **"Recommend" or nothing** → intent = matter type + dominant populated field.

## Step 3 — Generate

Load `workflows/generation.md` with enriched extraction, intent (or fixed type), `mode=direct`, and output preferences. Selects, guards, generates, delivers (rationale + alternatives), and runs refine loop.
