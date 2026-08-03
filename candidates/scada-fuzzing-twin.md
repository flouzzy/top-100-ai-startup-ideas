<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->

# Candidat : SCADA Fuzzing Twin

- **Domaine principal :** Cybersécurité & Résilience (OT/ICS)
- **Modèle économique :** B2B
- **Cible :** Opérateurs d'infrastructures critiques (OIV), producteurs d'énergie, réseaux de distribution d'eau, industrie lourde.
- **Le problème urgent :** Il est impossible de réaliser des tests de pénétration agressifs ou du fuzzing sur des systèmes de contrôle industriel (SCADA/PLC) en production sous peine d'interruption de service, de casse matérielle, ou d'explosion. Par conséquent, les vulnérabilités zero-day restent indétectées jusqu'à leur exploitation.
- **L'approche technique :** Extraction du firmware et configuration réseau des PLC/RTU pour créer un jumeau numérique hyper-réaliste (hardware-in-the-loop virtualisé). Le système utilise ensuite un moteur d'IA pour générer automatiquement des vecteurs de fuzzing massifs (injection de paquets industriels malformés) sur le jumeau afin d'identifier des crashes ou comportements anormaux.
- **Pourquoi une solution générique/SaaS classique échoue :** Les scanners de vulnérabilités IT classiques (Nessus, etc.) se contentent de vérifier les versions des OS. Ils ne comprennent pas les protocoles OT propriétaires (Modbus, DNP3, PROFINET) et ne peuvent simuler la logique physique associée aux capteurs/actionneurs.
- **Risques majeurs & Dépendances :** Difficulté à émuler parfaitement l'architecture matérielle (SoC, ASIC propriétaires) de certains automates industriels legacy. Réticence des constructeurs à faciliter l'extraction de firmware.
