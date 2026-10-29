<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : Orbital Debris Swarm Nav

* **Domaine principal :** Robotique / Deep Tech Infra
* **Modèle économique :** B2B / B2G
* **Cible :** Agences spatiales (ESA, NASA, JAXA), opérateurs de méga-constellations (Starlink, Kuiper), entreprises d'assurance spatiale.
* **Le problème urgent :** L'orbite basse (LEO) est encombrée de débris spatiaux (Syndrome de Kessler). Un seul débris millimétrique peut détruire un satellite de plusieurs millions. Les missions de nettoyage prévues impliquent des robots unitaires coûteux contrôlés depuis la Terre avec une forte latence. Une collision en chaîne lors du nettoyage pourrait aggraver le problème.
* **L'approche technique :** Création d'un système de navigation décentralisée (Swarm Navigation) pour des flottes de micro-satellites nettoyeurs. Chaque unité utilise l'Edge AI et des capteurs de vision spatiale (LIDAR/caméras) pour ajuster sa trajectoire en temps réel, capturer des débris multiples, et éviter les collisions, sans attendre les commandes de la Terre (qui souffrent de latence et de fenêtres de communication limitées).
* **Pourquoi une solution générique/SaaS classique échoue :** La mécanique orbitale requiert un calcul de trajectoire 6-DOF (degrés de liberté) en microgravité à plus de 28 000 km/h. Un algorithme de routage classique (comme pour des drones terrestres) échoue totalement à modéliser la dynamique orbitale non-képlérienne complexe et les contraintes de carburant extrêmement strictes des engins spatiaux.
* **Risques majeurs & Dépendances :** Réglementation spatiale très floue sur la propriété et la capture des débris (qui a le droit d'attraper le vieux satellite d'un autre pays ?). Coûts de lancement en orbite pour prouver le concept (PoC ultra-coûteux). Risque d'aggraver le problème si un satellite nettoyeur explose.
