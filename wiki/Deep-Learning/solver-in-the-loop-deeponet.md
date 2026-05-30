# Solver-in-the-Loop DeepONets

> Sources: ICLR 2026; [../../raw/Deep-Learning/2026-W20-physics-informed-ai.md](../../raw/Deep-Learning/2026-W20-physics-informed-ai.md) (编译参考)

## Overview

把经典数值求解器直接放进 DeepONet 的训练循环，训练速度提升两个数量级，同时保持与 PI-DeepONet 相当的精度。核心思想是不再追求"纯无数据"，而是让数值求解器做它擅长的事（计算可靠信号），神经网络做它擅长的事（泛化插值）。

## 核心洞察

传统 PI-DeepONet 通过自动微分计算 PDE 残差，计算开销巨大。Solver-in-the-Loop 用经典求解器的离散监督信号替代纯物理约束——在 Burger's 方程上验证有效，可扩展到高维 PDE（如 Navier-Stokes）。

## 方法论转变

| 传统方法 | Solver-in-the-Loop |
|---------|-------------------|
| 纯物理约束 (PDE 残差) | 数值求解器输出作为监督 |
| 自动微分计算梯度 | 标准监督学习梯度 |
| "无数据"理想 | "混合数据"务实路线 |

## 意义

可能是 operator learning 训练效率的范式转变。不再追求"纯无数据"，而是务实地让数值方法和神经网络各司其职。

## See Also

- [PINN 生态 2026](../Deep-Learning/pinn-ecosystem-2026.md)
- [K-PINN](../Deep-Learning/k-pinn-lattice-boltzmann.md)
