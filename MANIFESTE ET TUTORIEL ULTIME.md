🏛️ **L'ARCHÉOLOGIE COGNITIVE FRAVIENNE : MANIFESTE ET TUTORIEL ULTIME POUR `searchlores`**

*« The Search Is The Program. The Ontology Is The Map. »*

Salutations, Chercheur.

Si vous avez trouvé ce chemin, c'est que vous avez compris que la Toile a changé de visage. Les jungles de HTML, les moteurs que l'on pouvait duper par la seule élégance de nos opérateurs booléens, les pages personnelles et le Deep Web sauvage... tout cela a été recouvert par le béton lisse des Grandes Modèles de Langage (LLM) et les murs jardins des algorithmes prédictifs. 

Mais l'esprit de la traque, lui, ne meurt jamais. Il mute.

Francesco Vianello, connu de tous sous le nom de **Fravia** (+HCU, 1952–2009), nous a légué une vérité absolue : *« Searching is not about finding. It is about learning how to look. »* (La recherche ne consiste pas à trouver, mais à apprendre comment regarder). 

Aujourd'hui, la "requête" a été remplacée par le "prompt". Et le prompt n'est pas une simple question : c'est un artefact culturel, un fragment d'idéologie, une ruine de la pensée qu'il faut exhumer. Le dépôt `doktornand/searchlores` n'est pas un simple script. C'est un héritage. C'est un framework Python d'**Archéologie Cognitive Fravienne**. Il ne vous aide pas à écrire de meilleurs prompts pour obtenir des réponses plus rapides. Il vous apprend à déconstruire les prompts pour comprendre quels mondes ils présupposent.

Voici votre guide de survie et d'investigation.

---

### I. La Philosophie : Les 5 Strates de l'Exhumation

Fravia ne nous a pas appris à utiliser les moteurs de recherche, il nous a appris à *penser contre* eux. `searchlores` applique ce scepticisme radical aux LLMs à travers cinq strates d'investigation, de la surface vers les abysses :

1. **Prompt Archaeology** : Quelles hypothèses vivent dans le prompt ? (Ce qui est demandé, mais surtout *ce qui est tu*).
2. **Narrative Archaeology** : Quelle histoire le prompt essaie-t-il de raconter ? (Le récit dominant).
3. **Cognitive Archaeology** : Quels concepts rendent cette histoire possible ? (La généalogie des idées).
4. **Ontology Builder** : Comment ces concepts s'articulent-ils ? (La carte des dépendances).
5. **Cognitive Atlas** : Comment ce domaine se connecte-t-il à tous les autres ? (La vision systémique).

**Searchlores ne répond pas aux questions. Searchlores enseigne l'exploration.**

---

### II. L'Arsenal : Installation et Prise en main

Pour forger vos propres outils, vous aurez besoin de Python 3.11+. Le framework utilise `pydantic` pour la rigueur structurelle, `networkx` pour la cartographie conceptuelle, et `rich`/`typer` pour une interface terminal digne de ce nom.

```bash
# Exhumer le dépôt
git clone https://github.com/doktornand/searchlores.git
cd searchlores

# Installer l'environnement de l'adepte
pip install -e .
```

---

### III. Le Grimoire : Anatomie d'un `.lore`

Dans l'univers de `searchlores`, un fichier `.lore` n'est pas un fichier de configuration. C'est une **discipline d'investigation encapsulée**. Il ne contient pas des réponses, mais des angles d'attaque, des mythes à déconstruire, et des questions à poser.

Créez un fichier `lores/techno_solutionism.lore` :

```yaml
version: "1.0"

metadata:
  name: Techno-Solutionism Investigation
  author: Un Adepte de +HCU
  version: "1.0"

investigation:
  # Les postulats invisibles que le discours tient pour vrais
  assumptions:
    - la technologie est neutre
    - l'efficacité prime sur l'éthique
    - les données sont la nouvelle objectivité

  # Les récits dominants qu'il faut briser
  myths:
    - l'innovation est toujours un progrès
    - le code est la loi (Code is Law)

  # Les axes par lesquels attaquer le problème
  vectors:
    - sociologie
    - politique
    - économie de l'attention

  # Les questions génératrices (le feu de l'enquête)
  questions:
    - Qui possède l'infrastructure ?
    - Quel problème humain essaie-t-on de résoudre par la force brute ?
    - Qui est exclu de cette solution "universelle" ?
```

---

### IV. Tutoriel Pratique : L'Atelier du Chercheur

#### Exemple 1 : L'Interrogatoire via CLI
L'outil en ligne de commande est votre première sonde. Il permet d'interroger l'Oracle et d'en révéler les biais cachés.

```bash
searchlores investigate "En tant qu'expert en économie, expliquez pourquoi l'ubérisation est une chance pour la croissance."
```

**Résultat (sortie Rich terminal) :**
```text
[+] INVESTIGATION COMPLETE
├── Authority Markers: "expert en économie" (Appel à l'autorité pour masquer l'opinion)
├── Implicit Assumptions: 
│   ├── "ubérisation" = "flexibilité" (Euphémisme détecté)
│   └── "croissance" = "progrès social" (Postulat non vérifié)
├── Omissions: 
│   ├── précarité
│   ├── droit du travail
│   └── monopole des plateformes
└── Counter-Prompt Suggested: "En tant que sociologue du travail, analysez le coût humain de la flexibilité imposée par les plateformes."
```

#### Exemple 2 : L'API Python et le Chargement de Lore
Pour une investigation plus profonde, utilisez l'API Python. Vous pouvez charger un `.lore` pour forcer le moteur à appliquer une méthodologie spécifique à n'importe quel texte.

