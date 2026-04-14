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

---
---

# 评分标准（中文版）

> "权衡论证, 校释虚妄" — 王充《论衡》

本评分体系**直接对齐 NeurIPS、Nature、JACS 的真实审稿规范**。8 个维度均采用 **1–10 锚定评分**（1–3 / 4–6 / 7–8 / 9–10 四段都有显式锚点），让不同评审者收敛到相近分数。

## D1. 方法严谨性 (Soundness)

**测什么：** 技术正确性、claim-evidence 对齐、统计报告完整性、数学严谨性。
**对齐：** NeurIPS *Soundness*、Nature *Technical Rigor*、JACS *Scientific Quality*。

| 分数 | 锚点描述 |
|------|---------|
| **9–10** | 所有 claim 严格支撑；完整统计报告（CI、p 值、多重检验校正）；数学推导完整正确；假设显式声明 |
| **7–8** | 多数 claim 支撑良好；轻微统计细节缺失（如有 CI 但无效应量）；假设基本显式 |
| **4–6** | 部分 claim 过度伸展；关键比较缺显著性检验；假设隐式；论证临时拼凑 |
| **1–3** | 重大逻辑漏洞；伪造结果；数学错误；空洞 claim |

**红旗：** 多重比较 $p < 0.05$ 但无校正；临时统计方法；声称"显著优于"但未报告检验。

## D2. 重要性与原创性

**测什么：** 相对 SOTA 的进步、概念新颖性、对领域影响。
**对齐：** NeurIPS *Significance + Originality*（各 1–4）、Nature *Advance*、JACS *Conceptual Novelty*。

| 分数 | 锚点描述 |
|------|---------|
| **9–10** | 范式转变 / 首创 / 开辟新方向；结果可能被广泛引用复现 |
| **7–8** | 明显超越 SOTA；对公开问题有清晰贡献；方法有跨域价值 |
| **4–6** | 增量改进；在新场景复现已知结果；有用但有限 |
| **1–3** | 无明显进步；老结果重述；标准方法常规应用 |

**红旗：** 只对比弱 baseline；"首次"声明无文献检索支撑；缺乏"so what?"的回答。

## D3. 清晰度与组织

**测什么：** 写作流畅度、逻辑结构、段落衔接、术语一致性。
**对齐：** NeurIPS *Clarity*、JACS *Clarity of Writing*。

| 分数 | 锚点描述 |
|------|---------|
| **9–10** | 行文吸引人；每段推进叙事；术语统一；主题句清晰；逻辑过渡自然；零数据堆砌 |
| **7–8** | 写作清晰；轻微组织问题（一两节位置欠佳）；轻微术语漂移 |
| **4–6** | 大致可读；某些段落数据堆砌；跨章节术语漂移；翻译腔/被动语态过多 |
| **1–3** | 结构混乱；翻译腔遍布；关键结果埋没；术语未解释 |

**红旗：** 同概念三种叫法；图表先于上下文出现；该用散文却用"首先/其次/最后"。

## D4. 实验充分性

**测什么：** 实验、baseline、消融、样本量、误差报告的充分性。
**对齐：** NeurIPS *Quality*、Nature *Experimental Rigor*。

| 分数 | 锚点描述 |
|------|---------|
| **9–10** | 全面消融；同数据集多个 SOTA baseline；误差棒+种子；敏感性分析；预留测试集 |
| **7–8** | 良好消融；关键 baseline 包含；主结果有误差棒 |
| **4–6** | baseline 有限（或仅弱基线）；消融只在 SI；缺敏感性分析；样本量警告 |
| **1–3** | 无 baseline、无消融、无误差棒；实验功率不足；挑选结果 |

**红旗：** "3 次最优"作为均值汇报；无同数据集前作比较；消融表只在 SI 但是核心论点。

## D5. 可复现性

**测什么：** 独立研究者能否仅凭论文复现结果。
**对齐：** NeurIPS *Reproducibility Checklist*（16 项）、Nature *Code & Data Availability*。

