# 🤖 Embodied Intelligence Biweekly Report

**Scan Period:** 2026-09-09 → 2026-09-16 | **Focus:** human-data-training | **Tracking:** Danfei Xu

---

## 🔥 Top 5 Core Highlights

### 1. HuRo: Robotizing Human Videos for Scalable VLA Pretraining (arXiv:2609.10706, Sept 9)

**Team:** Jinho Jeong, Se June Joo, Jaehyun Kang, Dongyun Kim, Yena Kim, Hanjung Kim, Seon Joo Kim — Samsung AI

**What it does:** Builds a robotization pipeline that converts heterogeneous human videos into robot-aligned observations and action trajectories at scale, then uses the robotized data to pretrain VLA policies.

**How it works:** The pipeline handles five human-video sources with varying annotation levels, inferring missing intermediate signals. It produces the **HuRo dataset: ~630K robotized episodes / 142M processed frames**. The key question asked: can robotized human videos provide *effective and scalable* supervision for VLA pretraining?

**Results:** Across four real-world manipulation tasks, increasing robotized pretraining scale improved overall completion from **51.5% → 80.3%**, with gains on OOD generalization as well.

**Why it matters:** This is one of the largest-scale systematic studies of human-video-to-robot pretraining to date. The results make a strong case that robotized human videos are not just a stopgap but a genuinely scalable supervision source — directly addressing the data bottleneck that limits VLA generalization. The "robotization-first, pretrain-second" recipe could become a standard stage in VLA training pipelines.

**Link:** https://arxiv.org/abs/2609.10706

---

### 2. WLA³: World Latent Action Modeling for Semantics, Dynamics, and Kinematics (arXiv:2609.15870, Sept 14)

**Team:** Peidong Liu, Zhiyuan Xiang, Mingyang Li, Wenhao Li, Jiale Zhang, Jiahao Sun, Jiawei Li

**What it does:** Introduces a World Latent Action Model (WLAM) that learns how multimodal world states change over a local interval, producing compact latent actions — then builds a unified generalist policy framework (WLA³) that reuses these representations across semantics, dynamics, and kinematics.

**How it works:** WLAM encodes synchronized camera views and available embodiment-state changes into a compact local latent action plus a richer transition feature. Reconstruction from partial modalities and consistency across overlapping windows encourages robust transition representations. The insight: **observed world transitions offer a common source of action-related supervision** even when explicit hand-action labels are missing — which is the case for the vast majority of egocentric video.

**Why it matters:** This attacks the "noisy action label" problem from a different angle than GeoLAM or RoboTok. Instead of reconstructing what the human hand did, WLAM learns what *changed in the world* and uses that as a supervision signal. This is particularly relevant for scaling to the long tail of unlabeled human video where even hand tracking fails. The three-way reuse (semantics + dynamics + kinematics) from a single representation is architecturally elegant.

**Link:** https://arxiv.org/abs/2609.15870

---

### 3. ReWeight: Leveraging Human Data for VLA Post-Training via Demonstration Retrieval and Sample Weighting (arXiv:2609.13851, Sept 12)

**Team:** Chenwei Wang, Dianye Huang, Match W. L. Ko, Chenjia Bai, Zhongliang Jiang

**What it does:** Addresses a practical but underexplored question — how do you actually *mix* human egocentric data with robot data during VLA post-training without degrading performance?

**How it works:** ReWeight introduces a cross-embodiment visuomotor representation that combines visual observations with future actions to measure behavioral similarity between human and robot demonstrations. It then applies **demonstration-level retrieval** (finding which human demos are actually relevant) and **sample-level weighting** (how much each demo should contribute) during post-training.

**Why it matters:** The naive approach — just mixing human and robot data — often *hurts* performance due to cross-embodiment discrepancies. ReWeight provides a principled way to selectively incorporate human data, which is critical because post-training (not just pretraining) is where most practical VLA deployment effort goes. This sits in the same design space as EgoEngine's mutual-distillation but attacks the post-training stage specifically.

