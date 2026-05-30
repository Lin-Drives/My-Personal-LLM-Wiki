# C-JEPA: 物体级潜在干预的因果世界模型

> Sources: Nam, Le Lidec, Maes, LeCun, Balestriero — 2026 / arXiv:2602.11389
> Raw: [../../raw/World-Models/2026-nam-causal-jepa-object-level.md](../../raw/World-Models/2026-nam-causal-jepa-object-level.md); [../../raw/World-Models/2026-c-jepa-causal.md](../../raw/World-Models/2026-c-jepa-causal.md) (编译参考)

## Overview

将 JEPA 从 patch 级掩码预测升级为物体级掩码干预。通过 Slot Attention 提取物体槽位后，跨时间掩码整个物体，强制模型用其他物体的演化推断被掩码物体的状态。这种训练机制注入因果归纳偏置，让世界模型学会"物体 A 影响物体 B"的交互动力学。反事实 VQA 提升约 20%，仅用 1% DINO-WM 的输入特征达到可比规划性能。

## 核心问题

传统 JEPA 随机掩码 image patch，模型可通过局部纹理、物体自身动力学"作弊"预测，不需要理解物体间的关系。C-JEPA 通过物体级跨时间掩码，迫使模型做真正的交互推理。

## 方法

```
传统 JEPA: [图像] → patch → 随机掩码 → 预测
C-JEPA:    [视频] → Slot Attention → 掩码整个物体(所有帧) → 从其他物体推断
```

1. Frozen Slot Attention Encoder 提取 K 个物体槽位
2. 物体级掩码：跨整个历史窗口擦除一个物体
3. Transformer Predictor 联合恢复历史+预测未来

## 关键结果

- 反事实 VQA: 比同架构无物体掩码提升 ~20% 绝对
- Agent 规划: 仅用 DINO-WM 1% 输入特征达到可比性能

## 定位

JEPA 家族从"表征学习"走向"因果理解"的关键一跃。不生成像素、不学显式因果图，靠训练时的干预机制注入因果偏置。

## See Also

- [JEPA 生态 2026](../World-Models/jepa-ecosystem-2026.md)
- [V-JEPA 2](../World-Models/v-jepa-2.md)
- [世界模型综述](../World-Models/world-models-survey.md)
