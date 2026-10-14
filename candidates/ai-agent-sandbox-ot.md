<!-- markdownlint-disable MD013 -->
# Candidat : AIAgentSandboxOT

* **Domaine principal :** Cybersécurité & Résilience
* **Modèle économique :** B2B
* **Cible :** RSSI (CISO) et directeurs d'infrastructures industrielles (énergie, manufacturier critique, transport)
* **Le problème urgent :** L'intégration de modèles d'IA et d'agents autonomes pour l'optimisation des réseaux OT (Operational Technology) introduit des risques d'actions imprévisibles ou d'hallucinations qui pourraient altérer des processus physiques critiques, causant des dommages matériels majeurs, des arrêts de production très coûteux ou des violations de normes de sécurité strictes (IEC 62443).
* **L'approche technique :** Création d'un environnement bac à sable d'orchestration (Sandbox) fonctionnant au niveau du réseau industriel et du middleware SCADA, interceptant et simulant virtuellement les commandes des agents IA avant leur exécution physique. Validation par des règles physiques déterministes.
* **Pourquoi une solution générique/SaaS classique échoue :** Les API classiques ou pare-feu informatiques ne comprennent pas la physique des automates programmables (PLC). Une solution nécessite une intégration bas niveau aux protocoles industriels (Modbus, OPC UA) et une simulation physique en temps réel pour évaluer les conséquences d'une commande d'IA.
* **Risques majeurs & Dépendances :** Adoption lente dans les environnements industriels conservateurs, nécessité d'interfaçage avec du matériel obsolète (legacy), responsabilité légale en cas de défaillance.
