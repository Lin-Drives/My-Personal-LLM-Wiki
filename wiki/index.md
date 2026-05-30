# Knowledge Base Index

## AI-Infra

AI 基础设施：LLM 推理调度、分布式训练、KV Cache 管理。

| Article | Summary | Updated |
|---------|---------|---------|
| [LLM 推理调度理论](AI-Infra/llm-inference-scheduling.md) | SLAI 调度器以排队论证明吞吐量最优性，高负载下 TTFT 降低 53% | 2026-05-31 |
| [分布式并行策略](AI-Infra/distributed-training-parallelism.md) | DP/TP/PP/SP/EP 五种并行策略的通信模式与适用场景全景 | 2026-05-31 |
| [KV Cache 管理](AI-Infra/kv-cache-management.md) | PagedAttention→RadixTree→CacheGen 的 KV Cache 技术栈演进 | 2026-05-31 |

## Chip-Architecture

AI 芯片架构与设计。

| Article | Summary | Updated |
|---------|---------|---------|
| [M100 编排式数据流架构](Chip-Architecture/m100-orchestrated-dataflow-architecture.md) | 理想汽车自研车端 AI 推理芯片，UniAD 实时性能 3.8× NVIDIA Thor-U | 2026-05-31 |

## Deep-Learning

深度学习基础理论与架构。

| Article | Summary | Updated |
|---------|---------|---------|
| [Transformer Architecture](Deep-Learning/transformer-architecture.md) | 基于自注意力机制的序列建模架构，替代 RNN 实现并行化训练，是现代 LLM 的基础 | 2026-05-30 |
| [Mamba-3 状态空间模型](Deep-Learning/mamba-3-state-space-models.md) | ICLR 2026 Oral，complex-valued recurrence + MIMO，SSM 路线的里程碑 | 2026-05-31 |
| [Looped Transformers 稳定性](Deep-Learning/looped-transformers-stability.md) | Fixed-point 框架分析 looped transformers 三轴稳定性，internal recall 新变体 | 2026-05-31 |
| [Noise Stability 正则化](Deep-Learning/noise-stability-regularization.md) | 替代 average sensitivity 的新指标，训练加速 35-75% | 2026-05-31 |
| [K-PINN](Deep-Learning/k-pinn-lattice-boltzmann.md) | 介观 Lattice-Boltzmann 方程嵌入 PINN，误差降低 50-75% | 2026-05-31 |
| [Solver-in-the-Loop DeepONets](Deep-Learning/solver-in-the-loop-deeponet.md) | 数值求解器进入训练循环，训练速度提升 100x | 2026-05-31 |
| [PINN/KAN 生态 2026](Deep-Learning/pinn-ecosystem-2026.md) | PIKAN 家族、hard constraint 路线、operator learning 效率革命 | 2026-05-31 |

## Reinforcement-Learning

强化学习理论与应用。

| Article | Summary | Updated |
|---------|---------|---------|
| [AlphaGo](Reinforcement-Learning/alphago.md) | DeepMind 结合深度神经网络与 MCTS 的围棋程序，首个击败人类职业选手的 AI | 2026-05-30 |

## World-Models

世界模型：JEPA、预测未来、机器人规划。

| Article | Summary | Updated |
|---------|---------|---------|
| [世界模型综述](World-Models/world-models-survey.md) | Understanding vs Prediction 两大功能分类，四大应用领域，认知派 vs 生成派路线之争 | 2026-05-31 |
| [V-JEPA 2](World-Models/v-jepa-2.md) | 百万小时视频预训练→62h 机器人微调→零样本机械臂控制，LeCun 团队的实证落地 | 2026-05-31 |
| [Causal-JEPA](World-Models/causal-jepa.md) | 物体级掩码干预注入因果偏置，反事实推理提升 20%，JEPA 走向因果理解 | 2026-05-31 |
| [JEPA 生态 2026](World-Models/jepa-ecosystem-2026.md) | I-JEPA→V-JEPA→C-JEPA→AD-LiST-JEPA 演进全景 + 工程配方 | 2026-05-31 |
| [World Action Models](World-Models/world-action-models.md) | DreamZero/Fast-WAM/Cosmos Policy 从预测世界到可执行动作的范式转变 | 2026-05-31 |
