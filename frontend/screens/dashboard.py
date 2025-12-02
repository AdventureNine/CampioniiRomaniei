from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp


class MeniuPrincipal(MDScreen):
    def exit_app(self):
        MDApp.get_running_app().stop()