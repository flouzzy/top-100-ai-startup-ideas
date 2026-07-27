<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD036 MD037 MD039 MD041 MD060 -->

# Candidat : Firmware Trust OT

- **Domaine principal :** Cybersécurité & Résilience
- **Modèle économique :** B2B
- **Cible :** Infrastructures critiques (centrales électriques, usines de traitement des eaux, pipelines), fabricants d'automates (PLCs).
- **Le problème urgent :** Les automates industriels (OT/ICS) exécutent souvent des firmwares vieux de 10 ans sans mécanisme d'authentification cryptographique. Une mise à jour compromise (Supply Chain Attack) ou un accès physique permet de prendre le contrôle d'infrastructures physiques critiques (ex: Stuxnet).
- **L'approche technique :** Une architecture Zero-Trust implantée au niveau du micro-contrôleur : un micro-hyperviseur bare-metal qui isole l'exécution du code industriel (ladder logic) des piles réseau, et valide l'intégrité de la mémoire en temps réel via des puces TPM (Trusted Platform Module).
- **Pourquoi une solution générique/SaaS classique échoue :** Les solutions IT classiques (EDR type Crowdstrike, VPNs) ne peuvent pas être installées sur un automate industriel de 500 MHz avec 2 Mo de RAM fonctionnant sous un OS temps réel (RTOS). Il faut une ingénierie de bas niveau (C/Rust) respectant des contraintes de temps réel strictes.
- **Risques majeurs & Dépendances :** Les industriels ont peur de toucher aux systèmes qui fonctionnent ("If it ain't broke, don't fix it"); nécessite des partenariats avec les équipementiers (Siemens, Schneider) ou l'injection risquée de code dans du matériel legacy; longévité des cycles de remplacement (15-30 ans).
