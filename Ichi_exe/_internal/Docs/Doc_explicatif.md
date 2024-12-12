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
Le fichier **`ui.py`** définit l'interface utilisateur pour le jeu Uno. Il utilise **Kivy**, un framework Python pour créer des applications avec des interfaces graphiques.

### Classes principales :

#### **`GameScreen`**
La classe **`GameScreen`** hérite de **`Screen`** de Kivy et représente l'écran principal du jeu où les interactions de parties se déroulent.

### Méthodes principales :
**`on_enter()`** :
- Méthode déclenchée à l'entrée sur l'écran.
- Initialise une partie en créant une instance de la classe **`UnoGame`** (de **`main.py`**).
- Affiche la main du joueur, la carte du talon, et les cartes restantes de l'IA.

**`afficher_main()`** :
- Affiche les cartes du joueur en tant que boutons, avec l'image de chaque carte.
- Chaque bouton est lié à l'action **`jouer_carte(carte)`**, déclenchée lorsqu'on clique dessus.

**`afficher_cartes_ia()`** :
\
Met à jour l'affichage du nombre de cartes restantes dans la main de l'IA.

**`jouer_carte(carte)`** :
- Permet de jouer une carte si elle est valide (vérification avec **`carte_valide()`**).
- Gère les **Jokers** en ouvrant une fenêtre pour choisir une couleur avec **`choisir_couleur()`**.
- Si la carte n’est pas valide, un message est affiché.

**`appliquer_couleur(carte, couleur)`** :
- Applique une couleur choisie à un Joker ou **`Joker +4`**, puis exécute les effets et passe au tour suivant.

**`appliquer_effet_et_tour(carte)`** :
- Applique les effets des cartes spéciales via **`appliquer_effet()`** de **`UnoGame`**.
- Vérifie si un joueur a gagné.
- Alterne les tours entre le joueur et l'IA.

**`afficher_carte_talon()`** :
- Met à jour l'affichage de la carte actuelle du talon.
- Gère les messages contextuels pour les Jokers et leur couleur.

**`prochain_tour()`** :
- Gère le passage au tour suivant.
- Affiche la main du joueur si c’est son tour, ou programme l'action de l'IA via un délai avec **`Clock.schedule_once()`** de **Kivy**.

**`jouer_tour_ia()`** :
- Appelle la méthode **`tour_ia()`** de **`UnoGame`** pour exécuter le tour de l’IA.
- Met à jour l’affichage après le tour de l’IA et passe au joueur suivant.

**`passer_tour()`** :
\
Permet au joueur de passer son tour.
- Le joueur pioche une carte, puis c’est au tour de l’IA.

**`choisir_couleur(callback)`** :
- Affiche une fenêtre permettant au joueur de sélectionner une couleur pour son Joker.
- La couleur choisie est appliquée via le **callback**.

### Fonctionnalités globales :
- **Affichage dynamique** : Les mains des joueurs et le talon sont mis à jour en temps réel.
- **Interactivité** : Les boutons permettent de jouer des cartes, passer un tour, ou choisir une couleur.
- **Tour de l’IA** : Géré automatiquement après un délai pour simuler une réflexion.

### Intégration avec **`main.py`** :
Le fichier **`ui.py`** agit comme un pont entre la logique du jeu (dans **`main.py`**) et l'interface utilisateur que on personalise avec `Ichi.kv`. Il utilise les méthodes de **`UnoGame`** pour gérer les actions de jeu tout en mettant à jour l'affichage en conséquence.

---

### [Ichi.kv](https://github.com/Darwin974/ICHI/blob/main/game/Ichi.kv) :
Le fichier **`Ichi.kv`** contient les définitions de l'interface utilisateur notre jeu **Ichi**, construit avec **Kivy**. Il structure les écrans, les widgets et leurs propriétés, et applique un style personnalisé pour certains éléments.

### Principales sections :

**Bouton personnalisé, RoundedButton** :
\
Représente un bouton arrondi avec un style spécifique.
\
**Attributs principaux** :
  - `font_name` : définit une police personnalisée, ici une police japonaise.
  - `font_size` : ajuste la taille du texte.
  - `background_color` et `background_normal` : éliminent l'arrière-plan par défaut de Kivy.
  - `canvas.before` : ajoute un rectangle arrondi avec un rayon de 45 pour obtenir **l'effet visuel arrondi**.

**Gestionnaire d'écrans : MyScreenManager** :
\
Contrôle la navigation entre les écrans de l'application.
- Contient **trois écrans** principaux :
  - `HomeScreen` : l'écran d'accueil.
  - `GameSelect` : l'écran de sélection du mode de jeu. (Ne méne que vers solo pour le moment)
  - `GameScreen` : l'écran principal où se déroule la partie.

### Écrans définis :

**Écran d'accueil, HomeScreen** :
- Présente une interface d'accueil avec :
  - **Logo** : une image affichée au centre, redimensionnable pour s'adapter à l'écran.
  - **Bouton "Play"** : redirige vers l'écran de sélection des modes de jeu.
  - **Bouton "Exit"** : ferme l'application.

