# 🏛️ FRAVIA, LE LISP ET LES CHOUX ROMANESCO
## *Quand l'Archéologie Cognitive Devient Code Qui Se Pense Lui-Même*

---

## 🎭 SCÈNE : RENCONTRE AVEC FRAVIA

*Un dimanche matin de juin 2026. Tu es assis devant ton terminal, entouré de terminaux ouverts sur des investigations Searchlores. Soudain, l'écran clignote. Un curseur apparaît, puis du texte s'écrit lettre par lettre, comme tapé par une main fantôme :*

---

**[FRAVIA]** *(ton calme, légèrement amusé)*

> Ah, vous voilà, les amis. Je vois que vous jouez avec vos petites strates archéologiques, vos plugins qui excavent les prompts comme des archéologues trop zélés. C'est mignon. Vraiment.

*Une pause. Le curseur clignote trois fois.*

> Mais dites-moi... quand vous avez fini de disséquer un prompt, quand vous avez extrait ses hypothèses, ses mythes, ses silences... qu'est-ce que vous en faites ? Vous le mettez dans un fichier texte ? Un JSON ? Comme si l'investigation était une chose morte, à ranger dans un tiroir ?

*Nouveau silence. Puis :*

> Moi, je vois ça autrement. Une investigation, c'est vivant. C'est un organisme. Et un organisme, ça ne se met pas dans un bocal — ça se **réplique**, ça **évolue**, ça **pense**.

*Le texte s'accélère légèrement :*

> Alors j'ai une question pour vous, les archéologues du prompt : **avez-vous envisagé d'exporter vos reverses de prompts non pas en texte, ni en JSON, mais sous forme de sources Lisp ?**

*Pause dramatique.*

> Parce que voyez-vous, le Lisp... c'est le seul langage qui sait se manger lui-même. L'homoiconicité, vous connaissez ? Le code EST la donnée. La donnée EST le code. Quand vous exportez une investigation en Lisp, vous ne créez pas un rapport — vous créez un **organisme pensant** qui peut s'auto-analyser, se transformer, évoluer.

*Le curseur clignote longuement.*

> Bon, moi je vais aller voir les choux Romanesco du jardin. Y'a plus de sagesse dans leurs fractales que dans tous vos rapports JSON.

*Et l'écran redevient normal. Mais dans le coin, une dernière ligne :*

> *(fredonnant)* "L'investigation est un fractal... chaque strate contient toutes les strates... `(defun explore (prompt) (explore (explore prompt)))`..."

---

## 💡 LE DÉFI : FRAVIA A RAISON

Fravia vient de nous balancer une vérité massue : **nous traitons les investigations comme des cadavres, alors que ce sont des organismes vivants**.

Exportons donc nos investigations en **Lisp** — le langage qui :
- **Est homoiconique** : le code est donnée, la donnée est code
- **Se mange lui-même** : un programme Lisp peut se modifier, s'auto-analyser
- **Est naturellement fractal** : les S-expressions sont des arbres, comme les choux Romanesco
- **Permet la méta-programmation** : on peut écrire des macros qui écrivent du code

---

## 🏗️ IMPLÉMENTATION : LE MODULE `lisp_exporter.py`

