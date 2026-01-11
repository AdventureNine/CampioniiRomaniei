from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty, ListProperty
from frontend.components.common import FeedbackPopup

class GenericQuizScreen(Screen):
    question_text = StringProperty("Încărcare...")
    options = ListProperty(["", "", "", ""])
    correct_answer = ""
    bg_image = StringProperty("") # Important pentru fundal

    def load_data(self, data, step_number):
        self.question_text = data['question']
        self.options = data['options']
        self.correct_answer = data['correct']

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