# 🌍 World Models 周报 · 2026年8月23日 (W35)

> **扫描周期：** 2026-08-16 至 2026-08-23  
> **领域：** World Models（世界模型）  
> **核心趋势：** JEPA路线加速、World Action Model崛起、物理一致性诊断成为刚需

---

## 🔥 Top 5 核心看点

### 1. WorldSimProbe (arXiv:2608.09298, 8月10日) — 世界模型「体检报告」来了

**关键词：** 仿真保真度诊断 · 动作条件世界模型 · 具身操作

这篇工作提出了**WorldSimProbe**，一个专门诊断**动作条件世界模型**中仿真器保真度的框架。核心问题是：当前的世界模型在生成未来帧时，究竟有多忠实于真实物理？作者系统性地评估了世界模型在具身操作任务中的可靠性，发现很多模型在交互动力学方面存在系统性偏差。

**为什么重要：** 世界模型不能只是"看起来对"，还得"物理上对"。这篇为下游策略训练提供了可靠的模型筛选工具。

---

### 2. Diagnosing JEPA World Models (arXiv:2608.12939, 8月13日) — JEPA也开始做"体检"

**关键词：** JEPA · 动作条件预测一致性 · 表征坍塌

LeCun力推的JEPA路线虽然火，但训练稳定性和诊断工具一直缺位。这篇工作提出了一套**动作条件预测一致性**诊断方法，能够检测JEPA世界模型中的表征质量问题。值得注意的是，这篇直接引用了LeWorldModel作为基准架构。

**为什么重要：** JEPA从"能不能训"进入"训得好不好"阶段，诊断工具的出现意味着这个方向正在成熟。

---

### 3. A Definition and Roadmap for World Models (arXiv:2607.06401, 7月7日) — 终于有人给世界模型下定义了

**关键词：** 定义框架 · 路线图 · 跨社区对齐

世界模型这个词被用得太泛了——RL社区、视频生成社区、具身智能社区各说各话。这篇综述试图**统一定义**，并提出了一条清晰的roadmap：从"被动预测"到"主动交互"，从"像素空间"到" latent 空间"，从"单模态"到"全模态"。

**关键观点：**
- 世界模型 ≠ 视频生成模型（虽然overlap很大）
- 真正的世界模型需要支持**反事实推理**和**动作条件预测**
- 当前最大瓶颈：缺乏统一的评估标准和物理一致性保证

---

### 4. From World Models to World Action Models (arXiv:2607.00836, 7月1日) — WAM 正在成为新范式

**关键词：** World Action Model · VLA融合 · 端到端决策

这篇明确提出了 **World Action Model (WAM)** 的概念：不只是预测世界怎么变，而是直接输出"在这种世界状态下该做什么"。这是世界模型从"仿真器"向"决策器"进化的关键一步。文中讨论了如何将世界模型与VLA（Vision-Language-Action）模型统一。

**产业映射：**
- 小鹏 X-World、华为 WEWA 2.0 都是这个方向的工程落地
- Physical Intelligence的π0.7、π0.5也在走WAM路线

---

### 5. LeWorldModel 持续发酵 (arXiv:2603.19312) — LeCun路线的"稳定版"来了

**关键词：** JEPA · 端到端稳定训练 · 单GPU可训

LeWorldModel自3月发布以来已被引用**147次**。核心突破：
- 第一个能**端到端稳定训练**的JEPA世界模型（从raw pixels）
- 仅需**两个loss项**（预测loss + Gaussian正则），不需要EMA teacher、不需要多term loss
- ~15M参数，**单GPU几小时**即可训练
- 规划速度比基础模型世界模型快 **48x**

后续工作层出不穷：
- **Causal-JEPA** (ICML 2026) — 通过object-level latent intervention学习因果世界模型
- **SIGReg理论** (arXiv:2607.13612, 7月15日) — 从变分自由能角度解释JEPA目标函数
- **Equilibrium World Models** (arXiv:2606.23463) — 将JEPA应用于经济学异质主体模型

---

## 📊 产业动态

### 🚗 自动驾驶世界模型军备竞赛

