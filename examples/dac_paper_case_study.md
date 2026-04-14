# Case Study: DAC Materials ML Paper (R0 → R3)

A real-world application of Lunheng on a Chinese-language chemistry-ML manuscript targeting a Q1 journal.

## Paper Snapshot

| Field | Value |
|-------|-------|
| **Topic** | ML prediction of CO₂ adsorption on Direct Air Capture (DAC) sorbents |
| **Length** | 28 pages (LaTeX), 5 tables + 7 figures + 117 references |
| **Type** | Methodology + benchmark dataset |
| **Target venue** | Q1 chemistry/materials journal (CAS Tier 1) |
| **Author** | First-time master's-track researcher |

## Composite Score Trajectory

| Round | Composite $R$ | Verdict | Key changes |
|-------|---------------|---------|-------------|
| **R0** (baseline) | **6.89** | Borderline reject | Original draft, evaluated against the Lunheng rubric anchors |
| **R3** (after gap fixes) | **8.04** | Borderline accept | All five low-scoring dimensions targeted with concrete fixes |

For perspective, the single-Claude baseline (`lunheng-quick`) on the same R0 manuscript scored **7.6** but missed several substantive issues that the multi-agent Lunheng caught (e.g., missing bootstrap CIs, no Data Availability statement, 6 overfull hboxes including a 127pt overflow).

## Per-Dimension Breakdown

| Dim | Dimension | R0 | R3 | Δ | What changed |
|-----|-----------|----|----|----|--------------|
| D1 | Soundness | 7.0 | **8.2** | +1.2 | Added bootstrap 95% CI ($n=1000$) on R²/MAE/ρ; Wilcoxon signed-rank test alongside paired t-test for ablations |
| D2 | Significance & Originality | 6.5 | 6.5 | 0 | Untouched; remaining gap = no head-to-head SOTA comparison + no quantified "so-what" |
| D3 | Clarity & Organization | 8.0 | 8.0 | 0 | Already strong; minor terminology drift remains |
| D4 | Experimental Substance | 7.0 | **7.5** | +0.5 | Added `tab:ensemble_ablation` (single CatBoost / XGBoost / LightGBM vs. ensemble vs. Hybrid); main results now show CIs. External baselines (RF / MLP) still missing |
| D5 | Reproducibility | 6.5 | **8.5** | +2.0 | Full Data and Code Availability section: GitHub URL, Zenodo DOI commitment, CC-BY 4.0 / MIT licenses, 7 dependency versions, RTX 4090 / training time / memory disclosed |
| D6 | Citation Quality | 7.5 | 7.5 | 0 | Untouched; bib utilization 53% (53 unused entries) needs cleanup |
| D7 | Visual & Tabular Communication | 7.6 | **9.1** | +1.5 | Fixed 6 overfull hboxes (max 127pt → 0pt for tables); `tab:features` switched to `p{}` columns; column names shortened |
| D8 | Ethics, Limitations & Broader Impact | 5.0 | **9.0** | +4.0 | Independent Broader Impact section: positive impact (15–20× experimental cost reduction), negative impact + mitigations (applicability domain warnings), carbon footprint (25 kWh / 15 kg CO₂eq), conflict-of-interest statement, TDM compliance for the 164-paper extraction |
| **R** | **Composite** | **6.89** | **8.04** | **+1.15** | |

## Architect Findings (R0)

The Architect agent identified **3 most severe structural issues**:

1. **SI Phantom References** — main text cited `Tab. S1`, `Tab. S2`, `Tab. S3` but no SI document was attached and no tables were defined. → Fix: tables moved into main text.

2. **Number Drift Across Sections** — HUM count was 702 vs 703 in different tables; total paper count was 113 vs 150 vs 164; Random CV $R^2$ was 0.887 in Table but 0.882 in Figure caption. → Fix: the Visual Contract's `terminology_glossary` enforced single canonical values.

3. **Section Weight Imbalance** — Methods (35%) >> Results (22%) > Discussion (15%); the central methodological contribution ("ranking metrics over $R^2$") was buried in §3.2 instead of being foregrounded. → Fix: Discussion expanded with the evaluation-paradigm argument.

## Anchored-Score Examples

How Lunheng's anchored anchors translate to actionable fixes:

### D5 Reproducibility went 6.5 → 8.5 because:
- **R0 anchor 4–6 triggered:** "code 'will be released'; hyperparameters described in prose"
- **R3 anchor 7–8 reached:** "code+data available, key hyperparams given" (added `tab:hyperparams` with exact values for all 3 models, ensemble weights 0.35/0.30/0.35, full dependency version list)
- **What's still missing for 9–10:** the GitHub repo URL needs a real Zenodo DOI (registered post-acceptance); a `requirements.txt` with pinned versions; once those land, the score crosses 9

