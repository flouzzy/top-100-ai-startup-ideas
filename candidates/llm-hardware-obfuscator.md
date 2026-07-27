<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Hardware Obfuscator AI

- **Domaine principal :** Deep Tech & IA
- **Modèle économique :** B2B
- **Cible :** Concepteurs de puces IA (Fabless), fonderies de semi-conducteurs, IP cores providers (VP Hardware Engineering).
- **Le problème urgent :** Le vol de propriété intellectuelle matérielle coûte cher. Les fonderies offshore peuvent cloner des plans de puces (GDSII), insérer des chevaux de Troie matériels ou surproduire pour le marché gris.
- **L'approche technique :** Un moteur d'obfuscation de circuits logiques basé sur l'apprentissage par renforcement (RL). Il insère des "portes factices" et modifie la topologie du netlist pour que la puce ne fonctionne qu'après l'activation d'une clé cryptographique post-fabrication.
- **Pourquoi une solution générique/SaaS classique échoue :** La conception de circuits imprimés nécessite de respecter des contraintes physiques (PPA : Power, Performance, Area). L'IA doit opérer sur des graphes représentant des milliards de transistors sans dégrader les performances de la puce finale, ce qu'aucun SaaS logiciel classique ne fait.
- **Risques majeurs & Dépendances :** Validation par les fonderies géantes (TSMC, Samsung), réticence des ingénieurs hardware à modifier leurs workflows, augmentation possible de la surface de silicium.
