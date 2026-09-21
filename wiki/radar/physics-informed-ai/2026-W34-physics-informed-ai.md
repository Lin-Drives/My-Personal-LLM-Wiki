# 论文雷达周报 · Physics-informed AI / Scientific Machine Learning

**扫描周期：** 2026-08-09 至 2026-08-16  
**领域：** Physics-informed AI / Scientific Machine Learning  
**生成时间：** 2026-08-16 09:17 CST

---

## 🔥 Top 5 核心看点

### 1. CL-PINN: 参数化PDE的连续学习框架 (arXiv:2608.05569v1, 8月5日)

**标题：** Continual-Learning Physics-Informed Neural Networks for Parameterized Partial Differential Equations  
**作者：** Feiyang Chen et al.  
**机构：** 国防科技大学

**核心创新：**
- 首次将**连续学习(Continual Learning)**引入PINN，解决参数化PDE求解中的**灾难性遗忘**问题
- 提出CL-PINN框架：当模型按顺序学习不同参数配置的PDE时，自动保留先前学到的知识
- 通过梯度投影和参数隔离技术，在不影响新任务学习的前提下维持旧任务的精度

**意义：** 传统PINN在参数化PDE上训练时，学习新参数会遗忘旧参数，CL-PINN使单模型可连续适配不同物理场景，大幅提升了PINN的工程实用性。

---

### 2. EvoPINN: LLM驱动的PINN自动算法发现 (arXiv:2607.21046v1, 7月29日)

**标题：** EvoPINN: Agentic Discovery of Executable Algorithms for Physics-Informed Neural Networks  
**作者：** Aniket Jadhav et al.  
**机构：** Texas A&M University

**核心创新：**
- 将**LLM Agent**引入PINN算法设计，实现全自动的算法进化与发现
- 框架包含：LLM生成候选算法 → 自动代码执行 → 性能评估 → 反馈优化 → 迭代进化
- 自动发现的新算法在多个基准PDE上超越了人类手工设计的SOTA方法

**意义：** 这是"AI设计AI"在科学计算领域的重要落地。EvoPINN证明LLM不仅能写代码，还能自主发现解决PDE的新算法范式，标志着SciML进入**自动化算法工程**时代。

---

### 3. 多尺度最优输运神经算子 (arXiv:2608.08491v1, 8月10日)

**标题：** Multiscale Optimal Transport Neural Operator  
**作者：** 研究团队  
**机构：** —

**核心创新：**
- 将**最优输运理论(Optimal Transport)**与神经算子结合，构建多尺度PDE求解器
- 利用OT的度量特性，在多尺度间建立物理上合理的映射关系
- 相比传统FNO，在多尺度物理问题（如湍流、多孔介质流动）上表现更优

**意义：** 最优输运为神经算子提供了新的数学基础，可能在保持物理一致性的同时提升复杂多尺度问题的求解精度。

---

### 4. Enhanced Diffusion Sampling: 扩散模型赋能分子动力学 (Microsoft Research, 8月11日)

**标题：** Enhanced Diffusion Sampling: Efficient Rare Event Sampling and Free Energy Calculation with Diffusion Models  
**作者：** Yu Xie, Ludwig Winkler, Lixin Sun, Sarah Lewis 等  
**机构：** Microsoft Research AI for Science, Frank Noé 组

**核心创新：**
- 解决扩散模型（如BioEmu）在分子模拟中的**稀有事件采样**难题
- 提出三种增强采样算法：UmbrellaDiff（伞形采样+扩散）、ΔG-Diff（自由能差计算）、MetaDiff（批量化元动力学）
- 通过定量准确的引导协议生成偏置系综，再通过精确重加权恢复平衡统计

**结果：** 在蛋白质折叠景观和自由能计算上，可在GPU分钟到小时级别完成传统MD需数月的计算。

**意义：** 继BioEmu实现平衡系综高效采样后，Enhanced Diffusion Sampling进一步攻克了**稀有事件**这一MD核心瓶颈。扩散模型+物理重加权的组合，可能彻底改变计算化学的采样范式。

