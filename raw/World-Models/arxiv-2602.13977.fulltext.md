# arXiv:2602.13977 — PDF 原文文本提取

- Source: https://arxiv.org/abs/2602.13977
- Local PDF: `arxiv-2602.13977.pdf` (local only)
- PDF SHA-256: `342c6cfeee002d820a64e8b06e67b5dd422c199937d8988f98dc41d2e01e2c93`
- Converted at: 2026-10-06T23:51:13.232085+00:00
- Extractor: pypdf/6.10.0
- Pages: 21
- Pages without extractable text: none

> 逐页提取 PDF 文本，未使用模型改写或翻译，未进行内容核验。保留页码；多栏阅读顺序、公式、表格和图片可能不能准确还原。无文字页需要另行 OCR，不能视为完整文本覆盖。基础 ID 的具体版本尚未解析，以 PDF 哈希标识本次原文件。

## PDF page 1

```text
WoVR: World Models as Reliable Simulators for
Post-Training VLA Policies with RL
Zhennan Jiang2,3,4,* Shangqing Zhou2,3,* Yutong Jiang3 Zefang Huang4 Mingjie Wei4
Yuhui Chen2,3 Tianxing Zhou4 Zhen Guo5 Hao Lin5 Quanlu Zhang5
Yu Wang1 Haoran Li2,3, † Chao Yu1, † Dongbin Zhao2,3,4
∗Equal contribution †Corresponding authors
1Tsinghua university 2Institute of Automation, Chinese Academy of Sciences
3University of Chinese Academy of Sciences 4Zhongguancun Academy 5Infinigence AI
https://huggingface.co/Collections/RLinf/wovr
 https://github.com/RLinf/RLinf
Abstract:Reinforcement learning (RL) promises to unlock capabilities beyond
imitation learning for Vision–Language–Action (VLA) models, but its require-
ment for massive real-world interaction prevents direct deployment on physical
robots. Recent work attempts to use learned world models as simulators for policy
optimization, yet closed-loop imagined rollouts inevitably suffer from hallucina-
tion and long-horizon error accumulation. Such errors do not merely degrade vi-
sual fidelity—they corrupt the optimization signal, encouraging policies to exploit
model inaccuracies rather than genuine task progress. We propose WoVR, a reli-
able world-model-based reinforcement learning framework for post-training VLA
policies. Instead of assuming a faithful world model, WoVR explicitly regulates
how RL interacts with imperfect imagined dynamics. It improves rollout stability
through a controllable action-conditioned video world model, reshapes imagined
interaction to reduce effective error depth via Keyframe-Initialized Rollouts, and
maintains policy–simulator alignment through World Model-Policy co-evolution.
Extensive experiments on LIBERO benchmarks and real-world robotic manipu-
lation demonstrate that WoVR enables stable long-horizon imagined rollouts and
effective policy optimization, improving average LIBERO success from 39.95% to
69.2% (+29.3 points) and real-robot success from 61.7% to 91.7% (+30.0 points).
These results show that learned world models can serve as practical simulators for
reinforcement learning when hallucination is explicitly controlled.
1 Introduction
Vision–Language–Action (VLA) models [1, 2, 3, 4] have been increasingly adopted for robotic
manipulation, where actions are generated end-to-end by conditioning on language instructions and
visual observations. Most existing VLA systems are trained via imitation learning. While effective
in many downstream tasks, this paradigm fundamentally limits the performance ceiling of VLA
policies, as it is tightly constrained by the quality and coverage of demonstration data.
Recent studies have demonstrated that reinforcement learning for VLA [5, 6, 7, 8, 9, 10] can sub-
stantially improve policy performance and reduce reliance on imitation data [11]. However, most
approaches rely on standard on-policy optimization algorithms such as Proximal Policy Optimiza-
tion (PPO) [12] or Group Relative Policy Optimization (GRPO) [13, 14], which require large-scale
environment parallelism to achieve stable and efficient training. This requirement is impractical
for real-world robotic reinforcement learning, where physical robot interaction is expensive [15],
slow, and often requires substantial human supervision [16]. Although simulation-based alterna-
tives have been explored [7, 17], accurately aligning simulators with real-world dynamics remains
arXiv:2602.13977v1  [cs.RO]  15 Feb 2026
```

## PDF page 2

```text
·Stabilized Action-conditioned World Model
· Hallucination-Aware Policy Optimization in 
Imagination
· Policy-Aligned Co-Evolution Strategy
Hallucination in world model
Rollout in real world
Success in world model， 
fail in reality？ How to 
mitigate the hallucination?
WoVR
ΔSR
Average final SR
ΔSR
Real World Model
Real World Model
Use our WoVR
Figure 1:Hallucination in Closed-Loop World Model Rollouts.The world model imagines a
successful grasp (green frames), but real-world execution fails (red frames).To address this critical
mismatch, we propose three hallucination-aware mechanisms.
highly challenging, particularly for contact-rich manipulation tasks. These constraints motivate re-
placing real-environment interaction with a learned world model that serves as a simulator for policy
optimization.
Recent advances in large-scale generative video models [18, 19, 20] have made this direction in-
creasingly feasible. Several works directly treat pretrained video generators as simulators and per-
form reinforcement learning entirely in imagination [21, 22, 23].However, learned world models
are not faithful simulators.In this work, we definehallucinationas a systematic mismatch between
imagined and real outcomes in closed-loop interaction. The world model may produce visually plau-
sible rollouts while predicting physically incorrect state transitions or even spurious success signals
under the policy’s actions(Fig. 1).
Hallucination is not merely a generation artifact — it fundamentally undermines reinforcement
learning. In closed-loop autoregressive rollouts, prediction errors compound with horizon length
due to:
• Autoregressive feedback: the model conditions on its own generated frames, amplifying
small early errors;
• Distribution shift: as the policy evolves, its action distribution drifts away from the data
used to train the world model, increasing out-of-distribution prediction failures.
If hallucinated trajectories are directly used for policy optimization, reinforcement learning is in-
centivized to exploit systematic model errors rather than true task progress. This leads to a critical
question:
If world models inevitably hallucinate, how can reinforcement learning remain reliable under
imperfect imagined dynamics?
We argue that using world models for RL is not primarily a modeling problem, but a reliability prob-
lem. To make world-model-based reinforcement learning viable, one must control hallucination at
three interconnected levels: controllable simulator design, reliable interaction protocol, and pol-
icy–model alignment. To this end, we proposeWoVR, aWorld-model-based framework for post-
trainingVision–Language–Action policies withReinforcement Learning, built upon RLinf [24].
Rather than assuming the learned world model to be a faithful simulator, WoVR explicitly regulates
how reinforcement learning interacts with imperfect imagined dynamics. We first strengthen the
simulator itself by constructing a rollout-stable, action-controllable video world model with stabi-
lized autoregressive context modeling, reducing long-horizon drift and structural collapse. How-
ever, improving the simulator alone is insufficient, as prediction errors inevitably accumulate over
extended rollouts. We therefore reshape imagined interaction throughKeyframe-Initialized Roll-
outs (KIR), which shorten the effective prediction depth by initializing trajectories near task-critical
states, limiting the compounding of hallucination during learning. Finally, as policy optimization
shifts the action distribution and induces distribution mismatch between the policy and the world
2
```

## PDF page 3

