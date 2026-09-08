<!-- markdownlint-disable MD013 -->

# Candidat : Phage Tail-Fiber Binding Simulator

- **Domaine principal :** Biotech & Bio-informatique
- **Modèle économique :** B2B
- **Cible :** Pharmas développant des thérapies phagiques (pour contrer l'antibiorésistance), startups en microbiome, agriculture (traitements phytosanitaires bactériens).
- **Le problème urgent :** L'antibiorésistance croissante nécessite des bactériophages (virus tueurs de bactéries) sur mesure. Cependant, concevoir un phage qui cible une souche bactérienne pathogène spécifique est un processus lent d'essais-erreurs in vitro. Le goulot d'étranglement est la conception des protéines des "fibres caudales" (tail fibers) du phage, qui doivent se lier parfaitement aux récepteurs de surface de la bactérie, tout en évitant le système immunitaire humain.
- **L'approche technique :** Une plateforme logicielle utilisant des modèles de diffusion structurale et de la prédiction conformationnelle d'assemblages protéiques (type AlphaFold 3 orienté dynamiques de liaison). Elle simule spécifiquement l'affinité de liaison (binding affinity) des fibres caudales virales avec divers lipopolysaccharides (LPS) bactériens, permettant de générer in silico des phages hyper-spécifiques et d'optimiser leur capacité d'infection.
- **Pourquoi une solution générique/SaaS classique échoue :** L'ingénierie des protéines virales exige la modélisation de grandes macromolécules flexibles et d'interactions complexes protéines-glucides (LPS), ce que les outils standards de docking moléculaire pour les petites molécules gèrent très mal.
- **Risques majeurs & Dépendances :** Le repliement protéique in silico ne garantit pas la viabilité biologique complète du phage synthétisé (le phage peut ne pas s'assembler correctement in vivo). Dépendance aux capacités de synthèse ADN haute-fidélité pour les tests in vitro.
