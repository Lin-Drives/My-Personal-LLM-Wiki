# EgoVerse：全球 egocentric 机器人学习数据集

## Source

- **Original**: [raw/World-Models/2026-04-08-egoverse-egocentric-human-dataset.md](../raw/World-Models/2026-04-08-egoverse-egocentric-human-dataset.md)
- **Type**: arXiv preprint
- **Date**: 2026-04-08
- **URL**: https://arxiv.org/abs/2604.07607
- **Authors**: Ryan Punamiya, Simar Kareer, Zeyi Liu, Josh Citron, Ri-Zhao Qiu, Xiongyi Cai, Alexey Gavryushin, Jiaqi Chen, Davide Liconti, Lawrence Y. Zhu, Patcharapong Aphiwetsa, Baoyu Li, Aniketh Cheluva, Pranav Kuppili, Yangcen Liu, Dhruv Patel, Aidan Gao, Hye-Young Chung, Ryan Co, Renee Zbizika, Jeff Liu, Xiaomeng Xu, Haoyu Xiong, Geng Chen, Sebastiano Oliani, Chenyu Yang, Xi Wang, James Fort, Richard Newcombe, Josh Gao, Jason Chong, Garrett Matsuda, Aseem Doriwala, Marc Pollefeys, Robert Katzschmann, Xiaolong Wang, Shuran Song, Judy Hoffman, Danfei Xu (Georgia Tech, Stanford, UCSD, ETH Zürich, MIT, Meta, Scale AI)
- **Website**: https://egoverse.ai/

## Raw Content

> EgoVerse is a collaborative platform for human data-driven robot learning that unifies data collection, processing, and access under a shared framework. The current release includes 1,362 hours (80k episodes) of human demonstrations spanning 1,965 tasks, 240 scenes, and 2,087 unique demonstrators.

## Overview

EgoVerse 是迄今为止**最大的 egocentric 人类操作数据集**，由学术界和工业界联合构建，专为机器人学习设计。与 Ego4D、EPIC-KITCHENS 等通用人类视频数据集不同，EgoVerse 聚焦于**机器人可执行的操纵任务**，提供标准化的格式、操纵相关的标注（3D 手部/头部姿态、子任务级描述）和配套工具链。

## Body

### 核心问题：为什么需要一个"为机器人而生"的人类数据集？

通用人类视频数据集（Ego4D、EPIC-KITCHENS）虽然规模大，但存在根本性的局限：
- 缺乏操纵相关的标注（力/接触/手部关节角度）
- 包含大量机器人无法执行的任务（如跑步、游泳）
- 静态发布，难以扩展和更新

EgoVerse 的设计理念是 **"bounded diversity"** — 只收录双臂移动机器人可执行的任务，同时保持场景、物体、演示者的自然多样性。

#### 双组件架构：EgoVerse-A + EgoVerse-I

| 组件 | 目的 | 来源 | 特点 |
|------|------|------|------|
| **EgoVerse-A** (Academic) | 可复现研究 | 参与实验室标准化采集 | 严格协议、镜像采集、系统分析 |
| **EgoVerse-I** (Industry) | 规模与多样性 | 工业伙伴野外采集 | 真实场景、持续注入、对齐产业需求 |

#### 数据规模

| 指标 | 数值 |
|------|------|
| 总时长 | 1,362 小时 |
| 片段数 | 79,692 episodes |
| 任务数 | 1,965 个 |
| 场景数 | 240 个 |
| 演示者 | 2,087 人 |
| 标注 | 3D 手部/头部姿态、子任务级描述、操纵相关信号 |

### EgoDB：活的、可增长的数据管理系统

与 prior 静态数据集不同，EgoVerse 通过 **EgoDB** 支持持续数据注入：
- 标准化数据处理管线
- 统一存储格式
- 可控数据访问权限
- 可视化工具
- 下游学习算法接口
- 手机轻量采集 App（降低参与门槛）

### 人类到机器人迁移：跨实验室大规模研究

EgoVerse 不仅是数据集，更是一项**跨机构可复现研究**。

**实验设置**：
- 多机器人：Robot A/B/C（不同 embodiment）
- 多任务：object-in-container（单臂）、cup-on-saucer（精细双臂）、bag-grocery（长程双臂）
- 共享协议：统一任务定义、评估标准、数据格式

**核心发现**：
- 联合训练（EgoVerse-A + 机器人数据）显著提升性能：领域内 + 领域外最高提升 30%
- 人类数据对齐是关键：人类数据与机器人学习目标的对齐程度决定缩放效果
- 场景多样性影响泛化：在有限数据预算下，场景多样性对泛化能力至关重要

## Key Takeaways

- **最大的 egocentric 机器人学习数据集**：1,362 小时 / 80k episodes / 2k+ 演示者
- **活的生态系统**：EgoDB 支持持续注入，不是一次性静态发布
- **跨机构可复现**：共享协议 + 多机器人 + 多任务验证
- **人类数据对齐是 scaling 的关键**：单纯增加数据不够，需要与机器人目标对齐
- **场景多样性驱动泛化**：有限数据下优先增加场景多样性

## See Also

- [EgoScale：大规模人类视频预训练](egoscale.md) — NVIDIA 20,854h 预训练，log-linear scaling law
- [HumanEgo：零样本机器人学习](humanego.md) — 30 分钟零样本迁移，极端数据效率
- [VideoManip：从 RGB 视频重建 3D 轨迹](videomanip.md) — 从 RGB 视频重建 3D 轨迹，device-free 灵巧操作
- [World Action Models：从世界预测到可执行动作](../World-Models/world-action-models.md) — 从预测世界到可执行动作
