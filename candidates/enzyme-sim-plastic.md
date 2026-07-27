<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : PolyPhage AI

- **Domaine principal :** Biotech / Bio-informatique / ClimateTech
- **Modèle économique :** B2B (Licensing IP / JVs)
- **Cible :** Géants de la pétrochimie en transition, entreprises de traitement des déchets (Veolia, Suez) et fabricants de plastiques.
- **Le problème urgent :** Le recyclage mécanique du plastique (PET, PE, PP) dégrade la matière et est inefficace pour les plastiques mélangés. Le recyclage enzymatique (dépolymérisation) est le Saint Graal, mais la découverte d'enzymes robustes, rapides et capables d'opérer à température ambiante sur des déchets complexes prend des années en laboratoire par essais-erreurs (wet-lab).
- **L'approche technique :** Un modèle d'IA génératif structurel (type AlphaFold 3 / ESM-3 étendu) couplé à un pipeline de dynamique moléculaire (MD) accéléré par ML, spécifiquement entraîné (fine-tuned) sur les interactions enzyme-polymères plastiques. L'objectif est la génération _in silico_ de séquences d'acides aminés inédites formant des enzymes "mangeuses de plastique" hyper-optimisées pour des conditions industrielles précises.
- **Pourquoi une solution générique/SaaS classique échoue :** Les LLMs textuels ne "comprennent" pas le repliement des protéines ni l'énergie de liaison (binding affinity). La physique quantique (DFT) et la dynamique moléculaire des interactions biocatalytiques nécessitent une infrastructure de compute massive et des architectures de GNN (Graph Neural Networks) spécialisées, pas une interface de chat.
- **Risques majeurs & Dépendances :** Le "Reality Gap" : une enzyme brillante sur le simulateur peut être instable, insoluble ou impossible à exprimer dans des bactéries productrices (E. coli, levures) en réalité (wet-lab bottleneck). Nécessite un laboratoire de validation robotisé.
