# Paper Radar Weekly — World Models | 2026-W26

**扫描时间：** 2026-06-21 (Sun)  
**本周领域：** World Models（世界模型）  
**扫描范围：** arXiv + 社区热点 + 会议论文  

---

## 🔥 本周 Top 5 最值得关注

### 1️⃣ **LeWorldModel (LeWM)** (arXiv:2603.19312, Mar 13) — 第一个真正稳定端到端训练的 JEPA
**核心：** 现有 JEPA 方法依赖复杂多损失项、EMA、预训练编码器或辅助监督来避免表征坍缩。LeWM 只用 **两个损失项**（next-embedding prediction + Gaussian-distributed latent regularizer）就实现了稳定端到端训练。
**为什么重要：** 把可调超参从 6 个降到 1 个。~15M 参数，单 GPU 几小时训练完。在 2D/3D 控制任务上**比 foundation-model-based world models 快 48x** 规划速度。latent space 能通过探测编码有意义的物理结构（如物体位置、速度），且能检测物理上不合理的事件（surprise evaluation）。
**亮点：** 极简主义胜利——证明 JEPA 不需要 VICReg 七项损失、不需要 frozen DINOv2、不需要 stop-gradient。SIGReg 正则化器 asking a single question: "does the embedding cloud look like an isotropic Gaussian from a thousand random angles?"

### 2️⃣ **C-JEPA** (arXiv:2602.11389, May 28 v2) — 因果干预驱动的 Object-Centric JEPA
**核心：** 将 patch-level masked prediction 扩展到 object-centric representation，通过 object-level masking 创造"反事实式"预测查询：每个被 mask 的物体状态必须从周围物体推断，迫使模型学习交互依赖的动力学。
**为什么重要：** 现有 object-centric 方法能抽象物体，但不足以捕捉交互依赖动力学。C-JEPA 在 visual question answering 上提升约 **20%**（counterfactual reasoning），在 agent control 上仅用 patch-based world models **1% 的 latent input features** 就达到可比性能。形式化证明 object-level masking 通过控制可观测性诱导了因果归纳偏置。
**亮点：** 从 patch 到 object 的 masking 升级，不只是架构改进，而是对学习目标的结构性干预。

### 3️⃣ **TD-JEPA** (ICLR 2026) — 零样本强化学习的 latent-predictive 表征
**核心：** 将 temporal difference learning 与 JEPA 的 latent prediction 结合，学习零样本迁移的 predictive representations。
**为什么重要：** 世界模型在 RL 中的核心问题是 learned representations 能否支持零样本迁移到未见任务。TD-JEPA 证明 joint-embedding predictive representations 通过 TD-style bootstrapping 可以获得 task-agnostic 的动力学表征，为 world model-based RL 的泛化能力提供理论支撑。
**亮点：** ICLR 2026 接受，代表了 JEPA 方法论从自监督预训练向强化学习范式的正式扩展。

### 4️⃣ **JEDI** (arXiv 2026-05) — Joint Embedding Diffusion World Model for Online RL
**核心：** 第一个 **online end-to-end latent diffusion world model** for model-based RL。将 JEPA 与 diffusion denoising 结合，直接从 world-model objectives 学习 latent space，避免单独预训练。
**为什么重要：** 理论上证明 JEPA 诱导 predictive information bottleneck，而 diffusion denoising 实现 predictive-compression decomposition。在 Atari100k 上匹配 SOTA，**VRAM 减少 43%，采样快 3x，训练快 2.5x**。代表了生成式世界模型（diffusion）与判别式世界模型（JEPA）的融合方向。
**亮点：** 不是用 diffusion 生成像素，而是在 latent space 做 diffusion，效率更高。

### 5️⃣ **Phys-JEPA** (arXiv:2606.15xxx, Jun 15) — 物理信息潜空间世界模型
**核心：** 将 physics-informed learning 从 output space 搬到 **latent predictive state space**。预测状态被分解为 physical component 和 residual component，物理一致性直接施加在 latent states 和 latent transitions 上。
**为什么重要：** 这是 JEPA 与 Physics-informed AI（上周 W25 的领域）的**直接交叉**。在 Jena Climate 数据集上，aggregate MSE 从 0.12482 降到 0.12273（H=24）；在 Traffic 数据集上 H=192 的 MSE 从 0.800784 降到 0.773873。证明物理约束在 latent space 比在 output space 更有效。
**亮点：** 物理 + 世界模型 的交叉信号，回应了上周关于两领域交叉的疑问。

