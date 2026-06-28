# searchlores/gui/widgets/log_viewer.py
"""Viewer de logs verbeux avec coloration syntaxique"""

# searchlores/gui/widgets/log_viewer.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit, QLabel, QHBoxLayout, QPushButton
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCharFormat, QColor, QFont  # ← QFont ajouté


class LogViewer(QWidget):
    # ... reste du code inchangé
    """Viewer de logs avec coloration par niveau"""

    # Couleurs par niveau
    LEVEL_COLORS = {
        "DEBUG": "#95a5a6",
        "INFO": "#3498db",
        "WARNING": "#f39c12",
        "ERROR": "#e74c3c",
        "CRITICAL": "#c0392b"
    }

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Header
        header_layout = QHBoxLayout()
        label = QLabel("📋 LOGS (VERBOSE)")
        label.setStyleSheet("font-weight: bold; font-size: 14px; color: #1abc9c;")
        header_layout.addWidget(label)

        # Bouton clear
        clear_btn = QPushButton("🗑️ Clear")
        clear_btn.clicked.connect(self.clear)
        clear_btn.setStyleSheet("""
            QPushButton {
                background-color: #34495e;
                color: #ecf0f1;
                border: none;
                padding: 5px 10px;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        header_layout.addWidget(clear_btn)

        header_layout.addStretch()
        layout.addLayout(header_layout)

        # Zone de logs
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setFont(QFont("Consolas", 10))
        self.log_text.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                border: 1px solid #34495e;
                border-radius: 3px;
                padding: 5px;
            }
        """)
        layout.addWidget(self.log_text)

    def append_log(self, message: str, level: str = "INFO"):
        """Ajoute un message au log avec coloration"""
        color = self.LEVEL_COLORS.get(level, "#d4d4d4")

        # Formater le message
        html = f'<span style="color: {color}; font-family: Consolas, monospace;">{message}</span>'
        self.log_text.append(html)

        # Scroll vers le bas
        scrollbar = self.log_text.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def clear(self):
        """Efface les logs"""
        self.log_text.clear()
