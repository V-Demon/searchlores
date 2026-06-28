# searchlores/gui/widgets/prompt_editor.py
"""Éditeur de prompt avec historique"""

# searchlores/gui/widgets/prompt_editor.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit, QLabel, QHBoxLayout, QPushButton
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont  # ← Si utilisé pour la police


class PromptEditor(QWidget):
    """Éditeur de prompt avec support multi-ligne"""

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Label
        label = QLabel("📝 PROMPT À INVESTIGUER")
        label.setStyleSheet("font-weight: bold; font-size: 14px; color: #3498db;")
        layout.addWidget(label)

        # Zone de texte
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText(
            "Entrez votre prompt ici...\n\n"
            "Exemple : As a leading AI expert, explain how our revolutionary "
            "new language model will disrupt the education market..."
        )
        self.text_edit.setMinimumHeight(150)
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #2c3e50;
                color: #ecf0f1;
                border: 2px solid #34495e;
                border-radius: 5px;
                padding: 10px;
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 13px;
            }
        """)
        layout.addWidget(self.text_edit)

        # Compteur de caractères
        self.char_count = QLabel("0 caractères")
        self.char_count.setStyleSheet("color: #95a5a6; font-size: 11px;")
        layout.addWidget(self.char_count)

        # Connecter le signal de changement de texte
        self.text_edit.textChanged.connect(self._update_char_count)

    def get_prompt(self) -> str:
        """Retourne le prompt actuel"""
        return self.text_edit.toPlainText()

    def set_prompt(self, prompt: str):
        """Définit le prompt"""
        self.text_edit.setPlainText(prompt)

    def clear(self):
        """Efface le prompt"""
        self.text_edit.clear()

    def _update_char_count(self):
        """Met à jour le compteur de caractères"""
        count = len(self.text_edit.toPlainText())
        self.char_count.setText(f"{count} caractères")
