"""Portable intake and handoff for weekly scans; no model or Git credentials needed."""
import argparse
from datetime import datetime
import hashlib
import html
import json
from pathlib import Path
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
LAST_REQUEST = 0.0
ATOM = "{http://www.w3.org/2005/Atom}"
QUESTIONS = {
    "world-model-planning": "世界模型与可靠规划",
    "human-video-transfer": "人类视频与机器人数据需求",
    "robot-deployment": "机器人实际部署约束",
}


def timestamp(value):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("时间必须包含时区")
    return value


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def fetch_arxiv(identifier):
    global LAST_REQUEST
    time.sleep(max(0, 3 - (time.monotonic() - LAST_REQUEST)))
    LAST_REQUEST = time.monotonic()
    request = urllib.request.Request(
        "https://export.arxiv.org/api/query?id_list=" + identifier,
        headers={"User-Agent": "PersonalLLMWiki/1.0"},
    )
    with urllib.request.urlopen(request, timeout=40) as response:
        return response.read()


def source_metadata(payload, expected):
    root = ET.fromstring(payload)
    entry = root if root.tag == ATOM + "entry" else root.find(ATOM + "entry")
    if entry is None:
        raise ValueError("arXiv 未返回论文")
    identity = entry.findtext(ATOM + "id", "").rstrip("/").rsplit("/", 1)[-1]
    if not re.fullmatch(r"\d{4}\.\d{4,5}v[1-9]\d*", identity):
        raise ValueError("arXiv 返回无效论文身份")
    if identity.split("v")[0] != expected.split("v")[0] or ("v" in expected and identity != expected):
        raise ValueError("来源身份与请求不匹配")
    fields = {k: " ".join(entry.findtext(ATOM + k, "").split()) for k in ("title", "summary", "published", "updated")}
    if not fields["title"] or not fields["summary"]:
        raise ValueError("原始标题或摘要缺失")
    timestamp(fields["published"])
    timestamp(fields["updated"])
    return identity, fields


def validate_record(record):
    identifier = record["arxiv_id"]
    if not isinstance(identifier, str) or not re.fullmatch(r"\d{4}\.\d{4,5}", identifier):
        raise ValueError("arxiv_id 必须是基础 ID，如 2506.09985")
    version = record.get("arxiv_version", "")
    if version and (not isinstance(version, str) or not re.fullmatch(r"v[1-9]\d*", version)):
        raise ValueError("arxiv_version 必须为 v1、v2 等")
    for key in ("summary", "selection_reason"):
        if not isinstance(record.get(key), str) or not record[key].strip():
            raise ValueError(key + " 必须是非空文本")
    for key in ("tags", "questions"):
        if not isinstance(record.get(key), list) or not all(isinstance(x, str) for x in record[key]):
            raise ValueError(key + " 必须是字符串列表")
    if set(record["questions"]) - QUESTIONS.keys():
        raise ValueError("未知问题 ID；新主题可先放入 tags，questions 可为空")
    return identifier + version


