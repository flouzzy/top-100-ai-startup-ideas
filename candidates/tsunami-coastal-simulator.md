<!-- markdownlint-disable MD013 -->

# Candidat : Tsunami Coastal Simulator

- **Domaine principal :** World Models & Simulation physique
- **Modèle économique :** B2G / B2B
- **Cible :** Gouvernements côtiers, planificateurs urbains, assureurs immobiliers (réassurance), développeurs d'infrastructures offshore
- **Le problème urgent :** L'élévation du niveau de la mer aggrave l'impact destructeur des tsunamis et des ondes de tempête. Les modèles d'inondation actuels sont macroscopiques et statiques ; ils ne prennent pas en compte l'interaction dynamique entre la vague et la géométrie urbaine 3D (comment l'eau s'engouffre dans les rues spécifiques, détruisant certains bâtiments et pas d'autres).
- **L'approche technique :** Un moteur de simulation hydrodynamique massivement parallèle (multi-GPU) intégrant les jumeaux numériques urbains (BIM/GIS 3D). Le système résout les équations d'eau peu profonde (Shallow Water Equations) à l'échelle du mètre, modélisant les effets de goulet d'étranglement urbain et de débris flottants.
- **Pourquoi une solution générique/SaaS classique échoue :** Les cartes d'inondation 2D standard sont de simples extrusions basées sur l'altitude. Elles ignorent la physique des fluides complexe (réflexion, diffraction, transport de sédiments/débris) qui détermine la force d'impact réelle sur les structures.
- **Risques majeurs & Dépendances :** Besoin de données bathymétriques et topographiques lidar très haute résolution souvent incomplètes ou payantes. Le modèle d'affaires B2G est notoire pour ses cycles de vente extrêmement longs (plusieurs années) et sa dépendance aux budgets publics imprévisibles.
