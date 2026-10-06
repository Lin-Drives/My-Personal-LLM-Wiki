# arXiv 原论文 PDF 下载

`scripts/download_arxiv_pdfs.py` 使用 Python 标准库，不依赖扫描脚本。支持现代 arXiv ID、显式版本、扫描 JSON 或历史收录清单。运行前可预览，不会请求网络或创建文件：

```bash
python3 scripts/download_arxiv_pdfs.py --input radar/archive-coverage.json --dry-run
python3 scripts/download_arxiv_pdfs.py 2506.09985v1 --output raw/World-Models
python3 scripts/download_arxiv_pdfs.py --input radar/archive-coverage.json --limit 5
python3 scripts/download_arxiv_pdfs.py --input radar/archive-coverage.json
```

默认按清单中的已有知识文章、原始材料或扫描领域分类，保存到 `raw/<主题>/`；Physics-informed AI 归 Deep-Learning。不能判定分类时停止并要求显式指定目录，单独提供 ID 时用 `--output raw/<主题>`。历史主题目录中，文件名明确包含同一 ID 且通过基础 PDF 检查的文件会跳过；不根据论文标题猜测身份。未标 ID 的旧 PDF 可能重复下载，显式版本也不会因已有其他版本而跳过。

效率来自 ID 去重、跳过已有文件、流式写入、无需先调用搜索 API，以及重启后只处理未完成项。请求串行且间隔至少三秒，不使用高并发。每篇最多三次尝试；404 等错误不重复请求，429 按 Retry-After 秒值及退避等待。失败返回退出码 2，其他成功项保留。

下载中使用 `.part` 临时文件，检查响应长度、PDF 文件头与 EOF 后才改为最终文件名。这是基础完整性检查，不证明文件可被所有 PDF 阅读器解析，也不核实论文标题。失败不会留下伪 PDF；已有损坏最终文件会报告错误，须人工移走后重试。支持完成文件级续跑，不支持字节级断点续传；单个未完成文件会重新下载。每次下载结果增量写入 `radar/download-manifest.json`，成功项包含获取时间、URL 与 SHA-256。

基础 ID 下载当时的最新版本，manifest 明确标记版本未解析。需要可复现版本时提供 `vN`；没有版本的已有文件不会自动检测是否发布新版。不得把下载成功视为论文内容核验。一个输出目录同一时间只运行一个下载器。

## PDF 仅本地保存，原文 Markdown 上传

`raw/**/*.pdf` 已忽略；原始 PDF 保留在本地主题目录，不提交。运行下列命令把下载清单中的成功或已存在 PDF 转成同目录 `.fulltext.md`，已有同名 Markdown 不覆盖：

```bash
python3 -m pip install -r requirements-pdf.txt
python3 scripts/pdf_to_markdown.py
```

最多四个本地工作进程并行提取。每页原始文本放在文本代码块中，保留页码、源 URL、PDF 哈希、提取工具和时间，不进行模型改写。表格、公式、多栏顺序与图片不能保证还原；文字缺失页单独记录，无可提取文本的整篇报告失败。报告保存在 `radar/pdf-conversion-manifest.json`。转换成功不等于论文内容核验，也不代表已完成知识文章。

已存在 Git 历史中的旧 PDF 不因忽略规则自动消失；本次从当前跟踪树移除旧 PDF，但保留磁盘文件，不改写已推送的历史。
