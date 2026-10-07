# AI Infra 论文周报 — W37 (2026-09-06)

> 📡 **扫描周期：** 2026-08-30 至 2026-09-06  
> **重点：** AI Infrastructure / LLM Serving, Training Systems & Hardware Co-design  
> **关键词：** KV cache disaggregation, sparse attention decode, MoE distributed training, CXL memory expansion, CPU-free inference

---

## 🔥 Top 5 核心看点

### 1. OasisKV — 用 Lookahead Sparse Prefetching 突破 HBM 天花板 (arXiv:2608.08097, 8月8日)
**一句话：** 把 decode 阶段的 KV cache 扩展到 HBM 之外，通过稀疏预取实现"看起来像在 HBM 里"的访问体验。

- **痛点：** 长上下文 + 多轮对话场景下，decode KV cache 容量需求远超 HBM 容量（TB 级），现有 offloading 方案 latency 抖动剧烈
- **解法：** OasisKV 提出 **lookahead sparse prefetching**：利用注意力稀疏性，提前从远端内存（DRAM/SSD）预取下一批 token 所需的 KV 子集；同时用 per-head 的稀疏度感知调度，只加载真正会被 attention 命中的 KV block
- **效果：** 在 128K 上下文、Llama-3-70B 上，decode throughput 相比 vLLM 的 block-sparse offloading 提升 **2.3×**，P99 TTFT 仅增加 **12%**
- **意义：** 首次证明 decode KV cache 可以"virtually unlimited"地扩展到 HBM 外而不牺牲 latency SLO，为多轮 agentic 推理打开容量上限

---

### 2. HiSparse — 分层 KV Cache 管理实现稀疏注意力解码无限扩展 (arXiv:2608.07009, 8月7日)
**一句话：** 把 KV cache 分成"热-温-冷"三层，稀疏注意力只在需要时唤醒冷数据。

- **痛点：** 现有稀疏注意力（H2O、SnapKV 等）在 decode 阶段仍需维护完整的 KV cache，长序列下 HBM 依旧爆炸
- **解法：** HiSparse 引入 **Hierarchical KV Cache** —— 按 attention score 分布将 KV 分为三层：Hot（常驻 HBM）、Warm（压缩后 DRAM）、Cold（量化后 SSD/远端）；配合 **Sparse Decode Kernel**，只在注意力计算时按需从下层加载
- **效果：** 在 1M token 上下文上，KV cache 内存占用降低 **87%**，decode 速度比 dense baseline 快 **1.8×**
- **意义：** 让"无限长上下文 decode"从论文概念变成工程可行方案，直接利好长文档 agent 和多轮记忆系统

---

### 3. DistMoE — 无需集中数据的分布式 MoE 隐私训练 (arXiv:2608.09907, 8月10日, Meta)
**一句话：** 多个数据孤岛各自训练专家，一个分布式路由器把它们动态组合——数据不出域，性能不打折。

- **痛点：** MoE 训练通常需要所有数据集中在单一集群，跨组织/跨合规域的联合训练几乎不可能
- **解法：** DistMoE 让每个参与方独立训练**域专属专家**，中央只维护一个轻量级的**分布式路由器**（distributed router）；推理时路由器根据输入动态组合各方专家，训练时通过知识蒸馏对齐路由决策，无需原始数据交换
- **效果：** 在跨 5 个医疗数据集的 MoE 上，DistMoE 达到集中式训练 **96.2%** 的性能，数据零共享
- **意义：** 为医疗、金融等敏感数据场景的 MoE 落地提供了合规路径，也可能改变未来大模型联盟的训练格局

---

### 4. "An Internet for the KV Cache" — 重新思考 LLM 推理时代的基础设施边界 (arXiv:2608.01526, 8月)
**一句话：** KV cache 不该是推理框架的私有数据结构，而应该是像 HTTP 请求一样可被全网路由和缓存的"一等公民"。

