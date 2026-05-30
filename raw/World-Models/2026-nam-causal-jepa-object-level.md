# Causal-JEPA: Learning World Models through Object-Level Latent Masking

> Source: https://arxiv.org/abs/2602.11389
> Collected: 2026-05-31
> Published: 2026-02-11 (v1), revised 2026-05-28 (v2). ICML 2026.

**Authors:** Heejeong Nam, Quentin Le Lidec, Lucas Maes, Yann LeCun, Randall Balestriero

## Abstract

C-JEPA is a simple and flexible object-centric world model that extends masked joint embedding prediction from image patches to object-centric representations. By masking object-level latents, the method imposes structured partial observability during training, creating counterfactual-like prediction queries to avoid shortcuts. Empirically, the authors report an absolute improvement of about 20% in counterfactual reasoning over the same architecture without object-level masking. For agent control, C-JEPA enables substantially more efficient planning by using only 1% of the total latent input features compared to patch-based models with comparable performance. The work also includes a formal analysis demonstrating that object-level masking induces useful inductive bias by controlling observability. This represents a key upgrade in the JEPA family — from learning to predict to learning to understand causal interactions between objects.
