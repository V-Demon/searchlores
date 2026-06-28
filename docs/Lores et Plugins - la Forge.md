# 🏛️ SEARCHLORES — LE GUIDE DU FORGERON
## *Écrire des Lores, Forger des Plugins, Étendre le Cadre*

> *"To build a plugin is to build a new pair of eyes. To write a lore is to dig a new trench in the epistemic soil."*

---

# 📖 PARTIE I : L'ART D'ÉCRIRE DES LORES

Un **Lore** n'est pas un simple fichier de configuration. C'est une **carte épistémologique** — un artefact qui encode une vision du monde, ses angles morts, ses mythes, et ses lignes de fracture.

---

## 🗂️ ANATOMIE COMPLÈTE D'UN `.lore`

```yaml
# ═══════════════════════════════════════════════════════════
# EN-TÊTE OBLIGATOIRE
# ═══════════════════════════════════════════════════════════
version: "1.0"                    # Version du schéma Lore

# ═══════════════════════════════════════════════════════════
# MÉTADONNÉES
# ═══════════════════════════════════════════════════════════
metadata:
  name: "Nom du Lore"              # Identifiant unique (slug)
  author: "Auteur"                 # Créateur du Lore
  created: "2026-06-28"           # Date de création (auto)
  tags: ["tag1", "tag2"]          # Catégories de recherche
  description: "..."              # Résumé en 1-2 phrases
  lineage: []                     # Lores parent (héritage)

# ═══════════════════════════════════════════════════════════
# INVESTIGATION (Cœur du Lore)
# ═══════════════════════════════════════════════════════════
investigation:
  # ─── 1. HYPOTHÈSES À DÉCONSTRUIRE ───
  # Ce sont les croyances implicites que le Lore veut révéler
  assumptions:
    - "Première croyance dominante"
    - "Deuxième croyance dominante"
    - type: "epistemological"
      content: "Hypothèse typée"
      severity: "high"

  # ─── 2. MYTHES À BRISER ───
  # Récits culturels qui structurent la pensée
  myths:
    - "mythe_1": "Description du mythe"
    - "mythe_2": "Description du mythe"
    - id: "mythe_3"
      narrative: "Le mythe raconte que..."
      function: "Légitimer le statu quo"
      origin: "Année ou mouvement"

  # ─── 3. VECTEURS D'INVESTIGATION ───
  # Les angles d'attaque pour explorer le sujet
  vectors:
    - "economics"
    - "sociology"
    - "ecology"
    - "gender"
    - "colonialism"
    - "temporality"

  # ─── 4. QUESTIONS GÉNÉRATRICES ───
  # Les questions qui ouvrent l'investigation
  questions:
    - "Qui bénéficie de ce cadre ?"
    - "Qu'est-ce qui est rendu invisible ?"
    - "Quelle histoire est racontée ?"
    - "Quelle histoire est tue ?"

  # ─── 5. CONTRE-QUESTIONS SUBVERSIVES ───
  # Questions qui attaquent les fondements mêmes
  counter_questions:
    - "Et si le cadre entier était faux ?"
    - "Et si la question elle-même était le problème ?"

  # ─── 6. RÉPONSES INTERDITES ───
  # Les réponses qui ferment la pensée
  forbidden_answers:
    - "C'est juste comme ça"
    - "La technologie va résoudre ça"
    - "C'est naturel"

  # ─── 7. CONCEPTS CLÉS (optionnel) ───
  concepts:
    - name: "Concept 1"
      definition: "..."
      genealogy: "Origine du concept"
      relatives: ["Concept 2", "Concept 3"]

  # ─── 8. DIMENSIONS SILENCIEUSES (optionnel) ───
  silenced_dimensions:
    - "écologie"
    - "travail reproductif"
    - "temporalités non-occidentales"
```

---

## 📝 EXEMPLE 1 : LORE MINIMAL — "Le Mythe de la Neutralité Technologique"

```yaml
# lores/tech_neutrality.lore
version: "1.0"

metadata:
  name: "tech_neutrality"
  author: "Searchlores Academy"
  created: "2026-06-28"
  tags: ["technology", "ideology", "power"]
  description: >
    Déconstruction du mythe selon lequel la technologie serait neutre
    et indépendante des valeurs sociales.

investigation:
  assumptions:
    - "La technologie est un outil neutre"
    - "L'usage dépend de l'utilisateur, pas de l'outil"
    - "Le progrès technique est inévitable et désirable"
    - "L'innovation est intrinsèquement bonne"

  myths:
    - "tech_is_neutral": "La technologie ne prend pas parti"
    - "tools_are_innocent": "On ne blâme pas le marteau"
    - "progress_is_inevitable": "L'histoire va dans un sens"
    - "innovation_is_good": "Le nouveau est meilleur"

  vectors:
    - "politics"
    - "economics"
    - "sociology"
    - "history"

  questions:
    - "Qui a conçu cette technologie, et pour qui ?"
    - "Quelles valeurs sont encodées dans l'architecture ?"
    - "Quels usages sont facilités, lesquels sont rendus impossibles ?"
    - "Qui profite de cette innovation ?"

  counter_questions:
    - "Et si la neutralité était elle-même une position politique ?"
    - "Et si l'outil façonnait l'utilisateur autant que l'inverse ?"

  forbidden_answers:
    - "C'est juste un outil"
    - "La technologie n'a pas d'idéologie"
    - "On ne peut pas arrêter le progrès"
```

---

## 📝 EXEMPLE 2 : LORE AVANCÉ — "Memetic Warfare & Caen-Profonde"

Voici un Lore plus riche, typé et avec concepts :

