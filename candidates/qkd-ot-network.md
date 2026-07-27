<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : QKD OT Guardian

- **Domaine principal :** Cybersécurité & Quantique
- **Modèle économique :** B2B
- **Cible :** Opérateurs d'infrastructures critiques (réseaux électriques, centrales nucléaires, stations d'épuration) (CISO, OT Security Managers).
- **Le problème urgent :** Les réseaux opérationnels (OT/ICS) utilisent des protocoles industriels legacy vulnérables aux attaques "Store Now, Decrypt Later" par de futurs ordinateurs quantiques. La mise à jour matérielle des automates (PLC) est financièrement et physiquement impossible à grande échelle.
- **L'approche technique :** Un orchestrateur réseau de distribution de clés quantiques (QKD) et cryptographie post-quantique (PQC) agissant comme une surcouche de sécurité (Zero-Trust hardware gateway) placée devant les réseaux OT existants sans modifier les terminaux finaux.
- **Pourquoi une solution générique/SaaS classique échoue :** Les VPN/SaaS de sécurité traditionnels ajoutent trop de latence pour le contrôle industriel temps-réel (qui exige des temps de réponse < 5ms) et s'appuient sur une cryptographie classique (RSA/ECC) vouée à devenir obsolète.
- **Risques majeurs & Dépendances :** Standardisation PQC (NIST) encore en cours, coût matériel des passerelles QKD, nécessité de certifications industrielles strictes (IEC 62443).