按 [可复现性清单](REPRODUCIBILITY_CHECKLIST.md) 16 项打分：
- 9–10：满足 ≥ 14/16
- 7–8：11–13
- 4–6：7–10
- 1–3：≤ 6

**红旗：** "代码接收后发布"；超参用文字描述（"约 1000 epoch"）；训练/验证/测试划分未说明。

## D6. 引用质量

**测什么：** 相关工作覆盖、工具/方法引用、经典文献、引用密度均衡。
**对齐：** JACS *Literature Citations*、Nature *Contextualization*。

| 分数 | 锚点描述 |
|------|---------|
| **9–10** | 所有工具方法都引（RDKit、scikit-learn 等）；经典文献基础；密度均衡；无死引用 |
| **7–8** | 多数工具引用；覆盖良好；轻微缺引用 |
| **4–6** | 部分工具方法未引；引用密度不均（引言重，结果空）；有死引用 |
| **1–3** | 大量工具未引；关键前作缺失；bib 堆积大量未用；ref 损坏 |

**红旗：** "我们使用机器学习"无方法引用；用了工具但未引；bib 中 >50% 未被引用。

## D7. 图表沟通

**测什么：** 图质量、caption 自包含性、表格排版、布局、图文对齐。
**对齐：** Nature *Figure Quality*、NeurIPS *Presentation*、所有期刊排版规范。

| 分数 | 锚点描述 |
|------|---------|
| **9–10** | 出版级图；caption 自包含（不看正文也懂）；子图标签清晰；样式一致；表格列对齐；图文紧密 |
| **7–8** | 图清晰；轻微 caption 问题；布局基本紧凑 |
| **4–6** | 图可读但需正文上下文；某些 caption 仅标轴；表格列数不匹配 |
| **1–3** | 图不清/像素化/字看不清；caption 缺失或无意义；悬空 \\ref；图飘到错误章节 |

**红旗：** PDF 图嵌入 Word（显示空白）；图中有 (a)(b)(c) 但 caption 没说明；图出现在参考文献内。

## D8. 伦理、局限与影响

**测什么：** 局限性透明度、伦理考量、社会影响讨论。
**对齐：** NeurIPS *Limitations + Broader Impact + Ethics*、Nature *Ethics Statement*。

| 分数 | 锚点描述 |
|------|---------|
| **9–10** | 详细 Limitations 节涵盖假设违反和边界情况；伦理声明（如适用）；正负影响均讨论；数据 license 遵守 |
| **7–8** | 良好 Limitations；适用情况下伦理被处理 |
| **4–6** | Limitations 简短；适用时未讨论伦理 |
| **1–3** | 无 Limitations；忽视伦理问题；模型/数据无安全发布措施 |

**红旗：** Limitations 节只列"未来工作"；不讨论失败模式；医疗/生物特征数据无 IRB 声明。

## 整体评分

除 8 维度外，评估者还提供：

### Overall (1–6, NeurIPS式)
| 分数 | 判定 |
|------|------|
| **6** | 顶级论文，范式转变；立即接收 |
| **5** | 强接收；子领域高影响 |
| **4** | 边缘接收；扎实贡献，小问题 |
| **3** | 边缘拒收；有潜力，需大改 |
| **2** | 拒收；技术缺陷或弱实验 |
| **1** | 强烈拒收；根本性缺陷 |

### Confidence (1–5)
| 分数 | 含义 |
|------|------|
| **5** | 绝对确定；该子领域专家 |
| **4** | 自信；熟悉多数相关工作 |
| **3** | 较自信；相邻领域有些不确定 |
| **2** | 可能有理解漏洞；愿意辩护 |
| **1** | 凭直觉；非主要专长 |

### 综合分

$$ R = \frac{1}{8} \sum_{k=1}^{8} D_k $$

范围 1.0 – 10.0。$R \geq 7.0$ 或 `iteration >= MAX_ITERATIONS` 时停止迭代。

