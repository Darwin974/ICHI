from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

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
            return Builder.load_file("ichi.kv")

if __name__ == '__main__':
    Ichi().run()