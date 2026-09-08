<!-- markdownlint-disable MD013 -->

# Candidat : Orbital Laser Ablation Debris Predictor

- **Domaine principal :** World Models & Simulation physique / Deep Tech Infra
- **Modèle économique :** B2B / B2G
- **Cible :** Agences spatiales (ESA, NASA), opérateurs de constellations satellitaires en orbite basse (LEO) et startups de nettoyage de l'espace.
- **Le problème urgent :** Le nettoyage des débris spatiaux via ablation laser (tirer un laser depuis le sol ou l'espace pour vaporiser une partie du débris et modifier son orbite) crée de la matière éjectée (plasma et fragments microscopiques). Cette éjection crée une impulsion mais génère aussi un micro-nuage secondaire dont la trajectoire est chaotique et menace les autres satellites. Prévoir cette dispersion thermique et cinétique en LEO est actuellement trop lent et imprécis.
- **L'approche technique :** Un modèle génératif spatio-temporel simulant la dynamique d'ablation laser dans le vide et la dispersion du panache plasma/débris en microgravité. Il couple des solveurs hydrodynamiques radiatifs avec des réseaux de neurones informés par la physique (PINNs) pour fournir un jumeau numérique en temps réel du tir laser et de ses conséquences orbitales à 10 minutes, 1 heure et 24 heures.
- **Pourquoi une solution générique/SaaS classique échoue :** L'interaction laser-matière dans le vide spatial implique des transitions de phase complexes (solide à plasma) et des effets de pression de radiation. Les simulateurs orbitaux (comme STK) ne modélisent pas la thermodynamique de l'ablation à l'échelle moléculaire, et les SaaS IA standards n'ont aucune notion de la physique des plasmas.
- **Risques majeurs & Dépendances :** Dépendance aux matériaux exacts des débris visés (souvent inconnus ou dégradés). Validation expérimentale extrêmement coûteuse et limitée (nécessite des tests en chambre à vide ou des tirs en orbite réels pour calibrer le modèle).
