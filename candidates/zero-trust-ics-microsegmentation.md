<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : Quantum-Safe ICS Micro-segmentation

* **Domaine principal :** Cybersécurité & Résilience
* **Modèle économique :** B2B
* **Cible :** Infrastructures critiques (Réseaux électriques, Distribution d'eau, Nucléaire, Pétrole & Gaz).
* **Le problème urgent :** Les réseaux industriels (ICS/SCADA) ont été conçus pour être isolés. Aujourd'hui connectés, ils utilisent des protocoles en clair sans authentification forte. Une fois le réseau IT compromis (ex: ransomware), le pivot latéral vers l'OT est trivial, menaçant la sécurité nationale.
* **L'approche technique :** Un système de micro-segmentation dynamique au niveau matériel (Edge/Switch industriel) utilisant la cryptographie post-quantique (PQC) pour établir une architecture Zero-Trust stricte sans impacter la latence déterministe nécessaire aux systèmes de contrôle-commande (temps réel critique).
* **Pourquoi une solution générique/SaaS classique échoue :** Les solutions IT classiques (SDN, pare-feu traditionnels) introduisent du jitter et de la latence qui font planter les boucles de contrôle industriel (ex: protection des relais électriques). Les protocoles IT (IPsec, TLS lourds) ne peuvent pas être déployés sur de vieux automates.
* **Risques majeurs & Dépendances :** Downtime inacceptable lors du déploiement (les usines tournent H24), certification par des organismes de sécurité critiques (ex: ANSSI, NERC CIP), overhead computationnel de la PQC sur du matériel embarqué faible.
