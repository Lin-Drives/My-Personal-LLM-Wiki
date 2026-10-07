---
type: Project Guide
title: Overview — 项目概览与使用指南
description: 说明知识库结构与使用方式。
tags:
- 知识库
status: draft
---

# Overview — 项目概览与使用指南

## 仓库结构

```
My-Personal-LLM-Wiki/
├── raw/                    # 原始材料（不可变）
│   ├── AI-Infra/
│   ├── Chip-Architecture/
│   ├── Deep-Learning/
│   ├── Reinforcement-Learning/
│   ├── World-Models/
│   └── Companies/
├── wiki/                   # 编译后的知识文章
│   ├── index.md            # 全局主题索引
│   ├── updates.md          # 最新论文动态（自动整理）
│   ├── radar-archive.md    # 历史雷达及原文阅读入口
│   ├── log.md              # 中文操作日志（最新在前）
│   ├── knowledge-graph.md  # 交互式知识图谱
│   ├── overview.md         # 本页：项目概览与使用指南
│   ├── AI-Infra/
│   ├── Chip-Architecture/
│   ├── Deep-Learning/
│   ├── Embodied-Intelligence/  # 人类视频迁移、机器人操作与数据集
│   ├── Reinforcement-Learning/
│   ├── World-Models/
│   └── Companies/
├── radar/                  # 论文目录；扫描与研究任务在接入后生成
│   ├── reports/weekly/     # 历史周报与配套 JSON（二手整理）
│   ├── exports/            # 历史导出索引与清单
│   └── catalog.json        # 已接收的论文版本目录
├── templates/              # OKF 文章、扫描输入与核查报告模板
├── docs/
│   └── workflow.md         # 论文雷达与知识维护协议
├── scripts/                # 接入、任务状态、校验与构建脚本
│   ├── radar_pipeline.py   # 接收扫描结果、保存来源、生成动态
│   ├── research_task.py    # 研究任务交接与状态迁移
│   ├── validate_okf.py     # OKF 元数据校验
│   ├── generate_graph_data.py  # 扫描 wiki 生成知识图谱数据
│   └── mkdocs_hooks.py     # MkDocs 构建钩子
├── tests/                  # 接入、任务交接与元数据测试
├── .github/workflows/      # CI 检查与 GitHub Pages 部署
├── AGENTS.md               # 跨工具维护约定与测试、提交规则
├── knowledge-plan.md       # 跟踪问题、读者与来源规范
├── mkdocs.yml              # MkDocs 站点配置
├── purpose.md              # 项目宗旨与范围
└── README.md               # 项目入口说明
```

具身智能的知识文章已独立归入 `wiki/Embodied-Intelligence/`，包括 EgoScale、HumanEgo、VideoManip 和 EgoVerse。原始材料沿用历史存放位置：EgoScale、HumanEgo 及 EgoVerse 位于 `raw/World-Models/`，VideoManip 位于 `raw/Deep-Learning/`。原始材料目录不等同于知识文章的主题分类；文章的 OKF `sources` 指向实际来源文件。

接入新的论文扫描后，会生成 `raw/arxiv/`、`radar/scans/` 和 `radar/tasks/`；研究时按需创建 `drafts/` 与 `radar/reviews/`。接口与交接方式见仓库中的 `docs/workflow.md`。

## 如何阅读

### 按主题导航

左侧导航栏按主题组织：

| 主题 | 内容 | 代表文章 |
|------|------|----------|
| **AI-Infra** | LLM 推理调度、分布式训练、KV Cache | SLAI 调度器、五种并行策略全景 |
| **Chip-Architecture** | AI 芯片、数据流架构 | M100 车端推理芯片 |
| **Deep-Learning** | 架构、理论、物理信息 AI | Transformer、Mamba-3、PINN/KAN 生态 |
| **[Embodied-Intelligence](Embodied-Intelligence/index.md)** | 人类视频到机器人迁移、灵巧操作、具身数据集与 scaling | EgoScale、HumanEgo、VideoManip、EgoVerse |
| **Reinforcement-Learning** | 决策智能、游戏 AI | AlphaGo |
| **World-Models** | 环境表征、动态预测与基于模型的规划 | V-JEPA 2、Causal-JEPA、World Action Models |
| **Companies** | 科技公司资料 | X Corp. |

### 全局索引

[`wiki/index.md`](index.md) 提供按主题分组的文章表格，含摘要与最后更新日期，是快速定位文章的最佳入口。

### 知识图谱

[`wiki/knowledge-graph.md`](knowledge-graph.md) 以交互式网络图展示文章之间的引用关系：

- **节点颜色**对应主题领域（见图例）
- **双击节点**跳转对应文章
- **拖拽/缩放**自由浏览

> 提示：图谱在页面加载后自动稳定，稳定后物理模拟关闭，节点不再抖动。

## 核心工作流

### 1. Ingest — 录入新材料

```
获取论文/报告 → 存入 raw/YYYY-MM-DD-slug.md → 编译为 wiki/主题/文章.md → 更新 index.md / log.md
```

- `raw/` 文件按 `YYYY-MM-DD-descriptive-slug.md` 命名，无发布日期则省略日期前缀
- `wiki/` 仅支持一层主题子目录，不嵌套更深
- 所有 wiki 文章使用相对于当前文件的路径做内部链接
- Ingest（原文/元数据接入）与 Compile（知识文章编写）分别记动作；每次在同一提交中同步相关索引并在 `log.md` 顶部新增中文记录（最新在前）。
- 单篇日志列出 来源（原文与论文版本）、文章（文章路径）、更新（影响范围）、状态（真实完成与核验状态）；批次可统一记录范围、数量、失败与重试，并指向逐项清单。
- 任务 JSON、研究运行记录和提交说明不能替代日志。历史补录须明确标注补录，不改写旧日志或虚构执行日期。

### 2. Query — 查询与问答

在已有 wiki 中搜索关键词，优先使用 wiki 内容而非训练知识，回答需带引用标注来源。

### 3. Lint — 维护与自检

定期运行质量检查：

- 索引一致性（index.md 与目录文件对齐）
- 内部链接有效性（断链检测）
- Raw 引用有效性（确保来源文件存在）
- 事实时效性审查（标注可能过时的声明）

## 本地启动

```bash
# 方式一：uv 全局工具（推荐，无需重复安装）
uv tool install mkdocs
uv tool install mkdocs-material
mkdocs serve

# 方式二：项目内 venv（本仓库已配置）
cd My-Personal-LLM-Wiki
source .venv/Scripts/activate  # Windows
mkdocs serve
```

服务启动后访问：http://127.0.0.1:8000/

## 更新记录

操作日志见 [`wiki/log.md`](log.md)，记录每次 Ingest、Query、Lint 的时间、动作与影响范围。
