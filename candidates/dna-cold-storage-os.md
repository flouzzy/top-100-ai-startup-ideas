<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : DNA Cold Storage OS

- **Domaine principal :** Biotech & Bio-informatique
- **Modèle économique :** B2B
- **Cible :** Fournisseurs de cloud (Hyperscalers), centres d'archives nationales, institutions financières et cinématographiques (conservation à très long terme).
- **Le problème urgent :** L'explosion des données mondiales rend le stockage à froid sur bande magnétique (LTO) ou disques durs non durable (durée de vie limitée à quelques décennies, consommation d'espace et d'énergie, coût de migration perpétuelle des données).
- **L'approche technique :** Création d'un système d'exploitation complet pour le stockage de données sur ADN (DNA Data Storage). Cela inclut un compilateur qui encode les données binaires en séquences ATCG optimisées (pour la correction d'erreurs), et un système d'adressage moléculaire permettant un accès aléatoire (Random Access) lors du séquençage pour la lecture.
- **Pourquoi une solution générique/SaaS classique échoue :** Ce n'est pas un simple format de fichier. Cela nécessite l'orchestration de matériel de synthèse (écriture) et de séquençage (lecture) biologique, avec des algorithmes d'encodage spécifiques pour gérer le taux d'erreur inhérent à la biologie de synthèse.
- **Risques majeurs & Dépendances :** Le coût actuel prohibitif de la synthèse d'ADN (écriture), la latence de lecture, et la forte dépendance envers l'évolution du matériel biotechnologique pour passer à l'échelle commerciale.
