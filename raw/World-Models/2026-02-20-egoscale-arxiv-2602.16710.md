---
title: EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data
authors: Ruijie Zheng, Dantong Niu, Yuqi Xie, Jing Wang, Mengda Xu, Yunfan Jiang, Fernando Castañeda, Fengyuan Hu, You Liang Tan, Letian Fu, Trevor Darrell, Furong Huang, Yuke Zhu, Danfei Xu, Linxi Fan
venue: arXiv preprint, 2026
date: 2026-02-20
url: https://arxiv.org/abs/2602.16710
topics: World-Models, Robotics, Egocentric Data, Human-to-Robot Transfer, Dexterous Manipulation
---

## Abstract

Human behavior is among the most scalable sources of data for learning physical intelligence, yet how to effectively leverage it for dexterous manipulation remains unclear. We present EgoScale, a human-to-dexterous-manipulation transfer framework built on large-scale egocentric human data. We train a Vision–Language–Action (VLA) model on over 20,854 hours of action-labeled egocentric human video, more than 20× larger than prior efforts, and uncover a log-linear scaling law between human data scale and validation loss. This validation loss strongly correlates with downstream real robot performance, establishing large-scale human data as a predictable supervision source. Beyond scale, we introduce a simple two-stage transfer recipe: large-scale human pretraining followed by lightweight aligned human-robot mid-training. This enables strong long-horizon dexterous manipulation and one-shot task adaptation with minimal robot supervision. Our final policy improves average success rate by 54% over a no-pretraining baseline using a 22-DoF dexterous robotic hand, and transfers effectively to robots with lower-DoF hands.

## Key Points

- **20,854 hours** of egocentric human video — 20× larger than prior human-to-robot transfer datasets
- **Log-linear scaling law**: L = 0.024 − 0.003 × ln(D), R² = 0.9983 — validation loss predicts real-robot performance
- **Three-stage pipeline**: (I) Human pretraining → (II) Aligned mid-training (50h human + 4h robot) → (III) Task-specific fine-tuning
- **Flow-based VLA architecture**: Shared ViT/DiT backbone + lightweight embodiment MLP adapters for multi-robot support
- **Wrist action representation**: Relative SE(3) transforms eliminate global camera drift
- **Hand retargeting**: 21 human hand keypoints → 22-DoF Sharpa robotic hand via nonlinear optimization
- **Results**: 54% improvement over no-pretraining baseline, one-shot task adaptation, effective transfer to lower-DoF robots
- **Real robot**: Galaxea R1Pro humanoid with 22-DoF Sharpa hands

## Links

- PDF: [2026-02-20-egoscale-arxiv-2602.16710.pdf](../raw/World-Models/2026-02-20-egoscale-arxiv-2602.16710.pdf)
- arXiv: https://arxiv.org/abs/2602.16710
- Website: https://research.nvidia.com/labs/gear/egoscale/
