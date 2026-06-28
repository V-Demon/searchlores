# searchlores/gui/viz/contradiction_viz.py
"""Visualisation des contradictions"""

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class ContradictionViz(QWidget):
    """Visualisation des contradictions en graphe"""

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.figure, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.figure.patch.set_facecolor('#2c3e50')
        self.ax.set_facecolor('#34495e')

    def update_viz(self, context):
        """Met à jour la visualisation"""
        self.ax.clear()

        if not context.contradictions:
            self.ax.text(0.5, 0.5, "Aucune contradiction détectée", ha='center', va='center', color='white')
            self.canvas.draw()
            return

        # Créer le graphe
        G = nx.Graph()

        for i, contradiction in enumerate(context.contradictions):
            tension = contradiction.get('tension', f'contradiction_{i}')
            G.add_node(f"contradiction_{i}", label=tension, node_type="contradiction")

        # Positions
        pos = nx.spring_layout(G, k=3, iterations=50)

        # Dessiner
        nx.draw_networkx_nodes(G, pos, node_color='#e74c3c', node_size=3000, alpha=0.8, ax=self.ax)
        nx.draw_networkx_labels(G, pos, labels={n: G.nodes[n]['label'] for n in G.nodes()},
                               font_size=9, font_color='white', ax=self.ax)

        self.ax.set_title("⚡ Contradictions détectées", color='white', fontsize=14, fontweight='bold')
        self.ax.axis('off')

        self.canvas.draw()

    def clear(self):
        """Efface la visualisation"""
        self.ax.clear()
        self.canvas.draw()
