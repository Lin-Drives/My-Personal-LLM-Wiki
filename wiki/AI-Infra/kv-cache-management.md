# KV Cache 管理

> Sources: Yuhan Liu et al., 2024; 多篇推理框架论文
> Raw: [../../raw/AI-Infra/2023-liu-cachegen-kv-cache-compression.md](../../raw/AI-Infra/2023-liu-cachegen-kv-cache-compression.md); [../../raw/AI-Infra/2026-W18-ai-infra.md](../../raw/AI-Infra/2026-W18-ai-infra.md) (编译参考)

## Overview

KV Cache 是 LLM 推理的内存瓶颈。从 vLLM 的 PagedAttention 到 SGLang 的 RadixTree 再到 CacheGen 的压缩流式传输，KV Cache 管理技术栈快速迭代。CacheGen 提出了 KV tensor 的压缩+按需流式加载方案，与传统内存管理策略互补。

## 技术栈演进

| 技术 | 核心思想 | 代表性工作 |
|------|---------|-----------|
| PagedAttention | 分页管理 KV Cache，消除碎片 | vLLM |
| RadixTree | 前缀共享，多请求复用 | SGLang |
| Compression | 压缩 KV tensor，降低传输开销 | CacheGen |
| Streaming | 按需流式加载，减少常驻内存 | CacheGen, FlashInfer |

## CacheGen 核心思路

KV Cache 压缩后按需流式加载，大幅降低多轮对话和多副本部署的内存压力。与 PagedAttention 的分页管理正交互补——一个解决"怎么存"，一个解决"怎么传"。

## 趋势

KV Cache 管理正从单机内存优化走向分布式架构下的全局调度问题。NVIDIA Dynamo 的 KV cache 感知路由代表了这一方向。

## See Also

- [LLM 推理调度理论](../AI-Infra/llm-inference-scheduling.md)
- [分布式并行策略](../AI-Infra/distributed-training-parallelism.md)