---

## 📌 其他值得注意的论文

- **World Model for Robot Learning: A Comprehensive Survey** (arXiv:2605.00080, Apr 30) — 18 位作者（含 Berkeley, Stanford, ETH, Cambridge）的系统综述，涵盖 world models 作为 learned simulators、RL 训练、robotic video generation 到导航和自动驾驶的完整脉络。社区急需的 map。
- **WAM-Nav** (arXiv:2606.04907) — 用共享 DiT 做 asymmetric joint diffusion，同时生成长期 action 和短期 visual foresight。Image-Goal 导航成功率提升 15.7%，物理机器人 sim-to-real 85% 成功率。
- **MotionWAM** (arXiv:2606.09215, Jun 8) — 实时 WAM 驱动人形机器人 loco-manipulation，单 egocentric camera 输入。世界动作模型正在进入人形机器人实时控制领域。
- **HiMem-WAM** (arXiv:2606.10363, Jun 9) — Hierarchical Memory-Gated World Action Models，为长程机器人操作引入层次化记忆门控机制。
- **WorldDP** (arXiv:2606.08775) — 将 object-centric world models 与 diffusion policy 统一，用于多阶段机器人任务。世界模型在粒子滤波中优化 subgoals，底层 diffusion policy 执行。
- **Dit4Dit** (arXiv:2603.10448) — 联合建模 video dynamics 和 actions，用 DiT 做通用机器人控制，可 zero-shot 泛化到新环境。
- **NoiseGate** (arXiv:2605.07794) — 学习 per-latent timestep schedules 作为 world action models 中的任务自适应信息门，优化 diffusion-based WAM 的去噪效率。
- **DreamDojo** (arXiv:2602.06949, Feb 2026) — NVIDIA GEAR 团队重磅工作。从 44k 小时 egocentric 人类视频预训练的机器人基础世界模型，用连续潜在动作统一跨具身动作表示，支持实时遥操作、策略评估和基于模型的规划。10.81 FPS 实时蒸馏，代表了「人类视频预训练 + 世界模型」路线的关键工程突破。与 WAM 系列工作（如 World Action Models arXiv:2602.15922）同频共振。

---

## 📅 轮换进度

Physics-informed AI ✅ → **World Models ✅（本周 W26）** → AI Infra 📅（下周 W27） → Deep Learning 📅 → Embodied Intelligence 📅

---

## 🔍 领域趋势观察

**本周主题：JEPA 的「从复杂到极简」与 WAM 的「从预测到行动」**

1. **JEPA 进入极简时代：** LeWM 证明 2 个 loss terms 就能稳定训练端到端 JEPA，这可能会重新定义 world model 的训练门槛。不再是「需要 foundation model + 大量超参调优」的精英游戏。
2. **Object-Centric 是必经之路：** C-JEPA 和 WorldDP 都指向同一个方向——patch-level 的 latent prediction 不够，需要 object-level 的结构化推理。这与具身智能领域对 object-centric representation 的追求一致。
3. **World Action Models (WAM) 爆发：** 2026 年 6 月出现了 WAM 论文的井喷（MotionWAM, HiMem-WAM, WAM-Nav, NoiseGate, Gigaworld-Policy 等）。WAM 将世界模型从「纯预测器」升级为「预测-行动联合模型」，是 world models 向 embodied control 落地的关键一步。
4. **JEPA × Physics 的交叉：** Phys-JEPA 直接把物理约束嵌入 latent predictive state，验证了上周关于 Physics-informed AI 和 World Models 交叉的猜想。这个方向（latent physics）值得长期关注。
5. **Survey 出现信号：** 18 位顶校作者的 comprehensive survey 说明 world models for robotics 已经成熟到需要一个统一框架来梳理。领域从「explosion」进入「consolidation」阶段。

---

## 🤖 Machine Metadata — For Kimi Work Auto-Ingest

