<!-- markdownlint-disable MD013 -->

# Candidat : Protein Degrader Sim

- **Domaine principal :** Biotech & Bio-informatique
- **Modèle économique :** B2B
- **Cible :** Laboratoires pharmaceutiques (Big Pharma), biotechs spécialisées en oncologie et maladies neurodégénératives.
- **Le problème urgent :** La plupart des maladies graves sont causées par des protéines "undruggable" (impossibles à cibler avec des inhibiteurs classiques). Les PROTACs (Proteolysis Targeting Chimeras) permettent de détruire ces protéines, mais leur conception (trouver la bonne molécule liant la cible, l'enzyme E3 ligase et le linker) s'apparente à chercher une aiguille dans un espace combinatoire tridimensionnel immense, entraînant un taux d'échec clinique massif.
- **L'approche technique :** Un modèle génératif de type "World Model" moléculaire (intégrant la dynamique moléculaire, l'IA générative 3D géométrique de type AlphaFold3, et la mécanique quantique pour les interactions de liaison) spécifiquement entraîné pour simuler et générer des chimères de dégradation protéique (PROTACs, molecular glues) stables en solution aqueuse.
- **Pourquoi une solution générique/SaaS classique échoue :** Les outils de docking traditionnels (AutoDock) sont statiques et ne gèrent pas bien les molécules hautement flexibles (comme les linkers PROTAC) ni la formation de complexes ternaires (Cible-PROTAC-Ligase). Cela requiert une compréhension de la dynamique conformationnelle (physique) que les LLM purs ignorent.
- **Risques majeurs & Dépendances :** Besoin critique de données d'affinité de complexes ternaires (souvent propriétaires aux pharmas) pour l'entraînement ; coût computationnel énorme (simulation de dynamique moléculaire à l'échelle atomique) ; validation wet-lab in-vitro obligatoire pour prouver la prédiction.
