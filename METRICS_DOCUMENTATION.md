# 📚 SEARCHLORES METRICS - Documentation Complète

## 🎯 Philosophie : De l'Analyse Qualitative à l'Épistémologie Quantitative

**Searchlores Metrics** transforme l'analyse cognitive des prompts d'une discipline purement qualitative en une **science forensique computationnelle**. Inspiré par l'héritage de Fravia+ et sa "Search Art", ce module apporte une rigueur mathématique à l'exploration des strates de pensée.

> *"Mesurer l'entropie d'un prompt, c'est comme peser une étoile : on ne voit pas la masse, mais on en déduit la nature."*

---

## 🧪 Nouvelles Fonctionnalités

### 1. 📊 **Analyse d'Entropie Informationnelle**

Mesure la diversité, l'incertitude et la richesse informationnelle des textes.

#### Métriques Disponibles

| Métrique | Description | Interprétation |
|----------|-------------|----------------|
| **Token Entropy** | Entropie de Shannon sur la distribution des tokens | Faible (<3) = focalisé, Élevée (>5) = diversifié |
| **Type-Token Ratio** | Ratio types uniques / total tokens | Diversité lexicale (0-1) |
| **Lexical Density** | Proportion de mots lexicaux (non-stopwords) | Densité informationnelle |

#### Exemple d'Utilisation

```python
from lore.plugins import EntropyAnalyzer

analyzer = EntropyAnalyzer()
metrics = analyzer.analyze("Votre texte à analyser...")

print(f"Entropie: {metrics['token_entropy']:.2f} bits")
print(f"Diversité: {metrics['type_token_ratio']:.3f}")
print(f"Densité: {metrics['lexical_density']:.3f}")
```

#### Cas d'Usage

