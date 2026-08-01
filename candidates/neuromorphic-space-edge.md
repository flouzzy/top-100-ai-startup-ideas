<!-- markdownlint-disable MD013 -->

# Candidat : Neuromorphic Space Edge

- **Domaine principal :** Deep Tech Infra
- **Modèle économique :** B2B
- **Cible :** Les opérateurs de constellations de satellites (observation de la Terre, défense, télécoms) qui gèrent les budgets matériels et qui souffrent des goulots d'étranglement de la bande passante descendante (downlink).
- **Le problème urgent :** Les satellites génèrent des téraoctets de données brutes (images hyperspectrales, radar), mais la bande passante vers la Terre est très limitée et coûteuse. Envoyer des nuages ou de l'océan vide coûte de l'argent et retarde l'analyse d'images critiques (défense, catastrophes naturelles).
- **L'approche technique :** Intégration de puces neuromorphiques (SNN - Spiking Neural Networks) durcies contre les radiations directement sur les satellites (Edge Computing spatial). Ces puces traitent les données optiques/radar en temps réel avec une consommation énergétique ultra-faible (milliwatts) pour ne renvoyer que les anomalies ou cibles pertinentes sur Terre.
- **Pourquoi une solution générique/SaaS classique échoue :** Les GPU/TPU traditionnels ou les logiciels SaaS terrestres sont inutilisables en orbite en raison des contraintes extrêmes de puissance (énergie limitée par les panneaux solaires) et de dissipation thermique, sans compter la vulnérabilité aux radiations cosmiques.
- **Risques majeurs & Dépendances :** Complexité du durcissement contre les radiations (rad-hard), coût de lancement pour la validation en orbite (TRL 7+), et manque d'écosystème logiciel pour compiler des modèles vers du matériel neuromorphique.
