from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang import Builder

from components.cloud_transition import CloudTransitionLayout
from screens.menu import MenuScreen
from screens.map import MapScreen
from screens.region import RegionScreen
from screens.exercise import ExerciseScreen

Window.size = (1280, 800)


class DidacticApp(App):
    credit = NumericProperty(0)

    def build(self):
        # 1. Incarcam fisierele de design (.kv)
        Builder.load_file('components/common.kv')
        Builder.load_file('components/cloud_transition.kv')

        Builder.load_file('screens/menu.kv')
        Builder.load_file('screens/map.kv')
        Builder.load_file('screens/region.kv')
        Builder.load_file('screens/exercise.kv')

        # 2. Configurare Layout Principal
        self.root_layout = FloatLayout()

        # 3. Managerul de ecrane
        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(MapScreen(name='map'))
        self.sm.add_widget(RegionScreen(name='region'))
        self.sm.add_widget(ExerciseScreen(name='exercise'))

        # 4. Stratul de nori (deasupra)
        self.clouds = CloudTransitionLayout()

        self.root_layout.add_widget(self.sm)
        self.root_layout.add_widget(self.clouds)

        return self.root_layout


if __name__ == '__main__':
    DidacticApp().run()