# Legal Translation — extended notes (data as of 2026-07)

> Slice of the canonical dataset. Full cross-vertical data + update guide: repo `data/scorecard-2026-07.md`.
> Numbers are a point-in-time prior, not a verdict — re-check the live sources for high-stakes routing.

## 5. Legal Translation

**Weakest public-benchmark coverage of the five verticals — treat this section as directional, not
benchmark-backed the way §1–§3 are.** There is **no clean legal-translation leaderboard** for frontier
LLMs. Guidance is triangulated from (a) general MT benchmarks that don't touch legal text, (b) multilingual-
reasoning benchmarks used as a proxy, and (c) dedicated legal-MT studies. **Certified/sworn translation
always requires a qualified human translator — the LLM is a first-draft engine here, never the signatory.**

**General translation quality**
- **WMT25** (field's rigor standard): human eval → **Gemini** family won (topped 14/16 language pairs);
  GPT and Cohere Command-A close; DeepSeek/Claude second tier. Rankings are **metric-dependent** — a
  separate methodology put GPT-5, Grok 4, Claude Opus, Gemini in a different order. No settled "leader."
- **Per-language split (directional):** Claude leads German/Japanese/Korean/Dutch/Italian and is
  **preferred by professional translators for tone/register**; Gemini leads Chinese/Brazilian-Portuguese/
  Ukrainian and carries the larger context window for long documents.

**Multilingual reasoning (proxy when no legal-MT number exists)**
- Roughly: **Gemini 3.1 Pro** tops raw multilingual knowledge (~94 MMLU, approx.), **GPT-5.x** close and
  strongest on MMLU-ProX, **Claude Opus** a strong #3 with notably good multilingual math (MGSM).
- This is reasoning *in* a language, not translation *quality* — a proxy, not a substitute.

**Legal-translation-specific evidence (thin but real)**
- **SwiLTra-Bench** (arXiv 2503.01372) — the most rigorous dedicated legal-MT benchmark found (Swiss
  statutes/case-law, DE/FR/IT/Romansh). Finding: **general-purpose LLMs still trail specialized legal-MT
  systems** on terminology equivalence, statutory register, and precedent-preserving case-law translation.
- **EU EUR-Lex** explicitly tells users **not** to rely on its own MT tool for legislation — only the
  human-verified official-language texts are authentic. Institutional distrust of legal MT is stated, direct.
- Glossaries fix *terminology consistency* but not **negation accuracy**, **jurisdiction-concept mapping**
  (common-law "discovery"/"plea bargain" have no civil-law equivalent), **cross-reference integrity**, or
  **legal effect**. These are the failure modes that make legal MT dangerous.

**Arabic / MENA**
- **No Arabic legal-*translation* benchmark exists** — a genuine gap. Arabic legal *reasoning* benchmarks
  exist (**ArabLegalEval**, **ALARB**); tellingly, ArabLegalEval was built by machine-translating English
  LegalBench into Arabic *then* expert-verifying — an implicit admission that raw MT needs human check.
- General Arabic reasoning: **Gemini 3.1 Pro / 3 Pro** lead (~93), **Claude Opus** close (~91–92). Claude's
  Arabic prose is reported (soft/qualitative) as more natural.
- **Mistral is a documented Arabic weak point.** **Qwen** (Qwen-MT line) and **Cohere Aya** are purpose-built
  multilingual and are the strongest *self-hostable* Arabic options.
- **RTL is a UI problem, not a model problem** — output text is fine; display alignment is a front-end
  concern (relevant only if you build your own Arabic UI on the API).

**Routing metric:** none published. Route on the proxies above; **human legal-linguist review is mandatory,
not optional** — that is documented industry consensus, not a hedge.

---

## Cross-cutting caveats (bake these into every routing decision)

1. **Capability ≠ controllability** (Wei Chen, Atticus Project). A high benchmark score does not mean a model stays in scope, cites truthfully, or is safe to deploy unsupervised. Governance is a separate axis from raw performance.
2. **All-pass reality** (Harvey). A review that catches 8 of 10 risks is not 80% useful — it is materially incomplete. Route for reliability on high-stakes work, not average quality.
3. **Grading is imperfect.** legalbenchmarks.ai reliability is scored by a *single* LLM judge (Claude Sonnet 4.6); usefulness by a 2-judge panel (~82% agreement). Their own bias check: Sonnet tops neither board and Anthropic models rank lowest on length — evidence against self-grading favoritism, but LLM-judged scores are still not ground truth.
4. **Coverage is narrow.** legalbenchmarks.ai is English-only, US/UK-skewed, single-turn, one run per task (no drift/consistency testing), with a private task set. Vals LegalBench is multiple-choice reasoning, not drafting. **Non-US, non-English, multi-turn, and long-horizon work is under-measured.**
5. **Benchmark drift & routing collapse.** Numbers here go stale monthly; and a router that always picks one dominant model has stopped routing. Re-validate when new frontier models ship.
6. **Silent quality regression.** Cost savings show up instantly on the bill; quality loss shows up days later in the work product. Gate any cost-driven downgrade behind a spot-check.

---

## Live sources — re-check before high-stakes routing

- Contract Drafting & Info Extraction: https://www.legalbenchmarks.ai/leaderboard (+ /research/phase-2-research)
- Legal reasoning (LegalBench, 124 models, live): https://www.vals.ai/benchmarks/legal_bench
- Agentic legal task design: https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark
- "The Path to Better Legal AI: Benchmarks" (Wei Chen): https://www.linkedin.com/pulse/path-better-legal-ai-benchmarks-wei-chen-jpksc
- Atticus open datasets (CUAD/MAUD/ACORD): https://www.atticusprojectai.org/
- Generalist cross-check: https://artificialanalysis.ai/leaderboards/models · https://lmarena.ai · https://www.swebench.com
- Long-context efficiency (Mamba vs transformers on long legal docs): https://arxiv.org/abs/2509.00141

**Snapshot date: 2026-07.** If today is >2 months later, treat ranks as suspect and re-pull the live boards.