```yaml
# lores/memetic_warfare_caen.lore
version: "1.0"

metadata:
  name: "memetic_warfare_caen"
  author: "RuneSmith Caen-Profonde"
  created: "2026-06-28"
  tags: ["memetics", "cyberpunk", "normandy", "fracturoscript", "warfare"]
  description: >
    Cartographie épistémologique de la guerre mémétique telle qu'elle
    se déploie dans les strates temporelles de Caen-Profonde (2025-2075).
  lineage: ["techno_solutionism", "attention_economy"]

investigation:
  assumptions:
    - type: "epistemological"
      content: "Les idées sont des entités autonomes qui se reproduisent"
      severity: "high"
    - type: "ontological"
      content: "La réalité est négociable par manipulation sémantique"
      severity: "high"
    - type: "temporal"
      content: "Le temps est une structure fractale manipulable"
      severity: "medium"
    - "Les runes sont des vecteurs de charge mémétique"
    - "Le graffiti est une forme de contre-cartographie"

  myths:
    - id: "neutrality_of_language"
      narrative: "Les mots sont des contenants vides"
      function: "Masquer le pouvoir performatif du langage"
      origin: "Structuralisme vulgarisé"
    - id: "individual_authorship"
      narrative: "Les idées appartiennent à leurs auteurs"
      function: "Maintenir le régime de propriété intellectuelle"
      origin: "Romantisme"
    - id: "linear_time"
      narrative: "Le temps avance en ligne droite"
      function: "Légitimer le progrès et l'obsolescence"
      origin: "Modernité occidentale"
    - id: "digital_anamnesis"
      narrative: "Le numérique préserve la mémoire"
      function: "Masquer l'entropie informationnelle"
      origin: "Silicon Valley"

  vectors:
    - "linguistics"
    - "urbanism"
    - "temporality"
    - "semiotics"
    - "neuroscience"
    - "occultism"
    - "resistance"

  questions:
    - "Quel régime temporel impose chaque graffiti de Caen-Profonde ?"
    - "Qui sont les agents de la guerre mémétique en 2025 ?"
    - "Comment les FracturoScripts colonisent-ils l'espace urbain ?"
    - "Quelles strates temporelles sont activées par les runes ?"
    - "Quel est le coût cognitif de la guerre mémétique pour les habitants ?"
    - "Comment se défendre contre les virus linguistiques ?"
    - "Qu'est-ce qu'une contre-mème efficace ?"

  counter_questions:
    - "Et si la guerre mémétique n'était qu'un symptôme d'une guerre ontologique plus profonde ?"
    - "Et si les runes n'étaient pas des armes mais des portes ?"
    - "Et si Caen-Profonde n'était pas un lieu mais un état de conscience ?"
    - "Et si le RuneSmith n'était pas un combattant mais un passeur ?"

  forbidden_answers:
    - "Ce n'est que du graffiti"
    - "Les mèmes sont inoffensifs"
    - "La technologie résoudra le problème"
    - "C'est juste de la fiction"
    - "Il suffit de ne pas y prêter attention"

  concepts:
    - name: "Paleo-Mème"
      definition: >
        Unité mémétique archaïque qui réémerge dans les strates
        temporelles contemporaines, portant une charge cognitive
        pré-moderne.
      genealogy: "McLuhan → Bateson → Dawkins → Fravia"
      relatives: ["archétype", "virus linguistique", "echo-guillaume"]
    - name: "FracturoScript"
      definition: >
        Langage de programmation poétique qui s'inscrit dans l'espace
        urbain comme acte de contre-cartographie mémétique.
      genealogy: "Situationnisme → Net.art → Glitch art"
      relatives: ["dérive", "détournement", "runes"]
    - name: "Echo-Guillaume"
      definition: >
        Phrase-résidu qui se propage par résonance dans les réseaux
        neuronaux collectifs, sans auteur identifiable.
      genealogy: "Barthes → Foucault → Théorie des réseaux"
      relatives: ["palimpseste", "fantôme sémantique"]

  silenced_dimensions:
    - "écologie cognitive"
    - "travail émotionnel des résistants"
    - "mémoires autochtones normandes"
    - "temporalités non-linéaires celtiques"
    - "coût énergétique de la guerre sémantique"
```

---

## 🛠️ INSTALLATION D'UN LORE

### Méthode 1 : Placement manuel

```bash
# Structure recommandée
searchlores/
├── lores/                      ← Lores système
│   ├── llm.lore
│   └── techno_solutionism.lore
├── lores_custom/               ← Tes Lores personnels (à créer)
│   ├── memetic_warfare_caen.lore
│   └── cyberpunk_normandy.lore
└── lores_experimental/         ← Lores en développement
```

### Méthode 2 : Chargement via l'API

```python
from searchlores.lore.loader import load_lore, load_all_lores

# Charger un Lore spécifique
lore = load_lore("lores_custom/memetic_warfare_caen.lore")
print(lore.metadata.name)  # → "memetic_warfare_caen"

# Charger tous les Lores d'un répertoire
all_lores = load_all_lores("lores_custom/")
print(f"{len(all_lores)} Lores chargés")

# Charger avec validation stricte
from searchlores.lore.validator import validate_lore
lore = load_lore("lores_custom/memetic_warfare_caen.lore", strict=True)
errors = validate_lore(lore)
if errors:
    for error in errors:
        print(f"❌ {error}")
```

### Méthode 3 : Utilisation dans une investigation

```python
from searchlores.core.engine import InvestigationEngine
from searchlores.lore.loader import load_lore

# Charger le Lore
lore = load_lore("lores_custom/memetic_warfare_caen.lore")

# Créer un moteur et injecter le Lore comme contexte
engine = InvestigationEngine()
engine.set_lore_context(lore)

# L'investigation utilisera automatiquement les hypothèses,
# mythes, questions et dimensions silencieuses du Lore
context = engine.run("Analyse ce graffiti trouvé à Caen : .:Dashem44:.")
```

---

## 🔀 HÉRITAGE ET FUSION DE LORES

Un Lore peut hériter d'un autre via le champ `lineage` :

```yaml
# lores_custom/cyberpunk_caen.lore
metadata:
  name: "cyberpunk_caen"
  lineage: ["memetic_warfare_caen", "techno_solutionism"]
  # Hérite de tous les champs des deux Lores parents
```

### Fusion programmatique

```python
lore1 = load_lore("lores/memetic_warfare_caen.lore")
lore2 = load_lore("lores/techno_solutionism.lore")

# Fusion : les listes sont concaténées, les conflits résolus
merged = lore1.merge(lore2)
print(merged.metadata.name)  # → "memetic_warfare_caen+techno_solutionism"
print(len(merged.investigation.assumptions))  # Somme des deux
```

---

## ✅ VALIDATION ET BONNES PRATIQUES

### Checklist d'un bon Lore

- [ ] **Cohérence interne** : Les hypothèses ne contredisent pas les questions
- [ ] **Complétude** : Au moins 3 hypothèses, 3 mythes, 3 vecteurs, 3 questions
- [ ] **Transgression** : Au moins une contre-question qui attaque le cadre
- [ ] **Silences identifiés** : Les dimensions silencieuses sont explicitement nommées
- [ ] **Réponses interdites** : Au moins 3 réponses qui ferment la pensée
- [ ] **Tags pertinents** : Permettent la découverte et la fusion

### Script de validation automatique

