<!-- markdownlint-disable MD013 MD028 MD033 MD036 MD039 MD041 MD060 -->
# Candidat : AgentPay

* **Modèle économique :** M2M (Machine-to-Machine)
* **Cible :** Développeurs de frameworks d'agents autonomes, entreprises déployant des flottes d'IA, fournisseurs de services API.
* **Le problème urgent :** Les agents autonomes n'ont pas la capacité juridique ou technique de détenir des moyens de paiement traditionnels. Lorsqu'un agent IA doit négocier et acheter dynamiquement de la donnée, de la puissance de calcul ou un service API à un autre agent, il manque un protocole standardisé de micro-règlement et de mise en séquestre sans friction humaine. Cela bloque l'émergence d'une véritable économie entre machines.
* **L'approche technique :** Une infrastructure de paiement par API (ledger cryptographique haute performance) dédiée aux machines. Elle intègre des contrats de séquestre programmables (escrow) : l'agent acheteur provisionne des jetons/crédits, l'agent vendeur exécute la tâche en fournissant une preuve d'exécution, et la plateforme règle instantanément la transaction.
* **Pourquoi ChatGPT/Gemini échoue seul :** Les LLMs sont des moteurs de raisonnement cognitif, pas des infrastructures de paiement ou de confiance cryptographique. Un prompt ne peut pas retenir des fonds de manière sécurisée, ni garantir l'exécution déterministe d'une transaction financière avec un tiers.
