from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, NumericProperty, ColorProperty
from kivy.clock import Clock

from backend.domain.entities.Minigame import Rebus
from frontend.utils.colors import AppColors

from kivy.app import App


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
        self.padding = [0, 0, 0, 0]

        # actualizeaza padding dupa ce widgetul e creat
        Clock.schedule_once(self._update_padding, 0)

        # aplica dimensiuni celula
        self._apply_size()
        self.bind(cell_size=self._apply_size)

    def _update_padding(self, *_):
        # aliniaza vertical textul in celula
        lh = self.line_height
        vt = max(0, (self.height - lh) / 2.0)
        self.padding = [0, vt, 0, vt]

    def _apply_size(self, *args):
        self.width = self.cell_size
        self.height = self.cell_size

    def _focus_next(self, dt):
        # muta focusul la urmatoarea celula
        if self.next_cell:
            self.next_cell.focus = True
        elif self.next_row_first_cell:
            self.next_row_first_cell.focus = True

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        # navigare inapoi la celula anterioara
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
        if self.next_cell or self.next_row_first_cell:
            Clock.schedule_once(self._focus_next)


class RebusScreen(Screen):
    rebus_entity = ObjectProperty(None, allownone=True)

    game_container = ObjectProperty(None)
    is_checked = BooleanProperty(False)
    is_completed = BooleanProperty(False)
    background_image = StringProperty('')
    bg_image = StringProperty('')

    region_id = NumericProperty(0)
    primary_color = ColorProperty(AppColors.ACCENT)

    number_w = NumericProperty(50)
    clue_w = NumericProperty(400)
    cell_w = NumericProperty(42)
    max_cols = NumericProperty(15)

    def __init__(self, **kwargs):
        self._initialized = False
        super().__init__(**kwargs)
        self.words_data = []
        self.cells = []


    def _sync_text_size(self, inst, size):
        # aliniaza textul in label
        inst.text_size = size

    def _build_current_config(self):
        if not self.cells or not self.words_data:
            return {}

        # construieste configuratia curenta
        cfg = {}
        for row, word_info in zip(self.cells, self.words_data):
            typed = ''.join((cell.text or '') for cell in row if cell and isinstance(cell, RebusCell)).upper()
            cfg[word_info['clue']] = typed
        return cfg

    def set_theme_color(self):
        colors_map = {
            1: AppColors.TRANSILVANIA,
            2: AppColors.MOLDOVA,
            3: AppColors.TARA_ROMANEASCA,
            4: AppColors.DOBROGEA,
            5: AppColors.BANAT
        }
        self.primary_color = colors_map.get(self.region_id, AppColors.ACCENT)

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
                font_size='22sp',
                halign='center',
                valign='middle',
            )
            num_label.bind(size=self._sync_text_size)
            grid.add_widget(num_label)

            # indiciul / intrebarea
            clue_label = Label(
                text=word_info['clue'],
                size_hint_x=None,
                width=self.clue_w,
                color=(1, 1, 1, 1),
                font_size='20sp',
                halign='left',
                valign='middle',
                markup=True,
            )
            clue_label.bind(size=self._sync_text_size)
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
        if not self.cells or not self.words_data:
            self.is_completed = False
            return

        # coloreaza corect/gresit
        all_correct_cells = True
        for row in self.cells:
            for cell in row:
                if cell and isinstance(cell, RebusCell):
                    if cell.text.upper() == cell.correct_char:
                        cell.background_color = (0.8, 1, 0.8, 1) if cell.is_pivot else (0.6, 1, 0.6, 1)
                    else:
                        cell.background_color = (1, 0.8, 0.6, 1) if cell.is_pivot else (1, 0.6, 0.6, 1)
                        all_correct_cells = False

        # verifica
        is_win_by_entity = True
        if self.rebus_entity:
            current_cfg = self._build_current_config()
            self.rebus_entity.set_current_configuration(current_cfg)
            win_cfg = self.rebus_entity.get_win_configuration()
            is_win_by_entity = all(
                current_cfg.get(clue, '').upper() == answer.upper()
                for clue, answer in win_cfg.items()
            )

        self.is_completed = all_correct_cells and is_win_by_entity

    def reset_colors(self):
        # revine la default
        for row in self.cells:
            for cell in row:
                if cell and isinstance(cell, RebusCell):
                    cell.background_color = (1, 1, 0.7, 1) if cell.is_pivot else (1, 1, 1, 1)

    def clear_rebus(self):
        # goleste rebusul
        self.is_checked = False
        self.is_completed = False
        for row in self.cells:
            for cell in row:
                if cell and isinstance(cell, RebusCell):
                    cell.text = ""
                    cell.background_color = (1, 1, 0.7, 1) if cell.is_pivot else (1, 1, 1, 1)

        if self.rebus_entity:
            self.rebus_entity.set_current_configuration({})

    def finalize_rebus(self):
        # finalizare
        print("Rebus finalizat cu succes!")
        app = App.get_running_app()
        dashboard = app.sm.get_screen('region_dashboard')
        dashboard.load_next_step()

    def go_back(self):
        # inapoi la region dashboard
        app = App.get_running_app()
        app.clouds.change_screen('region_dashboard')

    def load_data(self, data, step_number):
        """
        Incarca date de rebus din backend.
        Format asteptat:
        {
            'type': 'rebus',
            'rebus': Entitate Rebus cu win_configuration si secret_word
        }
        """
        # Reseteaza UI
        self.game_container.clear_widgets()
        self.is_checked = False
        self.is_completed = False
        self.cells = []
        self.words_data = []

        # Obtine entitatea rebus din date
        rebus = data.get('rebus')
        if not rebus or not isinstance(rebus, Rebus):
            self.game_container.add_widget(
                Label(text="Eroare: Nu s-au gasit date de rebus.", color=(1, 1, 1, 1)))
            return

        self.rebus_entity = rebus
        win_configuration = rebus.get_win_configuration()
        secret_word = rebus.get_secret_word()

        if not win_configuration or not secret_word:
            self.game_container.add_widget(
                Label(text="Eroare: Rebus invalid.", color=(1, 1, 1, 1)))
            return


        MAX_COLS = int(self.max_cols)
        pivot_column = MAX_COLS // 2

        words_data = []

        # Proceseaza fiecare pereche indiciu-raspuns
        for secret_idx, (clue, answer) in enumerate(win_configuration.items()):
            word_upper = answer.upper()
            secret_char = secret_word[secret_idx].upper() if secret_idx < len(secret_word) else ''

            # Gaseste indexul pivot
            pivot_idx = -1
            for i, char in enumerate(word_upper):
                if char == secret_char:
                    pivot_idx = i
                    break

            if pivot_idx == -1:
                pivot_idx = len(word_upper) // 2

            # Calculeaza coloana de start astfel incat pivotul sa fie aliniat cu pivot_column
            start_col = pivot_column - pivot_idx

            # Ajusteaza daca cuvantul iese din limite
            if start_col < 0:
                start_col = 0
                pivot_idx = pivot_column if pivot_column < len(word_upper) else len(word_upper) // 2
            elif start_col + len(word_upper) > MAX_COLS:
                start_col = MAX_COLS - len(word_upper)
                pivot_idx = pivot_column - start_col if (pivot_column - start_col) < len(word_upper) else len(word_upper) // 2

            words_data.append({
                'word': word_upper,
                'clue': clue,
                'start_col': start_col,
                'pivot_idx': pivot_idx,
                'secret_index': secret_idx
            })

        # Sorteaza dupa ordinea literelor din cuvantul secret
        words_data.sort(key=lambda x: x['secret_index'])

        self.words_data = words_data
        self.cells = []
        self.game_container.add_widget(self.build_grid(words_data, MAX_COLS))
        self.set_theme_color()