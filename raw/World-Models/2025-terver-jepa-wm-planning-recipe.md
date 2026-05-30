# What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?

> Source: https://arxiv.org/abs/2512.24497
> Collected: 2026-05-31
> Published: 2025-12-30 (v1), revised 2026-05-18 (v3). Accepted at TMLR.

**Authors:** Basile Terver, Tsung-Yen Yang, Jean Ponce, Adrien Bardes, Yann LeCun

## Abstract

The paper addresses the challenge of developing AI agents that can solve diverse physical tasks and generalize to new ones. The approach involves training a world model from state-action trajectories then using it with a planning algorithm. The authors characterize a family of models as JEPA-WMs and investigate technical choices that make algorithms from this class work. They study model architecture, training objectives, and planning algorithms across simulated and real-world robotic data. Their proposed model outperforms two established baselines, DINO-WM and V-JEPA-2-AC, in both navigation and manipulation tasks. Key findings: RoPE + sequence conditioning is most robust across tasks; AdaLN prevents action information from vanishing in deep networks.
