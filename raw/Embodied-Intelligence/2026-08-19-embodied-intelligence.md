# 🤖 Embodied Intelligence Biweekly Report

**Scan Period:** 2026-08-12 to 2026-08-19  
**Focus:** human-data-training | **Tracking:** Danfei Xu  
**Report Date:** 2026-08-19

---

## 🔥 Top 5 Core Highlights

### 1. Ego2Robot (arXiv:2608.02580, August 3) — 18,561 Hours of Synthetic Robot Data from Human Video

**Team:** AIM3 Lab, Renmin University of China (Ye Wang et al.)

**What it does:**  
Ego2Robot is an end-to-end pipeline that converts egocentric human manipulation videos into embodiment-specific robot training data at unprecedented scale — **18,561 hours across 15 robot morphologies**, generated from ~1,940 hours of egocentric input.

**How it works:**
- **Action Alignment:** Retargets hand keypoints to robot end-effector trajectories via gripper TCP, width, and orientation mapping, with Savitzky-Golay temporal smoothing
- **Visual Alignment:** Segments human arms (SAM 3), inpaints them out, then renders robot arms into the scene via depth-aware compositing
- **Quality Curation:** Three-level filtering — L1 pipeline-internal (IK failures, collisions), L2 statistical (outliers, discontinuities), L3 VLM consistency check
- Supports both annotated ego datasets (Path A) and raw unannotated video (Path B via WiLoR + DynHaMR hand pose estimation)

**Results:**
- Joint pretraining on Ego2Robot + real robot data (1:1 ratio) achieves **53.5% on RoboTwin Randomized** (+2.6 over robot-only)
- Visual generalization gains are strongest: **+8 on lighting shifts, +4 on background changes, +6 on robot color changes**
- Cross-embodiment zero-shot: ARX improves from 44% → 51%, UR5 peaks at 31%
- Validated on real ARX ACone hardware across 5 long-horizon tasks

**Why it matters:**
This is the largest ego-to-robot synthesis effort to date, and it demonstrates that **the ceiling on training data stops being how many teleoperators you can hire**. The multi-morphology rendering (raw ego acts as a "16th morphology") is a key insight for scalable cross-embodiment pretraining. Also used in **Qwen-RobotManip** foundation model pretraining recipe.

**Link:** https://arxiv.org/abs/2608.02580

---

### 2. T-Rex (arXiv:2606.17055, June 2026) — Tactile-Reactive Dexterous Manipulation

**Team:** UC Berkeley · NVIDIA · Stanford · Georgia Tech (Dantong Niu*, Zhuoyang Liu*, Zekai Wang* et al.)  
**Senior authors:** Fei-Fei Li, Ken Goldberg, Jitendra Malik, Pieter Abbeel, Yuke Zhu, **Danfei Xu**, Jim Fan, Trevor Darrell

**What it does:**  
T-Rex addresses a fundamental gap in VLA models: they either ignore tactile feedback or use static encoders that can't exploit the high-frequency nature of touch. T-Rex treats **tactile as a real-time control signal** rather than an observation modality.

**How it works:**
- **100-hour tactile-synchronized bimanual dataset** with diverse motor primitives
- **Variable-rate Mixture-of-Transformers (MoT):** Three experts operating at different frequencies — latent expert (visual/language context), action expert (~5Hz coarse trajectories), tactile expert (~20Hz fine corrections)
- **Temporal tactile VQ-VAE encoder** for efficient high-frequency touch representation
- **Asynchronous cascaded flow matching:** Action Expert denoises first (6 steps), then Tactile Expert refines in real-time (4 steps) while the robot executes

**Results:**
- **65% average success** on 12 real-world contact-rich tasks vs **35%** for EgoScale baseline
- **30%+ improvement** over strongest dexterous-hand foundation models
- A critical warning: π₀.₅ + tactile *without* architecture alignment drops to **6%** (below π₀.₅ without tactile) — tactile needs proper architectural support

