from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import NumericProperty, StringProperty, ListProperty
from data import REGIONS_DATA, USER_PROGRESS  
from components.cloud_transition import change_screen_with_clouds


class RegionScreen(Screen):
    region_id = NumericProperty(0)
    region_name = StringProperty("Regiune")
    mission_description = StringProperty("Descriere Misiune")

    levels_unlocked = ListProperty([True, False, False, False, False, False])

    def on_pre_enter(self, *args):
        if self.region_id in USER_PROGRESS:
            self.levels_unlocked = USER_PROGRESS[self.region_id]

    def start_exercise(self, level_number):
        app = App.get_running_app()
        exercise_screen = app.sm.get_screen('exercise')

        exercise_screen.level_id = level_number
        exercise_screen.region_id_ref = self.region_id

        region_info = REGIONS_DATA.get(self.region_id, {})
        exercise_screen.exercise_title = f"{region_info.get('name', 'Joc')} - Etapa {level_number}"
        exercise_screen.exercise_content = f"Sarcina: {region_info.get('mission')}\n\nRezolvă task-ul numărul {level_number}!"

        change_screen_with_clouds(app, 'exercise')

    def unlock_next_level(self, current_level_completed):
        if current_level_completed < 6:
            self.levels_unlocked[current_level_completed] = True

            USER_PROGRESS[self.region_id] = self.levels_unlocked

    def go_back(self):
        app = App.get_running_app()
        change_screen_with_clouds(app, 'map')