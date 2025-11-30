from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, Ellipse, RoundedRectangle, Line
from frontend.regions.transilvania.colors import REGION_BG, HEADER_BG, HEADER_TITLE, HEADER_SUBTITLE, MAP_BG1, MAP_BG2, MAP_LABEL, MASCOT, MASCOT_NAME, TASK_CIRCLE_SHADOW, TASK_CIRCLE_LOCKED, TASK_CIRCLE_LINE, TASK_ICON_UNLOCKED, TASK_ICON_LOCKED, TASK_LABEL_UNLOCKED, TASK_LABEL_LOCKED, TASK_STAR, TASK_LOCK, BOTTOM_BG, START_BTN_BG, VERIFY_BTN_BG, HELP_BTN_BG


class TransilvaniaRegionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'transilvania'
        self.selected_task = None

        self.tasks_data = [
            {'id': 1, 'name': 'Muntii', 'unlocked': True, 'color': (0.25, 0.55, 0.35, 1)},
            {'id': 2, 'name': 'Dealuri si\nPodisuri', 'unlocked': False, 'color': (0.60, 0.85, 0.55, 1)},
            {'id': 3, 'name': 'Campuri\nsi Vai', 'unlocked': False, 'color': (0.55, 0.90, 0.55, 1)},
            {'id': 4, 'name': 'Agricultura', 'unlocked': False, 'color': (0.65, 0.85, 0.50, 1)},
        ]

        self.layout = FloatLayout()
        self.setup_ui()
        self.add_widget(self.layout)

    def setup_ui(self):
        with self.layout.canvas.before:
            Color(*REGION_BG)
            Rectangle(size=(1280, 800), pos=(0, 0))

        self.create_header()
        self.create_left_sidebar()
        self.create_task_circles()
        self.create_bottom_buttons()

    def create_header(self):
        header = FloatLayout(
            size_hint=(0.95, 0.13),
            pos_hint={'center_x': 0.5, 'top': 0.99}
        )

        with header.canvas.before:
            Color(*HEADER_BG)
            header_bg = RoundedRectangle(
                pos=(32, 696),
                size=(1216, 104),
                radius=[25]
            )

        title = Label(
            text='TRANSILVANIA',
            font_size='42sp',
            bold=True,
            color=HEADER_TITLE,
            size_hint=(1, 0.65),
            pos_hint={'center_x': 0.5, 'top': 1.0}
        )
        header.add_widget(title)

        subtitle = Label(
            text='Relieful de Poveste',
            font_size='24sp',
            color=HEADER_SUBTITLE,
            size_hint=(1, 0.35),
            pos_hint={'center_x': 0.5, 'top': 0.4}
        )
        header.add_widget(subtitle)

        self.layout.add_widget(header)

    def create_left_sidebar(self):
        sidebar = FloatLayout(
            size_hint=(0.28, 0.7),
            pos_hint={'x': 0.02, 'center_y': 0.48}
        )

        map_container = FloatLayout(
            size_hint=(1, 0.45),
            pos_hint={'center_x': 0.5, 'top': 1.0}
        )

        with map_container.canvas:
            Color(*MAP_BG1)
            RoundedRectangle(pos=(46, 390), size=(220, 180), radius=[15])
            Color(*MAP_BG2)
            RoundedRectangle(pos=(51, 395), size=(210, 170), radius=[12])

        map_label = Label(
            text='[Harta\nTransilvania]',
            font_size='15sp',
            color=MAP_LABEL,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        map_container.add_widget(map_label)
        sidebar.add_widget(map_container)

        mascot_container = FloatLayout(
            size_hint=(0.9, 0.5),
            pos_hint={'center_x': 0.5, 'y': 0.05}
        )

        mascot = Label(
            text='M',
            font_size='72sp',
            bold=True,
            color=MASCOT,
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        mascot_container.add_widget(mascot)

        mascot_name = Label(
            text='Geo - Muntii',
            font_size='18sp',
            bold=True,
            color=MASCOT_NAME,
            pos_hint={'center_x': 0.5, 'y': 0.15}
        )
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

        for i, task_data in enumerate(self.tasks_data):
            task = self.create_single_task(task_data, positions[i])
            self.layout.add_widget(task)

    def create_single_task(self, task_data, position):
        container = FloatLayout(
            size_hint=(None, None),
            size=(170, 170),
            pos_hint=position
        )

        with container.canvas.before:
            Color(*TASK_CIRCLE_SHADOW)
            Ellipse(pos=(8, 6), size=(164, 164))

            if task_data['unlocked']:
                Color(*task_data['color'])
            else:
                Color(*TASK_CIRCLE_LOCKED)

            Ellipse(pos=(10, 10), size=(150, 150))

            Color(*TASK_CIRCLE_LINE)
            Line(ellipse=(10, 10, 150, 150), width=5)

        task_icons = {
            1: 'M',
            2: 'D',
            3: 'C',
            4: 'A',
        }

        icon = Label(
            text=task_icons.get(task_data['id'], ''),
            font_size='56sp',
            bold=True,
            color=TASK_ICON_UNLOCKED if task_data['unlocked'] else TASK_ICON_LOCKED,
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        container.add_widget(icon)

        label = Label(
            text=task_data['name'],
            font_size='13sp',
            bold=True,
            color=TASK_LABEL_UNLOCKED if task_data['unlocked'] else TASK_LABEL_LOCKED,
            halign='center',
            valign='top',
            pos_hint={'center_x': 0.5, 'y': 0.15}
        )
        label.bind(size=label.setter('text_size'))
        container.add_widget(label)

        if task_data['id'] == 1 and task_data['unlocked']:
            star = Label(
                text='*',
                font_size='38sp',
                bold=True,
                color=TASK_STAR,
                pos_hint={'right': 0.95, 'top': 0.95}
            )
            container.add_widget(star)

        if not task_data['unlocked']:
            lock = Label(
                text='X',
                font_size='28sp',
                bold=True,
                color=TASK_LOCK,
                pos_hint={'right': 0.90, 'y': 0.08}
            )
            container.add_widget(lock)

        if task_data['unlocked']:
            if self.selected_task == task_data['id']:
                r, g, b, a = task_data['color']
                Color(r + 0.15, g + 0.15, b + 0.15, 1)
            else:
                Color(*task_data['color'])

        return container

    def create_bottom_buttons(self):
        container = FloatLayout(
            size_hint=(1, 0.14),
            pos_hint={'center_x': 0.5, 'y': 0.01}
        )

        with container.canvas.before:
            Color(*BOTTOM_BG)
            RoundedRectangle(pos=(0, 8), size=(1280, 112), radius=[30])

        start = Button(
            text='INCEPE MISIUNEA!',
            font_size='26sp',
            bold=True,
            size_hint=(None, None),
            size=(400, 75),
            pos_hint={'center_x': 0.32, 'center_y': 0.5},
            background_color=START_BTN_BG,
            color=(1, 1, 1, 1)
        )
        start.bind(on_press=lambda x: self.start_first_unlocked())
        container.add_widget(start)

        verify = Button(
            text='Verifica',
            font_size='22sp',
            bold=True,
            size_hint=(None, None),
            size=(170, 65),
            pos_hint={'center_x': 0.73, 'center_y': 0.5},
            background_color=VERIFY_BTN_BG,
            color=(1, 1, 1, 1)
        )
        container.add_widget(verify)

        help_btn = Button(
            text='Ajutor!',
            font_size='18sp',
            bold=True,
            size_hint=(None, None),
            size=(130, 65),
            pos_hint={'center_x': 0.90, 'center_y': 0.5},
            background_color=HELP_BTN_BG,
            color=(1, 1, 1, 1)
        )
        container.add_widget(help_btn)

        self.layout.add_widget(container)

    def select_task(self, task_id):
        self.selected_task = task_id
        self.layout.clear_widgets()
        self.setup_ui()

    def start_task(self, task_number):
        screen_names = {1: 'task_1', 2: 'task_2', 3: 'task_3', 4: 'task_4'}
        if self.manager and task_number in screen_names:
            self.manager.current = screen_names[task_number]

    def unlock_next_task(self, completed_task_id):
        for t in self.tasks_data:
            if t["id"] == completed_task_id + 1:
                t["unlocked"] = True

        self.layout.clear_widgets()
        self.setup_ui()

    def start_first_unlocked(self):
        if self.selected_task:
            self.start_task(self.selected_task)
            return

        for t in self.tasks_data:
            if t["unlocked"]:
                self.start_task(t["id"])
                break
