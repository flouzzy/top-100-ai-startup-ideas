<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : ForgeGuard ICS

- **Domaine principal :** Cybersécurité / Robotique & Systèmes embarqués
- **Modèle économique :** B2B
- **Cible :** Usines de fabrication avancée (gigafactories), raffineries, opérateurs d'énergie.
- **Le problème urgent :** L'environnement OT (Operational Technology - automates programmables PLC, SCADA) est intrinsèquement non sécurisé (protocols Modbus/PROFINET sans authentification ni chiffrement). Les firewalls OT actuels font de la détection d'anomalie réseau, ce qui génère trop de faux positifs et n'empêche pas un attaquant ayant compromis le réseau de modifier la logique de l'automate (ex: attaque Stuxnet-like ou ransomware bloquant la production).
- **L'approche technique :** Un moteur d'exécution (Runtime) Zero-Trust déployé directement en bordure (Edge) ou sur un proxy matériel en ligne (bump-in-the-wire) devant chaque automate critique. Il effectue une inspection sémantique profonde (Deep Packet Inspection) et une vérification d'état cryptographique (attestation d'intégrité de la logique de contrôle) en temps réel avec une latence sub-milliseconde.
- **Pourquoi une solution générique/SaaS classique échoue :** L'IT (cloud, SaaS) tolère des latences de plusieurs centaines de millisecondes. L'OT exige un déterminisme absolu (< 5ms) : si un paquet de sécurité retarde la commande de freinage d'un bras robotique, des vies humaines sont en jeu. Les solutions IT SaaS sont incompatibles avec les contraintes réseau (souvent air-gapped) et temporelles de l'usine.
- **Risques majeurs & Dépendances :** Refus absolu des industriels d'installer quoi que ce soit "in-line" de peur que la sécurité ne casse la production (le faux positif tue l'usine). Nécessité de certification drastique de type SIL (Safety Integrity Level).
