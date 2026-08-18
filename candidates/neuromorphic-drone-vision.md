<!-- markdownlint-disable MD013 -->

# Candidat : Neuromorphic Swarm Vision Engine

- **Domaine principal :** Robotique & Systèmes embarqués / IA
- **Modèle économique :** B2B / B2G
- **Cible :** Défense (essaims de drones tactiques), logistique d'urgence spatiale, inspection d'infrastructures critiques (pipelines, lignes haute tension).
- **Le problème urgent :** Les drones et robots actuels utilisent des caméras basées sur des frames (FPS). Cela génère une quantité massive de données redondantes, sature la bande passante, draine la batterie pour le traitement de l'image (calcul par GPU) et souffre de flou de mouvement, rendant l'évitement d'obstacles à très haute vitesse presque impossible en edge.
- **L'approche technique :** Remplacement de la pile de vision standard par des caméras événementielles (Neuromorphic/Event-based vision) associées à un compilateur embarqué de Réseaux de Neurones à Impulsions (Spiking Neural Networks - SNNs) sur des puces analogiques dédiées (ex: Akida, Loihi). Le système ne traite que les changements de pixels (comme un œil humain), permettant un traitement à micro-secondes de latence pour quelques milliwatts.
- **Pourquoi une solution générique/SaaS classique échoue :** Un LLM de vision par ordinateur (VLM) ou YOLO sur GPU demande trop d'énergie (SWaP-C : Size, Weight, Power, and Cost) pour des nano-drones autonomes. La solution nécessite une refonte matérielle et algorithmique du signal visuel lui-même, supprimant le concept d'image "frame".
- **Risques majeurs & Dépendances :** Écosystème logiciel balbutiant pour les SNNs, difficulté de l'entraînement des modèles neuromorphiques par rapport à la rétropropagation standard, dépendance envers les rares fonderies produisant des capteurs événementiels.
