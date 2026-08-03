<!-- markdownlint-disable MD009 MD010 MD013 MD022 MD028 MD032 MD033 MD034 MD036 MD037 MD039 MD041 MD058 MD060 -->
# Candidat : Haptic Teleop OS

- **Domaine principal :** Robotique & Systèmes embarqués
- **Modèle économique :** B2B (PaaS Robotique)
- **Cible :** Industries dangereuses (nucléaire, offshore), chirurgie à distance, et logistique spatiale nécessitant de la manipulation fine.
- **Le problème urgent :** La téléopération de robots dans des environnements hostiles souffre d'une perte d'information tactile et d'une latence réseau qui rendent la manipulation d'objets délicats ou inconnus lente et propice aux accidents. L'humain manque de retour de force (proprioception robotique) intuitif.
- **L'approche technique :** Un système d'exploitation et protocole de compression vidéo/haptique ultra-basse latence couplé à une IA de prédiction locale. Si la connexion est instable, l'IA d'edge computing sur le robot "complète" l'intention de mouvement de l'opérateur en temps réel tout en renvoyant un retour haptique synthétisé (force-feedback) au pilote.
- **Pourquoi une solution générique/SaaS classique échoue :** L'encodage vidéo standard (H.264/H.265) et les protocoles TCP/IP n'ont pas été conçus pour le streaming simultané de données sensorielles (kinématiques, force) avec des garanties de latence sous la barre des 10 millisecondes.
- **Risques majeurs & Dépendances :** Besoin d'intégration intime avec le hardware (capteurs de couple, effecteurs) qui est très fragmenté selon les constructeurs de robots. L'acceptabilité par les opérateurs habitués à un contrôle 100% manuel.
