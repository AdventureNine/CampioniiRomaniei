from kivy.uix.screenmanager import Screen
from kivy.app import App

class MenuScreen(Screen):
    def go_to_map(self):
        app = App.get_running_app()
        if hasattr(app, 'change_screen_with_clouds'):
            app.change_screen_with_clouds('map')
        else:
            app.sm.current = 'map'