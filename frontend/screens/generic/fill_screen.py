from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty, NumericProperty, ColorProperty
from frontend.components.common import FeedbackPopup
from frontend.utils.colors import AppColors
from frontend.utils.assets import image_path


class GenericFillScreen(Screen):
    question_text = StringProperty("")
    accepted_answers = []
    bg_image = StringProperty("")

    region_id = NumericProperty(0)
    primary_color = ColorProperty(AppColors.ACCENT)
    question_bg_image = StringProperty("")

    def load_data(self, data, step_number):
        self.question_text = data['question']
        self.accepted_answers = data['correct']

        if 'input_box' in self.ids:
            self.ids.input_box.text = ""

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

    def check_answer(self):
        input_widget = self.ids.get('input_box')
        if not input_widget: return
        user_text = input_widget.text.strip().lower()

        valid_answers = [ans.lower() for ans in self.accepted_answers]

        if user_text in valid_answers:
            popup = FeedbackPopup(type='success', title_text="Corect!", button_text="Continuă")
            popup.bind(on_dismiss=self.go_next)
            popup.open()
        else:
            popup = FeedbackPopup(type='fail', message_text="Verifică ortografia.")
            popup.open()

    def go_next(self, instance):
        app = App.get_running_app()
        dashboard = app.sm.get_screen('region_dashboard')
        dashboard.load_next_step()