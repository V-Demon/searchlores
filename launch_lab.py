# launch_lab.py
#!/usr/bin/env python3
"""
🎛️ Searchlores Laboratory — Lanceur
Le synthétiseur épistémologique pour bidouiller au feeling

Inspiré par :
  • Fravia+ — L'archéologie cognitive des prompts
  • Syd Barrett — La bidouille au feeling sur synthés analogiques
  • Le chou Romanesco — Les fractales qui se pensent elles-mêmes

Usage :
  python launch_lab.py
"""

import sys
import os
from pathlib import Path

# Ajouter le répertoire courant au path
sys.path.insert(0, str(Path(__file__).parent))

# Vérifier les dépendances
def check_dependencies():
    """Vérifie que toutes les dépendances sont installées"""
    missing = []

    try:
        import PyQt5
    except ImportError:
        missing.append("PyQt5")

    try:
        import matplotlib
    except ImportError:
        missing.append("matplotlib")

    try:
        import networkx
    except ImportError:
        missing.append("networkx")

    try:
        import searchlores
    except ImportError:
        missing.append("searchlores (le package lui-même)")

    if missing:
        print("❌ Dépendances manquantes :")
        for dep in missing:
            print(f"   • {dep}")
        print("\nInstallez-les avec :")
        print("   pip install PyQt5 matplotlib networkx")
        sys.exit(1)


def print_banner():
    """Affiche la bannière du laboratoire"""
    banner = """
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║   🎛️  SEARCHLORES LABORATORY — Le Synthétiseur Épistémologique   ║
║                                                                   ║
║   "The Search Is The Program. The Lore Is The Map."              ║
║   — In memoriam Fravia (1952–2009)                               ║
║                                                                   ║
║   🎸 Bidouille au feeling comme Syd Barrett sur son VCS3         ║
║   🥬 Les investigations sont des choux Romanesco fractaux        ║
║   💾 Le code est la donnée. La donnée est le code.               ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
    """
    print(banner)


def main():
    """Point d'entrée principal"""
    print_banner()
    check_dependencies()

    print("🔧 Initialisation du laboratoire...")

    # Importer et lancer la GUI
    from searchlores.gui.main_window import launch_laboratory

    print("🚀 Lancement de l'interface graphique...")
    print("💡 Branchez vos prompts, sélectionnez vos Lores et Plugins, et explorez !")
    print()

    launch_laboratory()


if __name__ == "__main__":
    main()
