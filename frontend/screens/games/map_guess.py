import math
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty, ColorProperty, NumericProperty
from kivy.uix.image import Image

from backend.domain.entities.Minigame import MapGuesser
from frontend.components.common import FeedbackPopup
from frontend.utils.assets import image_path
from frontend.utils.colors import AppColors


class PinWidget(Image):
    def __init__(self, color_type='red', **kwargs):
        super().__init__(**kwargs)
        self.source = image_path(f"games/map_guess/pin_{color_type}.png")
        self.size_hint = (None, None)
        self.size = ("40dp", "40dp")
        self.fit_mode = "contain"


class MapGuessScreen(Screen):
    map_container = ObjectProperty(None)
    is_completed = BooleanProperty(False)

    bg_image = StringProperty('')
    map_image = StringProperty('')
    main_question = StringProperty("...")
    current_target_text = StringProperty("...")

    primary_color = ColorProperty(AppColors.ACCENT)
    header_color = ColorProperty(AppColors.PRIMARY)
    region_id = NumericProperty(0)

    targets_list = []
    current_index = 0
    target_x = 0
    target_y = 0
    tolerance = 0.1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.targets_list = []

    def set_theme_color(self):
        colors_map = {
            1: AppColors.TRANSILVANIA,
            2: AppColors.MOLDOVA,
            3: AppColors.TARA_ROMANEASCA,
            4: AppColors.DOBROGEA,
            5: AppColors.BANAT
        }
        color = colors_map.get(self.region_id, AppColors.PRIMARY)
        self.primary_color = color
        self.header_color = color

    def load_data(self, data, step_number):
        if self.map_container:
            self.map_container.clear_widgets()
        self.is_completed = False
        self.main_question = "Găsește locațiile:"
        self.map_image = ""
        self.region_id = self.region_id

        map_entity = data.get('map_guesser')

        if not map_entity or not isinstance(map_entity, MapGuesser):
            print("Eroare: Nu s-au găsit date valide pentru MapGuesser.")
            return

        self.map_guesser_entity = map_entity

        config = self.map_guesser_entity.get_win_configuration()
        self.targets_list = []

        if config:
            for name, coords in config.items():
                self.targets_list.append({
                    'name': name,
                    'x': float(coords[0]),
                    'y': float(coords[1]),
                    'tolerance': 0.1
                })

        self.map_image = image_path("games/map_guess/harta_map_guess.png")

        self.set_theme_color()

        self.current_index = 0
        self.load_current_target()

    def load_current_target(self):
        if self.current_index < len(self.targets_list):
            t = self.targets_list[self.current_index]
            self.current_target_text = f"{self.current_index + 1}. {t['name']}"
            self.target_x = t['x']
            self.target_y = t['y']
            self.tolerance = t.get('tolerance', 0.05)

            if self.map_container:
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
        if not self.map_container:
            return

        pin = PinWidget(color_type=color)
        pin.pos_hint = {'center_x': x_pct, 'y': y_pct}
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
        self.is_completed = True
        app = App.get_running_app()
        dashboard = app.sm.get_screen('region_dashboard')
        dashboard.load_next_step()