from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import NumericProperty, StringProperty
from kivy.clock import Clock
from components.cloud_transition import change_screen_with_clouds

class ExerciseScreen(Screen):
    level_id = NumericProperty(0)
    region_id_ref = NumericProperty(0)
    exercise_title = StringProperty("Exercițiu")
    exercise_content = StringProperty("...")
    timer_seconds = NumericProperty(180)
    timer_text = StringProperty("03:00")
    timer_event = None

    def on_enter(self, *args):
        self.timer_seconds = 180
        self.update_timer_label(0)
        self.timer_event = Clock.schedule_interval(self.update_timer_label, 1)

    def on_leave(self, *args):
        if self.timer_event:
            self.timer_event.cancel()

    def update_timer_label(self, dt):
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            minutes = self.timer_seconds // 60
            seconds = self.timer_seconds % 60
            self.timer_text = f"{minutes:02}:{seconds:02}"
        else:
            self.timer_text = "00:00"

    def complete_exercise(self):
        app = App.get_running_app()
        app.credit += 10
        region_screen = app.sm.get_screen('region')
        region_screen.unlock_next_level(self.level_id)
        change_screen_with_clouds(app, 'region')

    def quit_exercise(self):
        app = App.get_running_app()
        change_screen_with_clouds(app, 'region')