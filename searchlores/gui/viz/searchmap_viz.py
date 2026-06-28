# searchlores/gui/viz/searchmap_viz.py
"""Visualisation de la SearchMap"""

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class SearchMapViz(QWidget):
    """Visualisation de la SearchMap en graphe"""

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Figure matplotlib
        self.figure, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.figure.patch.set_facecolor('#2c3e50')
        self.ax.set_facecolor('#34495e')

    def update_viz(self, context):
        """Met à jour la visualisation"""
        self.ax.clear()

        # Créer le graphe
        G = nx.DiGraph()

        # Ajouter le prompt comme nœud racine
        G.add_node("PROMPT", node_type="prompt")

        # Ajouter les strates
        for i, layer in enumerate(context.layers):
            stratum = layer.get('stratum', f'stratum_{i}')
            plugin = layer.get('plugin', 'unknown')
            node_id = f"{stratum}_{plugin}"
            G.add_node(node_id, node_type="layer", label=stratum)
            G.add_edge("PROMPT", node_id, label=plugin)

        # Ajouter les contradictions
        for i, contradiction in enumerate(context.contradictions):
            tension = contradiction.get('tension', f'contradiction_{i}')
            G.add_node(f"contradiction_{i}", node_type="contradiction", label=tension)

        # Ajouter les omissions
        for omission in context.omissions:
            G.add_node(f"omission_{omission}", node_type="omission", label=omission)

        # Positions
        pos = nx.spring_layout(G, k=2, iterations=50)

        # Couleurs par type
        color_map = {
            "prompt": "#3498db",
            "layer": "#9b59b6",
            "contradiction": "#e74c3c",
            "omission": "#95a5a6"
        }

        node_colors = [color_map[G.nodes[n].get('node_type', 'layer')] for n in G.nodes()]

        # Dessiner
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2000, alpha=0.8, ax=self.ax)
        nx.draw_networkx_labels(G, pos, font_size=8, font_color='white', ax=self.ax)
        nx.draw_networkx_edges(G, pos, edge_color='#7f8c8d', arrows=True, arrowsize=20, ax=self.ax)

        self.ax.set_title("🗺️ SearchMap — Graphe des strates", color='white', fontsize=14, fontweight='bold')
        self.ax.axis('off')

        self.canvas.draw()

    def clear(self):
        """Efface la visualisation"""
        self.ax.clear()
        self.canvas.draw()
