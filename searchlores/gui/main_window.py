# searchlores/gui/main_window.py
"""
Searchlores Laboratory — Fenêtre principale
Le synthétiseur épistémologique pour bidouiller au feeling
"""

import sys
from pathlib import Path
from datetime import datetime

# ─── IMPORTS PYQT5 CORRIGÉS ───
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTabWidget, QTextEdit, QLabel, QPushButton,
    QFileDialog, QMessageBox, QStatusBar, QMenuBar, QMenu,
    QAction, QToolBar
)
from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QFont, QTextCursor, QPalette, QColor

# ─── IMPORTS SEARCHLORES ───
from searchlores.gui.widgets.prompt_editor import PromptEditor
from searchlores.gui.widgets.lore_selector import LoreSelector
from searchlores.gui.widgets.plugin_selector import PluginSelector
from searchlores.gui.widgets.log_viewer import LogViewer
from searchlores.gui.widgets.export_panel import ExportPanel
from searchlores.gui.viz.searchmap_viz import SearchMapViz
from searchlores.gui.viz.timeline_viz import TimelineViz
from searchlores.gui.viz.contradiction_viz import ContradictionViz
from searchlores.gui.viz.power_viz import PowerViz

from searchlores.core.engine import InvestigationEngine
from searchlores.lore.loader import load_lore, load_all_lores
from searchlores.plugins.lisp_exporter import LispExporter


