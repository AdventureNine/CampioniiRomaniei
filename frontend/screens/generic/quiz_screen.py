from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty, ListProperty, NumericProperty, ColorProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from frontend.components.common import FeedbackPopup
from frontend.utils.colors import AppColors
from frontend.utils.assets import image_path

class QuizAnswerButton(ButtonBehavior, Label):
    btn_color = ColorProperty([0, 0, 0, 1])

class GenericQuizScreen(Screen):
    question_text = StringProperty("Încărcare...")
    options = ListProperty(["", "", "", ""])
    correct_answer = ""
    bg_image = StringProperty("")

    region_id = NumericProperty(0)
    primary_color = ColorProperty(AppColors.ACCENT)
    question_bg_image = StringProperty("")

    def load_data(self, data, step_number):
        self.question_text = data['question']
        self.options = data['options']
        self.correct_answer = data['correct']

        try:
            self.question_bg_image = image_path("ui/question_box.png")
        except:
            self.question_bg_image = ""

        self.set_theme_color()

    def set_theme_color(self):
        colors_map = {
            1: AppColors.TRANSILVANIA,
            2: AppColors.MOLDOVA,
            3: AppColors.TARA_ROMANEASCA,
            4: AppColors.DOBROGEA,
            5: AppColors.BANAT
        }
        self.primary_color = colors_map.get(self.region_id, AppColors.ACCENT)

    def check_answer(self, selected_text):
        if selected_text == self.correct_answer:
            popup = FeedbackPopup(
                type='success', title_text="Bravo!", message_text="Răspuns corect!", button_text="Continuă"
            )
            popup.bind(on_dismiss=self.go_next)
            popup.open()
        else:
            popup = FeedbackPopup(
                type='fail', title_text="Greșit", message_text="Mai încearcă o dată.", button_text="Ok"
            )
            popup.open()

    def go_next(self, instance):
        app = App.get_running_app()
        dashboard = app.sm.get_screen('region_dashboard')
        dashboard.load_next_step()