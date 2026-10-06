# Kimi Claw 论文雷达产出模板

依据 2026-10-06 导出的设置，保留原有扫描顺序与 Markdown 报告，在报告旁新增同名 JSON。三个长期问题用于关联，不替代领域轮换。本模板尚未配置到远端 Kimi 任务。

## 当前扫描安排

- 周日步骤 1 生成报告，步骤 2 更新轮换并统一推送摘要。
- 轮换顺序：AI Infra → Deep Learning → Physics-informed AI → World Models → Embodied Intelligence → AI Infra。
- 具身专项独立扫描 human-data-training，追踪 Danfei Xu，不推进周轮换。任务名虽为 biweekly，导出 cron 实际每周三 09:17 执行；本模板不修改频率。
- 获取顺序：国外 Survey / Review（高被引优先）→ 细分领域最新论文（arXiv + 顶会）。引用情况无法确认时注明。
- 阅读顺序：Abstract → Conclusion → 架构/图表/章节 → 关键细节 → 核心贡献 → 局限性 → 同领域整合。记录实际阅读范围，无法访问的环节不能冒充已完成。

## 可复制给步骤 1 / 具身专项的提示词

```text
你为 My-Personal-LLM-Wiki 执行论文雷达。
本次类型：<weekly 或 embodied-special>
扫描周期：<本期起止时间，含时区>
实际工具/模型标识：<真实标识；未知版本不补造>

weekly：读取 paperradar/config/rotation.json，按 fields[current_index] 扫描，不自行推进轮换。保留 AI Infra → Deep Learning → Physics-informed AI → World Models → Embodied Intelligence 的顺序。
embodied-special：扫描 human-data-training，追踪 Danfei Xu，不改周轮换状态。关键词沿用 human data training、humanoid robot learning、teleoperation data、human demonstration、dexterous manipulation from human data。

先获取国外综述（高被引优先），再获取细分领域最新论文。按 Abstract → Conclusion → 架构/图表/章节 → 关键细节 → 核心贡献 → 局限性 → 同领域整合阅读；说明实际阅读到哪一步。

读者已有机器学习基础，正在进入机器人领域。以下问题仅作为关联维度，不改变轮换或强行筛掉其他领域：
- world-model-planning：世界模型怎样支撑可靠的机器人规划？关注动作条件预测、规划、真机证据、长程误差与失效条件。
- human-video-transfer：在什么任务和迁移条件下，人类视频能减少哪些机器人数据需求？区分视觉预训练、轨迹监督与策略监督，说明仍需的机器人数据及迁移边界。
- robot-deployment：机器人策略如何满足实际部署约束？关注硬件、端到端延迟、控制频率、功耗与异常恢复。不能从通用推理性能直接推断机器人表现。

同时交付同名 Markdown 报告与 UTF-8 JSON：
- weekly 保存到 paperradar/weekly/YYYY-Www-<field-slug>.md 和 .json。
- embodied-special 保存到 paperradar/biweekly/YYYY-MM-DD-embodied-intelligence.md 和 .json。
- 保留现有 Markdown 的 Top 5、其他值得一看、趋势、学者追踪、Watch List 及下期预告等适用章节；不足五篇不凑数。
- Markdown 补充实际检索范围、访问失败与待确认事项。趋势与整合注明工具判断及依据，不冒充仓库作者观点。
- JSON 不含 Markdown 围栏或额外解释文字，schema_version 固定为 1。
- scan_id 唯一且不可变，包含类型、领域和批次，例如 2026-W42-weekly-ai-infra-01。修改批次或重试失败项使用新标识。
- scanned_at 是实际扫描时间（ISO 8601，含时区），不是论文发表日期。
- producer 填实际工具/模型标识，未知版本不补造。
- papers 收录报告中本期推荐、ID 已确认的现代 arXiv 论文，包括 Top 5 和其他值得一看；同一版本每批只列一次。Watch List 中待核实的候选不进入 papers。
- arxiv_id 为基础 ID，不含 URL 或版本；确认版本时可加 arxiv_version: v2，未知则省略。
- summary 中文概括问题、方法、证据与局限；只读摘要时明确写“仅依据摘要，未核对全文”。数字需有实际来源，不明处写“未报告”或“尚未确认”。
- selection_reason 说明推荐理由，这是工具判断。tags 自由填写；questions 可用上述多个 ID，不相关时用 []，不创造问题 ID。
- 不填改写的原始 Abstract、官方标题或日期；接入程序会获取官方 arXiv 响应、标题和日期。
- DOI、新闻、代码项目及旧式 arXiv ID 保留在 Markdown 中，不虚构现代 arXiv ID。
- 无候选时 papers: []，说明实际覆盖范围；扫描失败不能写成“没有新论文”。
- 保留步骤 1 不单独推送摘要的职责；专项通知沿用既有安排。
- 不直接修改 wiki、raw、已有任务、脚本或 CI，不执行 commit/push；交付产物给仓库执行者。
```

## JSON 形状

以下仅是形状示意，尖括号内容必须替换；可解析的字段示例见 [scan.example.json](scan.example.json)，其中摘要和推荐理由也需替换，不可直接发布。

```json
{
  "schema_version": 1,
  "scan_id": "<唯一批次标识>",
  "scanned_at": "<实际扫描时间，含时区>",
  "producer": "<实际工具或模型标识>",
  "papers": [
    {
      "arxiv_id": "<基础ID，如2506.09985>",
      "summary": "<问题、方法、证据、局限与实际阅读范围>",
      "selection_reason": "<工具推荐理由>",
      "tags": ["<主题标签>"],
      "questions": ["world-model-planning"]
    }
  ]
}
```

## 步骤 2 的交接建议

保留更新轮换与统一推送摘要的职责，但应检查本次预期领域、报告日期与扫描周期，不能仅按旧 `last_scan` 找文件；该字段记录上次完成日期，存在误认旧报告的风险。

确认本期 Markdown 报告完成后，周轮换每批只推进一次，history 记录实际报告路径。扫描成功与 wiki 接入成功分开记录：JSON 缺失或接入失败时记录待重试，不重复推进轮换。具身专项不推进轮换。这是待配置到 Kimi 的建议，仓库未实现或修改远端轮换程序。

## 仓库接入

```bash
python3 scripts/radar_pipeline.py ingest --input /absolute/path/report.json
python3 scripts/radar_pipeline.py validate
python3 scripts/radar_pipeline.py render
```

退出码 0 表示条目均已接收；2 表示部分失败，有效条目已保存；1 表示批次级错误。检查 `radar/scans/<scan_id>.json` 的 accepted/rejected，失败项用新 scan_id 重试。

当前脚本只读取 JSON；Markdown 中的领域整合、趋势与 Tracker 不会自动发布。重复论文版本保留首次解读，新版本另建记录。仓库执行者按 AGENTS.md 测试、commit，经推送授权后 push。动态不等待人工审核，但明确标注自动生成、未人工核验；来源身份匹配不等于内容核验。
