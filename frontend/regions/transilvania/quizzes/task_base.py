import random

from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from frontend.regions.transilvania.colors import PRIMARY_TEXT, DIFFICULTY_TEXT, TIMER_TEXT, BUTTON_BG, BUTTON_TEXT, INPUT_BG, INPUT_TEXT


class TaskScreenBase(Screen):
    def __init__(self, questions, bg_color, task_number, name=None, **kwargs):
        if name:
            kwargs['name'] = name
        super().__init__(**kwargs)
        self.questions = questions
        self.bg_color = bg_color
        self.task_number = task_number
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        self.timer = 60
        self.timer_event = None
        self.question = None
        self.difficulty = None
        self.correct = None
        self.input = None
        self.diff_label = None
        self.timer_label = None
        with self.canvas.before:
            Color(*self.bg_color)
            self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)
        self.setup_ui()

    def setup_ui(self):
        self.layout.clear_widgets()
        self.difficulty, qlist = random.choice(list(self.questions.items()))
        self.question, self.correct = random.choice(qlist)
        self.diff_label = Label(
            text=f'Dificultate: {self.difficulty}',
            font_size='21sp',
            bold=True,
            color=DIFFICULTY_TEXT,
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5, 'top': 0.9}
        )
        self.layout.add_widget(self.diff_label)
        self.timer_label = Label(
            text=f'Timp ramas: {self.timer}s',
            font_size='20sp',
            color=TIMER_TEXT,
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5, 'top': 0.82}
        )
        self.layout.add_widget(self.timer_label)
        question_label = Label(
            text=self.question,
            font_size='25sp',
            size_hint=(0.7, 0.2),
            pos_hint={'center_x': 0.5, 'top': 0.65},
            color=PRIMARY_TEXT
        )
        self.layout.add_widget(question_label)
        self.input = TextInput(
            multiline=False,
            font_size='20sp',
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            background_color=INPUT_BG,
            foreground_color=INPUT_TEXT
        )
        self.layout.add_widget(self.input)
        finish_btn = Button(
            text='Finalizare',
            size_hint=(0.25, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.08},
            background_color=BUTTON_BG,
            color=BUTTON_TEXT,
            font_size='20sp'
        )
        finish_btn.bind(on_press=self.finish_task)
        self.layout.add_widget(finish_btn)
        self.timer = 60
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)

    def _update_bg(self, *args):
        if self.bg_rect:
            self.bg_rect.size = self.size
            self.bg_rect.pos = self.pos

    def update_timer(self, dt):
        self.timer -= 1
        self.timer_label.text = f'Timp ramas: {self.timer}s'
        if self.timer <= 0:
            self.finish_task(None)

    def finish_task(self, instance):
        if self.timer_event:
            self.timer_event.cancel()
            self.timer_event = None

        user_answer = self.input.text.strip().lower()
        good_answer = self.correct.strip().lower()

        if user_answer == good_answer:
            prev_screen = self.manager.get_screen("transilvania")
            prev_screen.unlock_next_task(self.task_number)
            self.manager.current = "transilvania"
            return
        else:
            popup = Popup(
                title="Răspuns greșit",
                content=Label(text="Încearcă din nou!", font_size="20sp"),
                size_hint=(0.6, 0.3)
            )
            popup.open()
            return

    def on_pre_enter(self):
        self.timer = 60
        if self.timer_event:
            self.timer_event.cancel()
        self.setup_ui()