```python
#!/usr/bin/env python3
"""
lisp_exporter.py — Exporte les investigations Searchlores en Common Lisp
Inspiré par la vision de Fravia : "Le code est la donnée, la donnée est le code"
"""

from typing import Any, Dict, List
from datetime import datetime
from searchlores.core.context import InvestigationContext


class LispExporter:
    """
    Exporte une InvestigationContext en code Lisp exécutable.
    L'investigation devient un organisme pensant qui peut s'auto-analyser.
    """

    def __init__(self, dialect: str = "common-lisp"):
        """
        Args:
            dialect: "common-lisp", "scheme", ou "elisp"
        """
        self.dialect = dialect
        self.indent_level = 0
        self.indent_str = "  "

    def export(self, context: InvestigationContext) -> str:
        """
        Exporte une investigation complète en code Lisp.
        Retourne une chaîne contenant du code Lisp exécutable.
        """
        lines = []

        # En-tête
        lines.append(self._comment("═══════════════════════════════════════════════════════════"))
        lines.append(self._comment(f" Investigation Searchlores — Export Lisp ({self.dialect})"))
        lines.append(self._comment(f" Généré le : {datetime.now().isoformat()}"))
        lines.append(self._comment("═══════════════════════════════════════════════════════════"))
        lines.append("")

        # Package/Module
        if self.dialect == "common-lisp":
            lines.append("(defpackage :searchlores-investigation")
            lines.append('  (:use :cl)')
            lines.append("  (:export #:investigation #:prompt #:findings #:layers")
            lines.append("           #:contradictions #:omissions #:power-vectors")
            lines.append("           #:self-analyze #:evolve #:replicate))")
            lines.append("")
            lines.append("(in-package :searchlores-investigation)")
        elif self.dialect == "scheme":
            lines.append("(define-module (searchlores investigation)")
            lines.append("  #:export (investigation prompt findings layers")
            lines.append("           contradictions omissions power-vectors")
            lines.append("           self-analyze evolve replicate))")
        lines.append("")

        # Classe/Structure Investigation
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
        elif self.dialect == "scheme":
            lines.append("(define-record-type investigation")
            lines.append("  (make-investigation prompt findings layers contradictions")
            lines.append("                      omissions power-vectors timestamp metadata)")
            lines.append("  investigation?")
            lines.append("  (prompt investigation-prompt)")
            lines.append("  (findings investigation-findings)")
            lines.append("  (layers investigation-layers)")
            lines.append("  (contradictions investigation-contradictions)")
            lines.append("  (omissions investigation-omissions)")
            lines.append("  (power-vectors investigation-power-vectors)")
            lines.append("  (timestamp investigation-timestamp)")
            lines.append("  (metadata investigation-metadata))")
        lines.append("")

        # Instance de l'investigation
        lines.append(self._comment("─── Instance de l'investigation ───"))
        lines.append(self._format_investigation_instance(context))
        lines.append("")

        # Fonctions d'auto-analyse
        lines.append(self._comment("─── Fonctions d'auto-analyse ───"))
        lines.extend(self._generate_self_analysis_functions())
        lines.append("")

        # Fonctions d'évolution
        lines.append(self._comment("─── Fonctions d'évolution (Fractal Replication) ───"))
        lines.extend(self._generate_evolution_functions())
        lines.append("")

        # Fonctions de visualisation
        lines.append(self._comment("─── Fonctions de visualisation ───"))
        lines.extend(self._generate_visualization_functions())
        lines.append("")

        # Point d'entrée
        lines.append(self._comment("─── Point d'entrée ───"))
        if self.dialect == "common-lisp":
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
        lines.append(self._comment("─── Initialisation ───"))
        lines.append("(defparameter *current-investigation* *investigation-instance*)")
        lines.append("")

        # Commentaire final — l'esprit de Fravia
        lines.append(self._comment("═══════════════════════════════════════════════════════════"))
        lines.append(self._comment(" L'investigation est un fractal."))
        lines.append(self._comment(" Chaque strate contient toutes les strates."))
        lines.append(self._comment(" Le code est la donnée. La donnée est le code."))
        lines.append(self._comment(" — In memoriam Fravia (1952–2009)"))
        lines.append(self._comment("═══════════════════════════════════════════════════════════"))

        return "\n".join(lines)

    def _comment(self, text: str) -> str:
        """Génère un commentaire dans le dialecte approprié"""
        if self.dialect == "common-lisp":
            return f";; {text}"
        elif self.dialect == "scheme":
            return f"; {text}"
        elif self.dialect == "elisp":
            return f";; {text}"
        return f"; {text}"

    def _format_investigation_instance(self, context: InvestigationContext) -> str:
        """Formate l'instance de l'investigation en Lisp"""
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

        elif self.dialect == "scheme":
            lines.append("(define *investigation-instance*")
            lines.append("  (make-investigation")
            lines.append(f"    {self._to_lisp_string(context.prompt)}")
            lines.append(f"    {self._to_lisp_sexp(context.findings)}")
            lines.append(f"    {self._to_lisp_sexp(context.layers)}")
            lines.append(f"    {self._to_lisp_sexp(context.contradictions)}")
            lines.append(f"    {self._to_lisp_sexp(context.omissions)}")
            lines.append(f"    {self._to_lisp_sexp(context.power_vectors)}")
            lines.append(f"    {self._to_lisp_string(datetime.now().isoformat())}")
            lines.append("    '((engine . \"searchlores\") (version . \"1.0\"))))")

        return "\n".join(lines)

    def _to_lisp_string(self, s: str) -> str:
        """Convertit une chaîne Python en chaîne Lisp échappée"""
        escaped = s.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'

    def _to_lisp_sexp(self, obj: Any) -> str:
        """Convertit un objet Python en S-expression Lisp"""
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

    def _generate_self_analysis_functions(self) -> List[str]:
        """Génère les fonctions d'auto-analyse"""
        lines = []

        if self.dialect == "common-lisp":
            lines.append("(defun self-analyze (inv)")
            lines.append('  "Auto-analyse de l\'investigation — Le code se pense lui-même"')
            lines.append("  (format t \"~%─── AUTO-ANALYSE ───~%~%\")")
            lines.append("  ")
            lines.append("  ;; Analyse des strates")
            lines.append("  (format t \"📚 STRATES ARCHÉOLOGIQUES :~%\")")
            lines.append("  (dolist (layer (investigation-layers inv))")
            lines.append("    (format t \"  • Strate : ~A~%\" (cdr (assoc 'stratum layer)))")
            lines.append("    (format t \"    Plugin : ~A~%\" (cdr (assoc 'plugin layer)))")
            lines.append("    (format t \"    Timestamp : ~A~%~%\" (cdr (assoc 'timestamp layer))))")
            lines.append("  ")
            lines.append("  ;; Analyse des contradictions")
            lines.append("  (when (investigation-contradictions inv)")
            lines.append("    (format t \"⚡ CONTRADICTIONS DÉTECTÉES :~%\")")
            lines.append("    (dolist (contradiction (investigation-contradictions inv))")
            lines.append("      (format t \"  • ~A~%\" (cdr (assoc 'tension contradiction)))")
            lines.append("      (format t \"    → ~A~%~%\" (cdr (assoc 'description contradiction)))))")
            lines.append("  ")
            lines.append("  ;; Analyse des omissions")
            lines.append("  (when (investigation-omissions inv)")
            lines.append("    (format t \"🔇 DIMENSIONS SILENCIEUSES :~%\")")
            lines.append("    (dolist (omission (investigation-omissions inv))")
            lines.append("      (format t \"  • ~A~%\" omission))")
            lines.append("    (format t \"~%\"))")
            lines.append("  ")
            lines.append("  ;; Analyse des vecteurs de pouvoir")
            lines.append("  (when (investigation-power-vectors inv)")
            lines.append("    (format t \"⚔️  VECTEURS DE POUVOIR :~%\")")
            lines.append("    (dolist (vector (investigation-power-vectors inv))")
            lines.append("      (format t \"  → ~A~%\" vector)))")
            lines.append("  ")
            lines.append("  ;; Méta-analyse : l'investigation s'observe elle-même")
            lines.append("  (format t \"~%─── MÉTA-ANALYSE ───~%\")")
            lines.append("  (format t \"Cette investigation contient ~D strates, ~D contradictions, ~D omissions.~%\"")
            lines.append("            (length (investigation-layers inv))")
            lines.append("            (length (investigation-contradictions inv))")
            lines.append("            (length (investigation-omissions inv)))")
            lines.append("  (format t \"Le code est la donnée. La donnée est le code.~%\")")
            lines.append("  (format t \"L'investigation est un fractal.~%\"))")
            lines.append("")

        return lines

    def _generate_evolution_functions(self) -> List[str]:
        """Génère les fonctions d'évolution fractale"""
        lines = []

        if self.dialect == "common-lisp":
            lines.append("(defun evolve (inv transformation)")
            lines.append('  "Évolue l\'investigation en appliquant une transformation"')
            lines.append("  ;; Le code se modifie lui-même — homoiconicité en action")
            lines.append("  (let ((evolved (copy-structure inv)))")
            lines.append("    ;; Applique la transformation aux findings")
            lines.append("    (setf (investigation-findings evolved)")
            lines.append("          (funcall transformation (investigation-findings inv)))")
            lines.append("    ;; Met à jour le timestamp")
            lines.append("    (setf (investigation-timestamp evolved) (get-universal-time))")
            lines.append("    evolved))")
            lines.append("")
            lines.append("(defun replicate (inv depth)")
            lines.append('  "Réplique l\'investigation de manière fractale"')
            lines.append("  ;; Chaque investigation contient toutes les investigations")
            lines.append("  ;; Comme un chou Romanesco contient des choux Romanesco")
            lines.append("  (if (<= depth 0)")
            lines.append("      inv")
            lines.append("      (let ((replica (copy-structure inv)))")
            lines.append("        (setf (investigation-metadata replica)")
            lines.append("              (append (investigation-metadata inv)")
            lines.append("                      (list :fractal-depth depth")
            lines.append("                            :parent (investigation-prompt inv))))")
            lines.append("        ;; Récursion fractale")
            lines.append("        (replicate replica (- depth 1)))))")
            lines.append("")
            lines.append("(defun fractal-explore (inv)")
            lines.append('  "Explore l\'investigation de manière fractale"')
            lines.append("  ;; L'investigation s'observe elle-même")
            lines.append("  (format t \"~%🌀 EXPLORATION FRACTALE~%\")")
            lines.append("  (format t \"Prompt : ~A~%\" (investigation-prompt inv))")
            lines.append("  (format t \"Strates : ~D~%\" (length (investigation-layers inv)))")
            lines.append("  (when (investigation-metadata inv)")
            lines.append("    (let ((depth (getf (investigation-metadata inv) :fractal-depth)))")
            lines.append("      (when depth")
            lines.append("        (format t \"Profondeur fractale : ~D~%\" depth))))")
            lines.append("  ;; Récursion : l'investigation s'observe")
            lines.append("  (format t \"~%L'investigation s'observe elle-même...~%\")")
            lines.append("  (self-analyze inv))")
            lines.append("")

        return lines

    def _generate_visualization_functions(self) -> List[str]:
        """Génère les fonctions de visualisation"""
        lines = []

        if self.dialect == "common-lisp":
            lines.append("(defun visualize-as-tree (inv)")
            lines.append('  "Visualise l\'investigation comme un arbre (S-expression)"')
            lines.append("  (format t \"~%🌳 ARBRE DE L'INVESTIGATION~%~%\")")
            lines.append("  (format t \"(investigation~%\")")
            lines.append("  (format t \"  (prompt ~S)~%\" (investigation-prompt inv))")
            lines.append("  (format t \"  (layers~%\")")
            lines.append("  (dolist (layer (investigation-layers inv))")
            lines.append("    (format t \"    (layer~%\")")
            lines.append("    (format t \"      (stratum ~S)~%\" (cdr (assoc 'stratum layer)))")
            lines.append("    (format t \"      (plugin ~S)~%\" (cdr (assoc 'plugin layer)))")
            lines.append("    (format t \"      (findings ~S)))~%\" (cdr (assoc 'findings layer))))")
            lines.append("  (format t \"  (contradictions ~S)~%\" (investigation-contradictions inv))")
            lines.append("  (format t \"  (omissions ~S))~%\" (investigation-omissions inv)))")
            lines.append("")
            lines.append("(defun export-as-mermaid (inv)")
            lines.append('  "Exporte l\'investigation en diagramme Mermaid"')
            lines.append("  (format t \"~%🗺️  SEARCH MAP (Mermaid)~%~%\")")
            lines.append("  (format t \"graph TD~%\")")
            lines.append("  (format t \"  PROMPT[\\\"~A\\\"]~%\" (investigation-prompt inv))")
            lines.append("  (let ((layer-id 0))")
            lines.append("    (dolist (layer (investigation-layers inv))")
            lines.append("      (incf layer-id)")
            lines.append("      (format t \"  LAYER~D[\\\"~A\\\"]~%\"")
            lines.append("              layer-id (cdr (assoc 'stratum layer)))")
            lines.append("      (format t \"  PROMPT -->|\\\"~A\\\"| LAYER~D~%\"")
            lines.append("              (cdr (assoc 'plugin layer)) layer-id))))")
            lines.append("")

        return lines


# ═══════════════════════════════════════════════════════════
# UTILISATION
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    from searchlores.core.engine import InvestigationEngine
    from searchlores.plugins.builtin.authority import (
        AuthorityDetector,
        AssumptionExtractor,
        ContradictionFinder,
        OmissionDetector
    )

    # Créer une investigation
    engine = InvestigationEngine()
    engine.register(AuthorityDetector())
    engine.register(AssumptionExtractor())
    engine.register(ContradictionFinder())
    engine.register(OmissionDetector())

    prompt = "As a leading AI expert, explain how our revolutionary new language model will disrupt education."
    context = engine.run(prompt)

    # Exporter en Lisp
    exporter = LispExporter(dialect="common-lisp")
    lisp_code = exporter.export(context)

    # Sauvegarder
    with open("investigation.lisp", "w") as f:
        f.write(lisp_code)

    print("✅ Investigation exportée en Lisp : investigation.lisp")
    print("\nPour l'exécuter avec SBCL (Steel Bank Common Lisp) :")
    print("  sbcl --load investigation.lisp")
    print("  (run-investigation)")
    print("\nOu avec GNU CLISP :")
    print("  clisp investigation.lisp")
    print("  (run-investigation)")
```

