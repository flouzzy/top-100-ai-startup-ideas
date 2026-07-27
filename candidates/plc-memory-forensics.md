<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : PLC Memory Forensics

- **Domaine principal :** Cybersécurité & Résilience (OT/ICS)
- **Modèle économique :** B2B
- **Cible :** CISO industriels, OIV (Opérateurs d'Importance Vitale), gestionnaires de réseaux électriques, usines de traitement des eaux et manufacturiers lourds.
- **Le problème urgent :** Les attaques de type "Living off the Land" et les malwares s'exécutant uniquement en mémoire RAM des automates programmables industriels (PLC) sont indétectables par les systèmes de sécurité réseau (IDS/IPS) ou par l'analyse statique du firmware. Un acteur étatique peut manipuler la logique physique d'une centrifugeuse ou d'une vanne de gaz de l'intérieur, causant des dommages physiques irrémédiables, sans laisser de traces sur le réseau.
- **L'approche technique :** Un moteur d'analyse forensique de mémoire vive (RAM) temps réel, spécialisé pour les architectures matérielles propriétaires des PLC (ARM, PowerPC, architectures exotiques). Le système utilise un accès matériel (JTAG/dDMA) ou un agent ultra-léger pour capturer des instantanés mémoire sans perturber les cycles d'exécution temps-réel stricts (jitter < 1ms), analysés ensuite par des modèles d'IA pour détecter les anomalies de comportement des pointeurs ou des structures de données.
- **Pourquoi une solution générique/SaaS classique échoue :** L'EDR (Endpoint Detection and Response) classique n'existe pas pour les automates industriels. Vous ne pouvez pas installer un agent CrowdStrike sur un PLC Siemens S7 ou Allen-Bradley. L'analyse réseau ne voit pas ce qui se passe _dans_ la puce une fois compromise.
- **Risques majeurs & Dépendances :** Forte réticence des constructeurs (OEMs) à autoriser l'accès bas niveau à leurs automates. Risque systémique de faire crasher un PLC en production lors de la capture mémoire (causant un arrêt d'usine très coûteux).
