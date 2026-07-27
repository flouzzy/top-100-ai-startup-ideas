<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Passerelle OT Post-Quantique (PQC OT Gateway)

- **Domaine principal :** Cybersécurité & Résilience
- **Modèle économique :** B2B
- **Cible :** OIV (Opérateurs d'Importance Vitale), gestionnaires de réseaux électriques, usines de traitement de l'eau, et infrastructures industrielles lourdes.
- **Le problème urgent :** Les systèmes de contrôle industriel (ICS/SCADA) utilisent des protocoles de communication legacy en clair ou faiblement chiffrés. L'arrivée imminente d'ordinateurs quantiques (Q-Day) menace de briser les chiffrements asymétriques actuels, rendant ces infrastructures critiques vulnérables à des attaques de type "Store Now, Decrypt Later". Remplacer matériellement tous les automates (PLC) est financièrement impossible et nécessiterait des arrêts de production inacceptables.
- **L'approche technique :** Une passerelle matérielle/logicielle (edge gateway) déployée en amont des équipements legacy. Elle agit comme un tunnel IPsec/TLS post-quantique, encapsulant le trafic industriel non sécurisé (Modbus, DNP3) dans des algorithmes de cryptographie résistants au quantique (ex: Kyber/Dilithium) pour les communications inter-sites et cloud, sans nécessiter de mise à jour des PLC sous-jacents.
- **Pourquoi une solution générique/SaaS classique échoue :** Ce problème nécessite une intégration profonde au niveau du réseau physique (L2/L3), une faible latence stricte pour ne pas perturber les processus industriels temps réel, et une compatibilité avec des protocoles OT très spécifiques. Un simple prompt LLM ou un SaaS cloud ne peut pas sécuriser physiquement un flux de données provenant d'un automate de 1990 dans une usine isolée sans modifier le hardware.
- **Risques majeurs & Dépendances :** Standards du NIST encore en finalisation, besoin d'homologation matérielle stricte pour environnements industriels (température, vibrations), latence additionnelle induite par les algorithmes PQC qui pourrait désynchroniser les automates.
