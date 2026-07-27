<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Neural Physics Forge

- **Domaine principal :** World Models & Simulation physique
- **Modèle économique :** B2B
- **Cible :** Constructeurs automobiles, entreprises aérospatiales, fabricants de robotique industrielle.
- **Le problème urgent :** Les simulations physiques traditionnelles (CFD, FEA) nécessitent des clusters HPC massifs et prennent des jours pour calculer l'aérodynamique, la résistance des matériaux ou la dynamique des fluides, ralentissant considérablement le cycle de R&D.
- **L'approche technique :** Moteur de "Neural Physics" utilisant des Graph Neural Networks (GNN) et des Physics-Informed Neural Networks (PINN) entraînés sur des données de solveurs exacts, pour inférer des résultats de simulation avec une précision de 99% mais 10 000 fois plus rapidement.
- **Pourquoi une solution générique/SaaS classique échoue :** Un LLM textuel ne comprend pas la géométrie 3D, les lois de Navier-Stokes ou les tenseurs de contrainte. Il faut une architecture de modèle spécifique, optimisée pour des maillages non structurés 3D et des formats de CAO complexes.
- **Risques majeurs & Dépendances :** Besoin initial de données de simulation de haute qualité et extrêmement coûteuses à générer pour l'entraînement; scepticisme des ingénieurs traditionnels quant à la précision ("hallucinations physiques").
