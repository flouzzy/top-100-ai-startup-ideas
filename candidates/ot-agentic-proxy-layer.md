<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : Industrial Agent Proxy

* **Domaine principal :** IA & Agents autonomes
* **Modèle économique :** B2B
* **Cible :** Industries manufacturières, Usines chimiques, Gestionnaires d'infrastructures critiques (CISO, OT Managers).
* **Le problème urgent :** L'intégration d'agents IA (LLMs/VLM) pour l'optimisation des processus industriels (OT) expose les automates programmables (PLC/SCADA) à des actions non déterministes et potentiellement catastrophiques, empêchant toute adoption d'IA générative sur les lignes de production.
* **L'approche technique :** Une couche de proxy sécurisée (Middleware) agissant comme un 'garde-fou déterministe'. L'agent IA propose des actions complexes qui sont mathématiquement vérifiées contre des contraintes de sécurité physiques et logiques (Model Checking) avant traduction en commandes Modbus/OPC UA autorisées.
* **Pourquoi une solution générique/SaaS classique échoue :** Les agents IA hallucinent et n'ont pas de garantie de sécurité intrinsèque. Un simple wrapper API transmettrait directement des commandes dangereuses (ex: ouvrir une vanne à 100% au lieu de 10%). Il faut une compréhension formelle de la physique du processus (Digital Twin sémantique).
* **Risques majeurs & Dépendances :** Extrême prudence du secteur industriel (air-gap), intégration avec des protocoles legacy propriétaires, responsabilité légale majeure en cas de faille du proxy menant à un incident industriel.
