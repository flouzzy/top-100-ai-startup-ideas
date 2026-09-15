<!-- markdownlint-disable MD013 -->

# Candidat : Xenotransplantation Immune Sim

- **Domaine principal :** Biotech & Bio-informatique
- **Modèle économique :** B2B
- **Cible :** Entreprises de xénotransplantation, instituts de recherche en édition génomique (CRISPR), hôpitaux de recherche
- **Le problème urgent :** L'édition génomique d'organes d'animaux (ex: cœur de porc) pour la transplantation humaine fait face à la barrière mortelle du rejet hyperaigu et des virus endogènes. Les tests in-vivo sont lents, chers, éthiquement complexes et ne permettent pas de tester des milliers de combinaisons d'éditions génétiques.
- **L'approche technique :** Une plateforme de simulation multi-omique et d'immunologie in-silico. Elle modélise la cascade du complément humain et l'interaction des antigènes porcins (PERVs, Alpha-gal) avec le système immunitaire humain au niveau moléculaire en utilisant des réseaux de neurones graphiques (GNN) et de la dynamique moléculaire.
- **Pourquoi une solution générique/SaaS classique échoue :** Un LLM ne peut pas modéliser le repliement des protéines ni les réactions en cascade de l'immunologie complexe multi-espèces. Il faut un moteur de physique bio-moléculaire et des données d'entraînement omiques hautement propriétaires.
- **Risques majeurs & Dépendances :** Besoin critique de données cliniques de haute qualité (souvent secrètes ou inexistantes), complexité computationnelle extrême de la simulation du système immunitaire humain entier, barrières réglementaires FDA massives.