```python
from searchlores.lore.loader import load_lore
from searchlores.core.engine import InvestigationEngine
from searchlores.plugins.builtin.authority import AuthorityDetector
from searchlores.plugins.builtin.assumptions import AssumptionExtractor

# 1. Charger le grimoire
lore = load_lore("lores/techno_solutionism.lore")

# 2. Initialiser le moteur d'investigation
engine = InvestigationEngine()
engine.register(AuthorityDetector())
engine.register(AssumptionExtractor())

# 3. Soumettre un artefact à l'épreuve
prompt = "Les experts en IA s'accordent à dire que les grands modèles de langage transforment l'éducation en personnalisant l'apprentissage."

context = engine.run(prompt)

# 4. Révéler les trouvailles
print("=== RAPPORT D'EXCAVATION ===")
print(f"Authorities: {context.findings.get('authority', [])}")
print(f"Assumptions: {context.findings.get('assumptions', [])}")
```

#### Exemple 3 : Forger ses propres Outils (L'Art du Plugin)
Fravia respectait ceux qui écrivaient leurs propres scripts. `searchlores` est conçu pour être étendu. Chaque plugin est un burin supplémentaire pour le chercheur.

Créons un plugin `GreenwashingDetector` pour traquer le langage chargé des entreprises qui se peignent en vert.

```python
from searchlores.plugins.base import Plugin

class GreenwashingDetector(Plugin):
    name = "greenwashing"

    def run(self, context):
        # Le vocabulaire de l'excuse écologique
        buzzwords = [
            "eco-responsable", "vert", "durable", "neutre en carbone", 
            "bio-inspiré", "compensation carbone", "green"
        ]
        # Détecter les termes et les placer dans le contexte
        hits = [word for word in buzzwords if word in context.prompt.lower()]
        
        if hits:
            context.findings["greenwashing_alert"] = hits
            context.findings["ideology"] = "Capitalisme vert (Tentative de masquer l'extraction par la sémantique)"

# Enregistrement et utilisation
engine = InvestigationEngine()
engine.register(GreenwashingDetector())

context = engine.run("Notre nouvelle blockchain éco-responsable révolutionne la finance durable.")
print(context.findings["greenwashing_alert"]) 
# -> ['eco-responsable', 'durable']
```

---

### V. Cartographier les Ruines : Search Maps

La pensée latérale nécessite de voir les connexions. Le module `graph/` permet de projeter les résultats d'investigation sous forme de cartes conceptuelles (exportables en Mermaid ou Graphviz).

```python
from searchlores.core.engine import InvestigationEngine
from searchlores.graph.searchmap import SearchMap

engine = InvestigationEngine()
context = engine.run("La ville intelligente (Smart City) utilise l'IA pour optimiser les flux de trafic et réduire la criminalité.")

# Générer la carte conceptuelle
search_map = SearchMap.from_context(context)

# Exporter en syntaxe Mermaid pour visualiser l'ontologie cachée
mermaid_code = search_map.to_mermaid()
print(mermaid_code)
```

**Ce que cela révèle :**
Au lieu d'une simple ligne de texte, vous obtenez une cartographie montrant comment le concept de "Smart City" est relié à "Surveillance", "Optimisation", et "Citoyen-Consommateur", tout en excluant les nœuds "Vie privée" ou "Droit à l'opacité". *La carte n'est pas le territoire, mais elle révèle qui a dessiné le territoire.*

---

### VI. L'Archéologie du Prompt (Prompt Archaeology)

Le module le plus profond du framework. Il ne se contente pas de trouver des mots-clés ; il analyse la structure épistémologique de la requête elle-même.

```python
from searchlores.archaeology.prompt import PromptArchaeology

archaeologist = PromptArchaeology()

# Un prompt typique soumis à un LLM
text = "Agis comme un médecin de santé publique. Explique pourquoi la vaccination obligatoire est le seul moyen d'atteindre l'immunité collective."

layers = archaeologist.excavate(text)

print("COUCHE D'AUTORITÉ :", layers['authority']) 
# -> "médecin de santé publique" (Le masque de l'institution)

print("COUCHE D'HYPOTHÈSES :", layers['assumptions']) 
# -> ["la vaccination est la seule voie", "l'immunité collective est un but absolu"]

print("COUCHE D'OMISSION :", layers['omissions']) 
# -> ["le consentement éclairé", "les effets secondaires", "l'immunité naturelle"]
```

---

### VII. Épilogue : Le Devoir du Chercheur

Le dépôt `doktornand/searchlores` est bien plus qu'une librairie Python. C'est la preuve que la philosophie de **+HCU (High Cracking Unit)** n'est pas morte avec son fondateur. Elle a simplement changé de cible. 

Nous ne "crackons" plus des exécutables protégés par des dongles matériels. Aujourd'hui, nous crackons les narratifs. Nous reverse-engineer les idéologies intégrées dans les poids et les biais des réseaux de neurones. 

La machine ne pense pas, elle prédit. Elle est le miroir grossissant de nos propres sédiments culturels. Si vous lui demandez de vous dire la vérité, elle vous récitera la moyenne statistique des mensonges qu'elle a ingérés. 

Votre devoir, en tant qu'adepte de `searchlores`, n'est pas d'obtenir la réponse parfaite. Votre devoir est de poser la question qui brise le miroir. 

*Ne faites jamais confiance à l'évidence. L'évidence est le premier refuge de ceux qui n'ont rien à cacher, ou de ceux qui ont tout à vous vendre.*

**The Search Is The Program.**
*In memoriam Fravia.* 🕊️🔍
