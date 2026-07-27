<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : PlasmaControl AI

- **Domaine principal :** ClimateTech & Énergie (Fusion nucléaire)
- **Modèle économique :** B2B
- **Cible :** Startups de fusion nucléaire (Tokamak, Stellarator, confinement inertiel), instituts de recherche gouvernementaux (ITER).
- **Le problème urgent :** Maintenir un plasma à des millions de degrés de manière stable est le verrou de la fusion nucléaire. Les instabilités magnétohydrodynamiques (MHD) se développent en quelques microsecondes et détruisent le confinement, interrompant la réaction et endommageant les parois du réacteur.
- **L'approche technique :** Un contrôleur d'IA basé sur l'apprentissage par renforcement profond (Deep RL) à ultra-basse latence, entraîné sur des simulateurs physiques massivement parallèles. Il analyse les données des capteurs de diagnostic en temps réel et ajuste les bobines magnétiques des milliers de fois par seconde pour prévenir la disruption du plasma.
- **Pourquoi une solution générique/SaaS classique échoue :** Le temps de réaction requis est de l'ordre de la microseconde. L'inférence du modèle d'IA doit s'exécuter directement sur des FPGA couplés aux capteurs, aucune latence réseau n'est tolérée. Il faut modéliser la physique des plasmas qui est extrêmement chaotique.
- **Risques majeurs & Dépendances :** Pas de marché commercial massif à court terme (l'industrie de la fusion est en R&D); validation impossible sans accès à des réacteurs expérimentaux valant des milliards de dollars; risque scientifique que le confinement long terme soit physiquement impossible.