```text
model, we introducePACE, a policy-aligned co-evolution strategy that restores alignment by itera-
tively refining the world model under the evolving policy distribution, without requiring continuous
online supervision. Together, these components form a unified hallucination-aware reinforcement
learning framework that enables reliable policy optimization in imagination.
In summary, our contributions are as follows.
• We identify hallucination under closed-loop imagined interaction as a fundamental reliabil-
ity challenge in world-model-based reinforcement learning for VLA, showing that autore-
gressive error accumulation and policy-induced distribution shift can systematically corrupt
optimization signals.
• We propose WoVR, a hallucination-aware reinforcement learning framework that jointly
regulates controllable simulator design, reliable imagined interaction, and a policy-aligned
co-evolution strategy, enabling stable on-policy optimization entirely in imagination.
• Extensive experiments demonstrate that WoVR achieves state-of-the-art world-model qual-
ity across perceptual and temporal metrics while maintaining high rollout efficiency (23
FPS). More importantly, WoVR delivers strong downstream task performance, improving
average LIBERO success from 39.95% to 69.2% (+29.3 points) and real-robot success from
61.7% to 91.7% (+30.0 points).
2 Related Work
2.1 Online RL Fine-tuning for VLA Models
On-policy reinforcement learning [5, 12] has been increasingly adopted to fine-tune VLA mod-
els beyond imitation learning [5, 6]. However, directly transferring online on-policy fine-tuning to
real robots remains impractical, as such methods require large-scale parallel rollouts, repeated en-
vironment resets, and tightly coupled policy–environment interaction, which are difficult to support
under real-world hardware. To mitigate this, some off-policy approaches [8, 25] introduce offline
data reuse or human intervention, but often suffer from limited scalability and performance degra-
dation during online updates. An alternative direction builds large-scale real-robot infrastructures,
yet existing systems [26, 27] still cannot practically support fully on-policy algorithms at scale.
These limitations suggest that the challenge of online RL for VLA is systemic rather than algorith-
mic, motivating world-model-based approaches that decouple policy optimization from real-world
interaction.
2.2 World Models
Recent progress in large-scale general-purpose world models [28, 29, 30, 31, 32, 33, 34] has demon-
strated strong long-horizon generation and spatial memory under large viewpoint changes. However,
these models rely on complex Self-Forcing/DMD training pipelines [35, 36, 37, 38, 39, 40], require
massive pretraining data, cannot be trained from scratch, and are primarily designed for navigation-
style tasks with mouse–keyboard control. In contrast, embodied manipulation exhibits fixed view-
points, locally constrained dynamics, and fine-grained object interactions, leading to fundamentally
different modeling objectives, data distributions, and inference requirements.
To address embodied settings, prior works adapt pretrained video models into action-conditioned
world models using projected end-effector position [41, 42], AdaLN-based frame-wise action injec-
tion [43, 22, 44, 45], cross-attention [46, 47], and MoE-based conditioning [48]. Despite improved
action responsiveness, these approaches commonly suffer from slow inference, severe error accu-
mulation in long-horizon autoregressive generation, and unstable modeling of fine-grained physical
interactions, limiting their scalability for reinforcement learning.
3
```

## PDF page 4

```text
2.3 World Models as Simulators
Many works have validated the correlation between VLA performance in real environments and
in learned world models [43, 46, 42, 49] , demonstrating the potential of world models for out-
of-distribution generalization [43], and exploring the use of WM-generated synthetic data to train
VLAs [46, 42]. However, these approaches do not treat world models as true simulators.
World-Env [21] and WMPO [22] take an important step toward treating learned world models as
simulators, aiming to avoid costly interaction with real environments during reinforcement learning.
Despite these advances, both approaches largely treat the world model as a drop-in replacement for a
standard simulator, mechanically coupling on-policy reinforcement learning with imagined rollouts.
They do not explicitly address the fundamental challenge of reinforcement learning under halluci-
nated dynamics, where closed-loop prediction errors accumulate and incentivize policies to exploit
model inaccuracies. As a result, these methods lack dedicated mechanisms to regulate rollout hori-
zons, suppress post-success hallucinations, or align policy optimization with the reliability regime
of the world model.
3 Preliminary
3.1 Reinforcement Learning for VLA Fine-tuning
Recent work has increasingly adopted reinforcement learning to post-train VLA policies beyond
imitation learning. In this setting, policy optimization is commonly formulated as a Markov De-
cision Process (MDP), defined by the tupleM= (O,A, P, R, γ). At each time stept, given a
visual observationo t ∈ Oand a language instructionl t, the VLA policy outputs a chunked action
at ∼π θ(· |o t, lt)∈ A, which induces a state transitiono t+1 ∼P(· |o t, at)and yields a scalar
rewardr t =R(o t, at). The goal of reinforcement learning is to maximize the expected discounted
return:
J(π θ) =E τ∼π θ
" TX
t=1
γt−1rt
#
,(1)
whereγ∈(0,1]is the discount factor.
Following standard on-policy reinforcement learning, the policy is optimized via a policy gradient
objective:
∇θJ(π θ) =E τ∼π θ
" TX
t=1
∇θ logπ θ(at |o t, lt)A(o t, at)
#
,(2)
whereA(o t, at)denotes the advantage function. In general, the advantage function is defined as
A(ot, at) =Q(o t, at)−V(o t),(3)
whereQ(o t, at)is the action-value function representing the expected return after taking actionat at
observationo t, andV(o t)is the state-value function estimating the expected return under the current
policy.
3.2 Problem Formulation
While on-policy reinforcement learning provides a principled framework for fine-tuning VLA poli-
cies, applying it directly in real-world robotic environments is often impractical due to high inter-
action cost and limited environment parallelism. To address this limitation, our goal is to replace
real-environment interaction with a learned world model that can serve as a simulator for policy
optimization.
We reformulate the original MDP as aWorld Model-MDP (WM-MDP), defined as
MWM = (O,A, ˆPϕ, ˆRψ, γ),(4)
4
```

## PDF page 5

```text
World Model
SFT
Real world
VLA
Base policy rollout 
Evolving policy rollout 
WMBase
Performance
RL with
WMBase
RL with
WMEvo
VLA
WMEvo
SFT
Imagined trajectories
World model
Keyframe-Initialized Rollouts
VLA
denotes masking post-success steps
/ denotes skipping early frames
DiT
1 Stabilized Action-Conditioned World Model
𝑙𝑙𝑡𝑡
 𝑂𝑂𝑡𝑡
Pick the 
bowl to 
the plate
First-frame-anchored 
context
Dual-channel action injection
Calculate 
reward
2 Hallucination-Aware Policy Optimization in Imagination
chunk-by-chunk generation 
reward model
3 Policy-Aligned Co-Evolution Strategy
World Model
VLA
Calculate 
advantage
Imagined rollout
 Group 1
Group n
World Model
Figure 2:Overview of WoVR. WoVR builds a reliability-driven reinforcement learning framework
entirely around the learned world model. It first strengthens the world model as a controllable
simulator, ensuring rollout-stable and action-responsive generation. On top of this simulator, it
designs a reliable interaction protocol via Keyframe-Initialized Rollouts (KIR) and masked GRPO
to reduce effective error depth and prevent optimization on hallucinated success. Finally, it maintains
policy–model alignment through PACE, which co-evolves the world model with the evolving policy
to mitigate distribution shift and preserve simulator reliability.
where the transition dynamics ˆPϕ(ot+1 |o t, at)are approximated by a learned world model param-
eterized byϕ, and ˆRψ(ot, at)denotes a reward function parameterized byψ.
InM WM, trajectories are generated by interacting with the world model rather than the physical
environment. Specifically, given an observationo t and an actiona t sampled from the policy, the
next observation and reward are obtained as
˜ot+1 ∼ ˆPϕ(· |o t, at),˜r t = ˆRψ(˜ot+1),(5)
which allows the policy to perform closed-loop rollouts entirely in imagination. Under this formu-
lation, the policy optimization objective remains unchanged in form:
JWM(πθ) =E τ∼π θ, ˆPϕ
" TX
t=1
γt−1ˆrt
#
.(6)
4 Methods
We propose WoVR, a reliability-driven world-model-based reinforcement learning framework for
post-training Vision–Language–Action (VLA) policies without requiring parallel real-world inter-
action. As illustrated in Fig. 2, WoVR treats the learned world model as a generative simulator
and builds the entire reinforcement learning pipeline around controlling hallucination in closed-loop
imagination.
Specifically, WoVR regulates reliability at three interconnected levels. (1) Simulator-level control:
we construct an action-controllable, rollout-stable video world model with dual-channel action in-
jection and first-frame anchoring to suppress long-horizon drift. (2) Interaction-level reshaping: we
redesign imagined interaction through Keyframe-Initialized Rollouts (KIR) and masked GRPO to
5
```

