<!-- markdownlint-disable MD013 -->

# Candidat : Neural TeleOp Engine

- **Domaine principal :** Robotique / World Models
- **Modèle économique :** B2B (Licensing logiciel / API Edge)
- **Cible :** Entreprises de chirurgie robotique, opérateurs de drones sous-marins (ROV), exploitation minière à distance, logistique intercontinentale.
- **Le problème urgent :** La téléopération de robots à grande distance souffre de la latence du réseau (ping de 200ms à 2s). Cette latence provoque le mal de mer cognitif chez l'opérateur et rend les manipulations de précision dangereuses ou impossibles, bloquant l'adoption de l'industrie.
- **L'approche technique :** Un modèle génératif de prédiction d'état (World Model) embarqué en périphérie (Edge) du côté de l'opérateur. Il synthétise un flux vidéo et haptique artificiel sans latence en prédisant l'état futur immédiat de l'environnement physique et du robot (Next-Frame Prediction).
- **Pourquoi une solution générique/SaaS classique échoue :** Il faut une prédiction vidéo cohérente avec les lois de la physique en moins de 10ms, ce que les API LLM/Vision actuelles ou les algos de compression vidéo ne peuvent pas faire.
- **Risques majeurs & Dépendances :** Risque critique d'hallucination de l'IA (par exemple, masquer un obstacle soudain dans la prédiction), ce qui pourrait entraîner des crashs ou, dans le cas de la chirurgie, des accidents mortels. Exigence matérielle (GPU locaux puissants).
