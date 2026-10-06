<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : Tokamak Plasma Neural Predictor

* **Domaine principal :** ClimateTech & Énergie
* **Modèle économique :** B2B
* **Cible :** Entreprises privées de fusion nucléaire (ex: Commonwealth Fusion Systems), Laboratoires de recherche (ITER).
* **Le problème urgent :** Maintenir la stabilité du plasma (magnétohydrodynamique) dans un réacteur à fusion (Tokamak/Stellarator) est l'un des défis d'ingénierie les plus complexes. Les instabilités (disruptions) peuvent détruire les parois du réacteur en quelques millisecondes, mais les simulations MHD de haute fidélité prennent des jours à s'exécuter sur des supercalculateurs.
* **L'approche technique :** Un modèle IA prédictif de substitution (Physics-Informed Neural Network) capable de simuler l'évolution tridimensionnelle du plasma et de prédire les instabilités jusqu'à 100 millisecondes à l'avance, en temps réel. Ce modèle permet au contrôleur magnétique de réagir assez vite pour éviter l'effondrement du plasma.
* **Pourquoi une solution générique/SaaS classique échoue :** Les LLMs ou modèles d'apprentissage profond standard échouent à modéliser des systèmes physiques chaotiques obéissant à des équations de conservation strictes. Seule une approche IA contrainte par la physique (PINN) ou un Neural Operator couplé étroitement au système de contrôle magnétique ultra-rapide peut réussir.
* **Risques majeurs & Dépendances :** Dépendance au succès très hypothétique et lointain de la fusion nucléaire commerciale, accès limité aux données expérimentales des rares réacteurs existants, complexité extrême d'intégration avec des actionneurs magnétiques supraconducteurs.
