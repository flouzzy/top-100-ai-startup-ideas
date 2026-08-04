<!-- markdownlint-disable MD013 -->

# Candidat : Firmware Quantum Obfuscator

- **Domaine principal :** Cybersécurité & Résilience (PQC)
- **Modèle économique :** B2B
- **Cible :** Fabricants de matériel militaire, aérospatial, médical (IoT critique) et infrastructures essentielles (ICS/SCADA).
- **Le problème urgent :** L'approche de l'ère de l'informatique quantique menace de casser les algorithmes de signature numérique classiques (RSA, ECC) utilisés pour sécuriser les mises à jour de firmware (Secure Boot / OTA). Les systèmes embarqués critiques risquent d'être flashés avec des malwares impossibles à détecter si les clés de signature sont compromises par un ordinateur quantique ("Harvest now, decrypt later" s'applique aussi à l'ingénierie inverse des firmwares).
- **L'approche technique :** Un compilateur d'obfuscation de firmware et une chaîne d'outils de signature PQC (Post-Quantum Cryptography) intégrée (ex: CRYSTALS-Dilithium/Falcon), optimisée pour minimiser l'empreinte mémoire et le temps de démarrage sur des microcontrôleurs (MCU) à ressources limitées, couplée à un obfuscateur de code polymorphe.
- **Pourquoi une solution générique/SaaS classique échoue :** Les algorithmes PQC standardisés par le NIST nécessitent souvent beaucoup plus de mémoire (RAM/Flash) et de cycles CPU que RSA/ECC. Un simple changement d'API ne suffit pas ; il faut reprogrammer la logique de bootloader bas niveau et l'adapter au hardware spécifique.
- **Risques majeurs & Dépendances :** Contraintes de taille de signature PQC qui peuvent dépasser la mémoire disponible sur les vieux MCU ; évolution lente des standards de l'industrie (NIST) ; risque d'introduction de nouvelles vulnérabilités (side-channel) dans l'implémentation PQC optimisée.
