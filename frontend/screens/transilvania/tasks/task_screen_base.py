from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty, ListProperty
from frontend.regions.transilvania.tasks.task_logic import TaskLogic
from frontend.utils.popup_helper import create_simple_popup


class TaskScreenBase(Screen):
    timer = NumericProperty(60)
    question = StringProperty('')
    difficulty = StringProperty('')
    bg_color = ListProperty([1, 1, 1, 1])

    def __init__(self, questions, bg_color, task_number, name=None, **kwargs):
        if name:
            kwargs['name'] = name
        super().__init__(**kwargs)
        self.bg_color = bg_color
        self.logic = TaskLogic(questions, task_number)
        self.timer_event = None

    def on_pre_enter(self):
        self.timer = 60
        if self.timer_event:
            self.timer_event.cancel()
        self.setup_question()
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)

    def setup_question(self):
        self.difficulty, self.question = self.logic.get_random_question()
        if hasattr(self, 'ids') and 'answer_input' in self.ids:
            self.ids.answer_input.text = ''

    def update_timer(self, dt):
        self.timer -= 1
        if self.timer <= 0:
            self.finish_task()

    def finish_task(self):
        if self.timer_event:
            self.timer_event.cancel()
            self.timer_event = None

        if not hasattr(self, 'ids') or 'answer_input' not in self.ids:
            return

        user_answer = self.ids.answer_input.text

        if self.logic.check_answer(user_answer):
            prev_screen = self.manager.get_screen("transilvania")

            if self.logic.is_final_task():
                prev_screen.show_completion_popup()
            else:
                prev_screen.unlock_next_task(self.logic.task_number)
                self.manager.current = "transilvania"
        else:
            self.show_error_popup()

    def show_error_popup(self):
        popup = create_simple_popup(
            title="Răspuns greșit",
            message="Încearcă din nou!",
            button_text='OK'
        )
        popup.open()

