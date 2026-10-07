---
type: Research Synthesis
title: 世界模型综述
description: 整理世界模型综述的背景、主要内容与相关材料。
tags:
- 世界模型
status: draft
sources:
- id: raw-2024-ding-world-models-survey
  resource: ../../raw/World-Models/2024-ding-world-models-survey.md
- id: raw-2025-ding-world-models-survey
  resource: ../../raw/World-Models/2025-ding-world-models-survey.md
---

# 世界模型综述

## 来源

- [raw-2024-ding-world-models-survey](../../raw/World-Models/2024-ding-world-models-survey.md)

- [raw-2025-ding-world-models-survey](../../raw/World-Models/2025-ding-world-models-survey.md)

## 概述

> Sources: Ding et al., 2025 (ACM Computing Surveys)
> Raw: [../../raw/World-Models/2024-ding-world-models-survey.md](../../raw/World-Models/2024-ding-world-models-survey.md); [../../raw/World-Models/2025-ding-world-models-survey.md](../../raw/World-Models/2025-ding-world-models-survey.md) (编译参考)

首次系统地将世界模型文献按两大功能分类：Understanding（理解世界，构建内部表征来理解机制）和 Prediction（预测未来，预测未来状态指导决策）。梳理了生成游戏、自动驾驶、机器人、社会仿真四大应用领域，并呈现了认知派（JEPA，预测抽象表征）vs 生成派（Diffusion/AR，预测像素）的核心路线之争。

## 比较与证据

### 两大功能分类

| 功能 | 目标 | 代表工作 |
|------|------|---------|
| Understanding | 构建内部表征理解世界机制 | JEPA 系列、直观物理理解 |
| Prediction | 预测未来状态指导决策 | Dreamer、Sora、驾驶场景预测 |

### 四大应用领域

- 生成游戏 — AI 生成可交互的虚拟世界
- 自动驾驶 — 理解道路场景的时空演化
- 机器人 — 物理交互的模拟和规划
- 社会仿真 — 人类行为的建模和预测

### 两条路线

**认知派** (JEPA): 不生成像素，只预测表征空间中的未来。杨立昆坚持这条路线。
**生成派** (Diffusion/AR): 预测像素，可视化直观。业界主流。

### 作为入门的价值

定义了什么是世界模型 + 有哪些路线 + 谁在做什么。是从 Ha & Schmidhuber (2018) "World Models" 到 LeCun (2022) "A Path Towards Autonomous Machine Intelligence" 再到 Sora 的完整演进脉络的导航地图。

## 局限性

尚未整理局限性；未独立核验，不据缺少此节推断方法没有局限。

## 综合判断

待结合正文整理简短要点。

## 延伸阅读

- [JEPA 生态 2026](../World-Models/jepa-ecosystem-2026.md)
- [V-JEPA 2](../World-Models/v-jepa-2.md)
- [Causal-JEPA](../World-Models/causal-jepa.md)
