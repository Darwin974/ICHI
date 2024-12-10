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
Le fichier [carte.py](https://github.com/Darwin974/ICHI/blob/main/game/carte.py) définit la classe **```Carte```**, qui représente chaque carte individuelle dans le jeu. 
#### Cette classe inclut les attributs suivants :
```valeur``` : représente la valeur de la carte, comme un chiffre **(0 à 9)** ou une action spéciale **('+2', 'Inversion', etc)**.
\
```couleur :``` représente la couleur de la carte, **'Rouge', 'Bleu', 'Vert', ou 'Jaune'**. Les Jokers n'ont pas de couleur de base.
\
```image``` : contient le chemin vers l'image associée à la carte.

#### Les méthodes principales de cette classe sont :
```__str__``` : retourne une chaîne de caractères représentant la carte sous la forme **"valeur couleur"**, utile pour le débogage ou l'affichage.
\
Des getters pour accéder aux attributs **valeur** et **couleur** de manière sécurisée.

Cette classe sert de structure de base pour toutes les cartes qui seront générées et manipulées dans le jeu.

---

### [paquet.py](https://github.com/Darwin974/ICHI/blob/main/game/paquet.py) :
Le fichier **[paquet.py](https://github.com/Darwin974/ICHI/blob/main/game/paquet.py)** contient la classe ```JeuDeCartes```, qui gère l'ensemble des cartes du jeu.
#### Attributs principaux :
**```PaquetDeCarte```** : un tableau contenant toutes les cartes du jeu, générées grâce à la méthode ```creer_paquet()```.

#### Méthodes :
**```creer_paquet()```** : Génère un paquet de **108 cartes**, comme dans le jeu UNO. Ajoute les cartes numériques **(0 à 9)**, les cartes spéciales ('+2', 'Inversion', 'Passer') pour chaque couleur, et les Jokers.
Attribue un chemin d'image spécifique à chaque carte (Ex: ```img/Cartes/R/_0.png``` pour une carte rouge '0').
Retourne un tableau contenant toutes les cartes sous forme d’objets Carte.
\
```melanger_paquet()``` : mélange les cartes du paquet à l'aide de shuffle de la bibliothèque random.
\
```piocher()``` : retire et retourne la dernière carte du paquet, ou None si le paquet est vide.
\
```get_nb_cartes()``` : retourne le nombre total de cartes dans le paquet.
\
```get_paquet()``` : retourne une liste des cartes sous forme de chaînes de caractères (via leur méthode ```__str__```).

Cette classe permet donc de gérer toutes les opérations liées au paquet de cartes du jeu : **création, mélange, et gestion des tirages pendant la partie**.

---

### [main.py](https://github.com/Darwin974/ICHI/blob/main/game/main.py) :

---

### [ui.py](https://github.com/Darwin974/ICHI/blob/main/game/ui.py) :

---

### [Ichi.kv](https://github.com/Darwin974/ICHI/blob/main/game/Ichi.kv) :

## Les difficultés rencontrés

---
**By DAMOUR ROUGEMONT Maxime**