def ingest(root, batch, fetch=fetch_arxiv):
    # Refuse to extend or reuse a damaged catalog, including on idempotent retries.
    catalog = validate(root)
    scan_id = batch["scan_id"]
    if not isinstance(scan_id, str) or not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_-]{0,79}", scan_id):
        raise ValueError("scan_id 只能包含字母、数字、连字符和下划线")
    timestamp(batch["scanned_at"])
    if batch.get("schema_version") != 1 or not isinstance(batch.get("producer"), str) or not batch["producer"].strip():
        raise ValueError("需要 schema_version: 1 和 producer")
    if not isinstance(batch.get("papers"), list):
        raise ValueError("papers 必须是列表")
    scan_path = root / "radar/scans" / (scan_id + ".json")
    digest = hashlib.sha256(json.dumps(batch, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
    if scan_path.exists():
        old = read_json(scan_path)
        if old["input_sha256"] != digest:
            raise ValueError("同一 scan_id 内容已存在且不同，请使用新的 scan_id")
        return old
    catalog_path = root / "radar/catalog.json"
    records = {(p["arxiv_id"], p["arxiv_version"]): p for p in catalog["papers"]}
    accepted, rejected = [], []
    for item in batch["papers"]:
        try:
            expected = validate_record(item)
            requested_path = root / "raw/arxiv" / (expected + ".xml")
            payload = requested_path.read_bytes() if requested_path.exists() else fetch(expected)
            identity, fields = source_metadata(payload, expected)
            base, version = identity.split("v")
            version = "v" + version
            source_path = root / "raw/arxiv" / (identity + ".xml")
            if not source_path.exists():
                source_path.parent.mkdir(parents=True, exist_ok=True)
                source_path.write_bytes(payload)
            key = (base, version)
            if key not in records:
                record = {
                    "arxiv_id": base, "arxiv_version": version,
                    "title": fields["title"], "published_at": fields["published"],
                    "updated_at": fields["updated"], "source_url": "https://arxiv.org/abs/" + identity,
                    "source_path": source_path.relative_to(root).as_posix(),
                    "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
                    "summary": item["summary"], "selection_reason": item["selection_reason"],
                    "tags": item["tags"], "questions": item["questions"],
                    "scanned_at": batch["scanned_at"], "producer": batch["producer"], "scan_id": scan_id,
                }
                records[key] = record
            record = records[key]
            task_path = root / "radar/tasks" / (identity + ".json")
            if not task_path.exists():
                write_json(task_path, {
                    "paper": identity, "source": record["source_path"], "questions": record["questions"],
                    "state": "pending", "attempts": 0, "max_attempts": 2, "owner": None,
                    "independent_review_required": False,
                    "artifact": None, "review_report": None,
                    "next_step": "按需撰写解读；重要结论交独立核查，动态发布不等待本任务。",
                })
            accepted.append(identity)
        except (KeyError, ValueError, TypeError, AttributeError, OSError, ET.ParseError) as error:
            rejected.append({"input": item, "reason": str(error)})
    catalog["papers"] = sorted(records.values(), key=lambda p: (p["scanned_at"], p["arxiv_id"], int(p["arxiv_version"][1:])), reverse=True)
    write_json(catalog_path, catalog)
    report = {"input_sha256": digest, "batch": batch, "accepted": accepted, "rejected": rejected}
    write_json(scan_path, report)
    return report


def validate(root):
    catalog = read_json(root / "radar/catalog.json")
    if catalog.get("schema_version") != 1 or not isinstance(catalog.get("papers"), list):
        raise ValueError("catalog 格式无效")
    seen = set()
    for p in catalog["papers"]:
        identity = validate_record(p)
        if identity in seen:
            raise ValueError("重复论文版本 " + identity)
        seen.add(identity)
        timestamp(p["scanned_at"])
        path = (root / p["source_path"]).resolve()
        if path != (root / "raw/arxiv" / (identity + ".xml")).resolve():
            raise ValueError("原始来源路径不匹配")
        payload = path.read_bytes()
        if hashlib.sha256(payload).hexdigest() != p["source_sha256"]:
            raise ValueError("原始来源内容已改变 " + identity)
        _, fields = source_metadata(payload, identity)
        if any(p[key] != fields[source] for key, source in (("title", "title"), ("published_at", "published"), ("updated_at", "updated"))):
            raise ValueError("元数据与原始来源不一致 " + identity)
        if p["source_url"] != "https://arxiv.org/abs/" + identity:
            raise ValueError("来源 URL 不匹配")
    return catalog


def render(root, wiki_dir=None):
    catalog = validate(root)
    out = (wiki_dir or root / "wiki") / "updates.md"
    lines = ["---", "type: Research Feed", "title: 最新论文动态", "description: 持续展示论文雷达发现的论文与工具解读。", "tags: [论文雷达]", "status: draft", "---", "", "# 最新论文动态", "", "> 自动整理的扫描结果，尚未人工核验；摘要与推荐理由为扫描工具解读。原文链接可直接查看。", "", "按发现时间排列；论文发表与修订时间分别标注。深入解读的进度不阻塞这里更新。", ""]
    if not catalog["papers"]:
        lines += ["尚未接入新的扫描结果。已有知识文章请从首页主题索引阅读。", ""]
    for p in catalog["papers"]:
        safe = lambda value: html.escape(str(value)).replace("\n", "<br>")
        lines += ["<article>", "<h2>" + safe(p["title"]) + "</h2>",
                  '<p><a href="' + p["source_url"] + '">arXiv:' + p["arxiv_id"] + p["arxiv_version"] + " · 查看原文</a></p>",
                  "<p>发现：" + safe(p["scanned_at"]) + " · 发表：" + safe(p["published_at"]) + " · 修订：" + safe(p["updated_at"]) + "</p>",
                  "<p><strong>自动摘要：</strong>" + safe(p["summary"]) + "</p>",
                  "<p><strong>推荐理由（工具判断）：</strong>" + safe(p["selection_reason"]) + "</p>",
                  "<p>关联问题：" + safe("、".join(QUESTIONS[q] for q in p["questions"]) or "其他关注方向") + "</p>",
                  "<p>标签：" + safe("、".join(p["tags"])) + " · 生成者：" + safe(p["producer"]) + "</p>", "</article>", ""]
    content = "\n".join(lines)
    if not out.exists() or out.read_text(encoding="utf-8") != content:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")
    return len(catalog["papers"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("ingest", "validate", "render"))
    parser.add_argument("--input", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "ingest":
            if args.input is None:
                parser.error("ingest 需要 --input")
            report = ingest(ROOT, read_json(args.input))
            print(json.dumps({"accepted": report["accepted"], "rejected": report["rejected"]}, ensure_ascii=False))
            return 2 if report["rejected"] else 0
        print("papers:", len(validate(ROOT)["papers"]) if args.command == "validate" else render(ROOT))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