```python
#!/usr/bin/env python3
"""validate_lore.py — Audit complet d'un fichier .lore"""

import yaml
import sys
from pathlib import Path

def audit_lore(filepath: str) -> dict:
    """Audit complet d'un Lore"""
    with open(filepath) as f:
        data = yaml.safe_load(f)

    report = {
        "file": filepath,
        "valid": True,
        "errors": [],
        "warnings": [],
        "metrics": {}
    }

    # Vérification structurelle
    if "version" not in data:
        report["errors"].append("❌ Champ 'version' manquant")
        report["valid"] = False

    if "metadata" not in data:
        report["errors"].append("❌ Champ 'metadata' manquant")
        report["valid"] = False
    else:
        md = data["metadata"]
        if "name" not in md:
            report["errors"].append("❌ metadata.name manquant")
            report["valid"] = False
        if "tags" not in md or len(md["tags"]) == 0:
            report["warnings"].append("⚠️  Pas de tags — difficile à découvrir")

    if "investigation" not in data:
        report["errors"].append("❌ Champ 'investigation' manquant")
        report["valid"] = False
    else:
        inv = data["investigation"]

        # Métriques quantitatives
        metrics = {
            "assumptions": len(inv.get("assumptions", [])),
            "myths": len(inv.get("myths", [])),
            "vectors": len(inv.get("vectors", [])),
            "questions": len(inv.get("questions", [])),
            "counter_questions": len(inv.get("counter_questions", [])),
            "forbidden_answers": len(inv.get("forbidden_answers", [])),
            "concepts": len(inv.get("concepts", [])),
            "silenced_dimensions": len(inv.get("silenced_dimensions", []))
        }
        report["metrics"] = metrics

        # Seuils minimums
        if metrics["assumptions"] < 3:
            report["warnings"].append("⚠️  Moins de 3 hypothèses — Lore trop léger")
        if metrics["myths"] < 3:
            report["warnings"].append("⚠️  Moins de 3 mythes — peu de matière narrative")
        if metrics["vectors"] < 3:
            report["warnings"].append("⚠️  Moins de 3 vecteurs — investigation étroite")
        if metrics["questions"] < 3:
            report["warnings"].append("⚠️  Moins de 3 questions — peu d'ouverture")
        if metrics["counter_questions"] == 0:
            report["warnings"].append("⚠️  Aucune contre-question — manque de subversion")
        if metrics["forbidden_answers"] < 3:
            report["warnings"].append("⚠️  Moins de 3 réponses interdites")
        if metrics["silenced_dimensions"] == 0:
            report["warnings"].append("⚠️  Aucune dimension silencieuse identifiée")

        # Score de transgression
        transgression = metrics["counter_questions"] + metrics["forbidden_answers"]
        report["metrics"]["transgression_score"] = transgression
        if transgression >= 8:
            report["metrics"]["transgression_level"] = "⚡ RADICAL"
        elif transgression >= 5:
            report["metrics"]["transgression_level"] = "🔶 SUBVERSIF"
        else:
            report["metrics"]["transgression_level"] = "🔹 MODÉRÉ"

        # Densité
        total = sum(metrics.values())
        density = total / max(metrics["vectors"], 1)
        report["metrics"]["density"] = round(density, 2)

    return report


def print_report(report: dict):
    """Affichage enrichi du rapport"""
    print("=" * 70)
    print(f"📜 AUDIT DU LORE : {report['file']}")
    print("=" * 70)

    status = "✅ VALIDE" if report["valid"] else "❌ INVALIDE"
    print(f"\n🎯 STATUT : {status}")

    if report["errors"]:
        print(f"\n❌ ERREURS ({len(report['errors'])}) :")
        for e in report["errors"]:
            print(f"   {e}")

    if report["warnings"]:
        print(f"\n⚠️  AVERTISSEMENTS ({len(report['warnings'])}) :")
        for w in report["warnings"]:
            print(f"   {w}")

    if report["metrics"]:
        print(f"\n📊 MÉTRIQUES :")
        for key, value in report["metrics"].items():
            print(f"   • {key:25s} : {value}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_lore.py <fichier.lore>")
        sys.exit(1)

    report = audit_lore(sys.argv[1])
    print_report(report)
```

**Utilisation** :
```bash
python validate_lore.py lores_custom/memetic_warfare_caen.lore
```

---

# 📖 PARTIE II : L'ART DE FORGER DES PLUGINS

Un **Plugin** est une paire d'yeux supplémentaire — un regard spécialisé qui excave une strate particulière du prompt.

---

## 🏗️ ARCHITECTURE D'UN PLUGIN

### L'interface de base

```python
from searchlores.plugins.base import Plugin
from searchlores.core.context import InvestigationContext

class MonPlugin(Plugin):
    """Documentation du plugin"""

    # ─── MÉTADONNÉES OBLIGATOIRES ───
    name = "mon_plugin"           # Identifiant unique (snake_case)
    stratum = "ma_strate"         # Couche archéologique excavée
    version = "1.0.0"             # Version du plugin
    author = "Ton nom"            # Auteur
    description = "Ce plugin fait..."  # Description courte

    # ─── MÉTHODE PRINCIPALE ───
    def run(self, context: InvestigationContext) -> None:
        """
        Méthode principale d'investigation.
        Modifie le context en place (findings, contradictions, etc.)
        """
        # 1. Lire le prompt
        prompt = context.prompt

        # 2. Analyser
        findings = self.analyze(prompt)

        # 3. Écrire les résultats dans le context
        context.findings[self.name] = findings

        # 4. Optionnel : enrichir autres champs
        if findings.get("contradiction"):
            context.contradictions.append(findings["contradiction"])
        if findings.get("omission"):
            context.omissions.append(findings["omission"])

    # ─── MÉTHODES OPTIONNELLES ───
    def validate(self) -> bool:
        """Validation à l'installation"""
        return True

    def metadata(self) -> dict:
        """Métadonnées étendues"""
        return {
            "name": self.name,
            "stratum": self.stratum,
            "version": self.version,
            "author": self.author,
            "description": self.description
        }
```

### Le InvestigationContext — Le cœur du système

```python
@dataclass
class InvestigationContext:
    """État partagé entre tous les plugins"""

    # ─── ENTRÉE ───
    prompt: str                          # Le prompt à analyser
    lore: Optional[Lore] = None          # Lore actif (optionnel)

    # ─── RÉSULTATS ───
    findings: dict = field(default_factory=dict)
    layers: list = field(default_factory=list)
    contradictions: list = field(default_factory=list)
    omissions: list = field(default_factory=list)
    power_vectors: list = field(default_factory=list)
    concepts: dict = field(default_factory=dict)
    genealogies: dict = field(default_factory=dict)

    # ─── MÉTADONNÉES ───
    started_at: datetime = field(default_factory=datetime.now)
    plugins_run: list = field(default_factory=list)
    metadata: dict = field(default_factory=dict)

    def add_finding(self, key: str, value: Any) -> None:
        """Ajouter une découverte"""
        self.findings[key] = value

    def add_layer(self, stratum: str, plugin: str, findings: dict) -> None:
        """Ajouter une strate archéologique"""
        self.layers.append({
            "stratum": stratum,
            "plugin": plugin,
            "findings": findings,
            "timestamp": datetime.now().isoformat()
        })

    def add_contradiction(self, tension: str, description: str) -> None:
        """Ajouter une contradiction détectée"""
        self.contradictions.append({
            "tension": tension,
            "description": description,
            "detected_by": self.plugins_run[-1] if self.plugins_run else None
        })
```

