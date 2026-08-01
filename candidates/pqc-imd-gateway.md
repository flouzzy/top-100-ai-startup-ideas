<!-- markdownlint-disable MD013 -->

# Candidat : PQC IMD Gateway

- **Domaine principal :** Cybersécurité
- **Modèle économique :** B2B2C
- **Cible :** Les fabricants de dispositifs médicaux implantables (IMD - pacemakers, neurostimulateurs) et les hôpitaux, confrontés aux normes réglementaires imminentes de la FDA/MDR sur la cybersécurité.
- **Le problème urgent :** Les implants médicaux actuels utilisent des cryptographies classiques (RSA/ECC) qui seront vulnérables aux attaques quantiques (Harvest Now, Decrypt Later). Mettre à jour un pacemaker pour du chiffrement post-quantique (PQC) est impossible car ces puces ont des ressources mémoire et batterie critiques et limitées.
- **L'approche technique :** Une passerelle matérielle/logicielle ultra-basse consommation (sous forme de wearable ou de hub de chevet) agissant comme un bouclier PQC. Elle traduit les communications PQC du réseau externe vers des protocoles légers et sécurisés par clés symétriques gérées dynamiquement vers l'implant.
- **Pourquoi une solution générique/SaaS classique échoue :** Un SaaS ne peut pas interagir directement avec le matériel sous-cutané sans drainer la batterie vitale du patient. Le défi réside dans l'optimisation extrême au niveau du firmware, respectant les contraintes strictes des dispositifs médicaux implantés.
- **Risques majeurs & Dépendances :** Longueur des cycles de certification FDA/CE (MDR), complexité d'intégration avec l'écosystème fermé des grands fabricants de MedTech (Medtronic, Abbott), et gestion de la latence pour les interventions critiques.
