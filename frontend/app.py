import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.config import Config
from kivy.lang import Builder

from frontend.screens.transilvania.tasks.task_factory import create_task_screen
from frontend.screens.transilvania.transilvania_screen import TransilvaniaRegionScreen
from frontend.regions.transilvania import colors

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '800')

Window.size = (1280, 800)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
Builder.load_file(os.path.join(BASE_DIR, 'screens', 'transilvania', 'transilvania_screen.kv'))
Builder.load_file(os.path.join(BASE_DIR, 'screens', 'transilvania', 'tasks', 'task_screen_base.kv'))


class CampioniiRomanieiApp(App):
    def build(self):
        self.title = 'Campionii Romaniei'
        Window.bind(on_resize=self.prevent_resize)

        sm = ScreenManager()
        sm.add_widget(TransilvaniaRegionScreen())

        for task_num in range(1, 7):
            sm.add_widget(create_task_screen(task_num))
        sm.current = 'transilvania'
        return sm

    def prevent_resize(self, instance, width, height):
        if width != 1280 or height != 800:
            Window.size = (1280, 800)
        return True

    def get_color(self, color_name):
        return getattr(colors, color_name, (1, 1, 1, 1))


if __name__ == '__main__':
    CampioniiRomanieiApp().run()