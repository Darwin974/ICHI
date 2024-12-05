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

### [carte.py](https://github.com/Darwin974/ICHI/blob/main/game/carte.py) :
Le fichier **carte.py** permet uniquement d'héberger la class **Carte**, avec ses attributs d'objets et ses méthodes qui vont être utilisés par la suite dans **[paquet.py](https://github.com/Darwin974/ICHI/blob/main/game/paquet.py)** pour créer les cartes du jeu.

### [paquet.py](https://github.com/Darwin974/ICHI/blob/main/game/paquet.py) :
Le fichier **paquet.py** va héberger la class **JeuDeCartes**, cette class a comme unique attribut **```PaquetDeCarte```**. Comme son nom l'indique, c'est le Paquet de carte du jeu, il contient toutes les cartes du jeu (108 cartes comme au **[UNO](https://www.jeuxuno.com/regles-officielles)**). Pour le générer, on utilise la méthode **```creer_paquet()```**, cette méthode va créer le nombre de cartes nécessaires pour le jeu en respectant le nombres de cartes pour chaque couleurs et fait de même pour les cartes spéciales. Chaque carte sera stocké dans le tableau **```paquet```**, sous la forme d'objet de la class **Carte** qu'on importe du fichier **[carte.py](https://github.com/Darwin974/ICHI/blob/main/game/carte.py)**. Ce tableau sera à la fin de sa création notre **paquet de carte** fini. **```creer_paquet()```** renvoie **```paquet```** à la fin de son éxécution. La class **JeuDeCartes** contient aussi les méthodes : **```melanger_paquet()```** qui permet de mélanger les cartes de **```PaquetDeCarte```** aléatoirement grâce à la fonction **```shuffle```** de la bibliothéque random, et la méthode **```piocher()```** va elle retourner la dernière carte de **```PaquetDeCarte```** grâce à la fonction **```.pop```**. La class **JeuDeCartes** contient aussi les getters **```get_nb_cartes()```** qui retourne le nombres de cartes de **```PaquetDeCartes```**, et **```get_paquet()```** qui retourne chaque carte du paquet.

### [main.py](https://github.com/Darwin974/ICHI/blob/main/game/main.py) :

### [ui.py](https://github.com/Darwin974/ICHI/blob/main/game/ui.py) :

### [Ichi.kv](https://github.com/Darwin974/ICHI/blob/main/game/Ichi.kv) :


## Les difficultés rencontrés

**By DAMOUR ROUGEMONT Maxime**