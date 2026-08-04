<!-- markdownlint-disable MD013 -->

# Candidat : Airgapped Update Bridge

- **Domaine principal :** Cybersécurité & Résilience (OT/ICS)
- **Modèle économique :** B2B
- **Cible :** Opérateurs d'infrastructures d'importance vitale (OIV) : centrales nucléaires, réseaux électriques, usines de traitement de l'eau, lignes de production manufacturière critique.
- **Le problème urgent :** Les systèmes industriels (OT - Operational Technology) sont maintenus isolés d'Internet (air-gapped) pour des raisons de sécurité évidentes. Cependant, l'impossibilité de déployer des correctifs de sécurité (patchs virtuels) de manière continue les laisse vulnérables à des attaques de type Stuxnet (via clé USB). Les processus de mise à jour manuels actuels prennent des mois.
- **L'approche technique :** Une passerelle matérielle unidirectionnelle (Data Diode / FPGA) couplée à un bac à sable (sandbox) de jumeau numérique OT. Les mises à jour logicielles sont reçues via le réseau IT, testées de manière automatisée sur la réplique exacte du système industriel dans un environnement émulé (pour s'assurer qu'elles ne cassent pas le processus physique), puis transmises de manière unidirectionnelle physique via laser/optique vers le réseau OT pour un déploiement zéro-downtime sécurisé.
- **Pourquoi une solution générique/SaaS classique échoue :** Aucun logiciel Cloud (AWS, Azure) ne peut traverser un vrai air-gap physique. Une diode de données classique ne fait que passer l'information, elle ne certifie pas que le patch de l'automate (PLC) ne va pas provoquer l'arrêt d'une turbine. Il faut la combinaison d'une isolation matérielle stricte (hardware) et d'un jumeau numérique spécifique aux protocoles industriels (Modbus, DNP3, PROFINET).
- **Risques majeurs & Dépendances :** Certification matérielle draconienne par les agences nationales de sécurité (ex: ANSSI, CISA) ; difficulté de construire des jumeaux numériques 100% fidèles des anciens automates (Legacy PLCs) ; résistance culturelle des opérateurs OT face à l'automatisation des mises à jour.
