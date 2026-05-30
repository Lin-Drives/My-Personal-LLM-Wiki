# PINN/KAN 生态 2026

> Sources: W20 物理AI 周报, 2026-05
> Raw: [../../raw/Deep-Learning/2026-W20-physics-informed-ai.md](../../raw/Deep-Learning/2026-W20-physics-informed-ai.md)

## Overview

2026 年 Physics-informed AI 领域呈现三大趋势：KAN × PINN 大爆炸、Operator Learning 效率革命、物理约束从软到硬。PIKAN 家族（PIKAN, LegendKINN, J-PIKAN, LUT-KAN）正被疯狂嫁接到物理约束学习中，Neural Operator 从学术玩具走向工程工具，hard constraint 方法开始解决"近似满足物理不够用"的实际需求。

## 趋势一：KAN × PINN 大爆炸

Kolmogorov-Arnold Networks 的可解释性和局部适应性对 PDE 求解有天然优势。2026 年出现了 PIKAN 家族：LegendKINN（Legendre 多项式基）、J-PIKAN（Jacobi 正交多项式基）、LUT-KAN（查表量化加速推理）。真正的工业级落地要看训练稳定性和泛化性。

## 趋势二：Operator Learning 效率革命

- Physics-Informed Laplace Neural Operator — 在频域做算子学习
- GraphDeepONet — 适配图神经网络处理不规则网格
- DeepOmamba — 状态空间模型做时空 PDE 算子学习

## 趋势三：硬约束 PINN

PINN 社区意识到"近似满足物理"在工程场景不够用了。Hard Constraint Projection PINN 严格满足边界条件，GLinSat/LinSatNet 将线性约束直接编码进网络层。

## 关键论文速览

- QPINN: 量子可训练嵌入 + PINN (arXiv:2605.13892)
- PINN 训练教程: "A Didactic Guide to PINN Training Cycle" (arXiv:2604.18481)

## See Also

- [K-PINN](../Deep-Learning/k-pinn-lattice-boltzmann.md)
- [Solver-in-the-Loop DeepONets](../Deep-Learning/solver-in-the-loop-deeponet.md)
