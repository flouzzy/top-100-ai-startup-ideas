<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : Hypersonic Neuromorphic Tracker

* **Domaine principal :** Deep Tech Infra & Robotique
* **Modèle économique :** B2G / B2B
* **Cible :** Défense (Systèmes d'interception anti-missiles), Agences aérospatiales, Systèmes de protection orbitale.
* **Le problème urgent :** Les caméras traditionnelles, basées sur des fréquences d'images fixes, génèrent trop de données redondantes et ont une latence trop élevée pour détecter et suivre des objets se déplaçant à des vitesses hypersoniques (Mach 5+), comme des missiles avancés ou des micro-météorites en orbite.
* **L'approche technique :** Un système de vision neuromorphique embarqué (caméras événementielles couplées à un réseau de neurones à impulsions / SNN sur puce ASIC spécialisée). Le système ne réagit qu'aux changements asynchrones de luminosité à l'échelle de la microseconde, filtrant le bruit statique et offrant un suivi de cible ultra-rapide et économe en énergie.
* **Pourquoi une solution générique/SaaS classique échoue :** Les systèmes de Computer Vision classiques (CNNs sur GPUs) souffrent du goulot d'étranglement de von Neumann. Transférer des images matricielles de la caméra vers la mémoire puis vers le processeur prend trop de temps. Le calcul doit être asynchrone, parcimonieux et localisé directement à côté du capteur.
* **Risques majeurs & Dépendances :** Manque de maturité de l'écosystème logiciel pour les SNNs (Spiking Neural Networks), difficulté à fabriquer des ASICs neuromorphiques performants, marché restreint principalement aux budgets de défense très complexes à pénétrer.
