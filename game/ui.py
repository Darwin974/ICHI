from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from main import UnoGame

class GameScreen(Screen):
    def on_enter(self):
        self.game = UnoGame()
        self.game.ajouter_joueur("Joueur 1")
        self.game.ajouter_joueur("Joueur 2")
        # Affiche les cartes initiales et la carte du talon

    def afficher_main(self):
        self.ids['main_joueur'].clear_widgets()
        for carte in self.game.joueurs[self.game.joueur_actuel]['main']:
            btn = Button(text=str(carte), size_hint=(None, None), size=(50, 70))
            self.ids['main_joueur'].add_widget(btn)

    def afficher_carte_talon(self):
        self.ids['talon'].text = str(self.game.talon[-1])
        
    def prochain_tour(self):
        gagnant = self.game.verifier_victoire()
        if gagnant:
            self.ids['message'].text = f"{gagnant} a gagne!"
        else:
            self.game.jouer_tour()
            self.afficher_main()
            self.afficher_carte_talon()

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