# Lunheng Reproducibility Checklist

Adapted from the NeurIPS 2025 Paper Checklist, with extensions for chemistry/materials/physics papers. Each item is scored **Yes / Partial / No / N/A**.

A composite reproducibility score $D_5$ on the [main rubric](EVALUATION_RUBRIC.md):
- **9–10**: ≥ 14 of the 16 applicable items satisfied
- **7–8**: 11–13 satisfied
- **4–6**: 7–10 satisfied
- **1–3**: ≤ 6 satisfied

---

## Section A: Claims & Limitations

### A1. Claims–Abstract Alignment
> Do the claims in the abstract and introduction accurately reflect the paper's contributions and scope?

**Pass criteria:** Abstract claims are not stronger than what the experiments support. No "we prove" when only empirical evidence is given.

### A2. Limitations Section
> Does the paper include a Limitations section addressing assumptions, robustness violations, and failure modes?

**Pass criteria:** Distinct paragraph or subsection. Lists at least 3 concrete limitations. Not just "future work."

### A3. Theory Assumptions and Proofs
> Are theoretical results stated with full assumptions and complete proofs?

**Pass criteria:** Every theorem/proposition has explicit assumptions. Proofs in main text or appendix. **N/A** for purely empirical papers.

---

## Section B: Methodology Detail

### B1. Mathematical / Algorithmic Description
> Is the algorithm/model described with sufficient detail to be reimplemented?

**Pass criteria:** Pseudo-code, equations, or precise prose enabling reimplementation by an expert.

### B2. Hyperparameter Disclosure
> Are all hyperparameters reported with their search ranges and final values?

**Pass criteria:** Table or supplementary list of every hyperparameter. Search ranges declared. **Best values explicitly given** (not just "tuned via Optuna").

### B3. Train/Validation/Test Splits
> Are data splits exactly specified (sizes, random seeds, split criteria)?

**Pass criteria:** Sizes given. Splitting criteria documented (random / stratified / GroupKFold / temporal). Reproducible (seed or scripted).

### B4. Preprocessing Pipeline
> Is the preprocessing pipeline (cleaning, feature engineering, normalization) reproducible?

**Pass criteria:** Each step described or scripted. Decisions justified ("we removed X because Y").

---

## Section C: Experimental Setup

### C1. Statistical Significance
> Are error bars / CIs / standard deviations reported on main results?

**Pass criteria:** Mean ± SD or 95% CI on table values. Number of seeds/runs disclosed.

### C2. Multiple Comparisons
> If multiple methods/conditions are compared, is the multiplicity adjustment described?

**Pass criteria:** Bonferroni / Holm / FDR / paired t-test stated. **N/A** if only one comparison.

### C3. Compute Resources
> Is the compute budget (hardware, hours, memory) disclosed?

**Pass criteria:** GPU/CPU model, training time, memory peak. Allows readers to estimate cost.

---

## Section D: Code & Data

### D1. Code Availability
> Is code available for reproduction?

**Pass criteria:** Public repository (GitHub/GitLab/Zenodo). Not "available upon request." Not "will be released." **Partial** if only inference code is released.

### D2. Data Availability
> Is data available for reproduction?

**Pass criteria:** Public dataset (DOI, URL). License clear. **Partial** if data is released but processing scripts aren't.

### D3. Dependencies & Environment
> Are software dependencies pinned (versions) for reproduction?

**Pass criteria:** `requirements.txt`, `environment.yml`, `pyproject.toml`, or Dockerfile. Specific versions, not `>=`.

### D4. Random Seeds
> Are random seeds set and reported?

**Pass criteria:** Seeds in code; OR multiple seeds run and reported with variance.

---

## Section E: Ethics & Compliance

### E1. License Compliance
> If using existing assets (datasets, models, code), are creators cited and licenses respected?

**Pass criteria:** Each asset cited; licenses listed; conflicts noted.

### E2. Asset Documentation
> If releasing new assets, are they documented (model card / data card / dataset documentation)?

**Pass criteria:** README with usage, intended use, limitations, license.

### E3. Human Subjects / Animal Use
> If applicable, IRB/ethics approval documented?

**Pass criteria:** Approval ID, institution, consent procedure. **N/A** for non-applicable papers.

### E4. LLM Usage Declaration
> Is LLM usage in research process declared (if non-trivial)?

**Pass criteria:** "We used GPT-4 for code prototyping" type disclosure. **N/A** if only used for grammar.

---

## Section F: Domain Extensions (Chemistry / Materials)

> Use these for chemistry/materials/physics papers in addition to A–E above. Replace 2 of the N/A items above with these for a chemistry paper.

### F1. Material Synthesis Reproducibility
> Are synthesis protocols complete (precursor purity, solvent, T, time, yield)?

### F2. Characterization Methods
> Are characterization instruments and conditions specified (XRD model, BET conditions, TGA ramp rate)?

### F3. Spectroscopic Data Availability
> Are raw spectra / scattering / chromatograms deposited (e.g., Mendeley Data, Zenodo)?

### F4. Crystallographic Data
> If crystal structures reported, are CIF files deposited at CCDC?

---

## Scoring Examples

