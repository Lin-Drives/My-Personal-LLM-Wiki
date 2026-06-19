# Wiki Log

## [2026-06-19] Ingest | 批量补全 51 篇 arXiv PDF 原文
- 扫描全库：56 个独立 arXiv ID，原有 5 个有效 PDF，缺失 51 个
- 成功下载 46 篇（urllib/curl 双策略，含断点续传 + 限速）
- 重新下载修复：MAE (7.4MB → 有效), HumanEgo (9.4MB → 16MB 有效)
- 无效 ID 标记：2503.29237 (DeepOmamba) — arXiv 404，可能预印本已删除
- 当前状态：57 个 PDF 全部有效，覆盖 55 个独立 arXiv ID
- 按 topic 分布：
  - AI-Infra: 3 篇 | Chip-Architecture: 1 篇 | Deep-Learning: 12 篇
  - World-Models: 26 篇 | Reinforcement-Learning: 1 篇 (Nature) + 旧 PDF 2 篇
  - Embodied-Intelligence: 5 篇 (EgoScale/HumanEgo/VideoManip/EgoVerse + 相关)

## [2026-06-19] Polish | 标题与导航统一中文为主
- 8 篇文章标题改为中文（保留英文缩写作为专有名词）：
  - EgoScale → EgoScale：大规模人类 egocentric 视频预训练与灵巧操作
  - HumanEgo → HumanEgo：零样本机器人学习的极致数据效率
  - VideoManip → VideoManip：从 RGB 视频重建 3D 轨迹的 device-free 灵巧操作
  - EgoVerse → EgoVerse：全球 egocentric 机器人学习数据集
  - Transformer Architecture → Transformer 架构
  - World Action Models → World Action Models：从世界预测到可执行动作
  - 视觉 Transformer → 视觉 Transformer：一幅图像相当于 16×16 个词
  - 掩码自编码器（MAE） → 掩码自编码器（MAE）：可扩展的视觉自监督学习者
- 7 个 topic 落地页标题改为中文：AI 基础设施、AI 芯片架构、深度学习、具身智能、强化学习、世界模型、科技公司
- 全局索引 (wiki/index.md) + 各 topic 子索引 + See Also 跨引用，全部同步更新
- mkdocs.yml nav 修复：YAML 引号包裹含冒号标题，补全 Companies 和 ViT/MAE nav 缺失
- 知识图谱：重新生成 graph-data.json（25 节点, 52 边）

## [2026-06-19] Compile | 视觉 Transformer (Deep-Learning)
- Source: raw/Deep-Learning/2020-10-22-vit-arxiv-2010.11929.md (arXiv:2010.11929, Google Research, ICLR 2021)
- Compiled: wiki/Deep-Learning/vision-transformer.md
- Summary: 图像块化为 16×16 词元，纯 Transformer 取代 CNN，大规模预训练是关键

## [2026-06-19] Compile | 掩码自编码器 (Deep-Learning)
- Source: raw/Deep-Learning/2021-11-11-mae-arxiv-2111.06377.md (arXiv:2111.06377, Meta AI, CVPR 2022)
- Compiled: wiki/Deep-Learning/mae.md
- Summary: 75% 高比例遮挡像素重建，自监督预训练超越监督预训练，ViT 标准范式

## [2026-06-19] Ingest | 视觉 Transformer + 掩码自编码器（arXiv 下载）
- ViT (arXiv:2010.11929): Google Research, 2020-10, ICLR 2021 — 纯 Transformer 图像分类
- MAE (arXiv:2111.06377): Kaiming He / Meta AI, 2021-11, CVPR 2022 — 掩码自编码器自监督预训练
- PDFs: raw/Deep-Learning/2020-10-22-vit-arxiv-2010.11929.pdf, 2021-11-11-mae-arxiv-2111.06377.pdf
- Raw notes: raw/Deep-Learning/2020-10-22-vit-arxiv-2010.11929.md, 2021-11-11-mae-arxiv-2111.06377.md
- Status: 本地导入完成，已编译至 wiki/Deep-Learning/

