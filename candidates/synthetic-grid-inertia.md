<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Synthetic Grid Inertia

- **Domaine principal :** ClimateTech & Énergie
- **Modèle économique :** B2B / M2M
- **Cible :** Opérateurs de réseaux de transport électrique (TSOs), fournisseurs d'énergie renouvelable, gestionnaires de microgrids.
- **Le problème urgent :** La transition vers les énergies renouvelables (solaire, éolien) élimine les générateurs rotatifs lourds (charbon, gaz) qui fournissaient l'inertie physique naturelle au réseau. Sans cette inertie, de légères fluctuations de fréquence peuvent provoquer des blackouts en chaîne dévastateurs en quelques millisecondes, rendant l'intégration massive des renouvelables instable et dangereuse.
- **L'approche technique :** Un système d'onduleurs intelligents (grid-forming inverters) couplé à une couche logicielle temps réel très basse latence. Ce système mesure les dérivées de fréquence et injecte ou absorbe instantanément de la puissance (via des batteries ou supercondensateurs) pour émuler synthétiquement la masse inertielle, stabilisant ainsi le réseau de manière décentralisée.
- **Pourquoi une solution générique/SaaS classique échoue :** Cela nécessite un couplage matériel/logiciel (hardware-in-the-loop) fonctionnant à la microseconde, obéissant aux équations différentielles de la dynamique des réseaux électriques (swing equations). Un simple tableau de bord prédictif ou un algorithme asynchrone est beaucoup trop lent et ne peut pas agir physiquement sur le courant alternatif.
- **Risques majeurs & Dépendances :** Certification matérielle stricte par les opérateurs de réseaux nationaux, coût de déploiement de l'infrastructure de puissance (batteries/onduleurs), réglementation complexe et conservatrice du secteur de l'énergie.
