<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : V2X Orchestrator for Autonomous Fleets

- **Domaine principal :** Robotique / IA
- **Modèle économique :** B2B2C / M2M
- **Cible :** Opérateurs de flottes de véhicules autonomes (Waymo, Cruise), logisticiens longue distance, mairies (smart cities).
- **Le problème urgent :** Les véhicules autonomes actuels fonctionnent en silo ("ego-vehicles"). Aux intersections complexes, dans le brouillard, ou face à des travaux non cartographiés, ils se bloquent (phantom jams) car leurs capteurs locaux sont limités (pas de visibilité à l'aveugle). Cela ruine l'efficacité économique des robotaxis.
- **L'approche technique :** Une infrastructure cloud-edge V2X (Vehicle-to-Everything) permettant le partage de perception brute (Nuages de points LiDAR compressés, prédictions d'intentions) entre véhicules multimarques en moins de 10 millisecondes. Création d'un "essaim" où chaque voiture voit à travers les capteurs des autres via un consensus distribué.
- **Pourquoi une solution générique/SaaS classique échoue :** Une API cloud standard a une latence de 50-100ms, ce qui est mortel à 100 km/h. Il faut une architecture de compression neuronale extrême à la périphérie (edge computing) et une pile réseau déterministe (5G URLLC) que le web traditionnel ne gère pas.
- **Risques majeurs & Dépendances :** Manque d'interopérabilité et de standards entre les constructeurs (Tesla vs Waymo). Couverture et fiabilité des réseaux 5G (dépendance aux Telcos). Sécurité contre l'injection de fausses données (ghost vehicles).
