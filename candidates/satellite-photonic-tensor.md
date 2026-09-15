<!-- markdownlint-disable MD013 -->

# Candidat : Satellite Photonic Tensor

- **Domaine principal :** Deep Tech & Infra (Spatial)
- **Modèle économique :** B2B
- **Cible :** Opérateurs de constellations LEO (Starlink, Kuiper), agences de renseignement géospatial, et fournisseurs de données d'observation de la Terre.
- **Le problème urgent :** Les satellites LEO capturent des pétaoctets de données brutes (images hyperspectrales, SAR) mais sont limités par la bande passante descendante (downlink) pour les renvoyer sur Terre. Traiter ces données à bord avec des GPU classiques nécessite trop de puissance (Watts) et génère une chaleur impossible à dissiper dans le vide spatial.
- **L'approche technique :** Développement d'unités de calcul tensoriel photoniques (Photonic Tensor Cores) spatialisées. Ces puces calculent les multiplications de matrices pour les réseaux de neurones (ex: détection d'anomalies, compression intelligente) à la vitesse de la lumière, avec une consommation énergétique et thermique quasi nulle par rapport au silicium traditionnel.
- **Pourquoi une solution générique/SaaS classique échoue :** L'optimisation logicielle des modèles (quantization, pruning) a atteint ses limites physiques. Seule une rupture au niveau de l'architecture matérielle (utiliser des photons au lieu d'électrons) permet de franchir le mur de l'énergie et de la dissipation thermique dans les environnements spatiaux extrêmes (SWaP-C).
- **Risques majeurs & Dépendances :** Tolérance aux radiations spatiales des composants photoniques (Single Event Effects), alignement sub-nanométrique des fibres et guides d'ondes soumis aux vibrations de lancement, maturité des fonderies photoniques (silicon photonics).
