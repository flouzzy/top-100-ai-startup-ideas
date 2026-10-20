<!-- markdownlint-disable MD013 -->
# Candidat : ScadaShield (Legacy SCADA Modernizer & Protector)

* **Domaine principal :** Cybersécurité & Résilience / Deep Tech Infra
* **Modèle économique :** B2B
* **Cible :** Opérateurs d'Infrastructures d'Importance Vitale (OIV) : traitement de l'eau, centrales électriques, gazoducs, usines pétrochimiques.
* **Le problème urgent :** Les systèmes industriels critiques (OT/SCADA) fonctionnent avec des équipements (automates - PLC) vieux de 20 à 30 ans. Ils utilisent des protocoles de communication en clair, sans authentification cryptographique (Modbus, DNP3). Il est impossible de les mettre à jour ou de les éteindre. Une compromission (Ransomware) de ces réseaux peut entraîner des catastrophes écologiques ou paralyser un pays entier.
* **L'approche technique :** Une surcouche (Overlay Network) Zero-Trust matérielle et logicielle. Des micro-sondes passives non intrusives (bump-in-the-wire) placées physiquement devant les vieux automates, qui inspectent le trafic OT via des modèles de détection d'anomalies (Physics-aware AI). Le système bloque les commandes qui violeraient les lois de la physique du processus industriel (ex: ouvrir une vanne qui causerait une surpression).
* **Pourquoi une solution générique/SaaS classique échoue :** L'IT Security classique (CrowdStrike, Palo Alto) ne comprend pas les protocoles OT propriétaires ni les lois physiques du processus industriel. Un faux positif (bloquer une commande légitime) est aussi dangereux qu'une attaque. La solution doit être "Fail-Safe" et isolée d'Internet (Air-gapped).
* **Risques majeurs & Dépendances :** Cycle de vente cauchemardesque (aversion absolue au risque dans ces milieux, certifications draconiennes). Nécessité d'une présence matérielle physique robuste (hardware appliance) dans des environnements industriels hostiles (chaleur, poussière, vibrations).