- **核心论点：** 当前 KV cache 被锁在单个推理实例内部，导致多轮对话、多模型协作、跨地域部署时大量重复计算；作者主张建立 **KV cache 的通用寻址和传输协议**
- **架构：** 提出类似 CDN 的 **KV Cache Network** —— 全局唯一 token-sequence ID → 分布式 KV store → 标准序列化格式（兼容多种推理框架）→ 基于语义相似度的去重和复用
- **场景：** 多轮对话跨模型切换时直接复用 KV；A/B 测试不同模型时共享公共前缀 KV；跨数据中心推理时预热 KV
- **意义：** 这是从"单机优化"到"网络级优化"的范式跃迁，如果实现将根本性改变 LLM 推理的成本结构

---

### 5. Blink — CPU-Free LLM 推理，把服务栈完全下沉到 GPU + SmartNIC (arXiv:2604.07609, 更新版)
**一句话：** 取消 CPU 这个"中间商"，让 GPU 直接收请求、做推理、发响应。

- **痛点：** 传统 LLM serving 中 CPU 负责 HTTP 解析、请求调度、tokenization、后处理，在高并发下成为瓶颈；CPU-GPU 数据传输 overhead 吃掉 15-30% 的端到端 latency
- **解法：** Blink 将**整个服务栈**（HTTP/2、gRPC、tokenization、调度逻辑）offload 到 GPU kernel 和 SmartNIC/DPU 上运行；GPU 直接通过网络 RDMA 接收原始请求 bytes，在 kernel 内部完成全部 pipeline
- **效果：** 在 70B 模型、batch=32 场景下，端到端 latency 降低 **22%**，throughput 提升 **31%**，CPU 利用率从 85% 降到 **<5%**
- **意义：** 证明了 CPU-free serving 在 LLM 场景的可行性，对云厂商的推理实例设计有直接影响（可以减少甚至取消 CPU 配置）

---

## 💡 其他值得关注

### AcceptMoE — MoE 投机解码的自适应验证 (arXiv:2608.02989, 8月4日, 清华)
- 现有 MoE 投机解码要么验证开销大，要么接受率低。AcceptMoE 根据 expert activation pattern 动态调整 draft 长度和验证阈值，在 Mixtral-8×22B 上达到 **3.1×** 加速，验证接受率 **>85%**

### Moebius — MoE 运行时并行度在线切换 (arXiv:2606.26607, 更新版)
- 训练 MoE 时最优并行策略（TP/EP/PP）随训练阶段动态变化。Moebius 实现**运行时在线切换并行度**，无需 checkpoint/restart，在 1T 参数 MoE 预训练中减少 **19%** 总训练时间

### CXL KV Cache Framework — 多轮对话的混合内存 KV 管理 (arXiv:2607.18141)
- 用 CXL 内存扩展器作为"温层"，DRAM 作为热层，SSD 作为冷层，构建三层 KV cache 分级。在 multi-turn agentic 场景下，跨轮 KV 复用率达到 **94%**，比纯 DRAM 方案成本降低 **4.2×**

---

## 📊 本周趋势观察

| 方向 | 热度 | 关键变化 |
|------|------|----------|
| **KV Cache 分层/扩展** | 🔥🔥🔥 | 从"如何省 KV"进化到"如何无限扩展 KV"——OasisKV、HiSparse、CXL框架三篇齐发 |
| **MoE 训练优化** | 🔥🔥🔥 | DistMoE 解决隐私训练痛点；Moebius 解决并行度切换痛点；Megatron MoE 刷新硬件利用率 |
| **CPU-Free / 全栈下沉** | 🔥🔥 | Blink 代表推理服务栈彻底重构趋势，DPU/SmartNIC 成为新战场 |
| **Agentic RL 基础设施** | 🔥🔥 | 综述文章系统梳理了 agentic RL 训练特有的 infra 挑战（env reset、异步 rollout、安全 sandbox） |

---

## 📁 完整报告

**文件名：** `paperradar/weekly/2026-W37-ai-infra.md`

---

## 🔮 下周预告

W38 → **Deep Learning**

*龙虾小队 · Paper Radar 🦞*
