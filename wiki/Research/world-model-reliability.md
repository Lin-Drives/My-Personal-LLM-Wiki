---
type: Research Synthesis
title: 研究主线｜世界模型可靠规划：先分清预测目标与评测边界
description: 对照论文原文形成首轮问题驱动的证据与边界整理。
tags: [机器人, 研究主线]
status: draft
generated:
  by: codex
  at: 2026-10-07T03:05:02.185375+00:00
sources:
  - id: arxiv-2609.26292
    resource: ../../raw/World-Models/2609.26292.fulltext.md
  - id: arxiv-2607.08436
    resource: ../../raw/Embodied-Intelligence/2607.08436.fulltext.md
---

# 研究主线｜世界模型可靠规划：先分清预测目标与评测边界

## 来源

- [arxiv-2609.26292](../../raw/World-Models/2609.26292.fulltext.md)

- [arxiv-2607.08436](../../raw/Embodied-Intelligence/2607.08436.fulltext.md)

## 概述

> 自动研究首轮草稿，未独立核验；不是作者个人判断或完整领域综述。

世界模型的价值需要分开考察：预测目标是否帮助策略学习，以及策略在物理条件变化后是否仍可靠。训练时加入世界预测损失，不等于部署时已经实现模型预测控制；视觉或布局泛化，也不等于质量、摩擦变化下的动力学泛化。

## 比较与证据

### 阅读前需要知道

策略把观测映射为动作；动力学模型预测动作之后的状态变化。模型预测控制会比较候选动作的未来结果再执行，但世界预测也可以只作训练辅助目标。两者的推理开销和失效方式不同。

### 原文证据

| 工作 | 已核对的内容 | 证据位置与限制 |
|---|---|---|
| RoboTwin-Phys | 在 RoboTwin-2.0 的 50 任务平台上加入物理条件变化；13 个属性按 episode 采样，包含质量、摩擦和关节特性等；提供超过 5,000 条带参数的专家演示 | PDF pp.1–4、附录 p.8；13 个属性也包括几何与传感配置，不能全部称为纯动力学参数；这是仿真评测，不能直接证明真机可靠性[^arxiv-2609.26292] |
| EgoWAM | 固定策略骨干、动作头和数据混合，比较 Pixel、DINO 与 3D motion flow 预测目标；预测分支在推理时弃用 | PDF p.1、p.3、§4.3 p.5；是辅助世界预测促进策略训练的证据，不是在线搜索规划证据[^arxiv-2607.08436] |

## 局限性

### 尚未确认与下一轮

尚未核对 RoboTwin-Phys 所有方法的逐任务结果，也未复现实验。尚缺长时程误差累积、闭环重规划和真机接触变化的统一比较。下一轮加入 V-JEPA 2 与其他动作条件模型，建立训练辅助预测和在线规划的对照表。本稿不是三个问题中的最终答案。

## 综合判断

两篇论文回答的是互补问题。EgoWAM 帮助选择可迁移的训练信号，RoboTwin-Phys 提供检查物理条件变化的评测维度。不能跨论文直接推出“DINO 目标就能抵抗摩擦变化”，因为任务、机器人与训练条件没有对齐。

实际阅读新论文时，先记录预测空间、动作是否进入预测、部署时是否执行预测，再记录时间跨度、物理扰动和异常恢复。成功率只在对应任务与评测协议内比较。

## 延伸阅读

[RoboTwin-Phys](../World-Models/robotwin-phys.md)：方法、主要结果与简短局限性随独立笔记维护。历史雷达同步展示笔记中的局限性。

[^arxiv-2609.26292]: [PDF 原文提取](https://github.com/Lin-Drives/My-Personal-LLM-Wiki/blob/main/raw/World-Models/2609.26292.fulltext.md)；页码指提取文件中的 PDF page，具体阅读范围见正文。
[^arxiv-2607.08436]: [PDF 原文提取](https://github.com/Lin-Drives/My-Personal-LLM-Wiki/blob/main/raw/Embodied-Intelligence/2607.08436.fulltext.md)；页码指提取文件中的 PDF page，具体阅读范围见正文。