## PDF page 6

```text
1 Memory latents
1 Ref latent
2 Noise latents
1 Reference frame
4 Memory frames
8 Noisy frames
N 
  DiT blocks
𝛾𝛾1, 𝛽𝛽1
+ + +
𝛾𝛾2, 𝛽𝛽2 𝛼𝛼2𝛼𝛼1
+
Layer Norm
Scale, shift
Self - Attention
Scale
Layer Norm
Cross - Attention
Layer Norm
Scale, shift
FNN
Scale
generate autoregressively, chunk by chunk
Timestep Actions
MLP MLP
MLP
𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴− 𝑍𝑍𝑍𝑍𝑍𝑍𝑍𝑍
Figure 3:Architecture of the proposed action-conditioned world model.The world model is
built upon a video diffusion backbone and conditioned on actions via a dual-channel action injection
design, enabling frame-level controllability and stable chunk-by-chunk autoregressive generation for
long-horizon imagined rollouts.
reduce effective error depth and prevent optimization on hallucinated success. (3) Alignment-level
regulation: we introduce PACE, a policy–model co-evolution strategy that mitigates distribution
shift by periodically aligning the world model with the evolving policy.
Together, these components enable scalable and reliable on-policy optimization entirely in imagina-
tion.
4.1 Stabilized Action-Conditioned World Model
WoVR relies on a learned video world model as agenerative simulatorfor closed-loop imagined
interaction. However, long-horizon rollouts are prone to hallucination, where global scene structure
gradually drifts and the background collapses as the rollout length increases. We therefore design
the world model to be bothaction-controllableandrollout-stable, so that the simulated dynamics
remain consistent under iterative, policy-driven generation.
Backbone and action conditioning.Our world model is built upon the Wan2.2-TI2V-5B video
diffusion backbone [20]. Unlike conventional image-to-video generation, embodied simulation re-
quires explicit action conditioning to ensure that predicted state transitions respond causally to the
policy. To this end, we reformulate Wan2.2-TI2V into an action-conditioned generator via a dual-
channel action injection design (Fig. 3), which preserves the original DiT structure while enabling
frame-level controllability. Concretely, in each DiT block, action embeddings influence genera-
tion through two complementary pathways. First, action embeddings are fused with the diffusion
timestep embeddings and applied via AdaLN-Zero-style modulation, directly shaping the denoising
dynamics at the feature level. Second, we retain the original cross-attention operator but replace
textual embeddings with action embeddings, allowing actions to condition the network globally
across layers. Together, these two pathways provide both local modulation and global context for
action-conditioned video generation.
First-frame anchoring for rollout stability.Even with strong action conditioning, chunk-by-
chunk autoregressive generation can still accumulate errors, leading to spatial drift and gradual
background collapse. To suppress such long-horizon degradation, we adopt afirst-frame–anchored
inference context. At each autoregressive step, the model conditions on[o 0, o t′−c′:t′], which con-
catenates the episode’s initial reference frame with the most recent memory frames from the previous
chunk. This persistent reference constrains global appearance and scene layout, because many self-
attention heads naturally attend to the first frame during denoising (Fig. 4), consistent with prior
findings [50, 51, 31].
6
```

## PDF page 7

```text
Figure 4:Visualization of self attention probability map.During the denoising process, many
attention heads focus on the first frame of the sequence.
With dual-channel action conditioning and first-frame anchoring, we obtain a rollout-stable world
model that can be used as a generative simulator for closed-loop interaction. Starting from the first-
frame–anchored context[o 0, o t′−c′:t′], we first encode it into latent representations[z0, zt−c:t]using
the Wan encoder. We then sample Gaussian noise latentsznoise
t+1:t+H ∼ N(0,I)for the next chunk and
feed the concatenated latents[z 0, zt−c:t, znoise
t+1:t+H ]into a stack of action-conditioned DiT blocks.
The model predicts future latentsˆzt+1:t+H, which are decoded into framesˆot′+1:t′+H ′ and appended
to the context. By iterating this chunk-by-chunk procedure, the world model generates long-horizon
imagined rollouts under the policy’s actions while maintaining global scene consistency, and these
rollouts are subsequently used as the simulated environment for reinforcement learning.
We train the world model with the Rectified Flow objective [52]. Letx 1 =z t+1:t+H denote the
target future latents andx 0 ∼ N(0,I)be noise of the same shape. Given a sampled timet∈[0,1],
we obtain the intermediate latentx t and train the modelu(·;ϕ)to predict the velocityv t:
L=E x0,x1,c,t
h
∥u(xt, c, t;ϕ)−v t∥2
i
,(7)
where the conditioncincludes both the first-frame–anchored context and actions. To reduce the
train–inference gap in closed-loop rollouts, we additionally apply noisy context by injecting diffu-
sion noise into the non-reference context latentsz t−c:t during training. This discourages brittle vi-
sual copying from context and improves robustness when the model consumes self-generated frames
over long horizons [53, 46].
When serving as a simulator for reinforcement learning, the world model must also provide a reward
signal. In real-world robotic manipulation, designing dense rewards is often impractical, and training
typically relies on sparse success annotations. Therefore, we introduce a learned reward classifier
that produces a binary success signal based on the predicted next observation. Concretely, given the
generated observation˜ot+1 from the world model, the reward modelRψpredicts the probability of
task success, and the sparse reward is defined as
rt+1 =I(R ψ(˜ot+1)≥0.5),(8)
whereI(·)denotes the indicator function. Following HiL-SERL [16], the reward classifier is im-
plemented as a lightweight network and trained using binary cross-entropy (BCE) loss on labeled
success states.
4.2 Hallucination-Aware Policy Optimization in Imagination
WoVR optimizes the VLA policy by interacting with the learned world model, which serves as a
generative simulator for closed-loop imagined rollouts. The key difficulty is that, in long-horizon
rollouts starting from the initial state, world-model errors accumulate early and can eventually pro-
duce visually plausible but physically incorrect transitions and even spurious success signals. If
7
```

## PDF page 8

```text
reinforcement learning naively trusts such rollouts, the policy is encouraged to optimize toward
hallucinated outcomes rather than real task progress.
……
GT
Initial-State Rollouts
Hallucinated success
……
Correctly models failure
Keyframe-Initialized Rollouts
Error accumulation in early stage
Figure 5:Illustration of the effect of Keyframe-Initialized Rollouts (KIR).Starting from the ini-
tial state, long-horizon rollouts accumulate prediction errors in early stages, leading to hallucinated
success that contradicts the ground-truth failure. In contrast, Keyframe-Initialized Rollouts initialize
rollouts near critical states, enabling physically consistent predictions that correctly model failure,
which in turn facilitates more efficient and stable policy learning.
To reduce the effective error depth of imagined interaction, we introduce Keyframe-Initialized Roll-
outs (KIR). As illustrated in Figure 5, instead of always initializing rollouts from the episode start
o0, we initialize a portion of rollouts from keyframesok that lie near task-critical intermediate states,
especially failure states encountered by the current policy. The motivation is that many decisive con-
tacts and corrections happen locally around these states, whereas starting fromo 0 forces the world
model to predict a long prefix before reaching them, during which compounding errors can already
derail the rollout.
We adopt Group Relative Policy Optimization (GRPO) to update the policy using imagined rollouts.
For each update, we sample a group of imagined trajectories and compute a group-relative advan-
tage, then optimize a clipped GRPO objective. Because hallucinations often dominate after success
has been reached in imagination, we mask post-success steps and normalize each trajectory by its
valid length.
Formally, given a group of imagined trajectories{τ (i)}G
i=1 sampled in the world model,
τ (i) ={(o (i)
t , a(i)
t ,ˆr(i)
t )}T
t=1, o (i)
t+1 ∼ ˆPϕ(· |o (i)
t , a(i)
t ),(9)
we compute the returnR(τ (i))and group-relative advantage ˆA(i),
R(τ (i)) =
|τ (i)|X
t=1
γt−1ˆr(i)
t , ˆA(i) =R(τ (i))− 1
G
GX
j=1
R(τ (j)).(10)
8
```

