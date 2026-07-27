<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : LEO Mesh Router

- **Domaine principal :** Deep Tech & Infra (Communications spatiales)
- **Modèle économique :** B2B / M2M
- **Cible :** Opérateurs de méga-constellations (SpaceX, Kuiper, OneWeb), agences spatiales, fournisseurs cloud (Azure Space, AWS Ground Station).
- **Le problème urgent :** Les satellites en orbite basse (LEO) actuels opèrent majoritairement en architecture "bent-pipe" (relai stupide) ou dépendent de stations au sol pour router les données. Avec l'explosion du nombre de satellites, l'absence de véritable routage dynamique inter-satellites (Inter-Satellite Links - ISL) au niveau spatial crée des goulots d'étranglement massifs, augmente la latence globale et limite la résilience du réseau en cas de perte d'une station sol.
- **L'approche technique :** Un système de routage IP/MPLS embarqué et distribué (Software-Defined Space Networking), conçu pour fonctionner sur des processeurs spatiaux durcis (radiation-hardened). Ce routeur logiciel orchestre dynamiquement les liens laser (Optical Intersatellite Links) en temps réel, calculant les chemins optimaux dans une topologie de réseau qui change constamment et à très grande vitesse.
- **Pourquoi une solution générique/SaaS classique échoue :** Les protocoles de routage terrestres (BGP, OSPF) sont conçus pour des topologies fixes. Dans l'espace, la topologie entière change en quelques minutes. Cela nécessite de redévelopper des protocoles réseau ad-hoc tolérants aux délais et aux perturbations (DTN - Delay-Tolerant Networking) capables de tourner avec des ressources calculatoires limitées dans l'espace, hors de portée d'un simple overlay SaaS.
- **Risques majeurs & Dépendances :** Adoption complexe (les constructeurs de satellites développent souvent leurs solutions réseau propriétaires en silo), barrière à l'entrée très haute nécessitant des qualifications spatiales strictes (TRL), et dépendance au rythme de déploiement des lasers de communication.
