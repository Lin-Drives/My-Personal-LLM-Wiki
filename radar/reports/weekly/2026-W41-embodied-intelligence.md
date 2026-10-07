# 🤖 Embodied Intelligence 周报 · 2026-09-28 ~ 2026-10-04 (W41)

> **扫描周期：** 2026-09-28 → 2026-10-04
> **领域：** Embodied Intelligence（human-data-training 重点追踪 · Danfei Xu 动态）
> **核心趋势：** 人类第一视角数据（Egocentric Human Data）正式成为人形机器人预训练的"标准燃料"——本周三篇独立工作同时给出规模化实证，其中 IronMind 首次报告 log-linear scaling law，EgoHumanoid-V2 首次实现协调全身技能的零样本迁移。"人类视频 = 人形机器人的互联网"这个等式，正在被快速填实。

---

## 🔥 Top 5 核心看点

### 1. λ₀ (lambda_0) + HumanVerse-500：500 小时人类全身数据喂出全身人形 VLA

- **关键词：** egocentric whole-body data, humanoid loco-manipulation, VLA, 三阶段训练
- **机构：** Salesforce（Steven C.H. Hoi 团队）
- **链接：** [arXiv:2610.00438](https://arxiv.org/abs/2610.00438)（2026-09-30）
- **技术核心：** 提出 HumanVerse-500——500 小时第一人称人类全身操作数据集，用轻量可穿戴系统同步采集 ego 视频 + 身体运动 + 手部运动。在此之上构建 λ₀ 全身人形 VLA：三阶段训练（① 从大规模 ego 数据学交互 → ② 用 HumanVerse-500 协调身体与手部运动 → ③ 下游任务/本体适配）。三阶段共享同一表征空间完成"人类经验迁移"，领域专用接口处理人机状态/动作差异。
- **数据与效果：** 在 SIMPLE 基准 + 4 个真实 loco-manipulation 任务上达到 SOTA；论文系统分析了 scaling 行为、泛化性和各训练阶段的贡献（消融做得相当扎实）。代码、模型、数据承诺全部开源。
- **为什么重要：** 第一个系统性地把「第一人称人类全身数据」用于全身人形 loco-manipulation 的 VLA——绕开了人形遥操作"贵且难规模化"的死结。与 λ₀ 同一批作者的 EgoHumanoid-V2（见 #3）形成组合拳：一个做数据集+预训练，一个做迁移机制。

### 2. IronMind：万小时第一人称预训练，相机空间动作表示直接拆掉 embodiment gap

- **关键词：** camera-space action representation, scaling law, Mixture-of-Transformers, flow matching
- **机构：** 工业界团队（真实机器人部署于 IRON-R01 人形平台）
- **链接：** [arXiv:2609.39403](https://arxiv.org/abs/2609.39403)（2026-09-30）
- **技术核心：** 两大洞见。① **相机空间动作表示**：低成本 ego 视频没有躯干运动学，传统重argeting走不通——干脆把动作表示在相机坐标系（ego 视频的原生参考空间），人机动作维度做语义对齐，完全绕过显式身体重定向。② **数据引擎**：规则过滤 + 原子任务重标注 + 逐帧质量加权，把 10,000+ 小时 heterogeneous 数据（ego 人类视频 + 非目标本体机器人数据）清洗成可用语料。架构为双专家 MoT（VL 理解专家 + flow-matching 动作专家），训练期可挂语义/几何/视频动力学辅助监督、推理期全部拆掉。
- **数据与效果：** 预训练验证损失从 250h 到 10,000h 呈 log-linear 下降（斜率 −0.058/数量级，未饱和）；真实机器人 6 个 OOD 任务平均成功率 **55.0%**（≤5000h 的所有预算最多 11.7%，无预训练 5.0%）；相机空间 vs 躯干坐标基线 = 55.0% vs 26.7%（同数据同预算）；优于 InternVLA-A1.5 同数据后训练基线（30.0%）。
- **为什么重要：** 人形灵巧操作预训练的**第一个 scaling law 实证**——数据加数量级，性能还在涨，没见顶。而且"相机空间"这个选择既优雅又实用：ego 视频本来就长在相机坐标系里，重argeting 本来就是多余的中间层。附赠一个反直觉发现：world-prior 辅助监督在真实机器人上反而掉点（55.0%→31.7%），辅助预测目标与接触-rich 闭环控制存在错配。

### 3. EgoHumanoid-V2：首个第一人称人类→人形「协调全身技能」零样本迁移

- **关键词：** human-to-humanoid transfer, whole-body loco-manipulation, coarse-to-fine action alignment
- **机构：** 上海 AI Lab（Hongyang Li）+ Salesforce（Steven Hoi）
- **链接：** [arXiv:2609.37181](https://arxiv.org/abs/2609.37181)（2026-09-29）
- **技术核心：** 之前的 ego 迁移工作都停留在「场景泛化」+ 解耦控制（上身操作下身走路分开管）。本文攻的是更难的问题：**协调的全身 loco-manipulation 技能直接迁移**。核心是 coarse-to-fine 动作对齐——运动学参考校正（修末端位姿精度）+ 动力学感知精修（保全身协调性）；再叠加 robot-arm rendering 与训练时图像增强，缩小视觉 embodiment gap、提升视角鲁棒性。
- **数据与效果：** 4 个真实世界任务上，用对齐后的人类数据训练 VLA，**零样本**技能迁移（无目标任务机器人演示），任务分数与遥操作数据训练的 policy 相当——而采集成本低得多。
- **为什么重要：** 把"人类数据 = 直接技能监督"（direct skill supervision）从口号变成可复现的流程。对 human-data-training 社区的意义在于：迁移瓶颈不在数据量，而在**对齐质量**——这一篇把对齐做到了全身动力学级别。Danfei Xu 线的 EgoMimic/EgoVerse 证明了"能用"，EgoHumanoid-V2 证明了"能用到协调全身"。

### 4. UVTA：人类演示统一视觉-触觉-动作建模，灵巧操作的触觉规模化路线

- **关键词：** visuo-tactile-action, human-robot co-training, dexterous manipulation, diffusion policy
- **机构：** North robot + 22-DoF Sharpa Wave 灵巧手团队
- **链接：** [arXiv:2609.34182](https://arxiv.org/abs/2609.34182)（2026-09-29）
- **技术核心：** 灵巧操作需要触觉，但机器人触觉演示几乎无法规模化——UVTA 的路线是让**人类触觉演示**来补。人机数据在**同一轮联合训练**里混合（非分阶段预训练），weighted sampler 保证两个本体采样等概率；min-max 归一化分别处理不同本体；损失函数把 9 维腕部与 22 维手部分组均衡，防止高维手部目标主导梯度；扩散策略 + 未来触觉预测头。
- **数据与效果：** 真实平台（固定基座 + 22-DoF 灵巧手 + 指尖触觉 + 腕部单目）执行滴管移液等高精度力控任务；对比 ViTacFormer、RDP（reactive diffusion）、T-Rex（tactile-reactive 基础模型）等代表性强基线。
- **为什么重要：** 多模态策略从「视觉+动作」走向「视觉+触觉+动作」的关键一步，且给出的工程配方（分组均衡损失、单轮联合训练）非常简单可抄。当视觉侧 scaling 红利被吃干抹净，触觉可能是下一个数据 moat。

### 5. CAPEX：让基础模型自己当演示者，经验自适应推理把成本砍掉 80%

- **关键词：** foundation model distillation, autonomous demonstration collection, experience-adaptive reasoning
- **链接：** [arXiv:2609.33007](https://arxiv.org/abs/2609.33007)（2026-09-26）
- **技术核心：** 人采演示数据"贵、慢、不同步"，CAPEX 换个思路：直接让通用多模态基础模型当**自主演示者**，把物理行为蒸馏进可部署 policy。关键设计是 experience-conditioning——利用前几次尝试的执行经验，自适应调整基础模型需要"观察-推理-重规划"的频率（简单段少调用，卡壳段多调用）。
- **数据与效果：** RoboCasa + 真实 Franka + 双臂 YAM-arm 平台评测：成功演示数量 **4.3×**，单条成功演示成本 **−80%**。用 CAPEX 数据训的 Diffusion Policy / ACT 逼近同量人类演示训练的策略性能；从头训且训练更久时差距基本闭合。
- **为什么重要：** 在「人类采数据」和「纯 sim 生成数据」之间开辟了第三条路：基础模型当数据工厂。和本周的 ego-data 路线互为镜像——一个榨人类视频，一个榨大模型推理能力，共同指向同一件事：**机器人学习的瓶颈正在从算法转向数据供给方式**。

---

## 👤 学者动态：Danfei Xu 追踪

本周 RL² 无全新 arXiv 论文，但有两条值得记录的动态：

- **EgoWAM 被 CoRL 2026 接收**（Baoyu Li、Xinchen Yin、Mengying Lin、Yixin Zhang、Danfei Xu）：用 World Action Model 的状态表征设计桥接人机 embodiment gap，让 policy 性能随 in-the-wild ego 数据 scale 而提升（朴素 BC 联合训练做不到的）。同获 **Meta RSIE 2026（Egocentric Intelligence 峰会）Distinguished Poster Award**。arXiv:2607.08436。
- **EgoVerse 确认 RSS 2026 接收**（4 月已报）；**EgoScale（与 NVIDIA GEAR 合作）确认 CoRL 2026**——Danfei Xu 一系在 ego-human-data 方向已呈"流水线"态势：数据集（EgoVerse）→ 迁移框架（EgoBridge/EgoMimic/EMMA）→ 规模化（EgoScale）→ 表征机制（EgoWAM）。
- 学生 Simar Kareer 受邀在 **RSS 2026 Data-Centric Robotics Workshop** 演讲（7 月），方向正是 ego 人类经验数据。

**观察：** 加上本周 λ₀ / IronMind / EgoHumanoid-V2 的集体爆发，Georgia Tech RL² 系列从"先驱"变成了"诸神之一"——这个赛道已经开始拥挤，先发优势窗口正在关闭。

---

## 💡 本周洞察

### 1. 「人类数据周」——三篇独立工作同时引爆
λ₀（Salesforce）、IronMind（工业界）、EgoHumanoid-V2（上AI Lab+Salesforce）同周出现，全部指向同一结论：**第一人称人类数据是人形机器人预训练的最优燃料**。更关键的是 IronMind 给出的 scaling law——10000 小时还没饱和。可以预期，"ego 数据军备竞赛"即将开始，数据清洗/重标注/质量加权这类"数据工程"会成为下一个热点。

### 2. Embodiment gap 的解法在分化
本周至少出现了三条技术路线：① λ₀ 的共享表征空间 + 领域接口；② IronMind 的相机空间动作表示（放弃重定向）；③ EgoHumanoid-V2 的 coarse-to-fine 对齐（更精细的重定向）。"绕开重定向" vs "做好重定向"之争会延续一段时间——短期看 IronMind 的工程收益最直接，长期看哪条路线能吃到触觉和力反馈还不明朗。

### 3. 触觉开始上餐桌
UVTA + VisTacAlign（见下）同周出现，且都指向"人类触觉演示带机器人触觉"的联合训练配方。视觉 scaling 的边际收益递减后，力/触觉是灵巧操作绕不过去的模态。

### 4. 数据供给的三种范式在成型
人类采（遥操作，正在被 CAPEX 挑战）→ 人类视频榨取（本周主流）→ 基础模型自主采（CAPEX）。三种范式的成本结构差异巨大，未来的数据管线很可能是三者混合。

---

## 📌 其他值得一看

- **VisTacAlign**（[arXiv:2609.30959](https://arxiv.org/abs/2609.30959)，2026-09-25）— 人机联合训练 3D 视觉-触觉灵巧策略：手套追踪手部重定向到 17-DoF 触觉手（一次性指尖校正）+ 人手擦除替换机器人网格重跑 stereo 基础模型 + 电容触觉手套信号空间对齐。Lego 装配/摘草莓/电钻三任务证明触觉输入与视觉对齐缺一不可。
- **Contact-Anchored Retargeting + Residual Policy**（[arXiv:2609.24093](https://arxiv.org/abs/2609.24093)，2026-09-21）— 接触锚定重定向 + 跨任务单次训练的残差 RL，核心论点：从运动学记录恢复接触不是数据增强，而是接触丰富操作学习的**前置条件**。
- **高自由度灵巧 VLA 后训练**（[arXiv:2609.19666](https://arxiv.org/abs/2609.19666)，2026-09-17）— 无际科技 + 上科大：VLA 基础模型 + 真实 RL 后训练适配五指灵巧手，5 类任务（双臂传递、手中重定向、工具使用）20 次试验 100% 成功率。
- **MIT HumanScale 预印本**（cdfg.mit.edu）— 配套证据：ego 预训练 100→5000 小时同样 log-linear，且在下游泛化上**超过同规模真实机器人预训练**。

---

## 💡 趋势一句话

本周具身智能的关键词只有一个：**人类数据**。三篇独立工作同周证明 ego 人类数据能规模化驱动人形机器人（万小时 scaling law 首次确立），迁移瓶颈从"数据量"转向"对齐质量"，触觉与"大模型当数据工厂"成为新的数据供给变量。human-data-training 不再是小众路线，而是正在成为主流范式。

📅 **下周预告：** **AI Infra**（训练框架优化、推理加速、模型服务化）

---
龙虾小队 🦞 · 本周雷达收工
