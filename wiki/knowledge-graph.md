# Knowledge Graph

<script src="https://cdn.jsdelivr.net/npm/vis-data@7.1.9/peer/umd/vis-data.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vis-network@9.1.9/peer/umd/vis-network.min.js"></script>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/vis-network@9.1.9/styles/vis-network.min.css">

<div id="kg-container" style="width:100%; height:82vh; border:1px solid var(--md-default-fg-color--lightest); border-radius:8px; background:var(--md-default-bg-color);"></div>

<div style="margin-top:12px; display:flex; gap:16px; flex-wrap:wrap; font-size:0.85rem; color:var(--md-default-fg-color--light);" id="legend"></div>

<script>
(function () {
  const container = document.getElementById("kg-container");
  const legend = document.getElementById("legend");
  const topicColors = {
    "AI-Infra":              "#4A90D9",
    "Chip-Architecture":     "#E8913A",
    "Deep-Learning":         "#50B86C",
    "Reinforcement-Learning":"#E04A4A",
    "World-Models":          "#9B59B6",
  };

  async function init() {
    const resp = await fetch("/graph-data.json");
    if (!resp.ok) {
      container.innerHTML = '<p style="padding:2rem">graph-data.json not found. Run <code>python scripts/generate-graph-data.py</code> first.</p>';
      return;
    }
    const data = await resp.json();

    // Legend
    const groups = [...new Set(data.nodes.map(n => n.topic))];
    legend.innerHTML = groups.map(g =>
      `<span style="display:inline-flex;align-items:center;gap:4px"><span style="width:10px;height:10px;border-radius:50%;background:${topicColors[g]||"#888"}"></span> ${g}</span>`
    ).join("");

    const nodes = new vis.DataSet(data.nodes.map(n => ({
      ...n,
      shape: "dot",
      size: n.label.length > 20 ? 18 : 14,
      font: { size: 12, face: "system-ui", color: "var(--md-default-fg-color)" },
      borderWidth: 2,
      borderWidthSelected: 3,
    })));

    const edges = new vis.DataSet(data.edges.map(e => ({
      ...e,
      arrows: { to: { enabled: true, scaleFactor: 0.4 } },
      color: { opacity: 0.35 },
      smooth: { type: "continuous" },
      width: 0.8,
    })));

    const options = {
      physics: {
        solver: "forceAtlas2Based",
        forceAtlas2Based: {
          gravitationalConstant: -28,
          centralGravity: 0.008,
          springLength: 140,
          springConstant: 0.06,
          damping: 0.4,
        },
        stabilization: { iterations: 200 },
      },
      interaction: {
        hover: true,
        tooltipDelay: 150,
        zoomView: true,
        dragView: true,
      },
      layout: { improvedLayout: true },
    };

    const network = new vis.Network(container, { nodes, edges }, options);

    // Double-click → navigate to article
    network.on("doubleClick", function (params) {
      if (params.nodes.length > 0) {
        const node = nodes.get(params.nodes[0]);
        if (node && node.url) {
          window.location.href = "/" + node.url;
        }
      }
    });
  }

  // Respect MkDocs palette toggle
  const observer = new MutationObserver(() => {
    const bg = getComputedStyle(document.body).getPropertyValue("--md-default-bg-color");
    container.style.background = bg;
  });
  observer.observe(document.body, { attributes: true, attributeFilter: ["data-md-color-scheme"] });

  init();
})();
</script>
