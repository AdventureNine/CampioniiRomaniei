from kivy.uix.label import Label
from kivy.uix.button import Button


class Transilvania:

    def __init__(self, ui_screen):
        self.ui = ui_screen
        self.selected_task_id = None
        self.tasks = [
            {'id': 1, 'name': 'Muntii', 'unlocked': True, 'color': (0.25, 0.55, 0.35, 1)},
            {'id': 2, 'name': 'Dealuri si\nPodisuri', 'unlocked': False, 'color': (0.60, 0.85, 0.55, 1)},
            {'id': 3, 'name': 'Campuri\nsi Vai', 'unlocked': False, 'color': (0.55, 0.90, 0.55, 1)},
            {'id': 4, 'name': 'Agricultura', 'unlocked': False, 'color': (0.65, 0.85, 0.50, 1)},
        ]

    def select_task(self, task_id):
        self.selected_task_id = task_id
        self.ui.setup_ui()

    def start_task(self, task_number):
        self.ui.start_task(task_number)

    def unlock_next_task(self, completed_task_id):
        for t in self.tasks:
            if t["id"] == completed_task_id + 1:
                t["unlocked"] = True
                self.selected_task_id = t["id"]
        self.ui.setup_ui()

    def start_first_unlocked(self):
        if not self.selected_task_id:
            for t in self.tasks:
                if t["unlocked"]:
                    self.selected_task_id = t["id"]
                    break
        if self.selected_task_id:
            self.ui.start_task(self.selected_task_id)

    def show_completion_popup(self):
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.popup import Popup
        box = BoxLayout(orientation='vertical', padding=20, spacing=20)
        message = Label(text="Felicitări!\n\nAi terminat toate misiunile din Transilvania!",
                        font_size="26sp", halign="center", valign="middle")
        close_btn = Button(text="Înapoi la regiuni", size_hint=(1, 0.4), font_size="20sp", bold=True)
        close_btn.bind(on_press=lambda x: self.close_popup())
        box.add_widget(message)
        box.add_widget(close_btn)
        self.popup = Popup(title="Misiune Finalizată", content=box, size_hint=(0.55, 0.55), auto_dismiss=False)
        self.popup.open()

    def close_popup(self):
        self.popup.dismiss()
        self.ui.manager.current = "transilvania"
