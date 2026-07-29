<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : EMP Resilient OT Fabric

- **Domaine principal :** Cybersécurité & Résilience
- **Modèle économique :** B2B
- **Cible :** Opérateurs d'infrastructures critiques d'importance vitale (OIV), réseaux électriques, systèmes de contrôle du trafic aérien, armée.
- **Le problème urgent :** Une impulsion électromagnétique (EMP), qu'elle soit d'origine solaire (tempête géomagnétique sévère type Carrington) ou artificielle (High-Altitude EMP), induit des courants géomagnétiquement induits (GIC) qui détruisent les microcontrôleurs (PLCs/RTUs) des réseaux OT, paralysant l'ensemble de la société en quelques secondes. Il n'existe pas de solution de résilience logicielle face à une destruction matérielle de masse.
- **L'approche technique :** Une architecture réseau distribuée et asynchrone (mesh) combinant des microcontrôleurs durcis et isolés galvaniquement de nouvelle génération. Le logiciel orchestre de manière résiliente la reconfiguration dynamique de la topologie réseau (fail-over d'état critique) en tolérant la perte instantanée et simultanée de 90% des nœuds, assurant la reprise des fonctions industrielles vitales (graceful degradation) sans boot lent.
- **Pourquoi une solution générique/SaaS classique échoue :** Ce n'est pas un problème de cybersécurité logicielle (TCP/IP), mais de résilience matérielle/firmware de bas niveau face à une destruction physique. Les systèmes de tolérance aux pannes classiques cloud (Kubernetes) ne fonctionnent pas sur du bare-metal OT dont les cartes mères brûlent.
- **Risques majeurs & Dépendances :** Il faut concevoir et distribuer de l'équipement matériel personnalisé (hardware appliance), un marché très conservateur qui déteste remplacer son infrastructure legacy (vieille de 20 ans), tests d'assurance qualité en conditions extrêmes très coûteux.
