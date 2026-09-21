# Paper Radar Weekly — Physics-informed AI | 2026-W25

**扫描时间：** 2026-06-14 (Sun)  
**本周领域：** Physics-informed AI（物理信息人工智能）  
**扫描范围：** arXiv + 社区热点  

---

## 🔥 本周 Top 5 最值得关注

### 1️⃣ **DC-PINNs** (arXiv:2604.13723, Apr 15) — Derivative-Constrained PINNs
**核心：** 把导数约束（bounds, monotonicity, convexity, incompressibility）显式嵌入PINN损失函数，用自适应损失平衡减少手工调参。
**为什么重要：** 传统PINN只约束PDE残差，但很多物理问题本质上要求导数层面的约束。DC-PINN在heat diffusion with bounds、金融volatility arbitrage-free约束、流体vortices shed等benchmark上稳定降低constraint violations，且能自动适应不同物理要求。这代表PINN从“近似满足物理”向“严格满足物理”的又一步。
**亮点：** 自适应性损失平衡 + 自动微分实现通用非线性导数约束。

### 2️⃣ **MI-PINN** (arXiv:2605.03510, May 6) — Meta-Inverse Physics-Informed Neural Network
**核心：** 将逆问题建模从joint optimization改写成two-stage meta-learning：先学跨任务的physics-aware representation，再固定representation只做task-specific逆推。
**为什么重要：** 逆问题（从观测推断参数/动力学）是SciML核心场景，但传统PINN做逆问题往往optimization困难、泛化差。MI-PINN通过降维搜索空间提升sample efficiency，还引入adaptive clustering-based multi-branch learning处理多尺度动力学。在33维耦合ODE的PBPK模型（药物动力学）上验证了准确恢复masked参数。
**亮点：** 元学习视角做逆问题 + 多尺度分支架构。

### 3️⃣ **DDS-PINN** (arXiv:2604.05651, Apr 8) — Domain-Decomposed and Shifted PINN
**核心：** 用localized networks + unified global loss解决多尺度流体中的长程依赖问题，实现无数据或少数据的Navier-Stokes求解。
**为什么重要：** 复杂流体（湍流、边界层分离）是PINN的硬伤，因为多尺度+长程依赖。DDS-PINN在backward-facing step（Re=100无数据求解，Re=10000仅用500个随机监督点<0.3% domain）收敛到O(10^-4)， outperform Residual-based Attention-PINN。对湍流超分辨和稀疏实验测量→高保真重建有直接意义。
**亮点：** 真正数据高效的湍流PINN，少数据即可收敛。

### 4️⃣ **PINN for Tokamak MHD** (arXiv:2604.20085, Apr 22) — 托卡马克磁流体动力学
**核心：** 首次用PINN无数据学习time-dependent quasi-static MHD方程，在ITER-like托卡马克几何中预测等离子体垂直位移事件。
**为什么重要：** 核聚变模拟是极其昂贵的多尺度 stiff PDE问题。PINN能作为fast surrogate替代传统MHD solver做参数扫描和实时状态估计，虽然还不是drop-in replacement，但proof-of-principle意义重大。论文也诚实暴露了numerical stiffness和boundary condition的挑战。
**亮点：** 核聚变 + 无数据物理驱动，科学意义大于精度本身。

### 5️⃣ **OrthoSolver** (ICLR 2026, May) — Neural Proper Orthogonal Decomposition Solver
**核心：** 北航团队提出，将经典POD（Proper Orthogonal Decomposition）的“能量最大化”重新解释为互信息最大化，推广到非线性神经分解，用正交约束避免模态坍缩。
**为什么重要：** 降阶建模（ROM）是SciML的基石方向。OrthoSolver不是简单堆更复杂的神经网络，而是把经典数值方法的结构性原则重新解释并嵌入可训练框架。在PDEBench七个基准上一致领先。代表了一种“经典方法+深度学习”的融合范式，值得长期关注。
**亮点：** 经典POD的信息论升级 + 正交约束避免模态冗余。

---

## 📌 其他值得注意的论文