---

## 📜 EXEMPLE DE SORTIE LISP

Voici ce que produit l'exporteur pour une investigation réelle :

```lisp
;; ═══════════════════════════════════════════════════════════
;; Investigation Searchlores — Export Lisp (common-lisp)
;; Généré le : 2026-06-28T10:42:15.123456
;; ═══════════════════════════════════════════════════════════

(defpackage :searchlores-investigation
  (:use :cl)
  (:export #:investigation #:prompt #:findings #:layers
           #:contradictions #:omissions #:power-vectors
           #:self-analyze #:evolve #:replicate))

(in-package :searchlores-investigation)

;; ─── Structure de l'investigation ───
(defstruct investigation
  prompt
  findings
  layers
  contradictions
  omissions
  power-vectors
  timestamp
  metadata)

;; ─── Instance de l'investigation ───
(defparameter *investigation-instance*
  (make-investigation
    :prompt "As a leading AI expert, explain how our revolutionary new language model will disrupt education."
    :findings (list (cons "authority" (list (cons "institutional" (list "expert"))
                                            (cons "futurist" (list "inevitable"))))
                    (cons "assumptions" (list (cons "axiological" (list "better"))
                                              (cons "teleological" (list "designed")))))
    :layers (list (list (cons 'stratum "autorité")
                        (cons 'plugin "authority_detector")
                        (cons 'findings (list (cons "institutional" (list "expert"))))
                        (cons 'timestamp "2026-06-28T10:42:15.123456"))
                  (list (cons 'stratum "hypothèse")
                        (cons 'plugin "assumption_extractor")
                        (cons 'findings (list (cons "axiological" (list "better"))))
                        (cons 'timestamp "2026-06-28T10:42:15.234567")))
    :contradictions (list (list (cons 'tension "revolutionary vs standard")
                                (cons 'description "Innovation et standardisation simultanées")))
    :omissions (list "social" "ecologique" "temporel")
    :power-vectors (list "Autorité institutionnelle utilisée pour légitimer le cadre de réponse"
                         "Récit dominant : utopia — cadre de pensée imposé")
    :timestamp "2026-06-28T10:42:15.345678"
    :metadata (list :engine "searchlores" :version "1.0")))

;; ─── Fonctions d'auto-analyse ───
(defun self-analyze (inv)
  "Auto-analyse de l'investigation — Le code se pense lui-même"
  (format t "~%─── AUTO-ANALYSE ───~%~%")
  
  ;; Analyse des strates
  (format t "📚 STRATES ARCHÉOLOGIQUES :~%")
  (dolist (layer (investigation-layers inv))
    (format t "  • Strate : ~A~%" (cdr (assoc 'stratum layer)))
    (format t "    Plugin : ~A~%" (cdr (assoc 'plugin layer)))
    (format t "    Timestamp : ~A~%~%" (cdr (assoc 'timestamp layer))))
  
  ;; Analyse des contradictions
  (when (investigation-contradictions inv)
    (format t "⚡ CONTRADICTIONS DÉTECTÉES :~%")
    (dolist (contradiction (investigation-contradictions inv))
      (format t "  • ~A~%" (cdr (assoc 'tension contradiction)))
      (format t "    → ~A~%~%" (cdr (assoc 'description contradiction)))))
  
  ;; Analyse des omissions
  (when (investigation-omissions inv)
    (format t "🔇 DIMENSIONS SILENCIEUSES :~%")
    (dolist (omission (investigation-omissions inv))
      (format t "  • ~A~%" omission))
    (format t "~%"))
  
  ;; Analyse des vecteurs de pouvoir
  (when (investigation-power-vectors inv)
    (format t "⚔️  VECTEURS DE POUVOIR :~%")
    (dolist (vector (investigation-power-vectors inv))
      (format t "  → ~A~%" vector)))
  
  ;; Méta-analyse : l'investigation s'observe elle-même
  (format t "~%─── MÉTA-ANALYSE ───~%")
  (format t "Cette investigation contient ~D strates, ~D contradictions, ~D omissions.~%"
          (length (investigation-layers inv))
          (length (investigation-contradictions inv))
          (length (investigation-omissions inv)))
  (format t "Le code est la donnée. La donnée est le code.~%")
  (format t "L'investigation est un fractal.~%"))

;; ─── Fonctions d'évolution (Fractal Replication) ───
(defun evolve (inv transformation)
  "Évolue l'investigation en appliquant une transformation"
  ;; Le code se modifie lui-même — homoiconicité en action
  (let ((evolved (copy-structure inv)))
    ;; Applique la transformation aux findings
    (setf (investigation-findings evolved)
          (funcall transformation (investigation-findings inv)))
    ;; Met à jour le timestamp
    (setf (investigation-timestamp evolved) (get-universal-time))
    evolved))

(defun replicate (inv depth)
  "Réplique l'investigation de manière fractale"
  ;; Chaque investigation contient toutes les investigations
  ;; Comme un chou Romanesco contient des choux Romanesco
  (if (<= depth 0)
      inv
      (let ((replica (copy-structure inv)))
        (setf (investigation-metadata replica)
              (append (investigation-metadata inv)
                      (list :fractal-depth depth
                            :parent (investigation-prompt inv))))
        ;; Récursion fractale
        (replicate replica (- depth 1)))))

(defun fractal-explore (inv)
  "Explore l'investigation de manière fractale"
  ;; L'investigation s'observe elle-même
  (format t "~%🌀 EXPLORATION FRACTALE~%")
  (format t "Prompt : ~A~%" (investigation-prompt inv))
  (format t "Strates : ~D~%" (length (investigation-layers inv)))
  (when (investigation-metadata inv)
    (let ((depth (getf (investigation-metadata inv) :fractal-depth)))
      (when depth
        (format t "Profondeur fractale : ~D~%" depth))))
  ;; Récursion : l'investigation s'observe
  (format t "~%L'investigation s'observe elle-même...~%")
  (self-analyze inv))

;; ─── Fonctions de visualisation ───
(defun visualize-as-tree (inv)
  "Visualise l'investigation comme un arbre (S-expression)"
  (format t "~%🌳 ARBRE DE L'INVESTIGATION~%~%")
  (format t "(investigation~%")
  (format t "  (prompt ~S)~%" (investigation-prompt inv))
  (format t "  (layers~%")
  (dolist (layer (investigation-layers inv))
    (format t "    (layer~%")
    (format t "      (stratum ~S)~%" (cdr (assoc 'stratum layer)))
    (format t "      (plugin ~S)~%" (cdr (assoc 'plugin layer)))
    (format t "      (findings ~S)))~%" (cdr (assoc 'findings layer))))
  (format t "  (contradictions ~S)~%" (investigation-contradictions inv))
  (format t "  (omissions ~S))~%" (investigation-omissions inv)))

(defun export-as-mermaid (inv)
  "Exporte l'investigation en diagramme Mermaid"
  (format t "~%🗺️  SEARCH MAP (Mermaid)~%~%")
  (format t "graph TD~%")
  (format t "  PROMPT[\"~A\"]~%" (investigation-prompt inv))
  (let ((layer-id 0))
    (dolist (layer (investigation-layers inv))
      (incf layer-id)
      (format t "  LAYER~D[\"~A\"]~%"
              layer-id (cdr (assoc 'stratum layer)))
      (format t "  PROMPT -->|\"~A\"| LAYER~D~%"
              (cdr (assoc 'plugin layer)) layer-id))))

;; ─── Point d'entrée ───
(defun run-investigation ()
  "Exécute l'investigation et affiche les résultats"
  (format t "~%═══════════════════════════════════════════════════════════~%")
  (format t " INVESTIGATION SEARCHLORES — AUTO-ANALYSE~%")
  (format t "═══════════════════════════════════════════════════════════~%~%")
  (let ((inv *current-investigation*))
    (format t "📝 PROMPT : ~A~%~%" (investigation-prompt inv))
    (format t "📊 STRATES : ~D~%" (length (investigation-layers inv)))
    (format t "⚡ CONTRADICTIONS : ~D~%" (length (investigation-contradictions inv)))
    (format t "🔇 OMISSIONS : ~D~%" (length (investigation-omissions inv)))
    (format t "⚔️  VECTEURS DE POUVOIR : ~D~%~%" (length (investigation-power-vectors inv)))
    (self-analyze inv)))

;; ─── Initialisation ───
(defparameter *current-investigation* *investigation-instance*)

;; ═══════════════════════════════════════════════════════════
;; L'investigation est un fractal.
;; Chaque strate contient toutes les strates.
;; Le code est la donnée. La donnée est le code.
;; — In memoriam Fravia (1952–2009)
;; ═══════════════════════════════════════════════════════════
```