**Link:** https://arxiv.org/abs/2609.13851

---

### 4. GeoLAM: Learning Geometry-Grounded Latent Actions from Unlabeled Human Videos (arXiv:2609.17099, Sept 15)

**Team:** Yifan Xie, Hekun Tian, Jinkun Liu, YuAn Wang, Qiao Sun, Wenbo Ding — CUHK-Shenzhen

**What it does:** Learns latent action representations from *action-free* human videos by grounding them in 3D geometry rather than raw visual reconstruction.

**How it works:** GeoLAM combines future-frame reconstruction through a **frozen geometric feature hierarchy** with motion supervision from a **training-only 4D geometry teacher**. The teacher's predictions yield spatially pooled targets capturing 3D displacement, residual image-plane motion, and surface-orientation changes. Visibility and confidence weighting downweights unreliable estimates. The result: continuous latent actions that retain geometric motion without needing explicit hand pose labels.

**Why it matters:** Most latent action methods (LAM, LAPA, etc.) learn from visual features alone, which can entangle manipulation-relevant motion with appearance changes and camera movement. GeoLAM's geometry-first approach produces cleaner action representations — a potential upgrade for any downstream pipeline that consumes latent actions from human video (world models, VLA pretraining, etc.). This is especially relevant for in-the-wild egocentric video where camera motion is unpredictable.

**Link:** https://arxiv.org/abs/2609.17099

---

### 5. UniDex-ViTac: Unified Visuo-Tactile Dexterous Manipulation Policy from Human Video Data (arXiv:2609.16504, Sept 15)

**Team:** Hyesung Lee, Si-Hwan Heo, Sungwook Yang

**What it does:** Uses human-video-guided simulation to generate robot demonstrations paired with fingertip contact observations — training a single deployable visuo-tactile policy for dexterous manipulation.

**How it works:** Object-specific residual RL specialists adapt annotated human-object interaction references to a robotic arm-hand system. Their successful rollouts pair final robot action targets with robot-side fingertip contact observations. From **just 50 human demonstrations across ten objects**, the system collects **10,000 simulated trajectories** to train a single ACT-based generalist policy. The policy consumes point clouds, proprioception, and four binary contact signals.

**Why it matters:** This continues the "simulation as a data completion engine" theme (cf. Dex-X, arXiv:2609.07747), but with a focus on *tactile* completion — human videos show you what happened but not what was *felt*. The 200× data amplification (50 demos → 10K trajectories) demonstrates how simulation can bridge both the embodiment gap and the sensing gap. Visuo-tactile policies are increasingly seen as necessary for contact-rich tasks where vision alone is insufficient.

**Link:** https://arxiv.org/abs/2609.16504

---

## 📡 Trend Radar

- **Human-video robotization is hitting industrial scale.** HuRo's 630K episodes from five sources is the largest robotization effort we've seen from an industry lab. Combined with ReWeight's post-training recipe and WLA³'s transition-based supervision, the "human video as first-class training data" story is getting very concrete — multiple complementary entry points are maturing simultaneously.
- **Geometry as a supervisory signal is back.** GeoLAM (4D geometry teacher), GeoDP (spatial-temporal geometric consistency), and Dex-X (simulated contact geometry) all use geometric structure to replace or augment action labels. This is a meaningful shift from pure appearance-based learning.
- **Tactile is going mainstream in human-data pipelines.** Three papers this window touch visuo-tactile learning from human data: UniDex-ViTac, STAR (200-hour visuo-tactile-language dataset, arXiv:2609.12549), and GIFT (force-aware glove-to-robot transfer, arXiv:2609.14173). The question is shifting from "do we need touch?" to "how do we get touch signals from human video?"
- **VLA training efficiency is getting its own literature.** "What Makes an Efficient VLA?" (arXiv:2609.13984) and the REAL-I Challenge retrospective (arXiv:2609.13679) both tackle the practical question of extracting maximum performance from limited demonstration budgets — increasingly important as VLA deployments move from lab demos to production.

