# 知识库操作日志

> 最新记录在前；日志使用中文。各条状态反映当时的操作结果。

## [2026-10-07] 文章结构 | 按类型统一论文笔记与研究综合

- 论文笔记统一来源、概述、正文、局限性、关键要点、延伸阅读；研究综合统一来源、概述、比较与证据、局限性、综合判断、延伸阅读。保留已有内容、证据和脚注，各篇专属章节下移为子章节。
- 历史材料摘要注明非逐字原文，缺项明确待整理；新增各类型模板，后续同类型沿用固定结构。

## [2026-10-07] 导航显示 | 隐藏草稿状态图标

- 隐藏导航标题旁的草稿信息图标，保留文章头部的 draft 状态及正文核验说明。

## [2026-10-07] 论文笔记 | RoboTwin-Phys 与雷达局限性同步

- 新增 [RoboTwin-Phys 独立论文笔记](World-Models/robotwin-phys.md)，整理方法、结果及简短局限性；来源为本地 PDF 提取 pp.1–9 及表 4 说明，模型解读，未独立核验。
- 历史雷达条目读取笔记中的局限性替换占位描述；保留历史周报原文及历史阅读范围，同步笔记入口、研究主线、首页、主题索引和任务产物。

## [2026-10-07] 阅读维护 | 局限性改为简短概述

