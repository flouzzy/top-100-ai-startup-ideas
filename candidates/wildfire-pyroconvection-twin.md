<!-- markdownlint-disable MD013 -->
# Candidat : Wildfire Pyroconvection Twin

- **Domaine principal :** World Models / Simulation physique
- **Modèle économique :** B2B / B2G
- **Cible :** Agences forestières, sécurité civile, opérateurs de réseaux électriques, compagnies d'assurance (réassurance)
- **Le problème urgent :** Les modèles actuels prédisent mal le comportement des mégafeux (incendies de 6ème génération) car ils ignorent le micro-climat créé par le feu lui-même (pyroconvection). Cela entraîne des pertes matérielles et humaines imprévisibles, et les assurances refusent de couvrir ces risques sans modélisation précise.
- **L'approche technique :** Développement d'un Neural Physics Engine intégrant la dynamique des fluides computationnelle (CFD) en temps réel avec des réseaux de neurones informés par la physique (PINNs). Le système modélise l'interaction complexe entre la topographie, les carburants forestiers et les panaches thermiques générant leur propre météo.
- **Pourquoi une solution générique/SaaS classique échoue :** Un LLM ne comprend pas les équations de Navier-Stokes. Les outils SaaS SIG (Systèmes d'Information Géographique) sont statiques et ne peuvent pas simuler les boucles de rétroaction thermodynamiques non linéaires en temps réel (il faut calculer la physique, pas faire des requêtes en base de données).
- **Risques majeurs & Dépendances :** Besoin massif en compute (GPU clusters) pour l'entraînement initial, accès aux données satellitaires IR et lidar haute résolution pour calibrer les modèles, temps de validation scientifique (peer-review nécessaire pour rassurer les réassureurs).
