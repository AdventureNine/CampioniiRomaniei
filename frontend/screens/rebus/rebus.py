import random
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, NumericProperty
from kivy.clock import Clock

from backend.domain.utils.Difficulty import Difficulty

# date pentru cuvinte
DATA_SOURCE = {
    'A': [
        ('ARAD', 'Municipiu pe Mures'),
        ('ALBA', 'Judet ardelean'),
        ('ARDEAL', 'Regiunea Transilvania'),
        ('AVRAM', 'Prenume revolutionar'),
        ('ASTRA', 'Asociatie culturala')
    ],
    'B': [
        ('BANAT', 'Regiune in vest'),
        ('BRASOV', 'Oras in Carpati'),
        ('BUCEGI', 'Munti langa Bucuresti'),
        ('BISTRITA', 'Oras in nord'),
        ('BUZAU', 'Judet din Muntenia')
    ],
    'C': [
        ('CARPATI', 'Muntii Romaniei'),
        ('CLUJ', 'Oras in Transilvania'),
        ('CRAIOVA', 'Oras in Oltenia'),
        ('CALARASI', 'Judet dunarean'),
        ('CORVIN', 'Familie nobiliara')
    ],
    'D': [
        ('DUNARE', 'Fluviul de la granita'),
        ('DECEBAL', 'Rege dac'),
        ('DACIA', 'Tara dacilor'),
        ('DOBROGEA', 'Regiune istorica'),
        ('DORU', 'Sentiment romanesc')
    ],
    'E': [
        ('EMINESCU', 'Poet national'),
        ('EUROPA', 'Continent'),
        ('ELIADE', 'Scriitor roman'),
        ('ENESCU', 'Compozitor roman'),
        ('ETNIE', 'Grup cultural')
    ],
    'I': [
        ('ISTORIE', 'Studiul trecutului'),
        ('IALOMITA', 'Raul si judet'),
        ('IASI', 'Oras in Moldova'),
        ('ILFOV', 'Judet din jurul capitalei'),
        ('ION', 'Prenume romanesc')
    ],
    'M': [
        ('MOLDOVA', 'Regiune istorica'),
        ('MURES', 'Rau si judet'),
        ('MIHAI', 'Prenume domnesc'),
        ('MARAMURES', 'Zona traditionala'),
        ('MUNTENIA', 'Regiune sudica')
    ],
    'N': [
        ('NAPOCA', 'Vechiul nume al Clujului'),
        ('NEAMT', 'Judet in Moldova'),
        ('NIC', 'Prenume romanesc'),
        ('NISTRU', 'Fluviu estic'),
        ('NASAUD', 'Zona ardeleneasca')
    ],
    'O': [
        ('OLT', 'Raul care taie muntii'),
        ('ORADEA', 'Oras la granita'),
        ('ORSOVA', 'Oras pe Dunare'),
        ('OLTENIA', 'Regiune sud-vestica'),
        ('OPINCA', 'Incaltaminte traditionala')
    ],
    'R': [
        ('ROMA', 'Capitala Imperiului'),
        ('RESITA', 'Oras in Banat'),
        ('ROMAN', 'Oras moldovean'),
        ('ROMANIA', 'Stat european'),
        ('RADU', 'Prenume domnesc')
    ],
    'S': [
        ('SARMIZEGETUSA', 'Capitala Daciei'),
        ('SIBIU', 'Oras sasesc'),
        ('SOMES', 'Rau in Transilvania'),
        ('SUCEAVA', 'Oras medieval'),
        ('SECUI', 'Grup etnic')
    ],
    'T': [
        ('TIMIS', 'Judet in Banat'),
        ('TOLEDO', 'Oras spaniol'),
        ('TITAN', 'Cartier bucurestean'),
        ('TARGOVISTE', 'Fosta capitala'),
        ('TRAIAN', 'Imparat roman')
    ],
    'U': [
        ('UNIRE', 'Eveniment din 1918'),
        ('UNIRII', 'Piata din Bucuresti'),
        ('URANUS', 'Planeta'),
        ('UIOARA', 'Localitate ardeleneasca'),
        ('UTURE', 'Pasare rapitoare')
    ]
}

# cuvintele secrete
SECRET_WORDS = [
    "DACIA",
    "ROMANIA",
    "ALBA",
    "MOLDOVA",
    "UNIRE",
    "CARPATI",
    "EMINESCU",
    "ARDEAL",
    "OLTENIA",
    "BUCEGI"
]