## PDF page 9

```text
LetT valid
i be the number of valid timesteps up to (and including) the first success, and define
ρ(i)
t (θ) = πθ(a(i)
t |o(i)
t ,l)
πθold (a(i)
t |o(i)
t ,l). The masked, trajectory-length–normalized GRPO objective is
JGRPO(θ) =E

 1
G
GX
i=1
1
T valid
i
T valid
iX
t=1
min

ρ(i)
t (θ) ˆA(i),clip

ρ(i)
t (θ),1−ϵ,1 +ϵ

ˆA(i)


 .(11)
This objective also complements KIR: keyframe-initialized rollouts tend to reach task resolution
with fewer valid steps, and trajectory-length normalization increases their per-timestep contribution,
so gradients are dominated by short, task-critical segments rather than long, drift-prone continua-
tions.
4.3 PACE: Policy–Aligned Co-Evolution
While policy optimization proceeds entirely within the learned world model, the policy’s action dis-
tribution continuously evolves and drifts away from the data used to train the initial world model.
This inherent distribution shift leads to accumulating mismatch between the simulator and the im-
proving policy, ultimately degrading the reliability of imagined rollouts.
To address this issue, we introducePACE, a World Model–Policy co-evolution strategy. Instead of
treating the world model as a fixed, static simulator throughout policy optimization, PACE allows
the world model and VLA policy to evolve together throughout training.
Concretely, we realize this co-evolution through low-frequency, policy-driven refinement: we first
train an initial world model, denoted asWM Base, using trajectories collected from the base VLA
policy. After the first stage of policy optimization withinWM Base, we collect a limited set of
additional rollouts under the evolved policy and use them to further refine the world model. The
refined model is referred to asWM Evo.
Importantly, this refinement is performed only once (or at very low frequency), distinguishingPACE
from classical model-based reinforcement learning methods, which continuously update the dynam-
ics model at high frequency during policy optimization.
This low-frequency refinement provides two key advantages. First, unlike real-world online RL, it
does not require continuous human supervision or environment resets during policy training, signifi-
cantly reducing operational overhead. Second, by aligning the world model with the evolving policy
distribution,PACEmitigates compounding model errors and maintains simulator reliability without
sacrificing training stability.
System Implementation.We build WoVR on top of RLinf [24] to support efficient distributed
imagined rollouts and training. Concretely, we replace RLinf’s environment back-end with our
learned world model, enabling scalable closed-loop rollouts without a ground-truth simulator. GPU
allocation details are provided in Appendix A.
5 Experiments
We conduct extensive experiments to evaluate the effectiveness of WoVR as a world-model-based
reinforcement learning framework for post-training VLA policies. Our experimental design aims to
systematically answer the following three questions:
•Q1:Is the proposed world model stable, controllable, and efficient enough to serve as a
simulator for closed-loop reinforcement learning?
•Q2:Can WoVR effectively improve VLA task performance compared to existing world-
model-based reinforcement learning methods?
•Q3:Do the policies optimized with WoVR reliably transfer to real-world robotic manipu-
lation tasks?
9
```

## PDF page 10

```text
To answer these questions, we evaluate both the quality of the learned world model and the
downstream policy performance. For world model evaluation, we focus on long-horizon, action-
conditioned video generation under closed-loop, chunk-by-chunk autoregressive inference. We
adopt standard perceptual and distributional metrics, including LPIPS [54], FID [55], FVD [56]
and FloLPIPS [57]. Specifically,LPIPS(Learned Perceptual Image Patch Similarity) measures
frame-level perceptual similarity using deep feature representations;FID(Fr ´echet Inception Dis-
tance) evaluates distributional similarity between generated and real frames via feature statistics;
FVD(Fr ´echet Video Distance) extends this comparison to the temporal domain to assess video-
level realism and motion consistency; andFloLPIPSmeasures motion-aligned perceptual similarity
along estimated optical flow trajectories, emphasizing temporal coherence under action-conditioned
dynamics. Since the world model is intended to be used as a simulator for closed-loop on-policy
reinforcement learning, we also report inference throughput (frames per second) to quantify gener-
ation efficiency.
For policy evaluation, we use task success rate (SR) as the primary metric, reflecting the sparse-
reward setting commonly encountered in real-world robotic manipulation. All success rates are
computed over multiple independent rollouts with fixed initial conditions.
We compare WoVR against several representative baselines spanning bothworld model qualityand
policy optimization. For world model quality, we include EV AC [42], which conditions generation
on absolute end-effector actions, as well as Cosmos-Predict2 [58] and OpenSora [19], the latter
serving as the world-model backbone adopted in WMPO [22]. All compared models are evaluated
under the same chunk-wise autoregressive generation protocol to ensure a fair comparison.
For policy optimization, we consider the following baselines:
• OpenVLA-OFT-base [1]: a base VLA policy trained purely with imitation learning;
• GRPO (Online) [14]: trained with real-environment interaction under the same rollout bud-
get;
• WMPO [22]: performs reinforcement learning using an OpenSora-based world model.
All world-model-based methods are trained until convergence within their respective simulators,
while GRPO is reported under the same rollout budget to ensure a fair comparison. All experiments
are conducted using eight NVIDIA H100 GPUs.
5.1 Q1: Is the World Model Stable, Controllable, and Efficient?
We first investigate whether the proposed world model is sufficiently stable, controllable, and ef-
ficient to serve as a simulator for closed-loop reinforcement learning. In particular, we focus on
long-horizon, action-conditioned video generation under chunk-by-chunk autoregressive inference,
where modeling errors may accumulate and severely affect downstream policy optimization.
Experimental Setup.We conduct all world model evaluations in the LIBERO environment [59].
A total of 3,000 VLA rollout trajectories, each with a length of 512 frames, are collected to train
the world models. In addition, 200 held-out trajectories of the same length are used exclusively
for evaluation. We compare WoVR against three representative action-conditioned world models:
EV AC, Cosmos-Predict2, and OpenSora as adopted in WMPO. Among them, EV AC conditions
video generation on absolute end-effector actions, while Cosmos-Predict2, OpenSora, and WoVR
all use residual action representations.
During evaluation, all baseline models follow the same chunk-wise autoregressive generation pro-
tocol to ensure a fair comparison. Specifically, each model predicts future video segments by con-
ditioning on a 4-frame visual context together with an 8-step action chunk, and autoregressively
generates the subsequent 8 frames. For the first chunk, where only a single initial image is available,
the initial frame is replicated to fill the context window in order to align the inference procedure
across methods. We quantitatively evaluate the generated rollouts by comparing predicted videos
10
```

## PDF page 11

