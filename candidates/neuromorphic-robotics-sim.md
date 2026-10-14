<!-- markdownlint-disable MD013 -->
# Candidat : NeuromorphicRoboticsSim

* **Domaine principal :** Robotique & Systèmes embarqués (World Models)
* **Modèle économique :** B2B
* **Cible :** Constructeurs de robots humanoïdes, fabricants de drones autonomes, entreprises de logistique automatisée.
* **Le problème urgent :** L'entraînement de réseaux de neurones pour la robotique nécessitant des réflexes ultra-rapides est limité par l'architecture de calcul classique (Von Neumann), causant une latence trop élevée et une consommation énergétique prohibitive pour l'inférence embarquée.
* **L'approche technique :** Moteur de simulation physique générant synthétiquement des données événementielles (event-based) natives pour entraîner spécifiquement des réseaux de neurones à impulsions (Spiking Neural Networks - SNN) destinés à être déployés sur des puces neuromorphiques (ex: Loihi, Akida).
* **Pourquoi une solution générique/SaaS classique échoue :** Les moteurs comme Unity ou les simulateurs robotiques actuels génèrent des trames visuelles denses, inadaptées pour l'entraînement natif d'architectures asynchrones à impulsions. Il faut créer une pile logicielle et un simulateur pensés dès la conception pour le calcul neuromorphique, gérant les microsecondes de manière déterministe.
* **Risques majeurs & Dépendances :** La rareté et le coût d'accès au hardware neuromorphique, le manque d'outils de compilation pour les SNN, la résistance des équipes d'ingénierie formées au Deep Learning classique.
