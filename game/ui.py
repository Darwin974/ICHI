from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from main import UnoGame

class GameScreen(Screen):
    def on_enter(self):
        self.game = UnoGame(self)
        self.afficher_main()
        self.afficher_carte_talon()
        self._ia_en_cours = False
        self.afficher_cartes_ia()

    def afficher_main(self):
        self.ids['main_joueur'].clear_widgets()
        for carte in self.game.joueur['main']:
            btn = Button(text=str(carte), size_hint=(None, None), size=(50, 70))
            btn.bind(on_release=lambda instance, c=carte: self.jouer_carte(c))
            self.ids['main_joueur'].add_widget(btn)

    def afficher_cartes_ia(self):
        self.ids['nb_cartes_ia'].text = "IA : " + str(len(self.game.ia['main'])) + " cartes restantes"

    def jouer_carte(self, carte):
        if self.game.carte_valide(carte, self.game.talon[-1]):
            self.game.joueur['main'].remove(carte)
            self.game.jouer_carte(carte)

            if carte.valeur in ['Joker', 'Joker +4']:
                #Afficher la fenetre pour choisir une couleur
                self.choisir_couleur(lambda couleur: self.appliquer_couleur(carte, couleur))
            else:
                self.appliquer_effet_et_tour(carte)
        else:
            self.ids['message'].text = "Carte non valide !"

    def appliquer_couleur(self, carte, couleur):
        """Applique la couleur choisie au Joker ou Joker +4."""
        carte._couleur = couleur
        self.appliquer_effet_et_tour(carte)

    def appliquer_effet_et_tour(self, carte):
        """Appliquer l'effet de la carte et passer au tour suivant."""
        self.game.appliquer_effet(carte)

        #Verifie si victoire apres coup
        gagnant = self.game.verifier_victoire()
        if gagnant:
            self.ids['message'].text = f"{gagnant} gagné !"
            return
        
        #Alterne le tour
        self.game.tour_joueur = not self.game.tour_joueur
        self.prochain_tour()

    def afficher_carte_talon(self):
        self.ids['talon'].text = str(self.game.talon[-1])

    def prochain_tour(self):
        print("Passage au tour suivant")
        self.afficher_cartes_ia()

        if self.game.tour_joueur:
            self.afficher_main()
            self.afficher_carte_talon()
            self.ids['message'].text = "Votre tour !"
        else:
            #Verifiez que l'IA ne joue pas
            if not hasattr(self, '_ia_en_cours') or not self._ia_en_cours:
                self._ia_en_cours = True  #Bloque d'autres appels
                self.ids['message'].text = "Tour de l'IA..."
                Clock.schedule_once(lambda dt: self.jouer_tour_ia(), 1)

    def jouer_tour_ia(self):
        self.game.tour_ia()
        self._ia_en_cours = False
        self.prochain_tour()

    def passer_tour(self):
        print("Passage au tour suivant demandé")
        #Le joueur pioche une carte
        self.game.joueur['main'].append(self.game.piocher_carte())
        self.afficher_main()
        #Forcer le passage a l'IA
        self.game.tour_joueur = False
        self.prochain_tour()

    def choisir_couleur(self, callback):
        """Afficher une boîte de dialogue pour choisir une couleur."""
        couleurs = ['Rouge', 'Bleu', 'Vert', 'Jaune']

        layout = GridLayout(cols=4, spacing=10, padding=10)
        popup = Popup(title="Choisissez une couleur", size_hint=(0.6, 0.4))

        def choisir_couleur_callback(instance):
            couleur = instance.text
            popup.dismiss()
            callback(couleur)  #Appelle la fonction une fois la couleur choisie

        for couleur in couleurs:
            btn = Button(text=couleur, background_color=self.get_color_rgba(couleur))
            btn.bind(on_release=choisir_couleur_callback)
            layout.add_widget(btn)

        popup.content = layout
        popup.open()

    def get_color_rgba(self, couleur):
        """Retourne les valeurs RGBA associées aux couleurs."""
        return {
            'Rouge': (1, 0, 0, 1),
            'Bleu': (0, 0, 1, 1),
            'Vert': (0, 1, 0, 1),
            'Jaune': (1, 1, 0, 1)
        }.get(couleur, (1, 1, 1, 1))  #base : blanc

class HomeScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class GameSelect(Screen):
    pass

class GameScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

class Ichi(App):
        def build(self):
            return Builder.load_file("Ichi.kv")

if __name__ == '__main__':
    Ichi().run()