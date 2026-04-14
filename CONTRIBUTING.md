# Contributing to Lunheng

Thanks for considering a contribution! Lunheng is a Claude-native research tool, so most contributions fall into a few clear categories.

## What I Welcome

### 🎯 Rubric Refinements
The 8-dimension rubric in [`docs/EVALUATION_RUBRIC.md`](docs/EVALUATION_RUBRIC.md) is anchored to NeurIPS / Nature / JACS practice. If you have:
- A concrete venue rubric I missed (Science, Cell, ICML, etc.)
- A field-specific anchor that should be added (medical, social science, theoretical CS...)
- A red-flag pattern that catches something the current rubric misses

→ Open a PR editing the rubric markdown with the change + a paragraph of justification.

### 📋 Reproducibility Checklist Extensions
The current checklist mostly covers ML/computational papers + chemistry add-ons. I welcome additions for:
- Biology / wet-lab reproducibility (cell lines, antibodies, sequencing pipelines)
- HCI / user studies (sample size, IRB, replication packages)
- Theory papers (proof verification, computer-checked proofs)

→ PR to [`docs/REPRODUCIBILITY_CHECKLIST.md`](docs/REPRODUCIBILITY_CHECKLIST.md) with the new section.

### 🧪 Case Studies
Real papers run through Lunheng with permission to share are extremely valuable. If you used Lunheng on a real paper and can share (anonymized OK):
- The R0/R1/R2 score trajectory
- One or two key fixes the framework caught
- A reflection paragraph: where it helped most, where it missed

→ Add a markdown file under [`examples/`](examples/) following the pattern of `dac_paper_case_study.md`.

### 🔧 Skill Improvements
The skills under [`skills/`](skills/) are markdown-only by design. Improvements welcome:
- Better prompts for the Architect / Writer / Refiner / Evaluator agents
- Better stop-condition logic
- Better state-recovery on context-window compaction

→ PR to the relevant `SKILL.md`. Include before/after composite scores on a test paper if possible.

### 🌍 Translations
Right now we have English (`README.md`) and Chinese (`README_CN.md`). I'd welcome:
- Other major languages (Japanese, Korean, Spanish, French, German)
- Translation of `docs/EVALUATION_RUBRIC.md` so non-English authors can use it directly

## What I'd Rather Not Merge

- **Adding non-Claude backends** as the primary path. The point of Lunheng is to be Claude-native; if you want a multi-backend version, please fork.
- **Generating fake reviews** or **fabricating data** — these violate the framework's stated ethical scope. PRs that enable this will be closed without comment.
- **Unscoped expansions** ("let's also write the paper for the user") — Lunheng is review/improvement, not generation.

## Process

1. Open an issue describing what you want to add or change
2. Once we agree on scope, fork → branch → PR
3. PR description should include: motivation, what changed, how it was tested
4. I aim to respond to issues/PRs within 7 days

## Code of Conduct

Standard: be kind, be specific, prefer concrete examples over abstract criticism.

## Author

Yujie Ding · 中国石油大学（北京）克拉玛依校区

---
---

# 贡献指南（中文版）

感谢你考虑为论衡贡献力量！论衡是一个 Claude 原生的研究工具，多数贡献会落在以下几类。

## 欢迎的贡献

### 🎯 评分标准细化
[`docs/EVALUATION_RUBRIC.md`](docs/EVALUATION_RUBRIC.md) 中的 8 维评分对齐 NeurIPS / Nature / JACS 实践。如果你有：
- 我遗漏的具体期刊评分标准（Science、Cell、ICML 等）
- 某领域特有的锚点（医学、社会科学、理论 CS……）
- 当前规则没能捕获的"红旗模式"

→ 提 PR 修改 rubric 的 markdown，附一段说明。

### 📋 可复现性清单扩展
当前清单主要覆盖 ML/计算论文 + 化学扩展。欢迎新增：
- 生物 / 湿实验可复现性（细胞系、抗体、测序流程）
- HCI / 用户研究（样本量、IRB、复现包）
- 理论论文（证明验证、机器辅助证明）

→ 提 PR 至 [`docs/REPRODUCIBILITY_CHECKLIST.md`](docs/REPRODUCIBILITY_CHECKLIST.md)。

### 🧪 案例研究
真实论文经 Lunheng 评审后获授权分享的轨迹非常宝贵。如果你用过且可分享（匿名也可）：
- R0/R1/R2 评分轨迹
- 框架捕获到的 1-2 个关键修复
- 一段反思：哪里帮助最大、哪里它没看到

→ 在 [`examples/`](examples/) 下按 `dac_paper_case_study.md` 的模式新增一份。

### 🔧 Skill 改进
[`skills/`](skills/) 下的 skill 文件设计为纯 markdown。欢迎改进：
- 更优的 Architect / Writer / Refiner / Evaluator 提示词
- 更好的停止条件逻辑
- 上下文窗口压缩后的状态恢复

→ 提 PR 至相应 `SKILL.md`。如可能附测试论文的前后综合分对照。

### 🌍 翻译
目前有英文（`README.md`）和中文。欢迎其他主要语言：
- 日语、韩语、西班牙语、法语、德语
- `docs/EVALUATION_RUBRIC.md` 的多语翻译

## 不接受的贡献

- **将主路径改为非 Claude 后端**。论衡的核心定位是 Claude 原生；如想做多后端版本，请 fork。
- **生成假评审** 或 **伪造数据** —— 违反框架的伦理边界，PR 将不带评论关闭。
- **超范围扩展**（"顺便帮用户写论文"）—— 论衡只做评审/改进，不做生成。

## 流程

1. 先开 issue 描述你想加什么或改什么
2. 范围达成一致后，fork → 分支 → PR
3. PR 描述应包含：动机、变更内容、如何测试
4. 我争取 7 天内回复 issue/PR

## 行为准则

标准守则：友善、具体，用具体例子代替抽象批评。

## 作者

Yujie Ding · 中国石油大学（北京）克拉玛依校区

