<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Tensegrity OS

- **Domaine principal :** Robotique & Systèmes embarqués
- **Modèle économique :** B2B
- **Cible :** Agences spatiales, logistique en milieux dangereux, inspection d'infrastructures souterraines/effondrées
- **Le problème urgent :** Les robots traditionnels rigides se brisent lors d'impacts imprévus, tandis que les robots mous sont trop lents. Les robots basés sur la tenségrité (câbles et tiges) peuvent absorber d'énormes chocs mais sont atrocement complexes à contrôler de manière autonome.
- **L'approche technique :** Système d'exploitation (OS) dédié couplé à une puce neuromorphique embarquant un solveur de dynamique non linéaire temps réel, permettant un contrôle proprioceptif décentralisé de la locomotion et de la déformation élastique.
- **Pourquoi une solution générique/SaaS classique échoue :** Le contrôle d'un robot de tenségrité exige un traitement temps réel embarqué sans latence (edge computing) avec des modèles de physique complexes impossibles à déléguer au cloud ou à gérer avec des contrôleurs PID classiques.
- **Risques majeurs & Dépendances :** Hardware très spécifique à co-développer, complexité mécanique de la miniaturisation des actuateurs, marché d'adoption initiale de niche.