## [2026-06-19] lint | 0 issues found, 0 auto-fixed
- Index consistency: 18 indexed files match 18 actual files (0 missing, 0 orphaned)
- Internal links: all valid (0 broken)
- Raw references: all valid (59 references checked)
- Meta files (overview.md, knowledge-graph.md): all links valid
- Directory structure: 6 topic sections match 6 directories (0 mismatch)
- No fixes required; wiki is fully consistent

## [2026-06-03] lint | 3 issues found, 3 auto-fixed
- Removed broken See Also: m100-npu-details, mcts-fundamentals, transformer-positional-encoding

## [2026-06-03] ingest | X Corp. 公司概况
- Source: https://about.x.com/en (security-and-privacy, lobbying-disclosures, brand-toolkit, legal imprint, es/twitter-for-good)
- Created: Companies/x-corp-company-profile.md

## [2026-05-31] Compile | AI-Infra (new topic)
- Source: raw/AI-Infra/2026-W18-ai-infra.md (论文雷达周报 W18)
- Created: llm-inference-scheduling.md, distributed-training-parallelism.md, kv-cache-management.md

## [2026-05-31] Compile | Chip-Architecture (new topic)
- Source: raw/Chip-Architecture/m100-li-auto-dataflow-architecture.md (M100 ISCA 2026 论文笔记)
- Created: m100-orchestrated-dataflow-architecture.md

## [2026-05-31] Compile | Deep-Learning (new articles)
- Sources: raw/Deep-Learning/2026-W19-deep-learning.md, raw/Deep-Learning/2026-W20-physics-informed-ai.md
- Created: mamba-3-state-space-models.md, looped-transformers-stability.md, noise-stability-regularization.md, k-pinn-lattice-boltzmann.md, solver-in-the-loop-deeponet.md, pinn-ecosystem-2026.md

## [2026-05-31] Compile | World-Models (new topic)
- Sources: raw/World-Models/2025-ding-world-models-survey.md, 2025-vjepa2-lecun.md, 2026-ad-list-jepa-lidar.md, 2026-c-jepa-causal.md, 2026-W21-world-models.md
- Created: world-models-survey.md, v-jepa-2.md, causal-jepa.md, jepa-ecosystem-2026.md, world-action-models.md

## [2026-06-19] Redesign | 参考 GAC-BMS-wiki 优化 MkDocs 导航与主题
- 新增: navigation.indexes (topic 落地页可点击), toc.follow, content.code.copy
- 新增: 中文本地化 language: zh, search: lang: zh
- 新增: theme primary/accent: indigo, 配色统一
- 新增: 7 个 topic index.md 落地页 (AI-Infra, Chip-Architecture, Deep-Learning, Embodied-Intelligence, Reinforcement-Learning, World-Models, Companies)
- 新增: 丰富 markdown 扩展 (admonition, details, tabbed, inlinehilite, caret, mark, tilde, attr_list, md_in_html, tables, footnotes)
- 更新: 全局 index.md 添加 hide: toc + overview.md 快捷链接
- 更新: nav 结构为 topic/index.md 首位模式
- 参考: D:\01_Programming\Git Repository\GAC-BMS-wiki\projectdoc\mkdocs.yml

## [2026-06-19] Restructure | 新增 Embodied-Intelligence 分类
- 创建 wiki/Embodied-Intelligence/ 目录
- 从 World-Models 移入: egoscale.md, humanego.md
- 从 Deep-Learning 移入: videomanip.md
- 新建: egoverse.md (EgoVerse 数据集编译)
- 更新: wiki/index.md, mkdocs.yml nav
- 修复: 4 篇文章内部 See Also 链接

## [2026-06-19] Ingest | 批量抓取 3 篇机器人学习论文（WebBridge）
- EgoScale (NVIDIA, arXiv:2602.16710): 20,854h egocentric 预训练, log-linear scaling law, 22-DoF 灵巧手
- HumanEgo (UMD, arXiv:2605.24934): 零样本迁移, 30 分钟视频/任务→92.5% 成功率, 无需机器人数据
- VideoManip (CMU/UCB, arXiv:2602.09013): 从 RGB 视频重建 3D 手-物体轨迹, device-free 灵巧操作
- PDFs: raw/World-Models/ + raw/Deep-Learning/
- Wiki articles: wiki/World-Models/egoscale.md, humanego.md; wiki/Deep-Learning/videomanip.md
- Updated: wiki/index.md, mkdocs.yml nav

