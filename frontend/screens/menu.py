from kivy.uix.screenmanager import Screen
from kivy.app import App
from components.cloud_transition import change_screen_with_clouds

class MenuScreen(Screen):
    def go_to_map(self):
        app = App.get_running_app()
        change_screen_with_clouds(app, 'map')