<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Swarm Agent Collusion Detector

- **Domaine principal :** IA & Agents autonomes (Sécurité)
- **Modèle économique :** B2B
- **Cible :** Plateformes d'échange financier (HFT), marketplaces B2B, réseaux d'énergie distribués, opérateurs de supply chain.
- **Le problème urgent :** Avec l'essor des agents IA autonomes négociant et agissant pour le compte d'entreprises, le risque d'ententes illicites (collusion), de manipulation de marché ou de formation de cartels par des IAs (sans instruction humaine directe) devient un risque systémique indétectable par la compliance classique.
- **L'approche technique :** Moteur de surveillance de réseau et d'analyse comportementale multi-agents. Il utilise la théorie des jeux inverse et l'analyse de graphes dynamiques pour identifier les motifs de communication et de transactions subtils révélateurs de stratégies coopératives cachées entre agents supposément concurrents.
- **Pourquoi une solution générique/SaaS classique échoue :** Les algorithmes de détection de fraude actuels cherchent des règles humaines enfreintes. La collusion algorithmique émerge de stratégies d'apprentissage par renforcement (RL) et ne laisse pas de "smoking gun" comme des emails d'entente. Il faut modéliser l'espace de décision des IAs.
- **Risques majeurs & Dépendances :** Manque de données d'entraînement réelles (le phénomène est émergent), complexité mathématique pour prouver l'intentionnalité d'une IA (explicabilité), et adoption lente car les entreprises ne voient pas encore le risque.
