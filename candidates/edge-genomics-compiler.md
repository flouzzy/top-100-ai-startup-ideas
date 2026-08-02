<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : Edge Genomics Compiler

- **Domaine principal :** Biotech & Bio-informatique
- **Modèle économique :** B2B
- **Cible :** Hôpitaux de campagne, bases de recherche isolées, biosurveillance de terrain (pandémie, agriculture).
- **Le problème urgent :** Le séquençage génomique portable (ex: Oxford Nanopore) génère d'énormes volumes de données brutes (signaux électriques complexes). L'analyse (basecalling et alignement) nécessite aujourd'hui soit un envoi vers un cluster cloud (impossible sans haut débit), soit des GPU locaux très consommateurs d'énergie.
- **L'approche technique :** Un compilateur et moteur d'inférence neuronal ultra-quantifié (pruning, 4-bit) conçu spécifiquement pour exécuter le "basecalling" de l'ADN/ARN directement sur des puces neuromorphiques ou des FPGA à très basse consommation (Edge AI).
- **Pourquoi une solution générique/SaaS classique échoue :** Les pipelines bio-informatiques classiques sont des empilements de scripts Python/C++ conçus pour des serveurs x86 massifs. Ils ne peuvent pas s'exécuter sur batterie en plein milieu de la jungle amazonienne ou dans un navire océanographique.
- **Risques majeurs & Dépendances :** La précision du basecalling doit rester clinique (99.9%+) malgré la quantification agressive du modèle d'IA. Forte dépendance à l'évolution des capteurs de séquençage physique.
