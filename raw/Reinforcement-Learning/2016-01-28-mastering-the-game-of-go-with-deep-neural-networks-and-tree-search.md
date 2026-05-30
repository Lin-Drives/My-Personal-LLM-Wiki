# Mastering the Game of Go with Deep Neural Networks and Tree Search

> Source: Nature, Vol 529, pp 484-489, doi:10.1038/nature16961
> Collected: 2026-05-30
> Published: 2016-01-28

**Authors:** David Silver*, Aja Huang*, Chris J. Maddison, Arthur Guez, Laurent Sifre, George van den Driessche, Julian Schrittwieser, Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, Sander Dieleman, Dominik Grewe, John Nham, Nal Kalchbrenner, Ilya Sutskever, Timothy Lillicrap, Madeleine Leach, Koray Kavukcuoglu, Thore Graepel, Demis Hassabis (Google DeepMind / Google)

## Abstract

The game of Go has long been viewed as the most challenging of classic games for artificial intelligence owing to its enormous search space (b ≈ 250, d ≈ 150) and the difficulty of evaluating board positions and moves. Here we introduce a new approach to computer Go that uses 'value networks' to evaluate board positions and 'policy networks' to select moves. These deep neural networks are trained by a novel combination of supervised learning from human expert games, and reinforcement learning from games of self-play. Without any lookahead search, the neural networks play Go at the level of state-of-the-art Monte Carlo tree search programs that simulate thousands of random games of self-play. We also introduce a new search algorithm that combines Monte Carlo simulation with value and policy networks. Using this search algorithm, our program AlphaGo achieved a 99.8% winning rate against other Go programs, and defeated the human European Go champion by 5 games to 0. This is the first time that a computer program has defeated a human professional player in the full-sized game of Go, a feat previously thought to be at least a decade away.

## Background

All games of perfect information have an optimal value function, v*(s), which determines the outcome of the game from every board position under perfect play. These games may be solved by recursively computing the optimal value function in a search tree containing approximately b^d possible sequences of moves.

In large games like Go (b ≈ 250, d ≈ 150), exhaustive search is infeasible, but the effective search space can be reduced by two general principles:
- **Position evaluation**: truncating the search tree at state s and replacing the subtree by an approximate value function v(s) ≈ v*(s)
- **Action sampling**: sampling actions from a policy p(a|s) to reduce search breadth

Monte Carlo tree search (MCTS) uses Monte Carlo rollouts to estimate the value of each state in a search tree. The strongest Go programs prior to AlphaGo were based on MCTS enhanced by policies trained to predict human expert moves. However, prior work was limited to shallow policies or linear value functions.

## Training Pipeline

AlphaGo trains neural networks using a pipeline consisting of several stages:

### 1. Supervised Learning (SL) Policy Network

Train a 13-layer convolutional policy network p_σ from 30 million positions from the KGS Go Server to predict human expert moves. Achieved 57.0% test accuracy (vs 44.4% prior state-of-the-art). Also trained a fast rollout policy p_π with linear softmax of small pattern features (24.2% accuracy, 2 μs per action vs 3 ms for policy network).

### 2. Reinforcement Learning (RL) Policy Network

Improve policy network by policy gradient RL. The RL policy network p_ρ is identical in structure to the SL policy network. Weights are initialized to SL values (ρ = σ). Games are played between current policy and a randomly selected previous iteration to prevent overfitting. Updates maximize expected outcome (+1 win, -1 loss).

Results: RL policy network won >80% against SL policy network. Using no search at all, RL policy network won 85% against Pachi (a strong Monte Carlo search program ranked 2 amateur dan).

### 3. Value Network Training

Train a value network v_θ to predict expected outcome from positions of games played by the RL policy network against itself. The network has similar architecture to policy network but outputs a single prediction (scalar value) instead of probability distribution.

Key challenge: training on complete games leads to overfitting because successive positions are strongly correlated. Solution: generate 30 million distinct positions, each sampled from a separate self-play game. This reduced test set MSE from 0.37 to 0.234, indicating minimal overfitting.

A single evaluation of v_θ(s) approached the accuracy of Monte Carlo rollouts using the RL policy network p_ρ, but using **15,000 times** less computation.

