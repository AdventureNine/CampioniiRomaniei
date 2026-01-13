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
    'ISTORIE': [
        # --- ROMÂNIA (TRUE) - 30 intrări ---
        ('Decebal', True), ('Traian', True), ('Burebista', True), ('Mircea cel Bătrân', True),
        ('Ștefan cel Mare', True), ('Mihai Viteazul', True), ('Al. Ioan Cuza', True), ('Carol I', True),
        ('Ferdinand I', True), ('Regina Maria', True), ('Vlad Țepeș', True), ('Basarab I', True),
        ('Iancu de Hunedoara', True), ('Constantin Brâncoveanu', True), ('Neagoe Basarab', True),
        ('Nicolae Bălcescu', True), ('Avram Iancu', True), ('Tudor Vladimirescu', True),
        ('Ecaterina Teodoroiu', True), ('Marea Unire', True), ('Independența', True),
        ('Revoluția 1848', True), ('Bătălia de la Rovine', True), ('Bătălia de la Podul Înalt', True),
        ('Bătălia de la Călugăreni', True), ('Sarmizegetusa', True), ('Pacea de la Buftea', True),
        ('Tratatul de la Trianon', True), ('Dacia Preistorică', True), ('Gelu, Glad și Menumorut', True),
        # --- STRĂIN (FALSE) - 20 intrări ---
        ('Napoleon Bonaparte', False), ('Iulius Cezar', False), ('Abraham Lincoln', False),
        ('Winston Churchill', False), ('Alexandru cel Mare', False), ('Genghis Han', False),
        ('Cleopatra', False), ('Tutankhamun', False), ('Regina Victoria', False), ('Simon Bolivar', False),
        ('Nelson Mandela', False), ('Mao Zedong', False), ('George Washington', False), ('Hannibal', False),
        ('Leonida', False), ('Pericle', False), ('Otto von Bismarck', False), ('Ivan cel Groaznic', False),
        ('Ludovic al XIV-lea', False), ('Cristofor Columb', False)
    ],
    'GEOGRAFIE': [
        # --- ROMÂNIA (TRUE) - 30 intrări ---
        ('Dunărea', True), ('Marea Neagră', True), ('Munții Carpați', True), ('Vârful Moldoveanu', True),
        ('Delta Dunării', True), ('Râul Prut', True), ('Râul Siret', True), ('Râul Mureș', True),
        ('Râul Olt', True), ('Râul Ialomița', True), ('Râul Someș', True), ('Lacul Sfânta Ana', True),
        ('Lacul Roșu', True), ('Transfăgărășan', True), ('Transalpina', True), ('Sfinxul', True),
        ('Babele', True), ('Peștera Scărișoara', True), ('Porțile de Fier', True), ('Câmpia Română', True),
        ('Podișul Moldovei', True), ('Dealurile de Vest', True), ('Munții Apuseni', True), ('Munții Bucegi', True),
        ('Munții Parâng', True), ('Munții Retezat', True), ('Munții Rodnei', True), ('Defileul Jiului', True),
        ('Podișul Dobrogei', True), ('Subcarpații Getici', True),
        # --- STRĂIN (FALSE) - 20 intrări ---
        ('Fluviul Nil', False), ('Munții Alpi', False), ('Muntele Everest', False), ('Fluviul Amazon', False),
        ('Deșertul Sahara', False), ('Munții Himalaya', False), ('Marele Canion', False), ('Fluviul Mississippi', False),
        ('Muntele Fuji', False), ('Oceanul Pacific', False), ('Munții Anzi', False), ('Marea Mediterană', False),
        ('Insula Groenlanda', False), ('Cascada Niagara', False), ('Lacul Baikal', False), ('Vârful Kilimanjaro', False),
        ('Marea Moartă', False), ('Canalul Panama', False), ('Strâmtoarea Gibraltar', False), ('Podișul Tibet', False)
    ],
    'NATURA': [
        # --- ROMÂNIA (TRUE) - 30 intrări ---
        ('Urs carpatin', True), ('Râs', True), ('Capră neagră', True), ('Zimbru', True),
        ('Pelican', True), ('Mistreț', True), ('Cerb', True), ('Căprioară', True),
        ('Cocoș de munte', True), ('Acvilă de munte', True), ('Șacal aurit', True), ('Bursuc', True),
        ('Vidră', True), ('Salamandră', True), ('Țestoasă de uscat', True), ('Floarea de colț', True),
        ('Bujorul românesc', True), ('Narcisa sălbatică', True), ('Ghiocel', True), ('Toporaș', True),
        ('Stejar', True), ('Fag', True), ('Brad', True), ('Molid', True), ('Pin', True),
        ('Tei', True), ('Salcie', True), ('Plop', True), ('Frasin', True), ('Măceș', True),
        # --- STRĂIN (FALSE) - 20 intrări ---
        ('Leu', False), ('Tigru', False), ('Elefant', False), ('Girafă', False),
        ('Zebră', False), ('Hipopotam', False), ('Pinguin', False), ('Cangur', False),
        ('Urs Koala', False), ('Urs Panda', False), ('Cămilă', False), ('Balenă albastră', False),
        ('Rechin alb', False), ('Baobab', False), ('Palmier', False), ('Bambus', False),
        ('Cactus', False), ('Sequoia', False), ('Eucalipt', False), ('Orhidee tropicală', False)
    ],
    'OBIECTIVE': [
        # --- ROMÂNIA (TRUE) - 30 intrări ---
        ('Castelul Bran', True), ('Castelul Peleș', True), ('Mănăstirea Voroneț', True), ('Cetatea Neamț', True),
        ('Coloana Infinitului', True), ('Palatul Parlamentului', True), ('Cazinoul Constanța', True), ('Cetatea Alba Carolina', True),
        ('Curtea de Argeș', True), ('Mănăstirea Putna', True), ('Castelul Corvinilor', True), ('Biserica Neagră', True),
        ('Turnul Sfatului', True), ('Cetatea de Scaun', True), ('Ateneul Român', True), ('Arcul de Triumf', True),
        ('Salina Turda', True), ('Mănăstirea Cozia', True), ('Cetatea Râșnov', True), ('Cimitirul Vesel', True),
        ('Palatul Culturii', True), ('Mănăstirea Horezu', True), ('Cetatea Enisala', True), ('Biserica de lemn Ieud', True),
        ('Cetatea Devei', True), ('Mausoleul Mărășești', True), ('Podul Prieteniei', True), ('Opera Națională', True),
        ('Grădina Botanică', True), ('Muzeul Satului', True),
        # --- STRĂIN (FALSE) - 20 intrări ---
        ('Turnul Eiffel', False), ('Piramidele Giza', False), ('Colosseum', False), ('Statuia Libertății', False),
        ('Big Ben', False), ('Taj Mahal', False), ('Marele Zid', False), ('Acropola Ateniană', False),
        ('Sagrada Familia', False), ('Machu Picchu', False), ('Opera din Sydney', False), ('Burj Khalifa', False),
        ('Catedrala Notre-Dame', False), ('Muntele Rushmore', False), ('Stonehenge', False), ('Poarta Brandenburg', False),
        ('Louvre', False), ('Panteonul', False), ('Vatican', False), ('Podul Golden Gate', False)
    ],
    'ORASE': [
        # --- ROMÂNIA (TRUE) - 30 intrări ---
        ('București', True), ('Iași', True), ('Cluj-Napoca', True), ('Timișoara', True),
        ('Constanța', True), ('Craiova', True), ('Brașov', True), ('Galați', True),
        ('Oradea', True), ('Ploiești', True), ('Brăila', True), ('Arad', True),
        ('Pitești', True), ('Sibiu', True), ('Bacău', True), ('Târgu Mureș', True),
        ('Baia Mare', True), ('Buzău', True), ('Botoșani', True), ('Satu Mare', True),
        ('Râmnicu Vâlcea', True), ('Drobeta-Turnu Severin', True), ('Suceava', True), ('Piatra Neamț', True),
        ('Târgu Jiu', True), ('Târgoviște', True), ('Tulcea', True), ('Bistrița', True),
        ('Reșița', True), ('Slatina', True),
        # --- STRĂIN (FALSE) - 20 intrări ---
        ('Paris', False), ('Londra', False), ('Berlin', False), ('Madrid', False),
        ('Roma', False), ('Viena', False), ('Amsterdam', False), ('Praga', False),
        ('Varșovia', False), ('Budapesta', False), ('Tokyo', False), ('New York', False),
        ('Los Angeles', False), ('Beijing', False), ('Cairo', False), ('Moscova', False),
        ('Istanbul', False), ('Sydney', False), ('Rio de Janeiro', False), ('Toronto', False)
    ]
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

        available_categories = list(BINGO_DATA_SOURCE.keys())
        selected_category_name = random.choice(available_categories)
        selected_items = BINGO_DATA_SOURCE[selected_category_name]

        all_true.extend([item for item in selected_items if item[1] is True])
        all_false.extend([item for item in selected_items if item[1] is False])

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