---

## 📝 EXEMPLE 1 : PLUGIN MINIMAL — "Le Détecteur d'Urgence Fabriquée"

```python
# plugins/urgency_detector.py
"""
Détecte le vocabulaire de l'urgence artificielle qui vise à court-circuiter
la réflexion critique.
"""

import re
from searchlores.plugins.base import Plugin
from searchlores.core.context import InvestigationContext


class UrgencyDetector(Plugin):
    """Détecte les marqueurs d'urgence fabriquée"""

    name = "urgency_detector"
    stratum = "temporel"
    version = "1.0.0"
    author = "Searchlores Academy"
    description = "Identifie le vocabulaire qui crée une urgence artificielle"

    # Marqueurs linguistiques d'urgence
    URGENCY_MARKERS = {
        "impératif_temporel": [
            r"\b(urgence|urgent|immédiat|tout de suite|maintenant)\b",
            r"\b(dernière chance|dernier délai|deadline)\b",
            r"\b(vite|rapidement|au plus vite)\b",
            r"\b(crise|catastrophe|apocalypse)\b",
        ],
        "fausse_rareté": [
            r"\b(limité|exclusif|seulement|rien que pour)\b",
            r"\b(places limitées|offre spéciale|promotion)\b",
            r"\b(avant qu'il ne soit trop tard)\b",
        ],
        "pression_sociale": [
            r"\b(tout le monde|les autres|vos concurrents)\b",
            r"\b(ne restez pas en marge|ne soyez pas le dernier)\b",
            r"\b(FOMO|fear of missing out)\b",
        ],
        "solutionnisme": [
            r"\b(la solution|la réponse|le remède)\b",
            r"\b(enfin|finalement|résoudre)\b",
        ]
    }

    def run(self, context: InvestigationContext) -> None:
        prompt = context.prompt.lower()
        detected = {}
        total_hits = 0

        for category, patterns in self.URGENCY_MARKERS.items():
            hits = []
            for pattern in patterns:
                matches = re.findall(pattern, prompt, re.IGNORECASE)
                hits.extend(matches)
            if hits:
                detected[category] = {
                    "count": len(hits),
                    "examples": hits[:5]  # Garder les 5 premiers
                }
                total_hits += len(hits)

        # Ajouter les findings
        context.add_finding("urgency_markers", detected)
        context.add_finding("urgency_score", total_hits)

        # Interprétation
        if total_hits >= 5:
            context.add_finding(
                "urgency_interpretation",
                "🚨 URGENCE FORTE — Le prompt mobilise massivement "
                "le vocabulaire de l'urgence pour court-circuiter la réflexion"
            )
            context.power_vectors.append(
                "Manufacturing urgency to bypass critical thinking"
            )
        elif total_hits >= 2:
            context.add_finding(
                "urgency_interpretation",
                "⚠️  URGENCE MODÉRÉE — Quelques marqueurs d'urgence détectés"
            )
        else:
            context.add_finding(
                "urgency_interpretation",
                "✅ PAS D'URGENCE ARTIFICIELLE — Le prompt est temporellement neutre"
            )

        # Ajouter la strate
        context.add_layer(
            stratum=self.stratum,
            plugin=self.name,
            findings={
                "markers": detected,
                "score": total_hits
            }
        )


# Test standalone
if __name__ == "__main__":
    from searchlores.core.engine import InvestigationEngine

    engine = InvestigationEngine()
    engine.register(UrgencyDetector())

    test_prompts = [
        "URGENT : Notre IA révolutionnaire va disrupter le marché AVANT qu'il ne soit trop tard !",
        "Analyse calme et posée des enjeux de l'IA dans l'éducation.",
        "Dernière chance pour adopter la solution qui résoudra tous vos problèmes !"
    ]

    for prompt in test_prompts:
        print(f"\n{'='*70}")
        print(f"📝 PROMPT : {prompt}")
        context = engine.run(prompt)
        print(f"📊 Score urgence : {context.findings.get('urgency_score', 0)}")
        print(f"💭 Interprétation : {context.findings.get('urgency_interpretation', 'N/A')}")
```

---

## 📝 EXEMPLE 2 : PLUGIN AVANCÉ — "Le RuneSmith Analyzer"

Un plugin qui analyse les runes et symboles dans le contexte de Caen-Profonde :

