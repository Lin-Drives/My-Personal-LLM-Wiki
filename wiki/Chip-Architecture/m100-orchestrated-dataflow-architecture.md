# M100: 编排式数据流架构

> Sources: Xie et al. (理想汽车), ISCA 2026
> Raw: [../../raw/Chip-Architecture/2026-xie-m100-orchestrated-dataflow-isca.md](../../raw/Chip-Architecture/2026-xie-m100-orchestrated-dataflow-isca.md); [../../raw/Chip-Architecture/m100-li-auto-dataflow-architecture.md](../../raw/Chip-Architecture/m100-li-auto-dataflow-architecture.md) (编译参考)

## Overview

M100 是理想汽车自研的车端 AI 推理芯片（399.8mm², TSMC N5A），目标同时覆盖自动驾驶（UniAD/MindVLA）、大语言模型（LLaMA2-7B）和智能座舱。核心思路是在 GPGPU（通用贵）和 DSA（高效但僵化）之间找中间地带，提出了编排式数据流架构——编译器协同调度数据在时空上的流动，硬件保持简洁。

## 六大设计原则

1. **数据驱动并行执行** — 张量操作指令分发到执行单元，数据到位即触发计算
2. **编译器-架构协同设计** — 编译器编排的不只是计算，更是跨时空的数据移动
3. **消除多级缓存** — 张量计算由编译器+运行时管理的数据流驱动
4. **张量级操作粒度** — 张量作为调度/发射/执行的基本数据元素
5. **生产者-消费者同步** — 基于同步计数器(SC)，硬件级最小开销
6. **集中式指令分发** — 通过 ICB 菊花链广播张量操作指令

## 硬件架构

| 模块 | 规格 |
|------|------|
| NPU 计算 | 14 TPB Clusters × 4 TPBs，共 56 个计算核心 |
| 互连 | 2D Mesh (256GB/s) + Data Ring Bus (256GB/s) + Instruction Chain Bus |
| CCB 控制 | 4核 SiFive X280 RISC-V + 32MB SRAM |
| 内存 | 8×LPDDR5X, 64GB, 273 GB/s |
| CPU | 24核 ARM Cortex-A78AE |

单个 TPB 内: TCU (8×64 MAC 阵列) + CVU (可配置向量单元) + HBSM (2MB 共享 SRAM, 32 banks)

## 性能对比 vs NVIDIA Thor-U

UniAD 端到端自动驾驶:
- M100: 30 FPS — 满足实时要求
- Thor-U: 7.9 FPS — 不满足
- 加速比: 3.8× 总体，个别模块达 6.3×

LLaMA2-7B Decode: 两者相当（受限于相同 DDR 带宽）；Prefill: M100 1.95× 加速。

## 软件栈

三层编译器: PyTorch/TF/JAX → Space-Time Scheduler → Graph Compiler → Backend Compiler → M100 IR。运行时含 JIT 编译生成优化的 TPB 指令。

## See Also

- [理想 M100 NPU 架构详解](../Chip-Architecture/m100-npu-details.md)
