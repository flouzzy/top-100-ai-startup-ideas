<!-- markdownlint-disable MD013 -->
# Candidat : OT/ICS Zero-Trust Micro-Segmentation Mesh

* **Domaine principal :** Cybersécurité & Résilience
* **Modèle économique :** B2B
* **Cible :** Opérateurs d'infrastructures critiques (OIV/OSE), réseaux électriques, usines chimiques, traitement des eaux, et grands sites manufacturiers
* **Le problème urgent :** Les systèmes de contrôle industriel (OT/ICS) utilisent des protocoles legacy en clair (Modbus, DNP3) sans authentification. Une intrusion latérale (ex: via un ransomware ou un malware type Stuxnet/Triton) peut se propager instantanément, paralysant la production et menaçant la sécurité physique des installations, entraînant des pertes chiffrées en millions par heure.
* **L'approche technique :** Déploiement d'une architecture de Zero-Trust bas niveau directement sur les réseaux OT. Un maillage de micro-segmentation matérielle/logicielle intercepte, inspecte et filtre chaque trame de communication industrielle en temps réel (DPI - Deep Packet Inspection) sans introduire de latence bloquante pour les processus physiques.
* **Pourquoi une solution générique/SaaS classique échoue :** Les solutions IT classiques (VPN, pare-feu traditionnels) sont incompatibles avec les contraintes temps-réel (millisecondes) des automates (PLC/SCADA) et ne comprennent pas les protocoles propriétaires industriels. Une approche purement cloud est inacceptable pour des environnements air-gapped ou nécessitant une continuité absolue.
* **Risques majeurs & Dépendances :** La moindre latence introduite ou un faux positif peut déclencher un arrêt d'urgence de l'usine, résistance culturelle massive des ingénieurs d'exploitation à modifier des réseaux de production en activité, nécessité de certifications industrielles strictes (ex: IEC 62443).
