<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : PROTAC Ternary Complex Sim

- **Domaine principal :** Biotech & Bio-informatique
- **Modèle économique :** B2B
- **Cible :** Sociétés pharmaceutiques, startups de drug discovery, CROs.
- **Le problème urgent :** Découvrir des dégradeurs ciblés de protéines (PROTACs) est extrêmement coûteux (des millions par hit). La difficulté majeure n'est pas de trouver les liants, mais de prédire avec précision la stabilité dynamique et la formation du complexe ternaire (Protéine cible - PROTAC - Ligase) in vivo.
- **L'approche technique :** Simulation par réseaux de neurones graphiques géométriques (Geometric GNNs) et modèles génératifs spatio-temporels de la dynamique moléculaire spécifiquement calibrés pour prédire les poses conformationnelles de complexes ternaires massifs, complétée par un laboratoire (wet-lab) pour la validation en boucle fermée.
- **Pourquoi une solution générique/SaaS classique échoue :** Les outils de docking traditionnels (chimie quantique, force fields) sont trop lents et échouent lamentablement sur les structures flexibles des linkers PROTACs. AlphaFold3 donne une vue statique mais ne gère pas la dynamique de dégradation.
- **Risques majeurs & Dépendances :** Besoin critique d'infrastructures de calcul massives, rareté des données expérimentales publiques sur les complexes ternaires, risque technologique sur la précision du modèle face à la complexité biologique réelle.
