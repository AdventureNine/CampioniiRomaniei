from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty, ListProperty
from frontend.components.common import FeedbackPopup


class GenericFillScreen(Screen):
    question_text = StringProperty("")
    accepted_answers = []
    bg_image = StringProperty("")  # Important pentru fundal

    def load_data(self, data, step_number):
        self.question_text = data['question']
        self.accepted_answers = data['correct']
        if 'input_box' in self.ids:
            self.ids.input_box.text = ""

    def check_answer(self):
        input_widget = self.ids.get('input_box')
        if not input_widget: return
        user_text = input_widget.text.strip().lower()

        # Convertim răspunsurile corecte la lowercase
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