---

### 5. 跨模态Decoder-only模型求解PDE (arXiv:2510.05278v2, 2026年3月更新)

**标题：** Cross-Modal Adaptation of Decoder-only Models to PDEs  
**核心思路：**
- 将LLM（decoder-only架构）跨模态适配到PDE求解任务
- 不训练专用科学模型，而是利用预训练LLM的推理能力理解并求解偏微分方程
- 与PDE-FM、POSEIDON、UNISOLVER等专用基础模型形成互补路径

**意义：** 探索了"通用AI做科学"的可能性——无需专门训练科学模型，利用LLM的跨模态能力即可处理PDE。这暗示未来可能出现**统一的基础模型**，同时处理语言、代码和科学问题。

---

## 📊 其他重要进展

### 神经算子架构创新

| 论文 | 时间 | 核心贡献 |
|------|------|----------|
| **TF-SNO** (arXiv:2606.21189) | 2026-06 | 时频门控谱神经算子，专门攻克**非平稳PDE**，FNO架构的重要进化 |
| **Walk-on-Spheres Neural Operator** (arXiv:2603.01193) | 2026-06 | 将随机游走方法(WoS)与神经算子结合，处理复杂边界条件 |
| **Hartley Neural Operator** (arXiv:2606.24851) | 2026-06 | 基于Hartley变换的全新算子架构，替代Fourier变换 |

### PDE基础模型格局

当前PDE基础模型已形成**三大阵营**：
- **专用架构派：** POSEIDON（多尺度ViT）、UNISOLVER（PDE条件Transformer）、CNO-FM
- **通用模型跨模态派：** 本文介绍的Decoder-only跨模态适配
- **物理融合派：** PDE-FM（流匹配）、Walrus等

---

## 💡 本周趋势洞察

### 1. PINN进入"自动化+持续学习"时代
- **EvoPINN**证明LLM可自主发现PINN算法，人类设计→AI设计
- **CL-PINN**解决了PINN工程部署的关键障碍（参数化适配时的遗忘问题）
- PINN正从学术研究走向可连续部署的工程工具

### 2. 扩散模型成为分子模拟新基建
- **BioEmu**（扩散模型生成蛋白平衡系综，1kcal/mol精度）→ **Enhanced Diffusion Sampling**（稀有事件采样）
- 扩散模型在分子动力学中完成了从"生成结构"到"加速采样"到"计算自由能"的完整闭环
- 计算化学的采样瓶颈正在被AI系统性瓦解

### 3. 神经算子架构持续进化
- 从FNO → TF-SNO（时频分解）→ WoS-NO（随机游走）→ HNO（Hartley变换）→ OT-NO（最优输运）
- 数学工具的多元化（Fourier、Hartley、OT、WoS）推动神经算子家族不断壮大

### 4. "通用AI做科学" vs "专用科学模型"的路线之争
- 专用模型（POSEIDON、UNISOLVER）在精度上领先
- 跨模态通用模型（LLM适配PDE）在灵活性和泛化性上有优势
- 短期内专用模型仍是主流，但通用路线的长期潜力不容忽视

---

## 📁 参考资料

- CL-PINN: https://arxiv.org/abs/2608.05569
- EvoPINN: https://arxiv.org/abs/2607.21046
- Multiscale OT Neural Operator: https://arxiv.org/abs/2608.08491
- Enhanced Diffusion Sampling: https://arxiv.org/abs/2602.16634 / https://arxiv.org/abs/2608.03495
- Cross-Modal Decoder-only PDE: https://arxiv.org/abs/2510.05278
- TF-SNO: https://arxiv.org/abs/2606.21189
- WoS-NO: https://arxiv.org/abs/2603.01193
- Hartley Neural Operator: https://arxiv.org/abs/2606.24851
- Poseidon (PDE Foundation Model): https://arxiv.org/abs/2405.19101
- UNISOLVER: https://arxiv.org/abs/2405.19101 (ICML 2025)

---

*龙虾小队 · Paper Radar 🦞*
