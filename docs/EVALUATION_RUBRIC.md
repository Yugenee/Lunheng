# Lunheng Evaluation Rubric (论衡评价标准)

> "权衡论证, 校释虚妄" — 王充《论衡》
>
> Weighing arguments, examining what is false — *Lunheng*, Wang Chong (~80 CE)

This rubric is **aligned with the actual scoring practices of NeurIPS, Nature, and JACS**. Each of the 9 dimensions (D1–D9, D9 added in v2.0) uses a **1–10 scale with anchored anchors** at four levels (1–3 / 4–6 / 7–8 / 9–10), so different evaluators converge on similar scores.

### Anatomy of each dimension

For every dimension below you will see three blocks:

- **What it measures** — one-line definition of the dimension.
- **Aligned with** — the venue rubric this anchor inherits from.
- **Score table (1–10 with anchors)** — explicit description of what each band looks like; evaluators must reference these anchors when assigning a score, not vibes.
- **Red flags** — specific symptoms that automatically push the score into the 4–6 or lower band. Think of them as "smell tests": if a paper shows any red flag, the dimension cannot exceed 6 unless the evaluator gives a concrete justification for why the symptom does not apply.

---

## D1. Soundness 

**What it measures:** Technical correctness, claim–evidence alignment, statistical reporting, mathematical rigor.

**Aligned with:** NeurIPS *Soundness*, Nature *Technical Rigor*, JACS *Scientific Quality*.

| Score | Anchor |
|-------|--------|
| **9–10** | All claims rigorously supported; full statistical reporting (CIs, p-values, multiple testing); mathematical derivations complete and sound; assumptions explicitly stated. |
| **7–8** | Most claims well supported; minor statistical detail gaps (e.g., CI but no effect size); assumptions mostly explicit. |
| **4–6** | Some claims overreach; missing significance tests on key comparisons; assumptions implicit; ad-hoc justifications. |
| **1–3** | Major logical gaps; fabricated results; mathematical errors; unsupported sweeping claims. |

**Red flags:** $p < 0.05$ without correction for multiple testing; ad-hoc statistical methods; claims of "significantly better" without test reported.

**Overclaim trigger-word checklist (v2.2):** the following words, when used in main text without an explicit scope/evidence footnote within 2 sentences, automatically deduct 1 point from D1.

| Trigger | Safer replacement |
|---|---|
| `prove` / `proves` / `proven` | `show` / `demonstrate` |
| `conclusively` | `consistently` / (delete) |
| `unprecedented` | `among the strongest reported` |
| `best` / `superior` (unqualified) | `best in this benchmark` / `among the top` |
| `first` (unqualified) | `to our knowledge, the first` |
| `definitely` / `obviously` / `clearly` | (delete) |
| `significantly better` (no test reported) | report the test + p-value, OR use `outperforms` |

**Hedging calibration ladder.** Match verb strength to evidence strength. Flag any sentence whose verb sits one rung above what the evidence supports.

```
demonstrate (strong) ← suggest (moderate) ← may reflect (weak) ← is consistent with (very weak)
```

---

## D2. Significance & Originality 
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

## D3. Clarity & Organization 

**What it measures:** Writing flow, logical structure, paragraph cohesion, terminology consistency.

**Aligned with:** NeurIPS *Clarity*, JACS *Clarity of Writing*.

| Score | Anchor |
|-------|--------|
| **9–10** | Engaging writing; every paragraph advances narrative; consistent terminology; topic sentences clear; logical transitions; no data-dumping. |
| **7–8** | Clear writing; minor organizational issues (one or two sections feel out of place); minor terminology drift. |
| **4–6** | Mostly readable; some sections drag with data dumping; terminology drift across sections; awkward translations / passive voice overuse. |
| **1–3** | Confusing structure; rampant translation-style language; key results buried; jargon without explanation. |

**Red flags:** Same concept named 3 different ways; tables/figures referenced before context; "first/second/third" lists where prose is needed.

**Section-syntax drift anchors (v2.2):**

