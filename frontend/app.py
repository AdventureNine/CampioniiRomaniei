from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from frontend.regions.transilvania.transilvania_region import TransilvaniaRegionScreen

Window.size = (1280, 800)

class CampioniiRomanieiApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TransilvaniaRegionScreen())
        sm.current = 'transilvania'

        return sm

if __name__ == '__main__':
    CampioniiRomanieiApp().run()