from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import NumericProperty, StringProperty, ListProperty, BooleanProperty
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

from frontend.data.game_data import REGIONS_DATA
from frontend.data.question_data import QUESTIONS_DATA
from frontend.data.user_progress import USER_PROGRESS
from frontend.utils.assets import image_path
from frontend.components.common import FeedbackPopup


class LevelIcon(ButtonBehavior, Image):
    level_index = NumericProperty(1)
    region_id = NumericProperty(0)
    region_name = StringProperty("")
    is_locked = BooleanProperty(True)

    def on_level_index(self, instance, value):
        self.update_source()

    def on_is_locked(self, instance, value):
        self.update_source()
        self.disabled = value

    def on_region_id(self, instance, value):
        self.update_source()

    def on_region_name(self, instance, value):
        self.update_source()

    def update_source(self):
        if not self.region_name or self.region_id == 0:
            return

        state = "gray" if self.is_locked else "color"
        folder_name = self.region_name
        filename = f"ui/{folder_name}/level_{self.region_id}_{self.level_index}_{state}.png"

        try:
            self.source = image_path(filename)
        except Exception as e:
            print(f"Nu am găsit iconița: {filename}")


class RegionDashboardScreen(Screen):

    region_id = NumericProperty(0)
    region_name = StringProperty("Regiune")
    mission_text = StringProperty("Descriere Misiune")
    bg_image = StringProperty("")
    levels_status = ListProperty([True, False, False, False, False, False])

    # Variabile interne
    current_level_queue = []
    current_step_index = 0
    current_level_id = 0

    # Variabile Timer
    timer_event = None
    seconds_left = 0

    def on_pre_enter(self, *args):
        App.get_running_app().timer_text = ""
        data = REGIONS_DATA.get(self.region_id)
        if data:
            self.region_name = data['name']
            self.mission_text = data['mission']

            try:
                self.bg_image = image_path(f"backgrounds/bg_{self.region_id}.jpg")
            except:
                self.bg_image = ""

        if self.region_id in USER_PROGRESS:
            self.levels_status = USER_PROGRESS[self.region_id]

    def start_level(self, level_index):
        self.current_level_id = level_index
        region_data = QUESTIONS_DATA.get(self.region_id, {})
        if not region_data:
            print(f"Eroare: Nu există date în QUESTIONS_DATA pentru Regiunea {self.region_id}")
            return

        exercises = region_data.get(level_index, [])
        if not exercises:
            print(f"Nu există exerciții pentru Nivelul {level_index}")
            return

        self.current_level_queue = exercises
        self.current_step_index = 0

        self.seconds_left = 180
        self.update_timer_label(0)

        if self.timer_event: self.timer_event.cancel()
        self.timer_event = Clock.schedule_interval(self.update_timer_label, 1)

        self.load_next_step()

    def update_timer_label(self, dt):
        app = App.get_running_app()
        if self.seconds_left > 0:
            mins = self.seconds_left // 60
            secs = self.seconds_left % 60
            app.timer_text = f"{mins:02}:{secs:02}"
            self.seconds_left -= 1
        else:
            app.timer_text = "00:00"
            self.trigger_game_over()

    def trigger_game_over(self):
        if self.timer_event: self.timer_event.cancel()
        popup = FeedbackPopup(
            type='fail',
            title_text="Timpul a expirat!",
            message_text="Nu ai terminat nivelul la timp. Încearcă încă o dată.",
            button_text="Înapoi la Hartă"
        )
        popup.bind(on_dismiss=self.return_to_dashboard)
        popup.open()

    def return_to_dashboard(self, instance=None):
        app = App.get_running_app()
        app.timer_text = ""
        if self.timer_event: self.timer_event.cancel()
        app.clouds.change_screen('region_dashboard')

    def load_next_step(self):
        app = App.get_running_app()

        if self.current_step_index < len(self.current_level_queue):
            ex_data = self.current_level_queue[self.current_step_index]
            ex_type = ex_data['type']

            if ex_type == 'quiz':
                screen = app.sm.get_screen('generic_quiz')
                screen.load_data(ex_data, self.current_step_index + 1)
                screen.bg_image = self.bg_image
                app.clouds.change_screen('generic_quiz')

            elif ex_type == 'fill':
                screen = app.sm.get_screen('generic_fill')
                screen.load_data(ex_data, self.current_step_index + 1)
                screen.bg_image = self.bg_image
                app.clouds.change_screen('generic_fill')

            elif ex_type == 'puzzle':
                screen = app.sm.get_screen('puzzle')
                screen.game_grid = screen.ids.puzzle_grid
                screen.load_data(ex_data, self.current_step_index + 1)
                screen.bg_image = self.bg_image
                app.clouds.change_screen('puzzle')

            elif ex_type == 'map_guess':
                screen = app.sm.get_screen('map_guess')
                screen.load_data(ex_data, self.current_step_index + 1)
                app.clouds.change_screen('map_guess')

            elif ex_type == 'rebus':
                screen = app.sm.get_screen('rebus')
                screen.load_data(ex_data, self.current_step_index + 1)
                screen.bg_image = self.bg_image
                app.clouds.change_screen('rebus')

            elif ex_type == 'bingo':
                screen = app.sm.get_screen('bingo')
                screen.current_difficulty = ex_data.get('difficulty', screen.current_difficulty)
                screen.bg_image = self.bg_image
                app.clouds.change_screen('bingo')

            self.current_step_index += 1
        else:
            self.finish_level_sequence()

    def finish_level_sequence(self):
        app = App.get_running_app()
        if self.timer_event: self.timer_event.cancel()
        app.timer_text = ""

        points_earned = 50
        app.score += points_earned

        next_index = self.current_level_id

        if self.levels_status[
            self.current_level_id]:
            pass

        # Mesajele popup
        popup = FeedbackPopup(
            type='level_complete',
            title_text="Nivel Complet!",
            message_text=f"Felicitări! Ai câștigat {points_earned} puncte.",
            button_text="Super!"
        )
        popup.bind(on_dismiss=self.go_back_to_levels)
        popup.open()

        if next_index < 6:
            new_status = list(self.levels_status)

            if self.current_level_id < 6:
                new_status[self.current_level_id] = True
                self.levels_status = new_status
                USER_PROGRESS[self.region_id] = self.levels_status

    def go_back_to_levels(self, instance):
        app = App.get_running_app()
        app.clouds.change_screen('region_dashboard')