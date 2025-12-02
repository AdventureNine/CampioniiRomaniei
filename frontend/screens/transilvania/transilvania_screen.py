from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, Ellipse, RoundedRectangle, Line
from kivy.uix.image import Image
import os

from frontend.regions.transilvania.colors import (
    REGION_BG, HEADER_BG, HEADER_TITLE, HEADER_SUBTITLE, MASCOT_NAME,
    TASK_CIRCLE_SHADOW, TASK_CIRCLE_LOCKED, TASK_CIRCLE_LINE,
    TASK_LOCK, BOTTOM_BG,
    START_BTN_BG, VERIFY_BTN_BG, HELP_BTN_BG, TASK_LABEL_LOCKED
)

from frontend.regions.transilvania.transilvania import Transilvania

class TransilvaniaRegionScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logic = Transilvania(self)
        self.name = "transilvania"
        self.layout = FloatLayout()
        self.setup_ui()
        self.add_widget(self.layout)

    def setup_ui(self):
        self.layout.clear_widgets()
        with self.layout.canvas.before:
            Color(*REGION_BG)
            Rectangle(size=(1280, 800), pos=(0, 0))
        self.create_header()
        self.create_left_sidebar()
        self.create_task_circles()
        self.create_bottom_buttons()

    def create_header(self):
        header = FloatLayout(size_hint=(0.95, 0.13), pos_hint={'center_x': 0.5, 'top': 0.99})
        with header.canvas.before:
            Color(*HEADER_BG)
            RoundedRectangle(pos=(32, 696), size=(1216, 104), radius=[25])
        title = Label(text='TRANSILVANIA', font_size='42sp', bold=True, color=HEADER_TITLE,
                      size_hint=(1, 0.65), pos_hint={'center_x': 0.5, 'top': 1.0})
        subtitle = Label(text='Relieful de Poveste', font_size='24sp', color=HEADER_SUBTITLE,
                         size_hint=(1, 0.35), pos_hint={'center_x': 0.5, 'top': 0.4})
        header.add_widget(title)
        header.add_widget(subtitle)
        self.layout.add_widget(header)

    def create_left_sidebar(self):
        sidebar = FloatLayout(size_hint=(0.28, 0.7), pos_hint={'x': 0.02, 'center_y': 0.48})
        map_container = FloatLayout(size_hint=(1, 0.45), pos_hint={'center_x': 0.5, 'top': 1.0})
        here = os.path.dirname(__file__)
        map_path = os.path.normpath(os.path.join(here, '..', '..', 'regions', 'transilvania', 'assets', 'maps', 'transilvania.png'))
        map_image = Image(source=map_path, size_hint=(0.95, 0.95), pos_hint={'center_x': 0.5, 'center_y': 0.5},
                          allow_stretch=True, keep_ratio=True)
        map_container.add_widget(map_image)
        sidebar.add_widget(map_container)

        mascot_container = FloatLayout(size_hint=(0.9, 0.5), pos_hint={'center_x': 0.5, 'y': 0.05})
        mascot_path = os.path.normpath(os.path.join(here, '..', '..', 'regions', 'transilvania', 'assets', 'mascots', 'geo_muntii.png'))
        mascot = Image(source=mascot_path, size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.6},
                       allow_stretch=True, keep_ratio=True)
        mascot_container.add_widget(mascot)
        mascot_name = Label(text='Geo - Muntii', font_size='18sp', bold=True, color=MASCOT_NAME,
                            pos_hint={'center_x': 0.5, 'y': 0.02})
        mascot_container.add_widget(mascot_name)
        sidebar.add_widget(mascot_container)
        self.layout.add_widget(sidebar)

    def create_task_circles(self):
        positions = [
            {'center_x': 0.53, 'center_y': 0.65},
            {'center_x': 0.78, 'center_y': 0.65},
            {'center_x': 0.53, 'center_y': 0.40},
            {'center_x': 0.78, 'center_y': 0.40}
        ]
        for i, task in enumerate(self.logic.tasks):
            widget = self.create_single_task(task, positions[i])
            self.layout.add_widget(widget)

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
            here = os.path.dirname(__file__)
            play_path = os.path.normpath(os.path.join(
                here, '..', '..', 'regions', 'transilvania', 'assets', 'tasks', 'play.png'
            ))
            play_img = Image(
                source=play_path,
                size_hint=(0.5, 0.5),
                pos_hint={'center_x': 0.5, 'center_y': 0.55},
                allow_stretch=True,
                keep_ratio=True
            )
            play_img.bind(
                on_touch_down=lambda instance, touch, tid=task["id"]: self.on_play_touch(instance, touch, tid))
            container.add_widget(play_img)
        else:
            icons = {1: "M", 2: "D", 3: "C", 4: "A"}
            label_icon = Label(text=icons.get(task["id"], ""), font_size='56sp', bold=True,
                               color=(0.5, 0.5, 0.5, 1), pos_hint={'center_x': 0.5, 'center_y': 0.6})
            container.add_widget(label_icon)
            lock = Label(text="X", font_size='28sp', bold=True, color=TASK_LOCK,
                         pos_hint={'right': 0.90, 'y': 0.08})
            container.add_widget(lock)

        title = Label(
            text=task["name"],
            font_size='13sp',
            bold=True,
            color=(1, 1, 1, 1) if task["unlocked"] else TASK_LABEL_LOCKED,
            halign='center',
            valign='top',
            pos_hint={'center_x': 0.5, 'y': 0.15}
        )
        title.bind(size=title.setter("text_size"))
        container.add_widget(title)

        return container

    def create_bottom_buttons(self):
        container = FloatLayout(size_hint=(1, 0.14), pos_hint={'center_x': 0.5, 'y': 0.01})
        with container.canvas.before:
            Color(*BOTTOM_BG)
            RoundedRectangle(pos=(0, 8), size=(1280, 112), radius=[30])
        start = Button(text='INCEPE MISIUNEA!', font_size='26sp', bold=True, size_hint=(None, None),
                       size=(400, 75), pos_hint={'center_x': 0.32, 'center_y': 0.5}, background_color=START_BTN_BG,
                       color=(1, 1, 1, 1))
        start.bind(on_press=lambda x: self.logic.start_first_unlocked())
        container.add_widget(start)
        verify = Button(text='Verifica', font_size='22sp', bold=True, size_hint=(None, None), size=(170, 65),
                        pos_hint={'center_x': 0.73, 'center_y': 0.5}, background_color=VERIFY_BTN_BG, color=(1, 1, 1, 1))
        container.add_widget(verify)
        help_btn = Button(text='Ajutor!', font_size='18sp', bold=True, size_hint=(None, None), size=(130, 65),
                          pos_hint={'center_x': 0.90, 'center_y': 0.5}, background_color=HELP_BTN_BG, color=(1, 1, 1, 1))
        container.add_widget(help_btn)
        self.layout.add_widget(container)

    def start_task(self, task_id):
        screen_names = {1: 'task_1', 2: 'task_2', 3: 'task_3', 4: 'task_4'}
        if self.manager and task_id in screen_names:
            self.manager.current = screen_names[task_id]

    def unlock_next_task(self, task_id):
        self.logic.unlock_next_task(task_id)

    def show_completion_popup(self):
        self.logic.show_completion_popup()

    def on_play_touch(self, instance, touch, task_id):
        if instance.collide_point(*touch.pos):
            self.logic.select_task(task_id)