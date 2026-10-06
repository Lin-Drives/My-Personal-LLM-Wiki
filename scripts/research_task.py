"""Resume research with explicit artifacts; this command never publishes articles."""
import argparse
import hashlib
from datetime import datetime, timezone
from pathlib import Path
import re
import sys

from radar_pipeline import ROOT, read_json, write_json


def artifact_path(root, value, directory):
    path = (root / value).resolve()
    path.relative_to((root / directory).resolve())
    if not path.is_file():
        raise ValueError("产物不存在：" + value)
    return path


def transition(root, identity, state, owner, artifact=None, report=None, note=None):
    if not re.fullmatch(r"\d{4}\.\d{4,5}v[1-9]\d*", identity):
        raise ValueError("任务身份必须包含论文版本")
    if not owner.strip():
        raise ValueError("owner 不能为空")
    path = root / "radar/tasks" / (identity + ".json")
    task = read_json(path)
    old = task["state"]
    allowed = {
        "pending": {"in_progress", "parked"},
        "in_progress": {"needs_review", "completed", "parked"},
        "needs_review": {"in_progress", "completed", "parked"},
        "parked": {"in_progress"},
        "completed": set(),
    }
    if state not in allowed[old]:
        raise ValueError("不允许的状态迁移：" + old + " → " + state)
    if old in ("in_progress", "needs_review") and task.get("owner") != owner:
        raise ValueError("任务已有负责人；先由当前负责人停放并记录交接，再接手")
    if state == "in_progress":
        if task["attempts"] >= task["max_attempts"]:
            raise ValueError("已达到尝试上限；保留 parked，调整任务范围后再明确增加预算")
        task["attempts"] += 1
    if state in ("needs_review", "completed"):
        artifact = artifact or task.get("artifact")
        if not artifact:
            raise ValueError("需要 --artifact drafts/ 下的解读文件")
        artifact_path(root, artifact, "drafts")
        task["artifact"] = artifact
    if state == "completed" and task.get("independent_review_required"):
        if not report:
            raise ValueError("本任务需要独立核查报告")
        review = read_json(artifact_path(root, report, "radar/reviews"))
        if review.get("paper") != identity or review.get("artifact") != task["artifact"]:
            raise ValueError("核查报告的论文或产物不匹配")
        current_hash = hashlib.sha256(artifact_path(root, task["artifact"], "drafts").read_bytes()).hexdigest()
        if review.get("artifact_sha256") != current_hash:
            raise ValueError("草稿已变化或核查报告未记录内容哈希")
        if not review.get("reviewer") or review["reviewer"] == owner or review.get("outcome") != "pass":
            raise ValueError("核查者必须独立于生成者，结果必须 pass")
        claims = review.get("claims")
        if not isinstance(claims, list) or not claims:
            raise ValueError("报告必须逐项记录论断与证据")
        for claim in claims:
            if claim.get("verdict") != "supported" or not all(claim.get(k) for k in ("claim", "source", "location", "evidence")):
                raise ValueError("存在缺失证据或不受支持的论断")
            artifact_path(root, claim["source"], "raw")
        task["review_report"] = report
    if state == "parked" and not note:
        raise ValueError("停放任务需要 --note 记录问题与下一步")
    task.update(state=state, owner=owner, next_step=note or "按 docs/workflow.md 继续", updated_at=datetime.now(timezone.utc).isoformat())
    write_json(path, task)
    return task


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paper")
    parser.add_argument("state", choices=("in_progress", "needs_review", "completed", "parked"))
    parser.add_argument("--owner", required=True)
    parser.add_argument("--artifact")
    parser.add_argument("--report")
    parser.add_argument("--note")
    args = parser.parse_args()
    try:
        task = transition(ROOT, args.paper, args.state, args.owner, args.artifact, args.report, args.note)
        print(task["state"], "attempts:", task["attempts"])
        return 0
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
