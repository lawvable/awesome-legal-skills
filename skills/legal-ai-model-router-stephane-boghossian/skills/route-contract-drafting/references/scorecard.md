# Contract Drafting — extended notes (data as of 2026-07)

> Slice of the canonical dataset. Full cross-vertical data + update guide: repo `data/scorecard-2026-07.md`.
> Numbers are a point-in-time prior, not a verdict — re-check the live sources for high-stakes routing.

## 1. Contract Drafting

**Source:** legalbenchmarks.ai — "Contract Drafting" (34 tasks, 3rd installment, refreshed monthly).
**Metric:** `Reliability` = share of tasks passed *fully* correct on a lawyer-written checklist (binary;
one miss fails the whole task). `Usefulness` = 1–3 mean (clarity / length / structure). Cost = $/task.

| Rank | Model            | Provider  | Reliability | Usefulness | Cost/task |
|-----:|------------------|-----------|------------:|-----------:|----------:|
| 1    | Claude Opus 4.8  | Anthropic | 67.6%       | 2.67       | ~$0.29    |
| 2    | Claude Fable 5   | Anthropic | 61.8%       | 2.66       | ~$0.63    |
| 3    | Grok 4.5         | xAI       | 58.8%       | 2.61       | ~$0.19    |
| 4    | Gemini 3.5 Flash | Google    | 55.9%       | 2.60       | ~$0.08    |
| 5    | Claude Sonnet 4.6| Anthropic | 50.0%       | 2.63       | $0.13     |
| 5    | Gemini 3.1 Pro   | Google    | 50.0%       | 2.69       | $0.07     |
| 7    | GPT 5.6 Sol      | OpenAI    | 44.1%       | 2.75       | ~$0.19    |
| 7    | Qwen 3.7 Max     | Alibaba   | 44.1%       | 2.67       | ~$0.03    |
| 9    | GPT-5.5          | OpenAI    | 41.2%       | 2.77       | $0.15     |
| 10   | DeepSeek V4 Pro  | DeepSeek  | 26.5%       | 2.68       | ~$0.03    |
| 10   | GPT-5.4-mini     | OpenAI    | 26.5%       | 2.55       | ~$0.01    |

**Truths / nots**
- **Opus 4.8** — best all-round drafter; uniquely willing to *flag contradictory instructions* instead of drafting through them. Truth: highest reliability. Not: not the cheapest.
- **Fable 5** — ties Opus on quality but ~2.2× the cost/task without beating it. Not: overpriced for drafting.
- **Grok 4.5** — best non-Anthropic drafter, cheapest of the top 4; uniquely good at *leaving already-sound language untouched* (fewer gratuitous rewrites). Strong value pick.
- **GPT 5.6 Sol** — **highest usefulness (2.75) is a trap:** "more polished than accurate." >50% of its drafts miss ≥1 instruction hidden behind clean prose. Do not route drafting here on the strength of readability.
- **All models** — weak at conflict detection; GPT 5.6 Sol is the worst at silently drafting through contradictions.

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
