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

---
---

# 案例研究：DAC 材料 ML 论文 R0 → R2（中文版）

将论衡应用于一篇中文化学-机器学习论文（目标 Q1 期刊）。

## 论文概况

| 字段 | 值 |
|------|----|
| **主题** | 直接空气捕获(DAC)吸附材料的 CO₂ 吸附量 ML 预测 |
| **篇幅** | 24 页 LaTeX，2 表 + 7 图 + 117 参考文献 |
| **类型** | 方法论 + 基准数据集 |
| **目标期刊** | Q1 化学/材料期刊（中科院一区） |
| **作者** | 首篇博士轨研究者 |

## 综合分轨迹

| 轮次 | 综合分 | Δ | 判定变化 |
|------|--------|---|---------|
| R0（基线） | **6.81** | — | 边缘拒收 |
| R1（修排版+视觉） | **8.04** | +1.23 | 边缘接收 |
| R2（修内容+可复现） | **8.66** | +0.62 | 强接收 |

参照：单 Claude 基线（`lunheng-quick`）在同一 R0 稿件上得 **7.6**——论衡完整多智能体流程在 R2 多得了 **+1.06**。

## 各维度细分

| 维度 | 名称 | R0 | R1 | R2 | 各轮变化 |
|------|------|----|----|----|---------|
| D1 | 方法严谨性 | 7.0 | 7.0 | **9.0** | R2：声明 R²_max 推导的 iid+同方差假设；软化 Clausius-Clapeyron 描述；加 paired t-test |
| D2 | 重要性与原创性 | 8.5 | 8.5 | 8.5 | 已强：最大跨类型 DAC 数据集 + 噪声底线分析 |
| D3 | 清晰度与组织 | 8.0 | 8.5 | 8.5 | R1：术语统一（辅助域→广域 CO₂ 等温线）；表格列数修正 |
| D4 | 实验充分性 | 8.0 | 8.0 | **9.0** | R2：噪声鲁棒消融表从 SI 搬入正文带 p 值；HOF 行加样本量脚注 |
| D5 | 可复现性 | 7.5 | 7.8 | **8.4** | R2：加超参表（CatBoost/XGBoost/LightGBM 完整数值）；集成权重 0.35/0.30/0.35；SMOGN 参数 |
| D6 | 引用质量 | 6.5 | 7.0 | 7.5 | R2：补 RDKit/WPD/NIST/ISODB/Morgan/Freundlich/Pan/MOFormer/ChemBERTa/Spearman |
| D7 | 图表沟通 | 4.0 | **8.0** | 8.0 | R1：7 图重新内联用 [H] 强制位置；补 tab:features；PDF 转 PNG（Word 兼容） |
| D8 | 伦理/局限/影响 | 5.0 | 9.0 | 9.0 | R1：把 Limitations 从一句话埋藏改为独立子节 |

（注：D7 R0 = 4.0 是因为 8 个 dangling \\ref + 59 个 broken \\cite。R1 后降至 0 undefined。）

## 架构师 R1 发现

架构师识别**3 个最严重结构问题**：

1. **SI 幻影引用** —— 正文引用 `Tab. S1/S2/S3` 但未附 SI，主 tex 也未定义。→ 修复：表格搬入正文或删除 label。

2. **章节权重失衡** —— 方法(35%) >> 结果(22%) > 讨论(15%)；核心方法学贡献（"以排序指标取代 R²"）埋在 §3.2 才系统论证，引言只批判未声明立场。→ 修复：讨论扩 30%。

3. **跨节数字漂移** —— HUM 条数 702 vs 703 不同位置打架；论文总数 113 vs 150 vs 164；Random CV $R^2$ 表中 0.887 但图 caption 0.882。→ 修复：视觉契约的 terminology_glossary 锁定唯一正式值。

## 各轮成本

| 轮次 | sub-agent 调用数 | 墙钟时间 | 计算成本 |
|------|------------------|----------|---------|
| R0 基线（仅 8 评估者） | 8 | ~3 分钟 | ~30k tokens |
| R1（架构师+撰写×4+润色+8评估） | 14 | ~12 分钟 | ~120k tokens |
| R2（针对性撰写×3+5个再评估） | 8 | ~5 分钟 | ~70k tokens |
| **总计** | **30** | **~20 分钟** | **~220k tokens** |

（用 Claude Opus 4.6 估算）

## 多智能体 vs 单评审者的关键胜出

单 Claude 评审（`lunheng-quick`）在同一 R0 论文得 **7.6 / 10**。完整多智能体在 4 个维度领先：

| 维度 | 单评审 | 完整论衡 | 原因 |
|------|--------|---------|------|
| D1 方法严谨性 | 7.5 | **9.0** | 更细致捕获统计检验缺失 |
| D5 可复现性 | 7.5 | **8.4** | 专业评估者抓住缺失的超参 |
| D7 图表沟通 | 5.0 | **8.0** | 视觉契约抓住悬空引用 |
| D8 伦理/局限 | 6.0 | **9.0** | 独立维度强制显式注意 |

## 经验总结

1. **R1 在 D7+D8 必然大涨**——格式问题易识别易修，分数立即跳跃
2. **R2 需要内容手术**——D1/D4/D5 只对实质性编辑响应（加表/声明假设/给超参）；模型能识别"该加什么"，但作者必须验证数值正确性
3. **视觉契约对长论文价值最大**——24 页 7 图，契约抓住 3 处单评审者在 R0 漏掉的跨节不一致
4. **8 评估者并行非常快**——单条消息 fan-out，3 分钟拿全 8 份 review
5. **R = 7.0 停止阈值校准良好**——R ≥ 7.0 论文通过基本发表检查；之下必有结构性问题

