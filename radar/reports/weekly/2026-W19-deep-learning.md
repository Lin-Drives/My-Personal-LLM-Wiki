# 论文雷达周报 - 2026-W19 | Deep Learning

> 扫描时间: 2026-05-10 09:30 (Asia/Shanghai)
> 本周领域: Deep Learning
> 扫描来源: arXiv + PapersWithCode 热点 + ICLR 2026 接收论文

---

## 1. 综述/高影响力论文

### 🏆 本周最值得关注的综述/前沿工作

**1.1 Mamba-3: Improved Sequence Modeling using State Space Principles**
- **来源**: arXiv:2603.15569 (ICLR 2026 Oral)
- **作者**: Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, Albert Gu
- **关键词**: State Space Models, linear-time sequence modeling, inference efficiency
- **核心看点**: 
  - 从inference-first视角出发，提出三大改进：(1) 更expressive的recurrence（基于SSM discretization）；(2) complex-valued state update rule，实现richer state tracking；(3) MIMO (multi-input multi-output) formulation，不增加decode latency的前提下提升性能
  - 1.5B scale下平均下游accuracy比Gated DeltaNet高0.6个百分点，MIMO variant再提升1.2%
  - 用**一半**的state size即可达到Mamba-2的perplexity
  - 显著推进了performance-efficiency Pareto frontier
- **为什么值得关注**: Mamba系列是Transformer替代路线的核心竞争者，Mamba-3被ICLR 2026接收为Oral，标志着SSM范式进入主流视野。complex-valued state update的引入尤其值得关注——这在数学上更接近生物神经系统的振荡动力学

---

## 2. 最新研究亮点 (近30天)

### 🔥 本周热点论文

**2.1 Stability and Generalization in Looped Transformers**
- **作者**: Asher Labovich
- **日期**: 2026-04-16 (arXiv:2604.15259)
- **核心贡献**: 
  - 提出fixed-point based framework分析looped transformers的三个稳定性轴：reachability（可达性）、input-dependence（输入依赖性）、geometry（几何稳定性）
  - 理论证明：没有recall的looped network只有countable fixed points，无法实现强input-dependence
  - recall + outer normalization是最可靠路径，能让fixed point同时满足可达、局部平滑、反向传播稳定
  - 实验验证：在chess、sudoku、prefix-sums任务上，性能与理论预测一致
  - 提出**internal recall**新变体，在sudoku上远超标准recall placement
- **关联领域**: Test-time compute scaling、推理优化

**2.2 Noise Stability of Transformer Models**
- **作者**: Themistoklis Haris
- **日期**: 2026-02-09 (arXiv:2602.08287)
- **核心贡献**:
  - 提出**noise stability**作为衡量深度学习simplicity bias的新指标，替代传统的average sensitivity
  - noise stability衡量模型对**correlated noise**（同时作用于所有输入坐标）的鲁棒性
  - 对单层attention和ReLU MLP层进行理论分析，用covariance interval propagation处理多层传播
  - 开发practical noise stability regularization方法
  - 实验结果：algorithmic tasks上促进grokking，next-token prediction任务加速训练约35%-75%
- **为什么值得关注**: 为"为什么过参数化模型能泛化"提供了新的理论视角，且实际可用作regularizer

**2.3 Compiler-First State Space Duality and Portable O(1) Autoregressive Caching for Inference**
- **日期**: 2026-03-10 (arXiv:2603.09555)
- **核心贡献**:
  - 从compiler-first角度重新思考SSM的inference优化
  - 实现portable O(1) autoregressive caching
  - 与Mamba-3形成互补：Mamba-3改进模型质量，这篇改进推理效率
- **关联领域**: AI Infra (交叉)

**2.4 Transverse Instability, Superposition, and Weight Decay Phase Structure**
- **日期**: 2026-03-14 (arXiv:2602.18523)
- **核心贡献**:
  - 研究grokking现象中的phase transition结构
  - 揭示weight decay如何影响feature learning的phase structure
  - 与Montanari & Wang (2026)的"Phase transitions for feature learning in neural networks"形成系列工作
