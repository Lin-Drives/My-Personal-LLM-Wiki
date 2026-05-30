# Stability and Generalization in Looped Transformers

> Source: https://arxiv.org/abs/2604.15259
> Collected: 2026-05-31
> Published: 2026-04-16

**Author:** Asher Labovich

## Abstract

Looped transformers promise test-time compute scaling by spending more iterations on harder problems, but it remains unclear which architectural choices enable extrapolation to harder problems at test time versus memorizing training-specific solutions. The author introduces a fixed-point based framework for analyzing looped architectures along three axes of stability — reachability, input-dependence, and geometry. The framework characterizes when fixed-point iteration yields meaningful predictions. Theoretically, looped networks without recall have countable fixed points and cannot achieve strong input-dependence at any spectral regime. In contrast, recall combined with outer normalization reliably produces a regime in which fixed points are simultaneously reachable, locally smooth in the input, and supported by stable backpropagation. Empirically, single-layer looped transformers trained on chess, sudoku, and prefix-sums show downstream performance tracking the framework's predictions. The author introduces internal recall, a novel recall placement variant that becomes substantially better than standard recall placement on sudoku once outer normalization is applied.
