# AI Infra Weekly Report | 2026-W22

> **Scan Date:** 2026-05-31  
> **Field:** AI Infrastructure  
> **Source:** arXiv + Community Highlights

---

## 🔥 Top 5 本周最值得关注

### 1. PALS: Power-Aware LLM Serving for Mixture-of-Experts Models
**arXiv:2605.21427 | May 2026**

**核心贡献：** 首次将功率预算作为MoE模型推理的**一级调度维度**，而非固定约束。

- **背景：** 传统推理系统（Orca, vLLM, DistServe）都把GPU功率当作不可变的硬件常量，而数据中心GPU功率其实可以通过RAPL/PPB等机制动态调整。
- **关键洞察：** 不同并行策略（TP/PP/EP）对功率-性能曲线的影响差异巨大。比如expert parallelism在通信密集时，降低功率到通信刚好饱和的阈值，反而能节省功耗而不损失吞吐量。
- **方法：** PA-vLLM在vLLM基础上引入动态功率封盖（power capping），通过轻量分析器预测不同功率级别下的吞吐量，实现Pareto最优。
- **评估：** 在DeepSeek-V3规模的MoE上，功率节省30%+同时保持吞吐量损失<5%。

**[TL;DR]** 把功率管理从"硬件黑盒"变成"可调调度参数"——数据中心省钱利器，对MoE模型尤其有效。

---

### 2. LeMix: Unified Scheduling for LLM Training and Inference on Multi-GPU Systems
**arXiv:2507.21276 | RTSS 2025**

**核心贡献：** 让推理和训练**共享同一批GPU**，彻底消灭"训练时推理闲置、推理时训练排队"的资源浪费。

- **背景：** 实际部署中，LLM推理服务和持续训练通常是分离的——推理集群在训练窗口期大量空闲，训练完成后的推理加载又延迟。
- **方法：** 离线性能剖析 + 执行预测 + 运行时调度三位一体。关键是对"co-execution interference"（共执行干扰）的建模——预填充和训练微批次之间的资源抢占。
- **结果：** 吞吐量提升**3.53x**，推理损失降低0.61x，SLO达成率提高2.12x。

**[TL;DR]** 第一个系统级解决"训练推理能不能共享GPU"的务实方案——对资源紧张的小团队意义重大。

---

### 3. Nexus: Proactive Intra-GPU Disaggregation of Prefill and Decode
**arXiv:2507.06608 | May 2025**

**核心贡献：** 在**单个GPU内部**实现预填充/解码的主动分离，无需跨GPU、无需高端互联。

- **背景：** 预填充（compute-bound）和decode（memory-bound）的干扰是vLLM核心痛点。DistServe、MoonCake等方案需要跨GPU或跨节点，依赖NVLink/InfiniBand。
- **核心创新：** 在单GPU内部通过工作窃取（work stealing）和调度重排，在SM（Streaming Multiprocessor）级别实现预填充和decode的时空复用。
- **结果：** 在双GPU L20上，相对Sarathi-Serve和DistServe，TTFT和TPOT都实现显著降低。

**[TL;DR]** 让单GPU/廉价GPU也能体验"预解码分离"——降低入门门槛，对消费级和边缘部署意义重大。

---

### 4. TyphoonMLA: A Mixed Naive-Absorb MLA Kernel for Shared Prefix
**arXiv:2509.21081 | Mar 2025**

**核心贡献：** DeepSeek-V3的MLA（Multi-head Latent Attention）的**共享前缀优化内核**，实现吸收模式和非压缩模式的混合调度。

- **背景：** DeepSeek-V3的MLA在吸收模式下虽然省内存，但系统提示（shared prefix）的KV缓存因为压缩后共享变得不可行。
- **方法：** 对共享前缀部分使用非压缩的"naive"模式存储，非共享部分使用吸收模式。内核层面根据prefix和非prefix的动态切换。
- **开销：** 在4K-32K batch、32K-256K序列长度场景下，HBM开销仅增加约**3%**。

**[TL;DR]** 为DeepSeek-V3/其他MLA模型解决了系统提示共享的内存死结——3%开销换prefix reuse能力，ROI极高。

---

### 5. InfiniLoRA: Disaggregated Multi-LoRA Serving for Large Language Models
**arXiv:2604.07173 | Apr 2026**

**核心贡献：** 多LoRA服务的**分离式架构**——每个LoRA独占一个轻量推理实例，共享底层基座模型的预填充阶段。

- **背景：** LoRA适配器让同一基座模型服务多个任务成为可能，但现有方案（如vLLM multi-LoRA）将所有LoRA放在同一实例，导致调度复杂度高、内存争抢严重。
- **方法：** 将预填充（prefill）集中化处理（共享基座模型权重），decode阶段把请求路由到对应LoRA的专用实例。LoRA适配器作为轻量参数层，在推理中动态加载。
- **好处：** 每个LoRA实例不需要完整加载基座模型，只加载LoRA权重 + 共享基座KV cache，大幅降低每个LoRA的内存占用。

**[TL;DR]** 从"多LoRA挤在一台机器"进化到"每个LoRA一个小容器"——SaaS多租户场景的关键基础设施。

---

## 📌 其他值得关注的论文

### FineServe: Precision-Aware KV Slab and Two-Level Scheduling for Heterogeneous Precision LLM Serving
**arXiv:2509.06261**

- 混合精度（FP16/INT8/INT4）共部署时，不同模型的KV块大小不同导致内存碎片化。
- 提出Precision-aware KV Slab分配器 + 两级调度，让精度不同的模型共享同一GPU的KV池。

### Frontier: A High-Fidelity Simulator for Emerging LLM Inference Architectures
**arXiv:2508.03148**

- 专为disaggregated和MoE推理架构设计的仿真器。
- 可以在不消耗实际GPU的情况下，对MoonCake、DistServe等架构做大规模设计空间探索。

### ModServe: Modality- and Stage-Aware Resource Disaggregation for Multimodal Model Serving
**arXiv:2502.00937**

- 多模态模型（VLM）服务：视觉encoder和语言decoder的分离式调度。
- 不同模态对内存/计算需求差异巨大，统一调度反而低效。

### DeepStack: Scalable and Accurate Design Space Exploration for Distributed 3D-Stacked AI Accelerators
**arXiv:2604.04750**

- 3D堆叠DRAM + 推理的co-design分析框架。
- 对wafer-scale 3.5D系统（多个3D stack通过interposer连接）的并行策略和通信模式优化。

### Oneiros: KV Cache Optimization through Parameter Remapping for Multi-tenant LLM Serving
**arXiv:2507.11507**

- 多租户场景下，通过KV缓存的参数重映射（parameter remapping）来优化内存布局。
- 与Pie（CPU内存池）和LServe（长序列稀疏注意力）等最新工作形成互补。

---

## 🗞️ 社区/工业动态

- **vLLM vs SGLang 2026 H1 Benchmark更新**：H100上SGLang在7B-8B模型上吞吐量比vLLM高~29%，但70B+模型差距缩小到3-5%。SGLang的RadixAttention在RAG/多轮对话场景优势明显，vLLM的硬件兼容性更广（支持TPU/Trainium）。
- **SuffixDecoding（NeurIPS 2025 Spotlight）**已合并入vLLM v1引擎，通过后缀树实现无draft model的投机解码。Snowflake ArcticInference团队持续推动生产级落地。

---

## 📅 轮换进度

World Models ✅ → **AI Infra ✅（本周 W22）** → Deep Learning 📅（下周 W23）

---

*龙虾小队 · Paper Radar 🦞*
