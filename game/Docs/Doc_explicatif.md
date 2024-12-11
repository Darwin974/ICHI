# Document explicatif du projet ICHI
### Sommaire :
- **[L'objectif principal du projet](#objectif-principal)**
- **[Le fonctionnement du programme](#fonctionnement-du-programme)**
- **[Les difficultés rencontrés](#les-difficultés-rencontrés)**

## Objectif principal
L'objectif que je me suis fixé quand j'ai eu l'idée de faire **Ichi** était de réussir à faire un **UNO fonctionnel**, avec une **GUI** de bonne qualité et facile d'utilisation. Je voulais aussi pouvoir mettre le jeu sur **n'importe quel appareil**, c'est pour ça que j'ai décider d'utiliser le framework **kivy** car il permet de pouvoir faire des **packages** pour quasiment tout les **OS**.

## Fonctionnement du programme
### Sommaire :
- Le fichier **[carte.py](#cartepy-)**
- Le fichier **[paquet.py](#paquetpy-)**
- Le fichier **[main.py](#mainpy-)**
- Le fichier **[ui.py](#uipy-)**
- Le fichier **[Ichi.kv](#ichikv-)**

---

### [carte.py](https://github.com/Darwin974/ICHI/blob/main/game/carte.py) :
Le fichier [carte.py](https://github.com/Darwin974/ICHI/blob/main/game/carte.py) définit la classe **`Carte`**, qui représente chaque carte individuelle dans le jeu. 
### Cette classe inclut les attributs suivants :
`valeur` : représente la valeur de la carte, comme un chiffre **(0 à 9)** ou une action spéciale **('+2', 'Inversion', etc)**.
\
`couleur :` représente la couleur de la carte, **'Rouge', 'Bleu', 'Vert', ou 'Jaune'**. Les Jokers n'ont pas de couleur de base.
\
`image` : contient le chemin vers l'image associée à la carte.

### Les méthodes principales de cette classe sont :
`__str__` : retourne une chaîne de caractères représentant la carte sous la forme **"valeur couleur"**, utile pour le débogage ou l'affichage.
\
Des getters pour accéder aux attributs **valeur** et **couleur** de manière sécurisée.

Cette classe sert de structure de base pour toutes les cartes qui seront générées et manipulées dans le jeu.

---

### [paquet.py](https://github.com/Darwin974/ICHI/blob/main/game/paquet.py) :
Le fichier **[paquet.py](https://github.com/Darwin974/ICHI/blob/main/game/paquet.py)** contient la classe `JeuDeCartes`, qui gère l'ensemble des cartes du jeu.
### Attributs principaux :
**`PaquetDeCarte`** : un tableau contenant toutes les cartes du jeu, générées grâce à la méthode `creer_paquet()`.

### Méthodes :
**`creer_paquet()`** : Génère un paquet de **108 cartes**, comme dans le jeu UNO. Ajoute les cartes numériques **(0 à 9)**, les cartes spéciales ('+2', 'Inversion', 'Passer') pour chaque couleur, et les Jokers.
Attribue un chemin d'image spécifique à chaque carte (Ex: `img/Cartes/R/_0.png` pour une carte rouge '0').
Retourne un tableau contenant toutes les cartes sous forme d’objets Carte.

`melanger_paquet()` : mélange les cartes du paquet à l'aide de shuffle de la bibliothèque random.

`piocher()` : retire et retourne la dernière carte du paquet, ou None si le paquet est vide.

`get_nb_cartes()` : retourne le nombre total de cartes dans le paquet.

`get_paquet()` : retourne une liste des cartes sous forme de chaînes de caractères (via leur méthode `__str__`).

Cette classe permet donc de gérer toutes les opérations liées au paquet de cartes du jeu : **création, mélange, et gestion des tirages** pendant la partie.

---

### [main.py](https://github.com/Darwin974/ICHI/blob/main/game/main.py) :
Le fichier **`main.py`** contient la classe principale `UnoGame`, qui gère la logique et les interactions du jeu.

### Attributs principaux :
**`game_screen`** : représente l'écran de jeu fourni par le fichier **`ui.py`**. Cela permet de lié étroitement le fichier `main.py` et `ui.py`.
\
**`jeu`** : instance de la classe `JeuDeCartes`, utilisée pour manipuler le paquet de cartes **(création, mélange, pioche)**.
\
**`joueur`** et **`ia`** : dictionnaires contenant les informations du joueur et de l'IA, notamment leur nom et leur main (7 cartes initialement piochées).
\
**`pioche`** : tableau contenant les cartes restantes dans le paquet après distribution.
\
**`talon`** : liste des cartes jouées, initialisée avec une carte piochée du paquet.
\
**`tour_joueur`** : booléen déterminant le joueur actif : **`True`** pour le joueur, **`False`** pour l'IA.

### Méthodes principales :

**`piocher_carte()`** : 
Pioche une carte du paquet et la retourne. Utilise la méthode `piocher()` de la classe `JeuDeCartes`.

**`jouer_carte(carte)`** : Joue une carte en l'ajoutant au talon avec `.append`.

**`carte_valide(carte, carte_actuelle)`** :
- Vérifie si une carte est valide par rapport à la carte actuelle du talon.
  - Une carte est valide si elle a la même couleur, la même valeur, ou si c'est un Joker.
  - Si la carte initiale du jeu est un Joker le joueur peut posé n'importe quelle carte.

**`appliquer_effet(carte)`** :
\
Applique les effets des cartes spéciales :
- **`+2`** : ajoute deux cartes à la main de l'adversaire.
- **`Joker +4`** : ajoute quatre cartes à la main de l'adversaire.
- **`Passer`** : saute le prochain tour.

**`tour_ia()`** :
\
Gère le tour de l'IA avec les étapes suivantes :
  1. Cherche une carte valide à jouer dans sa main.
  2. Si une carte valide est trouvée :
     - La joue sur le talon.
     - Si c'est un Joker ou un Joker +4, l'IA choisit une couleur via **`choisir_couleur_ia()`**.
     - Applique l'effet de la carte jouée.
  3. Sinon, pioche une carte et l'ajoute à sa main.
  4. Met à jour le statut du tour (`tour_joueur`).

**`choisir_couleur_ia()`** :
\
Permet à l'IA de choisir une couleur lorsque nécessaire (par exemple, après avoir joué un Joker).
  - Prend la couleur la plus fréquente dans sa main pour maximiser ses chances.
  - Si aucune couleur n'est présente (Ex : l'ia n'a que des Joker), choisit une couleur aléatoire.

**`verifier_victoire()`** :
\
Vérifie les conditions de fin de partie :
  - Si la pioche est vide, la partie se termine par un match nul.
  - Si la main du joueur ou de l'IA est vide, il y a un vainqueur.
  - Sinon, la partie continue.

### Lancement du jeu :
La section suivante démarre le jeu avec la méthode **`Ichi().run()`** si le script est exécuté directement :

```python
if __name__ == '__main__':
    Ichi().run()
```

### Fonctionnalités globales :
- **Gestion des cartes** : pioche, talon, et vérification de validité.
- **Logique de jeu** : alternance des tours entre le joueur et l'IA.
- **Effets des cartes spéciales** : impact sur les joueurs selon les règles de [**Ichi**](https://github.com/Darwin974/ICHI/blob/main/game/Docs/Ichi_rules.md).
- **Condition de victoire** : détection de la fin de partie et des gagnants.

Cette classe centralise donc toutes les opérations essentielles pour simuler une partie de Uno, en combinant la logique du jeu avec les interactions utilisateur situées dans [ui.py](#uipy-).

---

### [ui.py](https://github.com/Darwin974/ICHI/blob/main/game/ui.py) :

---

### [Ichi.kv](https://github.com/Darwin974/ICHI/blob/main/game/Ichi.kv) :

## Les difficultés rencontrés

---
**By DAMOUR ROUGEMONT Maxime**