## MCTS in AlphaGo

AlphaGo combines policy and value networks in an MCTS algorithm. Each edge (s, a) stores action value Q(s, a), visit count N(s, a), and prior probability P(s, a).

At each time step t of each simulation, an action is selected by:
a_t = argmax_a (Q(s_t, a) + u(s_t, a))
u(s, a) ∝ P(s, a) / (1 + N(s, a))

When a leaf node s_L is reached:
- Leaf position is processed by SL policy network p_σ; output probabilities stored as priors P(s, a) = p_σ(a|s)
- Leaf evaluated in two ways:
  1. Value network v_θ(s_L)
  2. Random rollout using fast rollout policy p_π until termination
- Combined: V(s_L) = (1 - λ) v_θ(s_L) + λ z_L (mixing parameter λ)

After simulation, all traversed edges accumulate visit count and mean evaluation. The algorithm chooses the most visited move from the root.

Important finding: The SL policy network p_σ performed **better** in AlphaGo than the stronger RL policy network p_ρ, presumably because humans select a diverse beam of promising moves, whereas RL optimizes for the single best move. However, the value function derived from the stronger RL policy network performed better.

AlphaGo used 40 search threads, 48 CPUs, and 8 GPUs. The distributed version used 40 search threads, 1,202 CPUs and 176 GPUs.

## Results

### Against Other Programs

Single-machine AlphaGo won 494 out of 495 games (99.8%) against other Go programs (Crazy Stone, Zen, Pachi, Fuego, GnuGo). With four handicap stones, AlphaGo won 77% against Crazy Stone, 86% against Zen, and 99% against Pachi. The distributed version was significantly stronger, winning 77% of games against single-machine AlphaGo.

### Ablation

- Value network only (λ = 0): exceeded all other Go programs
- Rollouts only (λ = 1): competitive
- Mixed evaluation (λ = 0.5): performed best, winning ≥95% against other variants

This suggests value network and rollouts are complementary: the value network approximates games played by the strong but slow p_ρ, while rollouts precisely evaluate the weaker but faster rollout policy p_π.

### Match Against Fan Hui (European Champion)

AlphaGo defeated Fan Hui (professional 2 dan, European Go champion 2013-2015) 5 games to 0 in a formal match (5-9 October 2015). This was the first time a computer program defeated a human professional player in the full game of Go.

## Discussion

AlphaGo evaluated thousands of times fewer positions than Deep Blue did in its chess match against Kasparov; compensating by selecting positions more intelligently using the policy network, and evaluating them more precisely using the value network — an approach perhaps closer to how humans play. Furthermore, while Deep Blue relied on a handcrafted evaluation function, AlphaGo's neural networks are trained directly from gameplay purely through general-purpose supervised and reinforcement learning methods.

By combining tree search with policy and value networks, AlphaGo reached a professional level in Go, providing hope that human-level performance can be achieved in other seemingly intractable AI domains.

## Methods

**Asynchronous Policy and Value MCTS (APV-MCTS):** The search algorithm uses virtual loss to discourage parallel threads from exploring identical variations. Policy networks and value networks are computed asynchronously on GPUs.

**Symmetries:** AlphaGo exploits symmetries using a dynamic transformation approach — randomly selecting a single rotation/reflection for each evaluation and letting the search average over evaluations (implicit symmetry ensemble), rather than using rotationally invariant filters.

**Policy Network Architecture:** 13-layer CNN. Input: 19x19x48 feature planes. First layer: 5x5 conv. Layers 2-12: 3x3 conv. Output: 1x1 conv + softmax over all legal moves. Match version used k=192 filters.

**Value Network Architecture:** Similar to policy network with additional feature plane for current player color. Hidden layers 2-11 identical to policy network, layer 12 additional convolution, layer 13 1x1 conv, layer 14 fully connected (256 ReLU units), output: single tanh unit.

**Key parameters (match version):** β (softmax temperature) = 0.67, λ (mixing) = 0.5, n_vl (virtual loss) = 3, n_thr (expansion threshold) = 40, c_puct = 5.
