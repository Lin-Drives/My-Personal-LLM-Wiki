# CacheGen: KV Cache Compression and Streaming for Fast Large Language Model Serving

> Source: https://arxiv.org/abs/2310.07240
> Collected: 2026-05-31
> Published: 2023-10-11 (v1), SIGCOMM 2024

**Authors:** Yuhan Liu, Hanchen Li, Yihua Cheng, Siddhant Ray, Yuyang Huang, Qizheng Zhang, Kuntai Du, Jiayi Yao, Shan Lu, Ganesh Ananthanarayanan, Michael Maire, Henry Hoffmann, Ari Holtzman, Junchen Jiang

## Abstract

CacheGen is a fast context-loading module for LLM systems. The system uses a custom tensor encoder, leveraging the distribution characteristics of KV caches to encode them into a more compact bitstream representation, while dynamically adjusting compression levels for different parts based on available bandwidth. Compared to recent systems that reuse the KV cache, CacheGen reduces the KV cache size by 3.5-4.3x and reduces the total latency of fetching and processing in context by 3.2-3.7x, with negligible impact on LLM response quality. Code is open-sourced on GitHub.
