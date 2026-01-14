import random
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.app import App

from backend.domain.utils.Difficulty import Difficulty
from backend.domain.entities.Minigame import Bingo

class BingoCell(Button):
    is_target = BooleanProperty(False)
    is_selected = BooleanProperty(False)

    def on_release(self):
        self.is_selected = not self.is_selected
        self.update_color()

    def update_color(self):
        if not self.is_selected:
            self.background_color = (1, 1, 1, 1)
        else:
            self.background_color = (0.2, 0.6, 1, 1)

class BingoScreen(Screen):
    game_container = ObjectProperty(None)
    is_completed = BooleanProperty(False)
    is_wrong = BooleanProperty(False)
    bg_image = StringProperty('')
    current_difficulty = ObjectProperty(None, allownone=True)
    minigame_id = ObjectProperty(None)

    def __init__(self, **kwargs):
        if 'current_difficulty' not in kwargs:
            difficulty_levels = list(Difficulty)
            self.current_difficulty = difficulty_levels[1]
        super().__init__(**kwargs)
        self.cells = []

    def generate_bingo(self, *args):
        if not self.game_container:
            return

        if not hasattr(self, 'bingo_entity') or not self.bingo_entity:
            from kivy.uix.label import Label
            self.game_container.clear_widgets()
            self.game_container.add_widget(Label(text="Eroare: Nu există date de bingo!", color=(1, 1, 1, 1)))
            return

        self.game_container.clear_widgets()
        self.cells = []
        self.is_completed = False
        self.is_wrong = False

        difficulty_levels = list(Difficulty)
        if self.current_difficulty == difficulty_levels[0]:  # Easy
            num_true, num_false = 18, 7
        elif self.current_difficulty == difficulty_levels[1]:  # Medium
            num_true, num_false = 13, 12
        else:  # Hard
            num_true, num_false = 8, 17

        db_items = self.bingo_entity.get_win_configuration()
        if not db_items:
            from kivy.uix.label import Label
            self.game_container.add_widget(Label(text="Eroare: Configurație lipsă!", color=(1, 1, 1, 1)))
            return
        all_true = [(text, True) for text, val in db_items.items() if val is True]
        all_false = [(text, False) for text, val in db_items.items() if val is False]

        if not all_true and not all_false:
            from kivy.uix.label import Label
            self.game_container.add_widget(Label(text="Eroare: Nu există celule de bingo!", color=(1, 1, 1, 1)))
            return

        sample = random.sample(all_true, min(len(all_true), num_true)) + \
                 random.sample(all_false, min(len(all_false), num_false))
        random.shuffle(sample)

        current_win_cfg = {item[0]: item[1] for item in sample}
        self.bingo_entity.set_win_configuration(current_win_cfg)

        grid = GridLayout(cols=5, spacing=10, size_hint=(None, None))
        grid.bind(minimum_height=grid.setter('height'), minimum_width=grid.setter('width'))
        grid.width = 580

        for text, is_target in sample:
            cell = BingoCell(text=text, is_target=is_target)
            self.bind(is_wrong=cell.setter('disabled'))
            self.cells.append(cell)
            grid.add_widget(cell)

        self.game_container.add_widget(grid)

    def check_solution(self):
        current_cfg = {cell.text: cell.is_selected for cell in self.cells}
        self.bingo_entity.set_current_configuration(current_cfg)

        correct = True
        for cell in self.cells:
            if cell.is_target:
                if not cell.is_selected:
                    cell.background_color = (1, 0.3, 0.3, 1)
                    correct = False
                else:
                    cell.background_color = (0.3, 0.9, 0.3, 1)
            else:
                if cell.is_selected:
                    cell.background_color = (1, 0.3, 0.3, 1)
                    correct = False

        self.is_completed = correct
        self.is_wrong = not correct

    def clear_bingo(self):
        if self.is_wrong:
            return
        for cell in self.cells:
            cell.is_selected = False
            cell.background_color = (1, 1, 1, 1)
        self.is_completed = False

    def go_next(self):
        app = App.get_running_app()
        dashboard = app.sm.get_screen('region_dashboard')
        dashboard.load_next_step()

    def go_back(self):
        app = App.get_running_app()
        app.clouds.change_screen('region_dashboard')

    def load_data(self, data, step_number):
        """
        Încarcă datele pentru minigame-ul Bingo.
        Format așteptat:
        {
            'type': 'bingo',
            'bingo': Entitate Bingo cu win_configuration
        }
        """
        # Resetează UI
        if self.game_container:
            self.game_container.clear_widgets()
        self.is_completed = False
        self.is_wrong = False
        self.cells = []

        # Obține entitatea Bingo din date
        bingo = data.get('bingo')
        if not bingo or not isinstance(bingo, Bingo):
            from kivy.uix.label import Label
            if self.game_container:
                self.game_container.add_widget(
                    Label(text="Eroare: Nu s-au găsit date de bingo.", color=(1, 1, 1, 1)))
            return
        self.bingo_entity = bingo
        self.minigame_id = getattr(bingo, 'id', data.get('minigame_id', None))
        if 'difficulty' in data:
            self.current_difficulty = data['difficulty']
        # Generează grila de bingo
        self.generate_bingo()
