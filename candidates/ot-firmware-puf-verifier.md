<!-- markdownlint-disable MD013 -->

# Candidat : OT Firmware PUF Verifier

- **Domaine principal :** Cybersécurité & Résilience / Robotique & Systèmes embarqués
- **Modèle économique :** B2B
- **Cible :** Opérateurs d'infrastructures critiques (réseaux électriques, traitement de l'eau, pipelines), fabricants d'équipements industriels (OEM), industries de la défense.
- **Le problème urgent :** Les attaques sur les environnements OT (Operational Technology) et ICS ciblent de plus en plus bas dans la pile, modifiant le firmware des capteurs et automates (PLC) de manière furtive. Les solutions de cybersécurité informatique classiques ne peuvent pas vérifier l'intégrité matérielle de ces appareils sans provoquer d'arrêts de production inacceptables. L'incertitude quant à l'altération physique ou logicielle d'un capteur critique est une vulnérabilité fatale.
- **L'approche technique :** Utilisation des Physical Unfocusable Functions (PUF) inhérentes au silicium de chaque composant pour générer une empreinte digitale matérielle unique, non clonable. Un protocole de "Zero-Trust bas niveau" interroge ces PUF à chaque mise à jour de firmware ou cycle d'opération, croisant la signature matérielle avec le hash cryptographique du firmware, garantissant qu'il tourne sur la puce légitime, non falsifiée.
- **Pourquoi une solution générique/SaaS classique échoue :** Un scanner de vulnérabilités réseau ou un EDR (Endpoint Detection and Response) ne peut pas fonctionner sur un microcontrôleur d'automate avec quelques kilo-octets de RAM. La vérification doit lier la cryptographie à la physique de la puce elle-même, ce qu'aucun SaaS de gestion des logs ne peut faire.
- **Risques majeurs & Dépendances :** Nécessité d'intégration au niveau du design matériel (fabricants d'équipements devant inclure le support PUF), gestion du cycle de vie des clés cryptographiques en milieu industriel isolé (air-gapped), dérive physique potentielle des PUF sur des décennies.