| Drift | Penalty |
|---|---|
| Results paragraph uses Discussion-style hedging (`may`, `suggests`, `could indicate`, `is likely due to`) | -1 on D3 |
| Discussion paragraph is pure past-tense result restatement with no `may` / `suggest` / `consistent with` / `bounded by` | -1 on D3 |
| Methods uses vague stand-ins (`under standard conditions`, `routine methods`, `analyzed statistically`, `the method was validated`) | -1 on D3 **and** -1 on D5 |

**Paragraph-final sentence check (v2.2):** the last sentence of each paragraph is the most likely to bloat or drift. It should close the controlling idea, not stuff a tangential detail or new noun phrase. If the final sentence is `> 35 words` **and** introduces a noun phrase absent from the topic sentence, deduct 1 from D3 and tag for split.

---

## D4. Experimental Substance

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

## D5. Reproducibility 

**What it measures:** Whether an independent researcher can reproduce the results from the paper alone.

**Aligned with:** NeurIPS *Reproducibility Checklist* (16 items), Nature *Code & Data Availability*.

Use the [Reproducibility Checklist](REPRODUCIBILITY_CHECKLIST.md) (16 items adapted from NeurIPS) to score:
- 9–10: ≥ 14 / 16 items satisfied
- 7–8: 11–13 items satisfied
- 4–6: 7–10 items satisfied
- 1–3: ≤ 6 items satisfied

**Red flags:** "Code will be released upon acceptance"; hyperparameters described in prose only ("around 1000 epochs"); train/val/test splits unspecified.

---

## D6. Citation Quality 
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

## D7. Visual & Tabular Communication 

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

## D8. Ethics, Limitations & Broader Impact 

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

## D9. Narrative Flow & Conciseness [v2.0]

**What it measures:** Whether the paper respects the venue word budget and reads as a single connected narrative rather than a fragmented FAQ or spec sheet.

**Aligned with:** venue-specific length limits (Nature article, NeurIPS page limit, JACS communication limit, thesis chapter budget).

| Score | Anchor |
|-------|--------|
| **10** | Within 100% of venue budget; `\paragraph` count ≤ recommended; every cut would damage a claim. |
| **8–9** | Within 110% of budget; `\paragraph` count ≤ 1.5× recommended; minor tightening still possible. |
| **7** | Within 125% of budget OR 1–2 excess `\paragraph` blocks cause minor narrative fragmentation. |
| **5–6** | Within 150% of budget OR reads as FAQ / spec sheet rather than continuous prose. |
| **3–4** | > 150% of budget OR section flow broken by > 5 excess small-headings. |
| **1–2** | ≥ 2× budget or unreadable as a single-narrative paper. |

**Venue budget table:**

| venue | Main text | Abstract | `\paragraph` cap |
|-------|----------:|---------:|:----:|
| `journal` (JMC A / CEJ / JACS / Digital Discovery) | 8–10k CN chars | 200–350 chars | ≤ 3 |
| `nature_sub` (Nat Comm / Nat Comp Sci) | 2.5–3.5k | ≤ 250 EN words | 0 |
| `conference` (NeurIPS / ICML) | 6–8k EN words | 150–200 words | ≤ 2 |
| `thesis` (本科 / 硕士毕业) | 15–30k | 400–800 | allowed |

**Red flags:** Limitations expanded to 6 enumerate items to chase a D8 high band; `\paragraph{协议}` for every method micro-detail; Broader Impact > 1000 chars to defend against an Ethics reviewer.

**Stop-gate:** if word count is > 125% of venue budget, **R ≥ 7.0 alone does not stop iteration** — Chief Editor compression is forced.

---

## Holistic Scores

In addition to the 9 dimensions, evaluators provide:

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

$$ R = \frac{1}{9} \sum_{k=1}^{9} D_k \quad\text{(v2.0: 9 dimensions, includes D9 Narrative)} $$

Range: 1.0 – 10.0. **v2.0 stop criterion:** stop iteration when $R \geq 7.0$ **AND** word count $\leq$ venue budget $\times 1.10$, OR `iteration >= MAX_ITERATIONS`. R alone passing while word count > 125% budget triggers Chief Editor compression instead of stopping.

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

# 评分标准

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

**Overclaim 触发词清单 (v2.2)：** 以下词在正文中出现且 2 句内无显式 scope/证据脚注时，自动 D1 -1。