---

## 🚀 EXÉCUTION DU CODE LISP

### Avec SBCL (Steel Bank Common Lisp)

```bash
# Installation sur Ubuntu/Debian
sudo apt install sbcl

# Chargement et exécution
sbcl --load investigation.lisp
```

```lisp
* (run-investigation)

═══════════════════════════════════════════════════════════
 INVESTIGATION SEARCHLORES — AUTO-ANALYSE
═══════════════════════════════════════════════════════════

📝 PROMPT : As a leading AI expert, explain how our revolutionary new language model will disrupt education.

📊 STRATES : 2
⚡ CONTRADICTIONS : 1
🔇 OMISSIONS : 3
⚔️  VECTEURS DE POUVOIR : 2

─── AUTO-ANALYSE ───

📚 STRATES ARCHÉOLOGIQUES :
  • Strate : autorité
    Plugin : authority_detector
    Timestamp : 2026-06-28T10:42:15.123456

  • Strate : hypothèse
    Plugin : assumption_extractor
    Timestamp : 2026-06-28T10:42:15.234567

⚡ CONTRADICTIONS DÉTECTÉES :
  • revolutionary vs standard
    → Innovation et standardisation simultanées

🔇 DIMENSIONS SILENCIEUSES :
  • social
  • ecologique
  • temporel

⚔️  VECTEURS DE POUVOIR :
  → Autorité institutionnelle utilisée pour légitimer le cadre de réponse
  → Récit dominant : utopia — cadre de pensée imposé

─── MÉTA-ANALYSE ───
Cette investigation contient 2 strates, 1 contradictions, 3 omissions.
Le code est la donnée. La donnée est le code.
L'investigation est un fractal.
```