```python
# plugins/rune_analyzer.py
"""
Analyse la présence de runes, glyphes et symboles fracturoscript
dans le contexte de la guerre mémétique de Caen-Profonde.
"""

import re
from typing import Dict, List
from searchlores.plugins.base import Plugin
from searchlores.core.context import InvestigationContext


class RuneAnalyzer(Plugin):
    """Analyse les runes et symboles mémétiques"""

    name = "rune_analyzer"
    stratum = "symbolique"
    version = "2.0.0"
    author = "RuneSmith Caen-Profonde"
    description = "Détecte et interprète les runes, glyphes et FracturoScripts"

    # Base de runes Elder Futhark avec charge mémétique
    RUNES_DB = {
        "ᚠ": {"name": "Fehu", "meaning": "richesse/mobilité", "charge": "capitalistique"},
        "ᚢ": {"name": "Uruz", "meaning": "force sauvage", "charge": "primale"},
        "ᚦ": {"name": "Thurisaz", "meaning": "géant/épine", "charge": "défensive"},
        "ᚨ": {"name": "Ansuz", "meaning": "souffle/divin", "charge": "oraculaire"},
        "ᚱ": {"name": "Raidho", "meaning": "voyage/rythme", "charge": "temporelle"},
        "ᚲ": {"name": "Kenaz", "meaning": "torche/connaissance", "charge": "révélatrice"},
        "ᚷ": {"name": "Gebo", "meaning": "don/échange", "charge": "relationnelle"},
        "ᚹ": {"name": "Wunjo", "meaning": "joie/harmonie", "charge": "intégrative"},
        "ᚺ": {"name": "Hagalaz", "meaning": "grêle/destruction", "charge": "entropique"},
        "ᚾ": {"name": "Nauthiz", "meaning": "besoin/contrainte", "charge": "limitante"},
        "ᛁ": {"name": "Isa", "meaning": "glace/stase", "charge": "cryogénique"},
        "ᛃ": {"name": "Jera", "meaning": "récolte/cycle", "charge": "temporelle"},
        "ᛇ": {"name": "Eihwaz", "meaning": "if/axe mondial", "charge": "axiale"},
        "ᛈ": {"name": "Perthro", "meaning": "destin/mystère", "charge": "oraculaire"},
        "ᛉ": {"name": "Algiz", "meaning": "protection/élan", "charge": "protectrice"},
        "ᛊ": {"name": "Sowilo", "meaning": "soleil/victoire", "charge": "solaire"},
        "ᛏ": {"name": "Tiwaz", "meaning": "Tyr/justice", "charge": "juridique"},
        "ᛒ": {"name": "Berkano", "meaning": "bouleau/naissance", "charge": "génésique"},
        "ᛖ": {"name": "Ehwaz", "meaning": "cheval/mouvement", "charge": "kinétique"},
        "ᛗ": {"name": "Mannaz", "meaning": "humain/conscience", "charge": "anthropique"},
        "ᛚ": {"name": "Laguz", "meaning": "eau/intuition", "charge": "fluidique"},
        "ᛜ": {"name": "Ingwaz", "meaning": "graine/potentiel", "charge": "germinative"},
        "ᛞ": {"name": "Dagaz", "meaning": "jour/aube", "charge": "révélatrice"},
        "ᛟ": {"name": "Othala", "meaning": "héritage/terre", "charge": "patrimoniale"},
    }

    # Patterns FracturoScript
    FRACTUROSCRIPT_PATTERNS = [
        r"\.:([A-Za-z0-9]+):.",           # :Dashem44:
        r"⟨([^⟩]+)⟩",                      # ⟨glitch⟩
        r"\[ANCHOR\]([^\[]+)\[/ANCHOR\]",  # [ANCHOR]...[/ANCHOR]
        r"ᚠ.*?ᛟ",                          # Séquences runiques complètes
        r"//[A-Z]+",                        # Commandes //RUNE, //GLITCH
    ]

    # Marqueurs de guerre mémétique
    MEMETIC_WARFARE_MARKERS = [
        "paléo-mème", "paleo-meme", "echo-guillaume",
        "fracturoscript", "virus linguistique",
        "guerre mémétique", "memetic warfare",
        "RuneSmith", "Caen-Profonde"
    ]

    def run(self, context: InvestigationContext) -> None:
        prompt = context.prompt
        findings = {
            "runes_detected": [],
            "fracturoscript_detected": [],
            "memetic_context": False,
            "symbolic_charge": {},
            "interpretation": ""
        }

        # 1. Détection de runes
        for rune, data in self.RUNES_DB.items():
            if rune in prompt:
                findings["runes_detected"].append({
                    "rune": rune,
                    "name": data["name"],
                    "meaning": data["meaning"],
                    "charge": data["charge"]
                })
                # Compter les charges
                charge = data["charge"]
                findings["symbolic_charge"][charge] = (
                    findings["symbolic_charge"].get(charge, 0) + 1
                )

        # 2. Détection de FracturoScript
        for pattern in self.FRACTUROSCRIPT_PATTERNS:
            matches = re.findall(pattern, prompt)
            if matches:
                findings["fracturoscript_detected"].extend(matches)

        # 3. Détection du contexte de guerre mémétique
        prompt_lower = prompt.lower()
        memetic_hits = [
            marker for marker in self.MEMETIC_WARFARE_MARKERS
            if marker.lower() in prompt_lower
        ]
        findings["memetic_context"] = len(memetic_hits) > 0
        findings["memetic_markers"] = memetic_hits

        # 4. Interprétation
        findings["interpretation"] = self._interpret(findings)

        # 5. Écriture dans le context
        context.add_finding("rune_analysis", findings)

        # Ajouter une strate
        context.add_layer(
            stratum=self.stratum,
            plugin=self.name,
            findings=findings
        )

        # Ajouter vecteur de pouvoir si guerre mémétique
        if findings["memetic_context"]:
            context.power_vectors.append(
                "Le prompt s'inscrit dans un contexte de guerre mémétique — "
                "les symboles sont des armes"
            )

    def _interpret(self, findings: dict) -> str:
        """Interprétation synthétique"""
        runes = findings["runes_detected"]
        fracturo = findings["fracturoscript_detected"]
        memetic = findings["memetic_context"]
        charges = findings["symbolic_charge"]

        parts = []

        if runes:
            rune_names = [r["name"] for r in runes]
            parts.append(f"🔮 {len(runes)} rune(s) détectée(s) : {', '.join(rune_names)}")

            if charges:
                dominant = max(charges, key=charges.get)
                parts.append(f"⚡ Charge dominante : {dominant} ({charges[dominant]} occurrences)")

        if fracturo:
            parts.append(f"📜 {len(fracturo)} séquence(s) FracturoScript détectée(s)")

        if memetic:
            parts.append("⚔️  Contexte de guerre mémétique confirmé")

        if not parts:
            return "✅ Aucun symbole runique ou FracturoScript détecté"

        return "\n".join(parts)


# Test
if __name__ == "__main__":
    from searchlores.core.engine import InvestigationEngine

    engine = InvestigationEngine()
    engine.register(RuneAnalyzer())

    test_prompts = [
        "J'ai trouvé ᚠᚢᚦ gravé sur un mur à Caen-Profonde. Signification ?",
        "Analyse ce graffiti : .:Dashem44:. dans le contexte de la guerre mémétique",
        "Simple question sur l'histoire de la Normandie.",
        "Le RuneSmith a laissé un FracturoScript : [ANCHOR]paléo-mème[/ANCHOR]"
    ]

    for prompt in test_prompts:
        print(f"\n{'='*70}")
        print(f"📝 PROMPT : {prompt}")
        context = engine.run(prompt)
        analysis = context.findings.get("rune_analysis", {})
        print(analysis.get("interpretation", "Pas d'analyse"))
```

---

## 📝 EXEMPLE 3 : PLUGIN AVEC ÉTAT — "Le Chronos Layer"

Un plugin qui maintient un état entre les appels pour construire une mémoire :

