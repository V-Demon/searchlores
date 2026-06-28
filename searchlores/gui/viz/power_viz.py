# searchlores/gui/viz/power_viz.py
"""Visualisation des vecteurs de pouvoir"""

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QWidget, QVBoxLayout


class PowerViz(QWidget):
    """Visualisation des vecteurs de pouvoir"""

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.figure, self.ax = plt.subplots(figsize=(8, 5))
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.figure.patch.set_facecolor('#2c3e50')
        self.ax.set_facecolor('#34495e')

    def update_viz(self, context):
        """Met à jour la visualisation"""
        self.ax.clear()

        if not context.power_vectors:
            self.ax.text(0.5, 0.5, "Aucun vecteur de pouvoir détecté", ha='center', va='center', color='white')
            self.canvas.draw()
            return

        # Afficher les vecteurs comme texte
        y_positions = list(range(len(context.power_vectors)))
        self.ax.set_ylim(-1, len(context.power_vectors))

        for i, vector in enumerate(context.power_vectors):
            # Tronquer si trop long
            display_text = vector[:80] + "..." if len(vector) > 80 else vector
            self.ax.text(0.05, i, f"→ {display_text}", transform=self.ax.get_yaxis_transform(),
                        color='#e67e22', fontsize=10, verticalalignment='center',
                        bbox=dict(boxstyle='round,pad=0.5', facecolor='#34495e', alpha=0.8))

        self.ax.set_title("⚔️ Vecteurs de pouvoir identifiés", color='white', fontsize=14, fontweight='bold')
        self.ax.axis('off')

        self.canvas.draw()

    def clear(self):
        """Efface la visualisation"""
        self.ax.clear()
        self.canvas.draw()
