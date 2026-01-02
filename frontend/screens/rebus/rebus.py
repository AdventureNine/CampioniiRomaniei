import random
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.clock import Clock

DATA_SOURCE = {
    'D': [('DUNARE', 'Fluviul de la granita'), ('DECEBAL', 'Rege dac'), ('DACIA', 'Tara dacilor')],
    'A': [('ARAD', 'Municipiu pe Mures'), ('ALBA', 'Judet ardelean'), ('ARDEAL', 'Regiunea Transilvania')],
    'C': [('CARPATI', 'Muntii Romaniei'), ('CLUJ', 'Oras in Transilvania'), ('CRAIOVA', 'Oras in Oltenia')],
    'I': [('ISTORIE', 'Studiul trecutului'), ('IALOMITA', 'Raul si judet'), ('IASI', 'Oras in Moldova')],
    'R': [('ROMA', 'Capitala Imperiului'), ('RESITA', 'Oras in Banat'), ('ROMAN', 'Oras moldovean')],
    'O': [('OLT', 'Raul care taie muntii'), ('ORADEA', 'Oras la granita'), ('ORSOVA', 'Oras pe Dunare')],
    'N': [('NAPOCA', 'Vechiul nume al Clujului'), ('NEAMT', 'Judet in Moldova'), ('NIC', 'Prenume romanesc')],
    'S': [('SARMIZEGETUSA', 'Capitala Daciei'), ('SIBIU', 'Oras sasesc'), ('SOMES', 'Rau in Transilvania')],
    'T': [('TIMIS', 'Judet in Banat'), ('TOLEDO', 'Oras spaniol'), ('TITAN', 'Cartier bucurestean')],
    'B': [('BANAT', 'Regiune in vest'), ('BRASOV', 'Oras in Carpati'), ('BUCEGI', 'Munti langa Bucuresti')],
    'U': [('UNIRE', 'Eveniment din 1918'), ('UNIRII', 'Piata din Bucuresti'), ('URANUS', 'Planeta')],
    'E': [('EMINESCU', 'Poet national'), ('EUROPA', 'Continent'), ('ELIADE', 'Scriitor roman')],
    'M': [('MOLDOVA', 'Regiune istorica'), ('MURES', 'Rau si judet'), ('MIHAI', 'Prenume domnesc')]
}

SECRET_WORDS = ["DACIA", "ROMANIA", "ALBA"]


class RebusCell(TextInput):
    correct_char = StringProperty()
    next_cell = ObjectProperty(None, allownone=True)
    prev_cell = ObjectProperty(None, allownone=True)
    is_pivot = BooleanProperty(False)

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if keycode[1] == 'backspace' and self.text == "" and self.prev_cell:
            self.prev_cell.focus = True
            return True
        return super().keyboard_on_key_down(window, keycode, text, modifiers)

    def insert_text(self, substring, from_undo=False):
        if substring.upper().isalpha():
            self.text = substring.upper()
            if self.next_cell:
                Clock.schedule_once(lambda dt: setattr(self.next_cell, 'focus', True))


class RebusScreen(Screen):
    game_container = ObjectProperty(None)
    is_checked = BooleanProperty(False)

    def on_kv_post(self, base_widget):
        self.generate_rebus()

    def generate_rebus(self):
        self.game_container.clear_widgets()
        self.is_checked = False

        PIVOT_COLUMN = 5
        MAX_COLS = 15

        for _ in range(50):
            secret_word = random.choice(SECRET_WORDS).upper()
            words_data = []
            valid = True

            for idx, char in enumerate(secret_word):
                if char not in DATA_SOURCE:
                    valid = False
                    break

                valid_words = []
                for word, clue in DATA_SOURCE[char]:
                    word = word.upper()
                    for pos in [i for i, c in enumerate(word) if c == char]:
                        start = PIVOT_COLUMN - pos
                        if 0 <= start and start + len(word) <= MAX_COLS:
                            valid_words.append((word, clue, pos))

                if not valid_words:
                    valid = False
                    break

                word, clue, pivot_idx = random.choice(valid_words)
                words_data.append({
                    'word': word,
                    'clue': clue,
                    'start_col': PIVOT_COLUMN - pivot_idx,
                    'pivot_idx': pivot_idx
                })

            if valid:
                break

        if not valid:
            return

        self.cells = []
        self.game_container.add_widget(self.build_grid(words_data, MAX_COLS))

    def build_grid(self, words_data, max_cols):
        grid = GridLayout(cols=2, spacing=0, size_hint=(None, None))
        grid.bind(minimum_height=grid.setter('height'))
        grid.width = 400 + (max_cols * 40)

        for word_info in words_data:
            row_cells = []
            prev_cell = None

            grid.add_widget(Label(
                text=word_info['clue'],
                size_hint_x=None,
                width=400,
                color=(0, 0, 0, 1),
                font_size='16sp',
                halign='left',
                valign='middle',
                text_size=(390, None)
            ))

            row_box = GridLayout(cols=max_cols, spacing=0, size_hint=(None, None))
            row_box.width = max_cols * 40
            row_box.height = 40

            for col in range(max_cols):
                if col < word_info['start_col'] or col >= word_info['start_col'] + len(word_info['word']):
                    row_box.add_widget(Widget(size_hint_x=None, width=40))
                    row_cells.append(None)
                else:
                    idx = col - word_info['start_col']
                    is_pivot = (idx == word_info['pivot_idx'])

                    cell = RebusCell(
                        correct_char=word_info['word'][idx],
                        is_pivot=is_pivot,
                        background_color=(1, 1, 0.7, 1) if is_pivot else (1, 1, 1, 1)
                    )

                    if prev_cell:
                        cell.prev_cell = prev_cell
                        prev_cell.next_cell = cell

                    row_box.add_widget(cell)
                    row_cells.append(cell)
                    prev_cell = cell

            grid.add_widget(row_box)
            self.cells.append(row_cells)

        return grid

    def toggle_check(self):
        if self.is_checked:
            self.reset_colors()
        else:
            self.check_solution()
        self.is_checked = not self.is_checked

    def check_solution(self):
        for row in self.cells:
            for cell in row:
                if cell and isinstance(cell, RebusCell):
                    if cell.text.upper() == cell.correct_char:
                        cell.background_color = (0.8, 1, 0.8, 1) if cell.is_pivot else (0.6, 1, 0.6, 1)
                    else:
                        cell.background_color = (1, 0.8, 0.6, 1) if cell.is_pivot else (1, 0.6, 0.6, 1)

    def reset_colors(self):
        for row in self.cells:
            for cell in row:
                if cell and isinstance(cell, RebusCell):
                    cell.background_color = (1, 1, 0.7, 1) if cell.is_pivot else (1, 1, 1, 1)

    def auto_fill(self):
        for row in self.cells:
            for cell in row:
                if cell and isinstance(cell, RebusCell):
                    cell.text = cell.correct_char

    def clear_rebus(self):
        self.is_checked = False
        for row in self.cells:
            for cell in row:
                if cell and isinstance(cell, RebusCell):
                    cell.text = ""
                    cell.background_color = (1, 1, 0.7, 1) if cell.is_pivot else (1, 1, 1, 1)