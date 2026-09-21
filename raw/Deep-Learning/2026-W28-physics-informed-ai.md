# Physics-informed AI 周报 — W28, 2026

> 扫描时间：2026-07-12 | 领域：Physics-informed AI / Scientific Machine Learning  
> 覆盖周期：2026年6月–7月最新进展

---

## 🔥 Top 5 本周最值得关注

### 1️⃣ TF-SNO: Time-Frequency Gated Spectral Neural Operators
- **arXiv**: 2606.21189 | **日期**: 2026-06-19
- **核心突破**：提出**时频门控谱神经算子**，专门解决**非平稳PDE**的学习难题。传统FNO在频率域全局处理，难以捕捉时变特征；TF-SNO通过时频分解+门控机制，在谱域实现自适应时频局部化。
- **意义**：填补了神经算子在非平稳动力学（如湍流、波动传播）上的空白，是FNO架构的重要进化。

### 2️⃣ Pi-PINN: Transferable Physics-Informed Representations
- **arXiv**: 2604.21761 | **日期**: 2026-04-23
- **核心突破**：基于伪逆PINN框架，学习**可迁移的物理信息表示**，通过闭式头部适应（closed-form head adaptation）快速求解新PDE实例。无需任何新数据即可泛化到未见PDE。
- **性能**：比标准PINN快 **100–1000×**，误差低 **10–100×**。
- **意义**：PINN从「单问题求解器」迈向「通用物理表示学习」的关键一步。

### 3️⃣ Dual-Network PINNs for Optimal Control
- **arXiv**: 2606.15271 | **日期**: 2026-06-13
- **核心突破**：针对质量-弹簧-阻尼系统，提出**双网络PINN架构**统一状态近似、控制优化和参数估计，在可微优化框架内解决最优控制问题。
- **意义**：PINN方法论向**控制论**和**PDE约束优化**的系统性拓展，验证了物理信息学习在工程控制中的实用性。

### 4️⃣ Physics-aware Neural Operator Transformer for EAST Divertor
- **arXiv**: 2606.31574 | **日期**: 2026-06-30
- **核心突破**：将**物理感知神经算子与Transformer结合**，用于托卡马克（EAST）钨单块偏滤器的温度场重建。融合物理约束的注意力机制处理聚变装置中的极端热负荷。
- **意义**：SciML在**核聚变工程**中的前沿应用，展示了物理感知架构对高保真科学仪器的价值。

### 5️⃣ LAM-PINN: Compositional Meta-Learning for PINNs
- **arXiv**: 2604.26999 | **日期**: 2026-04-29
- **核心突破**：**组合式元学习PINN** —— 不依赖单一全局初始化，而是将模型分解为聚类专用子网络+共享元网络，通过学习亲和度动态路由，缓解任务异质性带来的负迁移。
- **性能**：在未见任务上MSE降低 **19.7倍**，仅需10%迭代次数。
- **意义**：为参数化PDE家族的高效迁移提供了模块化新范式。

---

## 📊 领域趋势观察

### 🔗 趋势一：PINN × Neural Operator 融合加速
- **PINO（Physics-Informed Neural Operator）** 成为明确主线：将神经算子的泛化能力与PINN的无数据训练结合。
- 代表性工作：6月的系统训练研究（arXiv:2606.06164）、Walk-on-Spheres Neural Operator（arXiv:2603.01193，用蒙特卡洛弱监督训练算子，训练速度提升 **6.31×**，GPU内存降低 **2.97×**）。
- **判断**：2026年可称为「PINO元年」，两个原本平行的范式正式进入融合期。

### 🎼 趋势二：谱方法与时频建模成为新焦点
- TF-SNO（时频门控）、Stable Spectral Neural Operator（人大张瑞团队，KDD 2026）等工作显示，**谱域学习**正从FNO的简单傅里叶变换向更精细的时频分解演进。
- 对**刚性PDE（stiff PDE）**和**多尺度物理**的建模能力显著提升。

