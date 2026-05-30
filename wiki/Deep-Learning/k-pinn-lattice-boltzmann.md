# K-PINN: 介观物理约束神经网络

> Sources: arXiv:2604.03481, 2026-04
> Raw: [../../raw/Deep-Learning/2026-meshram-k-pinn-lattice-boltzmann.md](../../raw/Deep-Learning/2026-meshram-k-pinn-lattice-boltzmann.md); [../../raw/Deep-Learning/2026-W20-physics-informed-ai.md](../../raw/Deep-Learning/2026-W20-physics-informed-ai.md) (编译参考)

## Overview

将介观尺度的 Lattice-Boltzmann 方程直接嵌入 PINN，突破了传统 PINN 只能处理宏观连续方程的限制。U-Net 编码器-解码器结构使误差相比传统神经网络降低 50-75%，质量守恒误差 < 1.5%。成功建模接触钉扎、各向异性铺展、毛细滞后等复杂液滴现象。收敛后实时预测速度 > 10^4 次/秒。

## 为什么重要

这是 PINN 从"宏观唯象"走向"介观机理"的关键一步。传统 PINN 基于 Navier-Stokes 等宏观方程，对多相流润湿性工程等场景精度不够。Lattice-Boltzmann 在介观层面保持物理一致性，打开了新的应用空间。

## 关键技术点

- Lattice-Boltzmann 方程直接作为物理约束嵌入损失函数
- U-Net 结构适合多尺度物理场的建模
- 质量守恒误差 < 1.5% 是工程可用的精度

## See Also

- [PINN 生态 2026](../Deep-Learning/pinn-ecosystem-2026.md)
- [Solver-in-the-Loop DeepONets](../Deep-Learning/solver-in-the-loop-deeponet.md)
