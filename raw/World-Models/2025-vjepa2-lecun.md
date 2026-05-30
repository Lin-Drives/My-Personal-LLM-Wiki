## V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

- **作者**: Mido Assran, Adrien Bardes, David Fan, Quentin Garrido, Russell Howes, Mojtaba Komeili, Matthew Muckley, Ammar Rizvi, Claire Roberts, Koustuv Sinha, Artem Zholus, Sergio Arnaud, Abha Gejji, Ada Martin, Francois Robert Hogan, Daniel Dugas, Piotr Bojanowski, Vasil Khalidov, Patrick Labatut, Francisco Massa, Marc Szafraniec, Kapil Krishnakumar, Yong Li, Xiaodong Ma, Sarath Chandar, Franziska Meier, **Yann LeCun**, Michael Rabbat, Nicolas Ballas
- **年份**: 2025
- **来源**: arXiv:2506.09985 / CVPR 2025
- **链接**: https://arxiv.org/abs/2506.09985
- **引用数**: 快速上升中 (2025年6月发布，已被多篇后续论文引用)
- **关键词标签**: #世界模型 #JEPA #杨立昆 #自监督学习 #视频理解 #机器人规划 #MetaFAIR

---

### 核心贡献（一句话）
> 证明了仅通过百万小时互联网视频自监督预训练 + 62小时无标注机器人视频微调，就能得到一个能理解视频、预测未来、并零样本在真实机械臂上执行物体抓取/放置任务的世界模型——无需任务特定训练、无需奖励函数、无需目标环境数据。

---

### 解决了什么问题

杨立昆一直批评LLM和生成式AI「不懂物理世界」。这篇论文是他的实证回应：
- **问题1**: 如何让AI像婴儿一样，主要通过观察（看）而不是手把手教（标注/奖励）来学习世界？
- **问题2**: 纯视觉自监督能不能支撑机器人规划，而不需要昂贵的任务特定数据？
- **问题3**: 生成的世界模型（预测像素）vs 预测表征的世界模型，哪个更适合物理世界？

---

### 方法概述

**三步Pipeline**:

1. **预训练 V-JEPA 2 (Action-Free)**
   - 数据：100万小时互联网视频 + 图像
   - 方法：Joint-Embedding Predictive Architecture (JEPA)
   - 关键：不重建像素，只预测视频帧在表征空间(latent space)的嵌入
   - 输出：能懂视频、预测动作后果的视觉表征

2. **对齐 LLM (V-JEPA 2 + LLM)**
   - 将视觉表征与语言模型对齐
   - 成果：8B参数规模下，视频问答达到SOTA (PerceptionTest 84.0, TempCompass 76.9)

3. **后训练 V-JEPA 2-AC (Action-Conditioned)**
   - 数据：< 62小时无标注机器人视频 (Droid数据集)
   - 方法：在latent space学习动作条件的世界模型
   - 部署：零样本(zero-shot)在**两个不同实验室的Franka机械臂**上执行pick-and-place
   - 关键：没在这些实验室采过数据，没任务训练，没奖励函数

---

### 关键结果

| 任务 | 结果 | 对比 |
|------|------|------|
| Something-Something v2 动作理解 | 77.3 top-1 accuracy | 超越此前task-specific模型 |
| Epic-Kitchens-100 动作预测 | 39.7 recall-at-5 | **SOTA** |
| PerceptionTest 视频问答 | 84.0 | 8B规模 **SOTA** |
| TempCompass 时间理解 | 76.9 | 8B规模 **SOTA** |
| Franka机械臂零样本规划 | 成功pick-and-place | 无需环境数据、无需奖励 |

---

### 局限性
- **作者自述**:
  - 仅展示了简单操作任务（pick-and-place），复杂长程规划未验证
  - 机器人数据虽少但仍是特定数据集(Droid)，通用性有待更多验证
  - 动作空间是离散的图像目标（image goals），连续控制未充分探索
- **我发现的**:
  - 100万小时视频的计算成本极高，复现门槛高（工业级实验室才能做）
  - 论文对比 baseline 时，部分baseline被剥夺了奖励标注（公平但现实中不常见）
  - JEPA的latent space可解释性未深入——模型"理解"了什么物理规律？难以验证
  - 未与其他世界模型路线（如RSSM/Dreamer、Diffusion World Model）做全面对比

---

### 与我已有知识的关联
- **相关论文**:
  - I-JEPA (2023, CVPR) — 图像版JEPA
  - V-JEPA (2024) — 视频版JEPA前身
  - LeJEPA (2025) — JEPA的理论证明
  - "A Path Towards Autonomous Machine Intelligence" (LeCun 2022) — 这篇是上述vision的实证落地
- **共识/冲突**:
  - **共识**: 自监督预训练 + 少量微调是高效范式
  - **冲突**: 业界主流（OpenAI/Google）押注生成式/自回归路线，杨立昆坚持「非生成」路线。这篇论文是Meta FAIR在机器人场景下对LLM路线的一次「绕过」——证明不用LLM也能做物理规划

---

### 阅读状态
- [x] 已读Abstract+Conclusion
- [x] 已理清架构 (三步Pipeline清晰)
- [x] 已聚焦关键细节 (latent action-conditioned world model + 零样本部署)
- [ ] 已整合到领域笔记 (待与I-JEPA、V-JEPA、LeJEPA整合为JEPA系列笔记)

---

### 兴趣评级
⭐⭐⭐⭐⭐ — 杨立昆团队世界模型的最新代表作，JEPA路线从理论到机器人落地的关键论文

---

### 队长批注
这篇论文是JEPA路线的「集大成者」——从纯视觉自监督 → 视频理解 → 语言对齐 → 机器人规划，串成了一条完整的证据链。对于你的论文追踪目标来说，它是必读的Anchor Paper。但要注意：它的成功建立在Meta级别的算力之上，个人研究者难以复现，重点学习其方法论而非工程细节。