```text
with ground-truth trajectories using standard video generation metrics, including LPIPS, FID, FVD
and FloLPIPS.
Table 1:World model quality, motion consistency, and efficiency comparison.Rollout denotes
the rollout horizon length.
Metrics
Method Rollout FPS↑LPIPS [54]↓FID [55]↓FVD [56]↓FloLPIPS [57]↓
EV AC [42]
512
2.7
0.146 46.528 345.818 0.205
2560.130 49.153 354.983 0.192
1280.106 44.337 423.132 0.166
Cosmos-Predict2 [58]
512
3.50
0.315 165.862 275.737 0.265
2560.226 106.324 203.853 0.306
1280.164 77.555 304.456 0.281
OpenSora [22]
512
7.00
0.105 38.478 89.391 0.156
2560.082 33.577 94.998 0.122
1280.069 33.413 111.643 0.113
WoVR (Ours)
512
23.0
0.091 34.252 68.011 0.154
2560.063 24.378 50.041 0.102
1280.047 18.553 39.047 0.079
Quantitative Results.Table 1 summarizes the quantitative comparison across different rollout
horizons. As shown in the table, WoVR consistently outperforms EV AC, Cosmos-Predict2, and
OpenSora across all evaluation metrics. In particular, WoVR achieves the lowest LPIPS, FID, FVD,
and FloLPIPS scores at all tested rollout lengths, indicating higher visual fidelity, stronger temporal
consistency, and more accurate action-conditioned dynamics. These improvements become more
pronounced as the rollout horizon increases, suggesting that WoVR is more robust to error accumu-
lation in long-horizon autoregressive generation.
Despite adopting a larger backbone (Wan,∼5B) than OpenSora (∼1.3B), WoVR achieves higher
inference throughput by requiring only five diffusion steps and leveraging a 3D V AE for spatiotem-
poral latent encoding, whereas OpenSora typically relies on more sampling steps and a 2D V AE.
5.2 Q2: Can WoVR Effectively Improve VLA Task Performance?
We next evaluate whether the proposed world model can effectively support reinforcement learn-
ing and lead to improved task performance of VLA policies. Beyond world model fidelity, this
experiment directly assesses the practical value of WoVR as a simulator for policy optimization.
Experimental Setup.We conduct policy optimization experiments on multiple LIBERO task
suites, including the Spatial, Object, Goal, and Long suites [59]. As the base policy, following
SimpleVLA-RL [17], we initialize from OpenVLA-OFT and perform one-trajectory supervised
fine-tuning.
Each LIBERO suite contains 10 tasks. For each suite, we allocate a total real-environment rollout
budget of 2,500 trajectories. We first collect 1,500 trajectories (150 per task) using the base VLA
policy to train the initial world modelWMBase. After the first stage of policy optimization in imagi-
nation, we collect an additional 1,000 trajectories under the updated policy and use them to refine the
world modelWM Evo, aligning the simulator with the evolving policy distribution. To balance align-
ment quality and computational efficiency, we perform only a single co-evolution step in practice,
resulting in one refinement fromWM Base toWM Evo rather than multiple iterative alternations.
To ensure a fair comparison, all methods are allocated the same real-environment rollout budget of
2,500 trajectories per suite. For world-model-based methods, including WMPO and WoVR, these
11
```

## PDF page 12

```text
Table 2:Task success rates (%) across LIBERO task suites.The base policy isOpenVLA-
OFT trained with one-trajectory supervised fine-tuning (one-trajectory SFT). All methods use
2,500 trajectories collected from the ground-truth simulator.GRPO (Online)consumes them for
on-policy interaction, whereasWMPOandWoVRuse them only for world model training and
perform policy optimization via imagined rollouts. Improvements are shown in parentheses relative
to the base policy.
Spatial Object Goal Long Avg↑
OpenVLA-OFT-base [1] 61.5 36.3 48.2 13.7 39.9
GRPO (online) [14] 66.6 45.1 52.1 14.5 44.6
WMPO [22] 67.8 48.0 54.6 13.7 46.2
WoVR (Ours)81.5(+20.0)82.0(+45.7)77.5(+29.3)35.8(+22.1)69.2(+29.3)
trajectories are used exclusively for world model training and refinement, while policy optimization
is conducted entirely within the learned world model via imagined rollouts, without further inter-
action with the ground-truth simulator. In contrast, GRPO directly interacts with the ground-truth
simulator and consumes the same 2,500-trajectory budget for on-policy policy optimization.
Table 2 summarizes success rates across LIBERO suites under this shared simulator-trajectory bud-
get: GRPO uses the 2,500 trajectories for on-policy optimization, whereas WMPO and WoVR use
them only to train the world model and optimize the policy via imagined rollouts.
Quantitative Results.Table 2 reports task success rates across LIBERO suites under a shared
simulator-trajectory budget. The base policy achieves moderate performance, reflecting the limi-
tations of imitation learning under sparse rewards and limited demonstrations. While GRPO im-
proves over the base policy, its gains come at a high interaction cost. In practice, each policy up-
date requires close to a thousand additional simulator trajectories, making the optimization process
sample-inefficient under realistic interaction constraints. This highlights the fundamental limitation
of purely online reinforcement learning in data-scarce robotic settings.
WMPO further improves performance on short- and medium-horizon suites (Spatial, Object, and
Goal), demonstrating that world-model-based optimization can provide benefits beyond online in-
teraction. However, WMPO does not achieve performance gains on theLIBERO-Longsuite, which
consists of longer-horizon tasks. In these tasks, rollout instability in later stages of autoregressive
generation degrades policy optimization, resulting in no improvement over the base policy.
In contrast, WoVR consistently achieves the highest success rates across all evaluated suites. No-
tably, WoVR improves performance by +20.0% on Spatial, +45.7% on Object, +29.3% on Goal, and
+22.1% on the long-horizon LIBERO-Long suite compared to the base policy. On average, WoVR
achieves a success rate of 69.2%, substantially outperforming both GRPO (44.6%) and WMPO
(46.2%).
These results indicate that the improved stability and controllability of the proposed world model
directly translate into more effective policy optimization. In particular, the strong performance on
long-horizon tasks highlights that suppressing error accumulation in imagined rollouts is critical for
reliable reinforcement learning with learned simulators.
5.3 Q3: Do Policies Optimized with WoVR Reliably Transfer to the Real World?
Finally, we evaluate whether policies optimized with WoVR reliably transfer to real-world robotic
manipulation tasks.
Experimental SetupOur experiments are conducted on a Franka Emika Panda robot. We consider
two contact-rich manipulation tasks:(i)Pick Banana, which requires picking a banana and placing
it onto a plate, and(ii)Pick Bread, which requires picking a bread item and placing it onto a
designated bread marker. For each task, we collect 10 teleoperated demonstrations to pre-train the
12
```

## PDF page 13

```text
Figure 6:Real-world setupon a Franka Panda for Pick Banana and Pick Bread.
Table 3:Real-world success rates (%, 30 trials per task) on a Franka Panda robot.Improve-
ments are shown in parentheses relative to the base policy.
Method Pick Banana Pick Bread Avg
OpenVLA-OFT-base 46.7 (14/30) 76.7 (23/30) 61.7
WoVR (Ours)93.3(28/30)(+46.6)90.0(27/30)(+13.3)91.7(+30.0)
base VLA policy, and additionally collect 150 rollouts from the base policy to train the world model.
After training, we deploy the resulting policies on the physical robot and evaluate success rates over
30 independent trials per task.
Quantitative Results.Table 3 reports the real-world success rates. OnPick Banana, the base
policy achieves a success rate of 46.67% (14/30), while WoVR improves it to 93.3% (28/30). On
Pick Bread, WoVR increases the success rate from 76.67% (23/30) to 90.0% (27/30). These results
demonstrate that WoVR delivers consistent real-world gains over imitation learning without requir-
ing additional online interaction during policy optimization, indicating strong sim-to-real transfer of
the optimized behaviors.
6 Ablation Study
6.1 Ablation on World Model Mechanisms
We first conduct ablation studies on the core design choices of the proposed world model, aiming
to understand how different context modeling mechanisms affect long-horizon video generation
stability. Specifically, we investigate the following factors: (i) the number of memory frames used
as visual context, (ii) the use of a fixed reference frame, and (iii) the effect of adding noise to context
frames during training.
Experimental Variants.We compare the full WoVR model against three ablated variants:
• WoVR w/o ref, which removes the fixed reference frame from the context window;
• WoVR w. mem=1, which uses only a single-frame context;
• WoVR w/o noisy context, which disables noise injection on context frames during training.
All variants are trained and evaluated on theLIBERO-Spatialsuite only. We train the world model
using 1,500 VLA rollout trajectories and evaluate on a held-out set of 24 trajectories.
13
```

## PDF page 14

