# Kimi Claw 每周论文雷达产出模板

把下面的提示词交给现有定时扫描任务，并填写本期时间范围与输出位置。机器接入格式沿用 `scan.example.json`；本文件不意味着定时任务已经接入。

## 可复制的提示词

```text
你为 My-Personal-LLM-Wiki 执行本期论文雷达扫描。

扫描时间范围：<填写本期起止时间，含时区>
输出 JSON 文件：<填写实际可写的绝对路径>/weekly-scan.json
实际工具/模型标识：<填写实际标识；未知版本不填写>

读者已有机器学习基础，正在进入机器人领域。优先关注以下问题，但允许收录其他有价值的主题，不要求每篇都关联这些问题：
1. 世界模型怎样支撑可靠的机器人规划？
   questions ID: world-model-planning
   关注动作条件预测、规划、真机证据、长程误差和失效条件。
2. 在什么任务和迁移条件下，人类视频能减少哪些机器人数据需求？
   questions ID: human-video-transfer
   区分视觉预训练、轨迹监督与策略监督，说明仍需的机器人数据及迁移边界。
3. 机器人策略如何满足实际部署约束？
   questions ID: robot-deployment
   关注硬件、端到端延迟、控制频率、功耗和异常恢复，勿从通用推理性能直接推断机器人表现。

交付要求：
- 主要产物是一个 UTF-8 JSON 文件，遵循下方 schema_version: 1 格式，不附加 Markdown 围栏或解释文字。
- scan_id 使用唯一且不可变的标识，如 2026-W41-robotics-01；修改批次或重试失败条目时使用新标识。
- scanned_at 填实际扫描时间（ISO 8601，含时区），不是论文发表日期。
- producer 填实际工具/模型标识，不猜测未知版本或生成者。
- papers 每项的 arxiv_id 为已找到并核对的现代 arXiv 基础 ID，不含 URL 或版本。
- 确认版本时可填写 arxiv_version，如 v2；未知版本时省略，接入程序会查询实际版本。
- summary 用中文概括问题、方法、证据和局限，标识模型解读；数字必须有实际来源支撑。只读了摘要时，明确写“仅依据摘要，未核对全文”；未找到的信息写“未报告”或“尚未确认”。
- selection_reason 说明本期推荐理由及与研究问题的联系，不冒充仓库作者观点，不将发布时间本身当作技术突破证据。
- tags 为自由主题标签列表。questions 可关联多个已定义 ID；不相关时用 []，不要创造新问题 ID。
- 每批同一论文版本只列一次。新版本可以再次收录；接入程序保留历史版本，重复版本不覆盖首次解读。
- 不填写原始 Abstract、官方标题或发布日期的改写副本；接入程序负责获取原始 arXiv 响应、标题与日期。自动摘要不进入 raw。
- 不直接编辑 wiki、raw、已有任务、脚本或 CI，不执行 commit/push。将产物交给仓库接入流程。
- 无候选时 papers 为 []，另说明扫描覆盖与结果；如果扫描失败，不把失败写成“没有新论文”。
- DOI、公司新闻、代码项目及旧式 arXiv ID 暂不进入 papers。另存补充 Markdown 报告，保留官方链接与待核实事项，不虚构现代 arXiv ID。
```

## JSON 形状

下方是占位示意，不可直接接入；所有尖括号内容都必须替换。真实 ID 的格式示例另见 [scan.example.json](scan.example.json)，其中解读仍是占位内容。

```json
{
  "schema_version": 1,
  "scan_id": "<唯一批次标识>",
  "scanned_at": "<实际扫描时间，含时区>",
  "producer": "<实际工具或模型标识>",
  "papers": [
    {
      "arxiv_id": "<基础ID，如2506.09985>",
      "summary": "<问题、方法、证据、局限；说明实际阅读范围>",
      "selection_reason": "<推荐理由；这是工具判断>",
      "tags": ["<主题标签>"],
      "questions": ["world-model-planning"]
    }
  ]
}
```

## 交付与接入

主产物：`weekly-scan.json`。可选补充产物：`weekly-scan-notes.md`，记录实际扫描范围、访问失败、非 arXiv 动态与待确认事项。补充报告不会自动进入动态页；当前脚本也不读取该报告。

仓库执行者收到 JSON 后运行：

```bash
python3 scripts/radar_pipeline.py ingest --input /absolute/path/weekly-scan.json
python3 scripts/radar_pipeline.py validate
python3 scripts/radar_pipeline.py render
```

接入退出码 `0` 表示条目均已接收；`2` 表示部分条目失败，有效条目已保存；`1` 表示批次级错误。查看 `radar/scans/<scan_id>.json` 中的 accepted/rejected，再决定重试。重试用新 scan_id，不修改已保存批次。

发布由仓库执行者串行处理：按 `AGENTS.md` 验证、commit，并在获得推送授权后 push。最新动态不等待人工审核，但必须保留“自动生成、未人工核验”的标识。JSON 合法和来源身份匹配均不等于解读内容已核验。