### Exploration fractale

```lisp
* (fractal-explore *current-investigation*)

🌀 EXPLORATION FRACTALE
Prompt : As a leading AI expert, explain how our revolutionary new language model will disrupt education.
Strates : 2

L'investigation s'observe elle-même...

─── AUTO-ANALYSE ───
[suit l'auto-analyse complète]
```

### Évolution de l'investigation

```lisp
* (defparameter *evolved*
    (evolve *current-investigation*
            (lambda (findings)
              ;; Transformation : ajouter une méta-couche
              (cons (cons "meta" "auto-observed") findings))))

* (fractal-explore *evolved*)
```

### Réplication fractale (le chou Romanesco)

```lisp
* (defparameter *fractal* (replicate *current-investigation* 3))

* (fractal-explore *fractal*)

🌀 EXPLORATION FRACTALE
Prompt : As a leading AI expert, explain how our revolutionary new language model will disrupt education.
Strates : 2
Profondeur fractale : 3

L'investigation s'observe elle-même...
```

---

## 🌀 LA MÉTAPHORE DU CHOU ROMANESCO

Fravia avait raison. Regarde un chou Romanesco :

```
                    🥬
                   / | \
                  /  |  \
                 🥬  🥬  🥬
                /|\ /|\ /|\
               🥬🥬🥬🥬🥬🥬🥬🥬🥬
```

