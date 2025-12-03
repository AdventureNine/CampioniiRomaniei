from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Ellipse, Line
from kivy.properties import ObjectProperty, StringProperty
from frontend.regions.transilvania.transilvania import Transilvania
from frontend.regions.transilvania.colors import (
    TASK_CIRCLE_SHADOW, TASK_CIRCLE_LOCKED, TASK_CIRCLE_LINE,
    TASK_LOCK, TASK_LABEL_LOCKED
)
from frontend.config.paths import TRANSILVANIA_MAP, TRANSILVANIA_MASCOT, TRANSILVANIA_PLAY_BUTTON


class TransilvaniaRegionScreen(Screen):
    logic = ObjectProperty(None)
    map_source = StringProperty('')
    mascot_source = StringProperty('')

    def __init__(self, **kwargs):
        self.name = "transilvania"
        self.logic = Transilvania(self)
        self.task_widgets = []

        self.map_source = TRANSILVANIA_MAP
        self.mascot_source = TRANSILVANIA_MASCOT

        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):
        self.create_task_circles()

    def create_task_circles(self):
        positions = [
            {'center_x': 0.53, 'center_y': 0.65},
            {'center_x': 0.78, 'center_y': 0.65},
            {'center_x': 0.53, 'center_y': 0.40},
            {'center_x': 0.78, 'center_y': 0.40}
        ]

        main_layout = self.children[0]
        for i, task in enumerate(self.logic.tasks):
            widget = self.create_single_task(task, positions[i])
            main_layout.add_widget(widget)
            self.task_widgets.append(widget)

    def create_single_task(self, task, position):
        container = FloatLayout(size_hint=(None, None), size=(170, 170), pos_hint=position)

        with container.canvas.before:
            Color(*TASK_CIRCLE_SHADOW)
            Ellipse(pos=(8, 6), size=(164, 164))
            if task["unlocked"]:
                Color(*task["color"])
            else:
                Color(*TASK_CIRCLE_LOCKED)
            Ellipse(pos=(10, 10), size=(150, 150))
            if self.logic.selected_task_id == task["id"]:
                Color(1, 1, 0, 0.4)
                Ellipse(pos=(10, 10), size=(150, 150))
            Color(*TASK_CIRCLE_LINE)
            Line(ellipse=(10, 10, 150, 150), width=5)

        if task["unlocked"]:
            btn = Button(
                background_color=(0, 0, 0, 0),
                size_hint=(1, 1)
            )
            btn.bind(on_press=lambda x, tid=task["id"]: self.logic.select_task(tid))
            container.add_widget(btn)

            title = Label(
                text=task["name"],
                font_size='18sp',
                bold=True,
                color=(1, 1, 1, 1),
                halign='center',
                valign='middle',
                pos_hint={'center_x': 0.5, 'center_y': 0.62}
            )
            title.bind(size=title.setter("text_size"))
            container.add_widget(title)

            play_img = Image(
                source=TRANSILVANIA_PLAY_BUTTON,
                size_hint=(None, None),
                size=(75, 75),
                pos_hint={'center_x': 0.5, 'center_y': 0.35},
                allow_stretch=True
            )
            container.add_widget(play_img)
        else:
            icons = {1: "M", 2: "D", 3: "C", 4: "A"}
            label_icon = Label(
                text=icons.get(task["id"], ""),
                font_size='56sp',
                bold=True,
                color=(0.5, 0.5, 0.5, 1),
                pos_hint={'center_x': 0.5, 'center_y': 0.6}
            )
            container.add_widget(label_icon)
            lock = Label(
                text="X", font_size='28sp', bold=True, color=TASK_LOCK,
                pos_hint={'right': 0.90, 'y': 0.08}
            )
            container.add_widget(lock)

            title = Label(
                text=task["name"],
                font_size='13sp',
                bold=True,
                color=TASK_LABEL_LOCKED,
                halign='center',
                valign='top',
                pos_hint={'center_x': 0.5, 'y': 0.15}
            )
            title.bind(size=title.setter("text_size"))
            container.add_widget(title)

        return container

    def start_task(self, task_id):
        screen_names = {1: 'task_1', 2: 'task_2', 3: 'task_3', 4: 'task_4'}
        if self.manager and task_id in screen_names:
            self.manager.current = screen_names[task_id]

    def unlock_next_task(self, task_id):
        self.logic.unlock_next_task(task_id)
        self.refresh_tasks()

    def refresh_tasks(self):
        main_layout = self.children[0]
        for widget in self.task_widgets:
            main_layout.remove_widget(widget)
        self.task_widgets.clear()
        self.create_task_circles()

    def show_completion_popup(self):
        self.logic.show_completion_popup()

