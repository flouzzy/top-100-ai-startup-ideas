<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : Microgravity Manufacturing Sim

- **Domaine principal :** World Models & Simulation physique
- **Modèle économique :** B2B
- **Cible :** Agences spatiales (NASA, ESA), startups spatiales de fabrication en orbite (In-Space Manufacturing), entreprises biopharmaceutiques et fabricants de semi-conducteurs.
- **Le problème urgent :** La fabrication de certains produits critiques (fibres optiques parfaites ZBLAN, cristallisation de protéines pour médicaments, semi-conducteurs sans défauts) est entravée par la gravité terrestre (convection, sédimentation). Fabriquer en orbite est la solution, mais chaque essai physique dans l'espace coûte des millions de dollars par lancement.
- **L'approche technique :** Un moteur de simulation multiphysique (fluides, thermique, cristallisation) spécifiquement conçu pour l'environnement de microgravité et le vide spatial. Il permet de prototyper et d'optimiser virtuellement les processus de fabrication avant d'envoyer la payload en orbite.
- **Pourquoi une solution générique/SaaS classique échoue :** Les logiciels de CAO/IA classiques sont calqués sur des lois physiques impliquant la gravité terrestre constante (1G). Retirer la gravité ou la modéliser de façon dynamique (micro-vibrations de l'ISS) modifie fondamentalement les équations de Navier-Stokes et nécessite un moteur physique spécialisé.
- **Risques majeurs & Dépendances :** Marché encore naissant dépendant de la baisse continue des coûts de lancement spatial (SpaceX, etc.), et difficulté extrême de validation croisée avec des expériences réelles en microgravité (qui restent rares).
