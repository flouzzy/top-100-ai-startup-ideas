<!-- markdownlint-disable MD013 -->

# Candidat : Agent Compute Liquidity

- **Domaine principal :** IA & Agents autonomes
- **Modèle économique :** B2B / M2M
- **Cible :** Plateformes d'agents autonomes, fournisseurs de cloud spécialisé (GPU-as-a-service), entreprises déployant des flottes d'agents d'inférence.
- **Le problème urgent :** Les agents autonomes (par exemple, pour le trading, la recherche, le code) ont des besoins en puissance de calcul (inférence) extrêmement volatils et imprévisibles (bursts). Réserver des GPU en permanence coûte trop cher, et s'appuyer sur du cloud spot est trop lent et incertain pour les tâches d'agents critiques.
- **L'approche technique :** Un protocole d'allocation de ressources (Compute Broker) de niveau M2M (Machine-to-Machine) ultra-faible latence, permettant aux agents de négocier, réserver et payer dynamiquement (via des micro-transactions ou un ledger rapide) des fractions de GPU/TPU à la milliseconde près, en fonction de leur priorité et budget internes.
- **Pourquoi une solution générique/SaaS classique échoue :** L'orchestration Kubernetes classique (HPA) est trop lente (secondes/minutes) pour l'économie agentique où un agent doit prendre une décision de scaling sub-seconde. Il faut un protocole de marché natif pour les machines.
- **Risques majeurs & Dépendances :** Adoption d'un standard de paiement/négociation M2M ; sécurité du multi-tenant sur les GPU fractionnés (side-channel attacks) ; latence réseau entre l'agent et la ressource allouée.
