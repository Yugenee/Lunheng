# Lunheng Multi-Format Support

> **TL;DR:** Lunheng supports four input formats — LaTeX (`.tex`), Markdown (`.md`), Word (`.docx`), and PDF (`.pdf`). The full **Architect → Writer → Refiner → Evaluator** pipeline runs only on text-source formats (LaTeX, Markdown). Word and PDF get **review-only** mode (Evaluator bench + Architect blueprint), with revisions delivered as a structured edit list for the author to apply manually.

## Feature Matrix

| Capability | `.tex` | `.md` | `.docx` | `.pdf` |
|------------|--------|-------|---------|--------|
| Auto-detect main file | ✅ | ✅ | ✅ | ✅ |
| 8-dim Evaluator bench | ✅ | ✅ | ✅ | ✅ |
| Architect blueprint | ✅ | ✅ | ✅ | ✅ |
| Visual contract (figures/tables registry) | ✅ full | ✅ full | ⚠ partial (no `\label`) | ⚠ read-only |
| Writer agent (re-drafts sections) | ✅ | ✅ | ❌ | ❌ |
| Refiner agent (global polish) | ✅ | ✅ | ❌ | ❌ |
| In-place revision output | ✅ | ✅ | edit-list only | edit-list only |
| Compile / build verification | ✅ xelatex | ✅ pandoc | n/a | n/a |
| Cross-reference validation | ✅ | ✅ | partial | ❌ |

## Auto-Detection

When invoked as `/lunheng <paper_dir>/`, the skill scans for the main file in this priority order:

1. `*.tex` files → if present, format = `tex`. Disambiguates by largest file or one containing `\documentclass`.
2. `*.md` files → if present (and no `.tex`), format = `md`. Picks the file with the most `# headings`.
3. `*.docx` files → if present (and no `.tex` / `.md`), format = `docx`.
4. `*.pdf` files → if present (and no source file), format = `pdf`.

Override with `/lunheng paper/ --format=docx` if auto-detection picks the wrong file.

## Per-Format Behavior

### `.tex` (full pipeline)

- **Read**: parse LaTeX, extract sections by `\section{}`, figures by `\includegraphics`, tables by `\begin{table}`, refs by `\ref/\cite/\label`.
- **Visual contract**: full schema; `\label` definitions and `\ref` usages are tracked.
- **Writer/Refiner**: produce `<SECTION_OUTPUT>...</SECTION_OUTPUT>` blocks of LaTeX that the orchestrator splices back into the source.
- **Compile**: `xelatex → bibtex → xelatex × 2`; verify `0 undefined refs/citations`.

### `.md` (full pipeline)

- **Read**: parse Markdown, extract sections by `## headings`, figures by `![alt](file)`, tables by `|---|` syntax, refs by `[text](#anchor)` and `[@cite-key]`.
- **Visual contract**: figures registered by their image filename; section obligations checked against headings.
- **Writer/Refiner**: produce Markdown blocks; spliced back into the source by the orchestrator.
- **Compile**: optional `pandoc → pdf` for visual verification.

### `.docx` (review-only + edit list)

- **Read**: extract text via `python-docx`; section structure from heading styles; figures from inline shapes / floats; tables from `doc.tables`.
- **Visual contract**: registers figures/tables by their position and caption text. Cannot validate cross-references because Word fields are opaque.
- **Writer/Refiner**: **not run.** Instead, the orchestrator produces `LUNHENG_EDIT_LIST.md` with structured edit instructions:
  ```markdown
  ## Suggested edits for section "Methods"
  ### Critical
  - **Para 3, line 2**: Replace "我们证明" with "我们的实验结果表明" (softens overclaim)
  - **Table 2 caption**: Add "(error bars = bootstrap 95% CI)"
  ### Major
  - **Insert after Para 5**: Add a sentence stating the iid assumption for the noise floor analysis
  ```
- The author copies these into Word manually.

### `.pdf` (evaluation only)

- **Read**: text extraction via `pdftotext` or Claude's native PDF reading; figures detected as image regions but not editable.
- **Visual contract**: read-only — figures/tables are listed but cannot be cross-validated against source.
- **Writer/Refiner**: **not run.**
- **Output**: `LUNHENG_REVIEW.md` with the 8-dim scores + per-dimension fixes, suitable for sharing with co-authors before the next revision cycle.

## Format Conversion Workarounds

If you have a Word/PDF paper but want the **full pipeline** (Writer + Refiner), convert first:

### Word → LaTeX → Lunheng → Word

```bash
# 1. Convert
pandoc paper.docx -o paper.tex --extract-media=figures/

# 2. Run Lunheng on the LaTeX
/lunheng paper/

# 3. Convert back
pandoc paper.tex -o paper_revised.docx
```

