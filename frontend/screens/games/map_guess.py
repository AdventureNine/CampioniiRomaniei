import math
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivy.uix.image import Image
from frontend.components.common import FeedbackPopup
from frontend.utils.assets import image_path


class PinWidget(Image):
    def __init__(self, color_type='red', **kwargs):
        super().__init__(**kwargs)
        self.source = image_path(f"games/map_guess/pin_{color_type}.png")
        self.size_hint = (None, None)
        self.size = (40, 40)
        self.fit_mode = "contain"


class MapGuessScreen(Screen):
    main_question = StringProperty("...")
    current_target_text = StringProperty("...")

    bg_image = StringProperty("")
    map_container = ObjectProperty(None)

    targets_list = []
    current_index = 0

    target_x = 0
    target_y = 0
    tolerance = 0.05

    debug_mode = BooleanProperty(False)

    def load_data(self, data, step_number):
        self.map_container.clear_widgets()

        self.main_question = data.get('question', "Găsește locațiile:")
        self.targets_list = data.get('targets', [])

        img_name = data.get('images', 'games/map_guess/harta_map_guess.png')
        self.bg_image = image_path(img_name)

        self.current_index = 0
        self.load_current_target()

    def on_map_touch(self, touch):
        map_widget = self.ids.map_area
        if not map_widget.collide_point(*touch.pos):
            return

        rel_x = (touch.x - map_widget.x) / map_widget.width
        rel_y = (touch.y - map_widget.y) / map_widget.height

        if self.debug_mode:
            self.place_pin(rel_x, rel_y, 'red')

            print(f'\n--- COORDONATE PENTRU COPY-PASTE ---')
            print(f'"x": {rel_x:.3f}, "y": {rel_y:.3f},')
            print(f'------------------------------------\n')

            return

        dist = math.sqrt((rel_x - self.target_x) ** 2 + (rel_y - self.target_y) ** 2)

        if dist <= self.tolerance:
            self.place_pin(rel_x, rel_y, 'green')
            self.show_feedback(True)
        else:
            self.place_pin(rel_x, rel_y, 'red')
            self.show_feedback(False)

    def load_current_target(self):
        if self.current_index < len(self.targets_list):
            t = self.targets_list[self.current_index]
            self.current_target_text = f"{self.current_index + 1}. {t['name']}"
            self.target_x = t['x']
            self.target_y = t['y']
            self.tolerance = t.get('tolerance', 0.1)

            self.map_container.clear_widgets()
        else:
            self.finish_game()

    def on_map_touch(self, touch):
        map_widget = self.ids.map_area
        if not map_widget.collide_point(*touch.pos):
            return

        rel_x = (touch.x - map_widget.x) / map_widget.width
        rel_y = (touch.y - map_widget.y) / map_widget.height

        dist = math.sqrt((rel_x - self.target_x) ** 2 + (rel_y - self.target_y) ** 2)

        if dist <= self.tolerance:
            self.place_pin(rel_x, rel_y, 'green')
            self.show_feedback(True)
        else:
            self.place_pin(rel_x, rel_y, 'red')
            self.show_feedback(False)

    def place_pin(self, x_pct, y_pct, color):
        pin = PinWidget(color_type=color)
        map_widget = self.ids.map_area
        pos_x = map_widget.x + (x_pct * map_widget.width)
        pos_y = map_widget.y + (y_pct * map_widget.height)
        pin.pos = (pos_x - pin.width / 2, pos_y)
        self.map_container.add_widget(pin)

    def show_feedback(self, success):
        if success:
            popup = FeedbackPopup(
                type='success',
                title_text="Bravo!",
                message_text="Ai găsit locația!",
                button_text="Următoarea"
            )
            popup.bind(on_dismiss=self.next_target)
        else:
            popup = FeedbackPopup(
                type='fail',
                title_text="Mai încearcă",
                message_text="Nu e chiar acolo. Caută mai atent!",
                button_text="Ok"
            )

        popup.open()

    def next_target(self, instance):
        self.current_index += 1
        self.load_current_target()

    def finish_game(self):
        app = App.get_running_app()
        dashboard = app.sm.get_screen('region_dashboard')
        dashboard.load_next_step()