# VideoManip：从 RGB 视频重建 3D 轨迹的 device-free 灵巧操作

## Source

- **Original**: [raw/Deep-Learning/2026-02-09-videomanip-arxiv-2602.09013.md](../raw/Deep-Learning/2026-02-09-videomanip-arxiv-2602.09013.md)
- **Type**: arXiv preprint
- **Date**: 2026-02-09
- **URL**: https://arxiv.org/abs/2602.09013
- **Authors**: Hongyi Chen, Tony Dong, Tiancheng Wu, Liquan Wang, Yash Jangir, Yaru Niu, Yufei Ye, Homanga Bharadhwaj, Zackory Erickson, Jeffrey Ichnowski (CMU + UC Berkeley)

## Raw Content

> VideoManip is a device-free framework that learns dexterous manipulation directly from RGB human videos. Reconstructs explicit 3D robot-object trajectories from monocular videos by estimating human hand poses, object meshes, and retargets the reconstructed human motions to robotic hands. 70.25% success in simulation (20 objects), 62.86% in real world (7 tasks).

## Overview

VideoManip 提出了**从 RGB 人类视频直接学习灵巧操作**的 device-free 框架，与 EgoScale/HumanEgo 的 egocentric 路线不同，VideoManip 专注于**从普通第三人称 RGB 视频**（如 YouTube、Instagram）重建 3D 手-物体交互轨迹，然后重定向到机器人手进行策略学习。核心创新是**手-物体接触优化**和**从单视频生成多样化训练轨迹**的合成策略。

## Body

### 核心问题：不用任何传感器，仅用 RGB 视频能学到灵巧操作吗？

现有方法要么需要昂贵的动作捕捉设备（MANUS 手套、Vive tracker），要么需要 egocentric 视角（Aria 眼镜）。VideoManip 走了一条更普适的路线：**从任意 RGB 人类视频学习**。

#### 三步重建管线

```
RGB 人类视频 → 3D 手部姿态估计 + 物体网格重建 → 运动重定向 → 机器人策略
```

| 步骤 | 技术 | 输出 |
|------|------|------|
| **1. 手部估计** | 基于 transformer 的 3D 手部姿态估计 | 每帧 21 个手部关键点 + 6D 腕部姿态 |
| **2. 物体重建** | 单目 3D 物体重建 | 物体网格 + 6D 物体姿态 |
| **3. 运动重定向** | 手部轨迹 → 机器人手关节空间 | 机器人手-物体交互轨迹 |

#### 接触优化：让重建数据适合灵巧操作

直接从人类视频重建的数据往往不适合机器人训练，因为：
- 人类手指和物体之间的接触模式与机器人不同
- 重建的轨迹可能违反物理约束
- 缺少 force/torque 信息

VideoManip 的解决方案：
- **Interaction-centric grasp modeling**：建模手-物体接触的几何关系
- **Contact optimization**：优化重建轨迹，确保物理可行性
- **Grasp stability analysis**：评估每个抓取配置的稳定性

#### 单视频多样化合成

一个 RGB 视频只能提供有限的数据。VideoManip 通过以下方式增加数据多样性：
- **轨迹扰动**：在关节空间对重建轨迹添加噪声
- **物体替换**：将视频中的物体替换为不同形状/纹理的物体
- **视角增强**：从不同虚拟相机视角渲染交互
- **时序子采样**：从同一视频提取多个子轨迹

### 实验结果

#### 仿真（Inspire Hand, 22-DoF）

| 指标 | 结果 |
|------|------|
| 抓取成功率 | 70.25%（20 个不同物体） |
| 物体类型 | 日常物品（杯子、瓶子、工具等） |
| 对比基线 | 重定向方法提升 15.87% |

#### 真实世界（LEAP Hand, 16-DoF）

| 任务 | 成功率 |
|------|--------|
| 7 个灵巧操作任务 | 62.86% 平均 |
| 对比重定向基线 | +15.87% |
| 数据来源 | 纯 RGB 人类视频，无机器人演示 |

### 与 EgoScale / HumanEgo 的对比

| 维度 | VideoManip | EgoScale | HumanEgo |
|------|-----------|----------|----------|
| **数据类型** | 第三人称 RGB 视频 | egocentric 人类视频 | egocentric 人类视频 |
| **传感器** | 无（device-free） | Aria 眼镜 / 头戴相机 | Aria 眼镜 |
| **3D 重建** | ✅ 显式重建手-物体轨迹 | ❌ 直接从像素学习 | ❌ 视觉预处理 + ICT |
| **数据规模** | 单视频即可 | 20,854 小时 | 30 分钟/任务 |
| **主要优势** | 最普适的数据源 | 可预测的 scaling law | 极致数据效率 |
| **机器人手** | Inspire / LEAP | Sharpa (22-DoF) | 通用 |

## Key Takeaways

- **RGB 视频是最普适的机器人学习数据源** — 不需要 egocentric 视角，不需要专用传感器
- **显式 3D 重建**（手-物体轨迹）比隐式学习（直接从像素）更适合灵巧操作
- **接触优化**是桥接人类视频到机器人策略的关键步骤
- **单视频多样化合成**让有限数据产生无限训练信号
- **三路线互补**：VideoManip（普适性）+ EgoScale（规模性）+ HumanEgo（效率性）

## See Also

- [EgoScale：大规模人类视频预训练](egoscale.md) — NVIDIA 20,854h 预训练，log-linear scaling law
- [HumanEgo：零样本机器人学习](humanego.md) — 30 分钟零样本迁移，极端数据效率
- [EgoVerse：全球 egocentric 数据集](egoverse.md) — 最大 egocentric 数据集，1,362h/80k episodes
- [World Action Models：从世界预测到可执行动作](../World-Models/world-action-models.md) — 从世界模型到可执行动作
