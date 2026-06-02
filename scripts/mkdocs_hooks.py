"""MkDocs hooks — regenerate graph-data.json before each build."""
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_graph_data import generate

log = logging.getLogger("mkdocs.hooks")


def on_pre_build(config):
    wiki_dir = Path(config["docs_dir"])
    if not wiki_dir.is_absolute():
        wiki_dir = Path.cwd() / wiki_dir
    output = wiki_dir / "graph-data.json"
    n, e = generate(wiki_dir, output)
    log.info(f"Graph data: {n} nodes, {e} edges → {output}")
