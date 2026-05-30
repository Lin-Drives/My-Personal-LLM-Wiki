## Understanding World or Predicting Future? A Comprehensive Survey of World Models

- **作者**: Jingtao Ding, Yunke Zhang, Yu Shang, Jie Feng 等 (共15人，多机构)
- **年份**: 2025
- **来源**: ACM Computing Surveys, Vol 58(3), pp.1-38
- **链接**: https://arxiv.org/abs/2411.14499
- **引用数**: 高 (顶刊综述，被多篇2025-2026论文引用)
- **关键词标签**: #世界模型 #综述 #AGI #杨立昆JEPA #自动驾驶 #机器人 #生成游戏

---

### 核心贡献（一句话）
> 首次系统地将世界模型文献按「理解世界」和「预测未来」两大功能分类，并梳理了在生成游戏、自动驾驶、机器人、社会仿真四大领域的应用，为研究者提供了完整领域地图。

---

### 解决了什么问题

世界模型这个概念在GPT-4、Sora之后火得不行，但文献分散在各个领域（RL、CV、NLP、机器人），缺乏统一视角。这篇综述把散落的珠子串起来了。

---

### 方法概述

**两大功能分类**:
1. **Understanding (理解世界)** — 构建内部表征来理解世界机制
   - 例子：JEPA系列学习物理规律、直观物理理解
2. **Prediction (预测未来)** — 预测未来状态以模拟和指导决策
   - 例子：Dreamer、Sora类视频生成模型、驾驶场景预测

**四大应用领域**:
- 生成游戏 (Generative Games)
- 自动驾驶 (Autonomous Driving)
- 机器人 (Robotics)
- 社会仿真 (Social Simulacra)

---

### 关键结果

- 整理了世界模型从2018 (Ha & Schmidhuber "World Models") 到2024+ 的完整演进脉络
- 明确指出了当前两条路线：**认知派** (JEPA，预测抽象表征) vs **生成派** (Diffusion/AR，预测像素)
- 总结了代表性论文及代码仓库 (GitHub链接)

---

### 局限性
- **作者自述**: 世界模型定义本身仍模糊，不同社区理解不同；部分新兴方向（如LLM as World Model）边界不清
- **我发现的**:
  - 对JEPA路线的技术细节展开不足（毕竟要覆盖全领域，单篇展开有限）
  - 引用截止2024年中，V-JEPA 2 (2025年6月) 和 LeJEPA (2025年11月) 未覆盖
  - 物理AI/科学计算方向的世界模型涉及较少

---

### 与我已有知识的关联
- **相关论文**: LeCun 2022 "A Path Towards Autonomous Machine Intelligence" — 这篇综述把LeCun的JEPA vision放入了更大的世界模型图景
- **共识/冲突**: 综述本身是中立的，但隐含的冲突是「认知派」vs「生成派」的路线之争——杨立昆坚持不生成像素、只预测表征，而业界主流（Sora、Diffusion）走生成路线

---

### 阅读状态
- [x] 已读Abstract+Conclusion
- [x] 已理清架构
- [ ] 已聚焦关键细节
- [ ] 已整合到领域笔记

---

### 兴趣评级
⭐⭐⭐⭐⭐ — 世界模型入门必读，建立领域地图的核心参考文献

---

### 队长批注
这篇综述是完美的「起点论文」——读完它，你知道世界模型领域有哪些山头、哪些路线、谁在做什么。接下来细分方向时再深入JEPA系列或Diffusion World Model。建议作为领域知识库的Anchor Paper。