**Écran de sélection, GameSelect** :
- Permet au joueur de choisir un mode de jeu.
- Inclut :
  - Un **Label** : indique à l'utilisateur de choisir un mode de jeu.
  - Un **Bouton "Solo"** : redirige vers l'écran de jeu principal.

**Écran principal : GameScreen** :
- Interface de la partie principale, utilisant divers widgets pour afficher l'état du jeu :
  - **Bouton de retour** : permet de revenir à l'écran d'accueil.
    - `background_normal` : utilise une image personnalisée (icône "return").
  - **Labels dynamiques** :
    - `nb_cartes_ia` : affiche le nombre de cartes dans la main de l'IA.
    - `msg_talon` : affiche les informations concernant la carte au sommet du talon.
    - `message` : permet d'afficher des messages au joueur.
  - **Relayout `talon`** :
    - Zone dédiée pour afficher la carte actuelle au sommet du talon.
  - **BoxLayout `main_joueur`** :
    - Contient les cartes du joueur sous forme d'une liste horizontale.
  - **Bouton "Passer le tour"** :
    - Appelle la méthode `passer_tour()` pour gérer l'alternance des tours.


### Fonctionnalités globales :
**Navigation fluide entre les écrans** :
   - Gestion simplifiée grâce au `ScreenManager`.

**Interface responsive** :
   - Les tailles et positions des éléments sont définies via `size_hint` et `pos_hint` pour s'adapter à différentes résolutions.

**Styles personnalisés** :
   - Les boutons et widgets sont visuellement distincts grâce à l'utilisation de polices spécifiques et d'images personnalisés.

Ce fichier définit donc l'aspect visuel et interactif du jeu tout en restant lié à la logique principale définie dans **`main.py`** et **`ui.py`**.

---

## Les difficultés rencontrés :
Pour la création de ce jeu, j'ai fait face à beaucoup de difficultés, la plupart de celle-ci sont dû au fait de d'utiliser pour la premiére fois **Kivy**. J'ai pris du temps à m'approprier Kivy surtout en python dans le fichier `ui.py` car je trouve que les fonctions python de Kivy ne sont pas forcément facile à comprendre, cependant pour le fichier `Ichi.kv` je n'ai pas eu beaucoup de difficultés malgré le language de programmation **.kv** de Kivy, en fait celui-ci me rappelait beaucoup le **CSS** que je maîtrise assez bien donc je me suis adapté rapidement, il suffisait juste de découvrir comment se nomment les fonctions de Kivy. Mais le fichiers qui m'a vraiment causé le plus de difficultés et de mals de têtes était **`ui.py`** car pour faire communiqué les fonctions python de Kivy avec le fichier de configuration `Ichi.kv` ce n'était pas évident et facile à comprendre je trouve. Par exemple j'ai dû apprendre et comprendre ce qu'était un **`callback`** et une fonction **`lambda`**. Car en lisant dans la documentation kivy et sur des tutos j'ai trouvé cette solution pour éxécuter une fonction aprés l'appuie d'un bouton kivy :
```python
btn.bind(on_release=lambda instance, c=carte: self.jouer_carte(c))
```
Le probléme ici c'est que je ne connaissait pas **`lambda`** et même en cherchant sur internet des informations sur cette fonction de python, je n'ai pas vraiment compris tout de suite donc je faisait un peu n'importe quoi avec pour essayer de faire marcher mais aprés j'ai compris et c'est devenu beaucoup plus facile et j'ai commencé à l'utiliser un peu partout.

Ensuite pour les fonctions python je trouve leur importations un peu laborieuse du fait qu'il faut importer chaque élément à la fois de cette manière :
```python
from kivy.uix.popup import Popup
```
Mais bon je pense que c'est dû au fait que la bibliothéque **Kivy** est très large, et c'est pas si embêtant aprés avoir compris quoi importer pour **son** projet.

La derniere grosse difficulté que j'ai rencontré c'était la comminication entre `main.py` et `ui.py` surtout avec leurs **Class**. Car j'avait quelques probléme où j'avais besoin d'accéder à certains attributs. Par exemple :
```python
for carte in self.game.joueur['main']:
```
Cette ligne ne fonctionnerait pas si je n'avait pas lié `main.py` et `ui.py` entre eux de cette manière :
```python
main.py :
class UnoGame:
    def __init__(self, game_screen):
        self.game_screen = game_screen

ui.py :
def on_enter(self):
    self.game = UnoGame(self)
```
Avec cette méthode je peux accéder aux attributs de `UnoGame` depuis `ui.py` sans problème alors que avant ça ne marchait pas je ne sais toujours pas vraiment pourquoi, mais j'ai trouvé cette solution sur un forum et heureusement car ça m'a beaucoup aidé.

Voilà c'est les plus gros problémes que j'ai rencontré en codant **Ichi**, et malgrès ceux-ci je trouve que le jeu est réussi et j'en suis fier.

---
**By DAMOUR ROUGEMONT Maxime**