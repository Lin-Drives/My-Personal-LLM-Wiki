---
type: Research Feed
title: 最新论文动态
description: 持续展示论文雷达发现的论文与工具解读。
tags: [论文雷达]
status: draft
---

# 最新论文动态

> 自动整理的扫描结果，尚未人工核验；摘要与推荐理由为扫描工具解读。原文链接可直接查看。

按发现时间排列；论文发表与修订时间分别标注。深入解读的进度不阻塞这里更新。

<article>
<h2>Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining</h2>
<p><a href="https://arxiv.org/abs/2610.00438v1">arXiv:2610.00438v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-10-04T09:22:20.729297+08:00 · 发表：2026-09-30T17:25:16Z · 修订：2026-09-30T17:25:16Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：λ₀ (lambda_0) + HumanVerse-500：500 小时人类全身数据喂出全身人形 VLA。问题/方法/证据：提出 HumanVerse-500——500 小时第一人称人类全身操作数据集，用轻量可穿戴系统同步采集 ego 视频 + 身体运动 + 手部运动。在此之上构建 λ₀ 全身人形 VLA：三阶段训练（① 从大规模 ego 数据学交互 → ② 用 HumanVerse-500 协调身体与手部运动 → ③ 下游任务/本体适配）。三阶段共享同一表征空间完成&quot;人类经验迁移&quot;，领域专用接口处理人机状态/动作差异。原报告标注日期：2026-09-30。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：第一个系统性地把「第一人称人类全身数据」用于全身人形 loco-manipulation 的 VLA——绕开了人形遥操作&quot;贵且难规模化&quot;的死结。与 λ₀ 同一批作者的 EgoHumanoid-V2（见 #3）形成组合拳：一个做数据集+预训练，一个做迁移机制。</p>
<p>关联问题：人类视频与机器人数据需求</p>
<p>标签：embodied-intelligence、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>IronMind: Scaling Humanoid Dexterous Manipulation via Camera-Space Ego-Centric Pretraining</h2>
<p><a href="https://arxiv.org/abs/2609.39403v1">arXiv:2609.39403v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-10-04T09:22:20.729297+08:00 · 发表：2026-09-30T09:45:59Z · 修订：2026-09-30T09:45:59Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：IronMind：万小时第一人称预训练，相机空间动作表示直接拆掉 embodiment gap。问题/方法/证据：两大洞见。① **相机空间动作表示**：低成本 ego 视频没有躯干运动学，传统重argeting走不通——干脆把动作表示在相机坐标系（ego 视频的原生参考空间），人机动作维度做语义对齐，完全绕过显式身体重定向。② **数据引擎**：规则过滤 + 原子任务重标注 + 逐帧质量加权，把 10,000+ 小时 heterogeneous 数据（ego 人类视频 + 非目标本体机器人数据）清洗成可用语料。架构为双专家 MoT（VL 理解专家 + flow-matching 动作专家），训练期可挂语义/几何/视频动力学辅助监督、推理期全部拆掉。原报告标注日期：2026-09-30。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：人形灵巧操作预训练的**第一个 scaling law 实证**——数据加数量级，性能还在涨，没见顶。而且&quot;相机空间&quot;这个选择既优雅又实用：ego 视频本来就长在相机坐标系里，重argeting 本来就是多余的中间层。附赠一个反直觉发现：world-prior 辅助监督在真实机器人上反而掉点（55.0%→31.7%），辅助预测目标与接触-rich 闭环控制存在错配。</p>
<p>关联问题：人类视频与机器人数据需求、机器人实际部署约束</p>
<p>标签：embodied-intelligence、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>EgoHumanoid-V2: Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for Loco-Manipulation</h2>
<p><a href="https://arxiv.org/abs/2609.37181v1">arXiv:2609.37181v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-10-04T09:22:20.729297+08:00 · 发表：2026-09-29T10:05:10Z · 修订：2026-09-29T10:05:10Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：EgoHumanoid-V2：首个第一人称人类→人形「协调全身技能」零样本迁移。问题/方法/证据：之前的 ego 迁移工作都停留在「场景泛化」+ 解耦控制（上身操作下身走路分开管）。本文攻的是更难的问题：**协调的全身 loco-manipulation 技能直接迁移**。核心是 coarse-to-fine 动作对齐——运动学参考校正（修末端位姿精度）+ 动力学感知精修（保全身协调性）；再叠加 robot-arm rendering 与训练时图像增强，缩小视觉 embodiment gap、提升视角鲁棒性。原报告标注日期：2026-09-29。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：把&quot;人类数据 = 直接技能监督&quot;（direct skill supervision）从口号变成可复现的流程。对 human-data-training 社区的意义在于：迁移瓶颈不在数据量，而在**对齐质量**——这一篇把对齐做到了全身动力学级别。Danfei Xu 线的 EgoMimic/EgoVerse 证明了&quot;能用&quot;，EgoHumanoid-V2 证明了&quot;能用到协调全身&quot;。</p>
<p>关联问题：人类视频与机器人数据需求</p>
<p>标签：embodied-intelligence、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Unified Visual-Tactile-Action Modeling from Human Demonstrations for Dexterous Manipulation</h2>
<p><a href="https://arxiv.org/abs/2609.34182v2">arXiv:2609.34182v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-10-04T09:22:20.729297+08:00 · 发表：2026-09-28T02:59:16Z · 修订：2026-09-29T02:47:09Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：UVTA：人类演示统一视觉-触觉-动作建模，灵巧操作的触觉规模化路线。问题/方法/证据：灵巧操作需要触觉，但机器人触觉演示几乎无法规模化——UVTA 的路线是让**人类触觉演示**来补。人机数据在**同一轮联合训练**里混合（非分阶段预训练），weighted sampler 保证两个本体采样等概率；min-max 归一化分别处理不同本体；损失函数把 9 维腕部与 22 维手部分组均衡，防止高维手部目标主导梯度；扩散策略 + 未来触觉预测头。原报告标注日期：2026-09-29。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：多模态策略从「视觉+动作」走向「视觉+触觉+动作」的关键一步，且给出的工程配方（分组均衡损失、单轮联合训练）非常简单可抄。当视觉侧 scaling 红利被吃干抹净，触觉可能是下一个数据 moat。</p>
<p>关联问题：人类视频与机器人数据需求</p>
<p>标签：embodied-intelligence、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>CAPEX: Efficiently Distilling Foundation Model Behavior into Deployable Robot Policies through Experience-Adaptive Reasoning</h2>
<p><a href="https://arxiv.org/abs/2609.33007v1">arXiv:2609.33007v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-10-04T09:22:20.729297+08:00 · 发表：2026-09-26T23:05:46Z · 修订：2026-09-26T23:05:46Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：CAPEX：让基础模型自己当演示者，经验自适应推理把成本砍掉 80%。问题/方法/证据：人采演示数据&quot;贵、慢、不同步&quot;，CAPEX 换个思路：直接让通用多模态基础模型当**自主演示者**，把物理行为蒸馏进可部署 policy。关键设计是 experience-conditioning——利用前几次尝试的执行经验，自适应调整基础模型需要&quot;观察-推理-重规划&quot;的频率（简单段少调用，卡壳段多调用）。原报告标注日期：2026-09-26。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：在「人类采数据」和「纯 sim 生成数据」之间开辟了第三条路：基础模型当数据工厂。和本周的 ego-data 路线互为镜像——一个榨人类视频，一个榨大模型推理能力，共同指向同一件事：**机器人学习的瓶颈正在从算法转向数据供给方式**。</p>
<p>关联问题：世界模型与可靠规划、人类视频与机器人数据需求</p>
<p>标签：embodied-intelligence、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>VisTacAlign: Co-Training Dexterous Policies on Tactile Human and Robot Demonstrations</h2>
<p><a href="https://arxiv.org/abs/2609.30959v1">arXiv:2609.30959v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-10-04T09:22:20.729297+08:00 · 发表：2026-09-25T08:12:04Z · 修订：2026-09-25T08:12:04Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：VisTacAlign。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：人类视频与机器人数据需求</p>
<p>标签：embodied-intelligence、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Dexterous Robot Manipulation from Human Demonstrations via Contact-Anchored Retargeting and Residual Policy Learning</h2>
<p><a href="https://arxiv.org/abs/2609.24093v1">arXiv:2609.24093v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-10-04T09:22:20.729297+08:00 · 发表：2026-09-21T04:26:26Z · 修订：2026-09-21T04:26:26Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Contact Anchored Retargeting + Residual Policy。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：embodied-intelligence、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Towards High-DoF Dexterous Manipulation through VLA Post-Training</h2>
<p><a href="https://arxiv.org/abs/2609.19666v1">arXiv:2609.19666v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-10-04T09:22:20.729297+08:00 · 发表：2026-09-17T04:12:21Z · 修订：2026-09-17T04:12:21Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：高自由度灵巧 VLA 后训练。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：embodied-intelligence、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>EgoWAM: World Action Models Beyond Pixels with In-the-Wild Egocentric Human Data</h2>
<p><a href="https://arxiv.org/abs/2607.08436v1">arXiv:2607.08436v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-10-04T09:22:20.729297+08:00 · 发表：2026-07-08T16:11:37Z · 修订：2026-07-08T16:11:37Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：EgoWAM 被 CoRL 2026 接收。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：人类视频与机器人数据需求</p>
<p>标签：embodied-intelligence、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>HelloWorld: Towards Practical Applications of Generative Driving World Models</h2>
<p><a href="https://arxiv.org/abs/2609.28931v1">arXiv:2609.28931v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-27T09:21:27.190330+08:00 · 发表：2026-09-24T02:28:50Z · 修订：2026-09-24T02:28:50Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：HelloWorld: A World Model System for Data Generation and Interactive Simulation in Autonomous Driving (arXiv:2609.28931, 2026-09-24)。问题/方法/证据：关键词 : 驾驶世界模型、因果蒸馏、多相机环视、LiDAR 生成、闭环仿真 面壁智能 &amp; 清华团队提出 HelloWorld——一个面向数据生成与交互仿真的可控驾驶世界模型系统。技术核心： 1 Block causal 架构 同时生成七路环视 RGB 视频； 2 因果教师蒸馏 ——将 20 步因果教师压缩为 4 步学生模型，大幅降低推理延迟； 3 RGB 条件 LiDAR 分支 与视觉生成共享世界表征，实现跨模态一致性。该系统将 world model 从&quot;视频生成器&quot;升级为覆盖数据生成与闭环仿真的完整基础设施。 为什么重要 : 自动驾驶数据的长尾问题（corner case 稀缺、标注昂贵）是世界模型最有商业价值的落地场景之一。HelloWorld 的意义在于系统性——不是只生成好看的视频，而是打通了&quot;生成 局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：自动驾驶数据的长尾问题（corner case 稀缺、标注昂贵）是世界模型最有商业价值的落地场景之一。HelloWorld 的意义在于系统性——不是只生成好看的视频，而是打通了&quot;生成 → 仿真 → 数据&quot;的闭环。因果蒸馏（20步→4步）代表了世界模型工程化的关键方向：再强的模型如果跑不出实时，就无法用于闭环策略评估。这与 GAIA 系列形成正面竞争。</p>
<p>关联问题：世界模型与可靠规划</p>
<p>标签：world-models、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>RoboTwin-Phys: Do WAMs and VLAs Understand the Physical World?</h2>
<p><a href="https://arxiv.org/abs/2609.26292v1">arXiv:2609.26292v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-27T09:21:27.190330+08:00 · 发表：2026-09-22T12:04:52Z · 修订：2026-09-22T12:04:52Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：RoboTwin-Phys: Do WAMs and VLAs Understand the Physical World? (arXiv:2609.26292, 2026-09-22)。问题/方法/证据：关键词 : 物理多样性基准、机器人操作、WAM/VLA 评测、sim to real gap 北大团队推出 RoboTwin Phys，一个将 物理条件多样性 作为显式评测维度的机器人操作基准。现有大规模仿真基准主要变化外观、场景布局和视觉观测，但底层物理参数（质量、摩擦、关节动力学）通常固定。RoboTwin Phys 覆盖 13 个物理属性、5000+ 专家演示，系统评测当前代表性的 World Action Models WAMs 和 Vision Language Action models VLAs 在物理条件变化下的鲁棒性。实验揭示了一致的鲁棒性缺口——模型在标准条件下表现优异，但物理参数偏移时性能显著退化。 为什么重要 : 这击中了当前 world model 评测的盲区——&quot;视觉逼真 ≠ 物理正局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：这击中了当前 world model 评测的盲区——&quot;视觉逼真 ≠ 物理正确&quot;。当 SOTA 模型在 Clean 设定下刷到 84% 成功率但 Random 物理条件下骤降到 55.7%，说明世界模型对物理规律的理解仍然表面化。这个基准迫使领域直面一个问题：你的模型是真的理解了物理世界，还是只是在背视觉模式？对 sim-to-real 部署有直接指导意义。</p>
<p>关联问题：世界模型与可靠规划</p>
<p>标签：world-models、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Can 4D Foundation Models Remember?</h2>
<p><a href="https://arxiv.org/abs/2609.20819v2">arXiv:2609.20819v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-27T09:21:27.190330+08:00 · 发表：2026-09-17T17:59:50Z · 修订：2026-09-21T04:15:03Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Can 4D Foundation Models Remember? (PersistBench) (arXiv:2609.20819, 2026-09-17)。问题/方法/证据：关键词 : 4D 基础模型、视觉记忆基准、持续学习、benchmark 康奈尔大学（Hadar Averbuch Elor &amp; Wei Chiu Ma 组）提出 PersistBench——第一个系统评测 4D 基础模型 视觉记忆 能力的基准。当前 4D 基础模型（相机可控视频模型、4D 重建模型）能感知和重建动态环境，但它们记住了多少？当 agent 在环境中移动、离开某个区域后再返回，模型还能保持一致的场景状态吗？PersistBench 通过一系列精心设计的探针任务量化这一能力。 为什么重要 : 持久记忆是 world model 从&quot;短视频预测器&quot;进化为&quot;可交互世界模拟器&quot;的必经之路。如果模型在 agent 转身之后就&quot;忘记&quot;了桌子上有几个物体，它就无法支撑任何需要空间推理的下游任务。这个基准与 Rob局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：持久记忆是 world model 从&quot;短视频预测器&quot;进化为&quot;可交互世界模拟器&quot;的必经之路。如果模型在 agent 转身之后就&quot;忘记&quot;了桌子上有几个物体，它就无法支撑任何需要空间推理的下游任务。这个基准与 RoboTwin-Phys 形成互补——一个测物理理解，一个测空间记忆——共同构成了 world model 评测的新维度。</p>
<p>关联问题：世界模型与可靠规划</p>
<p>标签：world-models、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Astronex-World 1.0: Real-Time Interactive World Model Foundation</h2>
<p><a href="https://arxiv.org/abs/2609.20034v1">arXiv:2609.20034v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-27T09:21:27.190330+08:00 · 发表：2026-09-17T10:38:22Z · 修订：2026-09-17T10:38:22Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Astronex-World 1.0: Real-Time Interactive World Model Foundation (arXiv:2609.20034, 2026-09-17)。问题/方法/证据：关键词 : 实时交互、视频世界模型、多条件控制（相机轨迹 + 连续动作 + 事件）、开放底座 南京信息工程大学推出 Astronex World 1.0——一个开放可控的实时交互式视频世界模型基础。模型以 Wan2.2 视频 VAE 为底层，给定文本提示（T2V）或初始观测（I2V），可预测未来视觉状态，支持三类控制信号的帧级对齐注入： 相机轨迹 、 连续动作 （键盘/手柄输入）、以及可在任意帧位置插入的 文本事件 ；同时通过 embodiment identifier 区分不同具身视角。模型做到了真正的实时交互推理。 为什么重要 : 交互式世界模型的&quot;实时&quot;门槛一直是最难啃的骨头。Astronex World 的贡献在于将多种控制信号（相机 + 动作 + 事件）统一在一个可实时运行的框架中，并且是 开放权重 局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：交互式世界模型的&quot;实时&quot;门槛一直是最难啃的骨头。Astronex-World 的贡献在于将多种控制信号（相机 + 动作 + 事件）统一在一个可实时运行的框架中，并且是**开放权重**的。多条件注入意味着它可以作为下游策略训练的可交互环境——不再只是单向的视频预测器，而是可被 agent 操作的世界模拟器。</p>
<p>关联问题：世界模型与可靠规划</p>
<p>标签：world-models、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Recency Forcing: Bridging the Long-Horizon Gap in Autoregressive Video Generation</h2>
<p><a href="https://arxiv.org/abs/2609.19729v1">arXiv:2609.19729v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-27T09:21:27.190330+08:00 · 发表：2026-09-17T05:40:53Z · 修订：2026-09-17T05:40:53Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Recency Forcing: Bridging the Long-Horizon Gap in Autoregressive Video Generation (arXiv:2609.19729, 2026-09-19)。问题/方法/证据：关键词 : KV eviction mismatch、长时程 AR 视频生成、Temporal Response Bias、零开销长视频 VinAI Research 团队诊断出 AR 视频生成长时程退化的一个被忽视的根本原因—— KV eviction mismatch ：模型训练时所有上下文帧都在 KV cache 中，但推理时内存限制迫使远端帧被驱逐，导致模型在&quot;没见过的条件下&quot;工作。他们提出 Recency Forcing：不截断上下文（保留时序信息），而是逐步降低远端帧的影响，使其最终 eviction 变得可忽略。具体通过 Temporal Response Bias TRB 施加在 pre softmax attention logits 上，并设计了 Biased Attention Repar局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：这是今年 AR 视频 world model 领域最优雅的分析之一。它没有发明新的架构，而是找到了训练-推理不一致这个&quot;隐形 bug&quot;并用一个数学上精确的 reparameterization 修复。零开销 + training-free 模式可用，意味着几乎所有现有 AR 视频模型都能直接受益。长时程一致性是 world model 实用性的核心瓶颈——如果模型只能稳定预测 2 秒，它就不是一个 world model。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>World Models for Embodied Intelligence: From Plausible to Controllable to Actionable</h2>
<p><a href="https://arxiv.org/abs/2609.16697v1">arXiv:2609.16697v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-27T09:21:27.190330+08:00 · 发表：2026-09-15T06:22:42Z · 修订：2026-09-15T06:22:42Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：World Models for Embodied Intelligence: From Plausible to Controllable to Actionable。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>RECAP-Forcing: Retaining Content Appearances for Long Video Generation</h2>
<p><a href="https://arxiv.org/abs/2608.26671v1">arXiv:2608.26671v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-27T09:21:27.190330+08:00 · 发表：2026-08-27T06:24:59Z · 修订：2026-08-27T06:24:59Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：RECAP Forcing: Retaining Content Appearances for Long Horizon Video Generation。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>PosteriorBench: From Point Estimates to Posterior Matching in Evaluating Generative Inverse Solvers</h2>
<p><a href="https://arxiv.org/abs/2609.20794v1">arXiv:2609.20794v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-20T09:21:15.725061+08:00 · 发表：2026-09-17T17:54:12Z · 修订：2026-09-17T17:54:12Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：PosteriorBench: 生成式反问题求解器的后验匹配基准。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Beyond PINNs: A Unified Gauss--Newton and Petrov--Galerkin Framework for Neural and Hybrid PDE Solvers</h2>
<p><a href="https://arxiv.org/abs/2609.20641v1">arXiv:2609.20641v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-20T09:21:15.725061+08:00 · 发表：2026-09-17T16:23:56Z · 修订：2026-09-17T16:23:56Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Beyond PINNs: Gauss–Newton + Petrov–Galerkin 统一框架 (arXiv:2609.20641)。问题/方法/证据：提出一个统一数学框架，将 PINN 的强式残差训练与有限元法的弱式变分离散纳入同一个 Gauss–Newton / Petrov–Galerkin 体系，使&quot;测试函数的选择&quot;成为显式的算法设计自由度。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：PINN 与 FEM 长期是两条平行线：一个基于强式残差+自动微分，一个基于弱式变分+离散化。这篇工作证明两者本质上是同一枚硬币的两面，为&quot;什么时候用弱式、什么时候混合经典求解器&quot;提供了理论决策依据——混合方法的春天可能来了。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Amortizing Physics-Informed Neural Solvers via Graph Hypernetworks</h2>
<p><a href="https://arxiv.org/abs/2609.19915v1">arXiv:2609.19915v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-20T09:21:15.725061+08:00 · 发表：2026-09-17T08:58:01Z · 修订：2026-09-17T08:58:01Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：图超网络摊销物理信息求解器：一个网络吃一族 PDE (arXiv:2609.19915)。问题/方法/证据：提出用**算子图**（operator graph）显式描述 PDE 中方程、场、导数、项、残差之间的关系，配合图超网络为每个目标方程生成对角码，初始化 meta 训练过的分解式 PINN，实现跨方程的求解器摊销。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：PINN 最大的实用痛点是每个 PDE 都要从头训练。摊销化（amortization）是 SciML 的圣杯之一。这篇工作给出的答案很诚实：显式方程关系在复杂耦合系统上价值巨大，但简单固定结构问题上老办法够用——这种&quot;知道边界在哪&quot;的结论比单点 SOTA 更有价值。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Physical knowledge on historical data matters more than enforcing physical constraints on the forecast</h2>
<p><a href="https://arxiv.org/abs/2609.19871v1">arXiv:2609.19871v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-20T09:21:15.725061+08:00 · 发表：2026-09-17T08:23:08Z · 修订：2026-09-17T08:23:08Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：历史数据上的物理知识比预测上的物理约束更重要。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Rapidity-Coupled Spin Dynamics in Pulsed Laser Fields from Physics-Informed Neural Networks</h2>
<p><a href="https://arxiv.org/abs/2609.19756v1">arXiv:2609.19756v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-20T09:21:15.725061+08:00 · 发表：2026-09-17T06:26:54Z · 修订：2026-09-17T06:26:54Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：PINN 学习脉冲激光场中的自旋动力学。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Physics-Informed Hemodynamic Modeling for Data-Free Prediction and Sparse-Data Assimilation</h2>
<p><a href="https://arxiv.org/abs/2609.19290v1">arXiv:2609.19290v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-20T09:21:15.725061+08:00 · 发表：2026-09-16T18:02:24Z · 修订：2026-09-16T18:02:24Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：PINN 学习脉冲激光场中的自旋动力学。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Fast Learning Rates for Physics-Informed Kernel Methods</h2>
<p><a href="https://arxiv.org/abs/2609.18901v1">arXiv:2609.18901v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-20T09:21:15.725061+08:00 · 发表：2026-09-16T16:39:32Z · 修订：2026-09-16T16:39:32Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：物理信息核方法的快速学习率：从理论到 n^-1/2 (arXiv:2609.18901)。问题/方法/证据：对物理信息核估计器（physics-informed kernel estimator）证明有限样本界，定量刻画微分信息能把预测误差改善多少、以及如何依赖 n（值观测数）、m（微分观测数）和算子 D。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：PINN/物理信息方法的&quot;为什么有效&quot;长期缺严格的统计理论。Rosasco 组这篇把&quot;微分信息值多少数据&quot;这个直觉问题变成了可计算的定量答案——m 存在阈值且饱和这一发现，直接指导实验设计：微分观测采到一定量就够了。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>HiLNO: A Hierarchical Latent Neural Operator with Multi-Scale Supervision for PDEs on General Geometries</h2>
<p><a href="https://arxiv.org/abs/2609.18419v1">arXiv:2609.18419v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-20T09:21:15.725061+08:00 · 发表：2026-09-16T10:12:44Z · 修订：2026-09-16T10:12:44Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：HiLNO: 层次化隐空间神经算子，参数砍 84% (arXiv:2609.18419)。问题/方法/证据：提出层次化隐空间神经算子 HiLNO，通过&quot;细→粗→细&quot;的隐空间构造 + 多尺度监督 + 各向异性高斯注意力，解决隐空间算子压缩时丢失多尺度解结构信息的问题。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：神经算子的落地瓶颈一直是算力成本。HiLNO 用层次化隐空间把&quot;压缩损失&quot;变成&quot;可监督的层次学习&quot;，在不掉精度的前提下把成本压到原来的 1/6~1/3，且直接打到了工业级（汽车气动）场景——这是算子学习从论文走向工程的重要一步。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Hybrid coupling with numerics-informed neural networks and the overlapping Schwarz alternating method</h2>
<p><a href="https://arxiv.org/abs/2609.17841v2">arXiv:2609.17841v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-20T09:21:15.725061+08:00 · 发表：2026-09-15T21:01:30Z · 修订：2026-10-05T17:50:59Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：NINN + 重叠 Schwarz 交替法耦合。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Development of a Physics-Informed Neural Framework, MEOWN, for Rapid Prediction of Muon Stopping Sites in Crystalline Materials, for understanding Quantum Magnet employing Muon Spectroscopy</h2>
<p><a href="https://arxiv.org/abs/2609.17063v1">arXiv:2609.17063v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-20T09:21:15.725061+08:00 · 发表：2026-09-15T12:08:11Z · 修订：2026-09-15T12:08:11Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：PINN 学习脉冲激光场中的自旋动力学。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Can Deep Learning Achieve Cross-Physics Mapping?</h2>
<p><a href="https://arxiv.org/abs/2609.16853v1">arXiv:2609.16853v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-20T09:21:15.725061+08:00 · 发表：2026-09-15T08:45:23Z · 修订：2026-09-15T08:45:23Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：跨物理场映射：深度学习能翻译不同方程的场吗？。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Physics Informed Random Feature Neural Networks for Solving PDEs</h2>
<p><a href="https://arxiv.org/abs/2609.16406v1">arXiv:2609.16406v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-20T09:21:15.725061+08:00 · 发表：2026-09-14T22:22:20Z · 修订：2026-09-14T22:22:20Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：物理信息随机特征网络。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Physics-Guided Conditional Flow Matching with Energy Regularization for Robust PDE Inverse Problems</h2>
<p><a href="https://arxiv.org/abs/2609.15536v1">arXiv:2609.15536v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-20T09:21:15.725061+08:00 · 发表：2026-09-14T13:22:16Z · 修订：2026-09-14T13:22:16Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：物理引导流匹配 + 能量正则化：对抗污染的 PDE 反问题 (arXiv:2609.15536)。问题/方法/证据：针对稀疏、含噪、甚至被污染的观测下的 PDE 反问题，提出两阶段流匹配框架：物理引导条件流匹配（PG-CFM）+ 能量正则化流匹配（ERFM）。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：反问题的观测数据从来都不是干净的——野外传感器漂移、实验记录错误是常态。现有方法对所有样本一视同仁，这篇工作给出了一个有理论解释的&quot;样本级&quot;抗污染机制，而且用的是当下最火的流匹配生成模型范式。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Single-condition neural solvers encode transferable response spaces for parametric differential equations</h2>
<p><a href="https://arxiv.org/abs/2609.15432v1">arXiv:2609.15432v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-20T09:21:15.725061+08:00 · 发表：2026-09-14T11:56:37Z · 修订：2026-09-14T11:56:37Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：单条件神经求解器的响应空间迁移。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>General Quantification of Covariate and Concept Shifts</h2>
<p><a href="https://arxiv.org/abs/2609.11918v1">arXiv:2609.11918v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-13T09:20:26.004892+08:00 · 发表：2026-09-10T17:57:52Z · 修订：2026-09-10T17:57:52Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：DataShifts — 可估计的分布偏移量化工具 (arXiv:2609.11918)。问题/方法/证据：基于熵最优传输（Entropic Optimal Transport），统一了协变量偏移和概念偏移的误差界，并提供了可从样本估计的实用工具。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：分布偏移是深度学习从实验室走向真实世界的最大障碍之一。理论界的泛化界往往不可估计，这篇工作试图在理论和实践之间架起桥梁。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Data Scarcity and Model Sparsity: Mixtures-of-Experts Overfit More to Repeated Data</h2>
<p><a href="https://arxiv.org/abs/2609.11917v1">arXiv:2609.11917v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-13T09:20:26.004892+08:00 · 发表：2026-09-10T17:57:33Z · 修订：2026-09-10T17:57:33Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：MoE 在数据重复场景下的脆弱性 (arXiv:2609.11917)。问题/方法/证据：系统研究了 Mixture-of-Experts（MoE）在训练数据重复时的退化行为，发现 MoE 比 dense 模型对数据重复更敏感。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：人类书写文本数据正在耗尽，数据重复已成为 LLM 训练的默认现实。MoE 架构是 2025-2026 年大模型效率化的主流选择，这篇工作揭示了其隐藏的脆弱性。</p>
<p>关联问题：人类视频与机器人数据需求</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>TART: A Modular Tool for Technique-Aware Audio-to-Tablature Guitar Transcription</h2>
<p><a href="https://arxiv.org/abs/2609.11904v1">arXiv:2609.11904v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-13T09:20:26.004892+08:00 · 发表：2026-09-10T17:55:12Z · 修订：2026-09-10T17:55:12Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：TART: 吉他自动转录系统。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>CoRA-NAS: Coarse Ranking and Anchor-Residual Refinement for Neural Architecture Search</h2>
<p><a href="https://arxiv.org/abs/2609.11884v1">arXiv:2609.11884v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-13T09:20:26.004892+08:00 · 发表：2026-09-10T17:49:19Z · 修订：2026-09-10T17:49:19Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：CoRA NAS: 低成本神经架构搜索。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement</h2>
<p><a href="https://arxiv.org/abs/2609.11873v3">arXiv:2609.11873v3 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-13T09:20:26.004892+08:00 · 发表：2026-09-10T17:44:23Z · 修订：2026-09-22T12:08:36Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Recursive Self-Improvement (RSI) 系统综述 (arXiv:2609.11873)。问题/方法/证据：首次系统梳理递归自改进（RSI）AI 的概念、路线图和应用场景，由国内大团队（约30位作者）联合撰写。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：RSI 是通往 AGI 讨论中的核心概念之一，但此前缺乏系统性综述。这篇 31MB 的巨篇为理解 RSI 提供了统一框架。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Model-Aware Schedules Improve Generation via Fiberwise Optimal Transport</h2>
<p><a href="https://arxiv.org/abs/2609.11842v1">arXiv:2609.11842v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-13T09:20:26.004892+08:00 · 发表：2026-09-10T17:30:44Z · 修订：2026-09-10T17:30:44Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Model-Aware Schedules via Fiberwise Optimal Transport (arXiv:2609.11842)。问题/方法/证据：提出基于 fiberwise 最优传输的 model-aware 采样调度方法，为扩散模型和流匹配模型构建与模型预测误差耦合的时间分配策略。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：扩散/流匹配领域的采样调度长期停留在 model-agnostic 的启发式设计。这篇工作首次将模型自身的预测误差结构纳入调度优化，并发现跨模型的普适规律，可能重塑高效采样的研究范式。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Thinking with Looped Flows</h2>
<p><a href="https://arxiv.org/abs/2609.11801v1">arXiv:2609.11801v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-13T09:20:26.004892+08:00 · 发表：2026-09-10T16:52:54Z · 修订：2026-09-10T16:52:54Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Looped Flows — 循环推理模型的新训练范式 (arXiv:2609.11801)。问题/方法/证据：用局部去噪目标训练循环推理模型，解决传统循环模型&quot;梯度只能回传一两步&quot;的核心瓶颈。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：ARC-AGI 是衡量抽象推理能力的硬基准。循环模型（test-time compute scaling 的一种形式）是 2026 年最活跃的方向之一，这篇工作解决了训练循环模型的根本难题。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Dynamic language model representations for multi-objective reaction optimisation</h2>
<p><a href="https://arxiv.org/abs/2609.11790v1">arXiv:2609.11790v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-13T09:20:26.004892+08:00 · 发表：2026-09-10T16:43:08Z · 修订：2026-09-10T16:43:08Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：文本驱动的化学反应优化。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Predicting Privacy Leakage from Weight Spectral Density</h2>
<p><a href="https://arxiv.org/abs/2609.11780v1">arXiv:2609.11780v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-13T09:20:26.004892+08:00 · 发表：2026-09-10T16:34:25Z · 修订：2026-09-10T16:34:25Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：谱分析用于隐私审计。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Learnware and AI Model Management System</h2>
<p><a href="https://arxiv.org/abs/2609.11656v1">arXiv:2609.11656v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-13T09:20:26.004892+08:00 · 发表：2026-09-10T15:01:27Z · 修订：2026-09-10T15:01:27Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Learnware Dock System。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>A Dataset and Model for Imputing Water Surface Elevation on a Large and Extremely Sparse Spatiotemporal Graph</h2>
<p><a href="https://arxiv.org/abs/2609.11580v2">arXiv:2609.11580v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-13T09:20:26.004892+08:00 · 发表：2026-09-10T14:12:02Z · 修订：2026-09-12T13:10:51Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：AmazonSWE: 大规模河流水位时空图补全。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Particle GFlowNets: Rethinking Generative Marginalization Models</h2>
<p><a href="https://arxiv.org/abs/2609.11538v1">arXiv:2609.11538v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-13T09:20:26.004892+08:00 · 发表：2026-09-10T13:37:28Z · 修订：2026-09-10T13:37:28Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Particle GFlowNets。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Generalized Score Matching for Parameter Estimation on Convex Domains</h2>
<p><a href="https://arxiv.org/abs/2609.11521v1">arXiv:2609.11521v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-13T09:20:26.004892+08:00 · 发表：2026-09-10T13:23:41Z · 修订：2026-09-10T13:23:41Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：广义 Score Matching。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>MUtE: A Dual Framework for Concept Erasure and Counterfactual Interventions</h2>
<p><a href="https://arxiv.org/abs/2609.11253v1">arXiv:2609.11253v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-13T09:20:26.004892+08:00 · 发表：2026-09-10T08:47:11Z · 修订：2026-09-10T08:47:11Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：概念擦除的最优边界。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>DistMoE: Private-data Rehearsal-free Routing in Mixture-of-Experts for Distributed Instruction Tuning</h2>
<p><a href="https://arxiv.org/abs/2608.09907v1">arXiv:2608.09907v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-06T09:35:46.598810+08:00 · 发表：2026-08-10T17:52:14Z · 修订：2026-08-10T17:52:14Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：DistMoE — 无需集中数据的分布式 MoE 隐私训练 (arXiv:2608.09907, 8月10日, Meta)。问题/方法/证据：一句话 : 多个数据孤岛各自训练专家，一个分布式路由器把它们动态组合——数据不出域，性能不打折。 痛点 : MoE 训练通常需要所有数据集中在单一集群，跨组织/跨合规域的联合训练几乎不可能 解法 : DistMoE 让每个参与方独立训练 域专属专家 ，中央只维护一个轻量级的 分布式路由器 （distributed router）；推理时路由器根据输入动态组合各方专家，训练时通过知识蒸馏对齐路由决策，无需原始数据交换 效果 : 在跨 5 个医疗数据集的 MoE 上，DistMoE 达到集中式训练 96.2% 的性能，数据零共享 意义 : 为医疗、金融等敏感数据场景的 MoE 落地提供了合规路径，也可能改变未来大模型联盟的训练格局局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：为医疗、金融等敏感数据场景的 MoE 落地提供了合规路径，也可能改变未来大模型联盟的训练格局</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching</h2>
<p><a href="https://arxiv.org/abs/2608.08097v1">arXiv:2608.08097v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-06T09:35:46.598810+08:00 · 发表：2026-08-08T12:27:03Z · 修订：2026-08-08T12:27:03Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：OasisKV — 用 Lookahead Sparse Prefetching 突破 HBM 天花板 (arXiv:2608.08097, 8月8日)。问题/方法/证据：一句话 : 把 decode 阶段的 KV cache 扩展到 HBM 之外，通过稀疏预取实现&quot;看起来像在 HBM 里&quot;的访问体验。 痛点 : 长上下文 + 多轮对话场景下，decode KV cache 容量需求远超 HBM 容量（TB 级），现有 offloading 方案 latency 抖动剧烈 解法 : OasisKV 提出 lookahead sparse prefetching ：利用注意力稀疏性，提前从远端内存（DRAM/SSD）预取下一批 token 所需的 KV 子集；同时用 per head 的稀疏度感知调度，只加载真正会被 attention 命中的 KV block 效果 : 在 128K 上下文、Llama 3 70B 上，decode throughput 相比 vLLM 的 bl局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：首次证明 decode KV cache 可以&quot;virtually unlimited&quot;地扩展到 HBM 外而不牺牲 latency SLO，为多轮 agentic 推理打开容量上限</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>HiSparse: Scaling Sparse-Attention Decoding with Hierarchical KV Cache Management</h2>
<p><a href="https://arxiv.org/abs/2608.07009v1">arXiv:2608.07009v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-06T09:35:46.598810+08:00 · 发表：2026-08-07T09:22:17Z · 修订：2026-08-07T09:22:17Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：HiSparse — 分层 KV Cache 管理实现稀疏注意力解码无限扩展 (arXiv:2608.07009, 8月7日)。问题/方法/证据：一句话 : 把 KV cache 分成&quot;热 温 冷&quot;三层，稀疏注意力只在需要时唤醒冷数据。 痛点 : 现有稀疏注意力（H2O、SnapKV 等）在 decode 阶段仍需维护完整的 KV cache，长序列下 HBM 依旧爆炸 解法 : HiSparse 引入 Hierarchical KV Cache —— 按 attention score 分布将 KV 分为三层：Hot（常驻 HBM）、Warm（压缩后 DRAM）、Cold（量化后 SSD/远端）；配合 Sparse Decode Kernel ，只在注意力计算时按需从下层加载 效果 : 在 1M token 上下文上，KV cache 内存占用降低 87% ，decode 速度比 dense baseline 快 1.8× 意义 : 让&quot;无限长上下文 局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：让&quot;无限长上下文 decode&quot;从论文概念变成工程可行方案，直接利好长文档 agent 和多轮记忆系统</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>AcceptMoE: Commitment-Weighted Self-Sizing Verifier Expert Sets for Efficient MoE Speculative Decoding</h2>
<p><a href="https://arxiv.org/abs/2608.02989v1">arXiv:2608.02989v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-06T09:35:46.598810+08:00 · 发表：2026-08-04T01:01:12Z · 修订：2026-08-04T01:01:12Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：AcceptMoE — MoE 投机解码的自适应验证 (arXiv:2608.02989, 8月4日, 清华)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>An Internet for the KV Cache: Rethinking Classical Infrastructure Boundaries in the LLM Inference Age</h2>
<p><a href="https://arxiv.org/abs/2608.01526v1">arXiv:2608.01526v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-06T09:35:46.598810+08:00 · 发表：2026-08-02T22:31:22Z · 修订：2026-08-02T22:31:22Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：An Internet for the KV Cache&quot; — 重新思考 LLM 推理时代的基础设施边界 (arXiv:2608.01526, 8月)。问题/方法/证据：一句话 : KV cache 不该是推理框架的私有数据结构，而应该是像 HTTP 请求一样可被全网路由和缓存的&quot;一等公民&quot;。 核心论点 : 当前 KV cache 被锁在单个推理实例内部，导致多轮对话、多模型协作、跨地域部署时大量重复计算；作者主张建立 KV cache 的通用寻址和传输协议 架构 : 提出类似 CDN 的 KV Cache Network —— 全局唯一 token sequence ID → 分布式 KV store → 标准序列化格式（兼容多种推理框架）→ 基于语义相似度的去重和复用 场景 : 多轮对话跨模型切换时直接复用 KV；A/B 测试不同模型时共享公共前缀 KV；跨数据中心推理时预热 KV 意义 : 这是从&quot;单机优化&quot;到&quot;网络级优化&quot;的范式跃迁，如果实现将根本性改变 LLM 推理的局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：这是从&quot;单机优化&quot;到&quot;网络级优化&quot;的范式跃迁，如果实现将根本性改变 LLM 推理的成本结构</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>A CXL Memory Rack for Multi-Turn LLM Serving</h2>
<p><a href="https://arxiv.org/abs/2607.18141v3">arXiv:2607.18141v3 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-06T09:35:46.598810+08:00 · 发表：2026-07-20T16:35:47Z · 修订：2026-08-05T22:55:21Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：CXL KV Cache Framework — 多轮对话的混合内存 KV 管理 (arXiv:2607.18141)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Moebius: Serving Mixture-of-Expert Models with Seamless Runtime Parallelism Switch</h2>
<p><a href="https://arxiv.org/abs/2606.26607v1">arXiv:2606.26607v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-06T09:35:46.598810+08:00 · 发表：2026-06-25T05:10:20Z · 修订：2026-06-25T05:10:20Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Moebius — MoE 运行时并行度在线切换 (arXiv:2606.26607, 更新版)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Blink: CPU-Free LLM Inference by Delegating the Serving Stack to GPU and SmartNIC</h2>
<p><a href="https://arxiv.org/abs/2604.07609v1">arXiv:2604.07609v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-09-06T09:35:46.598810+08:00 · 发表：2026-04-08T21:27:47Z · 修订：2026-04-08T21:27:47Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Blink — CPU-Free LLM 推理，把服务栈完全下沉到 GPU + SmartNIC (arXiv:2604.07609, 更新版)。问题/方法/证据：一句话 : 取消 CPU 这个&quot;中间商&quot;，让 GPU 直接收请求、做推理、发响应。 痛点 : 传统 LLM serving 中 CPU 负责 HTTP 解析、请求调度、tokenization、后处理，在高并发下成为瓶颈；CPU GPU 数据传输 overhead 吃掉 15 30% 的端到端 latency 解法 : Blink 将 整个服务栈 （HTTP/2、gRPC、tokenization、调度逻辑）offload 到 GPU kernel 和 SmartNIC/DPU 上运行；GPU 直接通过网络 RDMA 接收原始请求 bytes，在 kernel 内部完成全部 pipeline 效果 : 在 70B 模型、batch=32 场景下，端到端 latency 降低 22% ，throughput 提升局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：证明了 CPU-free serving 在 LLM 场景的可行性，对云厂商的推理实例设计有直接影响（可以减少甚至取消 CPU 配置）</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>SAGE: SLO-Aware Adaptive Retrieval for Production RAG Systems</h2>
<p><a href="https://arxiv.org/abs/2608.08237v1">arXiv:2608.08237v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-30T09:22:00.677779+08:00 · 发表：2026-08-08T17:05:36Z · 修订：2026-08-08T17:05:36Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：TrAct (arXiv:2608.08237, 8月25日) — 用「视觉轨迹」桥接控制和预测。问题/方法/证据：关键词 : 视觉轨迹 · 中间表征 · VLA增强 · 闭环控制 TrAct提出用 视觉轨迹（visual tracks） 作为控制和视觉预测之间的中间接口。传统VLA直接从像素输出动作，容易受到视觉干扰；TrAct先提取场景中的视觉轨迹（特征点在时间上的运动路径），再基于轨迹做控制和未来帧预测。 效果 : LIBERO INTEGRAL长程操作任务上显著提升 真实Franka机器人验证 视觉轨迹作为中间表征，天然支持 闭环重规划 为什么重要 : VLA的一个核心痛点是「开环执行」——一旦开始执行就难以根据视觉反馈调整。TrAct用视觉轨迹作为可解释的 intermediate representation，让控制策略具备了闭环修正能力。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：VLA的一个核心痛点是「开环执行」——一旦开始执行就难以根据视觉反馈调整。TrAct用视觉轨迹作为可解释的 intermediate representation，让控制策略具备了闭环修正能力。</p>
<p>关联问题：世界模型与可靠规划、机器人实际部署约束</p>
<p>标签：embodied-intelligence、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>From Annual Throughput to Vessel Schedules: A Stochastic Generator for Transshipment Hub Simulation</h2>
<p><a href="https://arxiv.org/abs/2608.07889v1">arXiv:2608.07889v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-30T09:22:00.677779+08:00 · 发表：2026-08-08T03:36:22Z · 修订：2026-08-08T03:36:22Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：HBVLA (arXiv:2608.07889, 8月20日) — VLA的「1-bit瘦身」方案。问题/方法/证据：关键词 : 1 bit量化 · 后训练 · 边缘部署 · 资源受限机器人 HBVLA（Highly Binarized VLA）提出了 1 bit后训练量化 方案，让大型VLA模型能在资源受限的机器人平台上实时运行。不需要从头训练，直接在预训练VLA上施加1 bit权重量化，配合专门的校准策略保持性能。 为什么重要 : 当前VLA模型越来越大（π0、GR00T N1等），边缘部署成为瓶颈。HBVLA证明即使是极端的1 bit压缩，通过精心设计的后训练校准，仍能在操作任务上保持可用性能。这对消费级机器人产品的落地意义重大。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：当前VLA模型越来越大（π0、GR00T N1等），边缘部署成为瓶颈。HBVLA证明即使是极端的1-bit压缩，通过精心设计的后训练校准，仍能在操作任务上保持可用性能。这对消费级机器人产品的落地意义重大。</p>
<p>关联问题：其他关注方向</p>
<p>标签：embodied-intelligence、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>LUCID: Latent-Skill Unified Control via Imagined Dynamics for Long-Horizon Humanoid Loco-Manipulation</h2>
<p><a href="https://arxiv.org/abs/2608.07746v1">arXiv:2608.07746v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-30T09:22:00.677779+08:00 · 发表：2026-08-07T20:26:34Z · 修订：2026-08-07T20:26:34Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：REFINE DP。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：embodied-intelligence、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Detection and Ranging of Transient Extrinsic Contacts Based on 6D Dynamic Tactile Sensing</h2>
<p><a href="https://arxiv.org/abs/2608.07075v1">arXiv:2608.07075v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-30T09:22:00.677779+08:00 · 发表：2026-08-07T10:27:37Z · 修订：2026-08-07T10:27:37Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Detection and Ranging of Transient Extrinsic Contacts。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：embodied-intelligence、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>AutoIntervene: Calibrated Intervention for Action-Chunking Imitation Learning Policies</h2>
<p><a href="https://arxiv.org/abs/2608.07065v1">arXiv:2608.07065v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-30T09:22:00.677779+08:00 · 发表：2026-08-07T10:14:29Z · 修订：2026-08-07T10:14:29Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：AutoIntervene (arXiv:2608.07065, 8月17日) — Action Chunk策略的「智能接管」。问题/方法/证据：关键词 : 人机协作 · Action Chunking · DAgger · 双向接管 悉尼大学PAIR Lab和范德堡大学的工作。Action chunking策略（如ACT、Diffusion Policy）在执行一个动作块时通常无法被安全中断。AutoIntervene提供了 在线、双向、分位数校准 的人机控制权切换： Phase local切入 ：在动作块执行中随时接管 Global交回 ：操作员完成干预后自动把控制权交还给策略 干预片段自动变成下一轮监督数据 效果 : 9项真机双臂任务，R2平均成功率80%，操作员干预时间低于完全人工接管和追加全演示。 为什么重要 : 这是机器人部署中「人在回路」（human in the loop）的关键技术。Action chunking虽然提升了流畅性，但牺牲局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：这是机器人部署中「人在回路」（human-in-the-loop）的关键技术。Action-chunking虽然提升了流畅性，但牺牲了可干预性。AutoIntervene在两者间找到了平衡。</p>
<p>关联问题：其他关注方向</p>
<p>标签：embodied-intelligence、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>$ω$-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation</h2>
<p><a href="https://arxiv.org/abs/2608.06375v2">arXiv:2608.06375v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-30T09:22:00.677779+08:00 · 发表：2026-08-06T17:59:31Z · 修订：2026-08-09T10:34:38Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：ω-0 (arXiv:2608.06375, 8月) — 人形机器人终于能「边走路边干活」了。问题/方法/证据：不重建未来视频，而是学习**紧凑的未来观测embedding**作为轻量世界模型信号局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：这是人形机器人从「能走」和「能抓」进化到「边走路边抓」的关键一步。之前的策略大多是分阶段（先走→停→操作→再走），ω-0证明了端到端并发控制的可行性。</p>
<p>关联问题：世界模型与可靠规划、人类视频与机器人数据需求</p>
<p>标签：embodied-intelligence、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Wan-Animate-2: Pushing the Application Boundaries of Character Animation</h2>
<p><a href="https://arxiv.org/abs/2608.06009v2">arXiv:2608.06009v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-30T09:22:00.677779+08:00 · 发表：2026-08-06T13:13:10Z · 修订：2026-08-08T11:15:00Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Fine Tuning VLAs with Self Demonstrated Generative Control。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：embodied-intelligence、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Do Tabular Foundation Models Agree with Themselves?</h2>
<p><a href="https://arxiv.org/abs/2608.06004v1">arXiv:2608.06004v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-30T09:22:00.677779+08:00 · 发表：2026-08-06T13:09:54Z · 修订：2026-08-06T13:09:54Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：The Embodiment Gap (arXiv:2608.06004, 8月19日) — 机器人基础模型的「本体鸿沟」有多大？。问题/方法/证据：关键词 : 跨本体泛化 · 基准测试 · 表征分析 · Robot Foundation Model 这篇工作系统性地测量了当前Robot Foundation Models在不同机器人本体（单臂→双臂→人形）之间的 迁移鸿沟 。发现： 视觉表征的迁移性远好于动作表征 动作空间的维度差异是跨本体泛化的最大瓶颈 当前SOTA模型在跨本体任务上性能下降30 60% 为什么重要 : 行业正在追捧「通用机器人大脑」的概念，但这篇工作泼了一盆冷水——本体之间的物理差异（自由度、运动学、动力学）造成的表征鸿沟，比想象中更难跨越。这为未来的跨本体学习研究指明了方向。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：行业正在追捧「通用机器人大脑」的概念，但这篇工作泼了一盆冷水——本体之间的物理差异（自由度、运动学、动力学）造成的表征鸿沟，比想象中更难跨越。这为未来的跨本体学习研究指明了方向。</p>
<p>关联问题：其他关注方向</p>
<p>标签：embodied-intelligence、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Novel Observable Signals from First-Order Gravitational Phase Transitions</h2>
<p><a href="https://arxiv.org/abs/2608.02736v1">arXiv:2608.02736v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-30T09:22:00.677779+08:00 · 发表：2026-08-03T18:00:04Z · 修订：2026-08-03T18:00:04Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Embodied.cpp。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：embodied-intelligence、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>ChainVLA: Chaining Vision-Language-Action Queries through a Unified Execution State for Long-Horizon Manipulation</h2>
<p><a href="https://arxiv.org/abs/2608.02326v2">arXiv:2608.02326v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-30T09:22:00.677779+08:00 · 发表：2026-08-03T14:48:20Z · 修订：2026-08-04T14:52:13Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：ChainVLA。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：embodied-intelligence、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone</h2>
<p><a href="https://arxiv.org/abs/2607.25895v1">arXiv:2607.25895v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-30T09:22:00.677779+08:00 · 发表：2026-07-28T15:52:02Z · 修订：2026-07-28T15:52:02Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：HiFi UMI。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：embodied-intelligence、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>DenseReward: Dense Reward Learning via Failure Synthesis for Robotic Manipulation</h2>
<p><a href="https://arxiv.org/abs/2607.13033v1">arXiv:2607.13033v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-30T09:22:00.677779+08:00 · 发表：2026-07-14T17:59:29Z · 修订：2026-07-14T17:59:29Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：DenseReward。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：embodied-intelligence、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>FlowWAM: Optical Flow as a Unified Action Representation for World Action Models</h2>
<p><a href="https://arxiv.org/abs/2607.13017v1">arXiv:2607.13017v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-30T09:22:00.677779+08:00 · 发表：2026-07-14T17:57:12Z · 修订：2026-07-14T17:57:12Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：FlowWAM。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：embodied-intelligence、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>From World Action Models to Embodied Brains: A Roadmap for Open-World Physical Intelligence</h2>
<p><a href="https://arxiv.org/abs/2607.11689v1">arXiv:2607.11689v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-30T09:22:00.677779+08:00 · 发表：2026-07-13T15:22:56Z · 修订：2026-07-13T15:22:56Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：From World Action Models to Embodied Brains。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：embodied-intelligence、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Artificial Foveated Perception for Mitigating Shortcut Learning in Robotic Foundation Models</h2>
<p><a href="https://arxiv.org/abs/2607.10655v2">arXiv:2607.10655v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-30T09:22:00.677779+08:00 · 发表：2026-07-12T08:42:36Z · 修订：2026-09-07T23:59:05Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Artificial Foveated Perception。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：embodied-intelligence、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models</h2>
<p><a href="https://arxiv.org/abs/2601.11404v2">arXiv:2601.11404v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-30T09:22:00.677779+08:00 · 发表：2026-01-16T16:17:06Z · 修订：2026-03-30T17:35:57Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：ACoT VLA。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：embodied-intelligence、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Diagnosing JEPA World Models with Action-Conditioned Predictive Consistency</h2>
<p><a href="https://arxiv.org/abs/2608.12939v1">arXiv:2608.12939v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-23T09:19:53.421472+08:00 · 发表：2026-08-13T08:18:41Z · 修订：2026-08-13T08:18:41Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Diagnosing JEPA World Models (arXiv:2608.12939, 8月13日) — JEPA也开始做&quot;体检。问题/方法/证据：关键词 : JEPA · 动作条件预测一致性 · 表征坍塌 LeCun力推的JEPA路线虽然火，但训练稳定性和诊断工具一直缺位。这篇工作提出了一套 动作条件预测一致性 诊断方法，能够检测JEPA世界模型中的表征质量问题。值得注意的是，这篇直接引用了LeWorldModel作为基准架构。 为什么重要 : JEPA从&quot;能不能训&quot;进入&quot;训得好不好&quot;阶段，诊断工具的出现意味着这个方向正在成熟。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：JEPA从&quot;能不能训&quot;进入&quot;训得好不好&quot;阶段，诊断工具的出现意味着这个方向正在成熟。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>WorldSimProbe: Diagnosing Simulator Faithfulness in Action-Conditioned World Models for Embodied Manipulation</h2>
<p><a href="https://arxiv.org/abs/2608.09298v1">arXiv:2608.09298v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-23T09:19:53.421472+08:00 · 发表：2026-08-10T08:48:06Z · 修订：2026-08-10T08:48:06Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：WorldSimProbe (arXiv:2608.09298, 8月10日) — 世界模型「体检报告」来了。问题/方法/证据：关键词 : 仿真保真度诊断 · 动作条件世界模型 · 具身操作 这篇工作提出了 WorldSimProbe ，一个专门诊断 动作条件世界模型 中仿真器保真度的框架。核心问题是：当前的世界模型在生成未来帧时，究竟有多忠实于真实物理？作者系统性地评估了世界模型在具身操作任务中的可靠性，发现很多模型在交互动力学方面存在系统性偏差。 为什么重要 : 世界模型不能只是&quot;看起来对&quot;，还得&quot;物理上对&quot;。这篇为下游策略训练提供了可靠的模型筛选工具。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：世界模型不能只是&quot;看起来对&quot;，还得&quot;物理上对&quot;。这篇为下游策略训练提供了可靠的模型筛选工具。</p>
<p>关联问题：世界模型与可靠规划</p>
<p>标签：world-models、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>The SIGReg Objective as Variational Free Energy: A Theoretical Active-Inference Account of JEPA World Models</h2>
<p><a href="https://arxiv.org/abs/2607.13612v1">arXiv:2607.13612v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-23T09:19:53.421472+08:00 · 发表：2026-07-15T08:59:36Z · 修订：2026-07-15T08:59:36Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：SIGReg理论。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>A Definition and Roadmap for World Models</h2>
<p><a href="https://arxiv.org/abs/2607.06401v1">arXiv:2607.06401v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-23T09:19:53.421472+08:00 · 发表：2026-07-07T15:31:32Z · 修订：2026-07-07T15:31:32Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：A Definition and Roadmap for World Models (arXiv:2607.06401, 7月7日) — 终于有人给世界模型下定义了。问题/方法/证据：关键词 : 定义框架 · 路线图 · 跨社区对齐 世界模型这个词被用得太泛了——RL社区、视频生成社区、具身智能社区各说各话。这篇综述试图 统一定义 ，并提出了一条清晰的roadmap：从&quot;被动预测&quot;到&quot;主动交互&quot;，从&quot;像素空间&quot;到&quot; latent 空间&quot;，从&quot;单模态&quot;到&quot;全模态&quot;。 关键观点 : 世界模型 ≠ 视频生成模型（虽然overlap很大） 真正的世界模型需要支持 反事实推理 和 动作条件预测 当前最大瓶颈：缺乏统一的评估标准和物理一致性保证局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation</h2>
<p><a href="https://arxiv.org/abs/2607.02604v1">arXiv:2607.02604v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-23T09:19:53.421472+08:00 · 发表：2026-07-01T13:16:44Z · 修订：2026-07-01T13:16:44Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：DynaWM。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>From World Models to World Action Models: A Concise Tutorial for Robotics</h2>
<p><a href="https://arxiv.org/abs/2607.00836v8">arXiv:2607.00836v8 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-23T09:19:53.421472+08:00 · 发表：2026-07-01T11:56:54Z · 修订：2026-09-08T09:16:15Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：From World Models to World Action Models (arXiv:2607.00836, 7月1日) — WAM 正在成为新范式。问题/方法/证据：关键词 : World Action Model · VLA融合 · 端到端决策 这篇明确提出了 World Action Model WAM 的概念：不只是预测世界怎么变，而是直接输出&quot;在这种世界状态下该做什么&quot;。这是世界模型从&quot;仿真器&quot;向&quot;决策器&quot;进化的关键一步。文中讨论了如何将世界模型与VLA（Vision Language Action）模型统一。 产业映射 : 小鹏 X World、华为 WEWA 2.0 都是这个方向的工程落地 Physical Intelligence的π0.7、π0.5也在走WAM路线局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Equilibrium World Models</h2>
<p><a href="https://arxiv.org/abs/2606.23463v1">arXiv:2606.23463v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-23T09:19:53.421472+08:00 · 发表：2026-06-22T15:12:02Z · 修订：2026-06-22T15:12:02Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Equilibrium World Models。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation</h2>
<p><a href="https://arxiv.org/abs/2606.03159v3">arXiv:2606.03159v3 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-23T09:19:53.421472+08:00 · 发表：2026-06-02T05:11:05Z · 修订：2026-09-23T19:11:35Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：NVIDIA OmniDreams。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Cosmos 3: Omnimodal World Models for Physical AI</h2>
<p><a href="https://arxiv.org/abs/2606.02800v4">arXiv:2606.02800v4 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-23T09:19:53.421472+08:00 · 发表：2026-06-01T19:12:30Z · 修订：2026-06-23T17:33:32Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Cosmos 3: Omnimodal World Models for Physical AI。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>RoboTrustBench: Benchmarking the Trustworthiness of Video World Models for Robotic Manipulation</h2>
<p><a href="https://arxiv.org/abs/2606.01600v2">arXiv:2606.01600v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-23T09:19:53.421472+08:00 · 发表：2026-06-01T02:56:09Z · 修订：2026-08-31T01:42:10Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：RoboTrustBench。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：世界模型与可靠规划</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>PhyWorld: Physics-Faithful World Model for Video Generation</h2>
<p><a href="https://arxiv.org/abs/2605.19242v1">arXiv:2605.19242v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-23T09:19:53.421472+08:00 · 发表：2026-05-19T01:28:52Z · 修订：2026-05-19T01:28:52Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：PhyWorld: Physics Faithful World Model for Video Generation。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Reinforcing VLAs in Task-Agnostic World Models</h2>
<p><a href="https://arxiv.org/abs/2605.12334v2">arXiv:2605.12334v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-23T09:19:53.421472+08:00 · 发表：2026-05-12T16:16:15Z · 修订：2026-05-20T07:28:11Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Reinforcing VLAs in Task Agnostic World Models。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation</h2>
<p><a href="https://arxiv.org/abs/2604.19092v2">arXiv:2604.19092v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-23T09:19:53.421472+08:00 · 发表：2026-04-21T05:09:56Z · 修订：2026-05-14T07:32:12Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：RoboWM Bench。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：世界模型与可靠规划</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>World-Gymnast: Training Robots with Reinforcement Learning in a World Model</h2>
<p><a href="https://arxiv.org/abs/2602.02454v1">arXiv:2602.02454v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-23T09:19:53.421472+08:00 · 发表：2026-02-02T18:44:45Z · 修订：2026-02-02T18:44:45Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：World gymnast。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：世界模型与可靠规划</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving</h2>
<p><a href="https://arxiv.org/abs/2510.12796v2">arXiv:2510.12796v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-23T09:19:53.421472+08:00 · 发表：2025-10-14T17:59:47Z · 修订：2025-12-18T07:25:29Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：DriveVLA W0。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>3D and 4D World Modeling: A Survey</h2>
<p><a href="https://arxiv.org/abs/2509.07996v4">arXiv:2509.07996v4 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-23T09:19:53.421472+08:00 · 发表：2025-09-04T17:59:58Z · 修订：2026-07-20T17:34:32Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：3D and 4D World Modeling: A Survey。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>TrustRoboReward: Preference-Ordered Isotonic Score Editing for Multi-Paradigm Robot Reward Models</h2>
<p><a href="https://arxiv.org/abs/2608.08491v1">arXiv:2608.08491v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-16T09:23:22.493231+08:00 · 发表：2026-08-09T05:25:22Z · 修订：2026-08-09T05:25:22Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：多尺度最优输运神经算子 (arXiv:2608.08491v1, 8月10日)。问题/方法/证据：标题 : Multiscale Optimal Transport Neural Operator 作者 : 研究团队 机构 : — 核心创新 : 将 最优输运理论 Optimal Transport 与神经算子结合，构建多尺度PDE求解器 利用OT的度量特性，在多尺度间建立物理上合理的映射关系 相比传统FNO，在多尺度物理问题（如湍流、多孔介质流动）上表现更优 意义 : 最优输运为神经算子提供了新的数学基础，可能在保持物理一致性的同时提升复杂多尺度问题的求解精度。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：最优输运为神经算子提供了新的数学基础，可能在保持物理一致性的同时提升复杂多尺度问题的求解精度。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>CoordRefer: Coordinate-Aware 3D Visual Grounding from Multiview Images</h2>
<p><a href="https://arxiv.org/abs/2608.05569v1">arXiv:2608.05569v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-16T09:23:22.493231+08:00 · 发表：2026-08-06T03:40:17Z · 修订：2026-08-06T03:40:17Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：CL-PINN: 参数化PDE的连续学习框架 (arXiv:2608.05569v1, 8月5日)。问题/方法/证据：标题 : Continual Learning Physics Informed Neural Networks for Parameterized Partial Differential Equations 作者 : Feiyang Chen et al. 机构 : 国防科技大学 核心创新 : 首次将 连续学习 Continual Learning 引入PINN，解决参数化PDE求解中的 灾难性遗忘 问题 提出CL PINN框架：当模型按顺序学习不同参数配置的PDE时，自动保留先前学到的知识 通过梯度投影和参数隔离技术，在不影响新任务学习的前提下维持旧任务的精度 意义 : 传统PINN在参数化PDE上训练时，学习新参数会遗忘旧参数，CL PINN使单模型可连续适配不同物理场景，大幅提升了PINN的工程实用性局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：传统PINN在参数化PDE上训练时，学习新参数会遗忘旧参数，CL-PINN使单模型可连续适配不同物理场景，大幅提升了PINN的工程实用性。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Thermodynamically consistent initialization of the Maxwell--Cattaneo---Vernotte heat conduction model: Analytical solutions and engineering applications</h2>
<p><a href="https://arxiv.org/abs/2608.03495v1">arXiv:2608.03495v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-16T09:23:22.493231+08:00 · 发表：2026-08-04T11:34:01Z · 修订：2026-08-04T11:34:01Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Enhanced Diffusion Sampling: /。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Discrete Truthful Heterogeneous Two-Facility Location: The Line and Beyond</h2>
<p><a href="https://arxiv.org/abs/2607.21046v1">arXiv:2607.21046v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-16T09:23:22.493231+08:00 · 发表：2026-07-23T08:29:21Z · 修订：2026-07-23T08:29:21Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：EvoPINN: LLM驱动的PINN自动算法发现 (arXiv:2607.21046v1, 7月29日)。问题/方法/证据：标题 : EvoPINN: Agentic Discovery of Executable Algorithms for Physics Informed Neural Networks 作者 : Aniket Jadhav et al. 机构 : Texas A&amp;M University 核心创新 : 将 LLM Agent 引入PINN算法设计，实现全自动的算法进化与发现 框架包含：LLM生成候选算法 → 自动代码执行 → 性能评估 → 反馈优化 → 迭代进化 自动发现的新算法在多个基准PDE上超越了人类手工设计的SOTA方法 意义 : 这是&quot;AI设计AI&quot;在科学计算领域的重要落地。EvoPINN证明LLM不仅能写代码，还能自主发现解决PDE的新算法范式，标志着SciML进入 自动化算法工程 时代。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：这是&quot;AI设计AI&quot;在科学计算领域的重要落地。EvoPINN证明LLM不仅能写代码，还能自主发现解决PDE的新算法范式，标志着SciML进入**自动化算法工程**时代。</p>
<p>关联问题：人类视频与机器人数据需求</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Real vs. Complex Spectral Bases for Neural Operators: The Role of Green&#x27;s Function Alignment</h2>
<p><a href="https://arxiv.org/abs/2606.24851v5">arXiv:2606.24851v5 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-16T09:23:22.493231+08:00 · 发表：2026-06-23T17:29:15Z · 修订：2026-09-28T17:39:21Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Hartley Neural Operator (arXiv:2606.24851)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Enhanced Diffusion Sampling: Efficient Rare Event Sampling and Free Energy Calculation with Diffusion Models</h2>
<p><a href="https://arxiv.org/abs/2602.16634v2">arXiv:2602.16634v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-16T09:23:22.493231+08:00 · 发表：2026-02-18T17:26:15Z · 修订：2026-06-28T12:48:36Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Enhanced Diffusion Sampling: /。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Decoding Partial Differential Equations: Cross-Modal Adaptation of Decoder-only Models to PDEs</h2>
<p><a href="https://arxiv.org/abs/2510.05278v2">arXiv:2510.05278v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-16T09:23:22.493231+08:00 · 发表：2025-10-06T18:46:50Z · 修订：2026-03-06T09:09:43Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：跨模态Decoder-only模型求解PDE (arXiv:2510.05278v2, 2026年3月更新)。问题/方法/证据：标题 : Cross Modal Adaptation of Decoder only Models to PDEs 核心思路 : 将LLM（decoder only架构）跨模态适配到PDE求解任务 不训练专用科学模型，而是利用预训练LLM的推理能力理解并求解偏微分方程 与PDE FM、POSEIDON、UNISOLVER等专用基础模型形成互补路径 意义 : 探索了&quot;通用AI做科学&quot;的可能性——无需专门训练科学模型，利用LLM的跨模态能力即可处理PDE。这暗示未来可能出现 统一的基础模型 ，同时处理语言、代码和科学问题。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：探索了&quot;通用AI做科学&quot;的可能性——无需专门训练科学模型，利用LLM的跨模态能力即可处理PDE。这暗示未来可能出现**统一的基础模型**，同时处理语言、代码和科学问题。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Poseidon: Efficient Foundation Models for PDEs</h2>
<p><a href="https://arxiv.org/abs/2405.19101v2">arXiv:2405.19101v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-16T09:23:22.493231+08:00 · 发表：2024-05-29T14:06:51Z · 修订：2024-11-05T16:32:43Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Poseidon (PDE Foundation Model)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>SpecDrop: Parameter-Free Category-Conditioned Routing for Modular Specialization</h2>
<p><a href="https://arxiv.org/abs/2608.04084v2">arXiv:2608.04084v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-09T09:37:41.890691+08:00 · 发表：2026-08-04T18:00:01Z · 修订：2026-09-27T04:41:15Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：SpecDrop — 无参数类别条件路由的模块化专业化 (arXiv:2608.04084)。问题/方法/证据：团队 : Boyao Wang, Zhihan Lei 对MoE路由机制的一次 概念性质疑 ：论文发现，在匹配总参数量的情况下，学到的路由器可能不如等权重的No Routing基线。瓶颈不在路由算法本身，而在 训练信号粒度与目标类别的对齐 。 核心发现 : SpecDrop：固定无参数路由方案（类别标签决定分支权重，无学习参数） 在CIFAR 100上达到79.23%（+4.75 over dense） 在ImageNet 1K上达到79.89%（+6.53 over No Routing+SE） 58% 100%分支 类别对齐率，证明类别监督可以内化为模块化结构 为什么重要 : 这篇论文提出了一个深刻的观点——MoE的收益可能来自 类别监督的结构化 ，而非路由算法的复杂性。这为MoE设计提供了新的简化方向。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：这篇论文提出了一个深刻的观点——MoE的收益可能来自**类别监督的结构化**，而非路由算法的复杂性。这为MoE设计提供了新的简化方向。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Spend Bits Where Queries Look: KV Cache Vector Quantization with Attention-Preserving Transforms</h2>
<p><a href="https://arxiv.org/abs/2608.04074v1">arXiv:2608.04074v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-09T09:37:41.890691+08:00 · 发表：2026-08-04T16:10:59Z · 修订：2026-08-04T16:10:59Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：NOVA-KV — 注意力感知的KV缓存向量量化 (arXiv:2608.04074)。问题/方法/证据：团队 : USC Fernández Menduiña, Ziashahabi, Ortega, Avestimehr 长上下文LLM推理的内存瓶颈正在被重新定义。NOVA KV将KV缓存量化问题重新建模为 变换编码问题 ——以注意力乘积误差为失真度量，推导出了闭式最优变换。 核心创新 : 最优Key变换 非正交 ，满足广义Parseval关系：变换域MSE = 原始域注意力失真 提出 等体积分组 策略，使固定大小码本逼近变率最优 在2 bits/element下，长上下文检索精度显著优于QuaRot、OSCAR等SOTA方法 在128K上下文下，Qwen3 8B上NOVA KV达到75.4 vs OSCAR的25.3 BF16基线83.4 为什么重要 : 这是首个从率失真理论出发、针对注意力产品而非单纯MSE局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：这是首个从率失真理论出发、针对注意力产品而非单纯MSE设计的KV缓存量化方案，为长上下文LLM serving提供了新的工程范式。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>SJEPA: Learning Elegant Latent Dynamics with Hybrid Symbolic-Neural Predictors</h2>
<p><a href="https://arxiv.org/abs/2608.04060v1">arXiv:2608.04060v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-09T09:37:41.890691+08:00 · 发表：2026-08-04T13:08:07Z · 修订：2026-08-04T13:08:07Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：SJEPA — 混合符号-神经预测器学习优雅潜动态 (arXiv:2608.04060)。问题/方法/证据：团队 : Yongchao Huang JEPA架构正在向 可解释性 方向进化。SJEPA（Symbolic JEPA）首次在联合嵌入预测架构中引入了符号动力学描述。 核心创新 : 混合转移模型 = 符号定律 + 正则化神经修正 表示约束保留信息丰富的非坍塌预测坐标 算子压缩偏好低复杂度符号 神经转移 在受控摆实验中，联合学习发现的符号动力学比事后拟合 更简单、长期 rollout 误差更低 为什么重要 : 这条路线试图解决深度学习最深层的问题之一——黑盒模型的可解释性。如果能在表示学习中自动发现简洁的符号规律，将是通往&quot;可理解AI&quot;的重要一步。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：这条路线试图解决深度学习最深层的问题之一——黑盒模型的可解释性。如果能在表示学习中自动发现简洁的符号规律，将是通往&quot;可理解AI&quot;的重要一步。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>LaPrune: Controllable Differentiable Sparsity at Million Scale</h2>
<p><a href="https://arxiv.org/abs/2608.04057v1">arXiv:2608.04057v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-09T09:37:41.890691+08:00 · 发表：2026-08-04T12:17:00Z · 修订：2026-08-04T12:17:00Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：LaPrune (arXiv:2608.04057)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>CAMP: A Cycle-Aware Multi-Scale Patch Mixer for Time Series Forecasting</h2>
<p><a href="https://arxiv.org/abs/2608.04051v1">arXiv:2608.04051v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-09T09:37:41.890691+08:00 · 发表：2026-08-04T10:04:16Z · 修订：2026-08-04T10:04:16Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：CAMP (arXiv:2608.04051)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Recurrent Residual Quantization: A Progressive Multi-Precision Representation for LLMs</h2>
<p><a href="https://arxiv.org/abs/2608.04048v1">arXiv:2608.04048v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-09T09:37:41.890691+08:00 · 发表：2026-08-04T08:32:05Z · 修订：2026-08-04T08:32:05Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Recurrent Residual Quantization (RRQ) — 单检查点多精度LLM (arXiv:2608.04048)。问题/方法/证据：团队 : Yu Luo, Bo Dong, Wenhua Cheng, Haihao Shen NeurIPS 2026投稿 核心洞察 : 传统量化需要为每个目标位宽单独训练/保存检查点。RRQ提出 递归残差量化 ，从单一2 bit基线出发，通过叠加轻量级2 bit残差，构造4/6/8 bit表示。 关键指标 : 构建2/4/6/8 bit全RTN包仅需1,293秒（比MatGPTQ快3.3倍） 校准无关，避免联合多比特优化 6 bit和8 bit精度具有竞争力 为什么重要 : 云服务商需要在同一硬件上服务不同精度要求的客户。RRQ的&quot;一次量化，多精度部署&quot;模式极具工程价值。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：云服务商需要在同一硬件上服务不同精度要求的客户。RRQ的&quot;一次量化，多精度部署&quot;模式极具工程价值。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Robust and Personalized Federated Learning for Aircraft-Engine Prognostics under Benign and Adversarial Client Heterogeneity</h2>
<p><a href="https://arxiv.org/abs/2608.04045v1">arXiv:2608.04045v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-09T09:37:41.890691+08:00 · 发表：2026-08-04T06:54:29Z · 修订：2026-08-04T06:54:29Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：联邦学习航空发动机 (arXiv:2608.04045)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Tactus: Open-Vocabulary Object Recognition from Low-Cost Pressure Arrays</h2>
<p><a href="https://arxiv.org/abs/2608.04043v1">arXiv:2608.04043v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-09T09:37:41.890691+08:00 · 发表：2026-08-04T06:08:21Z · 修订：2026-08-04T06:08:21Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Tactus (arXiv:2608.04043)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>An Explainable LLM Agent Layer for Open-World Anomaly Detection in Oil Wells</h2>
<p><a href="https://arxiv.org/abs/2608.04041v1">arXiv:2608.04041v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-09T09:37:41.890691+08:00 · 发表：2026-08-04T01:44:06Z · 修订：2026-08-04T01:44:06Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：油井异常检测LLM Agent (arXiv:2608.04041)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>A Trust-region Framework for Moment Estimation</h2>
<p><a href="https://arxiv.org/abs/2608.04026v2">arXiv:2608.04026v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-09T09:37:41.890691+08:00 · 发表：2026-07-26T20:46:45Z · 修订：2026-08-08T09:29:09Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Trust region Adam (arXiv:2608.04026)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>On Hamming-Lipschitz Type Stability of the Subdominant (Minmax) Ultrametric: Theory and Simple Proofs</h2>
<p><a href="https://arxiv.org/abs/2608.04014v1">arXiv:2608.04014v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-09T09:37:41.890691+08:00 · 发表：2026-04-27T12:16:34Z · 修订：2026-04-27T12:16:34Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Hamming Lipschitz稳定性 (arXiv:2608.04014)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>C$^2$MOE: Consistency and Complementarity-guided Mixture of Experts for Incomplete Multimodal Emotion Learning</h2>
<p><a href="https://arxiv.org/abs/2608.04013v1">arXiv:2608.04013v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-09T09:37:41.890691+08:00 · 发表：2026-04-22T13:17:48Z · 修订：2026-04-22T13:17:48Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：C²MOE — 不一致多模态情感学习的混合专家 (arXiv:2608.04013)。问题/方法/证据：团队 : Yuntao Shou, Tao Meng, Wei Ai, Keqin Li 针对真实世界中多模态数据 缺失模态 的问题，C²MOE提出了一致性与互补性引导的MoE框架。 核心创新 : 信息论框架统一表示学习与缺失模态插补 将多模态知识分解为一致性（跨模态可预测性最大化）和互补性（条件熵最大化） 双分支预测机制：一致性分支最小化不确定性，互补性分支利用模态独特线索 可学习重加权模块动态分配专家重要性 为什么重要 : 这是MoE架构在 多模态鲁棒学习 中的创新应用，对实际部署中常见的传感器/模态缺失问题有直接价值。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：这是MoE架构在**多模态鲁棒学习**中的创新应用，对实际部署中常见的传感器/模态缺失问题有直接价值。</p>
<p>关联问题：机器人实际部署约束</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>When Correct Solutions Repeat: Rarity-Aware Credit Redistribution for GRPO</h2>
<p><a href="https://arxiv.org/abs/2608.03467v2">arXiv:2608.03467v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-09T09:37:41.890691+08:00 · 发表：2026-08-04T11:02:26Z · 修订：2026-08-05T11:58:57Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Cue GRPO (arXiv:2608.03467)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Learning</h2>
<p><a href="https://arxiv.org/abs/2607.21653v3">arXiv:2607.21653v3 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-02T09:20:27.164349+08:00 · 发表：2026-07-22T18:06:15Z · 修订：2026-09-22T19:00:49Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Molt — 轻量级 Agentic RL 训练框架 (arXiv:2607.21653, 7月22日)。问题/方法/证据：一句话 : 只有 8.6K 行代码的 PyTorch native Agentic RL 框架，能训 1T MoE。 定位 : 比 verl ~62K LOC 和 slime ~25K LOC 更精简，专为 agentic 研究设计 架构 : AutoModel + vLLM，FSDP2 + EP/CP，原生支持 MoE 亮点 : Agent 就是普通 Python 函数，无 DSL 权重同步走 NCCL broadcast，不经过 router speculation decoding、prefix caching、CUDA graphs 都是 engine flag 验证 : 700B MoE @ EP256 端到端跑通；Qwen3 30B A3B 上与 slime 吞吐量持平 461 vs 502 tok局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：Agentic RL 训练门槛正在大幅降低</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Talaria: Session-Aware Serverless Serving of Hundred-Billion-Parameter LLMs</h2>
<p><a href="https://arxiv.org/abs/2607.17181v1">arXiv:2607.17181v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-02T09:20:27.164349+08:00 · 发表：2026-07-19T10:37:33Z · 修订：2026-07-19T10:37:33Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Talaria — 面向 Agentic 负载的无服务器多模型推理 (arXiv:2607.17181, 7月19日)。问题/方法/证据：一句话 : 给 Agent 用的推理系统，模型切换和会话返回比单次推理更重要。 场景 : Agentic 工作流中，多模型切换频繁，会话可能中断后返回，传统 serving 假设&quot;模型常驻 GPU&quot;不再成立 设计 : 模型可换出 GPU 而不丢失会话前缀 基于会话返回概率的预加载策略 多模型共置避免跨层 KV handoff 意义 : Agentic 负载正在重塑 serving 系统的核心假设局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：Agentic 负载正在重塑 serving 系统的核心假设</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>From Tensor Buffer to Distributed Memory Hierarchy: A Survey of KV Cache Management for LLM Serving</h2>
<p><a href="https://arxiv.org/abs/2607.02574v1">arXiv:2607.02574v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-02T09:20:27.164349+08:00 · 发表：2026-06-30T16:12:40Z · 修订：2026-06-30T16:12:40Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：KV Cache 管理全景综述 (arXiv:2607.02574, 6月30日)。问题/方法/证据：一句话 : 这是目前最系统的 KV Cache 管理综述，把零散工作归纳成 6 大设计策略 + 5 种系统范式。 六大设计响应 : 1. 本地 KV 虚拟化与阶段感知调度 PagedAttention, Orca 2. KV 压缩/量化/稀疏化 eviction, quantization, compression 3. Prefill/Decode 分离 DistServe, Splitwise 4. 跨层级 KV 迁移 HBM → DRAM → 远端存储 5. 共享前缀缓存 Prefix caching, RadixAttention 6. 多租户隔离与安全 五大系统范式 : 单体实例、分离式管道、共享存储池、分层缓存、无服务器 价值 : 做推理系统的人，这篇可以当导航图用局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Towards Load-Aware Prefill Deflection for Disaggregated LLM Serving</h2>
<p><a href="https://arxiv.org/abs/2607.02043v1">arXiv:2607.02043v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-02T09:20:27.164349+08:00 · 发表：2026-07-02T11:10:05Z · 修订：2026-07-02T11:10:05Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Kairos — 负载感知的 Prefill 偏转调度 (arXiv:2607.02043, 7月2日, Microsoft)。问题/方法/证据：一句话 : PD 分离架构下，把 Prefill 任务&quot;甩&quot;给负载轻的 Decode 节点，P95 TTFT 最高砍 81%。 痛点 : PD 分离后，Prefill 节点在流量突发时饱和，而 Decode 节点算力闲置；排队 + 跨节点 KV 传输占 TTFT 的 77 98% 解法 : Kairos 实时估计每个请求在 Prefill 节点的 TTFT，同时在每个 Decode 节点搜索&quot;安全 chunk 大小&quot;，在满足 TBT SLO 的前提下将 Prefill 任务偏转到 Decode 节点执行 效果 : P95 TTFT 降低最高 81%，SLO 达成率提升最高 79%，每次调度决策 &lt; 1ms 意义 : PD 分离不是终点，动态负载均衡才是下一步局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：PD 分离不是终点，动态负载均衡才是下一步</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving</h2>
<p><a href="https://arxiv.org/abs/2607.00466v2">arXiv:2607.00466v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-02T09:20:27.164349+08:00 · 发表：2026-07-01T05:34:38Z · 修订：2026-07-02T08:02:42Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：ELDR — MoE 解码路由的专家局部性感知 (arXiv:2607.00466, 7月1日)。问题/方法/证据：一句话 : MoE 的 Decode 阶段，&quot;负载均衡&quot;不够，还要看&quot;专家局部性&quot;。 发现 : 在 MoE 的 batched decode 中，延迟由批次中所有 token 选中的 专家并集 决定，而非 token 数量。active expert 从 16 增至 128，MoE 层延迟涨 4.7× 解法 : ELDR 在 PD 分离的 decode 路由中引入专家局部性感知，将具有相似专家偏好的请求路由到同一 worker 意义 : MoE 推理优化进入了&quot;第二维度&quot;——不只是 load balance，还有 expert locality局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：MoE 推理优化进入了&quot;第二维度&quot;——不只是 load balance，还有 expert locality</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Token-Operations-Oriented Inference Optimization Techniques for Large Models</h2>
<p><a href="https://arxiv.org/abs/2606.20295v2">arXiv:2606.20295v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-02T09:20:27.164349+08:00 · 发表：2026-06-18T14:33:09Z · 修订：2026-07-24T07:54:17Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Token Operations Oriented Inference Optimization 综述。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>From Detection to Recovery: Operational Analysis on LLM Pre-training with 504 GPUs</h2>
<p><a href="https://arxiv.org/abs/2605.09370v5">arXiv:2605.09370v5 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-02T09:20:27.164349+08:00 · 发表：2026-05-10T06:46:06Z · 修订：2026-06-15T04:11:47Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Lablup 504 GPU 预训练运维报告。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Scalable Training of Mixture-of-Experts Models with Megatron Core</h2>
<p><a href="https://arxiv.org/abs/2603.07685v2">arXiv:2603.07685v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-02T09:20:27.164349+08:00 · 发表：2026-03-08T15:42:43Z · 修订：2026-03-10T06:23:58Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Megatron Core MoE 技术报告。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>PROBE: Co-Balancing Computation and Communication in MoE Inference via Real-Time Predictive Prefetching</h2>
<p><a href="https://arxiv.org/abs/2602.00509v2">arXiv:2602.00509v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-02T09:20:27.164349+08:00 · 发表：2026-01-31T04:37:55Z · 修订：2026-02-03T06:25:29Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：PROBE。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving</h2>
<p><a href="https://arxiv.org/abs/2501.01005v2">arXiv:2501.01005v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-08-02T09:20:27.164349+08:00 · 发表：2025-01-02T02:02:20Z · 修订：2025-04-21T20:10:11Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：FLASHINFER。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>HiMem-WAM: Hierarchical Memory-Gated World Action Models for Robotic Manipulation</h2>
<p><a href="https://arxiv.org/abs/2606.10363v1">arXiv:2606.10363v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-24T22:58:46.442269+08:00 · 发表：2026-06-09T03:22:34Z · 修订：2026-06-09T03:22:34Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：HiMem WAM。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation</h2>
<p><a href="https://arxiv.org/abs/2606.09215v1">arXiv:2606.09215v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-24T22:58:46.442269+08:00 · 发表：2026-06-08T08:50:14Z · 修订：2026-06-08T08:50:14Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：MotionWAM。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：人类视频与机器人数据需求</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Unifying Object-Centric World Models and Diffusion Policy: A Hierarchical Framework for Multi-Stage Robotic Tasks</h2>
<p><a href="https://arxiv.org/abs/2606.08775v1">arXiv:2606.08775v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-24T22:58:46.442269+08:00 · 发表：2026-06-07T18:39:45Z · 修订：2026-06-07T18:39:45Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：WorldDP。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：世界模型与可靠规划</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>WAM-Nav: Asymmetric Latent World-Action Modeling for Unified Visual Navigation</h2>
<p><a href="https://arxiv.org/abs/2606.04907v2">arXiv:2606.04907v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-24T22:58:46.442269+08:00 · 发表：2026-06-03T14:05:19Z · 修订：2026-06-13T10:28:53Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：WAM Nav。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>NoiseGate: Learning Per-Latent Timestep Schedules as Information Gating in World Action Models</h2>
<p><a href="https://arxiv.org/abs/2605.07794v1">arXiv:2605.07794v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-24T22:58:46.442269+08:00 · 发表：2026-05-08T14:31:52Z · 修订：2026-05-08T14:31:52Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：NoiseGate。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels</h2>
<p><a href="https://arxiv.org/abs/2603.19312v3">arXiv:2603.19312v3 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-24T22:58:46.442269+08:00 · 发表：2026-03-13T19:48:14Z · 修订：2026-06-03T18:50:40Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：**LeWorldModel (LeWM)** (arXiv:2603.19312, Mar 13) — 第一个真正稳定端到端训练的 JEPA。问题/方法/证据：现有 JEPA 方法依赖复杂多损失项、EMA、预训练编码器或辅助监督来避免表征坍缩。LeWM 只用 **两个损失项**（next-embedding prediction + Gaussian-distributed latent regularizer）就实现了稳定端到端训练。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：把可调超参从 6 个降到 1 个。~15M 参数，单 GPU 几小时训练完。在 2D/3D 控制任务上**比 foundation-model-based world models 快 48x** 规划速度。latent space 能通过探测编码有意义的物理结构（如物体位置、速度），且能检测物理上不合理的事件（surprise evaluation）。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control</h2>
<p><a href="https://arxiv.org/abs/2603.10448v2">arXiv:2603.10448v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-24T22:58:46.442269+08:00 · 发表：2026-03-11T06:03:53Z · 修订：2026-03-22T07:28:45Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Dit4Dit。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos</h2>
<p><a href="https://arxiv.org/abs/2602.06949v1">arXiv:2602.06949v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-24T22:58:46.442269+08:00 · 发表：2026-02-06T18:49:43Z · 修订：2026-02-06T18:49:43Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：DreamDojo。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：世界模型与可靠规划、人类视频与机器人数据需求</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Temperature Field Reconstruction of Tungsten Monoblock Divertor on EAST using Physics-aware Neural Operator Transformer</h2>
<p><a href="https://arxiv.org/abs/2606.31574v1">arXiv:2606.31574v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-12T09:18:45.088994+08:00 · 发表：2026-06-30T12:33:06Z · 修订：2026-06-30T12:33:06Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Physics-aware Neural Operator Transformer for EAST Divertor。问题/方法/证据：将**物理感知神经算子与Transformer结合**，用于托卡马克（EAST）钨单块偏滤器的温度场重建。融合物理约束的注意力机制处理聚变装置中的极端热负荷。原报告标注日期：2026-06-30。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：SciML在**核聚变工程**中的前沿应用，展示了物理感知架构对高保真科学仪器的价值。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>TF-SNO: Time-Frequency Gated Spectral Neural Operators for Learning Non-Stationary Partial Differential Equations</h2>
<p><a href="https://arxiv.org/abs/2606.21189v1">arXiv:2606.21189v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-12T09:18:45.088994+08:00 · 发表：2026-06-19T07:57:43Z · 修订：2026-06-19T07:57:43Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：TF-SNO: Time-Frequency Gated Spectral Neural Operators。问题/方法/证据：提出**时频门控谱神经算子**，专门解决**非平稳PDE**的学习难题。传统FNO在频率域全局处理，难以捕捉时变特征；TF-SNO通过时频分解+门控机制，在谱域实现自适应时频局部化。原报告标注日期：2026-06-19。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：填补了神经算子在非平稳动力学（如湍流、波动传播）上的空白，是FNO架构的重要进化。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Dual-Network PINNs for Optimal Control: A Reproducible Benchmark on the Mass-Spring-Damper System</h2>
<p><a href="https://arxiv.org/abs/2606.15271v1">arXiv:2606.15271v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-12T09:18:45.088994+08:00 · 发表：2026-06-13T12:10:17Z · 修订：2026-06-13T12:10:17Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Dual-Network PINNs for Optimal Control。问题/方法/证据：针对质量-弹簧-阻尼系统，提出**双网络PINN架构**统一状态近似、控制优化和参数估计，在可微优化框架内解决最优控制问题。原报告标注日期：2026-06-13。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：PINN方法论向**控制论**和**PDE约束优化**的系统性拓展，验证了物理信息学习在工程控制中的实用性。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>On the training of physics-informed neural operators for solving parametric partial differential equations</h2>
<p><a href="https://arxiv.org/abs/2606.06164v1">arXiv:2606.06164v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-12T09:18:45.088994+08:00 · 发表：2026-06-04T13:36:22Z · 修订：2026-06-04T13:36:22Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：6.31×。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>jNO: A JAX Library for Neural Operator and Foundation Model Training</h2>
<p><a href="https://arxiv.org/abs/2605.10159v1">arXiv:2605.10159v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-12T09:18:45.088994+08:00 · 发表：2026-05-11T08:05:54Z · 修订：2026-05-11T08:05:54Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：jNO。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Compositional Meta-Learning for Mitigating Task Heterogeneity in Physics-Informed Neural Networks</h2>
<p><a href="https://arxiv.org/abs/2604.26999v1">arXiv:2604.26999v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-12T09:18:45.088994+08:00 · 发表：2026-04-29T03:09:57Z · 修订：2026-04-29T03:09:57Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：LAM-PINN: Compositional Meta-Learning for PINNs。问题/方法/证据：**组合式元学习PINN** —— 不依赖单一全局初始化，而是将模型分解为聚类专用子网络+共享元网络，通过学习亲和度动态路由，缓解任务异质性带来的负迁移。原报告标注日期：2026-04-29。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：为参数化PDE家族的高效迁移提供了模块化新范式。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Transferable Physics-Informed Representations via Closed-Form Head Adaptation</h2>
<p><a href="https://arxiv.org/abs/2604.21761v1">arXiv:2604.21761v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-12T09:18:45.088994+08:00 · 发表：2026-04-23T15:08:28Z · 修订：2026-04-23T15:08:28Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Pi-PINN: Transferable Physics-Informed Representations。问题/方法/证据：基于伪逆PINN框架，学习**可迁移的物理信息表示**，通过闭式头部适应（closed-form head adaptation）快速求解新PDE实例。无需任何新数据即可泛化到未见PDE。原报告标注日期：2026-04-23。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：PINN从「单问题求解器」迈向「通用物理表示学习」的关键一步。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Operator Learning Using Weak Supervision from Walk-on-Spheres</h2>
<p><a href="https://arxiv.org/abs/2603.01193v2">arXiv:2603.01193v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-12T09:18:45.088994+08:00 · 发表：2026-03-01T17:23:39Z · 修订：2026-03-03T18:07:51Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：6.31×。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Exact Constraint Enforcement in Physics-Informed Extreme Learning Machines using Null-Space Projection Framework</h2>
<p><a href="https://arxiv.org/abs/2601.10999v2">arXiv:2601.10999v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-12T09:18:45.088994+08:00 · 发表：2026-01-16T05:18:56Z · 修订：2026-01-20T15:28:58Z</p>
<p><strong>自动摘要：</strong>【已撤回，仅供历史参考】arXiv 官方 v2 于 2026-01-20 撤回；作者称需大幅修订表述及与相关文献的关系。v1 历史页面：https://arxiv.org/abs/2601.10999v1。以下为当时扫描解读，不作为当前有效结论：历史周报其他关注条目：Exact Constraint Enforcement in PIELMs。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Enabling self-supervised learned primal dual with Noise2Inverse</h2>
<p><a href="https://arxiv.org/abs/2606.26991v1">arXiv:2606.26991v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-05T09:20:20.343351+08:00 · 发表：2026-06-25T13:07:15Z · 修订：2026-06-25T13:07:15Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Enabling self supervised learned primal dual with Noise2Inverse。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Leveraging AutoML for Sustainable Deep Learning: A Multi-Objective HPO Approach on Deep Shift Neural Networks</h2>
<p><a href="https://arxiv.org/abs/2606.23208v1">arXiv:2606.23208v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-05T09:20:20.343351+08:00 · 发表：2026-06-22T11:53:42Z · 修订：2026-06-22T11:53:42Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Deep Shift Neural Networks + AutoML。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>ConTraIRL: Factorized Contrastive Abstractions for Transferable IRL</h2>
<p><a href="https://arxiv.org/abs/2606.03017v2">arXiv:2606.03017v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-05T09:20:20.343351+08:00 · 发表：2026-06-02T01:47:19Z · 修订：2026-09-25T23:03:17Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：ConTraIRL: Factorized Contrastive Abstractions for Transferable IRL。问题/方法/证据：将对比学习与逆强化学习结合，提出因子化对比抽象方法，实现跨任务的可迁移性。原报告标注日期：2026-06-02。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：连接了自监督表示学习与强化学习，为多任务迁移学习提供新范式。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Forget Attention: Importance-Aware Attention Is All You Need</h2>
<p><a href="https://arxiv.org/abs/2606.02332v2">arXiv:2606.02332v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-05T09:20:20.343351+08:00 · 发表：2026-06-01T14:42:06Z · 修订：2026-06-02T05:51:37Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Forget Attention: Importance-Aware Attention Is All You Need。问题/方法/证据：提出&quot;重要性感知注意力&quot;机制，通过动态评估token重要性来优化注意力计算，在保持性能的同时降低计算开销。原报告标注日期：2026-06-02。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：直接对标Transformer核心机制，可能替代传统注意力成为更高效的选择。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>BrainDINO: A Brain MRI Foundation Model for Generalizable Clinical Representation Learning</h2>
<p><a href="https://arxiv.org/abs/2604.27277v3">arXiv:2604.27277v3 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-05T09:20:20.343351+08:00 · 发表：2026-04-30T00:21:36Z · 修订：2026-06-11T15:15:37Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：BrainDINO。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>ELMoE-3D: Leveraging Intrinsic Elasticity of MoE for Hybrid-Bonding-Enabled Self-Speculative Decoding in On-Premises Serving</h2>
<p><a href="https://arxiv.org/abs/2604.14626v2">arXiv:2604.14626v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-05T09:20:20.343351+08:00 · 发表：2026-04-16T05:12:51Z · 修订：2026-04-23T01:19:26Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：ELMoE 3D。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>A PAC-Bayesian approach to generalization for quantum models</h2>
<p><a href="https://arxiv.org/abs/2603.22964v1">arXiv:2603.22964v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-05T09:20:20.343351+08:00 · 发表：2026-03-24T08:58:54Z · 修订：2026-03-24T08:58:54Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：A PAC Bayesian approach to generalization for quantum models。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Towards A Unified PAC-Bayesian Framework for Norm-based Generalization Bounds</h2>
<p><a href="https://arxiv.org/abs/2601.08100v1">arXiv:2601.08100v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-07-05T09:20:20.343351+08:00 · 发表：2026-01-13T00:42:22Z · 修订：2026-01-13T00:42:22Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Towards A Unified PAC-Bayesian Framework for Norm-based Generalization Bounds。问题/方法/证据：提出统一的PAC-Bayesian框架，将泛化界推导重新表述为各向异性高斯后验上的随机优化问题。原报告标注日期：2026-01-13。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：为深度学习的泛化理论提供了更紧致的、结构感知的理论保证。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>WiSP: A Working-Set View of Mixture-of-Experts Serving on Extremely Low-Resource Hardware</h2>
<p><a href="https://arxiv.org/abs/2606.21868v1">arXiv:2606.21868v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-28T12:00:14.444527+08:00 · 发表：2026-06-20T04:10:34Z · 修订：2026-06-20T04:10:34Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：WiSP — Routing-Aware Paging for Low-Resource MoE Serving。问题/方法/证据：针对 MoE 模型的**路由感知分页机制**。传统 paging 对 MoE 的 expert activation pattern 不敏感，WiSP 让内存管理器感知 router 的决策，把即将被激活的 expert 提前换入，减少 decode 阶段的 page fault。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：MoE serving 的内存效率一直是暗坑。WiSP 是少有的从&quot;router 语义&quot;切入做内存管理的论文，思路很刁钻。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>PithTrain: A Compact and Agent-Native MoE Training System</h2>
<p><a href="https://arxiv.org/abs/2605.31463v1">arXiv:2605.31463v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-28T12:00:14.444527+08:00 · 发表：2026-05-29T15:52:58Z · 修订：2026-05-29T15:52:58Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：PithTrain — Compact and Agent-Native MoE Training System。问题/方法/证据：一个专为 Agent 场景设计的**紧凑型 MoE 训练系统**。强调&quot;agent-native&quot;——不是把通用 MoE 模型拿来给 agent 用，而是从训练目标、数据混合策略、router design 三个层面重新设计。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：MoE 在 2026 年已经是标配，但&quot;通用 MoE&quot;和&quot;Agent MoE&quot;的 gap 越来越大。PithTrain 代表了从 infra 层开始为 agent 定制模型的趋势。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>VeriCache: Turning Lossy KV Cache into Lossless LLM Inference</h2>
<p><a href="https://arxiv.org/abs/2605.17613v1">arXiv:2605.17613v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-28T12:00:14.444527+08:00 · 发表：2026-05-17T19:18:39Z · 修订：2026-05-17T19:18:39Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：VeriCache — 把 Lossy KV Cache 变成 Lossless LLM Inference。问题/方法/证据：提出一种**验证机制**，让 KV Cache 可以先 aggressive 压缩（lossy），然后在推理阶段通过 lightweight verification 恢复无损输出。换句话说，**内存省了，但输出质量不打折**。这是 KV Cache 优化从&quot;近似够用&quot;走向&quot;严格无损&quot;的关键一步。原报告标注日期：2026-05-17。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：长上下文 + 大 batch 场景下的 KV Cache 内存瓶颈是 2026 年 serving 系统的头号痛点。VeriCache 提供了一条新路径：不是靠更精细的量化算法，而是靠&quot;先压后验&quot;的架构思路。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>SAGA: Workflow-Atomic Scheduling for AI Agent Inference on GPU Clusters</h2>
<p><a href="https://arxiv.org/abs/2605.00528v2">arXiv:2605.00528v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-28T12:00:14.444527+08:00 · 发表：2026-05-01T09:05:28Z · 修订：2026-06-19T00:26:12Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：SAGA — Workflow-Atomic Scheduling for AI Agent Inference。问题/方法/证据：针对 AI Agent 多步骤推理（tool call → 等待 → 再推理）的**间歇性执行特征**，提出&quot;工作流原子调度&quot;——把 agent 的整个推理链条作为一个原子单元调度，而不是按单个 token generation 切片。显著降低上下文切换和 KV Cache 反复加载的开销。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：Agentic AI 的 serving 和传统 chat completion 完全不同。SAGA 是第一个把&quot;agent workflow&quot;作为一级调度对象的系统，预示 2026 下半年会有更多 agent-native serving infra 出现。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>DiP-SD: Distributed Pipelined Speculative Decoding for Efficient LLM Inference at the Edge</h2>
<p><a href="https://arxiv.org/abs/2604.20919v1">arXiv:2604.20919v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-28T12:00:14.444527+08:00 · 发表：2026-04-22T04:02:13Z · 修订：2026-04-22T04:02:13Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：DiP-SD — Distributed Pipelined Speculative Decoding for Edge Multi-User。问题/方法/证据：把**投机解码**扩展到边缘多用户场景。设备本地生成 draft tokens，offload 到云端验证。通过流水线并行隐藏网络延迟。原报告标注日期：2026-04-22。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：2026 年投机解码（EAGLE-3、MTP、Medusa）已经是 serving 标配，但主要集中在数据中心单集群。DiP-SD 把这条技术路线延伸到 edge-cloud 协作，对端侧推理生态意义重大。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>AIConfigurator: Lightning-Fast Configuration Optimization for Multi-Framework LLM Serving</h2>
<p><a href="https://arxiv.org/abs/2601.06288v1">arXiv:2601.06288v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-28T12:00:14.444527+08:00 · 发表：2026-01-09T20:03:57Z · 修订：2026-01-09T20:03:57Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：AIConfigurator — 集群级配置空间搜索。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate</h2>
<p><a href="https://arxiv.org/abs/2504.19874v1">arXiv:2504.19874v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-28T12:00:14.444527+08:00 · 发表：2025-04-28T15:05:35Z · 修订：2025-04-28T15:05:35Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：TurboQuant — 3 bit KV Cache Quantization。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Optimizing LLM Inference: Fluid-Guided Online Scheduling with Memory Constraints</h2>
<p><a href="https://arxiv.org/abs/2504.11320v4">arXiv:2504.11320v4 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-28T12:00:14.444527+08:00 · 发表：2025-04-15T16:00:21Z · 修订：2026-06-13T16:11:21Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：WAIT — Fluid Guided Online Scheduling。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Apt-Serve: Adaptive Request Scheduling on Hybrid Cache for Scalable LLM Inference Serving</h2>
<p><a href="https://arxiv.org/abs/2504.07494v1">arXiv:2504.07494v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-28T12:00:14.444527+08:00 · 发表：2025-04-10T06:51:23Z · 修订：2025-04-10T06:51:23Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Apt Serve — Adaptive Request Scheduling on Hybrid Cache。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Courant: a State-Adaptive Perceiver-Based Neural Surrogate with Local Support and Interpretable Field Decomposition</h2>
<p><a href="https://arxiv.org/abs/2605.25115v1">arXiv:2605.25115v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-19T16:47:54.619869+08:00 · 发表：2026-05-24T14:55:12Z · 修订：2026-05-24T14:55:12Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Courant。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Rational Communication Shapes Morphological Composition</h2>
<p><a href="https://arxiv.org/abs/2605.03510v1">arXiv:2605.03510v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-19T16:47:54.619869+08:00 · 发表：2026-05-05T08:44:23Z · 修订：2026-05-05T08:44:23Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：**MI-PINN** (arXiv:2605.03510, May 6) — Meta-Inverse Physics-Informed Neural Network。问题/方法/证据：将逆问题建模从joint optimization改写成two-stage meta-learning：先学跨任务的physics-aware representation，再固定representation只做task-specific逆推。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：逆问题（从观测推断参数/动力学）是SciML核心场景，但传统PINN做逆问题往往optimization困难、泛化差。MI-PINN通过降维搜索空间提升sample efficiency，还引入adaptive clustering-based multi-branch learning处理多尺度动力学。在33维耦合ODE的PBPK模型（药物动力学）上验证了准确恢复masked参数。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>A Physics-Informed Neural Network for Solving the Quasi-static Magnetohydrodynamic Equations</h2>
<p><a href="https://arxiv.org/abs/2604.20085v1">arXiv:2604.20085v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-19T16:47:54.619869+08:00 · 发表：2026-04-22T01:05:16Z · 修订：2026-04-22T01:05:16Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：**PINN for Tokamak MHD** (arXiv:2604.20085, Apr 22) — 托卡马克磁流体动力学。问题/方法/证据：首次用PINN无数据学习time-dependent quasi-static MHD方程，在ITER-like托卡马克几何中预测等离子体垂直位移事件。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：核聚变模拟是极其昂贵的多尺度 stiff PDE问题。PINN能作为fast surrogate替代传统MHD solver做参数扫描和实时状态估计，虽然还不是drop-in replacement，但proof-of-principle意义重大。论文也诚实暴露了numerical stiffness和boundary condition的挑战。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Physics-Informed Neural Networks for Solving Derivative-Constrained PDEs</h2>
<p><a href="https://arxiv.org/abs/2604.13723v1">arXiv:2604.13723v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-19T16:47:54.619869+08:00 · 发表：2026-04-15T10:57:22Z · 修订：2026-04-15T10:57:22Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：**DC-PINNs** (arXiv:2604.13723, Apr 15) — Derivative-Constrained PINNs。问题/方法/证据：把导数约束（bounds, monotonicity, convexity, incompressibility）显式嵌入PINN损失函数，用自适应损失平衡减少手工调参。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：传统PINN只约束PDE残差，但很多物理问题本质上要求导数层面的约束。DC-PINN在heat diffusion with bounds、金融volatility arbitrage-free约束、流体vortices shed等benchmark上稳定降低constraint violations，且能自动适应不同物理要求。这代表PINN从“近似满足物理”向“严格满足物理”的又一步。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Probing Intrinsic Medical Task Relationships: A Contrastive Learning Perspective</h2>
<p><a href="https://arxiv.org/abs/2604.05651v1">arXiv:2604.05651v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-19T16:47:54.619869+08:00 · 发表：2026-04-07T09:54:37Z · 修订：2026-04-07T09:54:37Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：**DDS-PINN** (arXiv:2604.05651, Apr 8) — Domain-Decomposed and Shifted PINN。问题/方法/证据：用localized networks + unified global loss解决多尺度流体中的长程依赖问题，实现无数据或少数据的Navier-Stokes求解。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：复杂流体（湍流、边界层分离）是PINN的硬伤，因为多尺度+长程依赖。DDS-PINN在backward-facing step（Re=100无数据求解，Re=10000仅用500个随机监督点&lt;0.3% domain）收敛到O(10^-4)， outperform Residual-based Attention-PINN。对湍流超分辨和稀疏实验测量→高保真重建有直接意义。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>A Machine Learning Approach to the Nirenberg Problem</h2>
<p><a href="https://arxiv.org/abs/2602.12368v1">arXiv:2602.12368v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-19T16:47:54.619869+08:00 · 发表：2026-02-12T19:58:11Z · 修订：2026-02-12T19:58:11Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Nirenberg Neural Network。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>naPINN: Noise-Adaptive Physics-Informed Neural Networks for Recovering Physics from Corrupted Measurement</h2>
<p><a href="https://arxiv.org/abs/2602.02547v2">arXiv:2602.02547v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-19T16:47:54.619869+08:00 · 发表：2026-01-30T06:03:33Z · 修订：2026-06-01T14:00:04Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：naPINN。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Discovering Scaling Exponents with Physics-Informed Müntz-Szász Networks</h2>
<p><a href="https://arxiv.org/abs/2601.22751v1">arXiv:2601.22751v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-19T16:47:54.619869+08:00 · 发表：2026-01-30T09:29:17Z · 修订：2026-01-30T09:29:17Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：MSN PINN。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Hard Constraint Projection in a Physics Informed Neural Network</h2>
<p><a href="https://arxiv.org/abs/2601.06244v1">arXiv:2601.06244v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-19T16:47:54.619869+08:00 · 发表：2026-01-09T18:30:58Z · 修订：2026-01-09T18:30:58Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Hard Constraint Projection PINN。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>From Alignment to Prediction: A Study of Self-Supervised Learning and Predictive Representation Learning</h2>
<p><a href="https://arxiv.org/abs/2604.13518v1">arXiv:2604.13518v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-07T09:18:05.727478+08:00 · 发表：2026-04-15T06:04:45Z · 修订：2026-04-15T06:04:45Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：From Alignment to Prediction — 预测式表示学习的新范式分类。问题/方法/证据：系统梳理自监督学习发展，首次提出 **Predictive Representation Learning (PRL)** 新类别——基于对数据未观测部分的潜在预测。将 JEPA 定位为 PRL 的典范代表，与对齐式（BYOL）和重建式（MAE）方法并列。实验对比显示：MAE 相似度完美(1.00)但鲁棒性弱(0.55)，BYOL 准确率 0.98/鲁棒性 0.75，I-JEPA 准确率 0.95/鲁棒性 0.78。原报告标注日期：2026-04-15。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>From Static to Dynamic: Exploring Self-supervised Image-to-Video Representation Transfer Learning</h2>
<p><a href="https://arxiv.org/abs/2603.26597v1">arXiv:2603.26597v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-07T09:18:05.727478+08:00 · 发表：2026-03-27T16:56:50Z · 修订：2026-03-27T16:56:50Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Co-Settle — 从静态到动态的自监督视频表示迁移 (CVPR 2026)。问题/方法/证据：探索自监督图像到视频表示迁移学习。从静态图像预训练模型出发，通过 Co-Settle 方法高效迁移到视频任务。在 DAVIS 视频目标分割、JHMDB 姿态传播、VIP 语义部件传播等密集级基准上验证。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Self-Distillation of Hidden Layers for Self-Supervised Representation Learning</h2>
<p><a href="https://arxiv.org/abs/2603.15553v2">arXiv:2603.15553v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-07T09:18:05.727478+08:00 · 发表：2026-03-16T17:13:27Z · 修订：2026-07-27T17:51:19Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Bootleg — 层次化自蒸馏突破 I-JEPA。问题/方法/证据：提出 Bootleg 方法，让模型预测教师网络多个隐藏层的潜在表示，而非仅最终层。这种层次化目标强制模型同时捕捉不同抽象层次的特征。在 ImageNet-1K 和 iNaturalist-21 分类任务上比 I-JEPA 提升 **+10%**，在 ADE20K 和 Cityscapes 语义分割上也显著优于基线。原报告标注日期：2026-03-16。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Learning Generalizable 3D Medical Image Representations from Mask-Guided Self-Supervision</h2>
<p><a href="https://arxiv.org/abs/2603.13660v1">arXiv:2603.13660v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-07T09:18:05.727478+08:00 · 发表：2026-03-14T00:06:18Z · 修订：2026-03-14T00:06:18Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：MASS — 无标注 3D 医学图像自监督 (CVPR 2026)。问题/方法/证据：斯坦福团队提出 MASS，首个面向 3D 医学图像（CT/MRI/PET）的 mask-guided 自监督框架。核心创新：用自动生成 mask 替代专家标注，将每个 mask 转化为密集分割任务，实现&quot;分割原生&quot;表示学习。收敛快、泛化强，支持训练-free 上下文分割、少样本微调和冻结编码器分类。已开源完整 pipeline。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Self-Supervised Representation Learning with Joint Embedding Predictive Architecture for Automotive LiDAR Object Detection</h2>
<p><a href="https://arxiv.org/abs/2501.04969v2">arXiv:2501.04969v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-06-07T09:18:05.727478+08:00 · 发表：2025-01-09T04:47:51Z · 修订：2025-10-07T02:07:45Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：AD-L-JEPA — 自动驾驶 LiDAR 的 JEPA 自监督 (AAAI 2026)。问题/方法/证据：首个将 JEPA 架构应用于自动驾驶 LiDAR 场景的自监督表示学习方法。通过联合嵌入预测架构学习 3D 点云表示，在 KITTI3D 上预训练后，SECOND 和 PV-RCNN 检测器均有显著提升。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>PALS: Power-Aware LLM Serving for Mixture-of-Experts Models</h2>
<p><a href="https://arxiv.org/abs/2605.21427v1">arXiv:2605.21427v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-31T09:18:07.541807+08:00 · 发表：2026-05-20T17:19:20Z · 修订：2026-05-20T17:19:20Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：PALS: Power-Aware LLM Serving for Mixture-of-Experts Models。问题/方法/证据：首次将功率预算作为MoE模型推理的**一级调度维度**，而非固定约束。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>InfiniLoRA: Disaggregated Multi-LoRA Serving for Large Language Models</h2>
<p><a href="https://arxiv.org/abs/2604.07173v1">arXiv:2604.07173v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-31T09:18:07.541807+08:00 · 发表：2026-04-08T15:01:04Z · 修订：2026-04-08T15:01:04Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：InfiniLoRA: Disaggregated Multi-LoRA Serving for Large Language Models。问题/方法/证据：多LoRA服务的**分离式架构**——每个LoRA独占一个轻量推理实例，共享底层基座模型的预填充阶段。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>DeepStack: Facilitating Co-Design Exploration of 3D DRAM-Stacked Accelerators for Distributed LLM Inference</h2>
<p><a href="https://arxiv.org/abs/2604.04750v4">arXiv:2604.04750v4 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-31T09:18:07.541807+08:00 · 发表：2026-04-06T15:16:35Z · 修订：2026-09-11T14:11:13Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：arXiv:2604.04750。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>TyphoonMLA: A Mixed Naive-Absorb MLA Kernel For Shared Prefix</h2>
<p><a href="https://arxiv.org/abs/2509.21081v2">arXiv:2509.21081v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-31T09:18:07.541807+08:00 · 发表：2025-09-25T12:32:02Z · 修订：2026-02-12T17:01:37Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：TyphoonMLA: A Mixed Naive-Absorb MLA Kernel for Shared Prefix。问题/方法/证据：DeepSeek-V3的MLA（Multi-head Latent Attention）的**共享前缀优化内核**，实现吸收模式和非压缩模式的混合调度。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>FineServe: Precision-Aware KV Slab and Two-Level Scheduling for Heterogeneous Precision LLM Serving</h2>
<p><a href="https://arxiv.org/abs/2509.06261v2">arXiv:2509.06261v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-31T09:18:07.541807+08:00 · 发表：2025-09-08T00:57:50Z · 修订：2025-09-15T00:51:47Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：arXiv:2509.06261。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Frontier: Simulating the Next Generation of LLM Inference Systems</h2>
<p><a href="https://arxiv.org/abs/2508.03148v1">arXiv:2508.03148v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-31T09:18:07.541807+08:00 · 发表：2025-08-05T06:53:28Z · 修订：2025-08-05T06:53:28Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：arXiv:2508.03148。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>LeMix: Unified Scheduling for LLM Training and Inference on Multi-GPU Systems</h2>
<p><a href="https://arxiv.org/abs/2507.21276v1">arXiv:2507.21276v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-31T09:18:07.541807+08:00 · 发表：2025-07-28T19:03:26Z · 修订：2025-07-28T19:03:26Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：LeMix: Unified Scheduling for LLM Training and Inference on Multi-GPU Systems。问题/方法/证据：让推理和训练**共享同一批GPU**，彻底消灭&quot;训练时推理闲置、推理时训练排队&quot;的资源浪费。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。</p>
<p>关联问题：机器人实际部署约束</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Oneiros: KV Cache Optimization through Parameter Remapping for Multi-tenant LLM Serving</h2>
<p><a href="https://arxiv.org/abs/2507.11507v2">arXiv:2507.11507v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-31T09:18:07.541807+08:00 · 发表：2025-07-15T17:23:22Z · 修订：2025-10-29T21:56:19Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：arXiv:2507.11507。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Nexus:Proactive Intra-GPU Disaggregation of Prefill and Decode in LLM Serving</h2>
<p><a href="https://arxiv.org/abs/2507.06608v5">arXiv:2507.06608v5 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-31T09:18:07.541807+08:00 · 发表：2025-07-09T07:27:18Z · 修订：2025-08-07T12:26:15Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Nexus: Proactive Intra-GPU Disaggregation of Prefill and Decode。问题/方法/证据：在**单个GPU内部**实现预填充/解码的主动分离，无需跨GPU、无需高端互联。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>ModServe: Modality- and Stage-Aware Resource Disaggregation for Scalable Multimodal Model Serving</h2>
<p><a href="https://arxiv.org/abs/2502.00937v3">arXiv:2502.00937v3 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-31T09:18:07.541807+08:00 · 发表：2025-02-02T22:10:40Z · 修订：2025-10-22T16:21:57Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：arXiv:2502.00937。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Demo-JEPA: Joint-Embedding Predictive Architecture for One-shot Cross-Embodiment Imitation</h2>
<p><a href="https://arxiv.org/abs/2605.20811v1">arXiv:2605.20811v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-05-20T07:05:49Z · 修订：2026-05-20T07:05:49Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Demo-JEPA — 跨具身模仿的 One-shot 利器。问题/方法/证据：将跨具身模仿问题建模为**隐空间目标条件规划**。给定源演示视频和目标当前观测，Dreamer Predictor 先推断出一个具身兼容的隐式目标，然后在动作条件化的世界模型中通过 CEM 优化完成 latent planning。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：One-shot 跨具身迁移 —— 这是 JEPA 架构在机器人控制中的又一次能力扩展，从表征学习走向实际策略生成。</p>
<p>关联问题：世界模型与可靠规划</p>
<p>标签：world-models、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>World-Ego Modeling for Long-Horizon Evolution in Hybrid Embodied Tasks</h2>
<p><a href="https://arxiv.org/abs/2605.19957v1">arXiv:2605.19957v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-05-19T15:10:27Z · 修订：2026-05-19T15:10:27Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：World-Ego Modeling — 长程混合具身任务的新思路。问题/方法/证据：提出 World-Ego 双视角建模 —— **World-view** 负责环境全局演化，**Ego-view** 负责第一人称行为理解。两者协同解决长程时序任务中的身份漂移和视角混乱问题。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：针对长程任务中的&quot;我是谁我在哪&quot;问题给出了架构级解法，在 VLN 和具身推理任务中有显著优势。</p>
<p>关联问题：人类视频与机器人数据需求</p>
<p>标签：world-models、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>From Imagined Futures to Executable Actions: Mixture of Latent Actions for Robot Manipulation</h2>
<p><a href="https://arxiv.org/abs/2605.12167v1">arXiv:2605.12167v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-05-12T14:15:16Z · 修订：2026-05-12T14:15:16Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：MoLA — 混合隐式动作的世界动作模型。问题/方法/证据：提出 Mixture of Latent Actions (MoLA)，在世界动作模型（WAM）中引入**多个预训练逆动力学模型（IDM）作为隐动作接口**，桥接想象的未来视频与可执行动作。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：解决 WAM &quot;想得好看但做不出来&quot;的问题，用 mixture 机制增强动作解码的灵活性。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Latent State Design for World Models under Sufficiency Constraints</h2>
<p><a href="https://arxiv.org/abs/2605.01694v1">arXiv:2605.01694v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-05-03T03:19:42Z · 修订：2026-05-03T03:19:42Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Latent State Design for World Models。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>World Model for Robot Learning: A Comprehensive Survey</h2>
<p><a href="https://arxiv.org/abs/2605.00080v1">arXiv:2605.00080v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-04-30T14:35:31Z · 修订：2026-04-30T14:35:31Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：World Model for Robot Learning — 最全面的综述。问题/方法/证据：首次对世界模型在机器人学习中的角色做了**全景式系统分类**，提出三大核心能力框架局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：想快速了解这个领域全貌？这篇是目前的最佳入口。</p>
<p>关联问题：世界模型与可靠规划</p>
<p>标签：world-models、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training</h2>
<p><a href="https://arxiv.org/abs/2604.21741v2">arXiv:2604.21741v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-04-23T14:42:54Z · 修订：2026-05-05T16:01:35Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Human in the World Model (arXiv:2604.21741)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：人类视频与机器人数据需求</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Human Cognition in Machines: A Unified Perspective of World Models</h2>
<p><a href="https://arxiv.org/abs/2604.16592v2">arXiv:2604.16592v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-04-17T17:51:46Z · 修订：2026-06-15T02:33:48Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Human Cognition in Machines。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：人类视频与机器人数据需求</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>The Global Neural World Model: Spatially Grounded Discrete Topologies for Action-Conditioned Planning</h2>
<p><a href="https://arxiv.org/abs/2604.16585v1">arXiv:2604.16585v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-04-17T15:12:15Z · 修订：2026-04-17T15:12:15Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：GNWM (arXiv:2604.16585)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>World Reasoning Arena</h2>
<p><a href="https://arxiv.org/abs/2603.25887v1">arXiv:2603.25887v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-03-26T20:22:52Z · 修订：2026-03-26T20:22:52Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：World Reasoning Arena。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：人类视频与机器人数据需求</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Fast-WAM: Do World Action Models Need Test-time Future Imagination?</h2>
<p><a href="https://arxiv.org/abs/2603.16666v2">arXiv:2603.16666v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-03-17T15:33:43Z · 修订：2026-03-23T05:41:14Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Fast WAM。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>World Guidance: World Modeling in Condition Space for Action Generation</h2>
<p><a href="https://arxiv.org/abs/2602.22010v1">arXiv:2602.22010v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-02-25T15:27:09Z · 修订：2026-02-25T15:27:09Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：World Guidance (arXiv:2602.22010)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>FRAPPE: Infusing World Modeling into Generalist Policies via Multiple Future Representation Alignment</h2>
<p><a href="https://arxiv.org/abs/2602.17259v1">arXiv:2602.17259v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-02-19T11:00:46Z · 修订：2026-02-19T11:00:46Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：FRAPPE (arXiv:2602.17259)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL</h2>
<p><a href="https://arxiv.org/abs/2602.13977v2">arXiv:2602.13977v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-02-15T03:48:20Z · 修订：2026-06-27T16:11:05Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：WoVR。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model</h2>
<p><a href="https://arxiv.org/abs/2602.10098v2">arXiv:2602.10098v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-02-10T18:58:01Z · 修订：2026-02-14T03:00:50Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：VLA JEPA。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>BagelVLA: Enhancing Long-Horizon Manipulation via Interleaved Vision-Language-Action Generation</h2>
<p><a href="https://arxiv.org/abs/2602.09849v2">arXiv:2602.09849v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-02-10T14:54:01Z · 修订：2026-02-11T03:54:17Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：BagelVLA (arXiv:2602.09849)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>A Lightweight Library for Energy-Based Joint-Embedding Predictive Architectures</h2>
<p><a href="https://arxiv.org/abs/2602.03604v3">arXiv:2602.03604v3 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-02-03T14:56:24Z · 修订：2026-04-08T15:27:24Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：EB JEPA。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning</h2>
<p><a href="https://arxiv.org/abs/2601.16163v1">arXiv:2601.16163v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-01-22T18:09:30Z · 修订：2026-01-22T18:09:30Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Cosmos Policy。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Akasha 2: Hamiltonian State Space Duality and Visual-Language Joint Embedding Predictive Architectur</h2>
<p><a href="https://arxiv.org/abs/2601.06212v2">arXiv:2601.06212v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2026-01-08T18:40:31Z · 修订：2026-06-13T06:59:14Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Akasha 2 (arXiv:2601.06212)。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?</h2>
<p><a href="https://arxiv.org/abs/2512.24497v3">arXiv:2512.24497v3 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2025-12-30T22:50:03Z · 修订：2026-05-18T09:26:59Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：What Drives Success in Physical Planning with JEPA-WMs — JEPA 世界模型的配方书。问题/方法/证据：系统性拆解 JEPA-World Model 在物理规划任务中成功的关键设计选择，覆盖局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：这不是一篇新算法论文，而是一份**工程配方书** —— 如果你在做 JEPA 机器人规划，这篇能帮你少踩很多坑。</p>
<p>关联问题：世界模型与可靠规划</p>
<p>标签：world-models、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Object-Centric World Models for Causality-Aware Reinforcement Learning</h2>
<p><a href="https://arxiv.org/abs/2511.14262v3">arXiv:2511.14262v3 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-24T09:18:21.729512+08:00 · 发表：2025-11-18T08:53:09Z · 修订：2026-03-30T07:20:18Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：STICA。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>A QPINN Framework with Quantum Trainable Embeddings for the Lid-Driven Cavity Problem</h2>
<p><a href="https://arxiv.org/abs/2605.13892v1">arXiv:2605.13892v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-17T09:17:54.300157+08:00 · 发表：2026-05-12T10:03:45Z · 修订：2026-05-12T10:03:45Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Quantum Physics-Informed Neural Networks (QPINN)。问题/方法/证据：arXiv:2605.13892 | 2026 05 12 一句话 : 用量子可训练嵌入层增强 PINN，解决 Lid Driven Cavity 问题。 核心亮点 : 将量子可训练嵌入（Quantum Trainable Embeddings）引入物理约束学习 为量子计算与科学计算的交叉开辟了试验场 延续了 Karniadakis 团队在 PINN 方向的持续创新 为什么重要 : 不是实用突破，而是一个值得追踪的信号——量子增强的科学计算是否只是噱头，还是真的有优势？原报告标注日期：2026-05-12。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：不是实用突破，而是一个值得追踪的信号——量子增强的科学计算是否只是噱头，还是真的有优势？</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Physics-Informed Neural Networks: A Didactic Derivation of the Complete Training Cycle</h2>
<p><a href="https://arxiv.org/abs/2604.18481v1">arXiv:2604.18481v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-17T09:17:54.300157+08:00 · 发表：2026-04-20T16:34:47Z · 修订：2026-04-20T16:34:47Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：&quot;Physics Informed Neural Networks: A Didactic Derivation of the Complete Training Cycle&quot;。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Lattice-Boltzmann-Driven Physics-Informed Neural Networks for Droplet Wettability on Rough Surfaces</h2>
<p><a href="https://arxiv.org/abs/2604.03481v2">arXiv:2604.03481v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-17T09:17:54.300157+08:00 · 发表：2026-04-03T22:02:30Z · 修订：2026-04-20T05:21:11Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：K-PINN: Lattice-Boltzmann-Driven Physics-Informed Neural Networks。问题/方法/证据：arXiv:2604.03481 | 2026 04 03 一句话 : 把介观尺度的 Lattice Boltzmann 方程直接嵌入 PINN，突破了传统 PINN 只能处理宏观连续方程的限制。 核心亮点 : 在介观动力学层面保持物理一致性，质量守恒误差 &lt; 1.5% 成功建模接触钉扎、各向异性铺展、毛细滞后等复杂液滴现象 U Net 编码器 解码器结构使误差相比传统神经网络降低 50 75% 收敛后实时预测速度 10⁴ 次/秒 为什么重要 : 这是 PINN 从&quot;宏观唯象&quot;走向&quot;介观机理&quot;的关键一步，对多相流、润湿性工程有直接影响。原报告标注日期：2026-04-03。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：这是 PINN 从&quot;宏观唯象&quot;走向&quot;介观机理&quot;的关键一步，对多相流、润湿性工程有直接影响。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Physics-Informed Laplace Neural Operator for Solving Partial Differential Equations</h2>
<p><a href="https://arxiv.org/abs/2602.12706v2">arXiv:2602.12706v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-17T09:17:54.300157+08:00 · 发表：2026-02-13T08:19:40Z · 修订：2026-08-13T07:35:14Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：Physics Informed Laplace Neural Operator。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>LUT-KAN: Segment-wise LUT Quantization for Fast KAN Inference</h2>
<p><a href="https://arxiv.org/abs/2601.03332v1">arXiv:2601.03332v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-17T09:17:54.300157+08:00 · 发表：2026-01-06T18:00:45Z · 修订：2026-01-06T18:00:45Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：LUT KAN。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Multi-Resolution Training-Enhanced Kolmogorov-Arnold Networks for Multi-Scale PDE Problems</h2>
<p><a href="https://arxiv.org/abs/2507.19888v1">arXiv:2507.19888v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-17T09:17:54.300157+08:00 · 发表：2025-07-26T09:36:18Z · 修订：2025-07-26T09:36:18Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：LegendKINN。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Discontinuity-aware KAN-based physics-informed neural networks</h2>
<p><a href="https://arxiv.org/abs/2507.08338v2">arXiv:2507.08338v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-17T09:17:54.300157+08:00 · 发表：2025-07-11T06:37:16Z · 修订：2026-03-24T07:52:54Z</p>
<p><strong>自动摘要：</strong>历史周报 PIKAN 方向列出的另一篇论文，原 JSON 转换遗漏；尚未核对全文，不推断具体贡献或实验结果。</p>
<p><strong>推荐理由（工具判断）：</strong>原周报趋势部分已列出此 ID，补回原文收录清单。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Kolmogorov-Arnold Fourier Networks</h2>
<p><a href="https://arxiv.org/abs/2502.06018v3">arXiv:2502.06018v3 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-17T09:17:54.300157+08:00 · 发表：2025-02-09T20:21:43Z · 修订：2026-05-24T16:33:35Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：PIKAN。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：physics-informed-ai、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Stability and Generalization in Looped Transformers</h2>
<p><a href="https://arxiv.org/abs/2604.15259v2">arXiv:2604.15259v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-10T11:33:09.300662+08:00 · 发表：2026-04-16T17:35:49Z · 修订：2026-04-22T15:48:32Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：2。问题/方法/证据：提出fixed-point based framework分析looped transformers的三个稳定性轴：reachability（可达性）、input-dependence（输入依赖性）、geometry（几何稳定性）原报告标注日期：2026-04-16。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Mamba-3: Improved Sequence Modeling using State Space Principles</h2>
<p><a href="https://arxiv.org/abs/2603.15569v1">arXiv:2603.15569v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-10T11:33:09.300662+08:00 · 发表：2026-03-16T17:30:08Z · 修订：2026-03-16T17:30:08Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：1。问题/方法/证据：来源 : arXiv:2603.15569 ICLR 2026 Oral 作者 : Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, Albert Gu 关键词 : State Space Models, linear time sequence modeling, inference efficiency 核心看点 : 从inference first视角出发，提出三大改进： 1 更expressive的recurrence（基于SSM discretization）； 2 complex valued state update rule，实现richer state tracking； 3 MIMO mul局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：Mamba系列是Transformer替代路线的核心竞争者，Mamba-3被ICLR 2026接收为Oral，标志着SSM范式进入主流视野。complex-valued state update的引入尤其值得关注——这在数学上更接近生物神经系统的振荡动力学</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Compiler-First State Space Duality and Portable $O(1)$ Autoregressive Caching for Inference</h2>
<p><a href="https://arxiv.org/abs/2603.09555v2">arXiv:2603.09555v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-10T11:33:09.300662+08:00 · 发表：2026-03-10T12:03:00Z · 修订：2026-06-09T21:08:13Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：2。问题/方法/证据：从compiler-first角度重新思考SSM的inference优化原报告标注日期：2026-03-10。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>The Geometry of Multi-Task Grokking: Transverse Instability, Superposition, and Weight Decay Phase Structure</h2>
<p><a href="https://arxiv.org/abs/2602.18523v3">arXiv:2602.18523v3 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-10T11:33:09.300662+08:00 · 发表：2026-02-19T22:39:55Z · 修订：2026-04-03T01:46:22Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：2。问题/方法/证据：研究grokking现象中的phase transition结构原报告标注日期：2026-03-14。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Noise Stability of Transformer Models</h2>
<p><a href="https://arxiv.org/abs/2602.08287v1">arXiv:2602.08287v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-05-10T11:33:09.300662+08:00 · 发表：2026-02-09T05:43:22Z · 修订：2026-02-09T05:43:22Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：2。问题/方法/证据：提出**noise stability**作为衡量深度学习simplicity bias的新指标，替代传统的average sensitivity原报告标注日期：2026-02-09。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：为&quot;为什么过参数化模型能泛化&quot;提供了新的理论视角，且实际可用作regularizer</p>
<p>关联问题：其他关注方向</p>
<p>标签：deep-learning、legacy-report · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Distributed Hybrid Parallelism for Large Language Models: Comparative Study and System Design Guide</h2>
<p><a href="https://arxiv.org/abs/2602.09109v1">arXiv:2602.09109v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-04-26T13:23:00.602643+08:00 · 发表：2026-02-09T19:01:13Z · 修订：2026-02-09T19:01:13Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Distributed Hybrid Parallelism for Large Language Models。问题/方法/证据：系统梳理分布式LLM训练/推理的混合并行策略——数据并行(DP)、张量并行(TP)、流水线并行(PP)、序列并行(SP)、专家并行(EP)，给出每种策略的通信模式、内存占用和适用场景的数学建模原报告标注日期：2026。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：想做分布式训练infra的人，这篇是地图级参考</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、分布式训练、并行策略、综述、llm · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Throughput-Optimal Scheduling Algorithms for LLM Inference and AI Agents</h2>
<p><a href="https://arxiv.org/abs/2504.07347v3">arXiv:2504.07347v3 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-04-26T13:23:00.602643+08:00 · 发表：2025-04-10T00:12:12Z · 修订：2026-05-18T01:04:46Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：Optimal Scheduling Algorithms for LLM Inference。问题/方法/证据：从排队论角度建立LLM推理调度的严格理论框架，提出SLAI调度器——动态平衡prefill/decode阶段，在严格TBT延迟约束下实现吞吐量最优；高负载下TTFT降低53%，服务容量提升26%原报告标注日期：2025。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：AI Infra的&quot;根论文&quot;级工作——把LLM推理调度从经验工程推进到理论可证的阶段</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、调度理论、llm推理、slo保证、排队论 · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>CacheGen: KV Cache Compression and Streaming for Fast Large Language Model Serving</h2>
<p><a href="https://arxiv.org/abs/2310.07240v6">arXiv:2310.07240v6 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-04-26T13:23:00.602643+08:00 · 发表：2023-10-11T07:08:20Z · 修订：2024-07-19T21:04:14Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：CacheGen: KV Cache Compression and Streaming for Fast LLM Serving。问题/方法/证据：提出KV Cache的压缩+流式传输方案，将KV tensor压缩后按需流式加载，大幅降低多轮对话和多副本部署的内存压力原报告标注日期：2024。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：KV Cache管理是推理infra的核心子问题，这篇和vLLM、SGLang、FlashInfer共同构成技术栈</p>
<p>关联问题：其他关注方向</p>
<p>标签：ai-infra、legacy-report、kvcache、压缩、推理优化 · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>World Action Models are Zero-shot Policies</h2>
<p><a href="https://arxiv.org/abs/2602.15922v1">arXiv:2602.15922v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-04-23T19:37:47.339891+08:00 · 发表：2026-02-17T15:04:02Z · 修订：2026-02-17T15:04:02Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：[arXiv]( ⭐⭐⭐⭐ 世界模型 强化学习 零样本。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Self-Supervised JEPA-based World Models for LiDAR Occupancy Completion and Forecasting</h2>
<p><a href="https://arxiv.org/abs/2602.12540v1">arXiv:2602.12540v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-04-23T19:37:47.339891+08:00 · 发表：2026-02-13T02:42:21Z · 修订：2026-02-13T02:42:21Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：[arXiv]( ⭐⭐⭐ JEPA 自动驾驶 LiDAR。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Causal-JEPA: Learning World Models through Object-Level Latent Masking</h2>
<p><a href="https://arxiv.org/abs/2602.11389v2">arXiv:2602.11389v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-04-23T19:37:47.339891+08:00 · 发表：2026-02-11T21:47:26Z · 修订：2026-05-28T17:57:16Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：[arXiv]( ⭐⭐⭐⭐ JEPA 因果推断 物体中心。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Koopman Invariants as Drivers of Emergent Time-Series Clustering in Joint-Embedding Predictive Architectures</h2>
<p><a href="https://arxiv.org/abs/2511.09783v2">arXiv:2511.09783v2 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-04-23T19:37:47.339891+08:00 · 发表：2025-11-12T22:33:56Z · 修订：2026-01-23T13:40:42Z</p>
<p><strong>自动摘要：</strong>历史周报其他关注条目：[arXiv]( ⭐⭐⭐⭐ JEPA 理论 动力系统。问题/方法/证据/局限：原历史报告未提供可机读拆分，详见同名 Markdown。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>历史报告列入“其他值得一看/值得关注”或机器摘要区块；本次转换未重新筛选。</p>
<p>关联问题：其他关注方向</p>
<p>标签：world-models、legacy-report、other-mention · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning</h2>
<p><a href="https://arxiv.org/abs/2506.09985v1">arXiv:2506.09985v1 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-04-23T19:37:47.339891+08:00 · 发表：2025-06-11T17:57:09Z · 修订：2025-06-11T17:57:09Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：2。问题/方法/证据：百万小时互联网视频自监督预训练 → 62小时机器人数据微调 → 零样本在真实Franka机械臂执行抓取/放置，无需任务训练/奖励/环境数据原报告标注日期：2025。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。 原推荐理由：杨立昆路线 + 因果性，解决JEPA&quot;知其然不知其所以然&quot;的问题</p>
<p>关联问题：世界模型与可靠规划、机器人实际部署约束</p>
<p>标签：world-models、legacy-report、jepa、杨立昆、机器人、因果推断、物体中心、世界模型、强化学习 · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>

<article>
<h2>Understanding World or Predicting Future? A Comprehensive Survey of World Models</h2>
<p><a href="https://arxiv.org/abs/2411.14499v4">arXiv:2411.14499v4 · 查看原文</a></p>
<p>历史扫描时间估计（报告文件修改时间）：2026-04-23T19:37:47.339891+08:00 · 发表：2024-11-21T03:58:50Z · 修订：2025-12-10T02:53:14Z</p>
<p><strong>自动摘要：</strong>历史周报补处理条目：1。问题/方法/证据：首次系统分类世界模型文献为「理解世界」vs「预测未来」两大范式，覆盖生成游戏/自动驾驶/机器人/社会仿真四大领域原报告标注日期：2025。局限：原历史报告未单列，本次未重新核对全文。实际阅读范围：基于既有周报摘要转换，未在本次重新核对全文。</p>
<p><strong>推荐理由（工具判断）：</strong>既有周报主推荐条目；本次仅做历史格式转换，未重新筛选。</p>
<p>关联问题：世界模型与可靠规划</p>
<p>标签：world-models、legacy-report、综述、世界模型、agi · 生成者：OpenClaw paper-radar legacy weekly processor (kimi/k2d8-preview)</p>
</article>
