<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : Exascale Climate Emulator

- **Domaine principal :** World Models / ClimateTech
- **Modèle économique :** B2B / B2G
- **Cible :** Assureurs (réassurance), fonds d'infrastructures, urbanistes, et gouvernements nécessitant des prévisions hyper-locales des risques climatiques physiques.
- **Le problème urgent :** Les modèles climatiques globaux (GCM) actuels tournent sur des grilles de résolution grossières (ex: 50-100 km). Ils sont incapables de prédire avec précision l'impact micro-local (ex: inondation d'un quartier spécifique, stress thermique d'une usine), rendant la tarification du risque et la conception des infrastructures aveugles à la réalité du terrain.
- **L'approche technique :** Remplacement des solveurs différentiels déterministes par des réseaux neuronaux d'émulation (Machine Learning Emulators). En s'entraînant sur des décennies de données d'observation et de calculs exascale haute résolution, le modèle génère des simulations probabilistes régionales à l'échelle du mètre, 10 000 fois plus rapidement qu'un supercalculateur classique.
- **Pourquoi une solution générique/SaaS classique échoue :** Résoudre les équations de Navier-Stokes pour l'atmosphère à l'échelle globale requiert des clusters HPC hors de portée d'une startup classique. Seule une approche hybride (AI-surrogate models) permet de compresser cette complexité physique en un temps d'inférence viable.
- **Risques majeurs & Dépendances :** Qualité et densité des données satellites/radars nécessaires pour l'entraînement. Risque d'hallucination physique du réseau de neurones lors de conditions extrêmes hors-distribution (Black Swans).
