<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : PQC Drone Swarm Comm Mesh

- **Domaine principal :** Cybersécurité / Robotique
- **Modèle économique :** B2B / B2G
- **Cible :** Ministères de la Défense, entreprises de surveillance d'infrastructures critiques, flottes logistiques autonomes.
- **Le problème urgent :** Les communications en essaim (drone à drone) reposent actuellement sur des standards de cryptographie classique (ECC, RSA). Avec l'avènement des attaques par calcul quantique (SNDL - Store Now, Decrypt Later), l'interception des communications de contrôle des essaims devient une menace critique, permettant la prise de contrôle ou le spoofing de missions.
- **L'approche technique :** Implémentation d'un protocole de communication mesh bas-niveau intégrant de la cryptographie post-quantique (PQC) allégée (ex: CRYSTALS-Kyber optimisé) adaptée aux contraintes SWaP (Size, Weight, and Power) des drones. Il assure l'authentification et l'échange de clés ultra-rapide entre agents volants à faible ressource de calcul.
- **Pourquoi une solution générique/SaaS classique échoue :** Les bibliothèques PQC standards sont trop lourdes en empreinte mémoire et en latence de calcul pour des microcontrôleurs de vol. Les solutions logicielles classiques imposent des retards incompatibles avec la prise de décision en millisecondes requise par le vol en essaim.
- **Risques majeurs & Dépendances :** Standards du NIST encore en cours d'affinage, pouvant nécessiter une agilité crypto complexe en firmware. Risque de surconsommation énergétique réduisant l'autonomie en vol des drones de petites dimensions.
