# JEPA 生态 2026

> Sources: W21 World Models 周报 + 多篇 JEPA 论文笔记, 2026-05
> Raw: [../../raw/World-Models/2026-W21-world-models.md](../../raw/World-Models/2026-W21-world-models.md); [../../raw/World-Models/2026-ad-list-jepa-lidar.md](../../raw/World-Models/2026-ad-list-jepa-lidar.md)

## Overview

LeCun 的 JEPA 路线在 2026 年全面开花。从 I-JEPA (2023, 图像) 到 V-JEPA 2 (2025, 视频+机器人) 到 C-JEPA (2026, 因果) 到 AD-LiST-JEPA (2026, LiDAR)，JEPA 正从"自监督表征学习工具"进化为"机器人控制的默认 backbone"。

## 进化路线

```
2023  I-JEPA         — 图像: patch 掩码 → 预测表征
2024  V-JEPA         — 视频: 时空 patch 掩码
2025  V-JEPA 2       — 视频+机器人: 预测+规划，零样本控制
2025  LeJEPA         — 理论: 数学可扩展性证明
2025  VL-JEPA        — 视觉-语言跨模态
2026  C-JEPA         — 因果: 物体级掩码 → 交互推理
2026  AD-LiST-JEPA   — LiDAR: 3D 点云时空 JEPA → 自动驾驶
2026  Demo-JEPA       — 跨具身 one-shot 模仿 (VJEPA2.1 backbone)
2026  EB-JEPA         — 能量化: 解决特征坍塌
```

## 工程配方

"What Drives Success in Physical Planning with JEPA-WMs?" 给出的关键设计选择:
- **RoPE + sequence conditioning**: 大多数任务上最稳健
- **AdaLN**: 防止动作信息在深层网络中消失
- **Encoders frozen**: 表征质量不依赖下游任务

## 趋势

JEPA 不再是"LeCun 一个人的执念"——Demo-JEPA 的跨具身迁移、AD-LiST-JEPA 的 LiDAR 适配、V-JEPA 2 的机器人落地，证明了这条路线在不同模态、不同任务上的通用性。

## See Also

- [世界模型综述](../World-Models/world-models-survey.md)
- [V-JEPA 2](../World-Models/v-jepa-2.md)
- [Causal-JEPA](../World-Models/causal-jepa.md)
- [World Action Models：从世界预测到可执行动作](../World-Models/world-action-models.md)
