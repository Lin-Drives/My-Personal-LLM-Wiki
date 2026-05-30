# 🌍 World Models 周报 — 2026-W21

> **扫描时间：** 2026-05-24 (W21)
> **扫描领域：** World Models / 世界模型
> **覆盖范围：** arXiv + 社区热点，重点聚焦 2026 年 4-5 月新发表工作

---

## 🔥 本周 Top 5 最值得关注的论文

### 1. Demo-JEPA — 跨具身模仿的 One-shot 利器
- **论文：** *Demo-JEPA: Joint-Embedding Predictive Architecture for One-shot Cross-Embodiment Imitation* (arXiv:2605.20811, May 21 2026)
- **核心：** 将跨具身模仿问题建模为**隐空间目标条件规划**。给定源演示视频和目标当前观测，Dreamer Predictor 先推断出一个具身兼容的隐式目标，然后在动作条件化的世界模型中通过 CEM 优化完成 latent planning。
- **底层模型：** 采用 VJEPA2.1 作为动作条件化世界模型 backbone。
- **看点：** One-shot 跨具身迁移 —— 这是 JEPA 架构在机器人控制中的又一次能力扩展，从表征学习走向实际策略生成。

### 2. World Model for Robot Learning — 最全面的综述
- **论文：** *World Model for Robot Learning: A Comprehensive Survey* (arXiv:2605.00080, Apr 30 2026)
- **核心：** 首次对世界模型在机器人学习中的角色做了**全景式系统分类**，提出三大核心能力框架：
  - **Foresight（预见）：** 未来状态预测
  - **Imagination（想象）：** 内部模拟与策略优化
  - **Simulation（仿真）：** 作为 RL / 模仿学习的可交互环境
- **覆盖：** 从 JEPA 到 World Action Models (WAM)，从 VLA 内嵌 world model 到纯仿真器，应有尽有。
- **看点：** 想快速了解这个领域全貌？这篇是目前的最佳入口。

### 3. World-Ego Modeling — 长程混合具身任务的新思路
- **论文：** *World-Ego Modeling for Long-Horizon Evolution in Hybrid Embodied Tasks* (arXiv:2605.19957, May 19 2026)
- **核心：** 提出 World-Ego 双视角建模 —— **World-view** 负责环境全局演化，**Ego-view** 负责第一人称行为理解。两者协同解决长程时序任务中的身份漂移和视角混乱问题。
- **看点：** 针对长程任务中的"我是谁我在哪"问题给出了架构级解法，在 VLN 和具身推理任务中有显著优势。

### 4. What Drives Success in Physical Planning with JEPA-WMs — JEPA 世界模型的配方书
- **论文：** *What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?* (arXiv:2512.24497v3, May 2026)
- **核心：** 系统性拆解 JEPA-World Model 在物理规划任务中成功的关键设计选择，覆盖：
  - Predictor 架构（feature conditioning vs sequence conditioning vs AdaLN）
  - 编码器冻结 vs 端到端训练
  - Latent space 维度与规划步长
- **发现：** RoPE + sequence conditioning 在大多数任务上表现最稳健；AdaLN 能防止动作信息在深层网络中消失。
- **看点：** 这不是一篇新算法论文，而是一份**工程配方书** —— 如果你在做 JEPA 机器人规划，这篇能帮你少踩很多坑。

### 5. MoLA — 混合隐式动作的世界动作模型
- **论文：** *From Imagined Futures to Executable Actions: Mixture of Latent Actions for Robot Manipulation* (arXiv:2605.12167, May 12 2026)
- **核心：** 提出 Mixture of Latent Actions (MoLA)，在世界动作模型（WAM）中引入**多个预训练逆动力学模型（IDM）作为隐动作接口**，桥接想象的未来视频与可执行动作。
- **看点：** 解决 WAM "想得好看但做不出来"的问题，用 mixture 机制增强动作解码的灵活性。

---

## 📊 领域动态与趋势

### 🔹 World Action Models (WAM) 成为新范式
2026 年 Q1-Q2 最明确的趋势：从"预测世界的模型"走向"**同时预测世界和动作的模型**"。代表工作：
- **DreamZero** (NVIDIA, arXiv:2602.15922): 14B 自回归扩散 Transformer，联合生成未来视频 + 动作，零样本策略能力惊人
- **Fast-WAM** (arXiv:2603.16666): 将推理与动作执行解耦，实现 7Hz 实时闭环控制
- **Cosmos Policy** (NVIDIA/Stanford, arXiv:2601.16163): 在 Cosmos 视频模型基础上后训练，LIBERO 98.5%
- **WoVR** (arXiv:2602.13977): 用世界模型作为 VLA 后训练的可靠仿真器