### Example 1: Strong reproducibility (D5 = 9.5)
- A1 ✓ A2 ✓ A3 N/A
- B1 ✓ B2 ✓ B3 ✓ B4 ✓
- C1 ✓ C2 ✓ C3 ✓
- D1 ✓ D2 ✓ D3 ✓ D4 ✓
- E1 ✓ E2 ✓ E3 N/A E4 ✓
- → 14 / 14 applicable = 100% → score 9.5

### Example 2: Typical materials paper (D5 = 7.0)
- A1 ✓ A2 partial A3 N/A
- B1 ✓ B2 partial B3 ✓ B4 ✓
- C1 ✓ C2 N/A C3 ✗
- D1 ✗ D2 ✓ D3 ✗ D4 partial
- E1 ✓ E2 N/A E3 N/A E4 N/A
- → 7 ✓ + 3 partial (=1.5) of 11 applicable ≈ 77% → score 7.0

---
---

# 可复现性清单

改编自 NeurIPS 2025 Paper Checklist，附化学/材料/物理论文扩展。每项打分 **Yes / Partial / No / N/A**。

D5 综合分映射：
- **9–10**：满足 ≥ 14 / 16 项
- **7–8**：11–13
- **4–6**：7–10
- **1–3**：≤ 6

## A 节：声明与局限

### A1. 摘要-Claim 对齐
> 摘要和引言中的 claim 是否准确反映论文贡献和范围？

**通过条件：** 摘要 claim 不强于实验支撑。仅有经验证据时不写"我们证明"。

### A2. Limitations 章节
> 论文是否含独立 Limitations 节，讨论假设、健壮性违反、失败模式？

**通过条件：** 独立段落或子节。至少列 3 条具体局限。不能只是"未来工作"。

### A3. 理论假设与证明
> 理论结果是否含完整假设和完整证明？

**通过条件：** 每个 theorem/proposition 都有显式假设。证明在正文或附录。**纯实验论文 N/A。**

## B 节：方法学细节

### B1. 数学/算法描述
> 算法/模型是否描述足够清晰可被重新实现？

**通过条件：** 伪代码、方程或精确文字让专家可重现。

### B2. 超参数披露
> 所有超参数及其搜索范围、最终取值是否报告？

**通过条件：** 表格或附录列每个超参；声明搜索范围；**显式给出最优值**（不能只说"用 Optuna 调"）。

### B3. 训练/验证/测试划分
> 数据划分是否精确说明（大小、随机种子、划分准则）？

**通过条件：** 大小给出；划分准则文档化（随机/分层/GroupKFold/时间）；可复现（种子或脚本化）。

### B4. 预处理流程
> 预处理流程（清洗、特征工程、归一化）是否可复现？

**通过条件：** 每步描述或脚本化；决策有依据（"我们删除 X 因为 Y"）。

## C 节：实验设置

### C1. 统计显著性
> 主结果是否报告误差棒/CI/标准差？

**通过条件：** 表格值给均值±SD 或 95% CI；种子/run 数披露。

### C2. 多重比较
> 多方法/条件比较时，多重性调整是否说明？

**通过条件：** 说明 Bonferroni / Holm / FDR / paired t-test。**单一比较 N/A。**

### C3. 计算资源
> 计算预算（硬件、小时数、内存）是否披露？

**通过条件：** GPU/CPU 型号、训练时间、内存峰值；让读者能估算成本。

## D 节：代码与数据

### D1. 代码可用性
> 代码是否可获取以复现？

**通过条件：** 公开仓库（GitHub/GitLab/Zenodo）；不能"应要求提供"或"接收后发布"。**Partial** 若仅 inference 代码。

### D2. 数据可用性
> 数据是否可获取以复现？

**通过条件：** 公开数据集（DOI、URL）；license 清晰。**Partial** 若数据公开但处理脚本未公开。

### D3. 依赖与环境
> 软件依赖是否锁版本以便复现？

**通过条件：** `requirements.txt`、`environment.yml`、`pyproject.toml` 或 Dockerfile；具体版本号，不是 `>=`。

### D4. 随机种子
> 随机种子是否设置并报告？

**通过条件：** 代码中设种子；或多种子运行并报告方差。

## E 节：伦理与合规

### E1. License 合规
> 使用的资源（数据集、模型、代码）是否引用作者并尊重 license？

**通过条件：** 每个资源都引用；license 列出；冲突说明。

### E2. 资源文档
> 发布新资源是否文档化（model card / data card / dataset documentation）？

**通过条件：** README 含使用、预期用途、局限、license。

### E3. 人体/动物
> 如适用，IRB/伦理审批是否文档化？

**通过条件：** 审批 ID、机构、知情同意流程。**不适用 N/A。**

### E4. LLM 使用声明
> 研究流程中的 LLM 使用是否声明（若非琐碎）？

**通过条件：** 类似"我们使用 GPT-4 做代码原型"的声明。**仅用于语法校对 N/A。**

## F 节：领域扩展（化学/材料）

> 化学/材料/物理论文使用以下项替代上面 N/A 的某些项。

### F1. 材料合成可复现性
> 合成方案是否完整（前驱体纯度、溶剂、T、时间、产率）？

### F2. 表征方法
> 表征仪器和条件是否说明（XRD 型号、BET 条件、TGA 升温速率）？

### F3. 谱学数据可用性
> 原始谱图/散射/色谱是否存档（如 Mendeley Data、Zenodo）？

### F4. 晶体学数据
> 报告晶体结构时，CIF 文件是否在 CCDC 存档？

