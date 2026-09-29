<!-- markdownlint-disable MD013 -->
# Candidat : Fusion Plasma Containment Optimizer

* **Domaine principal :** Deep Tech & Infra (Énergie)
* **Modèle économique :** B2B
* **Cible :** Startups de fusion nucléaire (Tokamaks, Stellarators), laboratoires de recherche gouvernementaux (ITER)
* **Le problème urgent :** Maintenir le plasma en fusion stable (à 100 millions de degrés) nécessite de contrôler des instabilités magnétohydrodynamiques (MHD) chaotiques en temps réel. Les systèmes de contrôle actuels réagissent aux disruptions une fois qu'elles commencent, entraînant souvent la perte du plasma et l'arrêt de la réaction, empêchant la production d'énergie nette.
* **L'approche technique :** Utilisation d'architectures de réseaux neuronaux ultra-rapides (ex: Liquid Neural Networks) déployées sur des puces neuromorphiques ou des FPGA directement couplés aux capteurs magnétiques du réacteur. Le système prédit les instabilités plasma des millisecondes avant qu'elles ne se produisent et ajuste proactivement les bobines magnétiques pour maintenir le confinement.
* **Pourquoi une solution générique/SaaS classique échoue :** La latence tolérable entre la détection et la réaction est de l'ordre de la microseconde. Un modèle d'IA classique dans le cloud, ou même sur un GPU standard, est beaucoup trop lent et non déterministe pour cette boucle de contrôle critique.
* **Risques majeurs & Dépendances :** Le marché est limité à une poignée de méga-projets expérimentaux (TAM réduit à court terme), dépendance totale à l'avancement physique des réacteurs de fusion, et l'extrême difficulté de tester l'algorithme : une erreur peut endommager un réacteur valant des milliards.
