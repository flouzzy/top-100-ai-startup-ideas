<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : OT/ICS Zero-Trust Isolation Fabric

- **Domaine principal :** Cybersécurité & Résilience
- **Modèle économique :** B2B
- **Cible :** Industries lourdes, usines d'armement, centrales nucléaires, usines de traitement des eaux, et chaînes logistiques maritimes (ports).
- **Le problème urgent :** L'IT (informatique classique) et l'OT (Operation Technology, les automates industriels) convergent, exposant des automates programmables (PLC) vieux de 20 ans, impossibles à patcher, aux ransomwares et attaques par états-nations. Un hack entraîne l'arrêt physique de la production, ou pire, un désastre industriel.
- **L'approche technique :** Un maillage de sécurité (fabric) matériel et logiciel déployé au niveau de la couche 2 du réseau (L2). Des micro-firewalls sur rail DIN qui appliquent un Zero-Trust déterministe (micro-segmentation) avec une inspection profonde des protocoles industriels propriétaires (Modbus, DNP3, Profinet) pour isoler les machines sans casser la latence temps réel requise par l'usine.
- **Pourquoi une solution générique/SaaS classique échoue :** L'IT security (Crowdstrike, Palo Alto) nécessite l'installation d'agents sur des OS modernes. On ne peut pas installer un agent sur un automate Siemens des années 90 qui gère une vanne de pression. Un simple scan réseau SaaS ferait crasher l'automate.
- **Risques majeurs & Dépendances :** Forte réticence à l'adoption des ingénieurs OT qui craignent la perturbation des opérations. Certification industrielle matérielle longue et coûteuse (IEC 62443).
