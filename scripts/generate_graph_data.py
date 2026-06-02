"""Scan wiki/*.md files, extract internal links, emit graph-data.json."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
OUTPUT = WIKI / "graph-data.json"
TOPIC_COLORS = {
    "AI-Infra":              "#4A90D9",
    "Chip-Architecture":     "#E8913A",
    "Deep-Learning":         "#50B86C",
    "Reinforcement-Learning":"#E04A4A",
    "World-Models":          "#9B59B6",
}
FALLBACK_COLOR = "#888888"

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def extract_title(md_path: Path) -> str:
    with open(md_path) as f:
        for line in f:
            if line.startswith("# "):
                return line[2:].strip()
    return md_path.stem


def generate(wiki_dir: Path, output_path: Path) -> tuple[int, int]:
    wiki_abs = wiki_dir.resolve()
    file_to_id: dict[str, str] = {}
    nodes: list[dict] = []

    # --- pass 1: nodes ---
    for md_file in sorted(wiki_dir.rglob("*.md")):
        if md_file.name in ("index.md", "log.md", "knowledge-graph.md"):
            continue
        rel = str(md_file.relative_to(WIKI)).replace("\\", "/")
        topic = md_file.parent.name
        title = extract_title(md_file)
        nid = rel.replace("/", "-").replace(".md", "")

        file_to_id[rel] = nid
        nodes.append({
            "id": nid,
            "label": title,
            "group": topic,
            "color": TOPIC_COLORS.get(topic, FALLBACK_COLOR),
            "url": rel.replace(".md", "/"),  # MkDocs URL convention
            "topic": topic,
        })

    # --- pass 2: edges ---
    edges: list[dict] = []
    seen = set()

    for md_file in sorted(wiki_dir.rglob("*.md")):
        if md_file.name in ("index.md", "log.md", "knowledge-graph.md"):
            continue
        src_rel = str(md_file.relative_to(WIKI)).replace("\\", "/")
        src_id = file_to_id[src_rel]
        src_dir = md_file.parent.resolve()

        with open(md_file) as f:
            content = f.read()

        for m in LINK_RE.finditer(content):
            raw = m.group(2).split("#")[0]  # strip anchor
            if not raw.endswith(".md"):
                continue
            if raw.startswith("http"):
                continue

            resolved = (src_dir / raw).resolve()
            try:
                tgt_rel = str(resolved.relative_to(wiki_abs)).replace("\\", "/")
            except ValueError:
                continue  # outside wiki/ (raw references, etc.)

            if tgt_rel not in file_to_id:
                continue  # broken link or future article

            tgt_id = file_to_id[tgt_rel]
            if src_id == tgt_id:
                continue
            key = (src_id, tgt_id)
            if key in seen:
                continue
            seen.add(key)
            edges.append({"from": src_id, "to": tgt_id})

    graph = {"nodes": nodes, "edges": edges}
    output_path.write_text(json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8")
    return len(nodes), len(edges)


def main():
    n, e = generate(WIKI, OUTPUT)
    print(f"Written {n} nodes, {e} edges → {OUTPUT}")


if __name__ == "__main__":
    main()
