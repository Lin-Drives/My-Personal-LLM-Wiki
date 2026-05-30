# The Geometry of Multi-Task Grokking: Transverse Instability, Superposition, and Weight Decay Phase Structure

> Source: https://arxiv.org/abs/2602.18523
> Collected: 2026-05-31
> Published: 2026-02-19 (v1), revised 2026-04-03 (v3)

**Author:** Yongzhong Xu

## Abstract

The paper extends the geometric analysis of grokking from single-task to multi-task settings. The researcher trains shared-trunk Transformers on dual-task (mod-add + mod-mul) and triple-task (mod-add + mod-mul + mod-sq) modular arithmetic targets, conducting systematic weight decay scans. The paper reports five consistent phenomena: (1) staggered grokking order — multiplication generalizes first, followed by squaring, then addition; (2) universal integrability — optimization trajectories are confined to a low-dimensional execution manifold; (3) weight decay phase structure — grokking timescale and other metrics vary systematically with weight decay; (4) holographic incompressibility — final solutions occupy only 4-8 principal directions but are distributed across full-rank weights and are difficult to compress; (5) transverse fragility and redundancy — removing less than 10% of orthogonal gradient components eliminates grokking, but dual-task models partially recover under extreme deletion. These results support a dynamical picture where multi-task grokking constructs a compact superposition subspace in parameter space.