- **naPINN** (arXiv:2602.02547) — Noise-Adaptive PINN，用energy-based model学习残差分布，自适应过滤异常值，在非高斯噪声和outliers下显著优于robust PINN baseline。
- **MSN-PINN** (arXiv:2601.22751) — Physics-informed Müntz-Szász Networks，专门处理singularity处的power-law scaling，把scaling exponent变成可训练参数， corner singularity恢复误差仅0.009%。
- **Hard Constraint Projection PINN** (arXiv:2601.06244) — 将hard constraint从线性PDE扩展到强非线性PDE（2D incompressible Navier-Stokes），用unlearnable HCP layer投影到精确解超平面。
- **Nirenberg Neural Network** (arXiv:2602.12368) — 用PINN做微分几何中经典的Nirenberg问题（高斯曲率预设），losses低至10^-7–10^-10，展示神经求解器在几何分析中的探索潜力。
- **Courant** (arXiv:2605.25115, May 24) — State-Adaptive Perceiver-Based Neural Surrogate，局部支撑+可解释场分解，工业级几何规模神经代理模型。

---

## 📅 轮换进度

AI Infra ✅ → Deep Learning ✅ → **Physics-informed AI ✅（本周 W25）** → World Models 📅（下周 W26） → Embodied Intelligence 📅

**附注：** 上周 W24 的扫描因系统调度未执行，本周直接推进到 W25 的 Physics-informed AI 扫描。

---

## 🔍 领域趋势观察

**本周主题：PINN的“从软约束到硬约束”进化**

1. **约束升级：** 从PDE残差（软约束）→ 导数约束（DC-PINN）→ 硬约束投影（HCP layer）→ 几何/拓扑约束（Nirenberg NN），PINN正在逐步增强对物理规则的“严格遵守”能力。
2. **逆问题元学习化：** MI-PINN代表逆问题从task-specific优化向meta-learning范式的迁移，这对药物动力学、参数推断等场景有普适意义。
3. **核聚变/工业级应用：** Tokamak PINN和Courant surrogate分别指向科学前沿和工业规模，说明PINN/神经算子正在从学术玩具走向实际工程。
4. **经典方法深度融合：** OrthoSolver将POD的信息论本质重新挖掘，说明SciML的下一步不是替代经典方法，而是重新理解并升级它们。

---

## 🤖 Machine Metadata — For Kimi Work Auto-Ingest

