from kivy.uix.screenmanager import Screen
from kivy.app import App
from data import REGIONS_DATA
from components.cloud_transition import change_screen_with_clouds


class MapScreen(Screen):
    def open_region(self, region_id):
        app = App.get_running_app()
        region_screen = app.sm.get_screen('region')

        data = REGIONS_DATA.get(region_id, {"name": "Necunoscut", "mission": "..."})
        region_screen.region_id = region_id
        region_screen.region_name = data["name"]
        region_screen.mission_description = data["mission"]

        change_screen_with_clouds(app, 'region')

    def go_back(self):
        app = App.get_running_app()
        change_screen_with_clouds(app, 'menu')