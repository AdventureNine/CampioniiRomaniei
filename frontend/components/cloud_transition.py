from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.app import App


class CloudTransitionLayout(FloatLayout):

    def change_screen(self, next_screen_name):
        app = App.get_running_app()
        sm = app.sm

        if not sm.has_screen(next_screen_name):
            print(f"Eroare: Ecranul '{next_screen_name}' nu există!")
            return

        anim_duration = 0.7

        center_x = (Window.width / 2) - 500
        center_y = (Window.height / 2) - 500

        targets_in = {
            'c_top': {'y': center_y + 100},
            'c_bottom': {'y': center_y - 100},
            'c_left': {'x': center_x - 150},
            'c_right': {'x': center_x + 150},
            'c_tl': {'pos': (center_x - 100, center_y + 100)},
            'c_tr': {'pos': (center_x + 100, center_y + 100)},
            'c_bl': {'pos': (center_x - 100, center_y - 100)},
            'c_br': {'pos': (center_x + 100, center_y - 100)},
        }

        for cloud_id, props in targets_in.items():
            cloud = self.ids[cloud_id]
            anim = Animation(**props, duration=anim_duration, t='out_cubic')
            anim.start(cloud)

        Clock.schedule_once(lambda dt: self._perform_switch(sm, next_screen_name), anim_duration)

    def _perform_switch(self, sm, screen_name):
        sm.current = screen_name
        anim_duration = 0.6

        targets_out = {
            'c_top': {'y': Window.height},
            'c_bottom': {'y': -1000},
            'c_left': {'x': -1000},
            'c_right': {'x': Window.width},
            'c_tl': {'pos': (-1000, Window.height)},
            'c_tr': {'pos': (Window.width, Window.height)},
            'c_bl': {'pos': (-1000, -1000)},
            'c_br': {'pos': (Window.width, -1000)},
        }

        for cloud_id, props in targets_out.items():
            cloud = self.ids[cloud_id]
            anim = Animation(**props, duration=anim_duration, t='in_cubic')
            anim.start(cloud)