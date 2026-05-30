# AlphaGo

> Sources: Silver et al., 2016-01-28
> Raw: [../../raw/Reinforcement-Learning/2016-01-28-mastering-the-game-of-go-with-deep-neural-networks-and-tree-search.md](../../raw/Reinforcement-Learning/2016-01-28-mastering-the-game-of-go-with-deep-neural-networks-and-tree-search.md)

## Overview

AlphaGo is a computer Go program developed by Google DeepMind that combines deep neural networks with Monte Carlo tree search (MCTS). It was the first program to defeat a human professional player in the full-sized game of Go (19x19 board), a milestone previously thought to be at least a decade away. In October 2015, AlphaGo defeated European Go champion Fan Hui 5-0, and later in March 2016 defeated world champion Lee Sedol 4-1.

## The Go Challenge

Go is significantly harder than chess for AI:

| | Chess | Go |
|--|-------|-----|
| Branching factor (b) | ~35 | ~250 |
| Game length (d) | ~80 | ~150 |
| Search space | b^d | b^d |

The enormous search space makes exhaustive search infeasible. Prior to AlphaGo, the strongest Go programs used MCTS with shallow policies or linear value functions, reaching only strong amateur level.

## Training Pipeline

AlphaGo uses a four-stage training pipeline:

### Stage 1: Supervised Learning (SL) Policy Network

- 13-layer CNN trained on 30 million positions from the KGS Go Server
- Predicts human expert moves
- Accuracy: 57.0% (vs 44.4% prior state-of-the-art)
- Also trains a fast rollout policy p_π (24.2% accuracy, 2 μs/move)

### Stage 2: Reinforcement Learning (RL) Policy Network

- Initialize from SL policy network
- Play games against randomly selected previous versions of itself
- Policy gradient maximizes expected game outcome (+1/-1)
- Result: won >80% against SL policy; won 85% against Pachi (strong open-source program) with **no search at all**

### Stage 3: Value Network Training

- Predicts expected game outcome from a position under RL policy
- Similar CNN architecture to policy network, but outputs scalar value
- Key insight: training on complete games causes overfitting (MSE 0.37 test vs 0.19 train). Solution: sample one position per unique self-play game (30M positions)
- A single forward pass approaches the accuracy of Monte Carlo rollouts while using **15,000x less computation**

### Stage 4: MCTS Search

Combines policy and value networks in an asynchronous MCTS algorithm (APV-MCTS):

- Each edge stores: action value Q(s,a), visit count N(s,a), prior probability P(s,a)
- Action selection: a = argmax(Q(s,a) + u(s,a)), where bonus u(s,a) ∝ P(s,a)/(1+N(s,a)) encourages exploration
- Leaf evaluation: V(s) = (1-λ) * v_θ(s) + λ * z (rollout outcome), λ = 0.5
- Final move: select action with maximum visit count

## Key Design Decisions

**SL policy performed better than RL policy in search.** The SL policy network p_σ outperformed the stronger RL policy network p_ρ when used inside MCTS. Reason: humans select a diverse beam of promising moves, whereas RL optimizes for the single best move. The value function, however, benefited from using the stronger RL policy.

**Mixed evaluation is best.** Pure value network (λ=0) and pure rollouts (λ=1) are both viable, but combining them (λ=0.5) wins ≥95% against either variant. The two are complementary: value network approximates the strong but slow RL policy, rollouts precisely score the weaker but faster rollout policy.

**Implicit symmetry ensemble.** Rather than using rotationally invariant filters, AlphaGo randomly selects one of 8 symmetries (dihedral group) per evaluation and lets MCTS average over the evaluations.

## Compute Scale

| Version | Search Threads | CPUs | GPUs |
|---------|---------------|------|------|
| Single-machine | 40 | 48 | 8 |
| Distributed | 40 | 1,202 | 176 |

## Results

- **99.8%** win rate against other Go programs (Crazy Stone, Zen, Pachi, Fuego, GnuGo)
- **5-0** against European champion Fan Hui (Oct 2015)
- Distributed version won 77% against single-machine AlphaGo

## Significance

AlphaGo was one of AI's "grand challenges." Notable comparisons:

- Evaluated **thousands of times fewer** positions than Deep Blue did in chess — compensating by selecting and evaluating positions more intelligently
- Unlike Deep Blue's handcrafted evaluation function, AlphaGo's neural networks were trained purely from gameplay through general-purpose supervised and reinforcement learning methods
- The combination of tree search + neural networks created a template later applied to other domains (general game-playing, planning, scheduling)

## See Also

- [MCTS Fundamentals](../Reinforcement-Learning/mcts-fundamentals.md)
