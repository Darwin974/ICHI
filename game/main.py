from paquet import *
from ui import *
from kivy.clock import Clock
import random

class UnoGame:
    def __init__(self, game_screen):
        self.game_screen = game_screen
        self.jeu = JeuDeCartes()
        self.jeu.melanger_paquet()
        self.joueur = {'nom': 'Joueur', 'main': [self.piocher_carte() for i in range(7)]}
        self.ia = {'nom': 'IA', 'main': [self.piocher_carte() for i in range(7)]}
        self.pioche = self.jeu.PaquetDeCarte
        self.talon = [self.piocher_carte()]
        self.tour_joueur = True  #True pour le joueur, False pour l'IA

    def piocher_carte(self):
        return self.jeu.piocher()

    def jouer_carte(self, carte):
        self.talon.append(carte)

    def carte_valide(self, carte, carte_actuelle):
        return (carte.couleur == carte_actuelle.couleur or
                carte.valeur == carte_actuelle.valeur or
                carte.valeur in ['Joker +4', 'Joker'])

    def appliquer_effet(self, carte):
        if carte.valeur == '+2':
            cible = self.ia if self.tour_joueur else self.joueur
            cible['main'].extend([self.piocher_carte() for _ in range(2)])
        elif carte.valeur == 'Joker +4':
            cible = self.ia if self.tour_joueur else self.joueur
            cible['main'].extend([self.piocher_carte() for _ in range(4)])
        elif carte.valeur == 'Passer':
            self.tour_joueur = not self.tour_joueur 

    def tour_ia(self):
        """Logique du tour de l'IA."""
        print(f"Avant le tour - Joueur: {len(self.joueur['main'])} cartes, IA: {len(self.ia['main'])} cartes")
        main_ia = self.ia['main']
        carte_actuelle = self.talon[-1]

        #Trouve une carte valide pour jouer
        carte_a_jouer = None
        for carte in main_ia:
            if self.carte_valide(carte, carte_actuelle):
                carte_a_jouer = carte
                break

        if carte_a_jouer:
            main_ia.remove(carte_a_jouer)
            self.talon.append(carte_a_jouer)

            #Si c'est un Joker, Joker +4, choisir une couleur
            if carte_a_jouer.valeur in ['Joker', 'Joker +4']:
                couleur_choisie = self.choisir_couleur_ia()
                carte_a_jouer._couleur = couleur_choisie
                print(f"L'IA a choisi la couleur {couleur_choisie}.")


            self.appliquer_effet(carte_a_jouer)

        else:
            #L'IA pioche une carte si elle ne peut pas jouer
            carte_piochee = self.piocher_carte()
            main_ia.append(carte_piochee)
            print("L'IA pioche une carte.")

        self.tour_joueur = True
        self.game_screen.prochain_tour()
        print(f"Après le tour - Joueur: {len(self.joueur['main'])} cartes, IA: {len(self.ia['main'])} cartes")


    def choisir_couleur_ia(self):
        """Choisir une couleur basée sur les cartes de l'IA."""
        couleurs_possibles = ['Rouge', 'Bleu', 'Vert', 'Jaune']
        couleurs_presentes = [carte.couleur for carte in self.ia['main'] if carte.couleur in couleurs_possibles]

        if couleurs_presentes:
            #Prend la couleur la plus frequente dans la main de l'IA
            return max(set(couleurs_presentes), key=couleurs_presentes.count)
        else:
            #Choisi une couleur aleatoire si aucune n'est presente
            return random.choice(couleurs_possibles)


    def verifier_victoire(self):
        if not self.jeu.PaquetDeCarte:  #Verifie si la pioche est vide
            return "Il n'y a plus de carte..."
        elif not self.joueur['main']:
            return "Vous avez"
        elif not self.ia['main']:
            return "L'IA a"
        return None

#Lancement du jeu
if __name__ == '__main__':
    Ichi().run()
