#!/usr/bin/env python3
"""
Démonstration des analyses d'entropie et de complexité pour Searchlores
"""

import networkx as nx
from plugins.entropy_analyzer import EntropyAnalyzer
from plugins.complexity_analyzer import ComplexityAnalyzer
from plugins.metrics_visualizer import MetricsVisualizer

def demo_entropy_analysis():
    """Démonstration de l'analyse d'entropie"""
    analyzer = EntropyAnalyzer()
    visualizer = MetricsVisualizer()
    
    # Exemples de prompts avec différentes caractéristiques
    prompts = {
        "Simple": "What is AI?",
        "Modéré": "Explain the concept of artificial intelligence and its applications in modern society",
        "Complexe": "Analyze the epistemological implications of large language models, considering their training on vast corpora of human knowledge, their tendency to reproduce cognitive biases, and their potential to reshape our understanding of intelligence itself. How do these systems challenge traditional notions of authorship, creativity, and knowledge production?"
    }
    
    analyses = []
    
    for name, prompt in prompts.items():
        metrics = analyzer.analyze(prompt)
        analyses.append({
            'name': name,
            'entropy': metrics,
            'text': prompt
        })
    
    # Afficher l'analyse du prompt complexe
    visualizer.display_summary(analyses[2]['entropy'])
    
    # Comparaison
    visualizer.display_comparison(analyses)

def demo_complexity_analysis():
    """Démonstration de l'analyse de complexité sur un graphe"""
    analyzer = ComplexityAnalyzer()
    visualizer = MetricsVisualizer()
    
    # Création d'un graphe conceptuel exemple
    graph = nx.DiGraph()
    
    # Ajout de concepts et relations
    concepts = [
        ("Quantum Mechanics", "Physics"),
        ("Wave Function", "Quantum Mechanics"),
        ("Superposition", "Quantum Mechanics"),
        ("Entanglement", "Quantum Mechanics"),
        ("Observation", "Wave Function"),
        ("Copenhagen Interpretation", "Quantum Mechanics"),
        ("Many Worlds", "Quantum Mechanics"),
        ("Decoherence", "Quantum Mechanics"),
        ("Physics", "Science"),
        ("Epistemology", "Philosophy"),
        ("Observation", "Epistemology"),
    ]
    
    graph.add_edges_from(concepts)
    
    # Analyse
    metrics = analyzer.analyze(graph)
    
    # Affichage
    visualizer.display_complexity_metrics(metrics)

def demo_combined():
    """Démonstration combinée"""
    entropy_analyzer = EntropyAnalyzer()
    complexity_analyzer = ComplexityAnalyzer()
    visualizer = MetricsVisualizer()
    
    # Analyse d'un texte complexe
    complex_text = """
    The intersection of quantum mechanics and epistemology reveals profound questions 
    about the nature of observation and knowledge. When we consider wave function collapse, 
    we encounter the measurement problem: does observation create reality, or merely reveal it? 
    This connects to broader philosophical questions about consciousness, determinism, and the 
    limits of human understanding. The many-worlds interpretation offers one resolution, 
    suggesting that all possibilities are realized in branching universes, while decoherence 
    theory provides a physical mechanism for the appearance of collapse without invoking 
    conscious observers.
    """
    
    entropy_metrics = entropy_analyzer.analyze(complex_text)
    
    # Création d'un graphe conceptuel basé sur le texte
    graph = nx.DiGraph()
    graph.add_edges_from([
        ("Quantum Mechanics", "Epistemology"),
        ("Observation", "Wave Function"),
        ("Wave Function", "Measurement Problem"),
        ("Consciousness", "Observation"),
        ("Many Worlds", "Quantum Mechanics"),
        ("Decoherence", "Quantum Mechanics"),
        ("Determinism", "Epistemology"),
    ])
    
    complexity_metrics = complexity_analyzer.analyze(graph)
    
    # Affichage combiné
    visualizer.display_summary(entropy_metrics, complexity_metrics)

if __name__ == "__main__":
    print("\n" + "="*80)
    print("🎸 SEARCHLORES METRICS DEMO - A Saucerful of Secrets Edition 🎸")
    print("="*80 + "\n")
    
    print("\n📊 DÉMONSTRATION 1: Analyse d'Entropie")
    print("-" * 80)
    demo_entropy_analysis()
    
    print("\n\n🧠 DÉMONSTRATION 2: Analyse de Complexité")
    print("-" * 80)
    demo_complexity_analysis()
    
    print("\n\n🔬 DÉMONSTRATION 3: Analyse Combinée")
    print("-" * 80)
    demo_combined()
    
    print("\n\n" + "="*80)
    print("✨ Démo terminée ! Profitez bien de votre Lapsang Souchong ! 🍵")
    print("="*80 + "\n")