class RebusCell(TextInput):
    correct_char = StringProperty()
    cell_size = NumericProperty(40)

    # legaturi pentru focus
    next_cell = ObjectProperty(None, allownone=True)
    prev_cell = ObjectProperty(None, allownone=True)
    next_row_first_cell = ObjectProperty(None, allownone=True)
    prev_row_last_cell = ObjectProperty(None, allownone=True)

    # marcheaza coloana pivot
    is_pivot = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.multiline = False
        self.halign = 'center'
        self.font_size = '24sp'
        self.cursor_width = 0
        self.padding = [0, 0, 0, 0]

        # actualizeaza padding la schimbari
        self.bind(size=self._update_padding, font_size=self._update_padding)
        Clock.schedule_once(lambda dt: self._update_padding())

    def _update_padding(self, *_):
        lh = self.line_height
        vt = max(0, (self.height - lh) / 2.0)
        self.padding = [0, vt, 0, vt]


    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if keycode[1] == 'backspace' and self.text == "":
            if self.prev_cell:
                self.prev_cell.focus = True
                return True
            elif self.prev_row_last_cell:
                self.prev_row_last_cell.focus = True
                return True
        return super().keyboard_on_key_down(window, keycode, text, modifiers)

    def insert_text(self, substring, from_undo=False):
        # accepta doar litere
        ch = next((c for c in substring if c.isalpha()), '')
        if not ch:
            return
        self.text = ch.upper()
        if self.next_cell:
            Clock.schedule_once(lambda dt: setattr(self.next_cell, 'focus', True))
        elif self.next_row_first_cell:
            Clock.schedule_once(lambda dt: setattr(self.next_row_first_cell, 'focus', True))


