# searchlores/gui/viz/timeline_viz.py
"""Visualisation de la timeline des strates"""

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class TimelineViz(QWidget):
    """Visualisation de la timeline des strates"""

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.figure, self.ax = plt.subplots(figsize=(8, 4))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.figure.patch.set_facecolor('#2c3e50')
        self.ax.set_facecolor('#34495e')

    def update_viz(self, context):
        """Met à jour la visualisation"""
        self.ax.clear()

        if not context.layers:
            self.ax.text(0.5, 0.5, "Aucune strate", ha='center', va='center', color='white')
            self.canvas.draw()
            return

        # Données
        strata = [layer.get('stratum', 'unknown') for layer in context.layers]
        timestamps = list(range(len(strata)))

        # Barres horizontales
        bars = self.ax.barh(timestamps, [1] * len(strata), color='#9b59b6', alpha=0.7)

        # Labels
        self.ax.set_yticks(timestamps)
        self.ax.set_yticklabels(strata, color='white')
        self.ax.set_xlabel("Progression temporelle", color='white')
        self.ax.set_title("📅 Timeline des strates archéologiques", color='white', fontsize=14, fontweight='bold')

        # Style
        self.ax.tick_params(colors='white')
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['left'].set_color('white')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)

        self.canvas.draw()

    def clear(self):
        """Efface la visualisation"""
        self.ax.clear()
        self.canvas.draw()
