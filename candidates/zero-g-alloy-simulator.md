<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Zero-G Alloy Simulator

- **Domaine principal :** Deep Tech & Infra / Matériaux avancés
- **Modèle économique :** B2B
- **Cible :** Startups d'in-space manufacturing (ex: Varda Space), agences spatiales, industriels de l'aéronautique et des semi-conducteurs.
- **Le problème urgent :** La fabrication de nouveaux matériaux (alliages métalliques parfaits, fibres optiques ZBLAN sans défauts, cristaux pharmaceutiques) en microgravité offre des propriétés impossibles sur Terre. Cependant, envoyer des expériences physiques dans l'espace pour tester des hypothèses de cristallisation coûte des dizaines de millions de dollars et des mois d'attente. L'itération matérielle est trop lente.
- **L'approche technique :** Un jumeau numérique thermodynamique (World Model) simulant la dynamique des fluides computationnelle (CFD) et la cristallogenèse dans des environnements de microgravité ou de gravité partielle (Lune, Mars). Utilisation de réseaux de neurones informés par la physique (PINNs) pour accélérer massivement la simulation des changements de phase et de la tension superficielle hors gravité terrestre.
- **Pourquoi une solution générique/SaaS classique échoue :** Les logiciels de CAO ou de simulation multiphysique classiques (COMSOL, Ansys) sont calibrés empiriquement pour la gravité terrestre à 1G. Leurs solvers sont trop lents et souvent imprécis pour l'exploration rapide du vaste espace des hyper-paramètres des nouveaux alliages spatiaux.
- **Risques majeurs & Dépendances :** Validation expérimentale requise (besoin d'accords avec les opérateurs de stations spatiales privées pour confronter les prédictions IA aux résultats physiques réels en orbite). Taille très réduite du marché adressable actuel (TAM émergent).
