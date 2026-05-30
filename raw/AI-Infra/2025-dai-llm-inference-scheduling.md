# Throughput-Optimal Scheduling Algorithms for LLM Inference and AI Agents

> Source: https://arxiv.org/abs/2504.07347
> Collected: 2026-05-31
> Published: 2025-04-10 (v1), revised 2026-05-18 (v3)

**Authors:** J.G. Dai, Tianze Deng, Yueying Li, Tianyi Peng

## Abstract

The paper develops queueing fundamentals for LLM inference, analyzing throughput in LLM inference systems. The authors prove that a broad class of "work-conserving" scheduling algorithms achieve maximum throughput for both individual requests and AI-agent workloads involving DAG and fork-join routing patterns. They establish work-conserving as a key design principle. Technically, they develop a fluid-limit framework for multi-class batched processing networks under K-FCFS scheduling. Evaluations confirm that Orca and Sarathi-Serve are throughput-optimal, while FasterTransformer and vanilla vLLM are not maximally stable. The analysis also explores how constraints like batch size limits and cyclic routing introduce further complexities.
