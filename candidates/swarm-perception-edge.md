<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : SwarmEdge Perception

- **Domaine principal :** Robotique & Systèmes embarqués
- **Modèle économique :** B2B / M2M
- **Cible :** Défense, logistique par drone, agriculture de précision.
- **Le problème urgent :** Les flottes de drones ou de robots mobiles (swarms) s'effondrent lorsque le signal GPS est brouillé (GPS spoofing/jamming) ou dans des environnements denses (forêts, entrepôts), car ils dépendent de serveurs centraux pour la coordination et la cartographie.
- **L'approche technique :** Un moteur SLAM (Simultaneous Localization and Mapping) collaboratif et purement Edge, fonctionnant sur des puces neuromorphiques ou des NPU basse consommation, permettant à la flotte de partager des tenseurs de perception compressés via un mesh radio peer-to-peer (sans Cloud) pour maintenir une carte 3D unifiée.
- **Pourquoi une solution générique/SaaS classique échoue :** Impossible d'utiliser une API Cloud : la latence doit être inférieure à 10ms, et la connectivité est par définition non fiable ou inexistante (Denied Environments). La solution doit tenir dans quelques mégaoctets de RAM et consommer moins de 5 Watts.
- **Risques majeurs & Dépendances :** Forte barrière de l'intégration hardware-software; besoin de développer des protocoles radio résilients; marché dominé par des cycles d'approvisionnement gouvernementaux lents.
