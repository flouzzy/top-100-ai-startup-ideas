<!-- markdownlint-disable MD013 -->

# Candidat : PQC Satellite HSM (Hardware Security Module) Mesh

- **Domaine principal :** Cybersécurité & Résilience / Deep Tech Infra
- **Modèle économique :** B2B / M2M
- **Cible :** Opérateurs de constellations satellites (Starlink, Kuiper), fournisseurs de cloud gouvernemental, et institutions financières globales.
- **Le problème urgent :** Les clés de chiffrement symétriques échangées par les constellations satellites (LEO) pour sécuriser le trafic global sont vulnérables aux futures attaques quantiques (SNDL - Store Now, Decrypt Later). Mettre à jour l'infrastructure spatiale avec des algorithmes Post-Quantique (PQC) est un cauchemar car le hardware spatial (HSM) existant est sous-dimensionné pour la lourdeur des signatures PQC (ex: Dilithium, Falcon), entraînant des latences fatales pour le routage orbital inter-satellites (ISL).
- **L'approche technique :** Un système d'exploitation sécurisé (Zero-Trust) couplé à un accélérateur matériel (FPGA/ASIC) optimisé pour l'espace et dédié exclusivement aux opérations mathématiques sur les réseaux (lattices), au cœur de la plupart des algos PQC. Il permet une génération et un échange de clés PQC ultra-rapides et à faible consommation énergétique directement entre les satellites, sans repasser par des stations sol vulnérables.
- **Pourquoi une solution générique/SaaS classique échoue :** C'est un problème d'architecture matérielle et de contraintes de l'environnement spatial (radiations, limites de puissance). Un simple patch logiciel PQC sur les CPU rad-hard existants des satellites s'effondrerait sous le poids computationnel ou consommerait trop de batterie orbitale.
- **Risques majeurs & Dépendances :** Long cycle de qualification spatiale (radiation-hardening). Standardisation finale du NIST sur les algorithmes PQC encore en cours d'adoption. Coût de déploiement d'une nouvelle génération de hardware en orbite.
