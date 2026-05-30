# Compiler-First State Space Duality and Portable O(1) Autoregressive Caching for Inference

> Source: https://arxiv.org/abs/2603.09555
> Collected: 2026-05-31
> Published: 2026-03-10

**Author:** Cosmo Santoni

## Abstract

State-space model releases are typically coupled to fused CUDA and Triton kernels, inheriting a hard dependency on NVIDIA hardware. The author demonstrates that Mamba-2's state space duality algorithm is a natural fit for what XLA's optimization passes handle well, making custom kernels optional. The full inference pipeline (prefill and cached autoregressive decoding) is implemented using shaped standard primitives under XLA, without hand-written kernels. The implementation achieves portable O(1) state management via a compiled on-device cache, requiring no host synchronization. It runs on CPU, NVIDIA GPU, and Google Cloud TPU from a single JAX source. On TPU v6e across 130M-2.7B parameter scales, it reaches roughly 140 TFLOPS on single-stream prefill and up to 64% bandwidth utilization on decode. Greedy decoding matches the PyTorch/CUDA reference token-for-token across 64 steps.
