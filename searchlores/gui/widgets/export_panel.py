# searchlores/gui/widgets/export_panel.py
"""Panel d'export avec visualisation du code Lisp"""
# searchlores/gui/widgets/export_panel.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit, QLabel, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFont  # ← LIGNES MANQUANTES AJOUTÉES


class ExportPanel(QWidget):
    # ... reste du code inchangé
    """Panel d'export avec code Lisp"""

    export_lisp_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Label
        label = QLabel("💾 EXPORT LISP")
        label.setStyleSheet("font-weight: bold; font-size: 14px; color: #f1c40f;")
        layout.addWidget(label)

        # Zone de code
        self.code_view = QTextEdit()
        self.code_view.setReadOnly(True)
        self.code_view.setFont(QFont("Consolas", 9))
        self.code_view.setStyleSheet("""
            QTextEdit {
                background-color: #2c3e50;
                color: #ecf0f1;
                border: 1px solid #34495e;
                border-radius: 3px;
                padding: 5px;
            }
        """)
        self.code_view.setMaximumHeight(200)
        layout.addWidget(self.code_view)

        # Bouton d'export
        self.export_btn = QPushButton("📤 Générer Export Lisp")
        self.export_btn.clicked.connect(self.export_lisp_clicked)
        self.export_btn.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;
                color: white;
                font-weight: bold;
                padding: 10px;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #e67e22;
            }
        """)
        layout.addWidget(self.export_btn)

    def set_lisp_code(self, code: str):
        """Définit le code Lisp à afficher"""
        self.code_view.setPlainText(code)

    def clear(self):
        """Efface le panel"""
        self.code_view.clear()