### D8 Ethics went 5.0 → 9.0 because:
- **R0 anchor 4–6 triggered:** "brief Limitations paragraph; ethics not discussed"
- **R3 anchor 9–10 reached:** "detailed limitations + ethics statement + broader impact + license" — added Broader Impact section quantifying both positive (15–20× screening cost reduction) and negative (false-positive risk) impacts, plus carbon footprint and TDM compliance

## What Each Round Cost

| Phase | Sub-agent calls | Wall time | Compute cost |
|-------|-----------------|-----------|--------------|
| R0 baseline (8 evaluators in parallel) | 8 | ~5 min | ~40k tokens |
| R3 targeted fixes (5 re-evaluators on changed dimensions) | 5 | ~3 min | ~25k tokens |
| **Total** | **13** | **~8 min** | **~65k tokens** |

(Tokens approximate, using Claude Opus 4.6.)

## Key Methodological Wins (Multi-Agent vs. Single-Reviewer)

A single Claude reviewer (`lunheng-quick`) on the same R0 paper scored **7.6 / 10** — higher than Lunheng's **6.89**. Why is the multi-agent score *lower* yet *more useful*?

Because the single reviewer **missed several issues** that Lunheng's specialized evaluators caught:

| Dimension | Single reviewer | Lunheng (8 evaluators) | What single reviewer missed |
|-----------|-----------------|------------------------|-----------------------------|
| D1 Soundness | "Looks rigorous" | 7.0 | No bootstrap CI; no multiple-testing correction |
| D5 Reproducibility | "Has hyperparameters" | 6.5 | No GitHub URL; no compute disclosure; no library versions |
| D7 Visual | "Figures are nice" | 7.6 | 6 overfull hboxes including 127pt severe overflow in tab:features |
| D8 Ethics | "Has Limitations" | 5.0 | No Data Availability; no Broader Impact; no TDM compliance |

The lower R0 score is **not** "Lunheng being harsh" — it's anchor-based scoring revealing what a generalist reviewer glossed over. The R3 work that brought the paper to 8.04 was directly guided by Lunheng's per-dimension `score_change_criteria` outputs.

## Lessons Learned

1. **Anchored scoring exposes blind spots.** A free-form reviewer easily gives 8/10 to a paper missing Data Availability if it reads well; Lunheng's D8 anchors force the question "is there a license? a code URL?" — and the answer was no.

2. **Targeted fixes are cheap.** R3's gap-fix round used only 5 re-evaluators (no need for full re-architect); the targeted approach lifted the composite from 6.89 to 8.04 in ~8 minutes of wall time.

3. **Some dimensions don't move without external work.** D2 Significance stays at 6.5 until the authors actually do head-to-head SOTA comparison and quantify "so-what" — Lunheng can identify this gap but cannot fabricate the experiments.

4. **The Visual Contract pays off most for long papers** — for our 28-page paper with 7 figures and 5 tables, the contract caught 3 separate cross-section number inconsistencies that the single reviewer flagged as "minor" while the dedicated structural evaluator flagged as MAJOR.

5. **The composite $R = 7.0$ stop threshold is well-calibrated** — at $R = 8.04$ the paper passes basic publication checks; the remaining gap to top-tier ($R \geq 8.5$) is honest content work (external baselines, SOTA comparison) that no agent can shortcut.

## Reproducibility of This Case Study

All raw agent outputs are preserved in the `paper_final/lunheng_workspace/` and `paper_final/s2p_workspace/` directories of the source project (TODO: anonymize and upload to `examples/dac_artifacts/`):
- `blueprint.md`
- `visual_contract.json`
- 8 R0 evaluator outputs (raw)
- 5 R3 re-evaluator outputs (raw)
- Per-round LaTeX diffs

A reader can re-run any individual sub-agent with the saved prompt to verify the score it returned.

---
---

# 案例研究：DAC 材料 ML 论文 R0 → R3

将论衡应用于一篇中文化学-机器学习论文（目标 Q1 期刊）。

## 论文概况

| 字段 | 值 |
|------|----|
| **主题** | 直接空气捕获(DAC)吸附材料的 CO₂ 吸附量 ML 预测 |
| **篇幅** | 28 页 LaTeX，5 表 + 7 图 + 117 参考文献 |
| **类型** | 方法论 + 基准数据集 |
| **目标期刊** | Q1 化学/材料期刊（中科院一区） |
| **作者** | 首篇硕士轨研究者 |

## 综合分轨迹

| 轮次 | 综合分 $R$ | 判定 | 关键变化 |
|------|-----------|------|---------|
| **R0**（基线） | **6.89** | 边缘拒收 | 原始草稿，按论衡rubric评估 |
| **R3**（修补缺口后） | **8.04** | 边缘接收 | 5个低分维度针对性修复 |

参照：单 Claude 评审（`lunheng-quick`）在同一 R0 稿件得 **7.6**——表面上比论衡的 6.89 高，但**漏掉了多个实质性问题**（缺 bootstrap CI、缺 Data Availability、6 处 overfull hbox 包括 127pt 严重溢出）。这正是多智能体的价值。