---

## 🔬 Danfei Xu Lab Tracking

**🏆 CoRL 2026 Acceptance Round (September)**

The RL2 lab had a strong CoRL 2026 cycle:
- **EgoWAM** (Baoyu Li, Xinchen Yin, Mengying Lin, Yixin Zhang, Danfei Xu) — accepted at CoRL 2026. Also received the **Distinguished Poster Award** at the Meta Research Summit for Egocentric Intelligence (RSIE) 2026. EgoWAM systematically studies WAM state representations for bridging the human-robot embodiment gap, showing policy performance can scale with in-the-wild egocentric human data where naive BC co-training fails. [arXiv:2607.08436]
- **Human2Any** (Shuo Cheng et al.) — CoRL 2026. Human-to-robot transfer via constraint-aware compositional planning.
- **WT-UMI** — CoRL 2026. Whole-body teleoperation / humanoid manipulation.
- **EgoEngine** — CoRL 2026 (previously RSS 2026). [arXiv:2606.12604]
- **SIDO** — CoRL 2026.

**🎓 NSF CAREER Award**
Danfei Xu received the NSF CAREER award for research on **"on-the-job" robot training** — enabling robots to self-improve based on performance, new requirements, and user preferences in each deployment environment. The project frames robot learning as a continual, post-deployment process rather than a factory-complete product.

**📊 Context for Our Focus**
The lab's trajectory this year has been consistent: egocentric human data (EgoVerse → EgoEngine → EgoWAM) → action learning (WLAM-adjacent) → humanoid deployment (WT-UMI, SIDO). The CoRL acceptance cluster confirms that human-data-driven robot learning is the lab's core thesis, not a side project. Worth watching for: any follow-up to EgoWAM that connects WAM state representations to downstream policy scaling laws.

---

## 📋 Other Works Worth Noting

| Paper | arXiv ID | Date | One-liner |
|-------|----------|------|-----------|
| STAR: Sparse Tactile Representation in VTLA Models | 2609.12549 | Sept 11 | 200-hour bimanual visuo-tactile dataset + VTLA training recipe for dexterous manipulation |
| GIFT: Glove-Inferred Force Transfer | 2609.14173 | Sept 12 | Force-aware human-to-robot skill transfer via wearable sensing glove, no tactile sensors needed on robot |
| World Models for Embodied Intelligence Survey | 2609.16697 | Sept 15 | "From Plausible to Controllable to Actionable" — comprehensive world model survey |
| World-Action Models for Robot Learning Survey | 2609.16074 | Sept 13 | Systematic overview of WAM landscape (EgoWAM, DreamDojo, etc.) |
| What Makes an Efficient VLA? | 2609.13984 | Sept 12 | Navigating action-head design, scaling, and latency tradeoffs |
| How to Better Train VLAs (REAL-I Challenge) | 2609.13679 | Sept 12 | Lessons from ICRA 2026 challenge on fixed-budget VLA training |
| Dex-X (v2 update) | 2609.07747 | Sept 9 | Visual-tactile dexterous manipulation from human videos via simulation as tactile completion engine |
| OpenWAM | 2609.07398 | Sept 7 | Open, modular exploration toward systematic WAM pretraining |

---

## 🔗 Key Links

- HuRo: https://arxiv.org/abs/2609.10706
- WLA³: https://arxiv.org/abs/2609.15870
- ReWeight: https://arxiv.org/abs/2609.13851
- GeoLAM: https://arxiv.org/abs/2609.17099
- UniDex-ViTac: https://arxiv.org/abs/2609.16504
- STAR: https://arxiv.org/abs/2609.12549
- GIFT: https://arxiv.org/abs/2609.14173
- EgoWAM (CoRL 2026): https://arxiv.org/abs/2607.08436

---

*Report generated: 2026-09-16 | Paper Radar 🦞 Embodied Biweekly*
