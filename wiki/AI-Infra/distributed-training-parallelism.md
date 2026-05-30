# 分布式 LLM 训练与推理并行策略

> Sources: 多篇综述整合, 2026
> Raw: [../../raw/AI-Infra/2026-amer-distributed-hybrid-parallelism.md](../../raw/AI-Infra/2026-amer-distributed-hybrid-parallelism.md); [../../raw/AI-Infra/2026-W18-ai-infra.md](../../raw/AI-Infra/2026-W18-ai-infra.md) (编译参考)

## Overview

系统梳理了分布式 LLM 训练和推理中的混合并行策略全景：数据并行(DP)、张量并行(TP)、流水线并行(PP)、序列并行(SP)、专家并行(EP)。涵盖每种策略的通信模式、内存占用和适用场景的数学建模，从 Megatron-LM 到 DeepSeek DualPipe 均有覆盖。

## 五大并行策略

| 策略 | 原理 | 通信模式 | 代表框架 |
|------|------|---------|---------|
| DP (Data Parallelism) | 数据分片，每卡持有完整模型副本 | AllReduce 梯度同步 | PyTorch FSDP |
| TP (Tensor Parallelism) | 单层权重切分到多卡 | AllReduce 激活同步 | Megatron-LM |
| PP (Pipeline Parallelism) | 模型分层分到多卡 | 点对点激活传递 | DeepSpeed |
| SP (Sequence Parallelism) | 长序列切分到多卡 | 注意力计算跨卡 | DeepSpeed Ulysses |
| EP (Expert Parallelism) | MoE 专家路由到不同卡 | All-to-All | DeepSeek |

## 混合并行趋势

单一并行策略已不够用。现代 LLM 训练/推理标配 DP+TP+PP 组合，MoE 模型进一步加入 EP。DeepSeek DualPipe 在 PP 基础上自研通信调度，是这个方向的典型创新。

## See Also

- [LLM 推理调度理论](../AI-Infra/llm-inference-scheduling.md)
- [KV Cache 管理](../AI-Infra/kv-cache-management.md)
