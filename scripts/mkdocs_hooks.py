"""MkDocs hooks — validate and render radar, then regenerate the graph."""
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_graph_data import generate
from radar_pipeline import render
from validate_okf import validate as validate_okf

log = logging.getLogger("mkdocs.hooks")


def on_pre_build(config):
    wiki_dir = Path(config["docs_dir"])
    if not wiki_dir.is_absolute():
        wiki_dir = Path.cwd() / wiki_dir
    render(Path(__file__).resolve().parent.parent, wiki_dir)
    validate_okf(wiki_dir)
    output = wiki_dir / "graph-data.json"
    n, e = generate(wiki_dir, output)
    log.info(f"Graph data: {n} nodes, {e} edges → {output}")


def on_page_markdown(markdown, page, config, files):
    # Keep presentation settings outside the OKF root-index frontmatter.
    if page.file.src_uri == "index.md":
        page.meta["hide"] = ["toc"]
    return markdown
