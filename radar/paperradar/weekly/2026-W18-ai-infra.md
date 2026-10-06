## 🦞 论文雷达周报 | 2026-W18 | AI Infra

> 📊 本周扫描: arXiv cs.DC / cs.OS / cs.LG / cs.AI  
> 🔍 关键词: AI infrastructure, distributed training, LLM inference, GPU scheduling, KV cache, model serving  
> 📅 时间窗口: 2026-04-12 ~ 2026-04-26  
> 📄 共命中 30+ 篇，初筛后 **6 篇**值得关注

---

## 📌 必读推荐

### 1. "Optimal Scheduling Algorithms for LLM Inference"
- 作者: Yueying Li, Jim Dai, Tianyi Peng | 年份: 2025 | 来源: arXiv
- **核心贡献**: 从排队论角度建立LLM推理调度的严格理论框架，提出SLAI调度器——动态平衡prefill/decode阶段，在严格TBT延迟约束下实现吞吐量最优；高负载下TTFT降低53%，服务容量提升26%
- **一句话**: 用数学证明了work-conserving scheduler的吞吐量最优性，并给出工程上可落地的SLAI实现，解决了vLLM/Sarathi-Serve在异构SLO场景下的调度盲区
- [arXiv](https://arxiv.org/abs/2504.07347) | ⭐⭐⭐⭐⭐ | #调度理论 #LLM推理 #SLO保证 #排队论
- 💡 **为什么必读**: AI Infra的"根论文"级工作——把LLM推理调度从经验工程推进到理论可证的阶段

### 2. "Distributed Hybrid Parallelism for Large Language Models"
- 作者: 多篇综述整合 | 年份: 2026 | 来源: arXiv
- **核心贡献**: 系统梳理分布式LLM训练/推理的混合并行策略——数据并行(DP)、张量并行(TP)、流水线并行(PP)、序列并行(SP)、专家并行(EP)，给出每种策略的通信模式、内存占用和适用场景的数学建模
- **一句话**: 一份可以当"设计手册"用的分布式并行策略全景图，从Megatron-LM到DeepSeek的DualPipe都有覆盖
- [arXiv](https://arxiv.org/abs/2602.09109) | ⭐⭐⭐⭐⭐ | #分布式训练 #并行策略 #综述 #LLM
- 💡 **为什么必读**: 想做分布式训练infra的人，这篇是地图级参考

---

## 🔥 本周新论文速览

### 3. "NVIDIA Dynamo: A Low-Latency Distributed Inference Framework"
- 来源: NVIDIA Technical Blog, 2025
- **核心贡献**: NVIDIA开源的分布式推理框架，核心特性包括：disaggregated inference（prefill/decode分离）、smart routing（KV cache感知）、MoE专家并行调度
- **一句话**: NVIDIA亲自下场做推理框架了，对标vLLM/SGLang，主打低延迟+高吞吐，兼容K8s
- [Blog](https://developer.nvidia.com/blog) | ⭐⭐⭐⭐ | #推理框架 #NVIDIA #分布式推理
- 💡 **为什么值得关注**: 大厂infra战略的风向标，Dynamo可能成为下一代推理服务的事实标准

### 4. "llm-d: Distributed Inference with Disaggregated Prefill/Decode"
- 来源: Red Hat / Kubernetes社区, 2025-11
- **核心贡献**: 在K8s上实现LLM分布式推理的"well-lit paths"——prefill/decode分离、KV cache前缀复用、MoE跨节点调度，允许prefill跑CPU/decode跑GPU的异构部署
- **一句话**: 云原生+LLM推理的标准答案正在形成，llm-d可能是K8s生态的推理基础设施基石
- [Article](https://developers.redhat.com/articles/2025/11/21/introduction-distributed-inference-llm-d) | ⭐⭐⭐⭐ | #云原生 #K8s #推理分离
- 💡 **为什么值得关注**: 推理infra的"云原生化"趋势——从单机优化走向集群级调度

### 5. "CacheGen: KV Cache Compression and Streaming for Fast LLM Serving"
- 作者: Yuhan Liu et al. | 年份: 2024 | 来源: arXiv
- **核心贡献**: 提出KV Cache的压缩+流式传输方案，将KV tensor压缩后按需流式加载，大幅降低多轮对话和多副本部署的内存压力
- **一句话**: KV Cache是LLM推理的内存瓶颈，CacheGen用压缩+流式来解决，和vLLM的PagedAttention互补
- [arXiv](https://arxiv.org/abs/2310.07240) | ⭐⭐⭐⭐ | #KVCache #压缩 #推理优化
- 💡 **为什么值得关注**: KV Cache管理是推理infra的核心子问题，这篇和vLLM、SGLang、FlashInfer共同构成技术栈

### 6. "A Comprehensive Survey on Distributed Deep Learning Training"
- 年份: 2025-12 | 来源: Preprints.org
- **核心贡献**: 四大维度综述——并行策略(DP/MP/PP/EP)、框架(PyTorch FSDP/Megatron/DeepSpeed)、网络互联(RDMA/NVLink/InfiniBand)、推理优化(vLLM/Orca/Speculative Decoding)
- **一句话**: 分布式训练infra的"百科全书"，从算法到硬件全覆盖
- [Preprints](https://www.preprints.org/manuscript/202512.2207) | ⭐⭐⭐⭐ | #综述 #分布式训练 #全景图
- 💡 **为什么值得关注**: 快速建立AI Infra领域地图的首选入口

---

## 📊 本周趋势洞察

| 趋势 | 证据 |
|------|------|
| **推理调度走向理论化** | Li et al. 用排队论证明吞吐量最优，SLAI成为首个有严格SLO保证的调度器 |
| **Prefill/Decode分离成为共识** | NVIDIA Dynamo + llm-d + 多篇论文同时推进，推理架构正在重构 |
| **KV Cache是兵家必争之地** | PagedAttention(vLLM) → RadixTree(SGLang) → Compression(CacheGen) → Streaming，技术栈快速迭代 |
| **云原生推理基础设施成型** | llm-d代表K8s生态的标准化尝试，推理从"跑起来"走向"规模化部署" |
| **分布式并行策略进入"混合"时代** | 单一并行策略不够用了，DP+TP+PP+EP的组合设计成为标配 |

---

## 🗺️ AI Infra 领域地图（速查）

```
AI Infra
├── 训练层
│   ├── 分布式并行: DP / TP / PP / SP / EP
│   ├── 训练框架: PyTorch FSDP / Megatron-LM / DeepSpeed / Colossal-AI
│   └── 通信优化: NCCL / RDMA / NVLink / InfiniBand
├── 推理层
│   ├── 推理引擎: vLLM / SGLang / TensorRT-LLM / NVIDIA Dynamo
│   ├── 调度策略: FCFS / SARATHI / SLAI(新) / Continuous Batching
│   ├── KV Cache: PagedAttention / RadixTree / CacheGen / FlashInfer
│   └── 解码加速: Speculative Decoding / Medusa / Lookahead
├── 集群管理层
│   ├── GPU调度: Kubernetes + GPU Operator / Volcano / YARN
│   ├── 弹性伸缩: 自动扩缩容 / Spot Instance / 检查点恢复
│   └── 异构部署: CPU prefill + GPU decode / 边缘推理
└── 存储与网络
    ├── 模型存储: Model Registry / 分层存储 / 增量加载
    └── 高速互联: NVLink Switch / InfiniBand / RoCE
```

---

## 💬 队长操作指南

**回复我来做这些事**:
- `精读1` — 把论文1加入"精读列表"，单独做完整阅读卡片
- `精读2` — 把论文2加入"精读列表"
- `不感兴趣3` — 把论文3标记为不感兴趣，后续降低权重
- `加关键词 XXXX` — 新增AI Infra细分方向的扫描关键词
- `换领域` — 切换到深度学习 / 物理模型 / 世界模型扫描
- `推送到飞书` — 把本周报告推送到飞书

---

> 🦞 龙虾小队 · 论文雷达 · 每周一更  
> 存储位置: `~/paperradar/weekly/2026-W18-ai-infra.md`  
> 下次推送: 2026-05-03 (约) | 预计领域: 深度学习  
> **定时任务状态**: 已配置每周日自动扫描（轮询4领域）
