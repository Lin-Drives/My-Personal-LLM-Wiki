# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个 Claude Code 技能集合仓库。技能遵循 [Agent Skills](https://agentskills.io) 开放标准，存放在 `.claude/skills/` 下。

每个技能由以下部分组成：
- `SKILL.md` — 技能规范，包含 frontmatter（name、description）和工作流规则
- `references/` — 模板和辅助文件，供技能在运行时读取
- `examples/` — 真实使用示例

## 当前技能：karpathy-llm-wiki

实现 [Karpathy 的 LLM Wiki 理念](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)：由 LLM 维护个人知识库。

### 核心架构

三层设计，均位于用户项目根目录（而非此仓库）：

- **`raw/`** — 不可变的源材料，按主题子目录组织
- **`wiki/`** — 编译后的知识文章，含 `wiki/index.md`（全局索引）和 `wiki/log.md`（追加式操作日志）
- **`SKILL.md`**（本文件）— 模式层，定义结构和规则

### 三大操作

| 操作 | 功能 |
|------|------|
| **Ingest** | 将源内容抓取到 `raw/` 中，然后编译到 `wiki/` 中。始终执行两步。新源可能会级联更新文章并会添加到索引和日志中。 |
| **Query** | 搜索 wiki 并给出带引用的答案。引用 wiki 页面；优先使用 wiki 内容而非训练知识。可以选择将答案归档为新的 wiki 页面。 |
| **Lint** | 质量检查：索引一致性、断开的内部链接、原始引用的有效性、参见交叉引用（自动修复）。启发式检查（仅报告）：事实矛盾、过时声明、孤立页面。 |

### 关键约定

- `wiki/` 仅支持一层主题子目录，不支持更深嵌套
- wiki 文件内的所有 markdown 链接使用相对于当前文件的路径；对话输出中使用相对于项目根目录的路径
- Ingest 更新 `wiki/index.md` 和 `wiki/log.md`；Archive（来自 Query）同时更新两者；Lint 更新 `wiki/log.md`（仅在自动修复索引条目时更新 `wiki/index.md`）
- 原始文件命名：`YYYY-MM-DD-descriptive-slug.md`（无发布日期时省略日期前缀）

### 模板

`references/` 中的模板定义了写入新文件时的确切格式：
- `article-template.md` — wiki 文章（来源、原始内容、概述、正文、可选参见）
- `raw-template.md` — 原始文件元数据头部
- `archive-template.md` — 来自查询的已归档答案
- `index-template.md` — 全局索引表结构
