<!-- markdownlint-disable MD013 -->

# Candidat : Acoustic Levitation Foundry

- **Domaine principal :** Robotique & Systèmes embarqués / Deep Tech Infra
- **Modèle économique :** B2B
- **Cible :** Industries pharmaceutiques (cristallisation de protéines), fabricants de semi-conducteurs exotiques, et R&D en matériaux ultra-purs.
- **Le problème urgent :** Lors de la fabrication de certains matériaux avancés (comme les alliages amorphes, les verres optiques ZBLAN, ou des cristaux de protéines), tout contact avec les parois d'un creuset ou d'un conteneur introduit des impuretés ou déclenche une nucléation hétérogène non désirée, ruinant la pureté ou la structure amorphe du matériau.
- **L'approche technique :** Un réacteur de lévitation acoustique (ou aéro-acoustique) industriel, contrôlé par des réseaux de transducteurs ultrasoniques à commande de phase. Un agent de contrôle en temps réel (Reinforcement Learning) ajuste dynamiquement le champ de pression acoustique pour maintenir la gouttelette ou le matériau en fusion en lévitation stable, tout en modulant la température par chauffage laser sans aucun contact physique, même face aux changements de viscosité.
- **Pourquoi une solution générique/SaaS classique échoue :** Il s'agit d'un problème de physique appliquée et de contrôle matériel temps réel à très haute fréquence (kHz). Le logiciel seul ne peut rien faire sans le hardware acoustique spécifique, et les algorithmes PID classiques ne peuvent pas gérer l'instabilité chaotique d'un fluide en fusion changeant de phase en lévitation.
- **Risques majeurs & Dépendances :** Limite de masse levitable dictée par les lois de la physique acoustique terrestre (difficile de faire léviter des objets denses et lourds sous gravité 1G). Consommation d'énergie et gestion thermique des transducteurs.
