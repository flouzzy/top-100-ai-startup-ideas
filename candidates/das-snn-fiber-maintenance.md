<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : DAS SNN Fiber Maintenance

- **Domaine principal :** Deep Tech Infra / Sécurité
- **Modèle économique :** B2B
- **Cible :** Opérateurs télécoms (Tier 1), gestionnaires de pipelines (pétrole/gaz), opérateurs de réseaux ferroviaires et sociétés de surveillance de frontières.
- **Le problème urgent :** Le Distributed Acoustic Sensing (DAS) transforme n'importe quel câble de fibre optique existant en des milliers de capteurs de vibrations en mesurant la rétrodiffusion de Rayleigh. Cependant, générer des téraoctets de données acoustiques brutes par jour sur des milliers de kilomètres crée un cauchemar de traitement. Les fausses alertes constantes rendent le système inutilisable par des humains, empêchant la détection d'excavatrices menaçant les câbles, de fuites de pipelines ou d'intrusions sur les voies ferrées.
- **L'approche technique :** Intégration de puces neuromorphiques (Spiking Neural Networks - SNN) directement à l'edge, connectées aux interrogateurs optiques. Les SNN excellent dans le traitement natif de séries temporelles asynchrones et bruitées (comme le signal DAS), consommant une fraction de l'énergie des GPU standards tout en filtrant le bruit environnemental et en classifiant les signatures sismiques spécifiques (pas humain vs machinerie lourde) en temps réel avec des micro-latences.
- **Pourquoi une solution générique/SaaS classique échoue :** Uploader le flux continu non compressé du DAS vers le cloud pour une inférence par des modèles Transformers/CNN est impossible à l'échelle en termes de bande passante et de coût d'ingestion (S3). L'intelligence doit être à l'extrémité (edge) et traiter des impulsions acoustiques brutes, nécessitant un hardware spécifique (neuromorphic computing).
- **Risques majeurs & Dépendances :** Manque de maturité de la chaîne d'outils de compilation pour SNN (comparé à PyTorch/CUDA). Nécessité d'intégrations matérielles sur mesure avec les fournisseurs d'interrogateurs optiques (les lasers).
