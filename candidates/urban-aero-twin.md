<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Urban Aero Twin

- **Domaine principal :** World Models & Simulation physique
- **Modèle économique :** B2B / B2G
- **Cible :** Opérateurs de drones logistiques (livraison), concepteurs d'eVTOL (taxis volants), autorités de régulation aérienne urbaine.
- **Le problème urgent :** Les drones et eVTOLs rencontrent des micro-turbulences urbaines imprévisibles (effets de canyoning entre les gratte-ciel, rafales soudaines) qui provoquent des crashs et interdisent les vols à basse altitude en environnement dense. Il est impossible de cartographier physiquement l'aérologie complexe d'une ville en temps réel avec des capteurs traditionnels limités.
- **L'approche technique :** Un jumeau numérique (World Model) de la dynamique des fluides (CFD) urbaine, mis à jour en temps réel. Il ingère les données météorologiques macroscopiques, la topologie 3D fine (Lidar) et les données de télémétrie de la flotte pour générer un champ de vecteurs de vent prédictif haute résolution. Les drones interrogent cette API spatiale pour ajuster leurs trajectoires préventivement.
- **Pourquoi une solution générique/SaaS classique échoue :** Résoudre les équations de Navier-Stokes à l'échelle d'une ville prendrait des jours sur un supercalculateur classique. Il faut utiliser des "Neural Operators" (ex: Fourier Neural Operators) pour approximer la physique des fluides en quelques millisecondes, nécessitant une expertise pointue en modélisation mathématique et une infra distribuée spécialisée.
- **Risques majeurs & Dépendances :** Besoin de données topographiques 3D extrêmement précises et continuellement mises à jour, nécessité d'atteindre une précision quasi-parfaite (zéro tolérance au crash), dépendance à l'essor encore incertain du marché de la mobilité aérienne urbaine (UAM).
