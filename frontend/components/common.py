from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty, OptionProperty, NumericProperty, ColorProperty
from kivy.app import App

from frontend.utils.assets import image_path
from frontend.utils.colors import AppColors


# --- WIDGET SCOR ---
class ScoreDisplay(BoxLayout):
    coin_image = image_path(f"ui/coin.png")

# --- WIDGET TIMER ---
class TimerDisplay(BoxLayout):
    timer_image = image_path("ui/timer.png")

# --- POPUP FEEDBACK ---
class FeedbackPopup(ModalView):
    title_text = StringProperty("Info")
    message_text = StringProperty("Mesaj")
    button_text = StringProperty("Ok")
    type = OptionProperty('info', options=['success', 'fail', 'info', 'level_complete'])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.6, 0.5)
        self.auto_dismiss = True
        self.background_color = (0, 0, 0, 0.7)


# --- BUTON RĂSPUNS QUIZ ---
class AnswerButton(Button):
    pass

class StandardHeader(BoxLayout):
    title = StringProperty("Titlu")
    show_back_button = OptionProperty(True, options=[True, False])
    back_screen = StringProperty('menu')
    back_image = image_path(f"ui/back.png")

    # Proprietate nouă
    header_color = ColorProperty(AppColors.PRIMARY)