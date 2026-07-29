<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : RNA Tertiary Structure Sim

- **Domaine principal :** Biotech & Bio-informatique
- **Modèle économique :** B2B
- **Cible :** Startups de thérapies à base d'ARN (ARNm, ARNi), laboratoires pharmaceutiques développant des vaccins de nouvelle génération.
- **Le problème urgent :** Contrairement à l'ADN (stable et prévisible), l'ARN monocaténaire se replie sur lui-même en structures 3D (tertiaires) très complexes et instables. Prédire ces structures est crucial pour la conception de médicaments, mais AlphaFold et les modèles actuels sont focalisés sur les protéines, laissant les structures de l'ARN (pseudoknots, etc.) largement insolubles et empêchant l'émergence de nouvelles classes thérapeutiques.
- **L'approche technique :** Un modèle d'apprentissage profond géométrique (Geometric Deep Learning) spécifiquement entraîné sur les données de cryo-microscopie électronique (Cryo-EM) de l'ARN et la modélisation de la thermodynamique de l'appariement des bases de l'ARN, permettant de prédire le paysage de repliement 3D (et ses multiples conformations stables) des séquences d'ARN en quelques secondes.
- **Pourquoi une solution générique/SaaS classique échoue :** L'ARN ne se replie pas selon les mêmes lois thermodynamiques et règles de séquence que les acides aminés des protéines. Les algorithmes d'IA génériques textuels ou visuels ne peuvent pas appréhender la mécanique quantique/physique des interactions à 3 corps spécifiques à l'ARN.
- **Risques majeurs & Dépendances :** Manque sévère de données d'entraînement de haute qualité (il existe beaucoup moins de structures d'ARN résolues expérimentalement que de structures protéiques dans la PDB), coût très élevé du séquençage et des essais en laboratoire humide (wet-lab) pour valider les prédictions.