```text
Quantitative Results.Table 4 reports the quantitative results measured by LPIPS, FID, and FVD
under different rollout horizons. Compared to using a single-frame context, employing a multi-frame
context with a fixed reference anchor significantly improves performance across all metrics.
Table 4:Ablation study on world model mechanisms (LIBERO-Spatial).Rollout denotes the
rollout horizon length.
Metrics
Method Rollout LPIPS↓FID↓FVD↓FloLPIPS↓
WoVR (Ours)
5120.091 36.687 73.493 0.154
2560.069 27.238 63.948 0.110
1280.051 20.780 49.017 0.081
WoVR w/o ref
5120.133 73.942 123.502 0.168
2560.089 49.406 86.000 0.116
1280.064 35.559 86.146 0.090
WoVR w. mem=1
5120.120 64.501 86.042 0.165
2560.086 46.790 81.742 0.117
1280.065 36.047 79.605 0.095
WoVR w/o noisy context
5120.099 44.712 77.284 0.160
2560.074 31.691 61.660 0.115
1280.054 23.444 58.836 0.085
To better understand the failure modes behind these quantitative trends, we provide qualitative com-
parisons in Fig. 7. As shown in the figure, models without a fixed reference frame or noisy context
exhibit noticeable spatial drift and object disappearance over long-horizon rollouts, whereas the full
WoVR model remains visually stable and consistent with the ground truth.
Removing the reference frame leads to a clear degradation in performance, especially under longer
rollout horizons. This result suggests that anchoring the context with a fixed reference frame ef-
fectively suppresses error accumulation in the autoregressive feedback loop, which is critical for
maintaining stability in long-horizon video generation.
Furthermore, disabling noise injection on context frames also results in noticeable performance
drops. While the degradation is moderate for short rollouts, the gap becomes more pronounced as
the rollout length increases. This observation indicates that adding mild noise to context frames
improves robustness in long-horizon generation by reducing over-reliance on precise conditioning
inputs, thereby alleviating the train–inference gap.
Overall, these results demonstrate that the proposed context modeling strategy—combining a fixed
reference frame, a multi-frame memory window, and noisy context augmentation—plays a crucial
role in stabilizing long-horizon video generation. Together, these mechanisms enable WoVR to
maintain high fidelity and temporal consistency under closed-loop autoregressive inference, provid-
ing a more reliable simulator for downstream reinforcement learning.
6.2 Ablation on Policy Optimization Mechanisms
We next ablate key components in the policy optimization pipeline of WoVR, aiming to understand
how different design choices affect downstream VLA task performance. In particular, we focus on
mechanisms that facilitate stable policy learning and effective utilization of the learned world model.
Experimental Setup.All experiments are conducted on theLIBERO-Spatialsuite, with the same
training protocol, data budget, and evaluation procedure as described in Sec. 5.2. Specifically, the
base VLA policy is pre-trained following the same demonstration setup as in Q2, and policy opti-
14
```

## PDF page 15

```text
Ground 
Truth
WoVR
(Ours)
WoVR
w.mem=1
WoVR
w/o ref
WoVR
w/o noisy 
context
Frame 50 Frame 150 Frame 250 Frame 350 Frame 450
Figure 7:Qualitative ablation results on LIBERO-Spatial.Ablated variants exhibit error accu-
mulation and visual drift under long-horizon rollouts, while the full WoVR model remains stable
and consistent with the ground truth.
mization is performed using world-model-based reinforcement learning. Task performance is mea-
sured by the average success rate over the LIBERO-Spatial tasks.
We compare the full WoVR framework against the following ablated variants:
• WoVR w/o KIR, which removes keyframe-based initialization and starts policy optimiza-
tion from randomly sampled initial states in the world model;
• WoVR w/o PACE, which disables the co-evolution of the world model with the updated
policy and keeps the world model fixed during policy optimization.
Quantitative Results.Table 5 reports the success rates on the LIBERO-Spatial suite. The full
WoVR framework achieves the highest performance, with an average success rate of 0.815. Remov-
ing keyframe-based initialization leads to a noticeable drop in performance, reducing the success
rate to 0.782. This result indicates that KIR plays an important role in stabilizing early-stage policy
learning by providing meaningful initial states.
Disabling the co-evolution of the world model further degrades performance to 0.71. This suggests
that continuously refining the world model with updated policy rollouts is critical for maintaining
simulator accuracy and preventing compounding model errors during policy optimization.
7 Conclusion
In this work, we revisited world-model-based reinforcement learning for VLA policies through the
lens of reliability. Rather than assuming a learned world model to be a faithful simulator, we iden-
tified hallucination under closed-loop imagined interaction as the central obstacle: autoregressive
15
```

## PDF page 16

```text
Table 5:Ablation on policy optimization mechanisms on LIBERO-Spatial.Success rate is aver-
aged over all tasks in the suite.
Method Success Rate↑
WOVR (Ours)0.815
WOVR w/o KIR 0.782
WOVR w/o PACE 0.710
error accumulation and policy-induced distribution shift can systematically corrupt optimization sig-
nals, causing reinforcement learning to exploit model inaccuracies instead of genuine task progress.
To make RL in imagination viable under imperfect dynamics, we introduced WoVR, a hallucination-
aware framework that controls hallucination at three interconnected levels. First, we strengthen the
simulator itself by building a rollout-stable, action-controllable video world model, improving long-
horizon consistency under policy-driven generation. Second, because residual prediction errors are
unavoidable, we reshape the interaction protocol with Keyframe-Initialized Rollouts (KIR) to reduce
the effective error depth and concentrate learning on task-critical segments where dynamics must be
correct. Third, to prevent the evolving policy from drifting out of the simulator’s training distribu-
tion, we maintain policy–simulator alignment viaPACE, a policy-aligned co-evolution strategy that
mitigates distribution mismatch without requiring continuous online supervision.
Extensive experiments on LIBERO and real-world manipulation tasks demonstrate that WoVR en-
ables stable long-horizon imagined rollouts and effective on-policy optimization, yielding substan-
tial gains over imitation learning and reliable transfer to physical robots. Overall, our results suggest
that learned world models can serve as practical simulators for reinforcement learning when hallu-
cination is explicitly regulated by design, interaction, and alignment. Nevertheless, WoVR reduces
but does not fully eliminate hallucination, particularly in extremely long-horizon or highly contact-
sensitive settings, and it still relies on learned reward modeling and limited real-data refinement,
leaving broader reliability guarantees as an open direction for future work.
16
```

## PDF page 17

```text
References
[1] M. J. Kim, C. Finn, and P. Liang. Fine-tuning vision-language-action models: Optimizing
speed and success.arXiv preprint arXiv:2502.19645, 2025.
[2] K. Black, N. Brown, D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, L. Groom, K. Hausman,
B. Ichter, et al.π 0: A vision-language-action flow model for general robot control.arXiv
preprint arXiv:2410.24164, 2024.
[3] P. Intelligence, K. Black, N. Brown, J. Darpinian, K. Dhabalia, D. Driess, A. Esmail, M. Equi,
C. Finn, N. Fusai, M. Y . Galliker, D. Ghosh, L. Groom, K. Hausman, B. Ichter, S. Jakubczak,
et al.π 0.5: a vision-language-action model with open-world generalization.arXiv preprint
arXiv:2504.16054, 2025.
[4] H. Li, Y . Chen, W. Cui, W. Liu, K. Liu, M. Zhou, Z. Zhang, and D. Zhao. Survey of vision-
language-action models for embodied manipulation.arXiv preprint arXiv:2508.15201, 2025.
[5] H. Zang, M. Wei, S. Xu, Y . Wu, Z. Guo, Y . Wang, H. Lin, L. Shi, Y . Xie, Z. Xu, Z. Liu,
K. Chen, W. Tang, Q. Zhang, W. Zhang, C. Yu, and Y . Wang. Rlinf-vla: A unified and efficient
framework for vla+rl training, 2025.
[6] J. Liu, F. Gao, B. Wei, X. Chen, Q. Liao, Y . Wu, C. Yu, and Y . Wang. What can rl bring to vla
generalization? an empirical study.arXiv preprint arXiv:2505.19789, 2026.
[7] K. Chen, Z. Liu, T. Zhang, Z. Guo, S. Xu, H. Lin, H. Zang, X. Li, Q. Zhang, Z. Yu, G. Fan,
T. Huang, Y . Wang, and C. Yu.πRL: Online rl fine-tuning for flow-based vision-language-action
models, 2026.
[8] Y . Chen, S. Tian, S. Liu, Y . Zhou, H. Li, and D. Zhao. Conrft: A reinforced fine-tuning method
for vla models via consistency policy. InProceedings of Robotics: Science and Systems, RSS
2025, Los Angeles, CA, USA, Jun 21-25, 2025, 2025. doi:10.15607/RSS.2025.XXI.019.
[9] G. Lu, W. Guo, C. Zhang, Y . Zhou, H. Jiang, Z. Gao, Y . Tang, and Z. Wang. Vla-rl: To-
wards masterful and general robotic manipulation with scalable reinforcement learning.arXiv
preprint arXiv:2505.18719, 2025.
[10] Y . Li, X. Ma, J. Xu, Y . Cui, Z. Cui, Z. Han, L. Huang, T. Kong, Y . Liu, H. Niu, W. Peng,
J. Qiao, Z. Ren, H. Shi, Z. Su, J. Tian, Y . Xiao, S. Zhang, L. Zheng, H. Li, and Y . Wu. Gr-rl:
Going dexterous and precise for long-horizon robotic manipulation, 2025.
[11] K. Lei, H. Li, D. Yu, Z. Wei, L. Guo, Z. Jiang, Z. Wang, S. Liang, and H. Xu. Rl-100:
Performant robotic manipulation with real-world reinforcement learning, 2025.
[12] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov. Proximal policy optimization
algorithms.arXiv preprint arXiv:1707.06347, 2017.
[13] Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang, M. Zhang, Y . K. Li, Y . Wu,
and D. Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open language
models.arXiv preprint arXiv:2402.03300, 2024.
[14] D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, et al.
Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning.arXiv
preprint arXiv:2501.12948, 2025.
[15] W. Cui, C. Zhao, S. Wei, J. Zhang, H. Geng, Y . Chen, and H. Wang. Gapartmanip: a large-scale
dataset for generalizable and actionable part manipulation with material-agnostic articulated
objects. InIEEE International Conference on Robotics and Automation. IEEE, 2025.
[16] J. Luo, C. Xu, J. Wu, and S. Levine. Precise and dexterous robotic manipulation via human-
in-the-loop reinforcement learning.Science Robotics, 10(105):eads5033, 2025.
17
```

