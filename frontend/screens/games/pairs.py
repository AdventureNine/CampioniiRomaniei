import random
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.behaviors import DragBehavior
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty, ListProperty, ColorProperty, \
    NumericProperty
from kivy.app import App

from frontend.components.common import FeedbackPopup
from frontend.utils.assets import image_path
from frontend.utils.colors import AppColors


# --- Widget-ul care poate fi tras (Răspunsul) ---
class DraggableAnswer(DragBehavior, Label):
    current_slot = ObjectProperty(None)
    correct_text = StringProperty("")
    is_locked = BooleanProperty(False)
    background_color = ColorProperty((0.2, 0.6, 0.8, 1))
    state = StringProperty('normal')

    def on_touch_down(self, touch):
        if self.is_locked:
            return False

        if self.collide_point(*touch.pos):
            self.state = 'down'
            current_size = self.size
            self.size_hint = (None, None)
            self.size = current_size
            self.original_pos = self.pos
            self.parent.remove_widget(self)
            App.get_running_app().root.add_widget(self)
            self.center = touch.pos
            touch.grab(self)
            return True

        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if self.is_locked:
            return False
        if touch.grab_current is self:
            self.center = touch.pos
            return True
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            touch.ungrab(self)
            self.state = 'normal'

            if self._get_uid('drag_continue'):
                app = App.get_running_app()
                screen = app.sm.get_screen('pairs_game')

                # Fallback pentru debug
                if not screen:
                    pass

                found_slot = None
                if screen and hasattr(screen.ids, 'rows_container'):
                    for row in screen.ids.rows_container.children:
                        slot = row.ids.slot
                        slot_pos = slot.to_window(*slot.pos)
                        if (slot_pos[0] < touch.x < slot_pos[0] + slot.width) and \
                                (slot_pos[1] < touch.y < slot_pos[1] + slot.height):
                            found_slot = slot
                            break

                if found_slot:
                    self.move_to_slot(found_slot)
                else:
                    self.move_to_slot(self.current_slot)
            return True
        return super().on_touch_up(touch)

    def move_to_slot(self, target_slot):
        if self.parent:
            self.parent.remove_widget(self)

        occupant = None
        if target_slot.children:
            occupant = target_slot.children[0]

        if target_slot == self.current_slot and occupant == self:
            self.size_hint = (1, 1)
            target_slot.add_widget(self)
            return

        if occupant:
            target_slot.remove_widget(occupant)
            if self.current_slot:
                self.current_slot.add_widget(occupant)
                occupant.current_slot = self.current_slot
                occupant.size_hint = (1, 1)

        target_slot.add_widget(self)
        self.current_slot = target_slot
        self.size_hint = (1, 1)


# --- Slotul Gol (Receptorul) ---
class AnswerSlot(BoxLayout):
    pass


# --- Un Rând (Întrebare + Slot) ---
class PairsRow(BoxLayout):
    question_text = StringProperty("")
    pass


