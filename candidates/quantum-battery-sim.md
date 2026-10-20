<!-- markdownlint-disable MD013 -->
# Candidat : QBattSim (Quantum Battery & Material Simulator)

* **Domaine principal :** Quantique / ClimateTech & Énergie
* **Modèle économique :** B2B
* **Cible :** Départements R&D des fabricants de batteries (CATL, Panasonic, Northvolt), constructeurs automobiles (EVs) et entreprises de chimie des matériaux.
* **Le problème urgent :** La découverte de nouveaux matériaux pour les batteries solides (Solid-State Batteries) ou à haute densité énergétique (Sodium-Ion, Lithium-Sulfur) bloque sur la barrière de la simulation. La chimie quantique exacte des interactions moléculaires (VQE, DFT) est incalculable sur les supercalculateurs classiques, forçant des approximations massives qui ralentissent la R&D via des essais et erreurs en laboratoire physique lents et coûteux.
* **L'approche technique :** Plateforme hybride quantique-classique (VQE - Variational Quantum Eigensolver). Elle utilise des algorithmes d'inspiration quantique (Tensor Networks) sur des GPU classiques aujourd'hui, préparés pour s'exécuter sur les NISQ (Noisy Intermediate-Scale Quantum) de demain. Elle simule avec une précision quasi-parfaite la dynamique moléculaire et les mécanismes de dégradation (vieillissement) des nouveaux électrolytes.
* **Pourquoi une solution générique/SaaS classique échoue :** Les logiciels classiques de simulation de matériaux moléculaires utilisent la DFT (Density Functional Theory) qui approche de ses limites théoriques (trop d'approximations pour les matériaux fortement corrélés). Un SaaS LLM est inutile ici ; il s'agit de résoudre des équations de Schrödinger à N corps complexes.
* **Risques majeurs & Dépendances :** La promesse "Hardware-ready" dépend de l'évolution matérielle des ordinateurs quantiques (IBM, IonQ). Sur le court terme, risque de devoir se battre avec les performances pures des géants du calcul intensif (HPC) classique.
