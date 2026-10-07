---
type: Paper Note
title: 'RoboTwin-Phys：物理条件变化下的机器人策略评测'
description: 在仿真任务中检查物理条件变化对 WAM 与 VLA 的影响及证据边界。
tags: [世界模型, 机器人, 物理鲁棒性]
status: draft
arxiv_id: '2609.26292'
arxiv_version: v1
resource: https://arxiv.org/abs/2609.26292v1
generated:
  by: codex
  at: 2026-10-07T08:36:36.945100+00:00
sources:
  - id: paper
    resource: https://arxiv.org/abs/2609.26292v1
  - id: fulltext
    resource: ../../raw/World-Models/2609.26292.fulltext.md
---

# RoboTwin-Phys：物理条件变化下的机器人策略评测

> 模型生成的论文笔记，未独立核验，不代表仓库作者观点。阅读范围：本地 PDF 文本提取 pp.1–9 及 p.10 表 4 说明；未复现实验，未逐项核对表 4 全部数值。

## 问题与方法

外观和布局变化下表现良好，不能保证机器人在物体质量、摩擦或关节阻尼变化后仍然可靠。RoboTwin-Phys 在 RoboTwin-2.0 的 50 个仿真任务上引入 13 个属性的随机化；其中也包含几何和相机配置，不能全部称为纯动力学参数。参数按每次任务采样并在执行中保持固定，九个敏感任务采用专门的范围；专家规划先检查采样条件下任务是否可行。论文还提供超过 5,000 条带物理参数标注的专家演示。[^fulltext]

## 主要证据

论文比较 Fast-WAM、Motus、FACT、π0.5 和 Galaxea-VLA。表 1 中 Physical Random 成功率分别为 44.24%、39.60%、39.14%、31.60% 和 37.82%；Fast-WAM 的 Official Random 为 91.78%。每项任务的 Physical Random 评测包含 100 次 rollout。这说明物理条件变化能揭示传统外观随机化没有充分暴露的失败，但数值只适用于本文的仿真协议。证据位置：PDF p.6 表 1、pp.9–10 附录 D。[^fulltext]

## 局限性

模型解读：当前证据主要来自仿真；随机化同时改变动力学、几何和相机条件，因此成功率下降还不能直接归因为模型缺乏物理理解。基准分数引用既有公开评测，物理随机化由本文评测，配置是否完全一致尚待确认。参数在一次任务内固定，对运行中突变后的恢复和真机部署的支持仍有限。依据原文 PDF p.6 表 1、pp.8–9 的参数与评测说明，未独立核验。

## 与研究主线的关系

它为[世界模型可靠规划](../Research/world-model-reliability.md)提供压力测试维度，帮助区分视觉泛化与物理条件泛化；本文并未证明某种世界预测训练目标能消除这些失效。

[^fulltext]: [PDF 原文提取](https://github.com/Lin-Drives/My-Personal-LLM-Wiki/blob/main/raw/World-Models/2609.26292.fulltext.md)，PDF SHA-256 `aba2c21a1bc49bcefde600798ca16b02bf902297b996670729a914fc0d76aa61`。