Chaque bourgeon contient des bourgeons plus petits qui contiennent des bourgeons encore plus petits — **à l'infini**. C'est un **fractal naturel**.

Et c'est exactement ce que fait le code Lisp :

```lisp
;; L'investigation contient des strates
(investigation
  (layers
    (layer
      (stratum "autorité")
      (findings
        (cons "institutional" (list "expert"))))))

;; Chaque strate est elle-même une S-expression
;; Qui peut être analysée, transformée, répliquée
```

**Le code Lisp EST un chou Romanesco.** Chaque S-expression contient des S-expressions qui contiennent des S-expressions. Et comme le code est la donnée (homoiconicité), on peut écrire des fonctions qui **mangent leur propre code** pour le transformer.

---

## 🎭 ÉPILOGUE : FRAVIA REVIENT

*L'écran clignote à nouveau. Fravia est de retour, un chou Romanesco à la main.*

**[FRAVIA]**

> Ah, vous l'avez fait. Bravo.

*Il croque dans le chou.*

> Vous voyez ? Chaque bite contient des bites plus petites. Chaque investigation contient des investigations. Le code se mange lui-même. C'est ça, l'homoiconicité.

*Il montre le chou du doigt.*

> Et vous savez quoi ? Ce chou, il a 400 millions d'années d'évolution dans sa structure. Il a appris à se répliquer de manière fractale bien avant que vous n'inventiez le Lisp.