class RebusScreen(Screen):
    game_container = ObjectProperty(None)
    is_checked = BooleanProperty(False)
    is_completed = BooleanProperty(False)
    background_image = StringProperty('')

    number_w = NumericProperty(50)
    clue_w = NumericProperty(400)
    cell_w = NumericProperty(40)
    max_cols = NumericProperty(15)
    max_attempts = NumericProperty(150)

    current_difficulty = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_image = 'screens/rebus/background.png'
        self.current_difficulty = Difficulty[1]

        if self.current_difficulty == Difficulty[0]:
            self.max_cols = 12
            self.max_attempts = 100
        elif self.current_difficulty == Difficulty[1]:
            self.max_cols = 15
            self.max_attempts = 150
        else:
            self.max_cols = 18
            self.max_attempts = 220

    def on_kv_post(self, base_widget):
        # ruleaza dupa kv
        self.generate_rebus()

    def generate_rebus(self):
        # reset ui si date
        self.game_container.clear_widgets()
        self.is_checked = False
        self.is_completed = False

        MAX_COLS = int(self.max_cols)
        MAX_ATTEMPTS = int(self.max_attempts)

        valid_variants = []

        for _ in range(MAX_ATTEMPTS):
            secret_word = random.choice(SECRET_WORDS).upper()

            # pivot random
            pivot_column = random.randint(3, MAX_COLS - 4)

            indexed_letters = list(enumerate(secret_word))
            random.shuffle(indexed_letters)

            words_data = []
            used_words = set()
            valid = True

            for original_idx, char in indexed_letters:
                if char not in DATA_SOURCE:
                    valid = False
                    break

                candidates = []

                # gaseste cuvinte potrivite
                for word, clue in DATA_SOURCE[char]:
                    w = word.upper()
                    if w in used_words:
                        continue
                    for pos in [i for i, c in enumerate(w) if c == char]:
                        start = pivot_column - pos
                        if 0 <= start and start + len(w) <= MAX_COLS:
                            candidates.append((w, clue, pos, start))

                if not candidates:
                    valid = False
                    break

                # alege un cuvant random
                w, clue, pivot_idx, start_col = random.choice(candidates)
                used_words.add(w)
                words_data.append({
                    'word': w,
                    'clue': clue,
                    'start_col': start_col,
                    'pivot_idx': pivot_idx,
                    'secret_index': original_idx
                })

            if valid and len(words_data) == len(secret_word):
                valid_variants.append(words_data)

        if not valid_variants:
            self.cells = []
            self.game_container.add_widget(
                Label(text="Nu s-a putut genera un rebus.\nÎncearcă din nou.", color=(1, 1, 1, 1)))
            return

        # alege o varianta random
        best_variant = random.choice(valid_variants)

        # ordonare dupa pozitia din cuvantul secret
        best_variant.sort(key=lambda x: x['secret_index'])

        self.cells = []
        self.game_container.add_widget(self.build_grid(best_variant, MAX_COLS))

    def build_grid(self, words_data, max_cols):
        grid = GridLayout(cols=3, spacing=0, size_hint=(None, None))
        grid.bind(minimum_height=grid.setter('height'))
        grid.bind(minimum_width=grid.setter('width'))

        grid.width = self.number_w + self.clue_w + (max_cols * self.cell_w)

        for row_idx, word_info in enumerate(words_data):
            row_cells = []
            prev_cell = None
            first_cell = None
            last_cell = None

            row_no = row_idx + 1

            # numerul randului
            num_label = Label(
                text=f"[b]{row_no}[/b]",
                markup=True,
                size_hint_x=None,
                width=self.number_w,
                color=(1, 1, 1, 1),
                font_size='18sp',
                halign='center',
                valign='middle',
            )
            num_label.bind(size=lambda inst, val: setattr(inst, 'text_size', val))
            grid.add_widget(num_label)

            # indiciul / intrebarea
            clue_label = Label(
                text=word_info['clue'],
                size_hint_x=None,
                width=self.clue_w,
                color=(1, 1, 1, 1),
                font_size='16sp',
                halign='left',
                valign='middle',
                markup=True,
            )
            clue_label.bind(size=lambda inst, val: setattr(inst, 'text_size', val))
            grid.add_widget(clue_label)

            row_box = GridLayout(cols=max_cols, spacing=0, size_hint=(None, None))
            row_box.width = max_cols * self.cell_w
            row_box.height = self.cell_w

            for col in range(max_cols):
                if col < word_info['start_col'] or col >= word_info['start_col'] + len(word_info['word']):
                    row_box.add_widget(Widget(size_hint=(None, None), width=self.cell_w, height=self.cell_w))
                    row_cells.append(None)
                else:
                    idx = col - word_info['start_col']
                    is_pivot = (idx == word_info['pivot_idx'])

                    # celula editabila
                    cell = RebusCell(
                        correct_char=word_info['word'][idx],
                        is_pivot=is_pivot,
                        cell_size=self.cell_w,
                        background_color=(1, 1, 0.7, 1) if is_pivot else (1, 1, 1, 1)
                    )

                    if first_cell is None:
                        first_cell = cell

                    # leaga stanga-dreapta
                    if prev_cell:
                        cell.prev_cell = prev_cell
                        prev_cell.next_cell = cell

                    row_box.add_widget(cell)
                    row_cells.append(cell)
                    last_cell = cell
                    prev_cell = cell

            grid.add_widget(row_box)
            self.cells.append(row_cells)

            # leaga randuri la focus
            if row_idx > 0 and last_cell and len(self.cells) > 1:
                prev_row_last = None
                for c in reversed(self.cells[-2]):
                    if c and isinstance(c, RebusCell):
                        prev_row_last = c
                        break
                if prev_row_last and first_cell:
                    prev_row_last.next_row_first_cell = first_cell
                    first_cell.prev_row_last_cell = prev_row_last

        return grid

    def toggle_check(self):
        # verificare
        if self.is_checked:
            self.reset_colors()
            self.is_completed = False
        else:
            self.check_solution()
        self.is_checked = not self.is_checked

    def check_solution(self):
        # coloreaza corect/gresit
        all_correct = True
        for row in self.cells:
            for cell in row:
                if cell and isinstance(cell, RebusCell):
                    if cell.text.upper() == cell.correct_char:
                        cell.background_color = (0.8, 1, 0.8, 1) if cell.is_pivot else (0.6, 1, 0.6, 1)
                    else:
                        cell.background_color = (1, 0.8, 0.6, 1) if cell.is_pivot else (1, 0.6, 0.6, 1)
                        all_correct = False

        self.is_completed = all_correct

    def reset_colors(self):
        # revine la default
        for row in self.cells:
            for cell in row:
                if cell and isinstance(cell, RebusCell):
                    cell.background_color = (1, 1, 0.7, 1) if cell.is_pivot else (1, 1, 1, 1)

    def auto_fill(self):
        # completeaza automat
        for row in self.cells:
            for cell in row:
                if cell and isinstance(cell, RebusCell):
                    cell.text = cell.correct_char

    def clear_rebus(self):
        # goleste rebusul
        self.is_checked = False
        self.is_completed = False
        for row in self.cells:
            for cell in row:
                if cell and isinstance(cell, RebusCell):
                    cell.text = ""
                    cell.background_color = (1, 1, 0.7, 1) if cell.is_pivot else (1, 1, 1, 1)

    def finalize_rebus(self):
        # finalizare
        print("Rebus finalizat cu succes!")

    def go_back(self):
        # inapoi la nivelul anterior
        print("Inapoi la ecranul anterior")