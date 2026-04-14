# Lunheng Evaluation Rubric (论衡评价标准)

> "权衡论证, 校释虚妄" — 王充《论衡》
>
> Weighing arguments, examining what is false — *Lunheng*, Wang Chong (~80 CE)

This rubric is **aligned with the actual scoring practices of NeurIPS, Nature, and JACS**. Each of the 8 dimensions uses a **1–10 scale with anchored anchors** at four levels (1–3 / 4–6 / 7–8 / 9–10), so different evaluators converge on similar scores.

---

## D1. Soundness — 方法严谨性

**What it measures:** Technical correctness, claim–evidence alignment, statistical reporting, mathematical rigor.

**Aligned with:** NeurIPS *Soundness*, Nature *Technical Rigor*, JACS *Scientific Quality*.

| Score | Anchor |
|-------|--------|
| **9–10** | All claims rigorously supported; full statistical reporting (CIs, p-values, multiple testing); mathematical derivations complete and sound; assumptions explicitly stated. |
| **7–8** | Most claims well supported; minor statistical detail gaps (e.g., CI but no effect size); assumptions mostly explicit. |
| **4–6** | Some claims overreach; missing significance tests on key comparisons; assumptions implicit; ad-hoc justifications. |
| **1–3** | Major logical gaps; fabricated results; mathematical errors; unsupported sweeping claims. |

**Red flags:** $p < 0.05$ without correction for multiple testing; ad-hoc statistical methods; claims of "significantly better" without test reported.

---

## D2. Significance & Originality — 重要性与原创性

**What it measures:** Advance over state-of-the-art, conceptual novelty, impact on field.

**Aligned with:** NeurIPS *Significance + Originality* (each 1–4), Nature *Advance*, JACS *Conceptual Novelty*.

| Score | Anchor |
|-------|--------|
| **9–10** | Paradigm shift / first-of-kind / opens new research directions; results likely to be widely cited and replicated. |
| **7–8** | Solid advance over SOTA; clear contribution to a recognized open problem; useful methodology beyond the immediate domain. |
| **4–6** | Incremental improvement; replication of known results in new setting; useful but limited contribution. |
| **1–3** | No clear advance; well-known results restated; routine application of standard methods. |

**Red flags:** Comparison only to weak baselines; "first" claims not substantiated by literature search; no clear answer to "so what?"

---

## D3. Clarity & Organization — 清晰度与组织

**What it measures:** Writing flow, logical structure, paragraph cohesion, terminology consistency.

**Aligned with:** NeurIPS *Clarity*, JACS *Clarity of Writing*.

| Score | Anchor |
|-------|--------|
| **9–10** | Engaging writing; every paragraph advances narrative; consistent terminology; topic sentences clear; logical transitions; no data-dumping. |
| **7–8** | Clear writing; minor organizational issues (one or two sections feel out of place); minor terminology drift. |
| **4–6** | Mostly readable; some sections drag with data dumping; terminology drift across sections; awkward translations / passive voice overuse. |
| **1–3** | Confusing structure; rampant translation-style language; key results buried; jargon without explanation. |

**Red flags:** Same concept named 3 different ways; tables/figures referenced before context; "first/second/third" lists where prose is needed.

---

## D4. Experimental Substance — 实验充分性

**What it measures:** Adequacy of experiments, baselines, ablations, sample sizes, error reporting.

**Aligned with:** NeurIPS *Quality* (technical claims supported), Nature *Experimental Rigor*.

| Score | Anchor |
|-------|--------|
| **9–10** | Comprehensive ablations; multiple SOTA baselines on same dataset; error bars and seeds reported; sensitivity analyses; held-out test sets. |
| **7–8** | Good ablations; key baselines included; error bars on main results. |
| **4–6** | Limited baselines (or only weak ones); ablations only in supplementary; missing sensitivity analyses; small sample warnings. |
| **1–3** | No baselines; no ablations; no error bars; underpowered experiments; cherry-picked results. |

**Red flags:** "Best of 3 runs" reported as mean; no comparison to prior work with same dataset; ablation table only in SI when it's the key argument.

---

## D5. Reproducibility — 可复现性

**What it measures:** Whether an independent researcher can reproduce the results from the paper alone.

**Aligned with:** NeurIPS *Reproducibility Checklist* (16 items), Nature *Code & Data Availability*.

Use the [Reproducibility Checklist](REPRODUCIBILITY_CHECKLIST.md) (16 items adapted from NeurIPS) to score:
- 9–10: ≥ 14 / 16 items satisfied
- 7–8: 11–13 items satisfied
- 4–6: 7–10 items satisfied
- 1–3: ≤ 6 items satisfied

