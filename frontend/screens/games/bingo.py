import random
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.clock import Clock
from kivy.app import App

from backend.domain.utils.Difficulty import Difficulty
from backend.domain.entities.Minigame import Bingo

BINGO_DATA_SOURCE = {
    # --- ISTORIE ROMÂNIA (TRUE) ---
    'ISTORIE': [
    ('Decebal', True), ('Traian', True), ('Burebista', True), ('Mircea cel Bătrân', True),
    ('Ștefan cel Mare', True), ('Mihai Viteazul', True), ('Alexandru Ioan Cuza', True),
    ('Carol I', True), ('Ferdinand I', True), ('Regina Maria', True), ('Vlad Țepeș', True),
    ('Basarab I', True), ('Marea Unire', True), ('Independența României', True),
    ('1 Decembrie', True), ('Alba Iulia', True), ('Sarmizegetusa Regia', True),
    ('Matei Corvin', True), ('Nicolae Bălcescu', True), ('Avram Iancu', True),
    ('Tudor Vladimirescu', True), ('Nicolae Iorga', True), ('Bătălia de la Posada', True),
    ('Bătălia de la Rovine', True), ('Podul lui Traian', True), ('Curtea de Argeș', True),
    ('Regele Mihai I', True), ('Regina Elisabeta', True), ('Transilvania', True),
    ('Moldova', True), ('Muntenia', True), ('Basarabia', True), ('Dobrogea', True),
    ('Crișana', True), ('Banat', True)],

    # --- GEOGRAFIE ROMÂNIA (TRUE) ---
    'GEOGRAFIE': [('Dunărea', True), ('Marea Neagră', True), ('Munții Carpați', True), ('Vârful Moldoveanu', True),
    ('Delta Dunării', True), ('Râul Prut', True), ('Râul Siret', True), ('Râul Mureș', True),
    ('Râul Olt', True), ('Râul Ialomița', True), ('Râul Someș', True), ('Lacul Sfânta Ana', True),
    ('Lacul Roșu', True), ('Transfăgărășan', True), ('Transalpina', True), ('Sfinxul', True),
    ('Babele', True), ('Peștera Scărișoara', True), ('Porțile de Fier', True), ('Câmpia Română', True),
    ('Podișul Moldovei', True), ('Dealurile de Vest', True), ('București', True), ('Iași', True),
    ('Cluj-Napoca', True), ('Timișoara', True), ('Constanța', True), ('Brașov', True),
    ('Craiova', True), ('Galați', True), ('Munții Apuseni', True), ('Munții Bucegi', True),
    ('Munții Parâng', True), ('Munții Retezat', True), ('Munții Rodnei', True)],

    # --- DISTRAGERI / ELEMENTE STRĂINE (FALSE) ---
    'FALS': [('Paris', False), ('Londra', False), ('Berlin', False), ('Viena', False),
    ('Roma', False), ('Madrid', False), ('Lisabona', False), ('Amsterdam', False),
    ('Praga', False), ('Varșovia', False), ('Munții Alpi', False), ('Munții Pirinei', False),
    ('Munții Anzi', False), ('Munții Himalaya', False), ('Fluviul Nil', False),
    ('Fluviul Amazon', False), ('Fluviul Mississippi', False), ('Fluviul Volga', False),
    ('Napoleon Bonaparte', False), ('Iulius Cezar', False), ('Abraham Lincoln', False),
    ('Cristofor Columb', False), ('Leonardo da Vinci', False), ('Isaac Newton', False),
    ('Albert Einstein', False), ('W.A. Mozart', False), ('Ludwig van Beethoven', False),
    ('William Shakespeare', False), ('Pablo Picasso', False), ('Planeta Marte', False),
    ('Planeta Jupiter', False), ('Marele Zid Chinezesc', False), ('Statuia Libertății', False),
    ('Turnul Eiffel', False), ('Piramidele din Giza', False), ('Cascada Niagara', False),
    ('Marele Canion', False), ('Deșertul Sahara', False), ('Australia', False),
    ('Brazilia', False), ('Canada', False), ('Japonia', False), ('Oceanul Pacific', False),
    ('Oceanul Atlantic', False), ('Muntele Kilimanjaro', False)]
}

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

    def __init__(self, **kwargs):
        if 'current_difficulty' not in kwargs:
            difficulty_levels = list(Difficulty)
            self.current_difficulty = difficulty_levels[1]
        super().__init__(**kwargs)
        self.cells = []
        Clock.schedule_once(self.generate_bingo, 0.1)

    def generate_bingo(self, *args):
        if not self.game_container:
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

        all_true = []
        all_false = []
        for cat in BINGO_DATA_SOURCE.values():
            all_true.extend([item for item in cat if item[1] is True])
            all_false.extend([item for item in cat if item[1] is False])

        sample = random.sample(all_true, min(len(all_true), num_true)) + \
                 random.sample(all_false, min(len(all_false), num_false))
        random.shuffle(sample)

        win_cfg = {item[0]: item[1] for item in sample}
        self.bingo_entity = Bingo(bingo_id=2, win_configuration=win_cfg, theme= "dummy") # TODO backend connection

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
