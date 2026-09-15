<!-- markdownlint-disable MD013 -->

# Candidat : RF Side-Channel Firewall

- **Domaine principal :** Cybersécurité & Résilience
- **Modèle économique :** B2B
- **Cible :** Industries critiques, Datacenters souverains, Défense, Opérateurs d'Infrastructures Vitales (OIV)
- **Le problème urgent :** L'exfiltration de données cryptographiques ou sensibles via des attaques par canaux auxiliaires (Side-Channel) utilisant les émissions électromagnétiques (RF) ou acoustiques des processeurs. Les environnements dits "air-gapped" ne sont plus sûrs face aux capteurs avancés de l'espionnage industriel.
- **L'approche technique :** Un pare-feu physique et logiciel combinant une couverture métamatériau absorbant spécifiquement les fréquences de fuite CPU, et un orchestrateur logiciel (hyperviseur) qui injecte de manière dynamique du bruit algorithmique (entropy injection) dans les cycles CPU pour masquer la signature d'exécution des processus cryptographiques.
- **Pourquoi une solution générique/SaaS classique échoue :** C'est un problème fondamental de physique matérielle. Les pare-feux logiciels réseau ou les EDR sont aveugles aux émissions radiofréquences générées par les transistors d'un CPU exécutant une clé AES.
- **Risques majeurs & Dépendances :** Difficulté de calibrer le bruit algorithmique sans détruire les performances (overhead CPU), nécessité de déployer des composants physiques complexes dans des datacenters existants, vente longue et cycle B2G complexe.
