from frontend.utils.popup_helper import create_completion_popup


class Transilvania:
    TASK_POSITIONS = [
        {'center_x': 0.53, 'center_y': 0.75},
        {'center_x': 0.78, 'center_y': 0.75},
        {'center_x': 0.53, 'center_y': 0.50},
        {'center_x': 0.78, 'center_y': 0.50},
        {'center_x': 0.53, 'center_y': 0.25},
        {'center_x': 0.78, 'center_y': 0.25}
    ]

    TASK_ICONS = {1: "M", 2: "D", 3: "R", 4: "A", 5: "O", 6: "T"}

    SCREEN_NAMES = {1: 'task_1', 2: 'task_2', 3: 'task_3',
                    4: 'task_4', 5: 'task_5', 6: 'task_6'}

    def __init__(self, ui_screen):
        self.ui = ui_screen
        self.selected_task_id = None
        self.tasks = [
            {'id': 1, 'name': 'Muntii', 'unlocked': True, 'color': (0.25, 0.55, 0.35, 1)},
            {'id': 2, 'name': 'Dealuri si\nPodisuri', 'unlocked': False, 'color': (0.60, 0.85, 0.55, 1)},
            {'id': 3, 'name': 'Rauri\nsi Vai', 'unlocked': False, 'color': (0.55, 0.90, 0.55, 1)},
            {'id': 4, 'name': 'Agricultura', 'unlocked': False, 'color': (0.65, 0.85, 0.50, 1)},
            {'id': 5, 'name': 'Orase si\nMonumente', 'unlocked': False, 'color': (0.85, 0.65, 0.45, 1)},
            {'id': 6, 'name': 'Cultura si\nTraditii', 'unlocked': False, 'color': (0.75, 0.55, 0.75, 1)},
        ]

    def select_task(self, task_id):
        self.selected_task_id = task_id

    def start_task(self, task_number):
        self.ui.start_task(task_number)

    def get_screen_name(self, task_id):
        return self.SCREEN_NAMES.get(task_id)

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


