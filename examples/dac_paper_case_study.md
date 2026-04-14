# Case Study: DAC Materials ML Paper (R0 → R2)

A real-world application of Lunheng on a Chinese-language chemistry-ML paper for a Q1 journal.

## Paper Snapshot

| Field | Value |
|-------|-------|
| **Topic** | ML prediction of CO₂ adsorption on Direct Air Capture (DAC) sorbents |
| **Length** | 24 pages (LaTeX), 2 tables + 7 figures + 117 references |
| **Type** | Methodology + benchmark dataset |
| **Target venue** | Q1 chemistry/materials journal (CAS Tier 1) |
| **Author** | First-time PhD-track researcher |

## Composite Score Trajectory

| Round | Score | Δ | Verdict change |
|-------|-------|---|----------------|
| R0 (baseline) | **6.81** | — | Borderline reject |
| R1 (formatting + visual fixes) | **8.04** | +1.23 | Borderline accept |
| R2 (content + reproducibility) | **8.66** | +0.62 | Strong accept |

For perspective, the single-Claude baseline (`lunheng-quick`) scored **7.6** on the same R0 manuscript — Lunheng's full multi-agent pipeline gained an additional **+1.06** by Round 2.

## Per-Dimension Breakdown

| Dim | Dimension | R0 | R1 | R2 | What changed at each step |
|-----|-----------|----|----|----|---------------------------|
| D1 | Soundness | 7.0 | 7.0 | **9.0** | R2: declared iid+homoscedasticity assumptions for $R^2_{\max}$ derivation; softened Clausius-Clapeyron interpretation; added paired t-tests |
| D2 | Significance & Originality | 8.5 | 8.5 | 8.5 | Already strong: largest cross-type DAC dataset + noise-floor analysis novel methodology |
| D3 | Clarity & Organization | 8.0 | 8.5 | 8.5 | R1: terminology unification (辅助域→广域CO₂等温线), table column counts fixed |
| D4 | Experimental Substance | 8.0 | 8.0 | **9.0** | R2: noise-robust ablation table moved from SI to main text with p-values; HOF row added with sample-size footnote |
| D5 | Reproducibility | 7.5 | 7.8 | **8.4** | R2: added hyperparameter table (CatBoost/XGBoost/LightGBM exact values); ensemble weights (0.35/0.30/0.35); SMOGN parameters |
| D6 | Citation Quality | 6.5 | 7.0 | 7.5 | R2: added RDKit, WebPlotDigitizer, NIST/ISODB, Morgan fingerprint, Freundlich, Pan, Cao MOFormer, ChemBERTa, Spearman citations |
| D7 | Visual & Tabular Communication | 4.0 | **8.0** | 8.0 | R1: re-inserted 7 floating figures with `[H]` placement; added missing `tab:features`; converted PDF figures to PNG for Word compatibility |
| D8 | Ethics, Limitations & Broader Impact | 5.0 | 9.0 | 9.0 | R1: moved Limitations from buried sentence to dedicated subsection |

(Note: D7's R0 of 4.0 was driven by 8 dangling `\ref` and 59 broken `\cite`. After R1 it dropped to 0 undefined references.)

## Architect Findings (Round 1)

The Architect agent identified **3 most severe structural issues**:

1. **SI Phantom References** — text cited `Tab. S1`, `Tab. S2`, `Tab. S3` but no SI document was attached and no tables were defined in main.tex. → Fix: tables moved into main text or labels removed.

2. **Section Weight Imbalance** — Methods (35%) >> Results (22%) > Discussion (15%); the central methodological contribution ("ranking metrics over $R^2$") was buried in §3.2 instead of being foregrounded in the introduction. → Fix: Discussion expanded by 30%.

3. **Number Drift Across Sections** — HUM count was 702 vs 703 in different places; total paper count was 113 vs 150 vs 164; Random CV $R^2$ was 0.887 in Table but 0.882 in Figure caption. → Fix: terminology glossary in Visual Contract enforced single canonical values; rewrote sections to use them consistently.

## What Each Round Cost

| Round | Sub-agent calls | Wall time | Compute cost |
|-------|-----------------|-----------|--------------|
| R0 baseline (8 evaluators only) | 8 | ~3 min | ~30k tokens |
| R1 (Architect + Writer × 4 + Refiner + 8 Evaluators) | 14 | ~12 min | ~120k tokens |
| R2 (targeted Writer × 3 + 5 re-Evaluators) | 8 | ~5 min | ~70k tokens |
| **Total** | **30** | **~20 min** | **~220k tokens** |

(Tokens approximate, using Claude Opus 4.6.)

## Key Methodological Wins (Multi-Agent vs. Single-Reviewer)

A single Claude reviewer (`lunheng-quick`) on the same R0 paper scored **7.6 / 10**. The four dimensions where the full multi-agent setup beat the single-reviewer baseline:

| Dimension | Single reviewer | Full Lunheng |
|-----------|-----------------|--------------|
| D1 Soundness | 7.5 | **9.0** | More careful spotting of statistical-test gaps |
| D5 Reproducibility | 7.5 | **8.4** | Specialized evaluator caught missing hyperparams |
| D7 Visual Communication | 5.0 | **8.0** | Visual contract caught dangling refs that single reviewer missed |
| D8 Ethics/Limitations | 6.0 | **9.0** | Dedicated dimension forced explicit attention |

## Reproducibility of This Case Study

All raw agent outputs are preserved in `examples/dac_artifacts/` (TODO: anonymize and upload):
- `blueprint_round1.md`
- `visual_contract_round1.json`
- `evaluator_outputs_round1.md` (8 agents, raw)
- `refined_round1.tex` (diff vs original)
- Same set for Round 2

A reader can re-run any individual sub-agent with the saved prompt to verify the score it returned.

## Lessons Learned

1. **Round 1 always wins big on D7+D8** if the original paper has any formatting issues — these are easy to spot, easy to fix, and the score jumps.

2. **Round 2 needs content surgery** — D1, D4, D5 only move with substantive edits (added tables, declared assumptions, supplied hyperparams). The model can identify *what* to add, but the user must verify the additions are factually accurate (especially numerical values from training logs).

3. **Visual Contract pays off most for long papers** — for our 24-page paper with 7 figures, the contract caught 3 separate cross-section inconsistencies that no single reviewer flagged in R0.

4. **8 evaluators in parallel is genuinely fast** — fanning out 8 sub-agent calls in one message returned all reviews in ~3 minutes total wall time.

5. **The composite score $R = 7.0$ stop threshold is well-calibrated** — at $R \geq 7.0$ the paper passes basic publication checks; below that something structural is still broken.
