<!-- markdownlint-disable MD013 MD033 -->
# Candidat : Zero Trust Network Access pour Agents IA (ZTNA-AI)

* **Modèle économique :** B2B
* **Cible :** Entreprises tech, RSSI (CISO), équipes DevOps et SecOps déployant des agents autonomes.
* **Le problème urgent :** Les agents autonomes nécessitent des accès API et bases de données pour agir. En cas d'hallucination ou de "prompt injection", un agent doté de droits trop larges peut exfiltrer des données sensibles, corrompre l'infrastructure ou causer d'immenses factures cloud. C'est un risque de sécurité majeur qui freine l'adoption de l'IA agentique en entreprise.
* **L'approche technique :** Mise en place d'un reverse-proxy spécialisé (Gateway de permissions) qui intercepte chaque appel API/SQL d'un agent. Il valide l'intention de la requête via des politiques de sécurité "Zero Trust" strictes, applique des quotas (financiers/taux), et nécessite un jeton de permission dynamique pour chaque action, bloquant les requêtes anormales.
* **Pourquoi ChatGPT/Gemini échoue seul :** Les LLMs généraux n'ont pas de capacité déterministe à restreindre leurs propres permissions réseau. En cas de manipulation (jailbreak), ils contournent leurs propres règles. La sécurité exige une couche d'infrastructure externe, séparée du modèle génératif, pour imposer un contrôle d'accès réseau strict et auditable.
