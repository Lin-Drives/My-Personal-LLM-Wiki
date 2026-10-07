---
type: Research Synthesis
title: 研究主线｜人类视频能减少哪些机器人训练数据需求？
description: 对照论文原文形成首轮问题驱动的证据与边界整理。
tags: [机器人, 研究主线]
status: draft
generated:
  by: codex
  at: 2026-10-07T03:05:02.185375+00:00
sources:
  - id: arxiv-2607.08436
    resource: ../../raw/Embodied-Intelligence/2607.08436.fulltext.md
  - id: arxiv-2609.39403
    resource: ../../raw/Embodied-Intelligence/2609.39403.fulltext.md
---

# 研究主线｜人类视频能减少哪些机器人训练数据需求？

## 来源

- [arxiv-2607.08436](../../raw/Embodied-Intelligence/2607.08436.fulltext.md)

- [arxiv-2609.39403](../../raw/Embodied-Intelligence/2609.39403.fulltext.md)

## 概述

> 自动研究首轮草稿，未独立核验；不是作者个人判断或完整领域综述。

人类视频可以提供可扩展的视觉和场景变化监督，但必须区分预训练规模、机器人动作监督与下游适配数据。当前核对的 EgoWAM 与 IronMind 都不能概括为“完全不需要机器人数据”。

## 比较与证据

### 阅读前需要知道

跨具身迁移要处理相机运动、身体形态和可执行动作的差异。人手在视频中的轨迹，不一定是机器人末端可以执行的动作；视频时长也不能直接换算成机器人演示条数。

### 原文证据

| 维度 | EgoWAM | IronMind |
|---|---|---|
| 数据组成 | 人类与机器人联合训练；原文 §4.3 明确列出 robot action loss 和 human/world 相关目标 | 摘要明确称超过 10,000 小时由第一人称人类视频与异构机器人数据组成，不能把总量全算成人类视频 |
| 迁移机制 | 比较世界预测目标；相机稳定的 3D flow 使用 Aria VIO，避免把头部运动当场景动力学 | 使用相机空间动作表示与人机动作维度语义对齐；数据引擎清理与重标注轨迹 |
| 推理时世界分支 | 世界预测训练分支被丢弃，执行动作预测 | 辅助预测分支在推理时移除；随后还包含目标机器人数据的 post-training |
| 当前证据位置 | PDF pp.1、3、5、8[^arxiv-2607.08436] | PDF pp.1、4、6；后训练数量尚待逐表核对[^arxiv-2609.39403] |

## 局限性

### 尚未确认与下一轮

下一轮逐项核对机器人数据的小时数或演示数、用途、任务数量、数据采集设备和对照预算，加入 EgoHumanoid-V2 与 λ₀。本轮未对所有表格数字及图像重建做独立核查，不收录“首个”“完全解决 embodiment gap”等优先权或绝对表述。

## 综合判断

更准确的问题是“减少了哪一阶段、哪一种监督”，而不是笼统问“人类视频替代了多少机器人数据”。至少分开记录：视觉表征预训练、轨迹标注或动作对齐、目标机器人后训练、任务专属演示。两篇工作的数据来源和评测不一致，不能据总视频时长比较样本效率。

IronMind 给出的是混合语料的规模化证据；EgoWAM 给出的是联合训练中预测目标如何影响可迁移性的证据。它们还没有构成在同一预算下“少用多少机器人数据”的统一结论。

## 延伸阅读

暂无已整理的关联阅读。

[^arxiv-2607.08436]: [PDF 原文提取](https://github.com/Lin-Drives/My-Personal-LLM-Wiki/blob/main/raw/Embodied-Intelligence/2607.08436.fulltext.md)；页码指提取文件中的 PDF page，具体阅读范围见正文。
[^arxiv-2609.39403]: [PDF 原文提取](https://github.com/Lin-Drives/My-Personal-LLM-Wiki/blob/main/raw/Embodied-Intelligence/2609.39403.fulltext.md)；页码指提取文件中的 PDF page，具体阅读范围见正文。
