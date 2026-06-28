# searchlores/core/context.py
"""
InvestigationContext — État partagé entre tous les plugins
Version étendue avec méthodes helper
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional

from searchlores.lore.models import Lore


@dataclass
class InvestigationContext:
    """État partagé entre tous les plugins d'investigation"""

    # ─── ENTRÉE ───
    prompt: str = ""
    lore: Optional[Lore] = None

    # ─── RÉSULTATS (tous initialisés vides) ───
    findings: Dict[str, Any] = field(default_factory=dict)
    layers: List[Dict[str, Any]] = field(default_factory=list)
    contradictions: List[Dict[str, Any]] = field(default_factory=list)
    omissions: List[str] = field(default_factory=list)
    power_vectors: List[str] = field(default_factory=list)
    concepts: Dict[str, Any] = field(default_factory=dict)
    genealogies: Dict[str, Any] = field(default_factory=dict)

    # ─── MÉTADONNÉES ───
    started_at: datetime = field(default_factory=datetime.now)
    plugins_run: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    # ═══════════════════════════════════════════════════════
    # MÉTHODES HELPER (ajoutées pour la cohérence d'API)
    # ═══════════════════════════════════════════════════════

    def add_finding(self, key: str, value: Any) -> None:
        """Ajoute une découverte aux findings"""
        self.findings[key] = value

    def add_layer(self, stratum: str, plugin: str, findings: dict) -> None:
        """Ajoute une strate archéologique"""
        self.layers.append({
            "stratum": stratum,
            "plugin": plugin,
            "findings": findings,
            "timestamp": datetime.now().isoformat()
        })

    def add_contradiction(self, tension: str, description: str, **kwargs) -> None:
        """Ajoute une contradiction détectée"""
        self.contradictions.append({
            "tension": tension,
            "description": description,
            **kwargs
        })

    def add_omission(self, dimension: str) -> None:
        """Ajoute une dimension silencieuse"""
        if dimension not in self.omissions:
            self.omissions.append(dimension)

    def add_power_vector(self, vector: str) -> None:
        """Ajoute un vecteur de pouvoir"""
        if vector not in self.power_vectors:
            self.power_vectors.append(vector)

    def to_searchmap(self) -> dict:
        """Exporte le context en format SearchMap (dict)"""
        return {
            "prompt": self.prompt,
            "findings": self.findings,
            "layers": self.layers,
            "contradictions": self.contradictions,
            "omissions": self.omissions,
            "power_vectors": self.power_vectors,
            "concepts": self.concepts,
            "metadata": {
                "started_at": self.started_at.isoformat(),
                "plugins_run": self.plugins_run,
                **self.metadata
            }
        }
