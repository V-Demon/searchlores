# searchlores/lore/loader.py
"""
Chargeur de fichiers .lore
Compatible Python 3.8+
"""

from pathlib import Path
from typing import Union, List
import yaml

from searchlores.lore.models import Lore


def load_lore(path: Union[str, Path]) -> Lore:
    """
    Charge un fichier .lore et retourne un objet Lore
    
    Args:
        path: Chemin vers le fichier .lore
        
    Returns:
        Lore: Objet Lore parsé
        
    Raises:
        FileNotFoundError: Si le fichier n'existe pas
        ValueError: Si le fichier est invalide
    """
    path = Path(path)
    
    if not path.exists():
        raise FileNotFoundError(f"Fichier Lore introuvable: {path}")
    
    if not path.suffix == '.lore':
        raise ValueError(f"Le fichier doit avoir l'extension .lore: {path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    if not data:
        raise ValueError(f"Fichier Lore vide: {path}")
    
    return Lore(**data)


def load_all_lores(directory: Union[str, Path]) -> List[Lore]:
    """
    Charge tous les fichiers .lore d'un répertoire
    
    Args:
        directory: Chemin vers le répertoire
        
    Returns:
        List[Lore]: Liste des objets Lore chargés
    """
    directory = Path(directory)
    
    if not directory.exists():
        raise FileNotFoundError(f"Répertoire introuvable: {directory}")
    
    if not directory.is_dir():
        raise ValueError(f"Ce n'est pas un répertoire: {directory}")
    
    lores = []
    for lore_file in directory.glob("*.lore"):
        try:
            lore = load_lore(lore_file)
            lores.append(lore)
        except Exception as e:
            print(f"⚠️  Erreur lors du chargement de {lore_file}: {e}")
    
    return lores


def validate_lore_file(path: Union[str, Path]) -> bool:
    """
    Valide la structure d'un fichier .lore sans le charger complètement
    
    Args:
        path: Chemin vers le fichier .lore
        
    Returns:
        bool: True si le fichier est valide
    """
    try:
        path = Path(path)
        
        if not path.exists():
            return False
        
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        # Vérifier les champs obligatoires
        required_fields = ['version', 'metadata', 'investigation']
        for field in required_fields:
            if field not in data:
                return False
        
        # Vérifier metadata
        if 'name' not in data['metadata']:
            return False
        
        # Vérifier investigation
        investigation = data['investigation']
        required_inv_fields = ['assumptions', 'myths', 'vectors', 'questions']
        for field in required_inv_fields:
            if field not in investigation:
                return False
        
        return True
    
    except Exception:
        return False
