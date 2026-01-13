import os, sys, sqlite3
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.config import Config
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, StringProperty, ObjectProperty

from backend.domain.entities.Player import Player
from backend.repository.PlayerRepository import PlayerRepository
from backend.repository.QuizzTaskRepository import QuizzTaskRepository
from backend.repository.QuestionRepository import QuestionRepository
from backend.repository.FillInStatementRepository import FillInStatementRepository
from backend.repository.MinigameRepository import MinigameRepository

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
from frontend.screens.games.map_guess import MapGuessScreen
from frontend.screens.games.pairs import PairsGameScreen
from frontend.screens.statistics.statistics import PaginaStatistici

Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', False)
Config.write()
sys.path.append(os.path.join(os.path.dirname(__file__), 'frontend'))

class DidacticApp(MDApp):
    timer_text = StringProperty("")
    player = ObjectProperty(None)
    score = NumericProperty(0)
    conn, sm, clouds = None, None, None

    def on_stop(self): self.conn.close()

    def build(self):
        self.title = "Campionii Geografiei"
        self.conn = sqlite3.connect('../backend/domain/data.db')
        Window.size = (1280, 800)
        Factory.register('PolygonButton', cls=PolygonButton)
        root_layout = FloatLayout()

        #repositories
        player_repo = PlayerRepository(self.conn)
        quizz_task_repo = QuizzTaskRepository(self.conn)
        question_repo = QuestionRepository(self.conn)
        fill_in_repo = FillInStatementRepository(self.conn)
        minigame_repo = MinigameRepository(self.conn)

        #TODO: service

        loaded_player = player_repo.get()
        if loaded_player:
            self.player = loaded_player
            self.score = self.player.get_credits()
        else:
            self.player = Player(1, "Explorator")
            player_repo.save(self.player) #TODO service

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
        Builder.load_file('screens/games/pairs.kv')
        Builder.load_file('screens/statistics/statistics.kv')
        Builder.load_file('screens/cosmetics/cosmetics.kv')

        # Screen Manager
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
        self.sm.add_widget(PairsGameScreen(name='pairs_game'))
        self.sm.add_widget(PaginaStatistici(name='statistics'))
        self.sm.add_widget(CosmeticsScreen(name='cosmetics'))

        self.clouds = CloudTransitionLayout()
        root_layout.add_widget(self.sm)
        root_layout.add_widget(self.clouds) # strat nori

        return root_layout

if __name__ == '__main__': DidacticApp().run()