<!-- markdownlint-disable MD013 -->

# Candidat : ICS Sentinel Sandboxing

- **Domaine principal :** Cybersécurité & Résilience (OT/ICS)
- **Modèle économique :** B2B
- **Cible :** Opérateurs industriels (pétrole/gaz, traitement de l'eau, centrales électriques, usines de production).
- **Le problème urgent :** Les systèmes de contrôle industriel (PLC, SCADA) reçoivent des mises à jour de firmware qui peuvent être compromises (Supply Chain Attack, cf. Stuxnet ou SolarWinds). Il est impossible de tester ces firmwares en production sans risquer un arrêt d'usine ou une catastrophe physique.
- **L'approche technique :** Création d'une plateforme d'émulation matérielle hyper-réaliste (Digital Twin de niveau instruction) qui exécute et observe le comportement dynamique d'un firmware PLC ciblé en temps réel pour détecter les anomalies logiques avant le flashage.
- **Pourquoi une solution générique/SaaS classique échoue :** Les antivirus IT classiques ne comprennent pas les protocoles OT (Modbus, DNP3) ni les architectures matérielles exotiques (ARM, PowerPC anciens). Il faut une émulation au niveau des registres processeurs spécifiques à chaque équipementier industriel (Siemens, Schneider, Rockwell).
- **Risques majeurs & Dépendances :** Les firmwares PLC sont fermés, propriétaires et souvent chiffrés. Construire les émulateurs exacts demande un reverse-engineering complexe à la limite de la légalité des brevets OEM.
