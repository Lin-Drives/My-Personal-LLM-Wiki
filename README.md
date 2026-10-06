# My-Personal-LLM-Wiki

Personal AI/LLM Knowledge Wiki, covering deep learning, reinforcement learning, world models, AI Infra, chip architecture, and tech companies. Inspired by Andrej Karpathy's LLM-Wiki proposal.

- **Purpose**: [purpose.md](purpose.md) — 项目宗旨、关键问题、范围与方法论
- **更新方案**: [knowledge-plan.md](knowledge-plan.md) — 三个长期跟踪问题、来源规则与 OKF v0.2 头部约定
- **维护工作流**: [docs/workflow.md](docs/workflow.md) — Kimi 扫描接口、任务续跑、自动动态与独立核查
- **Kimi Claw 扫描模板**: [templates/kimi-claw-scan.md](templates/kimi-claw-scan.md) — 可复制的扫描提示词、JSON 格式与交付规则
- **原论文 PDF 下载**: [docs/pdf-download.md](docs/pdf-download.md) — 按 ID 或历史清单批量下载、去重与失败续跑
- **历史雷达收录核对**: [radar/archive-coverage.md](radar/archive-coverage.md) — 已有文章、原始材料候选与尚待整理的历史论文
- **Overview**: [wiki/overview.md](wiki/overview.md) — 仓库结构、阅读指南、核心工作流
- **Knowledge Index**: [wiki/index.md](wiki/index.md) — 按主题分组的全局文章索引
- **Knowledge Graph**: [wiki/knowledge-graph.md](wiki/knowledge-graph.md) — 交互式文章引用关系图谱

## Quick Start

```bash
# 推荐：uv 全局工具（一次安装，多项目共用）
uv tool install mkdocs
uv tool install mkdocs-material
mkdocs serve

# 或：项目内 venv（已配置）
source .venv/Scripts/activate   # Windows
mkdocs serve
```

访问 http://127.0.0.1:8000/
