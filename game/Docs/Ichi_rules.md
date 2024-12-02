##### Spoiler : Les régles du jeu sont exactement les mêmes que celles du UNO. :wink:

### Objectif du jeu
Le but est de se débarrasser de toutes ses cartes avant l'adversaire, tout en respectant les règles de correspondance des cartes.

### Déroulement du jeu
**Distribution des cartes :**
Chaque joueur **(l'humain et l'IA)** commence avec **7 cartes**.
Une carte est placée au **talon** (*pile où jouer les cartes*) pour débuter la partie.

**Tour des joueurs :**
Le jeu commence avec le joueur.
Les tours alternent entre le joueur et l'IA.

**Action pendant un tour :**
Le joueur joue une carte de sa main qui correspond à la couleur ou à la valeur de la carte sur le talon.
**Si aucune carte** ne peut être jouée, le joueur doit **piocher une carte**.
Après avoir joué une carte, l'effet de celle-ci est appliqué **(voir ["Effets des cartes"](#effets-des-cartes-spéciales))**.

### Cartes valides
**Une carte est valide si elle :**
A la **même couleur** que la carte sur le talon.
A la **même valeur** que la carte sur le talon.
Est un **Joker** ou un **Joker +4** (ces cartes peuvent être jouées à tout moment).

### Effets des cartes spéciales
**Carte +2 :**
L'adversaire **pioche 2** cartes.

**Carte Passer :**
Le joueur suivant **passe son tour**.

**Joker :**
Le joueur **choisit la couleur** à jouer.

**Joker +4 :**
L'adversaire **pioche 4** cartes.
Le joueur **choisit la couleur** à jouer.

### Victoire
Un joueur gagne dès qu'il n'a plus de cartes en main.
Si la pioche est vide, le jeu se termine et le gagnant est celui qui a le moins de cartes.

### Règles spécifiques à l'IA
L'IA cherche une carte valide dans sa main pour jouer.
Si elle ne peut pas jouer, elle pioche une carte.
Lorsqu'elle joue un Joker ou un Joker +4, elle choisit la couleur la plus fréquente dans sa main. Si aucune couleur n'est dominante, elle choisit une couleur aléatoire.

### Actions utilisateur

**Le joueur peut :**
Cliquer sur une carte pour la jouer.
Piocher une carte si aucune ne peut être jouée.
Choisir une couleur lorsqu'il joue un Joker ou un Joker +4.