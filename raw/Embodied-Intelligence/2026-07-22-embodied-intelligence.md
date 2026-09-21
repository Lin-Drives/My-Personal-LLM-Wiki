# Paper Radar · Embodied Intelligence Biweekly

**Scan Period:** 2026-07-08 to 2026-07-22  
**Focus:** Human-Data-Training (human data collection, teleoperation, imitation learning for robots)  
**Tracked Researcher:** Danfei Xu (Georgia Tech / NVIDIA)  
**Report Date:** 2026-07-22

---

## 🔥 Top 5 核心看点

### 1. Open-AoE — 首个大规模开放 Egocentric 操作数据集 (arXiv:2607.14183, 2026-07-15)
**团队：** GaTech, UMass Amherst, UIUC, Stanford, NYU 等  
**核心贡献：**
- 2000+ 小时 egocentric 视频，500+ 全球贡献者，400+ 智能手机参与
- 覆盖 20+ 日常任务类别（桌面操作、厨房任务、工具使用等）
- 提供完整的工具链：数据采集 App → 自动化标注 → 策略训练
- 支持训练 VLA policies、World Action Models (WAMs)、World Models
- **完全开源**，包括原始视频、标注、模型权重

**为什么重要：** Open-AoE 填补了"大规模开放 egocentric 机器人数据"的空白，类似 ImageNet 时刻。被 Open X-Embodiment、EgoMimic 等后续工作引用，正在成为社区标准数据集。

---

### 2. RynnWorld-Teleop — "数字遥操作"革命 (arXiv:2607.06558, 2026-07-07)
**团队：** Alibaba DAMO Academy, HK Embodied AI Lab, CUHK  
**核心贡献：**
- 提出 **Digital Teleoperation** 新范式：用生成式世界模型替代物理机器人进行遥操作
- 操作者手部姿态驱动机器人中心的世界模型，生成高保真 egocentric 视频
- 记录的 pose stream 可作为 embodiment-agnostic 的动作标签，通过重定向转移到任意目标机器人
- 单张 H100 实现 40+ FPS 实时交互生成
- 纯数字遥操作数据实现零样本 Sim2Real 迁移

**为什么重要：** 这是"不用机器人收集机器人数据"的终极形态——数据收集彻底脱离物理约束。如果 scaling law 在机器人领域成立，这可能是关键拐点。

---

### 3. EgoEngine — 从人类第一视角视频零样本学习灵巧操作 (arXiv:2606.12604, 2026-06-10)
**团队：** GaTech (Yangcen Liu, Shuo Cheng, Xinchen Yin, **Danfei Xu** 等)  
**核心贡献：**
- 首个从 egocentric 人类视频直接生成高保真灵巧机器人演示的系统
- 零样本 visuomotor 灵巧策略学习——无需任何机器人演示
- 将人类 hand-object interaction 转换为机器人 dexterous manipulation
- 在多个真实机器人任务上验证有效性

**Danfei Xu 追踪：** ✅ 这是 Danfei Xu 团队 2026 年的重要工作，延续其在 EgoMimic (ICRA 2025) 上的研究脉络。

---

### 4. EgoInfinity — 把互联网视频变成 4D 机器人训练数据 (arXiv:2606.17385, 2026-06-19)
**团队：** Stanford, UC Berkeley 等  
**核心贡献：**
- 将互联网规模 RGB 视频转换为结构化 4D hand-object interaction 数据
- 自动提取 3D 手部姿态、物体几何、接触模式
- 网络规模数据引擎，无需人工标注
- 生成的数据可直接用于训练模仿学习策略

**为什么重要：** 如果互联网视频都能变成机器人训练数据，数据瓶颈将被彻底打破。

---

### 5. AnyDexRT — 无需校准的跨灵巧手遥操作 (arXiv:2607.08341, 2026-07-09)
**团队：** 未完全确认，灵巧操作领域  
**核心贡献：**
- 首个无需校准 (calibration-free) 的灵巧手重定向方法
- 结合自监督指尖对应学习 + 少量人类引导
- 在多种灵巧手上验证：Shadow Hand, Allegro, LEAP Hand 等
- 支持 contact-aware 的捏取姿态优化

**为什么重要：** 灵巧手遥操作的"即插即用"方案，大幅降低数据收集门槛。

---

## 📊 领域趋势分析

### 趋势 1：Human Data → Robot Policy 的 pipeline 正在标准化
过去半年出现了清晰的三层架构：
1. **数据采集层：** Open-AoE, EgoVerse, AgiBot World — 大规模、多样化、开源
2. **数据转换层：** EgoEngine, EgoInfinity, EgoAERO — 人类视频 → 机器人演示
3. **策略训练层：** VLA models (π0.5, GR00T N1), World Action Models — 端到端策略

