from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

from screens.rebus.rebus import RebusScreen

Window.size = (1280, 800)

class DidacticApp(App):
    def build(self):
        Builder.load_file('screens/rebus/rebus.kv')

        self.root_layout = FloatLayout()

        self.sm_rebus = RebusScreen()

        self.root_layout.add_widget(self.sm_rebus)

        return self.root_layout


if __name__ == '__main__':
    DidacticApp().run()