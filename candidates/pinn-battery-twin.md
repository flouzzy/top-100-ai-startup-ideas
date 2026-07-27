<!-- markdownlint-disable MD013 -->

# Candidat : ElectroTwin PINN

- **Domaine principal :** ClimateTech & Énergie / World Models
- **Modèle économique :** B2B
- **Cible :** Constructeurs automobiles (EV), fabricants de cellules (Gigafactories), opérateurs de stockage réseau (Grid Storage).
- **Le problème urgent :** Le vieillissement prématuré des batteries Li-ion et Solid-State provoque des risques d'incendie (emballement thermique) et des dégradations de capacité imprévisibles, entraînant des rappels coûteux et une sur-conception (surpoids) des packs.
- **L'approche technique :** Jumeau numérique électrochimique via des Physics-Informed Neural Networks (PINNs). Ce modèle ingère la télémétrie BMS (tension, courant, température) et résout en temps réel les équations de diffusion ionique (équations de Newman) pour prédire l'état de santé (SoH) interne et la formation de dendrites.
- **Pourquoi une solution générique/SaaS classique échoue :** Les modèles purement basés sur les données (Data-Driven ML) échouent sur les cas marginaux (edge cases thermiques). Les simulations physiques classiques (FEM/COMSOL) sont impossibles à exécuter en temps réel dans un véhicule (trop de calculs).
- **Risques majeurs & Dépendances :** Accès limité aux données de télémétrie haute résolution des BMS (Battery Management Systems) propriétaires des constructeurs, variabilité de la chimie des cellules d'un fournisseur à l'autre.
