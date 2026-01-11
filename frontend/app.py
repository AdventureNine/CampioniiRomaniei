from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('graphics', 'resizable', '0')

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

from screens.bingo.bingo import BingoScreen

Window.size = (1280, 800)

class DidacticApp(App):
    def build(self):
        Builder.load_file('screens/bingo/bingo.kv')

        self.root_layout = FloatLayout()

        self.sm_bingo = BingoScreen()

        self.root_layout.add_widget(self.sm_bingo)

        def _eat_right_click(window, x, y, button, modifiers):
            return True if button == 3 else False

        Window.bind(on_mouse_down=_eat_right_click)

        return self.root_layout

if __name__ == '__main__':
    DidacticApp().run()