## 各维度细分

| 维度 | 名称 | R0 | R3 | Δ | 各轮变化 |
|------|------|----|----|----|---------|
| D1 | 方法严谨性 | 7.0 | **8.2** | +1.2 | 加 bootstrap 95% CI ($n=1000$) 于 R²/MAE/ρ；消融加 Wilcoxon 符号秩检验 |
| D2 | 重要性与原创性 | 6.5 | 6.5 | 0 | 未改；剩余 gap = 无 head-to-head SOTA + 无 so-what 量化 |
| D3 | 清晰度与组织 | 8.0 | 8.0 | 0 | 已强；轻微术语漂移仍存 |
| D4 | 实验充分性 | 7.0 | **7.5** | +0.5 | 加 tab:ensemble_ablation（单CatBoost/XGBoost/LightGBM vs 集成 vs Hybrid）；主结果加 CI。但外部 baseline (RF/MLP) 仍缺 |
| D5 | 可复现性 | 6.5 | **8.5** | +2.0 | 完整数据与代码可用性章节：GitHub URL、Zenodo DOI、CC-BY 4.0/MIT license、7 个依赖版本、RTX 4090/训练时间/内存披露 |
| D6 | 引用质量 | 7.5 | 7.5 | 0 | 未改；bib 利用率 53%（53 条未用）需清理 |
| D7 | 图表沟通 | 7.6 | **9.1** | +1.5 | 修 6 处 overfull hbox（127pt→0pt 表格）；tab:features 改 p{} 列；列名缩短 |
| D8 | 伦理/局限/影响 | 5.0 | **9.0** | +4.0 | 独立 Broader Impact 节：正向影响（15-20倍实验成本下降）、负向影响+缓解（applicability domain）、碳足迹（25 kWh/15 kg CO₂eq）、利益冲突声明、164 篇文献提取的 TDM 合规 |
| **R** | **综合** | **6.89** | **8.04** | **+1.15** | |

## 架构师 R0 发现

架构师识别**3 个最严重结构问题**：

1. **SI 幻影引用** —— 正文引用 `Tab. S1/S2/S3` 但未附 SI，主 tex 也未定义。→ 修复：表格搬入正文。

2. **跨节数字漂移** —— HUM 条数 702 vs 703 不同位置打架；论文总数 113 vs 150 vs 164；Random CV $R^2$ 表中 0.887 但图 caption 0.882。→ 修复：视觉契约的 terminology_glossary 锁定唯一正式值。

3. **章节权重失衡** —— 方法(35%) >> 结果(22%) > 讨论(15%)；核心方法学贡献（"以排序指标取代 R²"）埋在 §3.2 才系统论证。→ 修复：扩充讨论。

## 锚定评分如何指导修复

### D5 可复现性 6.5 → 8.5 的原因
- **R0 触发 4-6 锚点**："代码'将公开发布'；超参用文字描述"
- **R3 达到 7-8 锚点**："code+data 可用、关键超参给出"（加了 `tab:hyperparams` 含三模型完整数值、集成权重 0.35/0.30/0.35、依赖版本列表）
- **冲 9-10 还差**：补 Zenodo DOI（论文录用后注册）+ 锁版本的 `requirements.txt`，即可跨 9 分

### D8 伦理 5.0 → 9.0 的原因
- **R0 触发 4-6 锚点**："Limitations 简短；未讨论伦理"
- **R3 达到 9-10 锚点**："详细 Limitations + 伦理声明 + Broader Impact + license"——加了 Broader Impact 节量化正负影响，加了碳足迹和 TDM 合规

## 各阶段成本

| 阶段 | sub-agent 调用数 | 墙钟时间 | 计算成本 |
|------|------------------|----------|---------|
| R0 基线（8 评估者并行） | 8 | ~5 分钟 | ~40k tokens |
| R3 针对性修复（5 个再评估）| 5 | ~3 分钟 | ~25k tokens |
| **总计** | **13** | **~8 分钟** | **~65k tokens** |

（用 Claude Opus 4.6 估算）

## 经验总结

1. **锚定评分暴露盲点**——自由格式评审容易给 8/10，论衡 D8 锚点强制问"有 license 吗？有代码 URL 吗？"——发现答案是没有

2. **针对性修复成本极低**——R3 只用 5 个再评估者（无需重启完整架构师），8 分钟把综合分从 6.89 拉到 8.04

3. **某些维度需要外部工作**——D2 重要性卡在 6.5，直到作者真做 head-to-head SOTA 对比并量化 so-what；论衡能识别但不能伪造实验

4. **视觉契约对长论文价值最大**——28 页 7 图，契约抓住 3 处单评审者认为"小问题"但专业评估者标 MAJOR 的跨节不一致

5. **R = 7.0 停止阈值校准良好**——R = 8.04 通过基本发表检查；再上 8.5 的差距是诚实的内容工作（外部 baseline、SOTA 对比），无法取巧