# --- Ecranul Principal ---
class PairsGameScreen(Screen):
    bg_image = StringProperty('')
    is_checked = BooleanProperty(False)
    is_completed = BooleanProperty(False)
    region_id = NumericProperty(0)
    header_color = ColorProperty(AppColors.PRIMARY)  # Culoarea default a header-ului

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.win_config = {}

    def set_theme_color(self):
        """
        Setează culoarea header-ului în funcție de regiunea curentă.
        """
        colors_map = {
            1: AppColors.TRANSILVANIA,  # Maro
            2: AppColors.MOLDOVA,  # Verde
            3: AppColors.TARA_ROMANEASCA,  # Galben
            4: AppColors.DOBROGEA,  # Albastru
            5: AppColors.BANAT  # Turcoaz
        }
        # Dacă regiunea nu e găsită (0 sau alta), folosim PRIMARY (Albastru standard)
        self.header_color = colors_map.get(self.region_id, AppColors.PRIMARY)

    def load_data(self, data, step_number):
        print(f"--- DEBUG PAIRS: Date primite: {data}")  # Verifică consola pentru asta!

        self.ids.rows_container.clear_widgets()
        self.is_checked = False
        self.is_completed = False

        # 1. Configurare Fundal și Regiune (dacă există în date)
        if 'background' in data and data['background']:
            self.bg_image = image_path(data['background'])

        self.set_theme_color()

        # 2. Extragere Minigame (cu FALLBACK)
        minigame_entity = data.get('minigame') or data.get('pairs')

        self.win_config = minigame_entity.get_win_configuration()
        questions = list(self.win_config.keys())
        answers = list(self.win_config.values())

        # Amestecăm răspunsurile
        random.shuffle(answers)

        container = self.ids.rows_container

        # Generăm rândurile
        for i, question in enumerate(questions):
            row = PairsRow()
            row.question_text = str(question)

            ans_widget = DraggableAnswer(text=str(answers[i]))

            slot = row.ids.slot
            slot.add_widget(ans_widget)
            ans_widget.current_slot = slot

            container.add_widget(row)

    def check_solution(self):
        """
        Verifică răspunsurile, colorează și afișează popup-ul corespunzător.
        """
        correct_count = 0
        total_items = len(self.win_config)
        rows = self.ids.rows_container.children

        all_correct = True

        for row in rows:
            question = row.question_text
            slot = row.ids.slot

            if len(slot.children) > 0:
                answer_widget = slot.children[0]
                given_answer = answer_widget.text
                correct_answer = str(self.win_config.get(question))

                if given_answer == correct_answer:
                    # Răspuns Corect -> Verde și Blocat
                    correct_count += 1
                    answer_widget.is_locked = True
                    answer_widget.background_color = AppColors.SUCCESS
                else:
                    # Răspuns Greșit -> Roșu (temporar)
                    all_correct = False
                    answer_widget.background_color = AppColors.ERROR
            else:
                # Slot gol -> Considerat greșit pentru validarea finală
                all_correct = False

        self.is_checked = True

        # Afișăm popup-ul corespunzător
        if all_correct:
            self.is_completed = True
            self.show_success_popup()
        else:
            self.is_checked = False
            self.show_fail_popup(correct_count, total_items)

    def show_success_popup(self):
        popup = FeedbackPopup(
            type='success',
            title_text="Felicitări!",
            message_text="Ai asociat corect toate perechile!",
            button_text="Continuă"
        )
        popup.bind(on_dismiss=self.go_next)
        popup.open()

    def show_fail_popup(self, correct, total):
        """
        Afișează un popup de informare/eșec.
        La închidere (on_dismiss), resetează culorile greșite.
        """
        msg = f"Ai potrivit corect {correct} din {total} perechi.\nMai încearcă!"
        popup = FeedbackPopup(
            type='info',
            title_text="Nu te da bătut!",
            message_text=msg,
            button_text="Cotinua"
        )
        # Când se închide popup-ul, resetăm culorile roșii la albastru
        popup.bind(on_dismiss=self.reset_colors)
        popup.open()

    def reset_colors(self, instance=None):
        """
        Resetează la culoarea normală (albastru) doar răspunsurile care NU sunt blocate (cele greșite).
        """
        rows = self.ids.rows_container.children
        for row in rows:
            slot = row.ids.slot
            if slot.children:
                w = slot.children[0]
                # Dacă nu e blocat (deci a fost greșit sau nemutat), îl facem albastru
                if not w.is_locked:
                    w.background_color = (0.2, 0.6, 0.8, 1)  # Albastru standard

    def go_next(self, instance):
        app = App.get_running_app()
        if app.sm.current == 'pairs_game' and not hasattr(app, 'service'):
            return

        # Navigare normală
        if app.sm.has_screen('region_dashboard'):
            dashboard = app.sm.get_screen('region_dashboard')
            dashboard.load_next_step()