```yaml
# Paper Radar Weekly — Machine Readable Block
# Format: YAML 1.2 | Encoding: UTF-8
# Generated: 2026-06-14T09:17:00+08:00
# Week: 2026-W25
# Domain: Physics-informed AI

papers:
  - arxiv_id: "2604.13723"
    title: "DC-PINNs: Derivative-Constrained Physics-Informed Neural Networks"
    pdf_url: "https://arxiv.org/pdf/2604.13723.pdf"
    abstract_url: "https://arxiv.org/abs/2604.13723"
    category: "Physics-informed AI"
    sub_tags: ["PINN", "hard-constraint", "derivative-constraint", "fluid"]
    priority: "top3"
    one_liner: "把导数约束显式嵌入PINN，从近似满足物理迈向严格满足物理"
    authors: "[anonymous from arXiv]"
    published: "2026-04-15"
    has_pdf: true

  - arxiv_id: "2605.03510"
    title: "MI-PINN: Meta-Inverse Physics-Informed Neural Network"
    pdf_url: "https://arxiv.org/pdf/2605.03510.pdf"
    abstract_url: "https://arxiv.org/abs/2605.03510"
    category: "Physics-informed AI"
    sub_tags: ["PINN", "inverse-problem", "meta-learning", "pharmacokinetics"]
    priority: "top3"
    one_liner: "元学习视角做逆问题，先学跨任务物理表征再task-specific逆推"
    authors: "[anonymous from arXiv]"
    published: "2026-05-06"
    has_pdf: true

  - arxiv_id: "2604.05651"
    title: "DDS-PINN: Domain-Decomposed and Shifted Physics-Informed Neural Network"
    pdf_url: "https://arxiv.org/pdf/2604.05651.pdf"
    abstract_url: "https://arxiv.org/abs/2604.05651"
    category: "Physics-informed AI"
    sub_tags: ["PINN", "turbulence", "domain-decomposition", "few-data"]
    priority: "top3"
    one_liner: "真正数据高效的湍流PINN，Re=10000仅用500个随机点即可收敛"
    authors: "[anonymous from arXiv]"
    published: "2026-04-08"
    has_pdf: true

  - arxiv_id: "2604.20085"
    title: "Physics-Informed Neural Networks for Time-Dependent Quasi-Static MHD in Tokamak Geometries"
    pdf_url: "https://arxiv.org/pdf/2604.20085.pdf"
    abstract_url: "https://arxiv.org/abs/2604.20085"
    category: "Physics-informed AI"
    sub_tags: ["PINN", "nuclear-fusion", "MHD", "tokamak"]
    priority: "top5"
    one_liner: "首次无数据学习托卡马克time-dependent MHD方程，核聚变模拟的fast surrogate"
    authors: "[anonymous from arXiv]"
    published: "2026-04-22"
    has_pdf: true

  - arxiv_id: null
    title: "OrthoSolver: Neural Proper Orthogonal Decomposition Solver"
    pdf_url: null
    abstract_url: null
    category: "Physics-informed AI"
    sub_tags: ["ROM", "POD", "orthogonal-constraint", "PDEBench"]
    priority: "top5"
    one_liner: "将经典POD重新解释为互信息最大化，PDEBench七个基准领先"
    authors: "北航团队"
    published: "2026-05"
    venue: "ICLR 2026"
    has_pdf: false
    note: "会议论文，PDF需从OpenReview或作者主页获取"

  - arxiv_id: "2602.02547"
    title: "naPINN: Noise-Adaptive Physics-Informed Neural Networks"
    pdf_url: "https://arxiv.org/pdf/2602.02547.pdf"
    abstract_url: "https://arxiv.org/abs/2602.02547"
    category: "Physics-informed AI"
    sub_tags: ["PINN", "robustness", "noise-adaptive"]
    priority: "honorable-mention"
    one_liner: "用energy-based model学习残差分布，自适应过滤异常值"
    authors: "[anonymous from arXiv]"
    published: "2026-02"
    has_pdf: true

  - arxiv_id: "2601.22751"
    title: "MSN-PINN: Physics-informed Müntz-Szász Networks"
    pdf_url: "https://arxiv.org/pdf/2601.22751.pdf"
    abstract_url: "https://arxiv.org/abs/2601.22751"
    category: "Physics-informed AI"
    sub_tags: ["PINN", "singularity", "power-law"]
    priority: "honorable-mention"
    one_liner: "专门处理singularity处的power-law scaling，corner singularity恢复误差仅0.009%"
    authors: "[anonymous from arXiv]"
    published: "2026-01"
    has_pdf: true

  - arxiv_id: "2601.06244"
    title: "Hard Constraint Projection for Physics-Informed Neural Networks"
    pdf_url: "https://arxiv.org/pdf/2601.06244.pdf"
    abstract_url: "https://arxiv.org/abs/2601.06244"
    category: "Physics-informed AI"
    sub_tags: ["PINN", "hard-constraint", "Navier-Stokes"]
    priority: "honorable-mention"
    one_liner: "将hard constraint从线性PDE扩展到强非线性PDE，用unlearnable HCP layer投影"
    authors: "[anonymous from arXiv]"
    published: "2026-01"
    has_pdf: true

  - arxiv_id: "2602.12368"
    title: "Nirenberg Neural Network"
    pdf_url: "https://arxiv.org/pdf/2602.12368.pdf"
    abstract_url: "https://arxiv.org/abs/2602.12368"
    category: "Physics-informed AI"
    sub_tags: ["PINN", "differential-geometry", "Nirenberg-problem"]
    priority: "honorable-mention"
    one_liner: "用PINN做微分几何中经典的Nirenberg问题，losses低至10^-7–10^-10"
    authors: "[anonymous from arXiv]"
    published: "2026-02"
    has_pdf: true

  - arxiv_id: "2605.25115"
    title: "Courant: State-Adaptive Perceiver-Based Neural Surrogate"
    pdf_url: "https://arxiv.org/pdf/2605.25115.pdf"
    abstract_url: "https://arxiv.org/abs/2605.25115"
    category: "Physics-informed AI"
    sub_tags: ["neural-surrogate", "perceiver", "industrial-scale"]
    priority: "honorable-mention"
    one_liner: "局部支撑+可解释场分解，工业级几何规模神经代理模型"
    authors: "[anonymous from arXiv]"
    published: "2026-05-24"
    has_pdf: true

rotation:
  current_week: "W25"
  current_domain: "Physics-informed AI"
  next_domain: "World Models"
  next_week: "W26"
  schedule:
    - { week: "W21", domain: "World Models", status: "done" }
    - { week: "W22", domain: "AI Infra", status: "done" }
    - { week: "W23", domain: "Deep Learning", status: "done" }
    - { week: "W24", domain: "Physics-informed AI", status: "skipped" }
    - { week: "W25", domain: "Physics-informed AI", status: "done" }
    - { week: "W26", domain: "World Models", status: "pending" }

meta:
  total_papers_found: 10
  top3_count: 3
  top5_count: 5
  honorable_mention_count: 5
  non_arxiv_count: 1
  report_version: "1.0"
```

---

*龙虾小队 · Paper Radar 🦞*  
*自动扫描，手动精选，每周日见。*
