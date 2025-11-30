from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.config import Config
from frontend.regions.transilvania.transilvania_region import TransilvaniaRegionScreen
from frontend.regions.transilvania.quizzes.task_1 import Task1Screen
from frontend.regions.transilvania.quizzes.task_2 import Task2Screen
from frontend.regions.transilvania.quizzes.task_3 import Task3Screen
from frontend.regions.transilvania.quizzes.task_4 import Task4Screen

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '800')

Window.size = (1280, 800)

class CampioniiRomanieiApp(App):
    def build(self):
        self.title = 'Campionii Romaniei'

        Window.bind(on_resize=self.prevent_resize)

        sm = ScreenManager()
        sm.add_widget(TransilvaniaRegionScreen())
        sm.add_widget(Task1Screen())
        sm.add_widget(Task2Screen())
        sm.add_widget(Task3Screen())
        sm.add_widget(Task4Screen())
        sm.current = 'transilvania'
        return sm

    def prevent_resize(self, instance, width, height):
        if width != 1280 or height != 800:
            Window.size = (1280, 800)
        return True


if __name__ == '__main__':
    CampioniiRomanieiApp().run()