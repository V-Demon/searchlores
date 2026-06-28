# searchlores/plugins/lisp_exporter.py
"""
Plugin Lisp Exporter — Exporte les investigations en Common Lisp exécutable
Inspiré par la vision de Fravia : "Le code est la donnée, la donnée est le code"
"""

from typing import Any, Dict, List
from datetime import datetime
from searchlores.plugins.base import Plugin
from searchlores.core.context import InvestigationContext


class LispExporter(Plugin):
    """Exporte une InvestigationContext en code Lisp exécutable"""

    name = "lisp_exporter"
    stratum = "export"
    version = "1.0.0"
    author = "Searchlores Laboratory"
    description = "Exporte l'investigation en Common Lisp homoiconique"

    def __init__(self, dialect: str = "common-lisp"):
        super().__init__()
        self.dialect = dialect
        self.last_export = None

    def run(self, context: InvestigationContext) -> None:
        """Génère le code Lisp et l'ajoute aux findings"""
        lisp_code = self._generate_lisp_code(context)
        self.last_export = lisp_code

        # Ajouter aux findings
        context.add_finding("lisp_export", {
            "code": lisp_code,
            "dialect": self.dialect,
            "timestamp": datetime.now().isoformat(),
            "lines": len(lisp_code.split("\n"))
        })

        # Ajouter la strate
        context.add_layer(
            stratum=self.stratum,
            plugin=self.name,
            findings={"exported": True, "lines": len(lisp_code.split("\n"))}
        )

    def _generate_lisp_code(self, context: InvestigationContext) -> str:
        """Génère le code Lisp complet"""
        lines = []

        # En-tête
        lines.append(self._comment("═══════════════════════════════════════════════════════════"))
        lines.append(self._comment(f" Investigation Searchlores — Export Lisp ({self.dialect})"))
        lines.append(self._comment(f" Généré le : {datetime.now().isoformat()}"))
        lines.append(self._comment("═══════════════════════════════════════════════════════════"))
        lines.append("")

        # Package
        if self.dialect == "common-lisp":
            lines.append("(defpackage :searchlores-investigation")
            lines.append("  (:use :cl)")
            lines.append("  (:export #:investigation #:prompt #:findings #:layers")
            lines.append("           #:contradictions #:omissions #:power-vectors")
            lines.append("           #:self-analyze #:evolve #:replicate))")
            lines.append("")
            lines.append("(in-package :searchlores-investigation)")
        lines.append("")

        # Structure
        lines.append(self._comment("─── Structure de l'investigation ───"))
        if self.dialect == "common-lisp":
            lines.append("(defstruct investigation")
            lines.append("  prompt")
            lines.append("  findings")
            lines.append("  layers")
            lines.append("  contradictions")
            lines.append("  omissions")
            lines.append("  power-vectors")
            lines.append("  timestamp")
            lines.append("  metadata)")
        lines.append("")

        # Instance
        lines.append(self._comment("─── Instance de l'investigation ───"))
        lines.append(self._format_instance(context))
        lines.append("")

        # Fonctions d'auto-analyse
        lines.append(self._comment("─── Fonctions d'auto-analyse ───"))
        lines.extend(self._generate_self_analysis())
        lines.append("")

        # Fonctions d'évolution
        lines.append(self._comment("─── Fonctions d'évolution fractale ───"))
        lines.extend(self._generate_evolution())
        lines.append("")

        # Point d'entrée
        lines.append(self._comment("─── Point d'entrée ───"))
        lines.append("(defun run-investigation ()")
        lines.append('  "Exécute l\'investigation et affiche les résultats"')
        lines.append("  (format t \"~%═══════════════════════════════════════════════════════════~%\")")
        lines.append('  (format t " INVESTIGATION SEARCHLORES — AUTO-ANALYSE~%")')
        lines.append('  (format t "═══════════════════════════════════════════════════════════~%~%")')
        lines.append("  (let ((inv *current-investigation*))")
        lines.append("    (format t \"📝 PROMPT : ~A~%~%\" (investigation-prompt inv))")
        lines.append("    (format t \"📊 STRATES : ~D~%\" (length (investigation-layers inv)))")
        lines.append("    (format t \"⚡ CONTRADICTIONS : ~D~%\" (length (investigation-contradictions inv)))")
        lines.append("    (format t \"🔇 OMISSIONS : ~D~%\" (length (investigation-omissions inv)))")
        lines.append("    (format t \"⚔️  VECTEURS DE POUVOIR : ~D~%~%\" (length (investigation-power-vectors inv)))")
        lines.append("    (self-analyze inv)))")
        lines.append("")

        # Initialisation
        lines.append("(defparameter *current-investigation* *investigation-instance*)")
        lines.append("")

        # Signature Fravia
        lines.append(self._comment("═══════════════════════════════════════════════════════════"))
        lines.append(self._comment(" L'investigation est un fractal."))
        lines.append(self._comment(" Chaque strate contient toutes les strates."))
        lines.append(self._comment(" Le code est la donnée. La donnée est le code."))
        lines.append(self._comment(" — In memoriam Fravia (1952–2009)"))
        lines.append(self._comment("═══════════════════════════════════════════════════════════"))

        return "\n".join(lines)

    def _comment(self, text: str) -> str:
        """Génère un commentaire"""
        return f";; {text}" if self.dialect == "common-lisp" else f"; {text}"

    def _format_instance(self, context: InvestigationContext) -> str:
        """Formate l'instance de l'investigation"""
        lines = []

        if self.dialect == "common-lisp":
            lines.append("(defparameter *investigation-instance*")
            lines.append("  (make-investigation")
            lines.append(f"    :prompt {self._to_lisp_string(context.prompt)}")
            lines.append(f"    :findings {self._to_lisp_sexp(context.findings)}")
            lines.append(f"    :layers {self._to_lisp_sexp(context.layers)}")
            lines.append(f"    :contradictions {self._to_lisp_sexp(context.contradictions)}")
            lines.append(f"    :omissions {self._to_lisp_sexp(context.omissions)}")
            lines.append(f"    :power-vectors {self._to_lisp_sexp(context.power_vectors)}")
            lines.append(f"    :timestamp {self._to_lisp_string(datetime.now().isoformat())}")
            lines.append("    :metadata (list :engine \"searchlores\" :version \"1.0\")))")

        return "\n".join(lines)

    def _to_lisp_string(self, s: str) -> str:
        """Convertit une chaîne en chaîne Lisp"""
        escaped = s.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'

    def _to_lisp_sexp(self, obj: Any) -> str:
        """Convertit un objet Python en S-expression"""
        if obj is None:
            return "nil"
        elif isinstance(obj, bool):
            return "t" if obj else "nil"
        elif isinstance(obj, (int, float)):
            return str(obj)
        elif isinstance(obj, str):
            return self._to_lisp_string(obj)
        elif isinstance(obj, list):
            if not obj:
                return "nil"
            items = " ".join(self._to_lisp_sexp(item) for item in obj)
            return f"(list {items})"
        elif isinstance(obj, dict):
            if not obj:
                return "nil"
            pairs = []
            for k, v in obj.items():
                key = self._to_lisp_sexp(str(k))
                val = self._to_lisp_sexp(v)
                pairs.append(f"(cons {key} {val})")
            return f"(list {' '.join(pairs)})"
        else:
            return self._to_lisp_string(str(obj))

    def _generate_self_analysis(self) -> List[str]:
        """Génère les fonctions d'auto-analyse"""
        lines = []

        if self.dialect == "common-lisp":
            lines.append("(defun self-analyze (inv)")
            lines.append('  "Auto-analyse de l\'investigation"')
            lines.append("  (format t \"~%─── AUTO-ANALYSE ───~%~%\")")
            lines.append("  (format t \"📚 STRATES ARCHÉOLOGIQUES :~%\")")
            lines.append("  (dolist (layer (investigation-layers inv))")
            lines.append("    (format t \"  • Strate : ~A~%\" (cdr (assoc 'stratum layer)))")
            lines.append("    (format t \"    Plugin : ~A~%\" (cdr (assoc 'plugin layer)))")
            lines.append("    (format t \"    Timestamp : ~A~%~%\" (cdr (assoc 'timestamp layer))))")
            lines.append("  (when (investigation-contradictions inv)")
            lines.append("    (format t \"⚡ CONTRADICTIONS DÉTECTÉES :~%\")")
            lines.append("    (dolist (contradiction (investigation-contradictions inv))")
            lines.append("      (format t \"  • ~A~%\" (cdr (assoc 'tension contradiction)))")
            lines.append("      (format t \"    → ~A~%~%\" (cdr (assoc 'description contradiction)))))")
            lines.append("  (when (investigation-omissions inv)")
            lines.append("    (format t \"🔇 DIMENSIONS SILENCIEUSES :~%\")")
            lines.append("    (dolist (omission (investigation-omissions inv))")
            lines.append("      (format t \"  • ~A~%\" omission))")
            lines.append("    (format t \"~%\"))")
            lines.append("  (when (investigation-power-vectors inv)")
            lines.append("    (format t \"⚔️  VECTEURS DE POUVOIR :~%\")")
            lines.append("    (dolist (vector (investigation-power-vectors inv))")
            lines.append("      (format t \"  → ~A~%\" vector)))")
            lines.append("  (format t \"~%─── MÉTA-ANALYSE ───~%\")")
            lines.append("  (format t \"Cette investigation contient ~D strates, ~D contradictions, ~D omissions.~%\"")
            lines.append("            (length (investigation-layers inv))")
            lines.append("            (length (investigation-contradictions inv))")
            lines.append("            (length (investigation-omissions inv)))")
            lines.append("  (format t \"Le code est la donnée. La donnée est le code.~%\")")
            lines.append("  (format t \"L'investigation est un fractal.~%\"))")
            lines.append("")

        return lines

    def _generate_evolution(self) -> List[str]:
        """Génère les fonctions d'évolution fractale"""
        lines = []

        if self.dialect == "common-lisp":
            lines.append("(defun evolve (inv transformation)")
            lines.append('  "Évolue l\'investigation en appliquant une transformation"')
            lines.append("  (let ((evolved (copy-structure inv)))")
            lines.append("    (setf (investigation-findings evolved)")
            lines.append("          (funcall transformation (investigation-findings inv)))")
            lines.append("    (setf (investigation-timestamp evolved) (get-universal-time))")
            lines.append("    evolved))")
            lines.append("")
            lines.append("(defun replicate (inv depth)")
            lines.append('  "Réplique l\'investigation de manière fractale"')
            lines.append("  (if (<= depth 0)")
            lines.append("      inv")
            lines.append("      (let ((replica (copy-structure inv)))")
            lines.append("        (setf (investigation-metadata replica)")
            lines.append("              (append (investigation-metadata inv)")
            lines.append("                      (list :fractal-depth depth")
            lines.append("                            :parent (investigation-prompt inv))))")
            lines.append("        (replicate replica (- depth 1)))))")
            lines.append("")

        return lines

    def get_last_export(self) -> str:
        """Retourne le dernier export Lisp"""
        return self.last_export or ""
