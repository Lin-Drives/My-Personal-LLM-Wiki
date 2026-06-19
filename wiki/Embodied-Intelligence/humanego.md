# HumanEgo：零样本机器人学习的极致数据效率

## Source

- **Original**: [raw/World-Models/2026-05-28-humanego-arxiv-2605.24934.md](../raw/World-Models/2026-05-28-humanego-arxiv-2605.24934.md)
- **Type**: arXiv preprint
- **Date**: 2026-05-28
- **URL**: https://arxiv.org/abs/2605.24934
- **Authors**: Zhi Wang, Botao He, Kelin Yu, Seungjae Lee, Ruohan Gao, Furong Huang, Yiannis Aloimonos (University of Maryland)
- **Code**: https://github.com/TX-Leo/HumanEgo
- **Website**: https://humanego-ai.github.io/

## Raw Content

> HumanEgo is robot-data-free, hardware-agnostic, data-efficient, and zero-shot human-to-robot transferable. With only 30 minutes of human videos per task, achieves 92.5% average success across four real-world tasks (75% with just 15 minutes), outperforms matched-time robot teleoperation by 41%.

## Overview

HumanEgo 是 UMD 提出的**零样本人类到机器人迁移框架**，与 EgoScale 的"大规模预训练"路线不同，HumanEgo 走的是**极端数据效率**路线：仅需 **30 分钟人类 egocentric 视频/任务**，无需任何机器人数据，即可实现零样本迁移。核心创新在于通过**视觉预处理（手臂 inpainting + 虚拟夹爪渲染）**和**Interaction-Centric Tokens (ICT)** 来桥接 embodiment gap。

## Body

### 核心问题：没有机器人数据，仅用人类视频能学到什么？

传统方法要么需要大量机器人遥操作数据（昂贵），要么需要大规模预训练（计算密集）。HumanEgo 问了一个更激进的问题：**如果只有 30 分钟人类视频，能做到什么？**

#### 四阶段流程

```
人类佩戴 Aria 眼镜采集 → 视觉预处理 → ICT 编码 → Flow Matching 策略
```

| 阶段 | 技术 | 作用 |
|------|------|------|
| **1. 数据采集** | Aria Gen1 眼镜 + MPS | 6-DoF SLAM、3D 手部姿态、同步 RGB 流 |
| **2. 视觉预处理** | SAM2 + LaMa inpainting | 分割并移除人类手臂，消除视觉 embodiment gap |
| **3. 虚拟渲染** | 渲染虚拟夹爪 + 物体关键点 | 将 6D 姿态信息编码为视觉线索 |
| **4. ICT 编码** | 实体级交互表示 | 每个实体相对于其他任务实体的姿态 |
| **5. 策略学习** | Flow Matching + 3 个辅助目标 | 多模态双臂动作生成 |

#### 为什么 30 分钟就够？

- **Dense auxiliary objectives**：每个轨迹提供密集监督，放大有限数据的信号
- **Flow matching**：相比扩散模型，flow matching 在少样本下更稳定
- **Entity-level representation**：不学习"人类如何做"，而是学习"手-物体交互的几何关系"
- **Hardware-agnostic**：策略不依赖特定机器人形态，零样本迁移到新机器人

### 实验：四个真实世界任务

| 任务 | 类型 | 难度 |
|------|------|------|
| **Serve Bread** | 拾取-放置 | 中等 |
| **Downstack Cups** | 长程多步骤 | 高（需顺序推倒、抓取、重新堆叠） |
| **Water Flowers** | 接触丰富双臂 | 高（严格时序：一手持喷嘴，一手开阀门） |
| **Adjust Table** | 持续旋转控制 | 高（三整圈旋转，不释放） |

**结果对比**（30 分钟人类数据）：

| 方法 | 平均成功率 | 备注 |
|------|-----------|------|
| HumanEgo | **92.5%** | 零样本，无机器人数据 |
| ACT (机器人遥操作) | 51.2% | 需要 30 分钟机器人遥操作 |
| EgoZero | 45.0% | 零样本方法 |
| Point Policy | 19.2% | 关键点方法 |
| ZeroMimic | 5.8% | 目标条件方法 |
| Track2Act | 1.9% | 2D 跟踪方法 |

**关键发现**：即使是 **15 分钟** 人类数据（75.0%），也超过了 30 分钟机器人遥操作（51.2%）。

### 零样本迁移能力

- **新机器人**：无需重新训练，直接部署到新 embodiment
- **新相机**：不同视角、不同内参
- **新环境**：不同的桌子高度、光照、背景

这种泛化能力来源于 ICT 的**相对几何表示**：策略学习的是实体之间的空间关系，而不是绝对像素模式。

## Key Takeaways

- **30 分钟人类视频可以超越 30 分钟机器人遥操作** — 人类视频是 surprisingly potent 的数据源
- **视觉预处理（inpainting + 虚拟渲染）** 是桥接 embodiment gap 的关键，无需昂贵的域适应
- **ICT 表示**让策略对 embodiment、视角、环境不变
- **Flow matching + dense auxiliary objectives** 在极少量数据下也能稳定训练
- **完全开源**：https://github.com/TX-Leo/HumanEgo

## See Also

- [EgoScale：大规模人类视频预训练](egoscale.md) — NVIDIA 的大规模预训练路线，20,854 小时人类数据，log-linear scaling law
- [VideoManip：从 RGB 视频重建 3D 轨迹](videomanip.md) — 从 RGB 视频重建 3D 手-物体轨迹，device-free 灵巧操作
- [EgoVerse：全球 egocentric 数据集](egoverse.md) — 最大 egocentric 机器人学习数据集，1,362h/80k episodes
- [World Action Models：从世界预测到可执行动作](../World-Models/world-action-models.md) — 从预测世界到可执行动作的范式转变