## [2026-06-19] Compile | EgoScale (Embodied-Intelligence)
- Source: raw/World-Models/2026-02-20-egoscale-arxiv-2602.16710.md (NVIDIA arXiv)
- Compiled: wiki/Embodied-Intelligence/egoscale.md
- Summary: 20,854h 人类 egocentric 预训练，log-linear scaling law，22-DoF 灵巧手策略

## [2026-06-19] Compile | HumanEgo (Embodied-Intelligence)
- Source: raw/World-Models/2026-05-28-humanego-arxiv-2605.24934.md (UMD arXiv)
- Compiled: wiki/Embodied-Intelligence/humanego.md
- Summary: 零样本迁移，30 分钟视频/任务→92.5% 成功率，无需机器人数据

## [2026-06-19] Compile | VideoManip (Embodied-Intelligence)
- Source: raw/Deep-Learning/2026-02-09-videomanip-arxiv-2602.09013.md (CMU/UCB arXiv)
- Compiled: wiki/Embodied-Intelligence/videomanip.md
- Summary: 从 RGB 人类视频直接重建 3D 手-物体轨迹，device-free 灵巧操作学习

## [2026-06-19] Compile | EgoVerse (Embodied-Intelligence)
- Source: raw/World-Models/2026-04-08-egoverse-egocentric-human-dataset.md
- Compiled: wiki/Embodied-Intelligence/egoverse.md
- Status: ✅ completed (was pending wiki compilation)

## [2026-06-19] Ingest | EgoVerse (World-Models)
- Source: arXiv:2604.07607, Georgia Tech/Stanford/MIT/Meta/ETH Zürich/Scale AI
- Captured via Kimi WebBridge (browser automation)
- PDF: raw/World-Models/2026-04-08-egoverse-egocentric-human-dataset.pdf (22.54 MB)
- Raw notes: raw/World-Models/2026-04-08-egoverse-egocentric-human-dataset.md
- Status: WebBridge ✅ working, raw stored, pending wiki compilation

## [2026-05-31] Ingest | 补充 20 篇原始论文摘要到 raw/
- AI-Infra: dai-llm-inference-scheduling (arXiv:2504.07347), amer-distributed-hybrid-parallelism (arXiv:2602.09109), liu-cachegen-kv-cache-compression (arXiv:2310.07240)
- Chip-Architecture: xie-m100-orchestrated-dataflow (arXiv:2604.17862, ISCA 2026)
- Deep-Learning: lahoti-mamba-3 (arXiv:2603.15569, ICLR 2026), labovich-looped-transformers (arXiv:2604.15259), haris-noise-stability (arXiv:2602.08287, ICLR 2026), santoni-compiler-first-ssd (arXiv:2603.09555), xu-geometry-multitask-grokking (arXiv:2602.18523), meshram-k-pinn (arXiv:2604.03481), dehaghani-qpinn (arXiv:2605.13892)
- World-Models: ding-world-models-survey (arXiv:2411.14499), assran-v-jepa-2 (arXiv:2506.09985), nam-causal-jepa (arXiv:2602.11389, ICML 2026), zhu-ad-list-jepa (arXiv:2602.12540), he-demo-jepa (arXiv:2605.20811), hou-world-model-robot-learning (arXiv:2605.00080), li-mola (arXiv:2605.12167, ICML 2026), terver-jepa-wm-planning (arXiv:2512.24497, TMLR), lin-world-ego-modeling (arXiv:2605.19957)
- Updated: 所有关联 wiki 文章的 Raw 字段添加了原始论文引用

## [2026-05-30] Compile | Transformer Architecture (new topic: Deep-Learning)
- Source: raw/Deep-Learning/2017-06-12-attention-is-all-you-need.md (arXiv:1706.03762, NIPS 2017)
- Created: wiki/Deep-Learning/transformer-architecture.md

## [2026-05-30] Compile | AlphaGo (new topic: Reinforcement-Learning)
- Source: raw/Reinforcement-Learning/2016-01-28-mastering-the-game-of-go-with-deep-neural-networks-and-tree-search.md (Nature 2016)
- Created: wiki/Reinforcement-Learning/alphago.md
