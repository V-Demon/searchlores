from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class Metadata(BaseModel):
    name: str
    author: str
    version: str = "1.0"
    created: str = Field(default_factory=lambda: datetime.now().isoformat())
    tags: List[str] = []
    parent_lore: Optional[str] = None

class InvestigationSpec(BaseModel):
    assumptions: List[str] = []
    myths: List[str] = []
    vectors: List[str] = []
    questions: List[str] = []
    counter_questions: List[str] = []
    forbidden_answers: List[str] = []

class Lore(BaseModel):
    version: str = "1.0"
    metadata: Metadata
    investigation: InvestigationSpec

    def merge(self, other: 'Lore') -> 'Lore':
        return Lore(
            metadata=Metadata(
                name=f"{self.metadata.name} × {other.metadata.name}",
                author="LoreForge",
                tags=list(set(self.metadata.tags + other.metadata.tags))
            ),
            investigation=InvestigationSpec(
                assumptions=list(set(self.investigation.assumptions + other.investigation.assumptions)),
                myths=list(set(self.investigation.myths + other.investigation.myths)),
                vectors=list(set(self.investigation.vectors + other.investigation.vectors)),
                questions=list(set(self.investigation.questions + other.investigation.questions)),
                counter_questions=list(set(self.investigation.counter_questions + other.investigation.counter_questions)),
                forbidden_answers=list(set(self.investigation.forbidden_answers + other.investigation.forbidden_answers))
            )
        )

class EntropyMetrics(BaseModel):
    """Métriques d'entropie informationnelle"""
    token_entropy: float = Field(..., description="Entropie de Shannon sur les tokens")
    type_token_ratio: float = Field(..., description="Ratio type-token (diversité lexicale)")
    lexical_density: float = Field(..., description="Densité lexicale (mots lexicaux / total)")
    unique_tokens: int = Field(..., description="Nombre de tokens uniques")
    total_tokens: int = Field(..., description="Nombre total de tokens")
    
    @property
    def entropy_level(self) -> str:
        """Niveau d'entropie qualitatif"""
        if self.token_entropy < 3.0:
            return "FAIBLE"
        elif self.token_entropy < 5.0:
            return "MODÉRÉE"
        else:
            return "ÉLEVÉE"

class ComplexityMetrics(BaseModel):
    """Métriques de complexité structurelle"""
    cyclomatic_complexity: int = Field(..., description="Complexité cyclomatique (M = E - N + 2P)")
    conceptual_density: float = Field(..., description="Densité conceptuelle (arêtes / nœuds)")
    average_path_length: float = Field(..., description="Longueur moyenne des chemins")
    clustering_coefficient: float = Field(..., description="Coefficient de clustering")
    hierarchical_depth: int = Field(..., description="Profondeur hiérarchique maximale")
    pivot_concepts: Dict[str, float] = Field(default_factory=dict, description="Concepts pivots avec leur centralité")
    
    @property
    def complexity_level(self) -> str:
        """Niveau de complexité qualitatif"""
        if self.cyclomatic_complexity < 5:
            return "SIMPLE"
        elif self.cyclomatic_complexity < 15:
            return "MODÉRÉE"
        else:
            return "COMPLEXE"

class MetricsAnalysis(BaseModel):
    """Analyse complète des métriques pour une investigation"""
    entropy_metrics: Optional[EntropyMetrics] = None
    complexity_metrics: Optional[ComplexityMetrics] = None
    anomalies_detected: List[str] = Field(default_factory=list)
    
    class Config:
        arbitrary_types_allowed = True
