from frontend.utils.popup_helper import create_completion_popup


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

    def start_task(self, task_number):
        self.ui.start_task(task_number)

    def unlock_next_task(self, completed_task_id):
        for task in self.tasks:
            if task["id"] == completed_task_id + 1:
                task["unlocked"] = True
                self.selected_task_id = task["id"]
                break

    def start_first_unlocked(self):
        if not self.selected_task_id:
            for task in self.tasks:
                if task["unlocked"]:
                    self.selected_task_id = task["id"]
                    break

        if self.selected_task_id:
            self.ui.start_task(self.selected_task_id)

    def show_completion_popup(self):
        def on_close():
            self.ui.manager.current = "transilvania"

        popup = create_completion_popup(
            message="Felicitări!\n\nAi terminat toate misiunile din Transilvania!",
            button_text="Înapoi la regiuni",
            on_close=on_close
        )
        popup.open()


