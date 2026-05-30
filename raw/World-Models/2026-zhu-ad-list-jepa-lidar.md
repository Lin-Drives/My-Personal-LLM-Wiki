# Self-Supervised JEPA-based World Models for LiDAR Occupancy Completion and Forecasting

> Source: https://arxiv.org/abs/2602.12540
> Collected: 2026-05-31
> Published: 2026-02-13

**Authors:** Haoran Zhu, Anna Choromanska (NYU)

## Abstract

The paper focuses on world models for autonomous driving learned in a self-supervised manner. It introduces AD-LiST-JEPA, which leverages a joint-embedding predictive architecture (JEPA) to model the spatiotemporal evolution of the environment from LiDAR data without requiring manual annotations. The method is evaluated on a downstream LiDAR-based occupancy completion and forecasting (OCF) task. Proof of concept experiments show better OCF performance with a pretrained encoder after JEPA-based world model learning. This represents the first systematic transfer of the JEPA paradigm from 2D vision/video to 3D sparse LiDAR point clouds, extending the JEPA family's reach to autonomous driving perception. The work uses SIGReg regularization (which outperforms variance regularization) and demonstrates data efficiency at both small and large pretraining dataset scales.
