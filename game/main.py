from paquet import *
from ui import *
from kivy.clock import Clock

class UnoGame:
    def __init__(self):
        self.jeu = JeuDeCartes()
        self.jeu.melanger_paquet()
        self.joueurs = []
        self.pioche = self.jeu.PaquetDeCarte
        self.talon = [self.piocher_carte()]
        self.tour = 0
        self.sens = 1  # 1 pour sens horaire, -1 pour anti-horaire
        self.joueur_actuel = 0

    def ajouter_joueur(self, nom):
        # Chaque joueur reçoit 7 cartes
        main_joueur = [self.piocher_carte() for _ in range(7)]
        self.joueurs.append({'nom': nom, 'main': main_joueur})

    def piocher_carte(self):
        return self.pioche.pop() if self.pioche else None

    def jouer_carte(self, carte):
        self.talon.append(carte)

    def carte_valide(self, carte, carte_actuelle):
        # Vérifie si la carte jouée est valide
        return (carte.couleur == carte_actuelle.couleur or
                carte.valeur == carte_actuelle.valeur or
                carte.couleur == '' or  # Joker
                carte.valeur == 'Joker +4')

    def appliquer_effet(self, carte):
        if carte.valeur == '+2':
            joueur_suivant = (self.joueur_actuel + self.sens) % len(self.joueurs)
            self.joueurs[joueur_suivant]['main'].extend([self.piocher_carte() for _ in range(2)])
        elif carte.valeur == 'Changement de sens':
            self.sens *= -1
        elif carte.valeur == 'Passer':
            self.joueur_actuel = (self.joueur_actuel + self.sens) % len(self.joueurs)
        elif carte.valeur == 'Joker +4':
            joueur_suivant = (self.joueur_actuel + self.sens) % len(self.joueurs)
            self.joueurs[joueur_suivant]['main'].extend([self.piocher_carte() for _ in range(4)])
            carte.couleur = 'Rouge'  # Demander la couleur au joueur

    def jouer_tour(self):
        # Logique de déroulement d'un tour de jeu
        carte_actuelle = self.talon[-1]
        main_joueur = self.joueurs[self.joueur_actuel]['main']
        carte_jouee = None

        for carte in main_joueur:
            if self.carte_valide(carte, carte_actuelle):
                carte_jouee = carte
                break

        if carte_jouee:
            main_joueur.remove(carte_jouee)
            self.jouer_carte(carte_jouee)
            self.appliquer_effet(carte_jouee)
        else:
            main_joueur.append(self.piocher_carte())

        # Passe au joueur suivant
        self.joueur_actuel = (self.joueur_actuel + self.sens) % len(self.joueurs)

    def verifier_victoire(self):
        for joueur in self.joueurs:
            if len(joueur['main']) == 0:
                return joueur['nom']
        return None

# Initialisation et exécution du jeu dans l'interface
if __name__ == "__main__":
    Ichi().run()