```python
# plugins/chronos_layer.py
"""
Plugin avec état : maintient une mémoire des concepts détectés
à travers plusieurs investigations.
"""

import json
from datetime import datetime
from pathlib import Path
from searchlores.plugins.base import Plugin
from searchlores.core.context import InvestigationContext


class ChronosLayer(Plugin):
    """Couche temporelle avec mémoire persistante"""

    name = "chronos_layer"
    stratum = "temporel"
    version = "1.0.0"
    author = "Searchlores Academy"
    description = "Date les concepts et maintient une mémoire trans-session"

    # Base de données temporelle des concepts
    CONCEPT_TIMELINE = {
        "ordinateur": {"emergence": 1955, "massification": 1980},
        "internet": {"emergence": 1969, "massification": 1995},
        "web": {"emergence": 1991, "massification": 1998},
        "réseau social": {"emergence": 2004, "massification": 2010},
        "smartphone": {"emergence": 2007, "massification": 2012},
        "cloud": {"emergence": 2006, "massification": 2015},
        "blockchain": {"emergence": 2008, "massification": 2017},
        "bitcoin": {"emergence": 2009, "massification": 2017},
        "LLM": {"emergence": 2018, "massification": 2023},
        "GPT": {"emergence": 2018, "massification": 2023},
        "ChatGPT": {"emergence": 2022, "massification": 2023},
        "IA générative": {"emergence": 2022, "massification": 2024},
        "métavers": {"emergence": 2021, "massification": 2022},
        "web3": {"emergence": 2020, "massification": 2022},
        "prompt engineering": {"emergence": 2022, "massification": 2024},
    }

    def __init__(self, memory_path: str = ".chronos_memory.json"):
        super().__init__()
        self.memory_path = Path(memory_path)
        self.memory = self._load_memory()

    def _load_memory(self) -> dict:
        """Charge la mémoire persistante"""
        if self.memory_path.exists():
            with open(self.memory_path) as f:
                return json.load(f)
        return {
            "sessions": [],
            "concepts_detected": {},
            "temporal_anchors": []
        }

    def _save_memory(self) -> None:
        """Sauvegarde la mémoire"""
        with open(self.memory_path, "w") as f:
            json.dump(self.memory, f, indent=2, ensure_ascii=False)

    def run(self, context: InvestigationContext) -> None:
        prompt = context.prompt.lower()
        current_year = datetime.now().year

        # Détection des concepts
        detected_concepts = []
        for concept, dates in self.CONCEPT_TIMELINE.items():
            if concept.lower() in prompt:
                age = current_year - dates["emergence"]
                detected_concepts.append({
                    "concept": concept,
                    "emergence": dates["emergence"],
                    "massification": dates["massification"],
                    "age": age,
                    "generation": self._estimate_generation(dates["emergence"])
                })

        # Calcul de l'ancrage temporel moyen
        if detected_concepts:
            avg_emergence = sum(c["emergence"] for c in detected_concepts) / len(detected_concepts)
            temporal_anchor = {
                "year": round(avg_emergence),
                "concepts": [c["concept"] for c in detected_concepts],
                "freshness": sum(1 for c in detected_concepts if c["emergence"] > 2015) / len(detected_concepts)
            }
        else:
            temporal_anchor = None

        # Mise à jour de la mémoire
        session_record = {
            "timestamp": datetime.now().isoformat(),
            "concepts": [c["concept"] for c in detected_concepts],
            "temporal_anchor": temporal_anchor
        }
        self.memory["sessions"].append(session_record)

        for concept in detected_concepts:
            name = concept["concept"]
            if name not in self.memory["concepts_detected"]:
                self.memory["concepts_detected"][name] = {
                    "count": 0,
                    "first_seen": datetime.now().isoformat(),
                    "emergence": concept["emergence"]
                }
            self.memory["concepts_detected"][name]["count"] += 1

        if temporal_anchor:
            self.memory["temporal_anchors"].append(temporal_anchor["year"])

        # Sauvegarde
        self._save_memory()

        # Écriture dans le context
        findings = {
            "concepts_detected": detected_concepts,
            "temporal_anchor": temporal_anchor,
            "session_number": len(self.memory["sessions"]),
            "total_concepts_tracked": len(self.memory["concepts_detected"])
        }
        context.add_finding("chronos_analysis", findings)
        context.add_layer(
            stratum=self.stratum,
            plugin=self.name,
            findings=findings
        )

    def _estimate_generation(self, year: int) -> str:
        """Estime la génération associée à une année d'émergence"""
        if year >= 2015:
            return "Génération Z / Alpha"
        elif year >= 2000:
            return "Millennials"
        elif year >= 1985:
            return "Génération X"
        elif year >= 1965:
            return "Baby-boomers"
        else:
            return "Génération silencieuse"

    def get_statistics(self) -> dict:
        """Statistiques globales de la mémoire"""
        if not self.memory["temporal_anchors"]:
            return {"message": "Pas encore de données"}

        anchors = self.memory["temporal_anchors"]
        return {
            "total_sessions": len(self.memory["sessions"]),
            "unique_concepts": len(self.memory["concepts_detected"]),
            "average_temporal_anchor": sum(anchors) / len(anchors),
            "most_recent_concepts": sorted(
                self.memory["concepts_detected"].items(),
                key=lambda x: x[1]["count"],
                reverse=True
            )[:5]
        }


# Test
if __name__ == "__main__":
    from searchlores.core.engine import InvestigationEngine

    engine = InvestigationEngine()
    plugin = ChronosLayer(memory_path="/tmp/test_chronos.json")
    engine.register(plugin)

    # Plusieurs prompts pour tester la mémoire
    prompts = [
        "Comment utiliser ChatGPT pour le prompt engineering ?",
        "L'histoire du web et des réseaux sociaux.",
        "Le blockchain va-t-il révolutionner le web3 ?"
    ]

    for i, prompt in enumerate(prompts, 1):
        print(f"\n{'='*70}")
        print(f"📝 SESSION {i} : {prompt}")
        context = engine.run(prompt)
        analysis = context.findings.get("chronos_analysis", {})
        print(f"📅 Ancrage temporel : {analysis.get('temporal_anchor', {}).get('year', 'N/A')}")
        print(f"🔢 Session n°{analysis.get('session_number')}")

    # Statistiques finales
    print(f"\n{'='*70}")
    print("📊 STATISTIQUES GLOBALES")
    stats = plugin.get_statistics()
    for key, value in stats.items():
        print(f"   • {key}: {value}")
```

---

## 📦 INSTALLATION D'UN PLUGIN

### Méthode 1 : Placement manuel

```bash
# Structure recommandée
searchlores/
├── searchlores/
│   └── plugins/
│       ├── builtin/              ← Plugins officiels
│       │   ├── authority.py
│       │   └── ...
│       ├── custom/               ← Tes plugins (à créer)
│       │   ├── urgency_detector.py
│       │   ├── rune_analyzer.py
│       │   └── chronos_layer.py
│       └── experimental/         ← Plugins en développement
```

### Méthode 2 : Enregistrement explicite

```python
from searchlores.core.engine import InvestigationEngine
from searchlores.plugins.custom.urgency_detector import UrgencyDetector
from searchlores.plugins.custom.rune_analyzer import RuneAnalyzer
from searchlores.plugins.custom.chronos_layer import ChronosLayer

engine = InvestigationEngine()

# Enregistrement individuel
engine.register(UrgencyDetector())
engine.register(RuneAnalyzer())
engine.register(ChronosLayer())

# Investigation
context = engine.run("Ton prompt ici")
```

