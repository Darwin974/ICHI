from kivy.app import App
from kivy.uix.widget import Widget

class start(Widget):
    pass

class Ichi(App):
    def build(self):
            return start()

if __name__ == '__main__':
    Ichi().run()