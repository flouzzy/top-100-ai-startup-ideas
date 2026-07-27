<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : GridCarbon Ledger

- **Domaine principal :** ClimateTech & Énergie
- **Modèle économique :** B2B / M2M
- **Cible :** Gestionnaires de réseau de transport (GRT), producteurs d'énergie renouvelable, data centers (hyperscalers).
- **Le problème urgent :** La traçabilité de l'intensité carbone de l'électricité est actuellement gérée par des certificats annuels opaques (EAC/GO), empêchant les data centers et les industriels d'optimiser leur consommation en temps réel selon l'énergie verte disponible localement.
- **L'approche technique :** Infrastructure cryptographique distribuée (sans consensus lourd type PoW) qui ingère les données de télémétrie des onduleurs et des compteurs intelligents à la milliseconde, émettant des tokens de "Carbone Évité" géolocalisés et horodatés, permettant un arbitrage énergétique algorithmique par les machines (M2M).
- **Pourquoi une solution générique/SaaS classique échoue :** Les SaaS de comptabilité carbone actuels reposent sur des moyennes annuelles et des factures PDF. Ce problème nécessite une infrastructure d'ingestion de flux de données IoT à haute fréquence, une certification infalsifiable au niveau du réseau électrique et une intégration bas niveau avec les systèmes SCADA.
- **Risques majeurs & Dépendances :** Dépendance au bon vouloir et aux APIs des gestionnaires de réseau existants; l'adoption nécessite de nouveaux standards réglementaires (ex: 24/7 CFE par Google/Microsoft) pour obliger le marché à adopter cette granularité.
