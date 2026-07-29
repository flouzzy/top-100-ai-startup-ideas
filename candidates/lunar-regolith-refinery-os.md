<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Lunar Regolith Refinery OS

- **Domaine principal :** Robotique & Systèmes embarqués
- **Modèle économique :** B2B
- **Cible :** Agences spatiales (NASA, ESA), startups du New Space de minage spatial, constructeurs de bases lunaires.
- **Le problème urgent :** L'établissement d'une base lunaire permanente nécessite la production d'oxygène, d'eau et de matériaux de construction in-situ (In-Situ Resource Utilization - ISRU) à partir de la poussière lunaire (régolithe). Les processus de raffinage sont hautement instables à cause de la gravité réduite (1/6g), du vide, et de l'abrasivité extrême de la poussière lunaire qui détruit les systèmes de traitement.
- **L'approche technique :** Un système d'exploitation embarqué de robotique industrielle couplé à un jumeau numérique simulant la thermodynamique et la mécanique granulaire de la fonte du régolithe (par électrolyse ou micro-ondes) en condition de gravité zéro/lunaire. Ce système contrôle les essaims de robots de raffinage de manière autonome en compensant les erreurs de traitement.
- **Pourquoi une solution générique/SaaS classique échoue :** Il n'existe pas de données terrestres applicables. Les logiciels de contrôle industriel (SCADA) standards supposent une gravité terrestre, une atmosphère, et une intervention humaine en temps réel, ce qui est impossible à cause de la latence de communication Terre-Lune.
- **Risques majeurs & Dépendances :** Marché ultra-niche à très long terme, risque d'échec des missions d'alunissage nécessaires pour le déploiement matériel, budget de développement prohibitif, barrières réglementaires floues concernant l'exploitation minière spatiale (Traité de l'espace).
