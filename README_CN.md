# 论衡 (Lunheng)

> **多智能体学术论文审阅框架，对齐顶刊审稿标准。**
>
> 纯Claude / Claude Code skill — 无需OpenAI密钥。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skill: Claude Code](https://img.shields.io/badge/Skill-Claude%20Code-blueviolet)]()

> *"权衡论证, 校释虚妄"* — 王充《论衡》(~80 CE)

---

## 是什么

论衡是一个**契约约束的多智能体论文评审与改进框架**。它把你的论文视为一个契约系统：四类专业智能体（架构师 / 撰写者 / 润色者 / 评估者团）协同作业，所有agent共享一份**持久化视觉契约**，追踪图表、术语和交叉引用。

它是 [Story2Proposal](https://arxiv.org/abs/2603.27065)（AgentAlpha 2026）框架的Claude原生再实现+扩展。**关键扩展**：

- **8维度 1–10 分锚定评分**，每个分数段都有显式锚点描述，对齐NeurIPS 2025 / Nature / JACS的真实审稿规范
- **NeurIPS式16项可复现性清单**，含化学/材料学科扩展
- **纯Claude子代理**，不依赖OpenAI/Codex MCP
- **公开真实案例**：完整展示 R0→R2 在Q1论文上的轨迹

## 为什么叫"论衡"

王充《论衡》成书约公元80年，是中文世界第一部系统论述"权衡论据、校释虚妄"的著作。本框架的工作本质相同：把论文中的每个claim与其证据进行权衡，识别那些缺乏支撑的部分。

---

## 快速开始

### 安装为Claude Code / OpenClaw skill

```bash
git clone https://github.com/<your-user>/Lunheng.git
cd Lunheng

mkdir -p ~/.claude/skills
cp -r skills/lunheng ~/.claude/skills/
cp -r skills/lunheng-quick ~/.claude/skills/
```

在Claude Code中调用：

```
/lunheng path/to/your/paper/
```

执行流程：
1. **架构师**评审论文（1个子代理）→ 蓝图 + 视觉契约
2. **8维度并行评估**（8个子代理同时启动）→ 综合分 R₀
3. **循环迭代**：若 R < 7.0，调度撰写者+润色者修改后重新评估
4. **停止**于 R ≥ 7.0 或 3 轮迭代后
5. **生成日志** `LUNHENG_LOG.md`，含每轮完整变更记录

### 仅快速润色

如论文结构已经成型，仅需文字打磨：

```
/lunheng-quick path/to/paper/
```

单评审者2轮循环（约4个子代理调用）。

---

## 8 维评分体系

每维度 **1–10 分制**，4个分数段都有锚点描述（1–3 / 4–6 / 7–8 / 9–10），加 Overall verdict (1–6) 与 Confidence (1–5)。

| 维度 | 对齐顶刊标准 |
|------|-------------|
| **D1. 方法严谨性 (Soundness)** | NeurIPS Soundness, Nature Technical Rigor |
| **D2. 重要性与原创性** | NeurIPS Significance + Originality |
| **D3. 清晰度与组织** | NeurIPS Clarity, JACS Clarity |
| **D4. 实验充分性** | NeurIPS Quality |
| **D5. 可复现性** | NeurIPS 16项清单 |
| **D6. 引用质量** | JACS Literature Appropriateness |
| **D7. 图表沟通** | Nature Figure Quality |
| **D8. 伦理/局限/影响** | NeurIPS Limitations + Ethics |

📖 完整规则及锚点 → [docs/EVALUATION_RUBRIC.md](docs/EVALUATION_RUBRIC.md)
📋 可复现性清单 → [docs/REPRODUCIBILITY_CHECKLIST.md](docs/REPRODUCIBILITY_CHECKLIST.md)
🏗 架构与契约 schema → [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

---

## 真实案例

将论衡应用于一篇中文化学-机器学习论文（DAC吸附材料预测，目标Q1期刊）：

| 轮次 | 综合分 | 关键变化 |
|------|--------|---------|
| **R0**（基线） | **6.81** | 原始草稿 |
| **R1** | **8.04** | +1.23 — 修排版+视觉（图位置/引用/术语统一） |
| **R2** | **8.66** | +0.62 — 修内容（统计假设、超参表、消融搬入正文） |

对照[Story2Proposal原文报告](https://arxiv.org/abs/2603.27065)：
- DirectChat单次输出: **3.96**
- Story2Proposal（混合backbone）: **6.15**

📊 完整每维度细分 → [examples/dac_paper_case_study.md](examples/dac_paper_case_study.md)

---

## 架构 60 秒速览

```
                架构师 ──→ 蓝图 + 视觉契约
                              │
                ┌─────────────┼─────────────┐
                ▼             ▼             ▼
        撰写者(per-section) 润色者(global)  评估者团
        草稿（契约约束）     全局精炼+契约更新  (8 并行评估)
                │             │             │
                └─────────────┴─────────────┘
                              ▼
                       聚合 R = Σ Dₖ / 8
                       R ≥ 7.0  →  停止
                       R <  7.0  →  循环
```

**视觉契约（Visual Contract）** 是一份在所有agent调用之间持久化的JSON文件，包含：
- `global_visual_registry` — 每张图/表的语义描述与预期所属章节
- `section_obligations` — 每节必须包含哪些视觉元素
- `terminology_glossary` — 每个关键术语的标准形式
- `validation_rules` — unique-labels / all-visuals-referenced 等

这是防止多步改稿过程中"结构漂移"的核心机制。

---

## 与其他工具对比

| 工具 | 后端 | 输出 | 多智能体 | 视觉契约 | 锚定评分 |
|------|------|------|----------|----------|----------|
| **论衡 (本项目)** | 仅Claude | 改稿+8维分数 | ✅ 4+8 | ✅ | ✅ NeurIPS/Nature/JACS |
| Story2Proposal (论文) | 混合 | LaTeX手稿 | ✅ 4 | ✅ | ❌ 通用8维 |
| auto-paper-improvement-loop | GPT-5.4 | 改稿 | ❌ 单评审 | ❌ | ❌ |
| AI Scientist v2 | OpenAI | 端到端论文 | ✅ 树搜索 | ❌ | ❌ |
| PaperOrchestra (Google) | 混合 | 投稿就绪稿 | ✅ | ✅ | ❌ |

---

## 伦理使用声明

论衡用于**作者自审**——写作者在投稿前自己打磨论文。

**不得用于**：
- 伪造同行评审报告
- 生成虚假实验数据
- 绕过期刊peer-review流程
- 冒充审稿人

框架明确拒绝编造实验数据；仅指出缺失的实验并建议补充方向。

---

## 贡献与引用

引用本项目：

```bibtex
@software{lunheng2026,
  author = {Ding, Yujie},
  title  = {Lunheng (论衡): Multi-agent paper review framework anchored to top-tier journal rubrics},
  year   = {2026},
  url    = {https://github.com/<your-user>/Lunheng}
}
```

也请引用本工作所基于的Story2Proposal原文：

```bibtex
@article{story2proposal2026,
  title  = {Story2Proposal: A Scaffold for Structured Scientific Paper Writing},
  author = {AgentAlpha Team},
  year   = {2026},
  eprint = {2603.27065},
  archivePrefix = {arXiv}
}
```

## 协议

[MIT](LICENSE)
