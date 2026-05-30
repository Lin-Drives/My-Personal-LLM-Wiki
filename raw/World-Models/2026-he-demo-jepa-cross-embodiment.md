# Demo-JEPA: Joint-Embedding Predictive Architecture for One-shot Cross-Embodiment Imitation

> Source: https://arxiv.org/abs/2605.20811
> Collected: 2026-05-31
> Published: 2026-05-20

**Authors:** Jingyang He, Guangrun Li, Jieyu Zhang, Chengkai Hou, Zhengping Che, Shanghang Zhang

## Abstract

A core challenge in imitation learning is that actions are inherently embodiment-specific. Demo-JEPA decouples demonstration intent from embodiment-specific execution. It uses a JEPA-based world model to translate source visual demonstrations into target-compatible future latent trajectories. The target agent then treats these as subgoals and realizes them through planning under its own learned forward dynamics. The method avoids action-level correspondence and requires only visual demonstrations plus the target's own interaction data. Experiments on RLBench and real-world tasks show Demo-JEPA matches specialized in-domain planners and generalizes to unseen tasks where prior approaches fail. Uses VJEPA2.1 as the action-conditioned world model backbone.