- **Prompt Archaeology** : Identifier les prompts à haute exploration conceptuelle
- **Contradiction Detection** : Détecter les zones de tension logique (pics d'entropie)
- **Optimisation** : Équilibrer la diversité conceptuelle dans les prompts

---

### 2. 🧠 **Analyse de Complexité Structurelle**

Mesure la complexité des graphes conceptuels et ontologiques via la théorie des graphes.

#### Métriques Disponibles

| Métrique | Formule | Signification |
|----------|---------|---------------|
| **Cyclomatic Complexity** | M = E - N + 2P | Nombre de chemins cognitifs indépendants |
| **Conceptual Density** | Arêtes / Nœuds | Richesse des connexions conceptuelles |
| **Average Path Length** | Moyenne des plus courts chemins | Distance cognitive moyenne |
| **Clustering Coefficient** | Coefficient de clustering moyen | Tendance à former des clusters |
| **Hierarchical Depth** | Profondeur maximale | Complexité hiérarchique |
| **Pivot Concepts** | Betweenness centrality | Concepts structuraux pivots |

#### Exemple d'Utilisation

```python
from lore.plugins import ComplexityAnalyzer
import networkx as nx

analyzer = ComplexityAnalyzer()

# Créer un graphe conceptuel
graph = nx.DiGraph()
graph.add_edges_from([
    ("Quantum Mechanics", "Epistemology"),
    ("Observation", "Wave Function"),
    ("Wave Function", "Measurement Problem"),
    ("Consciousness", "Observation"),
])

metrics = analyzer.analyze(graph)

print(f"Complexité cyclomatique: {metrics['cyclomatic_complexity']}")
print(f"Densité conceptuelle: {metrics['conceptual_density']:.3f}")
print(f"Concepts pivots: {metrics['pivot_concepts']}")
```

#### Cas d'Usage

- **Cognitive Atlas** : Cartographier la densité entre domaines de connaissance
- **Ontology Builder** : Identifier les concepts pivots dans une ontologie
- **Anomaly Detection** : Détecter les zones de complexité anormale

---

### 3. 🎨 **Visualisation Feng-Shui**

Affichage élégant et coloré des métriques dans le terminal avec Rich.

#### Composants Visuels

- **Jauges colorées** : Gradient vert/jaune/rouge selon les seuils
- **Tableaux comparatifs** : Comparaison inter-prompts
- **Barres de progression** : Visualisation des concepts pivots
- **Panels arrondis** : Interface soignée et lisible

#### Exemple d'Utilisation

```python
from lore.plugins import MetricsVisualizer

visualizer = MetricsVisualizer()

# Afficher les métriques d'entropie
visualizer.display_entropy_metrics(entropy_metrics)

# Afficher les métriques de complexité
visualizer.display_complexity_metrics(complexity_metrics)

# Comparer plusieurs prompts
visualizer.display_comparison([
    {'name': 'Prompt 1', 'entropy': metrics1, 'complexity': {}},
    {'name': 'Prompt 2', 'entropy': metrics2, 'complexity': {}},
])
```

---

## 🔬 Analyse Combinée

Combine entropie et complexité pour une analyse épistémologique complète.

```python
from lore.plugins import EntropyAnalyzer, ComplexityAnalyzer, MetricsVisualizer
import networkx as nx

# Analyse d'entropie
entropy_analyzer = EntropyAnalyzer()
entropy_metrics = entropy_analyzer.analyze(texte_complexe)

# Analyse de complexité
complexity_analyzer = ComplexityAnalyzer()
graph = nx.DiGraph()
graph.add_edges_from([...])  # Votre graphe conceptuel
complexity_metrics = complexity_analyzer.analyze(graph)

# Visualisation combinée
visualizer = MetricsVisualizer()
visualizer.display_summary(entropy_metrics, complexity_metrics)
```

---

## 📈 Interprétation des Métriques

### Niveaux d'Entropie

| Niveau | Entropie | Interprétation |
|--------|----------|----------------|
| 🟢 **FAIBLE** | < 3.0 bits | Texte focalisé, vocabulaire restreint |
| 🟡 **MODÉRÉE** | 3.0 - 5.0 bits | Équilibre entre focalisation et diversité |
| 🔴 **ÉLEVÉE** | > 5.0 bits | Grande diversité conceptuelle, exploration large |

### Niveaux de Complexité

| Niveau | Complexité Cyclomatique | Interprétation |
|--------|-------------------------|----------------|
| 🟢 **SIMPLE** | < 5 | Structure linéaire, peu de chemins alternatifs |
| 🟡 **MODÉRÉE** | 5 - 15 | Structure ramifiée, chemins multiples |
| 🔴 **COMPLEXE** | > 15 | Structure hautement interconnectée |

---

## 🎯 Applications Avancées

### 1. Détection d'Anomalies Cognitives

```python
def detect_anomalies(entropy_values: list) -> list:
    """Détecte les pics d'entropie anormaux"""
    import numpy as np
    
    mean = np.mean(entropy_values)
    std = np.std(entropy_values)
    
    anomalies = []
    for i, value in enumerate(entropy_values):
        z_score = (value - mean) / std
        if abs(z_score) > 2:  # Déviation de 2 écarts-types
            anomalies.append({
                'index': i,
                'value': value,
                'z_score': z_score,
                'type': 'SPIKE' if z_score > 0 else 'DROP'
            })
    
    return anomalies
```

### 2. Optimisation de Prompts

```python
def optimize_prompt(target_entropy: float = 4.0, max_iterations: int = 10):
    """Optimise un prompt pour atteindre une entropie cible"""
    analyzer = EntropyAnalyzer()
    
    # Algorithme d'optimisation (exemple simplifié)
    current_prompt = "Votre prompt initial..."
    
    for i in range(max_iterations):
        metrics = analyzer.analyze(current_prompt)
        current_entropy = metrics['token_entropy']
        
        if abs(current_entropy - target_entropy) < 0.5:
            break
        
        # Ajuster le prompt (logique d'optimisation à implémenter)
        # ...
    
    return current_prompt
```

### 3. Cartographie Épistémologique

```python
def map_epistemological_landscape(prompts: dict) -> dict:
    """Cartographie la densité cognitive entre différents domaines"""
    analyzer = EntropyAnalyzer()
    
    landscape = {}
    for domain, prompt in prompts.items():
        metrics = analyzer.analyze(prompt)
        landscape[domain] = {
            'entropy': metrics['token_entropy'],
            'density': metrics['lexical_density'],
            'diversity': metrics['type_token_ratio']
        }
    
    return landscape
```

---

## 🚀 Intégration dans Searchlores

### Extension du Modèle Pydantic

Ajouter dans `lore/models.py` :

```python
class Investigation(BaseModel):
    # ... champs existants ...
    entropy_metrics: Optional[EntropyMetrics] = None
    complexity_metrics: Optional[ComplexityMetrics] = None
```

### Plugin d'Intégration

Créer `lore/plugins/metrics_plugin.py` :

```python
from lore.models import Investigation, EntropyMetrics, ComplexityMetrics
from .entropy_analyzer import EntropyAnalyzer
from .complexity_analyzer import ComplexityAnalyzer

class MetricsPlugin:
    """Plugin qui enrichit les investigations avec des métriques quantitatives"""
    
    def __init__(self):
        self.entropy_analyzer = EntropyAnalyzer()
        self.complexity_analyzer = ComplexityAnalyzer()
    
    def process(self, investigation: Investigation) -> Investigation:
        # Analyser chaque strate
        for layer in investigation.layers:
            entropy = self.entropy_analyzer.analyze(layer.content)
            layer.entropy_metrics = EntropyMetrics(**entropy)
        
        # Analyser l'ontologie globale
        if investigation.cognitive_atlas:
            complexity = self.complexity_analyzer.analyze(
                investigation.cognitive_atlas
            )
            investigation.complexity_metrics = ComplexityMetrics(**complexity)
        
        return investigation
```

---

## 📦 Installation

```bash
# Installer les dépendances
pip install rich networkx numpy

# Vérifier l'installation
python demo.py
```

---

## 🎸 Exemple Complet : Session d'Exploration

```python
#!/usr/bin/env python3
"""Session d'exploration cognitive avec Searchlores Metrics"""

from lore.plugins import (
    EntropyAnalyzer, 
    ComplexityAnalyzer, 
    MetricsVisualizer
)
import networkx as nx

# 1. Analyser un prompt complexe
prompt = """
Analyze the epistemological implications of quantum mechanics,
considering the measurement problem, the role of consciousness,
and the many-worlds interpretation.
"""

entropy_analyzer = EntropyAnalyzer()
entropy = entropy_analyzer.analyze(prompt)

# 2. Construire un graphe conceptuel
graph = nx.DiGraph()
graph.add_edges_from([
    ("Quantum Mechanics", "Epistemology"),
    ("Measurement Problem", "Quantum Mechanics"),
    ("Consciousness", "Observation"),
    ("Many Worlds", "Quantum Mechanics"),
    ("Observation", "Measurement Problem"),
])

complexity_analyzer = ComplexityAnalyzer()
complexity = complexity_analyzer.analyze(graph)

# 3. Visualiser les résultats
visualizer = MetricsVisualizer()
visualizer.display_summary(entropy, complexity)

# 4. Identifier les concepts pivots
print("\n🎯 Concepts Pivots:")
for concept, centrality in complexity['pivot_concepts'].items():
    print(f"  • {concept}: {centrality:.3f}")
```

---

## 🔮 Extensions Futures

- [ ] **Entropie Sémantique** : Via embeddings et similarité cosinus
- [ ] **Analyse Temporelle** : Évolution des métriques à travers les strates
- [ ] **Visualisations Interactives** : NetworkX + Plotly pour graphes 3D
- [ ] **Machine Learning** : Prédiction de la "profondeur cognitive"
- [ ] **Base de Données** : Stockage et comparaison de métriques historiques

---

## 📖 Références

- **Fravia+** : L'héritage de la "Search Art" et de l'investigation cognitive
- **Shannon, C.E. (1948)** : "A Mathematical Theory of Communication"
- **McCabe, T.J. (1976)** : "A Complexity Measure" (complexité cyclomatique)
- **NetworkX** : Documentation officielle https://networkx.org/

---

## 🍵 Crédits

Développé avec un Lapsang Souchong fumé et "A Saucerful of Secrets" en fond sonore. 🎸

*"The measure of intelligence is the ability to change."* — Albert Einstein

---
