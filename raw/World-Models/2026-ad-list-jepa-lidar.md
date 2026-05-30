## Self-Supervised JEPA-based World Models for LiDAR Occupancy Completion and Forecasting (AD-LiST-JEPA)

- **作者**: Haoran Zhu, Anna Choromanska (纽约大学, NYU)
- **年份**: 2026
- **来源**: arXiv:2602.12540v1
- **链接**: https://arxiv.org/abs/2602.12540
- **引用数**: 尚新，但其前作 AD-L-JEPA (2025 AAAI) 已有引用积累
- **关键词标签**: #JEPA #自动驾驶 #LiDAR #世界模型 #自监督学习 #占用预测 #纽约大学

---

### 核心贡献（一句话）
> 将杨立昆的JEPA架构首次应用于自动驾驶LiDAR数据，提出AD-LiST-JEPA——自监督学习3D世界的时空演化，并通过「占用补全与预测(OCF)」下游任务验证其感知+预测联合能力。

---

### 解决了什么问题

1. **自动驾驶需要世界模型**: 物理世界中运行的Agent（自动驾驶车）必须理解环境如何时空演化，才能做长期规划
2. **标注成本极高**: LiDAR数据的3D标注昂贵且耗时，自监督是规模化唯一路径
3. **JEPA在视觉/视频上成功了，LiDAR行吗？**: 这是JEPA从2D/视频向3D稀疏点云的首次系统性迁移
4. **怎么评估世界模型好坏？**: 提出用OCF（Occupancy Completion and Forecasting）作为联合评估感知+预测的下游任务

---

### 方法概述

**两阶段Pipeline**:

1. **Phase 1: JEPA自监督预训练**
   - 数据：Waymo数据集LiDAR序列（稀疏点云）
   - 架构：AD-LiST-JEPA（LiDAR SpatioTemporal JEPA）
   - 方法：在BEV（鸟瞰图）/3D体素空间中，用JEPA预测未来帧的嵌入表示（非像素/非点云重建）
   - 训练：30 epochs，8×A100，batch size 32
   - 正则化对比：Variance Regularization vs SIGReg（后者胜出）

2. **Phase 2: OCF下游微调**
   - 任务：给定过去5帧稀疏LiDAR输入，预测未来5帧的占用补全标签
   - 设置：单A100，3 epochs，恒定学习率
   - 评估指标：IoU_full（全范围） vs IoU_close（近场范围）

---

### 关键结果

| 配置 | IoU_full | IoU_close | 结论 |
|------|----------|-----------|------|
| 从头训练 (Scratch) | baseline | baseline | — |
| Variance Regularization 预训练 | 提升 | 提升 | JEPA预训练有效 |
| **SIGReg 预训练** | **更显著提升** | **更显著提升** | **SIGReg > Variance Reg** |

- **核心发现**: 使用JEPA预训练后的编码器，在OCF任务上显著优于从头训练
- **效率**: 延续了AD-L-JEPA的优良传统——相比Occupancy-MAE，GPU hours减少1.9-2.7×，GPU内存减少2.8-4×
- **数据集规模**: Small（190序列）和Large（950序列）预训练均有效，证明数据效率

---

### 局限性
- **作者自述**:
  - Proof of concept级别——网络架构相对简单，仅用于验证JEPA预训练对OCF的有效性
  - 未在完整的端到端自动驾驶pipeline中验证（仅做了感知/预测模块）
  - 只在Waymo一个数据集上实验
- **我发现的**:
  - 这是「前作follow-up」而非独立突破——AD-L-JEPA (2025 AAAI) 已经证明了JEPA对LiDAR检测有效，这篇只是把下游任务从「检测」换成了「占用预测+补全」
  - 与V-JEPA 2的机器人规划相比，这篇的「世界模型」尚未用于决策/控制闭环
  - SIGReg胜出 variance regularization，但为什么？论文解释不够深入，只说"promising direction"
  - 没有与生成式世界模型（如GAIA-1、World4Drive等）做直接对比

---

### 与我已有知识的关联
- **相关论文**:
  - **AD-L-JEPA (Zhu et al., 2025, AAAI)** — 前作，首次将JEPA用于LiDAR 3D检测，这篇是其时空扩展
  - **V-JEPA 2 (2025)** — JEPA路线的另一个分支（视频→机器人），两者形成「JEPA横向扩展」矩阵
  - **DINO-WM (Zhou et al., 2024)** — 也在做world model on visual features，但用DINOv2而非JEPA
  - **World4Drive (Zheng et al., 2025, ICCV)** — 生成式自动驾驶世界模型，与JEPA路线形成对比
- **共识/冲突**:
  - **共识**: 自动驾驶确实需要世界模型，自监督预训练是必经之路
  - **冲突**: 这篇走「非生成式」JEPA路线，而业界主流（GAIA-1、Waymo、特斯拉）更倾向生成式世界模型。JEPA在LiDAR上的优势是否足以对抗生成路线的直观可视化能力？未可知

---

### 阅读状态
- [x] 已读Abstract+Conclusion
- [x] 已理清架构 (两阶段Pipeline清晰)
- [x] 已聚焦关键细节 (SIGReg vs Variance, OCF任务定义)
- [ ] 已整合到领域笔记 (待与AD-L-JEPA、V-JEPA 2整合为「JEPA×自动驾驶」子领域)

---

### 兴趣评级
⭐⭐⭐ — 有价值的领域扩展验证，但属于「follow-up」性质，突破性不如V-JEPA 2或C-JEPA

---

### 队长批注
这篇论文的定位是「JEPA横向扩展」——证明JEPA不只能做视频和机器人，还能做自动驾驶LiDAR。但它更像是AD-L-JEPA的自然延伸，而非独立突破。对于你的论文追踪来说，它验证了JEPA的通用性，但如果时间有限，优先级可以放在V-JEPA 2、C-JEPA、LeJEPA之后。适合作为「领域地图填充」而非「精读核心」。
