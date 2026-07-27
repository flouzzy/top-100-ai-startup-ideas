<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Quantum Safe SBOM

- **Domaine principal :** Cybersécurité & Résilience
- **Modèle économique :** B2B
- **Cible :** Editeurs de logiciels gouvernementaux, sous-traitants défense, institutions financières (DevSecOps, CISO).
- **Le problème urgent :** Il est impossible de garantir qu'une bibliothèque open-source tierce insérée dans une chaîne de CI/CD ne contient pas de portes dérobées ou que sa signature cryptographique n'a pas été compromise face aux futures menaces quantiques.
- **L'approche technique :** Une plateforme d'analyse d'AST (Abstract Syntax Tree) sémantique qui trace la provenance du code source jusqu'au binaire final, en signant de manière indélébile chaque étape de la compilation via un registre distribué utilisant la cryptographie Post-Quantique.
- **Pourquoi une solution générique/SaaS classique échoue :** Les scanners de vulnérabilités classiques (SCA) se contentent de comparer des versions de packages avec une base de données de CVE connue, sans comprendre la structure du code ou détecter des malwares "zero-day" insérés lors de la compilation.
- **Risques majeurs & Dépendances :** Adoption des standards PQC, intégration complexe dans l'écosystème fragmenté des outils de CI/CD (GitHub, GitLab, Jenkins), besoin de convaincre les développeurs open-source d'adopter le standard.
