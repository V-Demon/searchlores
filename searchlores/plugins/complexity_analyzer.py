"""
Analyseur de complexité structurelle pour Searchlores
Mesure la complexité des graphes conceptuels et ontologiques
"""

import networkx as nx
from typing import Dict, List, Optional

class ComplexityAnalyzer:
    """Analyse la complexité structurelle des graphes conceptuels"""
    
    def __init__(self):
        pass
    
    def calculate_cyclomatic_complexity(self, graph: nx.DiGraph) -> int:
        """
        Complexité cyclomatique adaptée aux concepts
        M = E - N + 2P
        où E = arêtes, N = nœuds, P = composantes faiblement connexes
        
        Mesure le nombre de "chemins cognitifs indépendants"
        """
        if graph.number_of_nodes() == 0:
            return 0
        
        E = graph.number_of_edges()
        N = graph.number_of_nodes()
        P = nx.number_weakly_connected_components(graph)
        
        return E - N + 2 * P
    
    def calculate_conceptual_density(self, graph: nx.DiGraph) -> float:
        """
        Densité conceptuelle : ratio arêtes / nœuds
        Mesure la richesse des connexions conceptuelles
        """
        if graph.number_of_nodes() == 0:
            return 0.0
        
        return graph.number_of_edges() / graph.number_of_nodes()
    
    def calculate_average_path_length(self, graph: nx.DiGraph) -> float:
        """
        Longueur moyenne des plus courts chemins
        Mesure la "distance cognitive moyenne" entre concepts
        """
        if graph.number_of_nodes() <= 1:
            return 0.0
        
        try:
            # Convertir en graphe non-orienté pour les chemins
            undirected = graph.to_undirected()
            return nx.average_shortest_path_length(undirected)
        except nx.NetworkXError:
            return 0.0
    
    def calculate_clustering_coefficient(self, graph: nx.DiGraph) -> float:
        """
        Coefficient de clustering moyen
        Mesure la tendance des concepts à former des clusters
        """
        if graph.number_of_nodes() == 0:
            return 0.0
        
        undirected = graph.to_undirected()
        return nx.average_clustering(undirected)
    
    def find_pivot_concepts(self, graph: nx.DiGraph, top_n: int = 5) -> Dict[str, float]:
        """
        Identifie les concepts pivots via betweenness centrality
        Retourne les top_n concepts avec leur score de centralité
        """
        if graph.number_of_nodes() == 0:
            return {}
        
        centrality = nx.betweenness_centrality(graph)
        
        # Trier par centralité décroissante
        sorted_concepts = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
        
        return dict(sorted_concepts[:top_n])
    
    def calculate_hierarchical_depth(self, graph: nx.DiGraph) -> int:
        """
        Profondeur hiérarchique maximale du graphe
        Mesure la complexité de la structure hiérarchique
        """
        if graph.number_of_nodes() == 0:
            return 0
        
        try:
            # Trouver les nœuds sources (pas de prédécesseurs)
            sources = [n for n in graph.nodes() if graph.in_degree(n) == 0]
            
            if not sources:
                # Si pas de sources, prendre un nœud arbitraire
                sources = [list(graph.nodes())[0]]
            
            max_depth = 0
            for source in sources:
                try:
                    lengths = nx.single_source_shortest_path_length(graph, source)
                    max_depth = max(max_depth, max(lengths.values()) if lengths else 0)
                except nx.NetworkXError:
                    continue
            
            return max_depth
        except Exception:
            return 0
    
    def analyze(self, graph: nx.DiGraph) -> dict:
        """
        Analyse complète de la complexité d'un graphe conceptuel
        
        Returns:
            dict avec toutes les métriques de complexité
        """
        return {
            'cyclomatic_complexity': self.calculate_cyclomatic_complexity(graph),
            'conceptual_density': self.calculate_conceptual_density(graph),
            'average_path_length': self.calculate_average_path_length(graph),
            'clustering_coefficient': self.calculate_clustering_coefficient(graph),
            'hierarchical_depth': self.calculate_hierarchical_depth(graph),
            'pivot_concepts': self.find_pivot_concepts(graph)
        }
