<!-- markdownlint-disable MD013 -->
# Candidat : Space Debris Collision Twin

* **Domaine principal :** Deep Tech & Infra
* **Modèle économique :** B2B / B2G
* **Cible :** Opérateurs de constellations satellitaires (Starlink, Kuiper), agences spatiales (ESA, NASA), assurances spatiales
* **Le problème urgent :** L'orbite terrestre basse (LEO) est saturée. Le syndrome de Kessler (réaction en chaîne de collisions de débris) menace l'économie spatiale. Les bases de données de suivi actuelles manquent de précision orbitale et prédisent trop de "faux positifs", forçant les satellites à gaspiller de l'ergol précieux pour des manœuvres d'évitement inutiles.
* **L'approche technique :** Un moteur de prédiction orbitale couplant des données de radars spatiaux hétérogènes avec un modèle de propagation orbitale assisté par IA. Il simule en temps continu la trajectoire de millions de débris millimétriques avec un calcul d'incertitude bayésien pour fournir des alertes de collision (TCA) avec une précision de l'ordre du mètre.
* **Pourquoi une solution générique/SaaS classique échoue :** Les perturbations orbitales (pression de radiation solaire, traînée atmosphérique imprévisible due à la météo spatiale) exigent des solveurs d'astrodynamique non-linéaires massifs. Les algorithmes d'apprentissage machine standards ne conservent pas l'énergie et la quantité de mouvement sur le long terme.
* **Risques majeurs & Dépendances :** Accès classifié ou très coûteux aux données des capteurs radars souverains (US Space Command), responsabilité en cas de collision non prédite, marché fortement dépendant de la régulation internationale sur la gestion du trafic spatial (STM).
