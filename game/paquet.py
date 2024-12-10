from carte import Carte
from random import shuffle

class JeuDeCartes:
    def __init__(self):
        self.PaquetDeCarte = self.creer_paquet()

    def creer_paquet(self):
        couleurs = ['Rouge', 'Bleu', 'Vert', 'Jaune']
        couleur_codes = {'Rouge': 'R', 'Bleu': 'B', 'Vert': 'V', 'Jaune': 'J'}
        paquet = []

        #Ajoute les cartes de 0 a 9 pour chaque couleur
        for couleur in couleurs:
            code_couleur = couleur_codes[couleur]
            
            #Ajoute une carte 0
            paquet.append(Carte(0, couleur, f"img/Cartes/{code_couleur}/_0.png"))
            
            #Ajoute les cartes de 1 a 9 deux fois
            for valeur in range(1, 10):
                for i in range(2): 
                    paquet.append(Carte(valeur, couleur, f"img/Cartes/{code_couleur}/_{valeur}.png"))
            
            #Ajoute les cartes speciales
            for i in range(2):
                paquet.append(Carte('+2', couleur, f"img/Cartes/{code_couleur}/+2.png"))
                paquet.append(Carte('Inversion', couleur, f"img/Cartes/{code_couleur}/Inversion.png"))
                paquet.append(Carte('Passer', couleur, f"img/Cartes/{code_couleur}/Passer.png"))

        #Ajoute Joker et Joker +4
        for i in range(4):
            #Joker avec couleur "N" (None)
            paquet.append(Carte('Joker', '', f"img/Cartes/Specials/Joker.png"))
            paquet.append(Carte('Joker +4', '', f"img/Cartes/Specials/Joker+4.png"))

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
            return None  #Aucune carte a piocher