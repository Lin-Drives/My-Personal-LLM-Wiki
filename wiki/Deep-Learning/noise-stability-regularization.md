# Noise Stability 正则化

> Sources: Themistoklis Haris, 2026-02
> Raw: [../../raw/Deep-Learning/2026-haris-noise-stability-transformers.md](../../raw/Deep-Learning/2026-haris-noise-stability-transformers.md); [../../raw/Deep-Learning/2026-W19-deep-learning.md](../../raw/Deep-Learning/2026-W19-deep-learning.md) (编译参考)

## Overview

提出 noise stability 作为衡量深度学习 simplicity bias 的新指标，替代传统的 average sensitivity。noise stability 衡量模型对 correlated noise（同时作用于所有输入坐标）的鲁棒性，而非独立噪声。开发了实用的 noise stability regularization 方法，在 algorithmic tasks 上促进 grokking，next-token prediction 任务加速训练约 35-75%。

## 与 Average Sensitivity 的区别

传统 sensitivity 衡量单个输入坐标扰动的影响。noise stability 考察所有坐标同时受扰动的场景——更接近真实数据中的分布偏移。

## 方法论

利用 covariance interval propagation 处理多层网络中的噪声传播。对单层 attention 和 ReLU MLP 进行了理论分析。

## 实用价值

可直接作为 regularizer 加入训练，不需要额外标注或数据增强。35-75% 的训练加速是显著的工程收益。

## See Also

- [Looped Transformers 稳定性](../Deep-Learning/looped-transformers-stability.md)
