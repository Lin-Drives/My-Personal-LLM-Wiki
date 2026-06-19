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
│   ├── index.md            # 全局索引（本页）
│   ├── log.md              # 操作日志（追加式）
│   ├── knowledge-graph.md  # 交互式知识图谱
│   ├── overview.md         # 本页：项目概览与使用指南
│   ├── AI-Infra/
│   ├── Chip-Architecture/
│   ├── Deep-Learning/
│   ├── Reinforcement-Learning/
│   ├── World-Models/
│   └── Companies/
├── scripts/                # 构建与维护脚本
│   ├── generate_graph_data.py   # 扫描 wiki 生成知识图谱数据
│   └── mkdocs_hooks.py          # MkDocs 构建钩子
├── mkdocs.yml              # MkDocs 站点配置
├── purpose.md              # 项目宗旨与范围
└── README.md               # 项目入口说明
```

## 如何阅读

### 按主题导航

左侧导航栏按主题组织：

| 主题 | 内容 | 代表文章 |
|------|------|----------|
| **AI-Infra** | LLM 推理调度、分布式训练、KV Cache | SLAI 调度器、五种并行策略全景 |
| **Chip-Architecture** | AI 芯片、数据流架构 | M100 车端推理芯片 |
| **Deep-Learning** | 架构、理论、物理信息 AI | Transformer、Mamba-3、PINN/KAN 生态 |
| **Reinforcement-Learning** | 决策智能、游戏 AI | AlphaGo |
| **World-Models** | 世界模型、JEPA、机器人 | V-JEPA 2、Causal-JEPA、World Action Models |
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
