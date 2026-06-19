# Mamba-3: 状态空间模型的新范式

> Sources: Li, Chen, Wang, Bick, Kolter, Dao, Gu — ICLR 2026 Oral
> Raw: [../../raw/Deep-Learning/2026-lahoti-mamba-3-ssm.md](../../raw/Deep-Learning/2026-lahoti-mamba-3-ssm.md); [../../raw/Deep-Learning/2026-W19-deep-learning.md](../../raw/Deep-Learning/2026-W19-deep-learning.md) (编译参考)

## Overview

Mamba-3 从 inference-first 视角提出三大改进：(1) 更 expressive 的 recurrence（基于 SSM discretization）；(2) complex-valued state update rule，实现 richer state tracking；(3) MIMO (multi-input multi-output) formulation，不增加 decode latency 的前提下提升性能。1.5B 规模下比 Gated DeltaNet 高 0.6pp，MIMO variant 再提升 1.2pp。用一半的 state size 即可达到 Mamba-2 的 perplexity，显著推进了 performance-efficiency Pareto frontier。

## 核心创新

### Complex-Valued State Update

引入复数状态更新规则，在数学上更接近生物神经系统的振荡动力学。这使得模型能够追踪更丰富的状态信息，而不增加参数量。

### MIMO Formulation

多输入多输出的公式化，在不增加 decode latency 的前提下提升表达能力。这是与 Mamba-2 相比最关键的架构差异。

### Inference-First 设计哲学

从推理效率出发反推架构设计，而非训完再优化推理。这代表了 SSM 路线从"学术模型"走向"实用系统"的转变。

## 定位

ICLR 2026 Oral 接收，标志着 SSM 范式正式进入主流视野。与 Transformer 路线的关系从"替代"变为"互补"——不同任务场景选择不同骨干。

## See Also

- [Transformer 架构](../Deep-Learning/transformer-architecture.md)
- [Looped Transformers 稳定性](../Deep-Learning/looped-transformers-stability.md)
