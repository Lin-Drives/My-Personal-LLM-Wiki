# Mamba-3: Improved Sequence Modeling using State Space Principles

> Source: https://arxiv.org/abs/2603.15569
> Collected: 2026-05-31
> Published: 2026-03-16 (ICLR 2026 Oral)

**Authors:** Aakash Lahoti, Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, Albert Gu

## Abstract

Transformer-based models deliver strong model quality but suffer from quadratic compute and linear memory issues. Mamba-3 focuses on scaling inference-time compute and improving inference efficiency, proposing three core improvements: (1) a more expressive recurrence derived from SSM discretization; (2) a complex-valued state update rule that enables richer state tracking; and (3) a multi-input, multi-output (MIMO) formulation that boosts performance without increasing decode latency. At the 1.5B scale, Mamba-3 improves average downstream accuracy by 0.6 percentage points compared to the next best model, with the MIMO variant further improving accuracy by another 1.2 points for a total 1.8 point gain. Mamba-3 achieves comparable perplexity to Mamba-2 despite using half of its predecessor's state size, advancing the performance-efficiency Pareto frontier.