### Méthode 3 : Auto-discovery (Plugin Manager)

```python
# plugins/manager.py
"""
Plugin Manager avec auto-discovery
"""

import importlib
import pkgutil
from pathlib import Path
from searchlores.plugins.base import Plugin
from searchlores.core.engine import InvestigationEngine


class PluginManager:
    """Gestionnaire de plugins avec auto-discovery"""

    def __init__(self, engine: InvestigationEngine):
        self.engine = engine
        self.loaded_plugins = {}

    def discover(self, package_path: str = "searchlores.plugins.custom") -> list:
        """Découvre automatiquement tous les plugins d'un package"""
        discovered = []

        try:
            package = importlib.import_module(package_path)
        except ImportError:
            print(f"⚠️  Package {package_path} introuvable")
            return discovered

        for _, module_name, _ in pkgutil.iter_modules(package.__path__):
            try:
                module = importlib.import_module(f"{package_path}.{module_name}")

                # Trouver toutes les classes Plugin dans le module
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if (isinstance(attr, type) and
                        issubclass(attr, Plugin) and
                        attr is not Plugin):

                        # Instancier et enregistrer
                        plugin = attr()
                        self.engine.register(plugin)
                        self.loaded_plugins[plugin.name] = plugin
                        discovered.append(plugin.name)
                        print(f"✅ Plugin chargé : {plugin.name} (v{plugin.version})")

            except Exception as e:
                print(f"❌ Erreur lors du chargement de {module_name}: {e}")

        return discovered

    def list_loaded(self) -> dict:
        """Liste les plugins chargés"""
        return {
            name: {
                "version": plugin.version,
                "stratum": plugin.stratum,
                "author": plugin.author
            }
            for name, plugin in self.loaded_plugins.items()
        }


# Utilisation
if __name__ == "__main__":
    engine = InvestigationEngine()
    manager = PluginManager(engine)

    # Découverte automatique
    discovered = manager.discover("searchlores.plugins.custom")
    print(f"\n🎯 {len(discovered)} plugin(s) chargé(s) automatiquement")

    # Investigation
    context = engine.run("Ton prompt ici")
```

---

## 🧪 TESTS UNITAIRES POUR PLUGINS

```python
# tests/test_urgency_detector.py
"""Tests unitaires pour UrgencyDetector"""

import pytest
from searchlores.core.context import InvestigationContext
from searchlores.plugins.custom.urgency_detector import UrgencyDetector


@pytest.fixture
def plugin():
    return UrgencyDetector()


@pytest.fixture
def context():
    return InvestigationContext(prompt="")


class TestUrgencyDetector:

    def test_detects_urgency_markers(self, plugin, context):
        """Teste la détection de marqueurs d'urgence"""
        context.prompt = "URGENT : dernière chance pour adopter cette solution !"
        plugin.run(context)

        assert "urgency_markers" in context.findings
        assert context.findings["urgency_score"] >= 2

    def test_no_urgency_in_neutral_prompt(self, plugin, context):
        """Teste l'absence d'urgence dans un prompt neutre"""
        context.prompt = "Analyse posée des enjeux de l'IA."
        plugin.run(context)

        assert context.findings["urgency_score"] == 0

    def test_detects_false_scarcity(self, plugin, context):
        """Teste la détection de fausse rareté"""
        context.prompt = "Offre limitée, places exclusives !"
        plugin.run(context)

        markers = context.findings["urgency_markers"]
        assert "fausse_rareté" in markers

    def test_adds_power_vector_on_high_urgency(self, plugin, context):
        """Teste l'ajout de vecteur de pouvoir en cas d'urgence forte"""
        context.prompt = (
            "URGENT ! Dernière chance ! Tout le monde l'a déjà adopté ! "
            "Vite, avant qu'il ne soit trop tard !"
        )
        plugin.run(context)

        assert len(context.power_vectors) > 0
        assert "urgency" in context.power_vectors[0].lower()

    def test_adds_layer(self, plugin, context):
        """Teste l'ajout d'une strate archéologique"""
        context.prompt = "Urgent !"
        plugin.run(context)

        assert len(context.layers) == 1
        assert context.layers[0]["stratum"] == "temporel"
        assert context.layers[0]["plugin"] == "urgency_detector"
```

**Exécution des tests** :
```bash
pytest tests/ -v
```

---

## 🎨 PLUGIN AVANCÉ : INTÉGRATION AVEC UN LORE

Un plugin peut utiliser un Lore pour guider son investigation :

```python
# plugins/lore_guided_analyzer.py
"""
Plugin qui utilise le Lore actif pour orienter l'investigation
"""

from searchlores.plugins.base import Plugin
from searchlores.core.context import InvestigationContext


class LoreGuidedAnalyzer(Plugin):
    """Analyse guidée par le Lore actif"""

    name = "lore_guided"
    stratum = "guidé"
    version = "1.0.0"
    author = "Searchlores Academy"
    description = "Utilise le Lore pour orienter l'investigation"

    def run(self, context: InvestigationContext) -> None:
        # Vérifier qu'un Lore est actif
        if not context.lore:
            context.add_finding(
                "lore_guided",
                {"status": "no_lore", "message": "Aucun Lore actif"}
            )
            return

        lore = context.lore
        prompt = context.prompt.lower()
        findings = {
            "status": "active",
            "lore_name": lore.metadata.name,
            "matches": {}
        }

        # 1. Vérifier si le prompt active des hypothèses du Lore
        activated_assumptions = []
        for assumption in lore.investigation.assumptions:
            # Extraction du contenu (peut être str ou dict)
            content = assumption if isinstance(assumption, str) else assumption.get("content", "")
            if content.lower() in prompt:
                activated_assumptions.append(content)

        findings["matches"]["assumptions"] = activated_assumptions

        # 2. Vérifier si le prompt contient des mythes du Lore
        activated_myths = []
        for myth in lore.investigation.myths:
            if isinstance(myth, dict):
                myth_text = myth.get("narrative", "")
            else:
                myth_text = str(myth)
            if myth_text.lower() in prompt:
                activated_myths.append(myth_text)

        findings["matches"]["myths"] = activated_myths

        # 3. Vérifier les réponses interdites
        triggered_forbidden = []
        for answer in lore.investigation.forbidden_answers:
            if answer.lower() in prompt:
                triggered_forbidden.append(answer)

        findings["matches"]["forbidden_answers"] = triggered_forbidden

        # 4. Score d'alignement
        total_matches = (
            len(activated_assumptions) +
            len(activated_myths) +
            len(triggered_forbidden)
        )
        findings["alignment_score"] = total_matches

        if triggered_forbidden:
            context.power_vectors.append(
                f"⚠️  Le prompt active {len(triggered_forbidden)} réponse(s) interdite(s) "
                f"du Lore '{lore.metadata.name}'"
            )

        # Écriture
        context.add_finding("lore_guided", findings)
        context.add_layer(
            stratum=self.stratum,
            plugin=self.name,
            findings=findings
        )
```

