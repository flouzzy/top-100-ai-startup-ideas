<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Lithos Twin

- **Domaine principal :** World Models / ClimateTech / Deep Tech
- **Modèle économique :** B2B
- **Cible :** Entreprises de géothermie, miniers de transition énergétique (Lithium, Cuivre), opérateurs de stockage géologique de carbone (CCS).
- **Le problème urgent :** L'exploration du sous-sol profond est aveugle, lente et coûteuse (forages exploratoires à plusieurs millions). Les modèles géologiques 3D actuels sont statiques, déconnectés de la réalité en temps réel, et la sismique 3D requiert des mois de traitement de signal lourd. L'incertitude bloque le financement de projets géothermiques et de séquestration carbone.
- **L'approche technique :** Un "World Model" du sous-sol intégrant de multiples modalités (sismique, gravimétrique, électromagnétique, données de forages passés) pour générer un jumeau numérique probabiliste et continu de la croûte terrestre. Utilisation de modèles de diffusion conditionnels pour générer des millions de scénarios géologiques plausibles et réduire l'incertitude avant tout forage.
- **Pourquoi une solution générique/SaaS classique échoue :** Il s'agit d'un problème d'inversion géophysique massivement sous-contraint (trouver la structure 3D à partir de signaux de surface limités). Un outil data standard ne gère pas les tenseurs 3D voxélisés à l'échelle kilométrique, ni la physique de propagation des ondes (équation des ondes).
- **Risques majeurs & Dépendances :** La rareté et la fragmentation des données géologiques (souvent jalousement gardées par les majors pétrolières). La validation sur le terrain est lente (un forage prend des mois).
