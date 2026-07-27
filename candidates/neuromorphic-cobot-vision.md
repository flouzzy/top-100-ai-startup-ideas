<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : SpikingSight Robotics

- **Domaine principal :** Robotique & Systèmes embarqués / IA / Deep Tech
- **Modèle économique :** B2B (Vente de hardware/modules + licence logicielle)
- **Cible :** Fabricants de robots collaboratifs (cobots), drones industriels autonomes, logistique d'entrepôt ultra-rapide.
- **Le problème urgent :** Les systèmes de vision par ordinateur basés sur des caméras standards (RGB) génèrent 30 à 60 images complètes par seconde, saturant la bande passante et la puissance de calcul embarquée. Pour des robots évoluant très rapidement dans des environnements dynamiques, cela induit une latence fatale (motion blur, délais de réaction) et vide les batteries à cause du traitement GPU lourd.
- **L'approche technique :** L'intégration de capteurs de vision événementielle (Event-based cameras / Neuromorphic sensors) où chaque pixel est indépendant et ne signale qu'un changement de luminosité (micros-secondes). Couplé avec des Spiking Neural Networks (SNNs) asynchrones exécutés sur des puces neuromorphiques (ex: Akida, Loihi) pour traiter le flux de données clairsemé avec une consommation d'énergie de l'ordre du milliwatt et une latence quasi-nulle.
- **Pourquoi une solution générique/SaaS classique échoue :** Les frameworks IA actuels (PyTorch, TensorFlow) sont conçus pour des tenseurs denses et synchrones sur GPU. Le SaaS cloud ajoute de la latence réseau interdisant tout asservissement réactif d'un bras robotique. L'innovation requiert une refonte complète de la pile logicielle (vers l'asynchrone par événements) au plus près du capteur.
- **Risques majeurs & Dépendances :** Les SNNs sont notoirement difficiles à entraîner (la rétropropagation classique de gradient ne fonctionne pas directement sur les "spikes" discrets). Écosystème matériel neuromorphique encore jeune et coûteux.
