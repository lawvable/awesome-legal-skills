# Info Extraction — extended notes (data as of 2026-07)

> Slice of the canonical dataset. Full cross-vertical data + update guide: repo `data/scorecard-2026-07.md`.
> Numbers are a point-in-time prior, not a verdict — re-check the live sources for high-stakes routing.

## 2. Info Extraction

**Source:** legalbenchmarks.ai — "Info Extraction" (29 tasks). Documents sent in **native, unconverted form**,
so file-reading (incl. scanned docs) is part of what's tested. Same two-axis rubric as drafting.

| Rank | Model            | Provider  | Reliability | Usefulness | Cost/task |
|-----:|------------------|-----------|------------:|-----------:|----------:|
| 1    | GPT 5.6 Sol      | OpenAI    | 89.7%       | 2.78       | ~$0.19    |
| 2    | Claude Opus 4.8  | Anthropic | 86.2%       | 2.54       | ~$0.29    |
| 2    | Claude Fable 5   | Anthropic | 86.2%       | 2.51       | ~$0.63    |
| 4    | GPT-5.5          | OpenAI    | 82.8%       | 2.62       | $0.15     |
| 5    | Grok 4.5         | xAI       | 79.3%       | 2.70       | ~$0.19    |
| 6    | Claude Sonnet 4.6| Anthropic | 72.4%       | 2.47       | $0.13     |
| 7    | Gemini 3.1 Pro   | Google    | 65.5%       | 2.51       | $0.07     |
| 7    | Gemini 3.5 Flash | Google    | 65.5%       | 2.76       | ~$0.08    |
| 9    | DeepSeek V4 Pro  | DeepSeek  | 62.1%       | 2.37       | ~$0.03    |
| 10   | GPT-5.4-mini     | OpenAI    | 58.6%       | 2.75       | ~$0.01    |
| 11   | Qwen 3.7 Max     | Alibaba   | 55.2%       | 2.55       | ~$0.03    |

**Truths / nots**
- **GPT 5.6 Sol** — best at *exhaustive clause retrieval* and *cross-document comparison*. Blind spots: **scanned documents**, and **flattening conditional answers into absolutes** ("if X then Y" → "Y"). Verify conditionals.
- **Opus 4.8 / Fable 5** — most dependable pair (tied #2), but the **most verbose** answers tested; you pay in output tokens and post-processing.
- **Grok 4.5** — **best scanned-document handling of any model**, but under-returns on completeness ("almost all" instead of all). Route here for image-heavy/OCR-adjacent extraction, then double-check coverage.
- **Cheap tier (Qwen 3.7 Max, GPT-5.4-mini, DeepSeek V4 Pro)** — bottom of reliability (55–62%). Fine for low-stakes triage, not for extraction you'll rely on.

**Related academic anchors (Wei Chen / Atticus Project):** **CUAD** (clause extraction, 510 contracts, 41 clause types), **MAUD** (M&A reading comprehension, 92 question types), **ACORD** (clause retrieval, 1–5 relevance). These are the open datasets the field uses when it wants reproducible extraction/retrieval evaluation.

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