**Caveat**: pandoc's Word ↔ LaTeX round-trip loses some formatting (figure positioning, table styling, custom fonts). Best for content/structural improvements, not for final styling.

### Markdown → LaTeX (best for journal submission)

```bash
pandoc paper.md -o paper.tex --bibliography=refs.bib --citeproc
# then Lunheng pipeline on .tex
```

## Output Files Per Format

| Format | Compiled output | Review log | Edit list |
|--------|------------------|------------|------------|
| `.tex` | `<main>.pdf` | `LUNHENG_LOG.md` | (revisions in-place) |
| `.md` | `<main>.pdf` (optional) | `LUNHENG_LOG.md` | (revisions in-place) |
| `.docx` | (unchanged) | `LUNHENG_LOG.md` | `LUNHENG_EDIT_LIST.md` |
| `.pdf` | (unchanged) | `LUNHENG_REVIEW.md` | `LUNHENG_EDIT_LIST.md` |

## When Each Format Is Right

| Your situation | Recommended path |
|----------------|------------------|
| Writing in LaTeX from the start | `tex` — full pipeline |
| Writing in Word, comfortable with Markdown export | convert to `.md` → `tex` pipeline → convert back |
| Writing in Word, want hands-off review | `docx` — get edit list, apply manually |
| Already submitted, only have PDF | `pdf` — get review for revision planning |
| Markdown source (e.g., Quarto, R Markdown) | `md` — full pipeline |

---
---

# 多格式支持

> **一句话**：论衡支持四种输入格式——LaTeX、Markdown、Word、PDF。**完整流水线**（架构师→撰写者→润色者→评估者团）仅在文本源格式（LaTeX/Markdown）上运行；Word 和 PDF 走**只评不改**模式（评估者团 + 架构师蓝图），改动以"建议清单"形式输出，作者手动应用。

## 能力对照表

| 能力 | `.tex` | `.md` | `.docx` | `.pdf` |
|------|--------|-------|---------|--------|
| 自动检测主文件 | ✅ | ✅ | ✅ | ✅ |
| 8 维评估者团 | ✅ | ✅ | ✅ | ✅ |
| 架构师蓝图 | ✅ | ✅ | ✅ | ✅ |
| 视觉契约 | ✅ 完整 | ✅ 完整 | ⚠ 部分（无 `\label` 概念） | ⚠ 只读 |
| 撰写者改稿 | ✅ | ✅ | ❌ | ❌ |
| 润色者全局抛光 | ✅ | ✅ | ❌ | ❌ |
| 原地输出修改 | ✅ | ✅ | 仅给清单 | 仅给清单 |
| 编译/构建验证 | ✅ xelatex | ✅ pandoc | 无 | 无 |
| 交叉引用校验 | ✅ | ✅ | 部分 | ❌ |

## 自动检测

`/lunheng <paper_dir>/` 调用时按以下优先级扫描主文件：
1. `*.tex` → 选含 `\documentclass` 或最大者
2. `*.md` → 选标题层级最深者
3. `*.docx` → 默认选第一个
4. `*.pdf` → 仅当前三者都无

强制指定用 `/lunheng paper/ --format=docx`。

## 各格式行为要点

| 格式 | 读取方式 | 改稿支持 | 输出 |
|------|---------|---------|------|
| `.tex` | LaTeX 解析 | 撰写者+润色者 in-place | 改稿 + LUNHENG_LOG.md |
| `.md` | Markdown 解析 | 撰写者+润色者 in-place | 改稿 + LUNHENG_LOG.md |
| `.docx` | python-docx 提取文本+表格 | **不改** | LUNHENG_EDIT_LIST.md (结构化建议) |
| `.pdf` | pdftotext / Claude 原生 PDF 阅读 | **不改** | LUNHENG_REVIEW.md (评分+修复建议) |

## 格式转换变通

Word/PDF 想用完整流水线，先转 LaTeX：

```bash
# Word → LaTeX → 论衡 → Word
pandoc paper.docx -o paper.tex --extract-media=figures/
/lunheng paper/
pandoc paper.tex -o paper_revised.docx
```

注意：pandoc 的 Word ↔ LaTeX 往返会丢一些格式（图位置、表样式、自定义字体），适合内容/结构改进，不适合最终美化。

## 选哪种格式

| 你的情况 | 推荐路径 |
|---------|---------|
| LaTeX 写作 | `tex` — 完整流水线 |
| Word 写作但能导出 Markdown | 转 `.md` → `tex` 流程 → 转回 |
| Word 写作，要"少干预" review | `docx` — 拿建议清单手动应用 |
| 已投稿，只有 PDF | `pdf` — 评审报告辅助下一轮 revision |
| Markdown 源（Quarto / R Markdown） | `md` — 完整流水线 |
