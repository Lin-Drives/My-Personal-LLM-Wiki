# AI Infra 论文周报 — W32 (2026-08-02)

> 📡 **扫描周期：** 2026-07-12 至 2026-08-02  
> **重点：** AI Infrastructure / LLM Serving & Training Systems  
> **关键词：** disaggregated serving, KV cache, MoE parallelism, agentic RL training, speculative decoding

---

## 🔥 Top 5 核心看点

### 1. Kairos — 负载感知的 Prefill 偏转调度 (arXiv:2607.02043, 7月2日, Microsoft)
**一句话：** PD 分离架构下，把 Prefill 任务"甩"给负载轻的 Decode 节点，P95 TTFT 最高砍 81%。

- **痛点：** PD 分离后，Prefill 节点在流量突发时饱和，而 Decode 节点算力闲置；排队 + 跨节点 KV 传输占 TTFT 的 77-98%
- **解法：** Kairos 实时估计每个请求在 Prefill 节点的 TTFT，同时在每个 Decode 节点搜索"安全 chunk 大小"，在满足 TBT SLO 的前提下将 Prefill 任务偏转到 Decode 节点执行
- **效果：** P95 TTFT 降低最高 81%，SLO 达成率提升最高 79%，每次调度决策 < 1ms
- **意义：** PD 分离不是终点，动态负载均衡才是下一步

---

### 2. KV Cache 管理全景综述 (arXiv:2607.02574, 6月30日)
**一句话：** 这是目前最系统的 KV Cache 管理综述，把零散工作归纳成 6 大设计策略 + 5 种系统范式。

- **六大设计响应：**
  1. 本地 KV 虚拟化与阶段感知调度 (PagedAttention, Orca)
  2. KV 压缩/量化/稀疏化 ( eviction, quantization, compression)
  3. Prefill/Decode 分离 (DistServe, Splitwise)
  4. 跨层级 KV 迁移 (HBM → DRAM → 远端存储)
  5. 共享前缀缓存 (Prefix caching, RadixAttention)
  6. 多租户隔离与安全
- **五大系统范式：** 单体实例、分离式管道、共享存储池、分层缓存、无服务器
- **价值：** 做推理系统的人，这篇可以当导航图用

---

### 3. ELDR — MoE 解码路由的专家局部性感知 (arXiv:2607.00466, 7月1日)
**一句话：** MoE 的 Decode 阶段，"负载均衡"不够，还要看"专家局部性"。

- **发现：** 在 MoE 的 batched decode 中，延迟由批次中所有 token 选中的**专家并集**决定，而非 token 数量。active-expert 从 16 增至 128，MoE 层延迟涨 4.7×
- **解法：** ELDR 在 PD 分离的 decode 路由中引入专家局部性感知，将具有相似专家偏好的请求路由到同一 worker
- **意义：** MoE 推理优化进入了"第二维度"——不只是 load balance，还有 expert locality

---

### 4. Talaria — 面向 Agentic 负载的无服务器多模型推理 (arXiv:2607.17181, 7月19日)
**一句话：** 给 Agent 用的推理系统，模型切换和会话返回比单次推理更重要。

- **场景：** Agentic 工作流中，多模型切换频繁，会话可能中断后返回，传统 serving 假设"模型常驻 GPU"不再成立
- **设计：**
  - 模型可换出 GPU 而不丢失会话前缀
  - 基于会话返回概率的预加载策略
  - 多模型共置避免跨层 KV handoff
- **意义：** Agentic 负载正在重塑 serving 系统的核心假设

---

### 5. Molt — 轻量级 Agentic RL 训练框架 (arXiv:2607.21653, 7月22日)
**一句话：** 只有 8.6K 行代码的 PyTorch-native Agentic RL 框架，能训 1T MoE。

- **定位：** 比 verl (~62K LOC) 和 slime (~25K LOC) 更精简，专为 agentic 研究设计
- **架构：** AutoModel + vLLM，FSDP2 + EP/CP，原生支持 MoE
- **亮点：**
  - Agent 就是普通 Python 函数，无 DSL
  - 权重同步走 NCCL broadcast，不经过 router
  -  speculation decoding、prefix caching、CUDA graphs 都是 engine flag
- **验证：** 700B MoE @ EP256 端到端跑通；Qwen3-30B-A3B 上与 slime 吞吐量持平 (461 vs 502 tok/GPU/s)
- **意义：** Agentic RL 训练门槛正在大幅降低

---

## 📋 其他值得关注的论文

### 训练系统

**Megatron-Core MoE 技术报告** (arXiv:2603.07685, 3月10日, NVIDIA)  
→ Parallel Folding 解耦 Attention 和 MoE 的并行策略，支持 7 维并行 (TP/CP/DP/PP/EP/ETP/EDP)。GB200 vs H100 上 DeepSeek-V3 配置调优的完整 case study。

**Lablup 504 GPU 预训练运维报告** (arXiv:2605.09370, 5月10日)  
→ 63 节点 B200 集群 (504 GPU) 55 天 Prometheus 数据分析。发现：故障率、重启时间、检查点策略对大规模训练效率的影响量化。Sokovan 调度器通过 hint-based polling 实现可预测调度延迟。

### 推理优化

**PROBE** (arXiv:2602.00509, 1月31日)  
→ MoE 推理中计算与通信的协同优化。连续 look-ahead pipelining 预测下一层专家激活，动态复制 + 预取，Prefill 延迟降低 1.32×，Decode 吞吐提升 1.26×。

**Token-Operations-Oriented Inference Optimization 综述** (arXiv:2606.20295, 6月18日)  
→ 从模型优化、计算-模型融合、计算-网络-模型融合三个层面系统梳理 LLM 推理优化。涵盖 continuous batching、chunked prefill、PD 分离、speculative decoding、量化等。

**FLASHINFER** (arXiv:2501.01005v2)  
→ 可组合格式的共享前缀注意力引擎，支持 block sparse KV cache 存储，共享前缀查询可复用高带宽 shared memory。

---

## 💡 本周趋势总结

| 趋势 | 观察 |
|------|------|
| **PD 分离深化** | Kairos、ELDR、Talaria 都在 PD 分离基础上做更细粒度的动态调度 |
| **MoE 并行成为标配** | Megatron-Core、Molt、PROBE 都围绕 MoE 的 EP/ETP/EDP 做优化 |
| **Agentic 负载倒逼架构** | Talaria 和 Molt 都面向 agentic/agentic RL 场景重新设计 serving/training |
| **KV Cache 进入系统级竞争** | 从单点 PagedAttention 发展到集群级调度、分层存储、前缀复用 |
| **框架轻量化** | Molt 8.6K LOC 对比 verl 62K LOC，说明"足够简单才能足够快" |

---

## 🔭 下周预告

W33 → **Deep Learning**

---

*龙虾小队 · Paper Radar 🦞*