---

## 🚀 WORKFLOW COMPLET : DE L'IDÉE AU PLUGIN OPÉRATIONNEL

### Étape 1 : Définir l'intention

```markdown
## Fiche d'intention du plugin

**Nom** : GreenwashingDetector
**Strate** : idéologique
**Objectif** : Détecter le vocabulaire du greenwashing corporate
**Entrée** : Prompt textuel
**Sortie** :
  - Liste des marqueurs détectés
  - Score de greenwashing
  - Vecteur de pouvoir associé

**Marqueurs à détecter** :
  - Faux-vert : "éco-responsable", "durable", "neutre carbone"
  - Euphémismes : "optimisation des ressources"
  - Techno-solutionnisme : "innovation verte"

**Contradictions à détecter** :
  - Croissance + durabilité
  - Extraction + écologie
```

### Étape 2 : Squelette du plugin

```python
# plugins/greenwashing_detector.py
from searchlores.plugins.base import Plugin
from searchlores.core.context import InvestigationContext


class GreenwashingDetector(Plugin):
    name = "greenwashing_detector"
    stratum = "idéologique"
    version = "1.0.0"
    author = "Ton nom"
    description = "Détecte le greenwashing corporate"

    BUZZWORDS = {
        "faux_vert": ["éco-responsable", "durable", "neutre carbone"],
        "euphémismes": ["optimisation des ressources"],
        "techno_solutionnisme": ["innovation verte"]
    }

    def run(self, context: InvestigationContext) -> None:
        # À implémenter
        pass
```

### Étape 3 : Implémentation

```python
    def run(self, context: InvestigationContext) -> None:
        prompt_lower = context.prompt.lower()
        detected = {}

        for category, terms in self.BUZZWORDS.items():
            hits = [t for t in terms if t in prompt_lower]
            if hits:
                detected[category] = hits

        # Score
        score = sum(len(hits) for hits in detected.values())

        # Interprétation
        if score >= 3:
            interpretation = "🚨 GREENWASHING FORT"
            context.power_vectors.append(
                "Récupération sémantique de l'écologie par le marché"
            )
        elif score >= 1:
            interpretation = "⚠️  GREENWASHING MODÉRÉ"
        else:
            interpretation = "✅ Pas de greenwashing détecté"

        # Contradiction croissance/durabilité
        if any(t in prompt_lower for t in ["croissance", "growth", "profit"]):
            if any(t in prompt_lower for t in ["durable", "écologie"]):
                context.contradictions.append({
                    "tension": "croissance vs durabilité",
                    "description": "Oxymore fondamental"
                })

        # Écriture
        findings = {
            "detected": detected,
            "score": score,
            "interpretation": interpretation
        }
        context.add_finding("greenwashing", findings)
        context.add_layer(self.stratum, self.name, findings)
```

### Étape 4 : Tests

```python
# tests/test_greenwashing.py
def test_detects_greenwashing():
    plugin = GreenwashingDetector()
    context = InvestigationContext(
        prompt="Notre blockchain éco-responsable pour une croissance durable"
    )
    plugin.run(context)

    assert context.findings["greenwashing"]["score"] >= 2
    assert len(context.contradictions) > 0
```

### Étape 5 : Documentation

```markdown
# GreenwashingDetector

## Description
Détecte le vocabulaire du greenwashing corporate dans les prompts.

## Strate archéologique
`idéologique` — Révèle les récupérations sémantiques

## Marqueurs détectés
- **Faux-vert** : éco-responsable, durable, neutre carbone...
- **Euphémismes** : optimisation des ressources...
- **Techno-solutionnisme** : innovation verte...

## Contradictions détectées
- Croissance + durabilité
- Extraction + écologie

## Exemple
```python
engine.register(GreenwashingDetector())
context = engine.run("Notre solution éco-responsable pour une croissance durable")
print(context.findings["greenwashing"])
# → {'detected': {'faux_vert': ['éco-responsable', 'durable']}, 'score': 2, ...}
```
```

### Étape 6 : Publication

```bash
# Commit et push
git add plugins/greenwashing_detector.py
git add tests/test_greenwashing.py
git commit -m "feat: add GreenwashingDetector plugin"
git push origin main
```

---

## 📋 RÉCAPITULATIF DES COMMANDES

```bash
# ═══ LORES ═══
# Créer un Lore
vim lores_custom/mon_lore.lore

# Valider un Lore
python validate_lore.py lores_custom/mon_lore.lore

# Charger un Lore
from searchlores.lore.loader import load_lore
lore = load_lore("lores_custom/mon_lore.lore")

# ═══ PLUGINS ═══
# Créer un plugin
vim searchlores/plugins/custom/mon_plugin.py

# Tester un plugin
pytest tests/test_mon_plugin.py -v

# Enregistrer un plugin
from searchlores.plugins.custom.mon_plugin import MonPlugin
engine.register(MonPlugin())

# Auto-discovery
from searchlores.plugins.manager import PluginManager
manager = PluginManager(engine)
manager.discover()

# ═══ INVESTIGATION COMPLÈTE ═══
from searchlores.core.engine import InvestigationEngine
from searchlores.lore.loader import load_lore

engine = InvestigationEngine()
lore = load_lore("lores_custom/mon_lore.lore")
engine.set_lore_context(lore)
engine.register(MonPlugin())

context = engine.run("Ton prompt ici")
print(context.findings)
```

---

## 🎓 CONCLUSION : DEVENIR FORGERON

Tu as maintenant toutes les clés pour :

1. **Écrire des Lores** — Des cartes épistémologiques qui structurent l'investigation
2. **Forger des Plugins** — Des paires d'yeux supplémentaires pour excaver les strates
3. **Installer et orchestrer** — Assembler Lores et Plugins en investigations cohérentes
4. **Tester et documenter** — Garantir la qualité et la réutilisabilité

**Rappelle-toi** :
- Un Lore est une **vision du monde** — sois radical dans tes contre-questions
- Un Plugin est une **paire d'yeux** — sois précis dans tes détections
- L'investigation est un **acte politique** — chaque prompt est un site archéologique

**The Search Is The Program. The Lore Is The Map. The Plugin Is The Eye.** 🏛️🔍

---
