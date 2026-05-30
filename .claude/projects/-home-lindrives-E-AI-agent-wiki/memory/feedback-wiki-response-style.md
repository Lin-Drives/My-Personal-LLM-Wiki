---
name: feedback-wiki-response-style
description: Wiki 查询时的回复风格：并行化、简洁优先
metadata:
  type: feedback
---

回答 wiki 查询时：用 Agent 分流并行任务（多个独立查询同时跑），回复保持简洁，不展开细节除非用户追问。

**Why:** 用户反馈等待时间太长，大段输出影响效率。
**How to apply:** wiki 相关的 Query 操作中，能并行的搜索/读取用 Agent 同时发起，回答时直奔主题、一段讲完，不主动追加分析和建议。
