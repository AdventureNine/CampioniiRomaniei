from kivy.uix.screenmanager import Screen
from kivy.app import App
from frontend.data.game_data import REGIONS_DATA


class MapScreen(Screen):
    def open_region(self, region_id):
        app = App.get_running_app()

        # Preluăm datele regiunii selectate
        data = REGIONS_DATA.get(region_id)
        if not data:
            print(f"Eroare: Regiunea {region_id} nu există în game_data.py")
            return

        print(f"Navigare către: {data['name']}")

        dashboard = app.sm.get_screen('region_dashboard')
        dashboard.region_id = region_id

        # Declanșăm tranziția
        app.clouds.change_screen('region_dashboard')