### 🧩 趋势三：从「单任务求解」到「可迁移物理表示」
- Pi-PINN、LAM-PINN、Meta-Learning FNO等工作的共同方向：让SciML模型**跨PDE泛化**。
- 核心矛盾：神经算子需要大量仿真数据 vs. PINN优化困难。组合式元学习和闭式适应是两条有效路径。

### 🏭 趋势四：工程应用场景持续深化
- **聚变**：EAST偏滤器温度场重建（物理感知Transformer）
- **制造**：金属增材制造实时变形预测（PINO）
- **能源**：CO₂地质封存实时预测（Nested FNO）
- **流体**：OmniFluids统一流体动力学预训练模型（人大团队）

### 🛠️ 趋势五：JAX生态工具链成熟
- **jNO**（arXiv:2605.10159）：JAX原生神经算子库，支持PDE基础模型（Poseidon/Walrus/Morph）、FEM集成、LoRA式参数适配。
- 与NVIDIA PhysicsNeMo、DeepXDE形成三足鼎立之势。

---

## 📄 其他值得关注的论文

| 论文 | arXiv | 日期 | 亮点 |
|------|-------|------|------|
| On the training of physics-informed neural operators | 2606.06164 | 2026-06-04 | PINO训练的系统研究，揭示数据+物理约束的最佳配比 |
| Walk-on-Spheres Neural Operator | 2603.01193 | 2026-03-01 | 蒙特卡洛弱监督，避免高阶导数，数据-free |
| jNO: JAX Library for Neural Operator Training | 2605.10159 | 2026-04-29 | JAX原生，支持PDE基础模型和FEM |
| Exact Constraint Enforcement in PIELMs | 2601.10999 | 2026-01 | 零空间投影实现精确物理约束 |
| NPSolver: Neural Poisson Solver with Iterative Physics Supervision | — | KDD 2026 | 迭代物理监督的泊松求解器 |
| PerFlow: Physics-Embedded Rectified Flow | — | IJCAI 2026 | 物理嵌入整流流，用于时空动力学重建与UQ |

---

## 🎯 关键洞察

> **Physics-informed AI 正在经历从「方法验证」到「工程落地」的质变。**
>
> 2024年的核心问题是「PINN能不能解这个PDE」，2026年的核心问题是「如何让一个模型解一族PDE，并且部署到真实的 EAST 托卡马克里」。
>
> PINO的崛起、可迁移表示的成熟、JAX工具链的完善，意味着 SciML 正从学术玩具转变为工业级科学计算的替代方案。

---

## 📅 下周预告

W29 → **AI Infra**（循环回归）

---

## 🔗 机器摘要区块

```yaml
paper_radar:
  week: W28
  field: Physics-informed AI
  date: 2026-07-12
  top_papers:
    - title: "TF-SNO: Time-Frequency Gated Spectral Neural Operators"
      arxiv: "2606.21189"
      url: "https://arxiv.org/abs/2606.21189"
      highlight: "时频门控谱神经算子，解决非平稳PDE"
    - title: "Pi-PINN: Transferable Physics-Informed Representations"
      arxiv: "2604.21761"
      url: "https://arxiv.org/abs/2604.21761"
      highlight: "可迁移物理表示，闭式头部适应，100-1000x加速"
    - title: "Dual-Network PINNs for Optimal Control"
      arxiv: "2606.15271"
      url: "https://arxiv.org/abs/2606.15271"
      highlight: "双网络PINN统一状态-控制-参数估计"
    - title: "Physics-aware Neural Operator Transformer for EAST Divertor"
      arxiv: "2606.31574"
      url: "https://arxiv.org/abs/2606.31574"
      highlight: "聚变装置偏滤器温度场重建"
    - title: "LAM-PINN: Compositional Meta-Learning for PINNs"
      arxiv: "2604.26999"
      url: "https://arxiv.org/abs/2604.26999"
      highlight: "组合式元学习，19.7x误差降低"
  trends:
    - "PINN × Neural Operator 融合（PINO元年）"
    - "谱方法与时频建模精细化"
    - "可迁移物理表示学习"
    - "工程应用深化（聚变/制造/流体）"
    - "JAX工具链成熟"
```

---

*龙虾小队 · Paper Radar 🦞*
