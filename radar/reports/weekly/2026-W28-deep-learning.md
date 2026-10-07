# 🧠 论文雷达 · Deep Learning 周报 — 2026年W28

> **扫描周期：** 2026-06-29 ~ 2026-07-05  
> **轮换领域：** Deep Learning  
> **报告时间：** 2026-07-05 09:17 CST

---

## 🔥 本周 Top 5 精选论文

### 1️⃣ Mamba-3: Improved Sequence Modeling using State Space Principles
- **arXiv:** [2603.15569](https://arxiv.org/abs/2603.15569) (ICLR 2026)
- **作者：** Lahoti et al. (CMU/Princeton/Together.AI)
- **核心突破：** 在Mamba-2基础上进一步改进状态空间建模原则，引入新的状态空间理论框架，在语言建模、音频和基因组学等多模态任务上达到SOTA。
- **为什么重要：** 这是Mamba系列在ICLR 2026的正式发表版本，标志着状态空间模型(SSM)已从前沿探索走向主流架构竞争。

### 2️⃣ Forget Attention: Importance-Aware Attention Is All You Need
- **arXiv:** [2606.02332](https://arxiv.org/abs/2606.02332) (2026-06-02)
- **核心突破：** 提出"重要性感知注意力"机制，通过动态评估token重要性来优化注意力计算，在保持性能的同时降低计算开销。
- **为什么重要：** 直接对标Transformer核心机制，可能替代传统注意力成为更高效的选择。

### 3️⃣ Bootleg: Hierarchical Self-Distillation for Representation Learning
- **arXiv:** [2603.15553](https://arxiv.org/abs/2603.15553)
- **核心突破：** 层次化自蒸馏框架，多隐藏层预测+教师网络，在ImageNet上实现 **+10%** 的显著提升。
- **为什么重要：** 自监督学习领域的重要进展，突破了I-JEPA的瓶颈，为视觉表征学习开辟新方向。

### 4️⃣ ConTraIRL: Factorized Contrastive Abstractions for Transferable IRL
- **arXiv:** [2606.03017](https://arxiv.org/abs/2606.03017) (2026-06-02)
- **核心突破：** 将对比学习与逆强化学习结合，提出因子化对比抽象方法，实现跨任务的可迁移性。
- **为什么重要：** 连接了自监督表示学习与强化学习，为多任务迁移学习提供新范式。

### 5️⃣ Towards A Unified PAC-Bayesian Framework for Norm-based Generalization Bounds
- **arXiv:** [2601.08100](https://arxiv.org/abs/2601.08100) (2026-01-13)
- **作者：** Xinping Yi et al.
- **核心突破：** 提出统一的PAC-Bayesian框架，将泛化界推导重新表述为各向异性高斯后验上的随机优化问题。
- **为什么重要：** 为深度学习的泛化理论提供了更紧致的、结构感知的理论保证。

---

## 📊 其他值得关注的论文

### 表征学习 & 自监督
- **BrainDINO** (arXiv:2604.27277) — Brain MRI基础模型，可泛化的临床表征学习
- **Enabling self-supervised learned primal dual with Noise2Inverse** (arXiv:2606.26991, 2026-06-25) — 自监督CT重建，无需ground-truth
- **Skip Connections and Generalization: A PAC-Bayesian Perspective** (OpenReview 2025) — 从理论上解释残差连接为何能改善泛化

### 架构创新
- **ELMoE-3D** (arXiv:2604.14626) — 面向3D感知的MoE架构，高效处理高维空间数据
- **Compiler-First State Space Duality** (arXiv:2603.09555) — 面向编译器优化的SSM设计，O(1)自回归缓存
- **Co-Settle** (CVPR 2026) — 从静态到动态的自监督图像到视频表征迁移

### 优化与理论
- **A PAC-Bayesian approach to generalization for quantum models** (arXiv:2603.22964) — 量子模型的PAC-Bayesian泛化界
- **Deep Shift Neural Networks + AutoML** (arXiv:2606.23208, 2026-06-22) — 多目标超参优化实现可持续深度学习

---

## 🎯 领域趋势观察

1. **状态空间模型(Mamba)进入3.0时代**：从线性时间复杂度到编译器级优化，SSM正在全面挑战Transformer的地位。

2. **自监督学习向多模态和特定领域深化**：从通用视觉向医疗影像(BrainDINO)、CT重建(Noise2Inverse)等专业领域扩展。

3. **注意力机制的效率革命**："Forget Attention"等新型注意力变体，以及SSM的崛起，共同推动序列建模的效率边界。

4. **理论工具更加实用化**：PAC-Bayesian框架从纯理论走向能解释实际架构(残差连接)的工具。

---

## 📅 轮换进度

AI Infra ✅ → Deep Learning ✅ → **Physics-informed AI 📅（下周W29）** → World Models → Embodied Intelligence

---

*龙虾小队 · Paper Radar 🦞*
