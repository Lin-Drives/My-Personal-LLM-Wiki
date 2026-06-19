# EgoScale：大规模人类 egocentric 视频预训练与灵巧操作

## Source

- **Original**: [raw/World-Models/2026-02-20-egoscale-arxiv-2602.16710.md](../raw/World-Models/2026-02-20-egoscale-arxiv-2602.16710.md)
- **Type**: arXiv preprint
- **Date**: 2026-02-20
- **URL**: https://arxiv.org/abs/2602.16710
- **Authors**: Ruijie Zheng, Dantong Niu, Yuqi Xie, Jing Wang, Mengda Xu, Yunfan Jiang, Fernando Castañeda, Fengyuan Hu, You Liang Tan, Letian Fu, Trevor Darrell, Furong Huang, Yuke Zhu, Danfei Xu, Linxi Fan (NVIDIA + UC Berkeley + UMD)
- **Website**: https://research.nvidia.com/labs/gear/egoscale/

## Raw Content

> 20,854 hours of action-labeled egocentric human video, more than 20× larger than prior efforts. Log-linear scaling law: L = 0.024 − 0.003 × ln(D), R² = 0.9983. Three-stage pipeline: human pretraining → aligned mid-training → task-specific fine-tuning.

## Overview

EgoScale 是 NVIDIA 提出的**大规模人类到灵巧操作迁移框架**，核心发现是：**人类 egocentric 视频数据存在可预测的 scaling law**，验证损失与真实机器人性能强相关（R² = 0.9983）。20,854 小时的训练数据让 22-DoF 灵巧手策略的平均成功率比无预训练基线提升 54%，且仅需少量机器人数据即可实现 one-shot 任务适应。

## Body

### 核心问题：为什么人类视频数据能 scale 灵巧操作？

传统机器人学习依赖昂贵的机器人遥操作数据，而人类每天都在进行大量灵巧操作。EgoScale 的核心假设是：**人类 egocentric 视频不仅是数据来源，更是可预测的监督信号**。

#### 三阶段训练管线

| 阶段 | 数据 | 目的 | 训练细节 |
|------|------|------|----------|
| **Stage I: 人类预训练** | 20,854h 人类 egocentric 视频 | 学习通用操作先验 | 256×GB200, 100K steps, batch=8192, lr=5e-5 |
| **Stage II: 对齐中训练** | 50h 人类 + 4h 机器人 (344 任务) | 桥接 embodiment gap | 冻结 VLM 主干，只更新视觉编码器 + DiT 专家 |
| **Stage III: 任务微调** | 任务特定机器人演示 | 适配目标任务 | 10K steps, batch=512, lr=3e-5 |

#### 架构设计：Flow-based VLA + 轻量适配器

- **VLM 主干**：共享的 ViT 编码视觉输入，语言指令编码为文本嵌入
- **DiT 动作专家**：Diffusion Transformer 预测未来动作块，使用 flow matching 目标
- ** embodiment 适配器**：轻量 MLP 处理不同机器人的本体感知状态输入和手部动作输出
- **人类动作占位符**：人类视频没有本体感知信号，用可学习占位符替代，无需架构修改

#### 动作表征：消除全局依赖

- **腕部运动**：相对 SE(3) 变换 ΔWₜ = (Wₜ₋₁)⁻¹Wₜ，消除全局相机位置依赖
- **手部动作**：21 个人类手部关键点通过优化重定向到 22-DoF Sharpa 机器人手空间

### Scaling Law：人类数据的 log-linear 规律

EgoScale 最显著的科学贡献是发现了**人类数据规模与验证损失之间的 log-linear scaling law**：

```
L = 0.024 − 0.003 × ln(D)
```

- D = 人类预训练数据小时数
- R² = 0.9983，几乎完美拟合
- 关键发现：**验证损失直接预测真实机器人性能**，平均任务完成率从 1k 小时的 0.30 单调提升至 20k 小时的 0.71

这意味着：更多人类 egocentric 视频 = 更好的机器人策略，且这种关系是可预测、可度量的。

### 实验结果

- **仿真**：70.25% 抓取成功率（20 个不同物体，Inspire Hand）
- **真实世界**：62.86% 平均成功率（7 个任务，LEAP Hand），比重定向基线高 15.87%
- **One-shot 适应**：仅需 1 个机器人演示即可有效泛化
- **跨 embodiment 迁移**：从 22-DoF 灵巧手有效迁移到低自由度手机器人

## Key Takeaways

- **人类 egocentric 视频是灵巧操作的可预测监督源**，存在明确的 log-linear scaling law
- **三阶段解耦设计**将规模学习（Stage I）和 embodiment 对齐（Stage II）分离，提升工程可行性
- **相对腕部运动 + 手部重定向**的动作表征消除了人类与机器人之间的 embodiment gap
- **轻量 MLP 适配器**让同一模型支持多机器人平台，无需重新训练主干

## See Also

- [HumanEgo：零样本机器人学习](humanego.md) — 30 分钟 egocentric 视频的零样本机器人学习
- [EgoVerse：全球 egocentric 数据集](egoverse.md) — 最大 egocentric 机器人学习数据集
- [VideoManip：从 RGB 视频重建 3D 轨迹](videomanip.md) — 从 RGB 视频重建 3D 手-物体轨迹，device-free 灵巧操作
- [World Action Models：从世界预测到可执行动作](../World-Models/world-action-models.md) — 从预测世界到可执行动作