## PDF page 18

```text
[17] H. Li, Y . Zuo, J. Yu, Y . Zhang, Z. Yang, K. Zhang, X. Zhu, Y . Zhang, T. Chen, G. Cui,
et al. Simplevla-rl: Scaling vla training via reinforcement learning.arXiv preprint
arXiv:2509.09674, 2025.
[18] Z. Zheng, X. Peng, T. Yang, C. Shen, S. Li, H. Liu, Y . Zhou, T. Li, and Y . You. Open-sora:
Democratizing efficient video production for all.arXiv preprint arXiv:2412.20404, 2024.
[19] X. Peng, Z. Zheng, C. Shen, T. Young, X. Guo, B. Wang, H. Xu, H. Liu, M. Jiang, W. Li, et al.
Open-sora 2.0: Training a commercial-level video generation model in200k.arXiv preprint
arXiv:2503.09642, 2025.
[20] T. Wan, A. Wang, B. Ai, B. Wen, C. Mao, C.-W. Xie, D. Chen, F. Yu, H. Zhao, J. Yang,
et al. Wan: Open and advanced large-scale video generative models.arXiv preprint
arXiv:2503.20314, 2025.
[21] J. Xiao, Y . Yang, X. Chang, R. Chen, F. Xiong, M. Xu, W.-S. Zheng, and Q. Zhang. World-
env: Leveraging world model as a virtual environment for vla post-training.arXiv preprint
arXiv:2509.24948, 2025.
[22] F. Zhu, Z. Yan, Z. Hong, Q. Shou, X. Ma, and S. Guo. Wmpo: World model-based policy
optimization for vision-language-action models.arXiv preprint arXiv:2511.09515, 2025.
[23] H. Li, P. Ding, R. Suo, Y . Wang, Z. Ge, D. Zang, K. Yu, M. Sun, H. Zhang, D. Wang, and
W. Su. Vla-rft: Vision-language-action reinforcement fine-tuning with verified rewards in
world simulators.arXiv preprint arXiv:2510.00406, 2025.
[24] C. Yu, Y . Wang, Z. Guo, H. Lin, S. Xu, H. Zang, Q. Zhang, Y . Wu, C. Zhu, J. Hu, et al. Rlinf:
Flexible and efficient large-scale reinforcement learning via macro-to-micro flow transforma-
tion.arXiv preprint arXiv:2509.15965, 2025.
[25] X. Yuan, T. Mu, S. Tao, Y . Fang, M. Zhang, and H. Su. Policy decorator: Model-agnostic
online refinement for large policy model, 2024.
[26] M. Pan, S. Feng, Q. Zhang, X. Li, J. Song, C. Qu, Y . Wang, C. Li, Z. Xiong, Z. Chen, Y . Liu,
and J. Luo. Sop: A scalable online post-training system for vision-language-action models.
arXiv preprint arXiv:2601.03044, 2026.
[27] H. Zang, S. Yu, H. Lin, T. Zhou, Z. Huang, Z. Guo, X. Xu, J. Zhou, Y . Sheng, S. Zhang, F. Gao,
W. Tang, Y . Yue, Q. Zhang, X. Chen, C. Yu, and Y . Wang. Rlinf-user: A unified and extensible
system for real-world online policy learning in embodied ai, 2026.
[28] X. He, C. Peng, Z. Liu, B. Wang, Y . Zhang, Q. Cui, F. Kang, B. Jiang, M. An, Y . Ren,
B. Xu, H.-X. Guo, K. Gong, S. Wu, W. Li, X. Song, Y . Liu, Y . Li, and Y . Zhou. Matrix-
game 2.0: An open-source real-time and streaming interactive world model.arXiv preprint
arXiv:2508.13009, 2025.
[29] Y . Zhang, C. Peng, B. Wang, P. Wang, Q. Zhu, F. Kang, B. Jiang, Z. Gao, E. Li, Y . Liu, and
Y . Zhou. Matrix-game: Interactive world foundation model.arXiv preprint arXiv:2506.18701,
2025.
[30] J. Li, J. Tang, Z. Xu, L. Wu, Y . Zhou, S. Shao, T. Yu, Z. Cao, and Q. Lu. Hunyuan-gamecraft:
High-dynamic interactive game video generation with hybrid history condition.arXiv preprint
arXiv:2506.17201, 2025.
[31] J. Tang, J. Liu, J. Li, L. Wu, H. Yang, P. Zhao, S. Gong, X. Yuan, S. Shao, and Q. Lu.
Hunyuan-gamecraft-2: Instruction-following interactive game world model.arXiv preprint
arXiv:2511.23429, 2025.
[32] X. Mao, S. Lin, Z. Li, C. Li, W. Peng, T. He, J. Pang, M. Chi, Y . Qiao, and K. Zhang. Yume:
An interactive world generation model.arXiv preprint arXiv:2507.17744, 2025.
18
```

## PDF page 19