核心转变：动作学习从"密集状态-动作模仿"转向"**逆动力学对齐**" —— 让电机指令与预测的视觉未来对齐。

### 🔹 JEPA 生态持续扩张
LeCun 的 JEPA 路线在 2026 年全面开花：
- **V-JEPA 2.1** (Mar 2026): 密集预测表示学习，支持图像/视频 token 级任务
- **VLA-JEPA** (arXiv:2602.10098): 将 JEPA 世界模型注入 VLA，无泄漏地 grounding 动作相关动态
- **Demo-JEPA** (May 2026): 跨具身 one-shot 模仿
- **ThinkJEPA** (Mar 2026): 扩展语义推理路径，支持长程分层规划
- **EB-JEPA** (arXiv:2602.03604): 能量化 JEPA 库，解决特征坍塌
- **LeWorldModel** / **LeJEPA** (Mar 2026): 单 GPU 端到端训练，效率大幅提升

JEPA 正在从"自监督表征学习工具"进化为"**机器人控制的默认 backbone**"。

### 🔹 因果性与对象级建模升温
- **Causal-JEPA** (用户此前精读过的): 对象级潜在干预，因果感知的 JEPA
- **STICA** (arXiv:2511.14262, revised Mar 2026): Slot Transformer + 因果感知策略，对象级 token 预测
- **Latent State Design for World Models** (arXiv:2605.01694): 提出"压缩光谱"框架，从重建型到因果/反事实型世界模型的完整谱系

方向判断：**因果推理**正在成为世界模型从"预测相关"走向"理解机制"的关键分水岭。

### 🔹 综述与基准爆发
- **Human Cognition in Machines** (arXiv:2604.16592): 从人类认知角度统一审视世界模型，涵盖记忆、感知、语言、推理、想象、动机、元认知七大维度
- **World Reasoning Arena** (arXiv:2603.25887): 世界模型推理基准，暴露与人类水平假设推理之间的巨大差距
- **World Model for Robot Learning 综述** (如上): 领域全景图

这表明领域进入**系统化整理期** —— 从野蛮生长转向架构收敛。

---

## 🎯 其他值得关注的工作

| 论文 | 机构/时间 | 一句话总结 |
|------|----------|-----------|
| **Human-in-the-World-Model** (arXiv:2604.21741) | May 2026 | 人在回路 + 世界模型后训练，用人类干预作为隐式反馈信号 |
| **GNWM** (arXiv:2604.16585) | Apr 2026 | 全局神经世界模型，通过 2D 网格拓扑量化实现自稳定，不需要像素重建 |
| **World Guidance** (arXiv:2602.22010) | 2026 | 在条件空间中进行世界建模来生成动作 |
| **DriveVLA-W₀** (ICLR 2026) | 2026 | 世界模型放大自动驾驶中的数据 scaling law |
| **Vid2World** (ICLR 2026) | 2026 | 将视频扩散模型改造为可交互世界模型 |
| **WoVR** (arXiv:2602.13977) | Feb 2026 | 用世界模型作为 VLA 策略的可靠仿真器进行 RL 后训练 |
| **BagelVLA** (arXiv:2602.09849) | Feb 2026 | 交错视觉-语言-动作生成，增强长程操作能力 |
| **FRAPPE** (arXiv:2602.17259) | Feb 2026 | 通过多未来表征对齐将世界建模注入通用策略 |
| **Akasha 2** (arXiv:2601.06212) | Jan 2026 | 哈密顿状态空间对偶 + VL-JEPA，<50ms 移动端推理 |

---

## 📅 轮换进度

| 周次 | 领域 | 状态 |
|------|------|------|
| W17 | World Models | ✅ |
| W18 | AI Infra | ✅ |
| W19 | Deep Learning | ✅ |
| W20 | Physics-informed AI | ✅ |
| **W21** | **World Models** | **✅（本周）** |
| W22 | AI Infra | 📅（下周） |

> 轮换配置已更新，`current_index` 推进至 3，下周将扫描 **AI Infra**。

---

*龙虾小队 · Paper Radar 🦞*
