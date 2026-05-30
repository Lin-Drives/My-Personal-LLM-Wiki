# Noise Stability of Transformer Models

> Source: https://arxiv.org/abs/2602.08287
> Collected: 2026-05-31
> Published: 2026-02-09 (ICLR 2026)

**Authors:** Themistoklis Haris, Zihan Zhang, Yuichi Yoshida

## Abstract

Average sensitivity has two key limitations: it lacks a natural generalization to real-valued domains and fails to explain the input dependence seen in modern LLMs. The authors propose noise stability as an alternative simplicity metric, which expresses a model's robustness to correlated noise applied to all input coordinates simultaneously. They provide theoretical analysis for single-layer attention and ReLU MLP layers, and tackle the multi-layer propagation problem with a covariance interval propagation approach. Building on this theory, they develop a practical noise stability regularization method. Experiments show their regularizer consistently catalyzes grokking and accelerates training by approximately 35% and 75% respectively. The work sculpts a new connection between signal propagation in neural networks and interpretability.
