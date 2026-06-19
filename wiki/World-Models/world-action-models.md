# World Action Models：从世界预测到可执行动作

> Sources: W21 World Models 周报, 2026-05
> Raw: [../../raw/World-Models/2026-W21-world-models.md](../../raw/World-Models/2026-W21-world-models.md)

## Overview

2026 年 Q1-Q2 最明确的趋势：从"预测世界的模型"走向"同时预测世界和动作的模型"(WAM)。动作学习从密集模仿转向逆动力学对齐——让电机指令与预测的视觉未来对齐。

## 代表工作

| 模型 | 机构 | 关键能力 |
|------|------|---------|
| DreamZero | NVIDIA | 14B 扩散 Transformer，联合生成视频+动作，零样本策略 |
| Fast-WAM | — | 推理与动作解耦，7Hz 实时闭环控制 |
| Cosmos Policy | NVIDIA/Stanford | Cosmos 视频模型后训练，LIBERO 98.5% |
| WoVR | — | 世界模型作为 VLA 策略的可靠仿真器进行 RL 后训练 |
| MoLA | — | Mixture of Latent Actions，桥接想象与可执行动作 |

## 核心转变

传统方法：密集状态-动作模仿学习 → 在新的 task 上泛化差。
WAM 路线：先想象未来视频/状态 → 通过逆动力学模型转换为电机指令 → 对齐预测的未来与实际执行结果。

## MoLA 的关键洞察

解决 WAM "想得好看但做不出来"的问题。通过多个预训练逆动力学模型 (IDM) 作为隐动作接口的 mixture，增强动作解码的灵活性。

## See Also

- [JEPA 生态 2026](../World-Models/jepa-ecosystem-2026.md)
- [V-JEPA 2](../World-Models/v-jepa-2.md)
