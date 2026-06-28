"""
Analyseur d'entropie informationnelle pour Searchlores
Mesure la diversité et l'incertitude informationnelle dans les textes
"""

import numpy as np
from collections import Counter
from typing import List, Set
import re

class EntropyAnalyzer:
    """Analyse l'entropie et la diversité lexicale des textes"""
    
    # Stopwords français et anglais courants
    STOPWORDS: Set[str] = {
        # Anglais
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
        'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
        'could', 'should', 'may', 'might', 'must', 'shall', 'can', 'need',
        'dare', 'ought', 'used', 'it', 'its', 'this', 'that', 'these', 'those',
        # Français
        'le', 'la', 'les', 'un', 'une', 'des', 'du', 'de', 'd', 'l', 'et',
        'ou', 'mais', 'donc', 'car', 'ni', 'que', 'qui', 'quoi', 'dont',
        'est', 'sont', 'a', 'ont', 'ai', 'as', 'avons', 'avez', 'ont'
    }
    
    def __init__(self, language: str = 'auto'):
        """
        Args:
            language: 'fr', 'en', ou 'auto' pour détection automatique
        """
        self.language = language
    
    def tokenize(self, text: str) -> List[str]:
        """Tokenise le texte en mots (simple mais efficace)"""
        # Nettoyage basique
        text = text.lower()
        # Extraction des mots (supporte les accents)
        words = re.findall(r'\b\w+\b', text, re.UNICODE)
        return words
    
    def calculate_token_entropy(self, tokens: List[str]) -> float:
        """
        Calcule l'entropie de Shannon sur la distribution des tokens
        H = -Σ p(x) * log2(p(x))
        """
        if not tokens:
            return 0.0
        
        token_counts = Counter(tokens)
        total_tokens = len(tokens)
        
        probabilities = [count / total_tokens for count in token_counts.values()]
        entropy = -sum(p * np.log2(p) for p in probabilities if p > 0)
        
        return entropy
    
    def calculate_type_token_ratio(self, tokens: List[str]) -> float:
        """
        Ratio Type-Token : mesure la diversité lexicale
        TTR = types uniques / total tokens
        """
        if not tokens:
            return 0.0
        
        unique_types = len(set(tokens))
        total_tokens = len(tokens)
        
        return unique_types / total_tokens
    
    def calculate_lexical_density(self, tokens: List[str]) -> float:
        """
        Densité lexicale : proportion de mots lexicaux (non-stopwords)
        LD = mots lexicaux / total mots
        """
        if not tokens:
            return 0.0
        
        lexical_words = [t for t in tokens if t not in self.STOPWORDS]
        
        return len(lexical_words) / len(tokens)
    
    def analyze(self, text: str) -> dict:
        """
        Analyse complète de l'entropie d'un texte
        
        Returns:
            dict avec toutes les métriques d'entropie
        """
        tokens = self.tokenize(text)
        
        if not tokens:
            return {
                'token_entropy': 0.0,
                'type_token_ratio': 0.0,
                'lexical_density': 0.0,
                'unique_tokens': 0,
                'total_tokens': 0
            }
        
        return {
            'token_entropy': self.calculate_token_entropy(tokens),
            'type_token_ratio': self.calculate_type_token_ratio(tokens),
            'lexical_density': self.calculate_lexical_density(tokens),
            'unique_tokens': len(set(tokens)),
            'total_tokens': len(tokens)
        }
