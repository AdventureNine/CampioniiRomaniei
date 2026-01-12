import os
import sys

# --- CONFIGURARE ---
from kivy.config import Config

from frontend.screens.games.map_guess import MapGuessScreen

Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', False)
Config.write()

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty, ObjectProperty

sys.path.append(os.path.join(os.path.dirname(__file__), 'frontend'))

from frontend.components.cloud_transition import CloudTransitionLayout
from frontend.components.polygon_button import PolygonButton

from frontend.screens.menu.menu import MenuScreen
from frontend.screens.map.map import MapScreen
from frontend.screens.region_dashboard.region_dashboard import RegionDashboardScreen
from frontend.screens.generic.quiz_screen import GenericQuizScreen
from frontend.screens.generic.fill_screen import GenericFillScreen
from frontend.screens.games.puzzle import PuzzleGameScreen
from frontend.screens.games.rebus import RebusScreen
from frontend.screens.games.bingo import BingoScreen
from frontend.screens.cosmetics.cosmetics import CosmeticsScreen

import sqlite3
from backend.repository.PlayerRepository import PlayerRepository
from backend.domain.entities.Player import Player

from kivy.factory import Factory

class DidacticApp(App):
    score = NumericProperty(0)
    timer_text = StringProperty("")
    player = ObjectProperty(None)

    def build(self):
        Window.size = (1280, 800)
        self.title = "Campionii Geografiei"

        Factory.register('PolygonButton', cls=PolygonButton)

        self.conn = sqlite3.connect('../backend/domain/data.db')

        self.player_repo = PlayerRepository(self.conn)

        loaded_player = self.player_repo.get()
        if loaded_player:
            self.player = loaded_player
            self.score = self.player.get_credits()
        else:
            self.player = Player(1, "Explorator")
            self.player_repo.save(self.player)

        # 1. Încărcare Componente Grafice
        Builder.load_file('components/common.kv')
        Builder.load_file('components/cloud_transition.kv')
        Builder.load_file('screens/menu/menu.kv')
        Builder.load_file('screens/map/map.kv')
        Builder.load_file('screens/region_dashboard/region_dashboard.kv')
        Builder.load_file('screens/generic/quiz_screen.kv')
        Builder.load_file('screens/generic/fill_screen.kv')
        Builder.load_file('screens/games/map_guess.kv')
        Builder.load_file('screens/games/puzzle.kv')
        Builder.load_file('screens/games/rebus.kv')
        Builder.load_file('screens/games/bingo.kv')
        Builder.load_file('screens/cosmetics/cosmetics.kv')

        # 2. Layout Principal
        self.root_layout = FloatLayout()

        # 3. Screen Manager
        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(MapScreen(name='map'))
        self.sm.add_widget(RegionDashboardScreen(name='region_dashboard'))
        self.sm.add_widget(GenericQuizScreen(name='generic_quiz'))
        self.sm.add_widget(GenericFillScreen(name='generic_fill'))
        self.sm.add_widget(PuzzleGameScreen(name='puzzle'))
        self.sm.add_widget(MapGuessScreen(name='map_guess'))
        self.sm.add_widget(RebusScreen(name='rebus'))
        self.sm.add_widget(BingoScreen(name='bingo'))
        self.sm.add_widget(CosmeticsScreen(name='cosmetics'))

        # 4. Strat Nori
        self.clouds = CloudTransitionLayout()

        self.root_layout.add_widget(self.sm)
        self.root_layout.add_widget(self.clouds)

        return self.root_layout

if __name__ == '__main__':
    DidacticApp().run()