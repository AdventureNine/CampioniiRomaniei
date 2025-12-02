from kivy.config import Config

Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', False)

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, FadeTransition


from screens.dashboard import MeniuPrincipal
from screens.game import EcranJoc


class CampioniiRomanieiApp(MDApp):
    def build(self):
        self.title = "Campionii României"
        self.theme_cls.theme_style = "Dark"

        Builder.load_file('kv/dashboard.kv')
        Builder.load_file('kv/game.kv')

        sm = ScreenManager(transition=FadeTransition())

        sm.add_widget(MeniuPrincipal(name='meniu'))
        sm.add_widget(EcranJoc(name='joc'))

        return sm


if __name__ == '__main__':
    CampioniiRomanieiApp().run()