**Why it matters:**
This is a landmark paper for several reasons: (1) it establishes a practical recipe for tactile-reactive control at scale, (2) the MoT architecture elegantly solves the frequency mismatch problem, (3) the dataset is open-source. The "π₀.₅ + tactile = 6%" finding is a valuable cautionary tale about multimodal integration.

**Link:** https://arxiv.org/abs/2606.17055

---

### 3. EgoWAM (July 8) — World Action Models Beyond Pixels with In-the-Wild Egocentric Data

**Team:** Georgia Tech (Danfei Xu's Lab)

**What it does:**  
EgoWAM extends World Action Models (WAMs) beyond pixel-level prediction by incorporating **3D flow and geometric structure** from in-the-wild egocentric human data. It bridges the gap between action-conditioned video generation and physically grounded robot control.

**Key idea:**
- Leverages egocentric human videos (Ego4D, EPIC-Kitchens) to learn world dynamics
- Integrates 3D scene flow as an intermediate representation between pixels and actions
- Enables cross-embodiment transfer by grounding predictions in geometry rather than appearance

**Why it matters:**
Directly from Danfei Xu's lab, this work reinforces her research trajectory: **egocentric human video is the most scalable data source, but only when processed through structured intermediate representations** (here, 3D flow). It sits at the intersection of world models and human-data-training — two of the hottest themes in embodied intelligence right now.

**Link:** https://arxiv.org (search EgoWAM)

---

### 4. The August 6 "World Model Wave" — GeniWorld, XEWorld, DyPES-VLA

Three major papers dropped on the same day, all converging on world models for cross-embodiment manipulation:

**GeniWorld** (Tsinghua) — A generalizable interactive world model for robotic manipulation via **visual actions**. Instead of predicting low-dimensional motor commands, it predicts visual changes ("what will the scene look like after this action?"), making it naturally embodiment-agnostic.

**XEWorld** (Chinese Academy of Sciences) — Asks a critical question: *Can action-conditioned world models generalize to unseen robot embodiments?* Introduces a benchmark with held-out robots, showing that current world models struggle with embodiment transfer — pointing to a key research gap.

**DyPES-VLA** (HKUST Guangzhou) — Learns **shared dynamics priors** across embodiments while keeping embodiment-specific control heads. The dynamics prior captures physics (gravity, friction, contact) that transfers; the action expert adapts to each robot's morphology.

**Why it matters:**
This wave signals a shift from "world models as simulators" to "world models as cross-embodiment transfer vehicles." XEWorld's finding that embodiment generalization is still weak is particularly important — it defines the next frontier.

---

### 5. VLAff (arXiv, August 5) — Vision-Language-Affordance Model for Unified Actionable Affordances

**Team:** University of Tokyo

**What it does:**  
VLAff unifies three types of affordances that are usually treated separately: **visual affordances** (where to interact), **grasp affordances** (how to grasp), and **trajectory affordances** (the motion path). All three are generated from a single model conditioned on language and visual input.

**Key feature:** Zero-shot transfer to unseen objects and tasks by leveraging the compositional nature of affordances.

**Why it matters:**
Affordance prediction is a critical intermediate step in human-to-robot transfer — humans implicitly understand what objects afford, and robots need the same capability. VLAff's unified approach is more sample-efficient than training separate models for each affordance type.

**Link:** https://arxiv.org (IROS 2026)

---

## 📊 Key Trends This Fortnight

### 1. "Ego-to-Robot Synthesis" Becomes a Recognized Subfield
Ego2Robot joins Pegasus (July 29), SiMDex (Aug 4), and EgoEngine (June) in a rapidly maturing lineage. The common pattern: **human video → structured intermediate representation → robot training data**. The scale is escalating fast (Ego2Robot's 18K hours is ~3× the largest prior effort).

### 2. Tactile Enters the Mainstream
T-Rex's publication and open-sourcing (dataset + code) marks a turning point. The field is moving beyond "vision-only VLAs" toward multimodal policies that exploit touch. Expect more tactile-aware foundation models in the coming months.

### 3. World Models Face the Embodiment Generalization Test
XEWorld's benchmark exposes a critical gap: world models pretrained on one robot often fail on unseen morphologies. This creates demand for works like DyPES-VLA (shared dynamics priors) and EgoWAM (geometry-grounded prediction).

### 4. China-Based Labs Are Driving Scale
Ego2Robot (Renmin Univ), GeniWorld (Tsinghua), DyPES-VLA (HKUST GZ), Xiaomi-Robotics-1 (100K hours, July 16) — Chinese institutions are producing some of the largest-scale robot learning systems. The "data engineering" advantage is becoming visible.

---

## 🔬 Danfei Xu Tracking

**Status:** 📡 Active — Lab publications and continued co-authorship on major works

### New from her lab:
- **EgoWAM** (July 8): World Action Models with egocentric human data from Georgia Tech lab

### Co-authored works this period:
- **T-Rex** (arXiv:2606.17055): Senior author alongside Fei-Fei Li, Jim Fan, Yuke Zhu, Trevor Darrell, and others. This is a major multi-institution collaboration spanning UC Berkeley, NVIDIA, Stanford, and Georgia Tech.
- **SimFoundry** (arXiv 2026): Co-authored with NVIDIA GEAR Lab (Jim Fan, Yunfan Jiang et al.) on automated sim-to-real scene generation

### Ongoing Impact:
Danfei Xu's prior works continue to be foundational references:
- **EgoMimic** (ICRA 2025): Cited in T-Rex, Ego2Robot, and virtually every ego-to-robot paper
- **EgoScale** (arXiv:2602.16710): The scaling law paper is now the primary baseline for dexterous manipulation — T-Rex explicitly compares against it
- **EgoBridge** (NeurIPS 2025): Domain adaptation for cross-embodiment transfer
- **EgoVerse** (arXiv:2604.07607): Large-scale egocentric dataset from around the world

### Research Trajectory Assessment:
Danfei Xu is now operating at two levels simultaneously: (1) **her Georgia Tech lab** produces focused works like EgoWAM that advance the egocentric-to-robot pipeline, and (2) **as a senior collaborator** on large multi-institution projects (T-Rex, SimFoundry, EgoScale), she is shaping the field's direction alongside Fei-Fei Li, Jim Fan, and Trevor Darrell. Her core thesis — that egocentric human video is the most scalable data source for robot learning — is now the dominant paradigm.

---

## 📅 Upcoming Events & Predictions

- **IROS 2026:** October, Pittsburgh — VLAff, RynnVLA-001, and several ego-to-robot papers are accepted
- **Humanoids 2026:** December 6–9, Silicon Valley — expect major humanoid announcements
- **Predicted Trend:** "Tactile-VLA fusion" — following T-Rex, expect works that integrate touch into existing VLA architectures (OpenVLA, π₀) rather than building from scratch
- **Predicted Trend:** "Ego-to-robot at industrial scale" — Ego2Robot's pipeline will likely be replicated and scaled by industrial labs; the "data engineering" phase of embodied AI is here

---

## 📚 Additional Notable Papers

- **JoyAI-RA 0.5** (Aug 6): Scaling robot manipulation via dual action alignment — combines egocentric, simulation, and robot data with separate alignment mechanisms for each
- **World-to-Wrist** (Aug 5, HKUST): Task-conditioned future wrist modeling for fine-grained manipulation — predicts wrist pose instead of end-effector pose for finer control
- **FM-VLA** (July 20, Tsinghua): Force-based Memory for VLAs in contact-rich manipulation — adds force history as non-Markovian memory
- **Representation-Aligned Tactile Grounding** (July 16, Fudan): Aligns tactile representations with VLA action-expert features
- **DreamDojo** (arXiv:2602.06949, ICML 2026): NVIDIA's 44,711-hour world model from human videos — now with real-time 10.81 FPS distilled inference, open weights. Continues to gain citations and downstream adoption as a simulation platform.

---

*龙虾小队 · Paper Radar 🦞*  
*Report generated: 2026-08-19*