- 将 RoboTwin-Phys 独立分析合并为[世界模型可靠规划](Research/world-model-reliability.md#局限性概述)中的一段概述，保留原文页码、模型解读标记和待确认条件。
- 移除本轮新增的独立分析页与入口，后续局限性随对应笔记维护；其他论文的引用性评价注明来源，避免将其当作目标论文自述。


## [2026-10-07] 重点论文分析 | RoboTwin-Phys 局限性

- 新增 RoboTwin-Phys 的局限性与证据边界（后续已合并至研究主线），对照本地原文 pp.1–9 及表 4 说明，列出六项边界与所需补充实验。
- 同步首页、世界模型可靠规划研究主线及导航入口；模型解读草稿，未独立核验或复现实验。

## [2026-10-07] 历史雷达 | 解读字段分段显示

- 历史扫描解读中的“问题/方法/证据”“为什么重要”“局限”“实际阅读范围”另起一段，字段名加粗；已有“问题/方法/证据/局限”合并字段保持原意。
- 仅调整原文库页面的展示，保留历史摘要措辞与来源，不改写扫描记录或补充缺失字段。

## [2026-10-07] 阅读布局 | 放大正文并合并目录

- 保留现有主题配色、论文卡片及折叠交互；桌面正文增大到约 18–20px，行距调整为 1.8，展开卡片内文字使用相同字号。
- 页面目录并入左侧导航，释放右侧栏空间；放宽页面与正文宽度，同时限制超宽屏上的阅读行长。
- 窄屏保留自适应导航与正文边距，长标题和来源链接允许换行；原文链接仍在 GitHub 打开。

## [2026-10-07] 日志维护 | 统一中文与最新在前的顺序

- 全部记录按日期从新到旧排列；近期同日追加记录按写入顺序倒排，较早同日记录保留原有相对顺序，不补造具体执行时间。
- 操作类别、字段名称与说明统一使用中文；论文名称、文件路径、工具参数和提交编号保留原样。
- 更新维护约定：今后新记录写在本页顶部；历史补录明确标注补录，不把补录日期当作原始操作日期。

## [2026-10-07] 维护约定 | 明确日志为 材料接入 / 文章编写的完成条件

- `AGENTS.md` 与 `wiki/overview.md` 统一要求：来源、文章、索引和操作日志一起维护；任务 JSON、研究运行记录或提交说明不能代替操作日志。
- 单篇记 来源 / 文章 / 更新 / 状态；批次记范围、数量、失败与重试、逐项清单位置；历史补录标明补录身份，不编造执行日期。

## [2026-10-07] 文章编写 | JEPA 规划设计研究（第二轮补录）

- 来源： `raw/World-Models/2512.24497.fulltext.md`，全文首页 arXiv:2512.24497v4；官方版本响应为 `raw/arxiv/2512.24497v4.xml`。
- 文章： [wiki/World-Models/jepa-planning-design.md](World-Models/jepa-planning-design.md)；草稿副本 `drafts/World-Models/jepa-planning-design.md`。
- 摘要： 区分预测误差、规划优化和执行成功；DROID 的离线 Action Score 不能当作真机闭环成功率。
- 更新： `wiki/index.md`、`wiki/World-Models/index.md`、`mkdocs.yml`、知识图谱与历史收录清单。
- 状态： 草稿，未独立核验；编写对应 `584bcfe`。官方 v4 元数据请求首次超时，后续在 `9217805` 成功接入，v4 任务完成、v3 停放。

## [2026-10-07] 文章编写 | Demo-JEPA（第二轮补录）

- 来源： `raw/World-Models/2605.20811.fulltext.md`，arXiv:2605.20811v1。
- 文章： [wiki/World-Models/demo-jepa.md](World-Models/demo-jepa.md)；草稿副本 `drafts/World-Models/demo-jepa.md`。
- 摘要： 源视频推断目标机器人的潜空间目标，再由动作条件世界模型规划；明确配对轨迹、目标机器人动作数据与机器人间迁移的实验边界。
- 更新： `wiki/index.md`、`wiki/World-Models/index.md`、`mkdocs.yml`、知识图谱与历史收录清单。
- 状态： 草稿，未独立核验；任务 `radar/tasks/2605.20811v1.json` “已完成”仅表示本轮产物完成；对应提交 `584bcfe`。

## [2026-10-07] 文章编写 | 机器人部署约束（首轮补录）

- 来源： `raw/Embodied-Intelligence/2609.33007.fulltext.md`、`raw/Embodied-Intelligence/2609.39403.fulltext.md`。
- 文章： [wiki/Research/robot-deployment-cost-boundaries.md](Research/robot-deployment-cost-boundaries.md)；草稿副本 `drafts/Research/robot-deployment-cost-boundaries.md`。
- 状态： 草稿，模型整理，未独立核验；对应首轮提交 `9ed8d60`。数据采集成本、模型调用频率与底层控制频率分别记录。

## [2026-10-07] 文章编写 | 人类视频与机器人数据需求（首轮补录）

- 来源： `raw/Embodied-Intelligence/2607.08436.fulltext.md`、`raw/Embodied-Intelligence/2609.39403.fulltext.md`。
- 文章： [wiki/Research/human-video-data-boundaries.md](Research/human-video-data-boundaries.md)；草稿副本 `drafts/Research/human-video-data-boundaries.md`。
- 状态： 草稿，模型整理，未独立核验；对应首轮提交 `9ed8d60`。保留混合人类/机器人数据与迁移边界，未记为无需机器人数据。

## [2026-10-07] 文章编写 | 世界模型可靠规划（首轮补录）

- 来源： `raw/World-Models/2609.26292.fulltext.md`、`raw/Embodied-Intelligence/2607.08436.fulltext.md`。
- 文章： [wiki/Research/world-model-reliability.md](Research/world-model-reliability.md)；草稿副本 `drafts/Research/world-model-reliability.md`。
- 状态： 草稿，模型整理，未独立核验；对应首轮提交 `9ed8d60`。首轮任务关系与后续缺口见 `radar/research-runs/first-pass.json`。

## [2026-10-07] 追溯核对 | 补录近期 材料接入 / 文章编写 追溯信息

- 本次补录依据已有 Git 提交、来源头部和产物清单；补录时间为 2026-10-07，不表示重新下载或重新研究。
- 核对 `9ed8d60..9217805`：新增 2 篇世界模型单篇笔记，具身智能未新增文章；此前的 4 篇具身智能文章已见 2026-06-19 文章编写日志，5 篇既有世界模型文章已见 2026-05-31 文章编写日志。当前普通文章数为具身智能 4 篇、世界模型 7 篇，不含 index.md。
- 遗漏：批量原文与历史目录接入未在此记录完整的材料接入记录；研究文章仅有汇总，缺少逐篇 来源 / 文章 / 状态。已补齐相关记录，保留历史状态。

## [2026-10-07] JEPA v4 元数据重试与版本对账

- 重试 arXiv API 与官方摘要页均 HTTP 200，约 2 秒响应，确认 2512.24497v4 的更新时间为 2026-09-02，与本地全文首页一致。
- 新批次 20261007-jepa-v4-source-retry-01 接入官方 Atom、目录与版本任务；原超时批次保持不变。
- v4 单篇笔记任务完成，v3 保留停放以避免重复研究；第二轮研究记录与文章来源同步更新。
- 这是版本元数据身份核对，不代表文章结论经过独立核查或人工审核。

## [2026-10-07] 历史浏览改进与第二轮文章编写

- 历史雷达页改为主题分组、官方标题、折叠详情和周报索引，保留原文、知识笔记与来源异常入口。
- 新增 JEPA 规划设计研究（2512.24497v4）与 Demo-JEPA（2605.20811v1），依据原文方法、实验和失败条件整理，未进行独立核查。
- Demo-JEPA v1 任务完成本轮产物；2512.24497 目录 v3 与本地 PDF 首页 v4 不符，将 v3 任务停放，笔记明确使用 v4，不冒记版本任务完成。
- 研究主线综合文章保持现状；下一步接入 v4 官方元数据、核查部署指标及目标机器人训练成本。
- v4官方元数据请求读取超时；失败批次保存在 radar/scans/20261007-jepa-v4-source-check.json，本轮不新建未经核实的v4目录记录。

## [2026-10-07] 自动研究首轮

- 按三个长期问题联读四篇原文，产出三篇研究综合草稿并在首页提供入口。
- 四项论文任务记录首轮完成，未标记为已核验；其他任务保持原状态。
- 研究边界、原文页码与下一轮缺口保存在草稿和 radar/research-runs/first-pass.json。

## [2026-10-07] 论文雷达来源分离与原文补齐

- 四份旧 raw 周报与雷达归档逐字相同，统一迁入 radar/reports/weekly/；旧日志保留原始路径作为历史记录。
- 同步更新文章的来源链接与 OKF sources，保留二手报告来源性质。
- 补回 2507.08338 并取得原文，原 PDF 仅本地保存，Markdown 同主题归档。
- 历史雷达与原文入口见 [radar-archive.md](radar-archive.md)。

## [2026-06-19] 材料接入 | 批量补全 51 篇 arXiv PDF 原文

- 扫描全库：56 个独立 arXiv ID，原有 5 个有效 PDF，缺失 51 个
- 成功下载 46 篇（urllib/curl 双策略，含断点续传 + 限速）
- 重新下载修复：MAE (7.4MB → 有效), HumanEgo (9.4MB → 16MB 有效)
- 无效 ID 标记：2503.29237 (DeepOmamba) — arXiv 404，可能预印本已删除
- 当前状态：57 个 PDF 全部有效，覆盖 55 个独立 arXiv ID
- 按主题分布：
  - AI-Infra: 3 篇 | Chip-Architecture: 1 篇 | Deep-Learning: 12 篇
  - World-Models: 26 篇 | Reinforcement-Learning: 1 篇 (Nature) + 旧 PDF 2 篇
  - Embodied-Intelligence: 5 篇 (EgoScale/HumanEgo/VideoManip/EgoVerse + 相关)

## [2026-06-19] 内容润色 | 标题与导航统一中文为主

- 8 篇文章标题改为中文（保留英文缩写作为专有名词）：
  - EgoScale → EgoScale：大规模人类第一人称 视频预训练与灵巧操作
  - HumanEgo → HumanEgo：零样本机器人学习的极致数据效率
  - VideoManip → VideoManip：从 RGB 视频重建 3D 轨迹的 无需穿戴设备的灵巧操作
  - EgoVerse → EgoVerse：全球 第一人称 机器人学习数据集
  - Transformer Architecture → Transformer 架构
  - World Action Models → World Action Models：从世界预测到可执行动作
  - 视觉 Transformer → 视觉 Transformer：一幅图像相当于 16×16 个词
  - 掩码自编码器（MAE） → 掩码自编码器（MAE）：可扩展的视觉自监督学习者
- 7 个 主题落地页标题改为中文：AI 基础设施、AI 芯片架构、深度学习、具身智能、强化学习、世界模型、科技公司
- 全局索引 (wiki/index.md) + 各主题子索引 + 延伸阅读交叉引用，全部同步更新
- mkdocs.yml 导航 修复：YAML 引号包裹含冒号标题，补全 Companies 和 ViT/MAE 导航缺失
- 知识图谱：重新生成 graph-data.json（25 节点, 52 边）

## [2026-06-19] 文章编写 | 视觉 Transformer （深度学习）

- 来源： raw/Deep-Learning/2020-10-22-vit-arxiv-2010.11929.md (arXiv:2010.11929, Google Research, ICLR 2021)
- 文章： wiki/Deep-Learning/vision-transformer.md
- 摘要： 图像块化为 16×16 词元，纯 Transformer 取代 CNN，大规模预训练是关键

## [2026-06-19] 文章编写 | 掩码自编码器 （深度学习）

- 来源： raw/Deep-Learning/2021-11-11-mae-arxiv-2111.06377.md (arXiv:2111.06377, Meta AI, CVPR 2022)
- 文章： wiki/Deep-Learning/mae.md
- 摘要： 75% 高比例遮挡像素重建，自监督预训练超越监督预训练，ViT 标准范式

## [2026-06-19] 材料接入 | 视觉 Transformer + 掩码自编码器（arXiv 下载）

- ViT (arXiv:2010.11929): Google Research, 2020-10, ICLR 2021 — 纯 Transformer 图像分类
- MAE (arXiv:2111.06377): Kaiming He / Meta AI, 2021-11, CVPR 2022 — 掩码自编码器自监督预训练
- 本地 PDF： raw/Deep-Learning/2020-10-22-vit-arxiv-2010.11929.pdf, 2021-11-11-mae-arxiv-2111.06377.pdf
- 原文笔记： raw/Deep-Learning/2020-10-22-vit-arxiv-2010.11929.md, 2021-11-11-mae-arxiv-2111.06377.md
- 状态： 本地导入完成，已编译至 wiki/Deep-Learning/

## [2026-06-19] 质量检查 | 未发现问题，无需修复

- 索引一致性：18 项索引与 18 个实际文件一致，无缺失或未收录文件
- 内部链接：全部有效，无断链
- 原文引用：检查 59 项，全部有效
- 辅助页面（overview.md、knowledge-graph.md）：链接全部有效
- 目录结构：6 个主题栏目与 6 个目录一致
- 本次检查无需修复，知识库结构一致

## [2026-06-19] 导航改版 |  优化 MkDocs 导航与主题

- 新增： navigation.indexes (主题落地页可点击), toc.follow, content.code.copy
- 新增： 中文本地化 界面语言与搜索语言均设为中文（zh）
- 新增： 主题主色与强调色统一设为靛蓝（indigo）
- 新增： 7 个主题 index.md 落地页 (AI-Infra, Chip-Architecture, Deep-Learning, Embodied-Intelligence, Reinforcement-Learning, World-Models, Companies)
- 新增： 丰富 Markdown 扩展 (admonition, details, tabbed, inlinehilite, caret, mark, tilde, attr_list, md_in_html, tables, footnotes)
- 更新： 全局 index.md 添加 hide: toc + overview.md 快捷链接
- 更新： 导航结构为 topic/index.md 首位模式

## [2026-06-19] 目录调整 | 新增具身智能分类

- 创建 wiki/Embodied-Intelligence/ 目录
- 从世界模型移入： egoscale.md, humanego.md
- 从深度学习移入： videomanip.md
- 新建： egoverse.md (EgoVerse 数据集编译)
- 更新： wiki/index.md, mkdocs.yml 导航
- 修复： 4 篇文章内部延伸阅读链接

## [2026-06-19] 材料接入 | 批量抓取 3 篇机器人学习论文（WebBridge）

- EgoScale (NVIDIA, arXiv:2602.16710): 20,854h 第一人称视频预训练, 对数线性规模规律, 22-DoF 灵巧手
- HumanEgo (UMD, arXiv:2605.24934): 零样本迁移, 30 分钟视频/任务→92.5% 成功率, 无需机器人数据
- VideoManip (CMU/UCB, arXiv:2602.09013): 从 RGB 视频重建 3D 手-物体轨迹, 无需穿戴设备的灵巧操作
- 本地 PDF： raw/World-Models/ + raw/Deep-Learning/
- 知识文章： wiki/World-Models/egoscale.md, humanego.md; wiki/Deep-Learning/videomanip.md
- 更新： wiki/index.md, mkdocs.yml 导航

## [2026-06-19] 文章编写 | EgoScale （具身智能）

- 来源： raw/World-Models/2026-02-20-egoscale-arxiv-2602.16710.md (NVIDIA arXiv)
- 文章： wiki/Embodied-Intelligence/egoscale.md
- 摘要： 20,854h 人类第一人称视频预训练，对数线性规模规律，22-DoF 灵巧手策略

## [2026-06-19] 文章编写 | HumanEgo （具身智能）

- 来源： raw/World-Models/2026-05-28-humanego-arxiv-2605.24934.md (UMD arXiv)
- 文章： wiki/Embodied-Intelligence/humanego.md
- 摘要： 零样本迁移，30 分钟视频/任务→92.5% 成功率，无需机器人数据

## [2026-06-19] 文章编写 | VideoManip （具身智能）

- 来源： raw/Deep-Learning/2026-02-09-videomanip-arxiv-2602.09013.md (CMU/UCB arXiv)
- 文章： wiki/Embodied-Intelligence/videomanip.md
- 摘要： 从 RGB 人类视频直接重建 3D 手-物体轨迹，无需穿戴设备的灵巧操作学习

## [2026-06-19] 文章编写 | EgoVerse （具身智能）

- 来源： raw/World-Models/2026-04-08-egoverse-egocentric-human-dataset.md
- 文章： wiki/Embodied-Intelligence/egoverse.md
- 状态： 已完成文章编写（此前待编写）

## [2026-06-19] 材料接入 | EgoVerse （世界模型）

- 来源： arXiv:2604.07607, Georgia Tech/Stanford/MIT/Meta/ETH Zürich/Scale AI
- 获取方式：Kimi WebBridge 浏览器自动化
- 本地 PDF： raw/World-Models/2026-04-08-egoverse-egocentric-human-dataset.pdf (22.54 MB)
- 原文笔记： raw/World-Models/2026-04-08-egoverse-egocentric-human-dataset.md
- 状态： WebBridge 获取成功，原文已保存，待编写知识文章

## [2026-06-03] 质量检查 | 发现 3 项问题，已修复 3 项

- 已移除失效的延伸阅读链接： m100-npu-details, mcts-fundamentals, transformer-positional-encoding

## [2026-06-03] 材料接入 | X Corp. 公司概况

- 来源： https://about.x.com/en (security-and-privacy, lobbying-disclosures, brand-toolkit, legal imprint, es/twitter-for-good)
- 新增： Companies/x-corp-company-profile.md

## [2026-05-31] 文章编写 | AI 基础设施（新增主题）

- 来源： raw/AI-Infra/2026-W18-ai-infra.md (论文雷达周报 W18)
- 新增： llm-inference-scheduling.md, distributed-training-parallelism.md, kv-cache-management.md

## [2026-05-31] 文章编写 | AI 芯片架构（新增主题）

- 来源： raw/Chip-Architecture/m100-li-auto-dataflow-architecture.md (M100 ISCA 2026 论文笔记)
- 新增： m100-orchestrated-dataflow-architecture.md

## [2026-05-31] 文章编写 | 深度学习（新增文章）

- 来源： raw/Deep-Learning/2026-W19-deep-learning.md, raw/Deep-Learning/2026-W20-physics-informed-ai.md
- 新增： mamba-3-state-space-models.md, looped-transformers-stability.md, noise-stability-regularization.md, k-pinn-lattice-boltzmann.md, solver-in-the-loop-deeponet.md, pinn-ecosystem-2026.md

## [2026-05-31] 文章编写 | 世界模型（新增主题）

- 来源： raw/World-Models/2025-ding-world-models-survey.md, 2025-vjepa2-lecun.md, 2026-ad-list-jepa-lidar.md, 2026-c-jepa-causal.md, 2026-W21-world-models.md
- 新增： world-models-survey.md, v-jepa-2.md, causal-jepa.md, jepa-ecosystem-2026.md, world-action-models.md

## [2026-05-31] 材料接入 | 补充 20 篇原始论文摘要到 raw/

- AI-Infra: dai-llm-inference-scheduling (arXiv:2504.07347), amer-distributed-hybrid-parallelism (arXiv:2602.09109), liu-cachegen-kv-cache-compression (arXiv:2310.07240)
- Chip-Architecture: xie-m100-orchestrated-dataflow (arXiv:2604.17862, ISCA 2026)
- Deep-Learning: lahoti-mamba-3 (arXiv:2603.15569, ICLR 2026), labovich-looped-transformers (arXiv:2604.15259), haris-noise-stability (arXiv:2602.08287, ICLR 2026), santoni-compiler-first-ssd (arXiv:2603.09555), xu-geometry-multitask-grokking (arXiv:2602.18523), meshram-k-pinn (arXiv:2604.03481), dehaghani-qpinn (arXiv:2605.13892)
- World-Models: ding-world-models-survey (arXiv:2411.14499), assran-v-jepa-2 (arXiv:2506.09985), nam-causal-jepa (arXiv:2602.11389, ICML 2026), zhu-ad-list-jepa (arXiv:2602.12540), he-demo-jepa (arXiv:2605.20811), hou-world-model-robot-learning (arXiv:2605.00080), li-mola (arXiv:2605.12167, ICML 2026), terver-jepa-wm-planning (arXiv:2512.24497, TMLR), lin-world-ego-modeling (arXiv:2605.19957)
- 更新： 所有关联 wiki 文章的 Raw 字段添加了原始论文引用

## [2026-05-30] 文章编写 | Transformer Architecture （新增深度学习主题）

- 来源： raw/Deep-Learning/2017-06-12-attention-is-all-you-need.md (arXiv:1706.03762, NIPS 2017)
- 新增： wiki/Deep-Learning/transformer-architecture.md

## [2026-05-30] 文章编写 | AlphaGo （新增强化学习主题）

- 来源： raw/Reinforcement-Learning/2016-01-28-mastering-the-game-of-go-with-deep-neural-networks-and-tree-search.md (Nature 2016)
- 新增： wiki/Reinforcement-Learning/alphago.md