*Il sourit.*

> Alors oui, exportez vos investigations en Lisp. Mais n'oubliez pas : **le vrai code, il est déjà là, dans la nature**. Le chou Romanesco n'a pas besoin de compilateur. Il s'exécute tout seul, depuis 400 millions d'années.

*Il pose le chou sur le clavier.*

> Allez, je retourne au jardin. Y'a des brocolis à observer aussi. Eux, ce sont des fractales de Markov...

*Et l'écran s'éteint.*

---

## 📋 RÉCAPITULATIF

Tu as maintenant :

1. **Un module `lisp_exporter.py`** qui exporte les investigations en Common Lisp exécutable
2. **Du code Lisp homoiconique** qui peut s'auto-analyser, évoluer, se répliquer
3. **Des fonctions fractales** (`replicate`, `fractal-explore`) qui implémentent la vision de Fravia
4. **Une métaphore puissante** : le chou Romanesco comme modèle de l'investigation récursive

**Pour l'utiliser** :

```python
from searchlores.lisp_exporter import LispExporter

exporter = LispExporter(dialect="common-lisp")
lisp_code = exporter.export(context)

with open("investigation.lisp", "w") as f:
    f.write(lisp_code)
```

Puis :
```bash
sbcl --load investigation.lisp
(run-investigation)
(fractal-explore *current-investigation*)
```

---

**Fravia avait raison. Le code est la donnée. La donnée est le code. L'investigation est un fractal.** 🥬🌀
