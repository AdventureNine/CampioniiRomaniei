from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window

from frontend.regions.transilvania.transilvania import Transilvania
from frontend.config.paths import TRANSILVANIA_MAP, TRANSILVANIA_MASCOT, TRANSILVANIA_PLAY_BUTTON
from frontend.screens.transilvania.widgets.task_circle_widget import TaskCircleWidget


class TransilvaniaRegionScreen(Screen):
    # Proprietati
    logic = ObjectProperty(None)
    map_source = StringProperty('')
    mascot_source = StringProperty('')

    def __init__(self, **kwargs):
        self.name = "transilvania"
        self.logic = Transilvania(self)
        self.task_widgets = []
        self.map_source = TRANSILVANIA_MAP
        self.mascot_source = TRANSILVANIA_MASCOT
        super().__init__(**kwargs)

    def on_kv_post(self, base_widget):
        # Apelat dupa incarcarea layout-ului KV
        self.create_task_circles()

    # Creare task-uri
    def create_task_circles(self):
        # Creeaza si adauga toate widget-urile
        main_layout = self.children[0]
        for i, task in enumerate(self.logic.tasks):
            widget = self.create_single_task(task, self.logic.TASK_POSITIONS[i])
            main_layout.add_widget(widget)
            self.task_widgets.append(widget)

    def create_single_task(self, task, position):
        # Creeaza un widget de task cu configuratiile necesare
        container = TaskCircleWidget(
            pos_hint=position,
            task_color=task["color"],
            is_unlocked=task["unlocked"],
            task_name=task["name"],
            task_id=str(task["id"]),
            play_button_source=TRANSILVANIA_PLAY_BUTTON
        )

        # Bind pentru hover
        Window.bind(mouse_pos=container.on_mouse_pos)

        # Gaseste butonul si face bind pentru start
        for child in container.walk():
            if isinstance(child, Button) and child.background_color == [0, 0, 0, 0]:
                child.bind(on_press=lambda x, tid=task["id"]: self.start_task(tid))
                break

        return container

    # Gestionare task-uri
    def start_task(self, task_id):
        # Navigheza la ecranul task-ului
        screen_name = self.logic.get_screen_name(task_id)
        if self.manager and screen_name:
            self.manager.current = screen_name

    def unlock_next_task(self, task_id):
        # Deblocheaza urmatorul task
        self.logic.unlock_next_task(task_id)
        self.refresh_tasks()

    def refresh_tasks(self):
        # Actualizeaza toate widget-urile
        main_layout = self.children[0]
        for widget in self.task_widgets:
            main_layout.remove_widget(widget)
        self.task_widgets.clear()
        self.create_task_circles()

    def show_completion_popup(self):
        # Afiseaza popup de completare
        self.logic.show_completion_popup()
