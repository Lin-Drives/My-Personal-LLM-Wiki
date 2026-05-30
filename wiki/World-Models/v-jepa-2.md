# V-JEPA 2: 视频自监督到机器人零样本规划

> Sources: Assran, Bardes, LeCun et al. — CVPR 2025 / arXiv:2506.09985
> Raw: [../../raw/World-Models/2025-assran-v-jepa-2.md](../../raw/World-Models/2025-assran-v-jepa-2.md); [../../raw/World-Models/2025-vjepa2-lecun.md](../../raw/World-Models/2025-vjepa2-lecun.md) (编译参考)

## Overview

证明了仅通过百万小时互联网视频自监督预训练 + 62小时无标注机器人视频微调，就能得到一个能理解视频、预测未来、并零样本在真实 Franka 机械臂上执行物体抓取/放置任务的世界模型——无需任务特定训练、无需奖励函数、无需目标环境数据。这是 LeCun 对"LLM 不懂物理世界"批评的实证回应。

## 三步 Pipeline

1. **V-JEPA 2 预训练 (Action-Free)** — 百万小时互联网视频，JEPA 预测视频帧在 latent space 的嵌入，不重建像素
2. **LLM 对齐** — 视觉表征与语言模型对齐，8B 规模达到视频问答 SOTA (PerceptionTest 84.0, TempCompass 76.9)
3. **V-JEPA 2-AC 后训练** — < 62 小时无标注机器人视频微调，在 latent space 学习动作条件世界模型，零样本在两个不同实验室的 Franka 机械臂上部署

## 关键结果

| 任务 | 结果 | 对比 |
|------|------|------|
| SSv2 动作理解 | 77.3% top-1 | 超越 task-specific 模型 |
| Epic-Kitchens 动作预测 | 39.7 recall@5 | SOTA |
| Franka 零样本规划 | 成功 pick-and-place | 无需环境数据、无需奖励 |

## 方法论意义

杨立昆的 vision (LeCun 2022) 的实证落地。从纯视觉自监督 → 视频理解 → 语言对齐 → 机器人规划，串成完整证据链。证明了"不生成像素"的 JEPA 路线在实际机器人控制中是可行的。

## See Also

- [世界模型综述](../World-Models/world-models-survey.md)
- [Causal-JEPA](../World-Models/causal-jepa.md)
- [JEPA 生态 2026](../World-Models/jepa-ecosystem-2026.md)
