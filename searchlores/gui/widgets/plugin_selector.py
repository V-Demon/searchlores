# searchlores/gui/widgets/plugin_selector.py
"""Sélecteur de Plugins"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QLabel
from PyQt5.QtCore import Qt

# Importer les plugins built-in
from searchlores.plugins.builtin.authority import (
    AuthorityDetector,
    AssumptionExtractor,
    ContradictionFinder,
    OmissionDetector,
    NarrativeArcheologist,
    CognitiveGenealogist
)


class PluginSelector(QWidget):
    """Sélecteur de Plugins avec sélection multiple"""

    # Plugins disponibles
    AVAILABLE_PLUGINS = {
        "Authority Detector": AuthorityDetector,
        "Assumption Extractor": AssumptionExtractor,
        "Contradiction Finder": ContradictionFinder,
        "Omission Detector": OmissionDetector,
        "Narrative Archeologist": NarrativeArcheologist,
        "Cognitive Genealogist": CognitiveGenealogist,
    }

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        # Label
        label = QLabel("🔌 PLUGINS DISPONIBLES")
        label.setStyleSheet("font-weight: bold; font-size: 14px; color: #e67e22;")
        layout.addWidget(label)

        # Liste des Plugins
        self.plugin_list = QListWidget()
        self.plugin_list.setSelectionMode(QListWidget.MultiSelection)
        self.plugin_list.setStyleSheet("""
            QListWidget {
                background-color: #2c3e50;
                color: #ecf0f1;
                border: 1px solid #34495e;
                border-radius: 3px;
            }
            QListWidget::item:selected {
                background-color: #e67e22;
            }
        """)

        # Ajouter les plugins
        for name, plugin_class in self.AVAILABLE_PLUGINS.items():
            item = QListWidgetItem(name)
            item.setData(Qt.UserRole, plugin_class)
            self.plugin_list.addItem(item)

        layout.addWidget(self.plugin_list)

    def get_selected_plugins(self) -> list:
        """Retourne les classes des plugins sélectionnés"""
        return [
            item.data(Qt.UserRole)
            for item in self.plugin_list.selectedItems()
        ]

    def clear_selection(self):
        """Efface la sélection"""
        self.plugin_list.clearSelection()
