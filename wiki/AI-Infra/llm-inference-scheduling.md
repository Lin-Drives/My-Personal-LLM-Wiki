# LLM 推理调度理论

> Sources: Li, Dai, Peng, 2025
> Raw: [../../raw/AI-Infra/2025-dai-llm-inference-scheduling.md](../../raw/AI-Infra/2025-dai-llm-inference-scheduling.md); [../../raw/AI-Infra/2026-W18-ai-infra.md](../../raw/AI-Infra/2026-W18-ai-infra.md) (编译参考)

## Overview

从排队论角度建立了 LLM 推理调度的严格理论框架，提出 SLAI 调度器动态平衡 prefill/decode 阶段，在严格 TBT 延迟约束下实现吞吐量最优。高负载下 TTFT 降低 53%，服务容量提升 26%。被评价为 AI Infra 的"根论文"级工作——把 LLM 推理调度从经验工程推进到理论可证的阶段。

## SLAI 调度器

核心贡献是用排队论数学证明了 work-conserving scheduler 的吞吐量最优性。SLAI 动态平衡 prefill 和 decode 两个阶段的计算资源分配，解决了 vLLM/Sarathi-Serve 在异构 SLO 场景下的调度策略盲区。

关键指标:
- 高负载下 TTFT (Time to First Token) 降低 53%
- 服务容量提升 26%
- 在严格的 TBT (Time Between Tokens) 延迟约束下吞吐量最优

## 定位

传统推理调度（FCFS、Continuous Batching）本质是经验工程策略。SLAI 给出了首次严格理论分析，为调度决策提供了数学保证而非启发式规则。

## See Also

- [KV Cache 管理](../AI-Infra/kv-cache-management.md)
- [分布式并行策略](../AI-Infra/distributed-training-parallelism.md)
