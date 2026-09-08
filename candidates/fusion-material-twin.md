<!-- markdownlint-disable MD013 -->

# Candidat : Fusion First-Wall Material Twin

- **Domaine principal :** ClimateTech & Énergie / World Models
- **Modèle économique :** B2B
- **Cible :** Entreprises de fusion nucléaire (tokamaks, confinement inertiel, stellarators), instituts de recherche en matériaux sous conditions extrêmes.
- **Le problème urgent :** La commercialisation de l'énergie de fusion est bloquée par la dégradation des matériaux de la "première paroi" du réacteur. Face aux flux intenses de neutrons rapides et aux charges thermiques extrêmes du plasma, les alliages actuels (tungstène, aciers spécifiques) se fragilisent, gonflent ou fondent prématurément. Tester physiquement de nouveaux matériaux prend des mois et coûte des millions par échantillon.
- **L'approche technique :** Un jumeau numérique atomique prédisant la dégradation micro-structurelle (transmutation, déplacements par atome, cloquage par hélium) des matériaux sous irradiation neutronique de fusion. Le modèle utilise des réseaux de tenseurs (Tensor Networks) et du deep learning géométrique pour simuler l'évolution des défauts cristallins sur des échelles de temps macroscopiques, court-circuitant les simulations de dynamique moléculaire (MD) classiquement incalculables sur ces durées.
- **Pourquoi une solution générique/SaaS classique échoue :** Les outils de conception assistée (CAD) ou les solveurs d'éléments finis (FEA) ne descendent pas à l'échelle quantique/atomique. L'IA générative standard ne respecte pas les lois de conservation de l'énergie et ne peut simuler des cascades de collisions neutroniques.
- **Risques majeurs & Dépendances :** Besoin de données empiriques issues d'installations d'irradiation neutronique spécialisées (comme IFMIF-DONES, encore en construction) pour calibrer et valider les prédictions du modèle.
