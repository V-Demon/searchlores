# searchlores/gui/widgets/lore_selector.py
"""Sélecteur de Lores avec recherche"""

from pathlib import Path
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QListWidget, QListWidgetItem,
    QLineEdit, QLabel, QCheckBox, QHBoxLayout
)
from PyQt5.QtCore import Qt


class LoreSelector(QWidget):
    """Sélecteur de Lores avec recherche et sélection multiple"""

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Label
        label = QLabel("📜 LORES DISPONIBLES")
        label.setStyleSheet("font-weight: bold; font-size: 14px; color: #9b59b6;")
        layout.addWidget(label)

        # Barre de recherche
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("🔍 Rechercher un Lore...")
        self.search_box.textChanged.connect(self._filter_lores)
        self.search_box.setStyleSheet("""
            QLineEdit {
                background-color: #34495e;
                color: #ecf0f1;
                border: 1px solid #7f8c8d;
                border-radius: 3px;
                padding: 5px;
            }
        """)
        layout.addWidget(self.search_box)

        # Liste des Lores
        self.lore_list = QListWidget()
        self.lore_list.setSelectionMode(QListWidget.MultiSelection)
        self.lore_list.setStyleSheet("""
            QListWidget {
                background-color: #2c3e50;
                color: #ecf0f1;
                border: 1px solid #34495e;
                border-radius: 3px;
            }
            QListWidget::item:selected {
                background-color: #9b59b6;
            }
        """)
        layout.addWidget(self.lore_list)

        # Charger les Lores
        self._load_lores()

    def _load_lores(self):
        """Charge la liste des Lores disponibles"""
        # Répertoires à scanner
        lore_dirs = [
            Path("lores"),
            Path("lores_custom"),
            Path("searchlores/lores")
        ]

        for lore_dir in lore_dirs:
            if lore_dir.exists():
                for lore_file in lore_dir.glob("*.lore"):
                    item = QListWidgetItem(lore_file.stem)
                    item.setData(Qt.UserRole, str(lore_file))
                    self.lore_list.addItem(item)

    def _filter_lores(self, search_text: str):
        """Filtre les Lores selon la recherche"""
        search_lower = search_text.lower()
        for i in range(self.lore_list.count()):
            item = self.lore_list.item(i)
            item.setHidden(search_lower not in item.text().lower())

    def get_selected_lores(self) -> list:
        """Retourne les chemins des Lores sélectionnés"""
        return [
            item.data(Qt.UserRole)
            for item in self.lore_list.selectedItems()
        ]

    def clear_selection(self):
        """Efface la sélection"""
        self.lore_list.clearSelection()