```text
[33] X. Mao, Z. Li, C. Li, X. Xu, K. Ying, T. He, J. Pang, Y . Qiao, and K. Zhang. Yume-1.5: A
text-controlled interactive world generation model.arXiv preprint arXiv:2512.22096, 2025.
[34] R. Team, Z. Gao, Q. Wang, Y . Zeng, J. Zhu, K. L. Cheng, Y . Li, H. Wang, Y . Xu, S. Ma,
Y . Chen, J. Liu, Y . Cheng, Y . Yao, J. Zhu, Y . Meng, K. Zheng, Q. Bai, J. Chen, Z. Shen,
Y . Yu, X. Zhu, Y . Shen, and H. Ouyang. Advancing open-source world models.arXiv preprint
arXiv:2601.20540, 2026.
[35] X. Huang, Z. Li, G. He, M. Zhou, and E. Shechtman. Self forcing: Bridging the train-test gap
in autoregressive video diffusion.arXiv preprint arXiv:2506.08009, 2025.
[36] Y . Lu, Y . Zeng, H. Li, H. Ouyang, Q. Wang, K. L. Cheng, J. Zhu, H. Cao, Z. Zhang, X. Zhu,
Y . Shen, and M. Zhang. Reward forcing: Efficient streaming video generation with rewarded
distribution matching distillation.arXiv preprint arXiv:2512.04678, 2025.
[37] H. Zhu, M. Zhao, G. He, H. Su, C. Li, and J. Zhu. Causal forcing: Autoregressive diffusion
distillation done right for high-quality real-time interactive video generation.arXiv preprint
arXiv:2602.02214, 2026.
[38] T. Yin, Q. Zhang, R. Zhang, W. T. Freeman, F. Durand, E. Shechtman, and X. Huang.
From slow bidirectional to fast autoregressive video diffusion models.arXiv preprint
arXiv:2412.07772, 2025.
[39] T. Yin, M. Gharbi, T. Park, R. Zhang, E. Shechtman, F. Durand, and W. T. Freeman. Improved
distribution matching distillation for fast image synthesis.arXiv preprint arXiv:2405.14867,
2024.
[40] T. Yin, M. Gharbi, R. Zhang, E. Shechtman, F. Durand, W. T. Freeman, and T. Park. One-step
diffusion with distribution matching distillation.arXiv preprint arXiv:2311.18828, 2024.
[41] Y . Liao, P. Zhou, S. Huang, D. Yang, S. Chen, Y . Jiang, Y . Hu, J. Cai, S. Liu, J. Luo, L. Chen,
S. Yan, M. Yao, and G. Ren. Genie envisioner: A unified world foundation platform for robotic
manipulation.arXiv preprint arXiv:2508.05635, 2025.
[42] Y . Jiang, S. Chen, S. Huang, L. Chen, P. Zhou, Y . Liao, X. He, C. Liu, H. Li, M. Yao, and
G. Ren. Enerverse-ac: Envisioning embodied environments with action condition.arXiv
preprint arXiv:2505.09723, 2025.
[43] J. Quevedo, A. K. Sharma, Y . Sun, V . Suryavanshi, P. Liang, and S. Yang. Worldgym: World
model as an environment for policy evaluation.arXiv preprint arXiv:2506.00613, 2025.
[44] A. Bagchi, Z. Bao, H. Bharadhwaj, Y .-X. Wang, P. Tokmakov, and M. Hebert. Walk through
paintings: Egocentric world models from internet priors.arXiv preprint arXiv:2601.15284,
2026.
[45] F. Zhu, H. Wu, S. Guo, Y . Liu, C. Cheang, and T. Kong. Irasim: A fine-grained world model
for robot manipulation.arXiv preprint arXiv:2406.14540, 2025.
[46] Y . Guo, L. X. Shi, J. Chen, and C. Finn. Ctrl-world: A controllable generative world model
for robot manipulation.arXiv preprint arXiv:2510.10125, 2025.
[47] Y . Li, Y . Zhu, J. Wen, C. Shen, and Y . Xu. Worldeval: World model as real-world robot policies
evaluator.arXiv preprint arXiv:2505.19017, 2025.
[48] Y . Zhu, J. Feng, W. Zheng, Y . Gao, X. Tao, P. Wan, J. Zhou, and J. Lu. Astra: General interac-
tive world model with autoregressive denoising.arXiv preprint arXiv:2512.08931, 2026.
[49] Z. Jiang, K. Liu, Y . Qin, S. Tian, Y . Zheng, M. Zhou, C. Yu, H. Li, and D. Zhao. World4rl:
Diffusion world models for policy refinement with reinforcement learning for robotic manipu-
lation.arXiv preprint arXiv:2509.19080, 2025.
19
```

## PDF page 20

```text
[50] J. Shin, Z. Li, R. Zhang, J.-Y . Zhu, J. Park, E. Shechtman, and X. Huang. Motionstream:
Real-time video generation with interactive motion controls.arXiv preprint arXiv:2511.01266,
2025.
[51] S. Yang, W. Huang, R. Chu, Y . Xiao, Y . Zhao, X. Wang, M. Li, E. Xie, Y . Chen, Y . Lu,
S. Han, and Y . Chen. Longlive: Real-time interactive long video generation.arXiv preprint
arXiv:2509.22622, 2025.
[52] P. Esser, S. Kulal, A. Blattmann, R. Entezari, J. M¨uller, H. Saini, Y . Levi, D. Lorenz, A. Sauer,
F. Boesel, D. Podell, T. Dockhorn, Z. English, K. Lacey, A. Goodwin, Y . Marek, and R. Rom-
bach. Scaling rectified flow transformers for high-resolution image synthesis.arXiv preprint
arXiv:2403.03206, 2024.
[53] B. Chen, D. M. Monso, Y . Du, M. Simchowitz, R. Tedrake, and V . Sitzmann. Diffusion forcing:
Next-token prediction meets full-sequence diffusion.arXiv preprint arXiv:2407.01392, 2024.
[54] R. Zhang, P. Isola, A. A. Efros, E. Shechtman, and O. Wang. The unreasonable effectiveness
of deep features as a perceptual metric. InProceedings of the IEEE conference on computer
vision and pattern recognition, pages 586–595, 2018.
[55] M. Heusel, H. Ramsauer, T. Unterthiner, B. Nessler, and S. Hochreiter. Gans trained by a two
time-scale update rule converge to a local nash equilibrium.Advances in neural information
processing systems, 30, 2017.
[56] T. Unterthiner, S. Van Steenkiste, K. Kurach, R. Marinier, M. Michalski, and S. Gelly. To-
wards accurate generative models of video: A new metric & challenges.arXiv preprint
arXiv:1812.01717, 2018.
[57] D. Danier, F. Zhang, and D. Bull. Flolpips: A bespoke video quality metric for frame interpoa-
tion.arXiv preprint arXiv:2207.08119, 2022.
[58] J. Pennington, P. Joshi, and A. Bhide. Develop custom physical ai foundation
models with nvidia cosmos predict-2.https://developer.nvidia.com/blog/
develop-custom-physical-ai-foundation-models-with-nvidia-cosmos-predict-2/,
June 11 2025. NVIDIA Developer Blog.
[59] B. Liu, Y . Zhu, C. Gao, Y . Feng, Q. Liu, Y . Zhu, and P. Stone. Libero: Benchmarking knowl-
edge transfer for lifelong robot learning.arXiv preprint arXiv:2306.03310, 2023.
20
```

## PDF page 21

```text
A GPU Allocation Strategy
The reinforcement-learning pipeline can be decomposed into three components:Generation,Simu-
lator, andTraining. In WoVR, theSimulatoris instantiated by the learnedworld model, which gen-
erates the next observation given the current observation and action. In the rollout phase,Generation
performs policy inference to produce an (optionally chunked) action from the current observation,
while theSimulatorexecutes the action and returns the next observation; this closed-loop interaction
repeats until a batch of trajectories is collected. In the optimization phase,Trainingupdates the VLA
policy using the collected trajectories, after which the system alternates back to rollout for the next
iteration.
Following the system abstraction in RLinf-VLA, WoVR adopts a collocated (shared) GPU allo-
cation strategy, where the three RL pipeline components co-exist on the same set of GPUs, with
theSimulatorimplemented as the world-model rollout module. Unlike physical simulators that
require dedicated device-side state, WoVR’s simulator is a neural network; thus, offload/onload
can be naturally realized by swapping only themodel parametersbetween GPU and host mem-
ory, without migrating any external simulator state. In its original form, collocated execution re-
lied on frequent GPU↔CPU offload/onload to keep only one component resident on GPUs at a
time; however, in embodied settings the simulator and generator must interact iteratively, making
per-interaction offload/onload prohibitively expensive. Therefore, we use the modified collocated
strategy: offload/onload for Generation and Simulator happens only at the beginning and end of the
rollout phase, avoiding repeated transfers during closed-loop imagined interaction, as illustrated in
Fig. 8.
Obs To VLAActions To Sim
Generation Simulator Training
GPU Process
0
1
2
3
…
…
…
4
5
…
…
offload
offload
onload
onload
onload
offload
Figure 8: Collocated GPU Allocation Strategy
21
```
