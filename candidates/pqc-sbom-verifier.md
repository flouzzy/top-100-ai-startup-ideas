<!-- markdownlint-disable MD013 -->
# Candidat : PQCBom (Post-Quantum Cryptography SBOM Verifier)

* **Domaine principal :** Cybersécurité & Résilience
* **Modèle économique :** B2B
* **Cible :** RSSI (CISO), équipes DevSecOps d'infrastructures critiques (Banques, Défense, Santé) et éditeurs de logiciels.
* **Le problème urgent :** Avec l'arrivée imminente des ordinateurs quantiques, les algorithmes de chiffrement actuels (RSA, ECC) deviendront obsolètes ("Q-Day"). La transition vers la cryptographie post-quantique (PQC) est obligatoire. Cependant, les entreprises ne savent pas exactement où se cachent les vulnérabilités cryptographiques dans leur chaîne d'approvisionnement logicielle tentaculaire (dépendances open source, bibliothèques tierces), rendant la remédiation impossible.
* **L'approche technique :** Un moteur d'analyse statique (SAST) et dynamique profond qui scanne les binaires et le code source pour générer une "Crypto-SBOM" (Software Bill of Materials cryptographique) précise. Il cartographie non seulement l'usage des librairies crypto, mais identifie l'implémentation spécifique des algorithmes obsolètes dans l'arbre des dépendances transitives, avec une automatisation de la substitution vers les standards NIST PQC.
* **Pourquoi une solution générique/SaaS classique échoue :** Les scanners SBOM traditionnels (Trivy, Snyk) détectent les CVE connues ou les noms de packages. Ils ne comprennent pas l'implémentation cryptographique bas niveau (ex: si une lib custom implémente secrètement du RSA-1024 en dur). Cela requiert de l'analyse sémantique de code, de la décompilation de binaires et une compréhension de la taxonomie cryptographique.
* **Risques majeurs & Dépendances :** Adoption lente si le "Q-Day" est perçu comme lointain. Complexité technique de scanner divers langages (C/C++, Rust, Java, Go) et binaires compilés sans accès au code source des fournisseurs.