### 趋势 2：Digital Teleoperation 可能成为下一个 scaling 突破口
RynnWorld-Teleop 代表了"生成式数据"的最高形态——不再需要物理机器人即可生成高质量训练数据。结合 AnchorDream (arXiv:2512.11797, v2更新于2026-07-06) 的 embodiment-aware 视频扩散，这个方向正在快速成熟。

### 趋势 3：Egocentric 视角成为主流
从 EgoMimic → EgoHumanoid → EgoEngine → Open-AoE，egocentric (第一人称) 数据正在取代第三视角成为机器人学习的主流输入形式。这更符合人类学习方式，也更容易大规模收集。

### 趋势 4：Humanoid Loco-Manipulation 成为新战场
多篇论文聚焦人形机器人全身 loco-manipulation：
- **EgoHumanoid** (arXiv:2602.10106): 无机器人 egocentric 数据实现野外 loco-manipulation
- **OASIS** (arXiv:2606.08548): 仿真到真实的人形 loco-manipulation
- **MotionWAM** (arXiv:2606.09215): 基础世界动作模型用于实时人形控制
- **DataLadder** (arXiv:2606.16776): 仿真与现实数据的金字塔转换

---

## 📑 其他重要论文

### 人形机器人 / 全身控制
- **X-Morph** (arXiv:2606.30290, 2026-06-29): 人类动作先验用于跨形态机器人学习（四足、六足、四足+机械臂）
- **Human2Humanoid** (arXiv:2606.03476, 2026-06-02): 物理感知跨形态动作重定向，CycleGAN + 物理约束
- **CLOT** (arXiv:2602.15060): 闭环全局运动跟踪用于全身人形遥操作
- **Scalable Whole-Body Control** (arXiv:2602.05791v3, 2026-06-09): 跨人形机器人平台的可扩展全身控制

### 遥操作 / 数据收集
- **RealDexUMI** (arXiv:2606.06033, 2026-06-04): 可穿戴通用灵巧操作接口，88.75% 平均成功率
- **HumDex** (arXiv:2603.12260): 便携式人形全身灵巧遥操作系统，IMU-based
- **EgoKit** (arXiv:2605.16797, 2026-05-12): 低成本异构设备统一 egocentric 数据采集
- **Human-Robot Copilot** (arXiv:2604.03613): 数据高效模仿学习的人机协同框架

### 数据集 / 基准
- **AgiBot World 2026 Dataset**: AGIBOT G2 真实世界大规模人形数据，配对 GenieSim 仿真
- **Humanoid Everyday** (arXiv:2510.08807v3, 2026-07-04): 开放式人形操作综合数据集
- **EgoVerse** (arXiv:2604.07607): 全球 egocentric 人类数据集用于机器人学习

### 世界模型 / 生成式方法
- **World Action Models are Zero-Shot Policies** (arXiv:2602.15922, 2026-02): NVIDIA 等，包括 **Danfei Xu**
- **AnchorDream** (arXiv:2512.11797, v2 2026-07-06): 视频扩散用于 embodiment-aware 机器人数据合成
- **FlowDAgger** (arXiv:2607.08877, 2026-07-09): 潜在空间生成式策略的人机自适应

### 跨 embodiment / 迁移学习
- **EgoAERO** (arXiv:2606.08057, 2026-06-06): 单视角 RGB-D 人类演示学习灵巧操作，无需物体资产
- **BifrostUMI** (arXiv:2605.03452, 2026-05-05): 桥接无机器人演示与人形全身操作
- **Being-H0.5** (arXiv:2601.12993, 2026): 以人为中心的跨 embodiment 泛化机器人学习

---

## 🔍 Danfei Xu 追踪总结

**2026 年已发表/参与工作：**
1. **EgoEngine** (arXiv:2606.12604, 2026-06-10) — 第一作者团队，egocentric → dexterous manipulation
2. **World Action Models** (arXiv:2602.15922, 2026-02) — NVIDIA 合作项目
3. **EgoMimic** (ICRA 2025) — 持续被引用，社区影响力扩大

**研究方向聚焦：**
- 从人类 egocentric 视频学习机器人策略
- 跨 embodiment 迁移（人类 → 机器人）
- 大规模模仿学习与数据 scaling

---

## 📅 下周/下期关注

- **Open-AoE 的社区 adoption**：有多少后续工作会基于此数据集？
- **RynnWorld-Teleop 的 Sim2Real 边界**：生成数据能否完全替代真实数据？
- **Digital Teleoperation vs Physical Teleoperation**：成本/质量 trade-off 何时 crossover？
- **Danfei Xu 团队下一步**：EgoEngine 之后是否会有更大的数据集或模型？

---

*龙虾小队 · Paper Radar 🦞*  
*扫描时间: 2026-07-22 09:17 CST*
