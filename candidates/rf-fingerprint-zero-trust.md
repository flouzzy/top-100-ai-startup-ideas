<!-- markdownlint-disable MD013 -->
# Candidat : RF Fingerprint Zero Trust

- **Domaine principal :** Cybersécurité & Résilience (OT/ICS)
- **Modèle économique :** B2B
- **Cible :** Opérateurs d'Infrastructures d'Importance Vitale (OIV), usines manufacturières, gestionnaires de centrales électriques et réseaux de distribution d'eau.
- **Le problème urgent :** Les systèmes industriels (OT) critiques utilisent souvent des capteurs sans fil ou des liaisons radio obsolètes vulnérables aux attaques de type "spoofing" ou "replay". Les attaquants peuvent injecter de fausses données de capteurs (ex: température d'une turbine) sans alerter les systèmes de sécurité IT/OT classiques.
- **L'approche technique :** Implémentation d'une couche Zero-Trust bas niveau analysant les micro-imperfections matérielles des transmissions radio (Radio Frequency Fingerprinting) via des modèles de machine learning embarqués sur des FPGA en périphérie (edge), authentifiant ainsi le composant physique émetteur de manière incontestable.
- **Pourquoi une solution générique/SaaS classique échoue :** Les solutions de sécurité réseau classiques se basent sur des adresses IP, des MAC adresses ou des certificats cryptographiques qui peuvent être usurpés ou volés. L'analyse des signaux analogiques au niveau physique (Layer 1) nécessite une expertise en traitement du signal et du hardware spécifique (SDR, FPGA) impossible à fournir via un simple logiciel.
- **Risques majeurs & Dépendances :** Variabilité des empreintes RF due aux changements de température ou au vieillissement des composants, intégration matérielle intrusive requise sur les infrastructures existantes (brownfield), fausses alertes pouvant paralyser des processus industriels continus.