**Red flags:** "Code will be released upon acceptance"; hyperparameters described in prose only ("around 1000 epochs"); train/val/test splits unspecified.

---

## D6. Citation Quality — 引用质量

**What it measures:** Coverage of related work, tool/method citations, classical references, balance.

**Aligned with:** JACS *Literature Citations Appropriateness*, Nature *Contextualization*.

| Score | Anchor |
|-------|--------|
| **9–10** | All tools and methods cited (RDKit, scikit-learn, etc.); classical literature foundation; balanced citation density across sections; no dead bib entries. |
| **7–8** | Most tools cited; good coverage; minor missing citations. |
| **4–6** | Some tool/method citations missing; uneven density (intro heavy, results bare); some dead bib entries. |
| **1–3** | Many tools uncited; key prior work missing; bib bloat with unused entries; broken refs. |

**Red flags:** "We use machine learning" without method citation; tool packages used but creator not credited; >50% of bib entries unused.

---

## D7. Visual & Tabular Communication — 图表沟通

**What it measures:** Figure quality, caption self-containedness, table formatting, layout, figure–text alignment.

**Aligned with:** Nature *Figure Quality*, NeurIPS *Presentation*, all journals' typesetting standards.

| Score | Anchor |
|-------|--------|
| **9–10** | Publication-quality figures; self-contained captions (readable without main text); subfigure labels clear; consistent style; table columns aligned; tight figure–text placement. |
| **7–8** | Clear figures; minor caption gaps; mostly tight layout. |
| **4–6** | Figures readable but require text for context; some captions just label axes; tables with column count mismatches. |
| **1–3** | Figures unclear / pixelated / unreadable text; captions absent or trivial; dangling \\ref; figures floating to wrong sections. |

**Red flags:** PDF figures embedded in Word documents (render blank); subfigure (a)(b)(c) in image but not in caption; figures appearing inside references list.

---

## D8. Ethics, Limitations & Broader Impact — 伦理/局限/影响

**What it measures:** Transparency about limitations, ethical considerations, societal impact.

**Aligned with:** NeurIPS *Limitations + Broader Impact + Ethics*, Nature *Ethics Statement*.

| Score | Anchor |
|-------|--------|
| **9–10** | Detailed limitations section addressing assumption violations and edge cases; ethics statement (where applicable); broader impact (positive AND negative); data licensing respected. |
| **7–8** | Good limitations section; ethics addressed if applicable. |
| **4–6** | Brief limitations paragraph; ethics not discussed even when applicable. |
| **1–3** | No limitations; ethical issues ignored; data/model release without safeguards. |

**Red flags:** Limitations section that just lists future work; no discussion of failure modes; medical/biometric data without IRB statement.

---

## Holistic Scores

In addition to the 8 dimensions, evaluators provide:

### Overall Score (1–6, NeurIPS-style)

| Score | Verdict |
|-------|---------|
| **6** | Top-tier paper, paradigm-shifting; immediate accept |
| **5** | Strong accept; high impact in subfield |
| **4** | Borderline accept; solid contribution with minor gaps |
| **3** | Borderline reject; has potential, needs major revision |
| **2** | Reject; technical flaws or weak experiments |
| **1** | Strong reject; fundamentally flawed |

### Confidence (1–5)

| Score | Meaning |
|-------|---------|
| **5** | Absolutely certain; expert in this exact subfield |
| **4** | Confident; familiar with most of related work |
| **3** | Fairly confident; some gaps in adjacent areas |
| **2** | Possible gaps in understanding; willing to defend |
| **1** | Educated guess; outside primary expertise |

### Composite Score

$$ R = \frac{1}{8} \sum_{k=1}^{8} D_k $$

Range: 1.0 – 10.0. Stop iteration when $R \geq 7.0$ OR `iteration >= MAX_ITERATIONS`.

---

## Reviewer's Output Template

Each evaluator returns:

```yaml
dimension: D1_Soundness
score: 7
confidence: 4
strengths:
  - "Statistical tests reported with effect sizes"
  - "Assumptions explicit"
weaknesses:
  CRITICAL:
    - "Multiple testing not corrected (5 comparisons, no Bonferroni)"
  MAJOR:
    - "p < 0.05 reported but no CIs"
  MINOR:
    - "Variance estimator not specified"
fixes:
  - "Add Holm-Bonferroni correction in Section 3.2"
  - "Add 95% CI to Table 2"
score_change_criteria:
  - "Score will rise to 8.5 if multiple-testing correction added"
  - "Score will rise to 9 if CIs and effect sizes added throughout"
```
