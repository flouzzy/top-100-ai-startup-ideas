<!-- markdownlint-disable MD013 MD028 MD033 MD036 MD039 MD041 MD060 -->
# Candidat : Legacy Twin

* **Modèle économique :** B2B
* **Cible :** DSI, architectes cloud et équipes de modernisation IT des grandes entreprises (banques, assurances, institutions) qui migrent leurs systèmes Legacy (COBOL, Fortran).
* **Le problème urgent :** L'IA est utilisée pour traduire massivement du code Legacy vers des langages modernes, mais les entreprises n'osent pas déployer ce code généré car il est impossible de garantir qu'il reproduit exactement la même logique métier complexe et les mêmes cas particuliers. Les tests de validation manuels coûtent plus cher et prennent plus de temps que la traduction elle-même.
* **L'approche technique :** Un moteur d'exécution symbolique et de "fuzzing" différentiel. Le système ingère le code Legacy et sa version traduite, génère automatiquement des millions de scénarios de test via des solveurs SMT, et compare les états de mémoire et les sorties des deux systèmes en parallèle pour garantir une équivalence sémantique stricte.
* **Pourquoi ChatGPT/Gemini échoue seul :** Un LLM peut traduire la syntaxe d'un langage à un autre, mais il ne peut ni exécuter le code, ni prouver formellement une équivalence d'état. La preuve d'équivalence nécessite des solveurs mathématiques déterministes (SMT) et une infrastructure de fuzzing, ce qu'un modèle probabiliste textuel ne peut pas accomplir.
