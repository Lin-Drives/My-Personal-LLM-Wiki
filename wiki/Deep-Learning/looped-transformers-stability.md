# Looped Transformers 稳定性与泛化

> Sources: Asher Labovich, 2026-04
> Raw: [../../raw/Deep-Learning/2026-labovich-looped-transformers-stability.md](../../raw/Deep-Learning/2026-labovich-looped-transformers-stability.md); [../../raw/Deep-Learning/2026-W19-deep-learning.md](../../raw/Deep-Learning/2026-W19-deep-learning.md) (编译参考)

## Overview

提出基于 fixed-point 的框架分析 looped transformers 的稳定性，从三个维度考察：reachability（可达性）、input-dependence（输入依赖性）、geometry（几何稳定性）。理论证明没有 recall 的 looped network 只有 countable fixed points，无法实现强 input-dependence。提出 internal recall 新变体，在 sudoku 上远超标准 recall placement。

## 三个稳定性轴

| 维度 | 含义 | 结论 |
|------|------|------|
| Reachability | fixed point 能否被到达 | recall 是必要条件 |
| Input-Dependence | 输出对输入的敏感程度 | recall + outer normalization 最可靠 |
| Geometry | 损失景观的局部平滑性 | 影响反向传播稳定性 |

## 核心发现

recall + outer normalization 是最可靠的组合，能让 fixed point 同时满足可达、局部平滑、反向传播稳定。实验在 chess、sudoku、prefix-sums 上验证了理论预测。

## 关联

Looped Transformers 是 test-time compute scaling 的重要载体。理解其稳定性理论对设计可扩展的推理时计算策略至关重要。

## See Also

- [Transformer Architecture](../Deep-Learning/transformer-architecture.md)
- [Mamba-3 状态空间模型](../Deep-Learning/mamba-3-state-space-models.md)
