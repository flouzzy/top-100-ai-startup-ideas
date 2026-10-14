<!-- markdownlint-disable MD013 -->
# Candidat : SpaceDebrisCollisionTwin

* **Domaine principal :** Deep Tech & Infra (Spatial)
* **Modèle économique :** B2B
* **Cible :** Opérateurs de constellations satellitaires en orbite basse (LEO), agences spatiales, compagnies d'assurance spatiale.
* **Le problème urgent :** L'encombrement de l'orbite terrestre basse crée un risque exponentiel de collisions (syndrome de Kessler). Les alertes de collision actuelles génèrent trop de faux positifs, forçant les satellites à manœuvrer inutilement, brûlant du carburant précieux et réduisant leur durée de vie.
* **L'approche technique :** Un World Model prédictif fusionnant en temps réel les données de multiples radars terrestres et capteurs optiques spatiaux pour simuler la mécanique orbitale non linéaire complexe. Il utilise l'IA différentiable pour affiner continuellement le calcul des probabilités de collision spatiale.
* **Pourquoi une solution générique/SaaS classique échoue :** La modélisation orbitale nécessite de gérer les perturbations atmosphériques imprévisibles (liées à la météo spatiale), le vent solaire et l'interaction gravitationnelle de milliers de corps, avec une extrême précision. Un LLM ou un SaaS de gestion ne peut modéliser la physique stochastique à très haute vélocité de ce niveau.
* **Risques majeurs & Dépendances :** Accès coûteux et limité aux données brutes des radars militaires (Space Force) et commerciaux, responsabilité énorme en cas de recommandation de "non-manœuvre" qui mènerait à une collision.