```yaml
# Paper Radar Weekly — Machine Readable Block
# Format: YAML 1.2 | Encoding: UTF-8
# Generated: 2026-06-21T09:17:00+08:00
# Week: 2026-W26
# Domain: World Models

papers:
  - arxiv_id: "2603.19312"
    title: "LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels"
    pdf_url: "https://arxiv.org/pdf/2603.19312.pdf"
    abstract_url: "https://arxiv.org/abs/2603.19312"
    category: "World Models"
    sub_tags: ["JEPA", "end-to-end", "minimal", "latent-dynamics", "control"]
    priority: "top3"
    one_liner: "2个损失项实现稳定端到端JEPA，15M参数单GPU训练，规划速度48x"
    authors: "Maes, Le Lidec, Scieur, LeCun, Balestriero"
    published: "2026-03-13"
    has_pdf: true

  - arxiv_id: "2602.11389"
    title: "C-JEPA: Learning World Models through Object-Level Latent Interventions"
    pdf_url: "https://arxiv.org/pdf/2602.11389.pdf"
    abstract_url: "https://arxiv.org/abs/2602.11389"
    category: "World Models"
    sub_tags: ["JEPA", "object-centric", "causal", "counterfactual", "VQA"]
    priority: "top3"
    one_liner: "object-level masking制造反事实预测，因果推理提升20%"
    authors: "Nam, Le Lidec, Maes, LeCun, Balestriero"
    published: "2026-02-11"
    has_pdf: true

  - arxiv_id: null
    title: "TD-JEPA: Latent-Predictive Representations for Zero-Shot Reinforcement Learning"
    pdf_url: null
    abstract_url: "https://openreview.net/forum?id=SzXDuBN8M1"
    category: "World Models"
    sub_tags: ["JEPA", "RL", "zero-shot", "TD-learning", "ICLR2026"]
    priority: "top3"
    one_liner: "JEPA+TD学习实现零样本强化学习迁移"
    authors: "Bagatella, Pirotta, Touati, Lazaric, Tirinzoni"
    published: "2026"
    venue: "ICLR 2026"
    has_pdf: false
    note: "会议论文，PDF从OpenReview获取"

  - arxiv_id: "2605.???"
    title: "JEDI: Joint Embedding Diffusion World Model for Online Model-Based Reinforcement Learning"
    pdf_url: "https://arxiv.org/pdf/2605.???.pdf"
    abstract_url: "https://arxiv.org/abs/2605.???"
    category: "World Models"
    sub_tags: ["JEPA", "diffusion", "online-RL", "latent-diffusion", "Atari"]
    priority: "top5"
    one_liner: "首个在线端到端潜空间扩散世界模型，VRAM减43%"
    authors: "Lim, Shah, Ikram, Yu"
    published: "2026-05-13"
    has_pdf: true
    note: "arxiv_id需确认"

  - arxiv_id: null
    title: "Phys-JEPA: Physics-Informed Latent World Models for Multivariate Time-Series Forecasting"
    pdf_url: null
    abstract_url: null
    category: "World Models"
    sub_tags: ["JEPA", "physics-informed", "time-series", "latent-constraint"]
    priority: "top5"
    one_liner: "物理约束从输出空间搬到潜空间预测状态，JEPA×Physics交叉"
    authors: "[unknown]"
    published: "2026-06-15"
    has_pdf: false
    note: "Preliminary manuscript，arxiv_id待确认"

  - arxiv_id: "2605.00080"
    title: "World Model for Robot Learning: A Comprehensive Survey"
    pdf_url: "https://arxiv.org/pdf/2605.00080.pdf"
    abstract_url: "https://arxiv.org/abs/2605.00080"
    category: "World Models"
    sub_tags: ["survey", "robot-learning", "review", "embodied-AI"]
    priority: "honorable-mention"
    one_liner: "18位顶校作者系统综述机器人学习中的世界模型"
    authors: "Hou, Li, Jia, An, Guo, Leng, Geng, Ze, Harada, Torr, Mees, Pollefeys, Liu, Wu, Abbeel, Malik, Du, Yang"
    published: "2026-04-30"
    has_pdf: true

  - arxiv_id: "2606.09215"
    title: "MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation"
    pdf_url: "https://arxiv.org/pdf/2606.09215.pdf"
    abstract_url: "https://arxiv.org/abs/2606.09215"
    category: "World Models"
    sub_tags: ["WAM", "humanoid", "loco-manipulation", "real-time"]
    priority: "honorable-mention"
    one_liner: "实时世界动作模型驱动人形机器人全身操作，单目相机输入"
    authors: "[multiple]"
    published: "2026-06-08"
    has_pdf: true

  - arxiv_id: "2606.10363"
    title: "HiMem-WAM: Hierarchical Memory-Gated World Action Models for Robotic Manipulation"
    pdf_url: "https://arxiv.org/pdf/2606.10363.pdf"
    abstract_url: "https://arxiv.org/abs/2606.10363"
    category: "World Models"
    sub_tags: ["WAM", "memory", "hierarchical", "manipulation"]
    priority: "honorable-mention"
    one_liner: "层次化记忆门控世界动作模型，服务长程机器人操作"
    authors: "Sun et al."
    published: "2026-06-09"
    has_pdf: true

  - arxiv_id: "2606.04907"
    title: "WAM-Nav: Asymmetric Latent World-Action Modeling for Unified Visual Navigation"
    pdf_url: "https://arxiv.org/pdf/2606.04907.pdf"
    abstract_url: "https://arxiv.org/abs/2606.04907"
    category: "World Models"
    sub_tags: ["WAM", "navigation", "DiT", "diffusion", "sim-to-real"]
    priority: "honorable-mention"
    one_liner: "共享DiT非对称联合扩散，同时生成长期动作和短期视觉预见，sim-to-real 85%"
    authors: "[multiple]"
    published: "2026-06"
    has_pdf: true

  - arxiv_id: "2606.08775"
    title: "Unifying Object-Centric World Models and Diffusion Policy: A Hierarchical Framework for Multi-Stage Robotic Tasks"
    pdf_url: "https://arxiv.org/pdf/2606.08775.pdf"
    abstract_url: "https://arxiv.org/abs/2606.08775"
    category: "World Models"
    sub_tags: ["object-centric", "diffusion-policy", "hierarchical", "multi-stage"]
    priority: "honorable-mention"
    one_liner: "物体-centric世界模型+粒子滤波优化subgoals+底层diffusion policy执行"
    authors: "[multiple]"
    published: "2026-06-27"
    has_pdf: true

  - arxiv_id: "2602.06949"
    title: "DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos"
    pdf_url: "https://arxiv.org/pdf/2602.06949.pdf"
    abstract_url: "https://arxiv.org/abs/2602.06949"
    category: "World Models"
    sub_tags: ["world-model", "robotics", "latent-actions", "human-videos", "NVIDIA", "distillation"]
    priority: "honorable-mention"
    one_liner: "44k小时人类视频预训练的世界模型，连续潜在动作统一跨具身表示，10.81FPS实时蒸馏"
    authors: "Gao, Liang, Zheng, Malik, Ye, Yu, Tseng, Dong, Mo, Lin, Ma, Nah, Magne, Xiang, Xie, Zheng, Niu, Tan, Zentner, Kurian, Indupuru, Jannaty, Gu, Zhang, Malik, Abbeel, Liu, Zhu, Jang, Fan"
    published: "2026-02-06"
    has_pdf: true
    note: "补充收录，NVIDIA GEAR团队"

rotation:
  current_week: "W26"
  current_domain: "World Models"
  next_domain: "AI Infra"
  next_week: "W27"
  schedule:
    - { week: "W21", domain: "World Models", status: "done" }
    - { week: "W22", domain: "AI Infra", status: "done" }
    - { week: "W23", domain: "Deep Learning", status: "done" }
    - { week: "W24", domain: "Physics-informed AI", status: "skipped" }
    - { week: "W25", domain: "Physics-informed AI", status: "done" }
    - { week: "W26", domain: "World Models", status: "done" }
    - { week: "W27", domain: "AI Infra", status: "pending" }

meta:
  total_papers_found: 10
  top3_count: 3
  top5_count: 5
  honorable_mention_count: 5
  non_arxiv_count: 1
  report_version: "1.0"
  cross_domain_signals: ["Physics-informed AI × JEPA (Phys-JEPA)"]
```

---

*龙虾小队 · Paper Radar 🦞*  
*自动扫描，手动精选，每周日见。*
