from carte import Carte
from random import shuffle

class JeuDeCartes:
    def __init__(self):
        self.PaquetDeCarte = self.creer_paquet()

    def creer_paquet(self):
        couleurs = ['Rouge', 'Bleu', 'Vert', 'Jaune']
        paquet = []

        #Ajoute les cartes de 0 à 9 pour chaque couleur
        for couleur in couleurs:
            paquet.append(Carte(0, couleur))  #Ajoute une seule carte 0
            for valeur in range(1, 10):
                #Ajoute les cartes de 1 à 9 deux fois
                for i in range(2):
                    paquet.append(Carte(valeur, couleur))

            #Ajoute les cartes spéciales (deux de chaque par couleur)
            for i in range(2):
                paquet.append(Carte('+2', couleur))
                paquet.append(Carte('Changement de sens', couleur))
                paquet.append(Carte('Passer', couleur))

        #Ajoute les cartes Joker et Joker +4
        for i in range(4):
            paquet.append(Carte('Joker', ''))      #4 cartes Joker
            paquet.append(Carte('Joker +4', ''))   #4 cartes Joker +4

        return paquet

    def get_nb_cartes(self):
        return len(self.PaquetDeCarte)

    def get_paquet(self):
        return [str(carte) for carte in self.PaquetDeCarte]

    def melanger_paquet(self):
        shuffle(self.PaquetDeCarte)

    def piocher(self):
        if self.PaquetDeCarte:  
            return self.PaquetDeCarte.pop()  #Tire la carte du haut du paquet
        else:
            return None  #Aucune carte à piocher

jeu1 = JeuDeCartes()
jeu1.melanger_paquet()
print(jeu1.piocher())