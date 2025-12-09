from backend.service.PlayerService import PlayerService
from backend.service.QuizzService import QuizzService
from backend.service.QuestionService import QuestionService
from backend.service.FillInStatementService import FillInStatementService
from backend.service.MinigameService import MinigameService


class GameService:
    def __init__(self,
                 player_service: PlayerService,
                 quizz_service: QuizzService,
                 question_service: QuestionService,
                 fill_in_statement_service: FillInStatementService,
                 minigame_service: MinigameService):
        self._player_service = player_service
        self._quizz_service = quizz_service
        self._question_service = question_service
        self._fill_in_statement_service = fill_in_statement_service
        self._minigame_service = minigame_service
        self._player = None
        self._regions = [
            {"id": 1, "name": "Region 1", "unlocked": True},
            {"id": 2, "name": "Region 2", "unlocked": False},
            {"id": 3, "name": "Region 3", "unlocked": False},
            {"id": 4, "name": "Region 4", "unlocked": False},
            {"id": 5, "name": "Region 5", "unlocked": False},
        ]
        self._tasks = {
            1: [
                {"id": 1, "name": "Task 1.1", "unlocked": True},
                {"id": 2, "name": "Task 1.2", "unlocked": False},
                {"id": 3, "name": "Task 1.3", "unlocked": False},
                {"id": 4, "name": "Task 1.4", "unlocked": False},
                {"id": 5, "name": "Task 1.5", "unlocked": False},
                {"id": 6, "name": "Task 1.6", "unlocked": False},
            ],
            # Add tasks for other regions here
        }

    def set_player(self, player_id: int):
        self._player = self._player_service.get_player(player_id)

    def get_regions(self):
        return self._regions

    def get_tasks(self, region_id: int):
        return self._tasks.get(region_id, [])

    def complete_task(self, region_id: int, task_id: int):
        tasks = self._tasks.get(region_id)
        if not tasks:
            return

        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                task["unlocked"] = False
                if i + 1 < len(tasks):
                    tasks[i + 1]["unlocked"] = True
                break

        # Unlock next region if all tasks in the current region are completed
        if all(not task["unlocked"] for task in tasks):
            for i, region in enumerate(self._regions):
                if region["id"] == region_id and i + 1 < len(self._regions):
                    self._regions[i + 1]["unlocked"] = True
                    break
