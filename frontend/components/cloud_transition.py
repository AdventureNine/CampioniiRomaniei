from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.clock import Clock

class CloudTransitionLayout(FloatLayout):
    pass


def change_screen_with_clouds(app_instance, next_screen_name):
    clouds = app_instance.clouds
    sm = app_instance.sm

    left_cloud = clouds.ids.left_cloud
    right_cloud = clouds.ids.right_cloud

    anim_duration = 0.6

    anim_in = Animation(x=0, duration=anim_duration, t='out_cubic')
    anim_in_right = Animation(x=Window.width - right_cloud.width, duration=anim_duration, t='out_cubic')

    anim_in.start(left_cloud)
    anim_in_right.start(right_cloud)

    Clock.schedule_once(lambda dt: _switch_screen_internal(sm, clouds, next_screen_name), anim_duration)


def _switch_screen_internal(sm, clouds, screen_name):
    sm.current = screen_name

    left_cloud = clouds.ids.left_cloud
    right_cloud = clouds.ids.right_cloud

    anim_out = Animation(x=-left_cloud.width, duration=0.6, t='in_cubic')
    anim_out_right = Animation(x=Window.width, duration=0.6, t='in_cubic')

    anim_out.start(left_cloud)
    anim_out_right.start(right_cloud)