| 厂商 | 产品 | 技术路线 | 关键创新 |
|------|------|----------|----------|
| **NVIDIA** | Cosmos 3 + OmniDreams | Omnimodal World Models | 实时闭环仿真，支持Physical AI全链路 |
| **小鹏** | X-World | 基于WAN 2.2的DiT backbone | 视角-时间自注意力，七路环视摄像头几何一致性 |
| **华为** | 乾崑ADS 5 + WEWA 2.0 | 云端World Engine + 车端World Action Model | 博弈论训练效率提升10倍，碰撞风险降低50% |
| **AGIBOT** | Genie Sim 3.0 | LLM驱动的高保真仿真 | 基于NVIDIA Isaac Sim，自然语言驱动场景生成 |

**关键数据：** 华为云端算力已达 **60 EFLOPS**，较2023年提升21倍。

---

## 📑 其他重要论文速览

### 基础架构

- **Cosmos 3: Omnimodal World Models for Physical AI** (NVIDIA, arXiv:2606.02800)  
  NVIDIA世界模型平台第三代，支持全模态物理AI。Cosmos生态已覆盖视频生成、闭环仿真、机器人训练全链路。

- **NVIDIA OmniDreams** (arXiv:2606.03159)  
  实时生成式世界模型，用于自动驾驶闭环仿真。

- **PhyWorld: Physics-Faithful World Model for Video Generation** (arXiv:2605.19242)  
  研究视频生成模型作为Physical AI世界模拟器的物理忠实度。

### 自动驾驶专用

- **DriveVLA-W0** (ICLR 2026, arXiv:2510.12796) — 世界模型放大自动驾驶数据Scaling Law  
- **DeltaWorld** (CVPR 2026) — "一帧一Token"的高效生成世界建模  
- **DriveDreamer-Policy** (arXiv:2606.04xxx) — 几何 grounded 的世界-动作统一模型  
- **LMGenDrive** (arXiv:2606.04xxx) — 多模态理解与生成世界建模的端到端驾驶

### 机器人学习

- **DynaWM** (arXiv:2607.02604) — 基于Base-VLA引导的动态物体操作世界基础模型  
- **VLA-JEPA** (arXiv:2602.10098) — 用潜在世界模型增强VLA  
- **World-gymnast** (arXiv:2602.02454) — 在世界模型中用RL训练机器人  
- **Reinforcing VLAs in Task-Agnostic World Models** (arXiv:2605.12334) — 任务无关世界模型中的VLA强化

### 评测与基准

- **WorldModelBench** (NeurIPS 2026) — 将视频生成模型作为世界模型来评判  
- **RoboWM-Bench** (arXiv:2604.19092) — 机器人操作世界模型评测  
- **RoboTrustBench** (arXiv:2606.01600) — 机器人操作视频世界模型的可信度评测  
- **PhyGround** (arXiv:2605.xxxxx) — 生成世界模型的物理推理基准  
- **3D and 4D World Modeling: A Survey** (arXiv:2509.07996v4, 7月20日更新) — 全面综述

---

## 💡 本周洞察

### 1. JEPA路线正在"出圈"
LeWorldModel证明了JEPA可以稳定端到端训练后，这个方向的研究爆发式增长。从纯控制任务扩展到经济学（Equilibrium World Models）、医疗（ECG-WM）、甚至无线通信（Composable World Models）。SIGReg的理论解释也为JEPA提供了更扎实的数学基础。

### 2. World Action Model是下一个战场
世界模型不再满足于"预测未来"，而是要直接参与决策。小鹏X-World叫自己"VLA 2.0的云端矩阵"，华为把车端模型叫WA (World Action Model)，Physical Intelligence的π系列也是WAM路线。这个命名统一化的趋势说明产业界正在凝聚共识。

### 3. 物理一致性从"加分项"变成"必选项"
WorldSimProbe、PhyGround、RoboTrustBench等一批评测工具的出现，标志着世界模型领域从"能生成视频"进入"生成的东西物理上合理"的阶段。这对自动驾驶和机器人等安全关键应用尤其重要。

### 4. NVIDIA Cosmos生态的护城河在加深
Cosmos 3 + OmniDreams + FastGen + GR00T N1，NVIDIA正在构建从世界模型生成到机器人策略训练的完整闭环。开源世界模型社区（如Robbyant Team的advancing open-source world models）虽然在追赶，但在算力和数据规模上差距明显。

---

## 📅 下周预告

W36 → **Embodied Intelligence**（具身智能）

重点关注：human-data-training、跨本体学习、触觉感知、VLA新架构

---

*龙虾小队 · Paper Radar 🦞*
