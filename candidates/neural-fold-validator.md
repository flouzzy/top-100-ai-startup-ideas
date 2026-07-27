<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Neural Fold Validator

- **Domaine principal :** Biotech & Bio-informatique
- **Modèle économique :** B2B
- **Cible :** Entreprises pharmaceutiques, laboratoires de recherche en biologie synthétique (CSOs, Directeurs R&D).
- **Le problème urgent :** Les modèles génératifs comme AlphaFold génèrent des millions de structures protéiques potentielles, mais plus de 90% échouent en laboratoire (wet-lab) en raison de problèmes de solubilité, de toxicité ou de mauvais repliement dynamique (folding) en milieu aqueux. Synthétiser et tester chaque protéine coûte des millions de dollars et des années d'essais in vitro gaspillés.
- **L'approche technique :** Un moteur de simulation de dynamique moléculaire (Molecular Dynamics - MD) accéléré par réseaux de neurones (Neural Physics Engine) qui valide les prédictions structurelles. Il simule le repliement de la protéine dans un solvant réel, intégrant les forces interatomiques, à une fraction du coût en calcul des simulateurs classiques, servant de filtre de viabilité avant l'entrée en wet-lab.
- **Pourquoi une solution générique/SaaS classique échoue :** Un LLM ne comprend pas les lois de la thermodynamique ni les interactions électrostatiques complexes au niveau atomique. Il faut des pipelines d'intégration MLOps lourds croisant des modèles de graphes (GNN) avec des solveurs d'équations différentielles stochastiques sur des clusters de GPU spécialisés.
- **Risques majeurs & Dépendances :** Besoin massif en puissance de calcul (GPU/TPU) pour l'entraînement du surrogate model, complexité de l'accès aux données expérimentales de haute qualité (Cryo-EM) pour la validation croisée, et difficulté d'adoption par les biologistes traditionnels.
