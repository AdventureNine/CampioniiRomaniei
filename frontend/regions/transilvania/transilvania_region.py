from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class TransilvaniaRegionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'transilvania'

        layout = FloatLayout()

        title_bar_height = 100

        with layout.canvas.before:
            Color(0.2, 0.5, 0.2, 1)
            Rectangle(size=(Window.size[0], title_bar_height), pos=(0, Window.size[1] - title_bar_height))

        title = Label(
            text='TRANSILVANIA\nRelieful de Poveste',
            font_size='40sp',
            bold=True,
            halign='center',
            valign='middle',
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(Window.size[0], title_bar_height),
            pos=(0, Window.size[1] - title_bar_height)
        )

        title.bind(size=title.setter('text_size'))
        layout.add_widget(title)

        self.add_widget(layout)

