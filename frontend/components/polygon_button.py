from kivy.uix.button import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, BooleanProperty
from kivy.graphics import Color, Line


class PolygonButton(ButtonBehavior, Widget):
    relative_points = ListProperty([])
    points = ListProperty([])
    debug_mode = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(size=self.calculate_pixels, pos=self.calculate_pixels)
        self.bind(relative_points=self.calculate_pixels)

    def calculate_pixels(self, *args):
        if not self.relative_points:
            self.points = []
            return

        new_points = []
        for i in range(0, len(self.relative_points), 2):
            if i + 1 < len(self.relative_points):
                rel_x = self.relative_points[i]
                rel_y = self.relative_points[i + 1]

                abs_x = self.x + (rel_x * self.width)
                abs_y = self.y + (rel_y * self.height)
                new_points.extend([abs_x, abs_y])

        self.points = new_points
        self.draw_debug()

    def draw_debug(self, *args):
        self.canvas.after.clear()
        if self.debug_mode and len(self.points) > 4:
            with self.canvas.after:
                Color(1, 0, 0, 0.7)
                Line(points=self.points, width=2, close=True)

    def collide_point(self, x, y):
        if not self.points:
            return False

        x_list = self.points[::2]
        y_list = self.points[1::2]
        if not (min(x_list) <= x <= max(x_list) and min(y_list) <= y <= max(y_list)):
            return False

        n = len(self.points) // 2
        inside = False
        p1x, p1y = self.points[0], self.points[1]

        for i in range(n + 1):
            idx = (i % n) * 2
            p2x, p2y = self.points[idx], self.points[idx + 1]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y

        return inside