<!-- markdownlint-disable MD013 -->

# Candidat : CRISPR Off-target Predictor

- **Domaine principal :** Biotech & Bio-informatique / IA
- **Modèle économique :** B2B
- **Cible :** Entreprises pharmaceutiques, laboratoires de thérapie génique, startups de biologie synthétique, centres de recherche clinique.
- **Le problème urgent :** L'édition génomique (CRISPR-Cas9 et variantes) est révolutionnaire, mais elle provoque des mutations "off-target" (hors cible) dangereuses et souvent invisibles (mutations silencieuses, oncogenèse). Identifier ces risques nécessite actuellement des mois de tests en laboratoire (wet-lab) coûteux sur des modèles cellulaires, ce qui ralentit le pipeline clinique de plusieurs années et fait échouer des essais à plusieurs millions de dollars.
- **L'approche technique :** Un modèle d'IA fondationnel (transformer/graph neural network) entraîné sur des jeux de données multi-omiques massifs (épigénétique, conformation 3D de la chromatine, séquences génomiques) pour simuler et prédire l'interaction exacte entre le complexe ribonucléoprotéique CRISPR et l'ADN entier d'un patient. Il modélise la thermodynamique de l'hybridation pour cartographier les risques in-silico.
- **Pourquoi une solution générique/SaaS classique échoue :** Les outils de bio-informatique standards reposent sur un alignement de séquences linéaire (heuristique) qui ignore la topologie 3D du génome et les marques épigénétiques dynamiques. Un LLM généraliste ne peut pas calculer la physique de liaison enzymatique moléculaire.
- **Risques majeurs & Dépendances :** Besoin de données d'entraînement de très haute qualité (souvent propriétaires aux labos), validation empirique obligatoire par les agences réglementaires (FDA/EMA) pour que la prédiction in-silico puisse remplacer ou alléger la phase préclinique.
