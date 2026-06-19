# Transformer 架构

> Sources: Vaswani et al., 2017-06-12
> Raw: [../../raw/Deep-Learning/2017-06-12-attention-is-all-you-need.md](../../raw/Deep-Learning/2017-06-12-attention-is-all-you-need.md)

## Overview

The Transformer is a neural network architecture introduced in the 2017 paper "Attention Is All You Need" that replaces recurrent neural networks (RNNs) with a self-attention mechanism for sequence transduction tasks. It enables significantly more parallelization during training, achieving state-of-the-art results on machine translation with a fraction of the training cost of RNN or CNN based approaches. The architecture became the foundation for virtually all subsequent large language models (GPT, BERT, Claude, etc.).

## Architecture

The Transformer follows an encoder-decoder structure:

- **Encoder:** N=6 identical layers, each with two sub-layers:
  1. Multi-head self-attention
  2. Position-wise feed-forward network
  - Each sub-layer has residual connection + layer normalization: LayerNorm(x + Sublayer(x))
  - Output dimension: d_model = 512

- **Decoder:** N=6 identical layers, each with three sub-layers:
  1. Masked multi-head self-attention (prevents attending to future positions)
  2. Multi-head attention over encoder output (encoder-decoder attention)
  3. Position-wise feed-forward network

### Scaled Dot-Product Attention

The core operation:

Attention(Q, K, V) = softmax(Q K^T / sqrt(d_k)) V

Key dimensions: queries and keys of dimension d_k, values of dimension d_v. The scaling factor 1/sqrt(d_k) prevents dot products from growing too large and pushing softmax into regions of extremely small gradients.

### Multi-Head Attention

Rather than performing a single attention function, the model projects queries, keys, and values h times with different learned linear projections, performs attention in parallel on each, then concatenates and projects the output:

MultiHead(Q, K, V) = Concat(head_1, ..., head_h) W^O

The paper uses h = 8 heads, each with d_k = d_v = d_model/h = 64. Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions.

### Position-wise Feed-Forward Networks

FFN(x) = max(0, x W_1 + b_1) W_2 + b_2

Input/output dimension: 512. Inner-layer dimension: 2048. Applied identically to each position, but with different parameters per layer.

### Positional Encoding

Since the model has no recurrence or convolution, position information must be injected. The paper uses sinusoidal functions:

PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

Learned positional embeddings produced nearly identical results, but sinusoidal encodings are used because they may allow extrapolation to unseen sequence lengths.

## Why Self-Attention Over RNNs/CNNs

Three comparison criteria:

|  | Self-Attention | Recurrent | Convolutional |
|--|---------------|-----------|---------------|
| Computational complexity | O(n^2 * d) | O(n * d^2) | O(k * n * d^2) |
| Sequential operations | O(1) | O(n) | O(1) |
| Max path length | O(1) | O(n) | O(log_k(n)) |

Self-attention provides constant-length paths between any two positions, making it easier to learn long-range dependencies. It's also faster than recurrent layers when n < d, which is typical for NLP.

## Training Details

| Setting | Base Model | Big Model |
|---------|-----------|-----------|
| d_model | 512 | 1024 |
| d_ff | 2048 | 4096 |
| h | 8 | 16 |
| P_drop | 0.1 | 0.3 |
| Training steps | 100K | 300K |
| Training time | 12 hours | 3.5 days |
| Hardware | 8 P100 GPUs | 8 P100 GPUs |

- **Optimizer:** Adam (beta_1=0.9, beta_2=0.98, epsilon=10^-9), with warmup (4000 steps) then inverse square root decay
- **Data:** WMT 2014 English-German (4.5M pairs) and English-French (36M pairs)
- **Regularization:** Residual dropout + label smoothing (epsilon_ls = 0.1)

## Key Results

| Task | Model | BLEU |
|------|-------|------|
| EN-DE | Transformer (big) | 28.4 |
| EN-FR | Transformer (big) | 41.0 |
| EN Parsing (WSJ) | Transformer (4 layers) | 91.3 F1 |
| EN Parsing (semi-supervised) | Transformer (4 layers) | 92.7 F1 |

On English-to-German, the big Transformer outperformed the best previous model including ensembles by over 2 BLEU.

## Ablation Insights

- Single-head attention is 0.9 BLEU worse than 8 heads; too many heads also degrades quality
- Reducing d_k hurts quality, suggesting dot-product compatibility benefits from sufficient dimensionality
- Bigger models (> d_ff, > h) consistently better, dropout essential against overfitting
- Sinusoidal positional encoding performs on par with learned embeddings

## Impact

This paper introduced the architecture that underpins GPT (decoder-only), BERT (encoder-only), and all modern LLMs. The self-attention mechanism's ability to capture long-range dependencies at constant computational path length made scaling to very large models practical.
