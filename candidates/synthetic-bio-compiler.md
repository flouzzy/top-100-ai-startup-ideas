<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : DNA to Protein Neural Compiler

- **Domaine principal :** Biotech & Bio-informatique
- **Modèle économique :** B2B
- **Cible :** Pharmas (Pfizer, Moderna), biotechs spécialisées dans l'oncologie ou l'agriculture (fermentation de précision), laboratoires de biologie synthétique.
- **Le problème urgent :** Designer de nouvelles protéines ou enzymes de novo relève de l'alchimie. Le processus de "Fold to Function" prend des années de wet-lab et des millions de dollars pour un taux d'échec de 99%, ralentissant la création de médicaments ciblés ou de matériaux biodégradables.
- **L'approche technique :** Un compilateur IA qui traduit des contraintes fonctionnelles (ex: "une enzyme stable à 80°C qui dégrade le PET") en séquences d'acides aminés, avec un modèle de diffusion 3D prédisant l'affinité de liaison et les toxicités potentielles avant la moindre synthèse. Couplé à un orchestrateur de wet-lab automatisé pour vérifier la viabilité en boucle fermée.
- **Pourquoi une solution générique/SaaS classique échoue :** L'espace conformationnel des protéines est plus vaste que le nombre d'atomes dans l'univers. Les logiciels de chimie computationnelle classiques exigent des réglages manuels infinis. AlphaFold prédit la structure, mais ne génère pas de séquences _à partir d'une fonction désirée_ avec des contraintes industrielles.
- **Risques majeurs & Dépendances :** Dépendance au coût des synthétiseurs d'ADN physiques pour les tests (wet-lab in the loop). L'acquisition de données propriétaires sur les échecs ("negative data" très rares dans la littérature scientifique) pour entraîner le modèle. Biosecurité (empêcher la création de pathogènes).
