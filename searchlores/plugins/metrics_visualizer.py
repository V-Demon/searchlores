"""
Visualiseur de métriques pour Searchlores
Affichage Feng-Shui des analyses d'entropie et de complexité
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich import box
from typing import Dict, List

class MetricsVisualizer:
    """Visualisation élégante des métriques cognitives"""
    
    def __init__(self):
        self.console = Console()
    
    def create_gauge(self, value: float, max_value: float, label: str, color: str = "green") -> str:
        """Crée une jauge visuelle pour une métrique"""
        percentage = min(100, (value / max_value) * 100)
        filled = int(percentage / 5)
        empty = 20 - filled
        
        bar = "█" * filled + "░" * empty
        return f"[{color}]{label}: [{bar}] {value:.2f}[/{color}]"
    
    def display_entropy_metrics(self, metrics: dict):
        """Affiche les métriques d'entropie de manière élégante"""
        self.console.print("\n")
        self.console.print(Panel(
            "[bold cyan]📊 ANALYSE D'ENTROPIE INFORMATIONNELLE[/bold cyan]",
            box=box.ROUNDED,
            border_style="cyan"
        ))
        
        # Jauge d'entropie
        entropy = metrics['token_entropy']
        entropy_color = "green" if entropy < 3.0 else "yellow" if entropy < 5.0 else "red"
        self.console.print(self.create_gauge(entropy, 8.0, "Entropie", entropy_color))
        
        # Jauge de diversité lexicale
        ttr = metrics['type_token_ratio']
        self.console.print(self.create_gauge(ttr, 1.0, "Diversité Lexicale", "magenta"))
        
        # Jauge de densité lexicale
        density = metrics['lexical_density']
        self.console.print(self.create_gauge(density, 1.0, "Densité Lexicale", "blue"))
        
        # Statistiques
        self.console.print(f"\n[bold]Tokens uniques:[/bold] {metrics['unique_tokens']}")
        self.console.print(f"[bold]Total tokens:[/bold] {metrics['total_tokens']}")
        
        # Niveau qualitatif
        level = "FAIBLE" if entropy < 3.0 else "MODÉRÉE" if entropy < 5.0 else "ÉLEVÉE"
        level_color = "green" if entropy < 3.0 else "yellow" if entropy < 5.0 else "red"
        self.console.print(f"\n[bold {level_color}]Niveau d'entropie: {level}[/bold {level_color}]")
    
    def display_complexity_metrics(self, metrics: dict):
        """Affiche les métriques de complexité de manière élégante"""
        self.console.print("\n")
        self.console.print(Panel(
            "[bold magenta]🧠 ANALYSE DE COMPLEXITÉ STRUCTURELLE[/bold magenta]",
            box=box.ROUNDED,
            border_style="magenta"
        ))
        
        # Complexité cyclomatique
        cc = metrics['cyclomatic_complexity']
        cc_color = "green" if cc < 5 else "yellow" if cc < 15 else "red"
        self.console.print(f"[bold {cc_color}]Complexité Cyclomatique:[/bold {cc_color}] {cc}")
        
        # Densité conceptuelle
        density = metrics['conceptual_density']
        self.console.print(self.create_gauge(density, 3.0, "Densité Conceptuelle", "cyan"))
        
        # Longueur des chemins
        path_length = metrics['average_path_length']
        self.console.print(f"[bold]Longueur Moyenne des Chemins:[/bold] {path_length:.3f}")
        
        # Coefficient de clustering
        clustering = metrics['clustering_coefficient']
        self.console.print(self.create_gauge(clustering, 1.0, "Coefficient de Clustering", "green"))
        
        # Profondeur hiérarchique
        depth = metrics['hierarchical_depth']
        self.console.print(f"[bold]Profondeur Hiérarchique:[/bold] {depth}")
        
        # Concepts pivots
        if metrics['pivot_concepts']:
            self.console.print("\n[bold yellow]🎯 Concepts Pivots (Betweenness Centrality):[/bold yellow]")
            for concept, centrality in metrics['pivot_concepts'].items():
                bar_length = int(centrality * 50)
                bar = "▓" * bar_length + "░" * (50 - bar_length)
                self.console.print(f"  [cyan]{concept}:[/cyan] [{bar}] {centrality:.3f}")
    
    def display_comparison(self, analyses: List[Dict[str, dict]]):
        """Compare plusieurs analyses dans un tableau"""
        self.console.print("\n")
        self.console.print(Panel(
            "[bold green]📈 COMPARAISON INTER-PROMPTS[/bold green]",
            box=box.ROUNDED,
            border_style="green"
        ))
        
        table = Table(box=box.ROUNDED, show_header=True, header_style="bold cyan")
        table.add_column("Prompt", style="cyan", no_wrap=True)
        table.add_column("Entropie", justify="right", style="magenta")
        table.add_column("Diversité", justify="right", style="blue")
        table.add_column("Densité", justify="right", style="green")
        table.add_column("Complexité", justify="right", style="yellow")
        
        for analysis in analyses:
            name = analysis['name']
            entropy = analysis['entropy']
            complexity = analysis.get('complexity', {})
            
            table.add_row(
                name,
                f"{entropy['token_entropy']:.2f}",
                f"{entropy['type_token_ratio']:.3f}",
                f"{entropy['lexical_density']:.3f}",
                f"{complexity.get('cyclomatic_complexity', 'N/A')}"
            )
        
        self.console.print(table)
    
    def display_summary(self, entropy_metrics: dict, complexity_metrics: dict = None):
        """Affiche un résumé complet"""
        self.display_entropy_metrics(entropy_metrics)
        if complexity_metrics:
            self.display_complexity_metrics(complexity_metrics)
