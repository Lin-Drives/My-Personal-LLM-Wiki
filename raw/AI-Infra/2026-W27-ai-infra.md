# AI Infra Weekly Report — W27 (2026-06-22 ~ 2026-06-28)

> **Scan Field:** AI Infra  
> **Week:** W27  
> **Generated:** 2026-06-28  
> **Status:** Manual补跑（原定weekly cron在09:17执行超时，已定位原因）

---

## 🔥 本周 Top 5 核心看点

### 1. VeriCache — 把 Lossy KV Cache 变成 Lossless LLM Inference

- **arXiv:** 2605.17613  
- **日期:** 2026-05-17  
- **核心突破：** 提出一种**验证机制**，让 KV Cache 可以先 aggressive 压缩（lossy），然后在推理阶段通过 lightweight verification 恢复无损输出。换句话说，**内存省了，但输出质量不打折**。这是 KV Cache 优化从"近似够用"走向"严格无损"的关键一步。
- **Why it matters:** 长上下文 + 大 batch 场景下的 KV Cache 内存瓶颈是 2026 年 serving 系统的头号痛点。VeriCache 提供了一条新路径：不是靠更精细的量化算法，而是靠"先压后验"的架构思路。

---

### 2. SAGA — Workflow-Atomic Scheduling for AI Agent Inference

- **arXiv:** 2605.00528  
- **日期:** 2026-05  
- **核心突破：** 针对 AI Agent 多步骤推理（tool call → 等待 → 再推理）的**间歇性执行特征**，提出"工作流原子调度"——把 agent 的整个推理链条作为一个原子单元调度，而不是按单个 token generation 切片。显著降低上下文切换和 KV Cache 反复加载的开销。
- **Why it matters:** Agentic AI 的 serving 和传统 chat completion 完全不同。SAGA 是第一个把"agent workflow"作为一级调度对象的系统，预示 2026 下半年会有更多 agent-native serving infra 出现。

---

### 3. PithTrain — Compact and Agent-Native MoE Training System

- **arXiv:** 2605.31463  
- **日期:** 2026-05  
- **核心突破：** 一个专为 Agent 场景设计的**紧凑型 MoE 训练系统**。强调"agent-native"——不是把通用 MoE 模型拿来给 agent 用，而是从训练目标、数据混合策略、router design 三个层面重新设计。
- **Why it matters:** MoE 在 2026 年已经是标配，但"通用 MoE"和"Agent MoE"的 gap 越来越大。PithTrain 代表了从 infra 层开始为 agent 定制模型的趋势。

---

### 4. DiP-SD — Distributed Pipelined Speculative Decoding for Edge Multi-User

- **arXiv:** 2604.20919  
- **日期:** 2026-04-22  
- **核心突破：** 把**投机解码**扩展到边缘多用户场景。设备本地生成 draft tokens，offload 到云端验证。通过流水线并行隐藏网络延迟。
- **Why it matters:** 2026 年投机解码（EAGLE-3、MTP、Medusa）已经是 serving 标配，但主要集中在数据中心单集群。DiP-SD 把这条技术路线延伸到 edge-cloud 协作，对端侧推理生态意义重大。

---

### 5. WiSP — Routing-Aware Paging for Low-Resource MoE Serving

- **arXiv:** 2606.21868v1  
- **日期:** 2026-06  
- **核心突破：** 针对 MoE 模型的**路由感知分页机制**。传统 paging 对 MoE 的 expert activation pattern 不敏感，WiSP 让内存管理器感知 router 的决策，把即将被激活的 expert 提前换入，减少 decode 阶段的 page fault。
- **Why it matters:** MoE serving 的内存效率一直是暗坑。WiSP 是少有的从"router 语义"切入做内存管理的论文，思路很刁钻。

---

## 📊 其他值得关注的论文

| 论文 | arXiv | 核心看点 |
|------|-------|----------|
| **WAIT** — Fluid-Guided Online Scheduling | 2504.11320v4 | 把流体力学直觉引入 LLM 推理调度，用"流体密度"类比 request batch 的内存压力 |
| **Apt-Serve** — Adaptive Request Scheduling on Hybrid Cache | 2504.07494 | 混合缓存（DRAM + SSD + 远端）上的自适应请求调度，针对分层存储的 serving 场景 |
| **TurboQuant** — 3-bit KV Cache Quantization | 2504.19874 (ICLR 2026) | PolarQuant + QJL 组合，3-bit KV cache 零精度损失，H100 上 8x attention 加速 |
| **AIConfigurator** — 集群级配置空间搜索 | 2601.06288 | 把超参数配置建模为搜索问题，自动优化分布式训练集群配置 |

---

## 🎯 领域趋势判断

1. **Agent-Native Infra 成新主线：** SAGA、PithTrain 两篇文章都指向同一个趋势——2026 下半年 infra 层的创新会从"通用 LLM serving"转向"Agent 专用 serving"。Agent 的间歇性执行、多 tool 调用、长上下文往返等特征，对传统 continuous batching 假设构成根本挑战。

2. **KV Cache 进入"后量化时代"：** VeriCache、TurboQuant、WiSP 三条路线并行——lossy→lossless 的验证架构、极限低 bit 量化、router-aware 内存管理。KV Cache 不再只是"压缩一下"，而是成为系统设计的核心对象。

3. **投机解码从数据中心走向边缘：** DiP-SD 代表了投机解码的扩散。2026 年 EAGLE-3 在 vLLM/SGLang 中已经 production-ready，下一步是边缘化和异构化。

---

## 📅 轮换进度

**AI Infra ✅（本周 W27）** → Deep Learning 📅（下周 W28） → Physics-informed AI 📅 → World Models 📅 → Embodied Intelligence 📅

---

*龙虾小队 · Paper Radar 🦞*  
*Generated manually after cron timeout. Original cron failure: `cron: job execution timed out` at 2026-06-28 09:17.*