| 触发词 | 安全替代 |
|---|---|
| `prove` / `proves` / `proven` / `证明` | `show` / `demonstrate` / `表明` |
| `conclusively` / `决定性地` | `consistently` / 删除 |
| `unprecedented` / `史无前例` | `among the strongest reported` / `迄今最强之一` |
| `best` / `superior` / `最佳`（无限定） | 加 cohort：`best in this benchmark` / `本基准内最佳` |
| `first` / `首次`（无限定） | `to our knowledge, the first` / `据我们所知首次` |
| `definitely` / `obviously` / `clearly` / `显然` | 删除——让证据自证 |
| `significantly better` / `显著优于`（未报告检验） | 报告检验+p 值，或用 `outperforms` / `优于` |

**Hedging 校准阶梯：** 动词强度必须匹配证据强度。任何句子的动词高出证据一档 → 标红。

```
demonstrate (强) ← suggest (中) ← may reflect (弱) ← is consistent with (很弱)
```

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

**章节句法漂移 anchors (v2.2)：**

| 漂移类型 | 扣分 |
|---|---|
| Results 段使用 Discussion 风格 hedging（`may` / `suggests` / `could indicate` / `is likely due to` / `可能反映` / `推测` ） | D3 -1 |
| Discussion 段全是过去时结果罗列，缺 `may` / `suggest` / `consistent with` / `bounded by` / `可能` / `提示` / `受限于` | D3 -1 |
| Methods 用模糊套话（`under standard conditions` / `routine methods` / `analyzed statistically` / `the method was validated` / `常规方法` / `统计分析` / `方法已验证`） | D3 -1 **且** D5 -1 |

**段尾句检查 (v2.2)：** 每段最后一句最容易膨胀或漂移。它应该收束 controlling idea，不该塞旁支细节或新名词短语。若段尾句 `> 35 词` **且** 引入主题句中没有的新名词短语 → D3 -1，标记需拆分。

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

### D9 Narrative Flow & Conciseness (v2.0 新增)

对齐 venue-specific 字数预算, 惩罚冗长和 FAQ 式片段化。

| 分数 | 锚点 |
|------|------|
| **10** | 字数 ≤ venue 预算 100%; `\paragraph` 小标题数 ≤ 推荐值; 删任何一处都会伤 claim |
| **8-9** | 字数 ≤ 110% 预算; `\paragraph` ≤ 1.5× 推荐; 可轻微精简 |
| **7** | 字数 ≤ 125% 预算 OR 1-2 处多余 `\paragraph` 造成微弱叙事断裂 |
| **5-6** | 字数 ≤ 150% 预算 OR 读起来像 FAQ / 规格说明而非论文散文 |
| **3-4** | 字数 > 150% 预算 OR 超过 5 个多余小标题打断章节流畅度 |
| **1-2** | 字数 ≥ 2× 预算或无法作为单一叙事论文阅读 |

**venue 预算表**:

| venue | 正文 | 摘要 | `\paragraph` 上限 |
|-------|-----:|-----:|:----:|
| `journal` (JMC A / CEJ / JACS / Digital Discovery) | 8-10k CN 字 | 200-350 字 | ≤ 3 |
| `nature_sub` (Nat Comm / Nat Comp Sci) | 2.5-3.5k | ≤ 250 英文 words | 0 |
| `conference` (NeurIPS / ICML) | 6-8k 英文 words | 150-200 words | ≤ 2 |
| `thesis` (本科 / 硕士毕业) | 15-30k | 400-800 | 允许 |

**D9 stop-gate**: 字数超预算 > 25% 时即使 R ≥ 7.0 也不停, 强制触发 Chief Editor 压缩。

### 综合分

$$ R = \frac{1}{9} \sum_{k=1}^{9} D_k \quad\text{(v2.0: 9 维度)} $$

范围 1.0 – 10.0。**v2.0 stop criterion**: $R \geq 7.0$ **且** 字数 ≤ venue 预算 × 1.10 才停止迭代。单纯 R 达标但字数超标 → 跳过 Writer, 只跑 Chief Editor 压缩。