- **关联领域**: 可解释性、泛化理论

**2.5 Emergent and Generalizable Task-Specific Features in Language Models: Geometric Characterization and Model Attribution**
- **作者**: Agnibh Dasgupta, Abdullah Tanvir, Xin Zhong
- **日期**: 2026-05-07 (arXiv:2605.0645x)
- **核心贡献**:
  - 研究语言模型中"emergent and generalizable task-specific features"的几何特征
  - 用几何方法刻画任务特定特征的出现和泛化行为
  - model attribution分析
- **为什么值得关注**: 直接呼应scaling law中讨论的"emergent abilities"现象，从几何角度给出新的分析工具

**3.1 MASS: Learning Generalizable 3D Medical Image Representations from Mask-Guided Self-Supervision**
- **来源**: CVPR 2026, Stanford University
- **作者**: Yunhe Gao, Yabin Zhang, Chong Wang 等
- **核心看点**:
  - 零标注成本：用in-context segmentation作为pretext task，自动生成class-agnostic masks
  - 可扩展性强：从20 scans到5K multi-modal CT/MRI/PET volumes都有效
  - Few-shot能力突出：仅20-40%标注数据即可match full supervision，比prior SSL方法高>20 Dice points
  - Frozen-encoder classification在unseen pathologies上表现接近fully supervised
- **为什么值得关注**: 代表了self-supervised learning从NLP向视觉、医学领域的迁移范式

---

## 4. 代码/数据集/开源项目

| 项目 | 链接 | 说明 |
|------|------|------|
| mamba-3 (官方实现) | https://github.com/paperwave/mamba-3 | Mamba-3 开源代码 |
| mamba-minimal-jax | https://github.com/radarFudan/mamba-minimal-jax | 极简JAX实现 |
| MASS (CVPR 2026) | https://github.com/Stanford-AIMI/MASS | 医学图像自监督 |

---

## 5. 领域趋势观察

### Deep Learning 本周关键词云
- **Mamba/SSM 持续火热**: Mamba-3 (ICLR 2026 Oral) + 编译器优化，从模型质量到推理效率双管齐下
- **Looped Transformers 崛起**: test-time compute scaling的重要载体，稳定性和泛化理论开始跟进
- **Noise Stability 新指标**: 替代average sensitivity，连接信号传播与可解释性
- **Self-Supervised 向垂直领域渗透**: MASS代表医学图像领域的新突破
- **Grokking / Phase Structure**: 从经验现象到理论分析，2026年有多篇相关论文

### 与相邻领域的交叉
- Deep Learning × AI Infra: SSM编译优化、O(1) inference caching
- Deep Learning × 可解释性: noise stability、phase structure、superposition
- Deep Learning × 医学AI: MASS的mask-guided自监督范式

---

## 6. 本周阅读建议

**优先级排序:**
1. ⭐⭐⭐ **Mamba-3** (arXiv:2603.15569) — ICLR 2026 Oral，SSM路线的里程碑，必须精读abstract和conclusion
2. ⭐⭐ **Stability and Generalization in Looped Transformers** — 理论和实验都很扎实，理解test-time compute scaling的关键
3. ⭐⭐ **Noise Stability of Transformer Models** — 新的regularization工具，实验结果亮眼（加速35%-75%）
4. ⭐ **MASS** — 如果关注视觉/医学方向，这篇的few-shot能力很惊人

---

## 7. 轮换记录

| 周次 | 领域 | 状态 |
|------|------|------|
| 2026-W17 | World Models | ✅ 已完成 |
| 2026-W18 | AI Infra | ✅ 已完成 |
| **2026-W19** | **Deep Learning** | ✅ 本周已扫描 (重新整理版) |
| 2026-W20 | Physics-informed AI | 📅 下周待扫描 |

---

*Generated by 龙虾小队 · Paper Radar 🦞*
*Revision: v2 (2026-05-10 09:30, 替换占位符为真实论文数据)*
