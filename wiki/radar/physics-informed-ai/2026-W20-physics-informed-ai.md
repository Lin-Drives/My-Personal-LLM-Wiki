# 🧬 论文雷达周报 · Physics-informed AI · 2026-W20

> 扫描时间：2026-05-17 | 领域轮换：Deep Learning ✅ → **Physics-informed AI** ✅（本周）→ World Models 📅（下周 W21）

---

## 🔥 本周最值得关注的 3 篇论文

### 1. K-PINN: Lattice-Boltzmann-Driven Physics-Informed Neural Networks
**arXiv:2604.03481** | 2026-04-03

**一句话：** 把介观尺度的 Lattice-Boltzmann 方程直接嵌入 PINN，突破了传统 PINN 只能处理宏观连续方程的限制。

**核心亮点：**
- 在介观动力学层面保持物理一致性，质量守恒误差 < 1.5%
- 成功建模接触钉扎、各向异性铺展、毛细滞后等复杂液滴现象
- U-Net 编码器-解码器结构使误差相比传统神经网络降低 50-75%
- 收敛后实时预测速度 > 10⁴ 次/秒

**为什么重要：** 这是 PINN 从"宏观唯象"走向"介观机理"的关键一步，对多相流、润湿性工程有直接影响。

---

### 2. Solver-in-the-Loop DeepONets
**ICLR 2026 (OpenReview)**

**一句话：** 把传统数值求解器直接放进训练循环，训练速度提升两个数量级，同时保持与 PI-DeepONet 相当的精度。

**核心亮点：**
- 避免自动微分计算 PDE 残差的巨大开销
- 用经典求解器的离散监督信号替代纯物理约束
- 在 Burger's 方程实验上验证有效
- 可扩展到高维 PDE（如 Navier-Stokes）

**为什么重要：** 这可能是 operator learning 训练效率的范式转变——不再追求"纯无数据"，而是"让数值求解器做它擅长的事，神经网络做它擅长的事"。

---

### 3. Quantum Physics-Informed Neural Networks (QPINN)
**arXiv:2605.13892** | 2026-05-12

**一句话：** 用量子可训练嵌入层增强 PINN，解决 Lid-Driven Cavity 问题。

**核心亮点：**
- 将量子可训练嵌入（Quantum Trainable Embeddings）引入物理约束学习
- 为量子计算与科学计算的交叉开辟了试验场
- 延续了 Karniadakis 团队在 PINN 方向的持续创新

**为什么重要：** 不是实用突破，而是一个值得追踪的信号——量子增强的科学计算是否只是噱头，还是真的有优势？

---

## 📊 领域趋势速览

### 🌊 趋势一：KAN × PINN 大爆炸
Kolmogorov-Arnold Networks 正被疯狂嫁接到物理约束学习中，形成 PIKAN 家族：
- **PIKAN** (arXiv:2502.06018, 2507.08338)
- **LegendKINN** (arXiv:2507.19888) — Legendre 多项式基
- **J-PIKAN** — Jacobi 正交多项式基
- **LUT-KAN** (arXiv:2601.03332) — 查表量化加速推理

**判断：** KAN 的可解释性和局部适应性确实对 PDE 求解有天然优势，但真正的工业级落地还要看训练稳定性和泛化性。

### ⚡ 趋势二：Operator Learning 的效率革命
不只是 Solver-in-the-Loop DeepONets，还有：
- **Physics-Informed Laplace Neural Operator** (arXiv:2602.12706) — 在频域做算子学习
- **GraphDeepONet** — 将 DeepONet 适配到图神经网络，处理不规则网格
- **DeepOmamba** (arXiv:2503.29237) — 状态空间模型做时空 PDE 算子学习

**判断：** Neural Operator 正从"学术玩具"走向"工程工具"，关键在于与经典数值方法的混合策略。

### 🔬 趋势三：物理一致性从"软约束"走向"硬约束"
- **Hard Constraint Projection PINN** (arXiv:2601.06244) — 严格满足边界条件
- **GLinSat / LinSatNet** — 将线性约束直接编码进网络层
- **Interval-Constrained PINN** — 对气液界面等复杂场景施加区间约束

**判断：** PINN 社区终于意识到，"近似满足物理"在很多工程场景不够用了。

---

## 📝 论文清单（本周扫描汇总）

| 标题 | 类型 | 机构/作者 | 亮点 |
|------|------|-----------|------|
| K-PINN: Lattice-Boltzmann-Driven PINN | 新方法 | — | 介观物理嵌入 |
| Solver-in-the-Loop DeepONets | 新方法 | ICLR 2026 | 训练效率提升100x |
| QPINN with Quantum Embeddings | 交叉 | — | 量子+科学计算 |
| Physics-Informed Laplace Neural Operator | 新架构 | — | 频域算子学习 |
| Hard Constraint Projection in PINN | 改进 | — | 严格物理约束 |
| DeepOmamba: State-Space PDE Operator | 新架构 | — | Mamba×算子学习 |
| GraphDeepONet: Irregular Grid PDE Solver | 改进 | J. Comp. Physics | GNN+DeepONet |
| A Didactic Guide to PINN Training Cycle | 教程 | GitHub 开源 | 训练技巧综述 |
| LUT-KAN: Fast KAN Inference | 加速 | — | 查表量化 |
| Physics-Informed Neural Operator (PINO) | 综述/方法 | ACM 2024 | 数据+物理联合学习 |

---

## 🎯 下周预告

**轮换至：World Models**

重点扫描方向：
- JEPA / Joint Embedding Predictive Architecture
- Latent World Models for Planning
- Embodied AI & Visual Planning
- 杨立昆团队最新工作（如果发表）

---

## 📚 推荐阅读（前置知识）

如果你对 Physics-informed AI 还不熟悉，本周新增了一篇极佳的入门材料：

**"Physics-Informed Neural Networks: A Didactic Derivation of the Complete Training Cycle"** (arXiv:2604.18481)

这是一篇逐步推导的教程，覆盖了 PINN 完整训练周期的每个环节，适合从原理到实践的系统学习。

---

*龙虾小队 · Paper Radar 🦞*  
*扫描范围：arXiv + 社区热点 | 生成时间：2026-05-17*
