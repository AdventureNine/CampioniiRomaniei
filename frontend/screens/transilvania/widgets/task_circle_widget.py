from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty, BooleanProperty, StringProperty


class TaskCircleWidget(FloatLayout):
    # Proprietati
    task_color = ListProperty([1, 1, 1, 1])
    is_unlocked = BooleanProperty(False)
    task_name = StringProperty('')
    task_id = StringProperty('')
    play_button_source = StringProperty('')
    is_hovered = BooleanProperty(False)

    # Gestionare hover
    def on_touch_move(self, touch):
        # Detecteaza hover cand mouse-ul se misca
        if self.is_unlocked and self.collide_point(*touch.pos):
            self.is_hovered = True
        else:
            self.is_hovered = False
        return super().on_touch_move(touch)

    def on_mouse_pos(self, *args):
        # Detecteaza hover cand mouse-ul se misca pe fereastra
        if not self.get_root_window():
            return

        pos = self.to_widget(*self.get_root_window().mouse_pos)
        if self.is_unlocked:
            self.is_hovered = self.collide_point(*pos)
        else:
            self.is_hovered = False