class SearchloresLaboratory(QMainWindow):
    """Fenêtre principale du laboratoire Searchlores"""

    # Signal pour les logs
    log_signal = pyqtSignal(str, str)  # message, level

    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎛️ Searchlores Laboratory — Le Synthétiseur Épistémologique")
        self.setGeometry(100, 100, 1600, 1000)

        # État
        self.engine = InvestigationEngine()
        self.current_context = None
        self.lisp_exporter = LispExporter()

        # Initialiser l'UI
        self._init_ui()
        self._init_menu()
        self._init_toolbar()
        self._init_statusbar()

        # Connecter les logs
        self.log_signal.connect(self.log_viewer.append_log)

        # Log de bienvenue
        self._log("🎛️ Searchlores Laboratory initialisé", "INFO")
        self._log("💡 Branchez un prompt, sélectionnez des Lores et Plugins, et appuyez sur RUN", "INFO")
        self._log("🎸 L'esprit de Syd Barrett plane sur ce laboratoire...", "DEBUG")

    def _init_ui(self):
        """Initialise l'interface utilisateur"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        main_layout = QHBoxLayout(central_widget)

        # Splitter horizontal : Gauche (contrôles) | Droite (visualisations)
        splitter = QSplitter(Qt.Horizontal)

        # ─── PANNEAU GAUCHE : CONTRÔLES ───
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        # Éditeur de prompt
        self.prompt_editor = PromptEditor()
        left_layout.addWidget(self.prompt_editor)

        # Tabs pour Lores et Plugins
        config_tabs = QTabWidget()

        # Tab Lores
        self.lore_selector = LoreSelector()
        config_tabs.addTab(self.lore_selector, "📜 Lores")

        # Tab Plugins
        self.plugin_selector = PluginSelector()
        config_tabs.addTab(self.plugin_selector, "🔌 Plugins")

        left_layout.addWidget(config_tabs)

        # Boutons d'action
        button_layout = QHBoxLayout()

        self.run_button = QPushButton("🚀 RUN INVESTIGATION")
        self.run_button.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                font-weight: bold;
                padding: 15px;
                font-size: 14px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        self.run_button.clicked.connect(self.run_investigation)
        button_layout.addWidget(self.run_button)

        self.clear_button = QPushButton("🗑️ CLEAR")
        self.clear_button.clicked.connect(self.clear_all)
        button_layout.addWidget(self.clear_button)

        left_layout.addLayout(button_layout)

        # Panel d'export
        self.export_panel = ExportPanel()
        self.export_panel.export_lisp_clicked.connect(self.export_to_lisp)
        left_layout.addWidget(self.export_panel)

        splitter.addWidget(left_panel)

        # ─── PANNEAU DROIT : VISUALISATIONS ET LOGS ───
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)

        # Tabs pour visualisations
        viz_tabs = QTabWidget()

        # SearchMap
        self.searchmap_viz = SearchMapViz()
        viz_tabs.addTab(self.searchmap_viz, "🗺️ SearchMap")

        # Timeline
        self.timeline_viz = TimelineViz()
        viz_tabs.addTab(self.timeline_viz, "📅 Timeline")

        # Contradictions
        self.contradiction_viz = ContradictionViz()
        viz_tabs.addTab(self.contradiction_viz, "⚡ Contradictions")

        # Power Vectors
        self.power_viz = PowerViz()
        viz_tabs.addTab(self.power_viz, "⚔️ Power Vectors")

        right_layout.addWidget(viz_tabs)

        # Log viewer
        self.log_viewer = LogViewer()
        right_layout.addWidget(self.log_viewer)

        splitter.addWidget(right_panel)

        # Proportions
        splitter.setSizes([500, 1100])

        main_layout.addWidget(splitter)

    def _init_menu(self):
        """Initialise le menu"""
        menubar = self.menuBar()

        # Menu File
        file_menu = menubar.addMenu("&File")

        load_prompt_action = QAction("&Load Prompt...", self)
        load_prompt_action.triggered.connect(self.load_prompt)
        file_menu.addAction(load_prompt_action)

        save_lisp_action = QAction("&Save Lisp Export...", self)
        save_lisp_action.triggered.connect(self.save_lisp_export)
        file_menu.addAction(save_lisp_action)

        file_menu.addSeparator()

        exit_action = QAction("E&xit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Menu View
        view_menu = menubar.addMenu("&View")

        clear_logs_action = QAction("Clear &Logs", self)
        clear_logs_action.triggered.connect(self.log_viewer.clear)
        view_menu.addAction(clear_logs_action)

        # Menu Help
        help_menu = menubar.addMenu("&Help")

        about_action = QAction("&About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def _init_toolbar(self):
        """Initialise la barre d'outils"""
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        toolbar.addAction("🚀 Run", self.run_investigation)
        toolbar.addAction("🗑️ Clear", self.clear_all)
        toolbar.addSeparator()
        toolbar.addAction("💾 Save Lisp", self.save_lisp_export)

    def _init_statusbar(self):
        """Initialise la barre de statut"""
        self.statusBar().showMessage("Prêt à investiguer")

    def _log(self, message: str, level: str = "INFO"):
        """Ajoute un message au log"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.log_signal.emit(f"[{timestamp}] [{level}] {message}", level)

    def run_investigation(self):
        """Exécute l'investigation"""
        prompt = self.prompt_editor.get_prompt()

        if not prompt.strip():
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un prompt")
            return

        self._log("=" * 70, "INFO")
        self._log(f"🚀 DÉMARRAGE DE L'INVESTIGATION", "INFO")
        self._log(f"📝 Prompt : {prompt[:100]}...", "INFO")

        # Configurer le moteur
        self.engine = InvestigationEngine()

        # Charger les Lores sélectionnés
        selected_lores = self.lore_selector.get_selected_lores()
        if selected_lores:
            self._log(f"📜 {len(selected_lores)} Lore(s) sélectionné(s)", "INFO")
            for lore_name in selected_lores:
                try:
                    lore = load_lore(lore_name)
                    self.engine.set_lore_context(lore)
                    self._log(f"  ✓ Lore chargé : {lore.metadata.name}", "DEBUG")
                except Exception as e:
                    self._log(f"  ✗ Erreur chargement Lore {lore_name}: {e}", "ERROR")

        # Enregistrer les plugins sélectionnés
        selected_plugins = self.plugin_selector.get_selected_plugins()
        self._log(f"🔌 {len(selected_plugins)} Plugin(s) sélectionné(s)", "INFO")
        for plugin_class in selected_plugins:
            try:
                plugin = plugin_class()
                self.engine.register(plugin)
                self._log(f"  ✓ Plugin enregistré : {plugin.name}", "DEBUG")
            except Exception as e:
                self._log(f"  ✗ Erreur enregistrement plugin: {e}", "ERROR")

        # Ajouter le Lisp exporter
        self.engine.register(self.lisp_exporter)
        self._log("💾 Lisp Exporter activé", "DEBUG")

        # Exécuter
        self._log("⚙️  Exécution de l'investigation...", "INFO")
        try:
            self.current_context = self.engine.run(prompt)
            self._log("✅ Investigation terminée avec succès", "INFO")

            # Mettre à jour les visualisations
            self._update_visualizations()

            # Mettre à jour le panel d'export
            lisp_code = self.lisp_exporter.get_last_export()
            self.export_panel.set_lisp_code(lisp_code)

            self.statusBar().showMessage(
                f"Investigation terminée — {len(self.current_context.layers)} strates, "
                f"{len(self.current_context.contradictions)} contradictions"
            )

        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            self._log(f"❌ Erreur: {e}", "ERROR")
            self._log(f"\n{error_details}", "ERROR")
            QMessageBox.critical(self, "Erreur", f"{e}\n\n{error_details}")

    def _update_visualizations(self):
        """Met à jour toutes les visualisations"""
        if not self.current_context:
            return

        self._log("🎨 Mise à jour des visualisations...", "DEBUG")

        try:
            self.searchmap_viz.update_viz(self.current_context)
            self._log("  ✓ SearchMap mise à jour", "DEBUG")
        except Exception as e:
            self._log(f"  ✗ Erreur SearchMap: {e}", "ERROR")

        try:
            self.timeline_viz.update_viz(self.current_context)
            self._log("  ✓ Timeline mise à jour", "DEBUG")
        except Exception as e:
            self._log(f"  ✗ Erreur Timeline: {e}", "ERROR")

        try:
            self.contradiction_viz.update_viz(self.current_context)
            self._log("  ✓ Contradictions mises à jour", "DEBUG")
        except Exception as e:
            self._log(f"  ✗ Erreur Contradictions: {e}", "ERROR")

        try:
            self.power_viz.update_viz(self.current_context)
            self._log("  ✓ Power Vectors mis à jour", "DEBUG")
        except Exception as e:
            self._log(f"  ✗ Erreur Power Vectors: {e}", "ERROR")

    def clear_all(self):
        """Efface tout"""
        self.prompt_editor.clear()
        self.lore_selector.clear_selection()
        self.plugin_selector.clear_selection()
        self.log_viewer.clear()
        self.searchmap_viz.clear()
        self.timeline_viz.clear()
        self.contradiction_viz.clear()
        self.power_viz.clear()
        self.export_panel.clear()
        self.current_context = None
        self.statusBar().showMessage("Prêt à investiguer")
        self._log("🗑️ Tout a été effacé", "INFO")

    def load_prompt(self):
        """Charge un prompt depuis un fichier"""
        filename, _ = QFileDialog.getOpenFileName(
            self, "Charger un prompt", "", "Text Files (*.txt);;All Files (*)"
        )
        if filename:
            try:
                with open(filename, 'r') as f:
                    prompt = f.read()
                self.prompt_editor.set_prompt(prompt)
                self._log(f"📄 Prompt chargé depuis {filename}", "INFO")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur lors du chargement:\n{e}")

    def export_to_lisp(self):
        """Exporte en Lisp"""
        if not self.current_context:
            QMessageBox.warning(self, "Erreur", "Aucune investigation à exporter")
            return

        lisp_code = self.lisp_exporter.get_last_export()
        if lisp_code:
            self.export_panel.set_lisp_code(lisp_code)
            self._log("💾 Code Lisp généré et affiché dans le panel d'export", "INFO")

    def save_lisp_export(self):
        """Sauvegarde l'export Lisp dans un fichier"""
        if not self.current_context:
            QMessageBox.warning(self, "Erreur", "Aucune investigation à exporter")
            return

        lisp_code = self.lisp_exporter.get_last_export()
        if not lisp_code:
            QMessageBox.warning(self, "Erreur", "Aucun code Lisp à sauvegarder")
            return

        filename, _ = QFileDialog.getSaveFileName(
            self, "Sauvegarder l'export Lisp", "investigation.lisp", "Lisp Files (*.lisp)"
        )
        if filename:
            try:
                with open(filename, 'w') as f:
                    f.write(lisp_code)
                self._log(f"💾 Export Lisp sauvegardé dans {filename}", "INFO")
                QMessageBox.information(self, "Succès", f"Export sauvegardé dans:\n{filename}")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur lors de la sauvegarde:\n{e}")

    def show_about(self):
        """Affiche la boîte de dialogue À propos"""
        QMessageBox.about(
            self,
            "À propos de Searchlores Laboratory",
            "<h2>🎛️ Searchlores Laboratory</h2>"
            "<p><b>Le Synthétiseur Épistémologique</b></p>"
            "<p>Un laboratoire expérimental pour l'archéologie cognitive des prompts.</p>"
            "<p>Inspiré par Fravia+ et l'esprit de bidouille de Syd Barrett.</p>"
            "<p><i>Le code est la donnée. La donnée est le code.</i></p>"
            "<p>Version 1.0 — Juin 2026</p>"
        )


def launch_laboratory():
    """Lance le laboratoire"""
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # Palette de couleurs sombre
    from PyQt5.QtGui import QPalette, QColor
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    window = SearchloresLaboratory()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    launch_laboratory()
